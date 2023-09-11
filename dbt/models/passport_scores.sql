with source as (
    select * from {{ source('public', 'raw_passport_scores') }}
),

renamed as (
    select
        address,
        score,
        status,
        last_score_timestamp,
        json_extract_string(evidence, '$.type') as evidence_type,
        json_extract_string(evidence, '$.success') as evidence_success,
        json_extract_string(evidence, '$.rawScore') as evidence_raw_score,
        json_extract_string(evidence, '$.threshold') as evidence_threshold,
    from source
)

select * from renamed
