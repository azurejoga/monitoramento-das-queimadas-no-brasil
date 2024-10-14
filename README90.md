# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84c83e62-b3ac-32cf-a3e7-4afbdc1c7432 | -9.43511 | -53.2015 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd2b2be5-9f00-336b-ac9c-265b8b39823b | -9.43292 | -53.19349 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c1207b4-f334-32c9-a4da-4383aece8caf | -9.43232 | -53.19717 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e996e2f-a845-3b24-b547-642d6f2a5096 | -9.43172 | -53.20091 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bee6f7e2-c434-3e7e-a173-f08784f44cf3 | -9.43012 | -53.18928 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 34118c5e-ded3-33d0-b908-5c83701bea80 | -9.42952 | -53.19292 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc0a08af-0b62-3a25-abf7-66af95e401df | -9.41452 | -53.22067 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 371dc59e-4979-3bb3-a6cc-cb53629663af | -9.41111 | -53.22012 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 280b5b4f-a14e-3559-9a2b-a461ae2c8856 | -11.56458 | -53.85997 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 591f9ba6-6b1a-368a-ba4c-50c6f6bdd469 | -11.56398 | -53.86373 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cf27a35-786a-3b08-aa4c-e830192ebf7a | -11.56177 | -53.85565 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef2de7b6-7726-35b7-a4cd-d0fa0930348e | -11.56117 | -53.85941 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfe83794-c704-3379-bdaf-2cc864f75051 | -11.56056 | -53.86316 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 746eaf63-ba25-3b66-8c59-c4890a26f3e6 | -11.55896 | -53.85135 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c674d77-f87d-3447-bc10-32d657c55655 | -11.55836 | -53.85508 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd413ba6-da2b-3665-828f-5247179fc238 | -11.55775 | -53.85883 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ead2dc3b-2b7b-3451-8da7-495f1604ee7c | -11.55714 | -53.86258 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2f28c6d-1d55-3e2f-b189-3660403a9833 | -11.55653 | -53.86635 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 027a02da-ae07-3302-ae86-6d5cb6222e11 | -11.55554 | -53.85078 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a74b24ff-9160-375d-819b-a0c48d5d2cfe | -11.55494 | -53.85451 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0545e945-cf72-3d11-be24-a17a4fce1ca2 | -11.55372 | -53.86201 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b840a54a-93ca-3be7-b815-5bc58e7bdce9 | -11.55311 | -53.86577 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1c28eae-35b5-3f2a-a4cd-9c9e29dae996 | -11.55273 | -53.84648 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e456e08-e094-3cd0-a450-2565b7f10dfd | -11.55212 | -53.8502 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed78d2ae-81a6-360a-9406-d46e6b7e8264 | -11.54969 | -53.8652 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 927c924c-9e78-368f-8ce1-f7dffe629436 | -11.54931 | -53.8459 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ccd1403-aa93-3490-b111-8810c54352d8 | -11.54871 | -53.84963 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9797a94f-1b87-37ad-8eda-5a01c1e3e54d | -11.5459 | -53.84533 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2eaf1519-edd8-3936-91de-18df31bb4ef9 | -11.54566 | -53.86839 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37675266-c591-3ace-95a2-173cfe20b0d8 | -11.54308 | -53.84103 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3f50cff-a90f-3eaa-af60-86d7e7a104e3 | -11.53967 | -53.84046 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aaa52f31-fc98-3d39-8033-94f964d466a0 | -11.53625 | -53.83989 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7a484fc-77c9-3afd-8d03-2b0a5de77d8f | -11.5282 | -53.8462 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e356ea07-7868-3858-80ff-52e859c9720a | -11.52478 | -53.84563 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bd4e86a-0104-3713-b29d-b0b2c2d15e8f | -11.52453 | -53.86867 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86939309-9532-3126-b8db-d5e6644ad65f | -11.52417 | -53.84936 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acf492fe-05bb-3bd6-9195-3e145d658d16 | -11.5211 | -53.86811 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11caffe4-5d52-39a5-8ccb-bea6cbc1bbdb | -13.01978 | -53.48011 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71186586-5a1d-356a-a06e-e64f911a71c5 | -12.88873 | -53.5368 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fad654ac-b8f2-3fde-be6b-4dcb9a01a1f9 | -12.88814 | -53.54044 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 633a56fc-763e-3491-a23e-ddb7e1164755 | -12.88755 | -53.54408 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bce25fd-a83a-3857-8d5b-18cc1ecfb204 | -12.88654 | -53.52897 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fa4d8a5-40f8-3a20-acad-022cfe729e50 | -12.88595 | -53.5326 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfa7c15c-4877-32d6-8aa7-9f053a45d15e | -12.88536 | -53.53624 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1aabbc0e-8410-369a-81e2-f45a1fa584e4 | -12.88478 | -53.53987 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c751ad3-6279-3d3a-844c-a568271a3fcc | -12.88419 | -53.54351 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f6f55ef-6d89-3e47-b841-30d5fa041f25 | -12.88317 | -53.52841 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b42521c-6c6d-3400-b1a5-6b876fe6062d | -12.88259 | -53.53204 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f18aa52-d254-3344-80da-a9a02728a8b1 | -12.882 | -53.53568 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9855f541-f1fd-3920-ac3d-2041189bc45e | -12.88141 | -53.53931 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bc10276-bd29-368f-bf5e-4911e265d96e | -12.88083 | -53.54295 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a1fe961-f8ed-3fb9-9957-c4b7f75c39bf | -12.8804 | -53.52422 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ff94307-ff6e-3a62-a535-7acc20a0fa22 | -12.87981 | -53.52785 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc2f90d3-80db-3c74-9103-bbd5912a42c4 | -12.87922 | -53.53148 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95328d3f-f3c5-35a5-af22-f7f48ae28ead | -12.87864 | -53.53511 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc6df5b1-6624-38fd-b9c4-31b20cf40074 | -12.87805 | -53.53875 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ca4a3bd-e234-3b6f-a972-97a73beffa7d | -12.87762 | -53.52003 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e0973eb-23f3-3777-be68-955dfe388f14 | -12.87746 | -53.54239 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 899e891d-6a2b-376f-a157-d103623c363e | -12.87703 | -53.52366 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8abd88f7-3487-3b52-b2df-2050cb220dc3 | -12.87645 | -53.52729 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50960fe4-b048-3a05-8a11-7d32009f9486 | -12.87586 | -53.53092 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0c60a02-0c5c-324a-b78f-b4174d80736a | -12.87527 | -53.53456 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2675657f-242e-3d3c-8a82-9a5182edfd9e | -12.87485 | -53.51585 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 592b3cff-df84-3895-a5ba-7b170254b9ad | -12.87469 | -53.53819 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f7641e1-1db5-30c3-b837-41b33d8165f3 | -12.87426 | -53.51948 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ed620b5-d439-37aa-98cb-5833a02f1ca1 | -12.8741 | -53.54182 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb9af827-4ddf-3cbd-b56e-aaf06fcca659 | -12.87367 | -53.52311 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9a4c7d7-c406-33b3-b5ee-7a7a70a1fb04 | -12.87308 | -53.52673 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91ddc1b1-67ea-36ee-9d0e-984564486498 | -12.8725 | -53.53036 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f7cd1d1-e0f1-3dc9-879f-19fe66eacf41 | -12.87191 | -53.534 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e70c0173-4f14-38cf-b534-aab4e46cc436 | -12.87132 | -53.53763 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99db1110-487d-3f3b-a6c8-6ae70452956c | -12.5867 | -53.07331 | 2024-10-14 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4693d208-bca4-3056-a1c5-ff76d3cdf146 | -9.274 | -54.58247 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89b6f4de-89b3-3f4c-8153-41c5e2e1d681 | -9.01001 | -54.51122 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b136fca-2470-31d5-833f-009ce4b5fc5c | -9.00932 | -54.51534 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8863a235-367a-33b0-94eb-d5fa174d5219 | -9.00864 | -54.51947 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 490bb142-7e3c-3699-9b1e-f51c6fad3330 | -9.0071 | -54.50652 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d85c65e-9e98-31a2-a5c6-42784390a762 | -9.00641 | -54.51063 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5fdc4c4-09f1-3786-ad90-f9da3a273451 | -8.98746 | -54.57985 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a617033-3e52-3065-bb9d-6fa8271e1184 | -8.98677 | -54.584 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e04219d-53d3-35d5-9979-9a196d1b3769 | -8.90205 | -54.57474 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 500e9a29-2174-3e59-9748-2e565dc61039 | -8.89844 | -54.57411 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a42353cf-b835-37a6-8936-c9bf13ff811d | -10.71438 | -54.11889 | 2024-10-14 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb8b5518-9f49-3db4-a33a-6cc77ec71882 | -10.62562 | -54.61139 | 2024-10-14 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26deaeca-8379-352f-93e7-7ee9a2d1aae8 | -10.62207 | -54.61084 | 2024-10-14 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6df13f6-d888-3a86-8cd6-969ae376fd96 | -10.28937 | -54.99149 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 03ca9750-085c-3364-bb75-9b4d1904481e | -10.03853 | -54.34068 | 2024-10-14 04:46:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aa0b4f78-6499-3c4f-994e-21238f070172 | -10.03501 | -54.34007 | 2024-10-14 04:46:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 21630a53-ead7-3cb0-ab02-743e9dc0caee | -12.20861 | -54.25607 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ec4c42f2-e809-34b5-97c5-ae05a1c6201e | -11.63407 | -54.9945 | 2024-10-14 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f8c32ec-16d2-387e-94ea-07977d9076a4 | -11.6305 | -54.99387 | 2024-10-14 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82523189-4a8e-38c9-98e4-8692914498a7 | -11.62982 | -54.99796 | 2024-10-14 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b1941dd-44c1-37c3-b209-653baa6bc556 | -11.62625 | -54.99734 | 2024-10-14 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42921083-583b-3d88-a2d5-ad5e42dea9da | -11.41199 | -55.06961 | 2024-10-14 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e030b952-e108-31e0-8bdf-51ed6b86a12a | -11.39902 | -55.05888 | 2024-10-14 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75776d3f-7214-33fb-9e93-67e5271f9d1e | -11.39543 | -55.05827 | 2024-10-14 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ac0f765-972f-3d61-ad4f-93f1320fb99b | -11.35904 | -55.20709 | 2024-10-14 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01dc797a-8113-3557-b635-8f7ffedaec86 | -11.35542 | -55.20647 | 2024-10-14 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1b52bdb-00d7-3020-aa7f-f352bc8d11d4 | -11.27603 | -54.5877 | 2024-10-14 04:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c2ca2f3-0fd1-3e03-8fef-2351018e935c | -11.19976 | -53.97411 | 2024-10-14 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README91.md)
