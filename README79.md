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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0dc1464b-da4d-3703-8663-8fde8de944ff | -14.78426 | -59.72403 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1310d042-d76d-3b00-a932-e513a3f06747 | -15.08514 | -48.51627 | 2025-08-28 05:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5e49595-d6cf-3742-84c5-20f9df6f1495 | -14.33431 | -53.34471 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 356a277a-a755-3089-99b9-a8bc681de300 | -14.34956 | -53.3502 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e61b3c2c-5984-37a6-8c35-215fc73c4588 | -15.67249 | -52.74524 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec5fd316-dd58-3344-9b69-d10c1d8b6c22 | -14.32958 | -51.91261 | 2025-08-28 05:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee880894-7fbc-3b59-ad74-62c2218c002e | -15.67331 | -52.73809 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ca93487-7d54-35dc-b212-0e2fc1b14431 | -14.29112 | -53.05225 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 819df5ae-d99d-3a89-a977-0c9fbd55e6d7 | -15.63214 | -52.755 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1c51c8c-9b8a-3d91-bd77-995dac223c3f | -15.17942 | -52.33412 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce3faae7-93dc-3961-874a-bfcbd767f90b | -14.26695 | -53.07312 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d15b1699-6df6-3644-b92b-9df61fad86f1 | -14.34435 | -53.34937 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a1973655-7f41-3254-ac94-0d250b51b3b4 | -14.35019 | -53.3487 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d23ddd9d-d47e-3cb8-b312-d59f929f6565 | -14.34945 | -53.35509 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8a7a5b0-15a5-36a3-8942-2fb68cb5e65c | -14.43811 | -53.19103 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5eb40eec-6d20-38b8-b131-f2ade8ce5757 | -14.31792 | -60.37243 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cd6edea-9cb6-3600-b852-cda301cb5a78 | -15.60918 | -52.72014 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8335c0a-f123-318a-b976-4eb83a7ad1f0 | -12.22287 | -64.22791 | 2025-08-28 05:27:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74746e26-9d65-33e1-b7d3-1b90ad2ecdf0 | -14.33914 | -53.34864 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4c91c18b-b048-3da2-a330-9c9279ea811d | -14.34474 | -53.34617 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3cc94799-f7b7-3035-95db-c69b5bdf0a4c | -14.27885 | -53.0641 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fee21b69-cd9a-304e-9f41-daeb65bfd4b1 | -14.26779 | -53.06629 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3973a235-37b9-3bdb-af0e-c2d7b71d12af | -14.36153 | -52.08967 | 2025-08-28 05:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 11c13635-44c1-336d-891b-8330896177d1 | -14.29724 | -53.04641 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 10f3f34e-9922-399e-8604-3a0829618a6e | -14.3672 | -52.09039 | 2025-08-28 05:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fe98dd7c-cfe8-3fb3-98c0-b838ea736906 | -14.52683 | -53.10711 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff19ceea-2f7b-39d3-83ba-39d5f7d37f17 | -15.63175 | -52.7585 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89832ae8-18ae-3045-a02a-aa1ec50426c9 | -14.33953 | -53.34542 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| af6a92a6-e55c-343e-b4aa-47e81a037266 | -14.44299 | -53.19505 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1066a535-526d-354c-a67f-60421c29b375 | -14.34995 | -53.34701 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ef1cc650-8359-32d5-8468-c1961bcdafd4 | -15.6729 | -52.7417 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 107d3bd9-2619-3f70-af84-af2ec024dc67 | -14.7646 | -55.94852 | 2025-08-28 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d5ca1f7-bba3-3316-aec5-4beedac72395 | -14.27352 | -53.06351 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21af3d0a-be25-320c-a7a4-c9cbe6569671 | -15.63254 | -52.75143 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 195089c7-360a-3b23-8d46-a3df82a410a9 | -14.26655 | -53.07646 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 376888a4-16c4-32f2-b5e3-1725e73c1cfc | -15.6215 | -52.74998 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ba476ee-e752-36e6-b9f2-4c57485a3350 | -14.36107 | -52.09357 | 2025-08-28 05:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fba3b2ac-d497-3573-9f69-2256d82e5705 | -14.2731 | -53.06699 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a89c9e1b-6a50-3dec-9d20-f62f18bb713b | -14.34877 | -53.35656 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4294003e-1ae8-394d-a942-1b4bf522bb9a | -14.27843 | -53.06758 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bf107ab-25fc-31cf-9dcb-24a20af9518a | -14.29153 | -53.04892 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5b70677b-85b0-3bde-850e-1cc01c63da80 | -14.29002 | -53.0411 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5d38d3cd-48c2-3d0b-b0e8-5370e5d6ccd9 | -14.33992 | -53.34222 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5f6d8992-9d15-38aa-a42e-ef96dcd2baf7 | -14.35475 | -53.35109 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49c4c0b3-e7a7-3a7c-918f-84b2475089a2 | -15.66822 | -52.73355 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 413c7d96-f246-3aa4-b988-782ba8518c9a | -15.60734 | -52.72586 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5d4ef5d-3f52-3c3b-9d9f-e67d401e1aa6 | -14.34916 | -53.35339 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 998e9ab1-dc3c-35c0-94e6-e09d7e41cba6 | -15.09246 | -48.51479 | 2025-08-28 05:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e6ccfd1-45fa-359c-8f03-8b7d5f9460aa | -15.66696 | -52.74458 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93949cf5-5fc8-357e-88ef-5316bb7cb961 | -14.29493 | -53.0454 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5c674e65-4a4b-32ae-aae1-f8f1f71bdd15 | -14.76778 | -59.73781 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a77db1e6-869d-3610-81b7-96fc2fd93d23 | -14.29454 | -53.04879 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 74f22338-42f1-3954-98f0-717a048c7bb2 | -15.67888 | -52.73849 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a8bc3bc-5e9a-3468-8b24-4a9d158a46f3 | -14.31849 | -60.36862 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a17971c9-e925-3286-b31d-08eea8769073 | -15.61326 | -52.72313 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 229ce9ef-a7cc-36e4-8775-3e56d13df93e | -14.27627 | -53.06667 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 417ad222-496b-3f8d-8288-300d405a3a0f | -15.60813 | -52.71875 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b241f38-f02b-3e56-9540-b4e9ab2e1b76 | -15.18507 | -52.33482 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dde1ca5e-3f51-3853-951b-cad73ed00705 | -14.77953 | -59.70708 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c03594e-c4bb-3200-b1b1-24b06671d158 | -14.4434 | -53.19167 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 098b2d25-af6e-3639-85fd-e79ab0407659 | -17.77698 | -48.50502 | 2025-08-28 05:27:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 274077e2-71cc-3056-a365-0a4199039efb | -14.78482 | -59.7202 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df3960a9-adfa-39ab-b8a3-a7ce6f80d208 | -22.53506 | -50.44326 | 2025-08-28 05:29:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9406fa3d-3e6f-3c4d-b412-231b204982cf | -22.5285 | -50.43776 | 2025-08-28 05:29:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cdda2b13-4331-34bb-b5c5-243c0b8f6588 | -22.53538 | -50.43808 | 2025-08-28 05:29:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 478a6c5a-1fbc-36bc-aa84-088267c5d1da | -22.5282 | -50.4428 | 2025-08-28 05:29:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5b0a70e8-ef0a-3608-80ab-7c194bbfc7fe | -22.53582 | -50.43172 | 2025-08-28 05:29:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9a41d577-63c7-3570-9162-2dbefb48b61f | -22.53555 | -50.4368 | 2025-08-28 05:29:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5d662ba8-1b06-3d41-8924-e12198610a2d | -22.52867 | -50.43652 | 2025-08-28 05:29:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2e99d80e-cc91-3cbb-b51d-6e76016c0865 | -9.1339 | -65.788 | 2025-08-28 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 204.0 |
| 90310fba-3c23-30cb-a965-f90bf6e99878 | -10.7862 | -60.7655 | 2025-08-28 05:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ee0eff84-af22-376c-b777-8c6cdd406d8d | -9.1338 | -65.8067 | 2025-08-28 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 428718e7-c0ce-3eda-a430-d290cdf33558 | -9.1153 | -65.8073 | 2025-08-28 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| aa62a948-1f9c-3618-b512-a3118791dc94 | -8.2893 | -45.1586 | 2025-08-28 05:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| fb54d316-aee8-32d3-8078-258756b10b09 | -9.134 | -65.7694 | 2025-08-28 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| f4fc6c99-1073-3091-be86-85206ffe0076 | -9.1155 | -65.7699 | 2025-08-28 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 116.6 |
| a5e1bc74-bdbc-3c24-83c5-ffbfad2572de | -10.4738 | -57.9366 | 2025-08-28 05:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 9b8a06d8-1839-34fe-b557-abbb35c26a78 | -6.4355 | -44.5764 | 2025-08-28 05:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 5675aae4-02d8-3f58-ac2e-c4fdd1775aa4 | -10.4736 | -57.9563 | 2025-08-28 05:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 228d4b2c-763a-30fc-9cc0-db49e2272db7 | -10.8049 | -60.7644 | 2025-08-28 05:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 771c0725-9aa8-395d-9195-5bc525668c67 | -12.8032 | -48.1516 | 2025-08-28 05:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| d9a51a41-1ea3-3410-9c90-887e1d2b89c4 | -6.8772 | -43.6152 | 2025-08-28 05:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 521a077b-aaed-30dd-abc3-ace290163b82 | -9.1154 | -65.7886 | 2025-08-28 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 261.4 |
| 2aa3210d-e93e-39d6-9b02-9aa79d2fd4f7 | -10.8047 | -60.7837 | 2025-08-28 05:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 34d4b9e7-01e4-3553-953a-5e6e408f13eb | -8.289 | -45.1814 | 2025-08-28 05:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 423198ae-00f4-3d3e-989f-8c40dae9b75e | -8.289 | -45.1814 | 2025-08-28 05:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 93e78532-3bb6-3083-9e0d-2cae00cfdf4a | -9.1338 | -65.8067 | 2025-08-28 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 67fbdc47-e80b-3a7d-9fe2-0f765c55ed83 | -9.1154 | -65.7886 | 2025-08-28 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 239.9 |
| ed45eee1-8998-3e8b-947d-39d8bc836ba1 | -9.134 | -65.7694 | 2025-08-28 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 223375af-80e2-3848-89fd-2eadc01cd1d1 | -9.1155 | -65.7699 | 2025-08-28 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| f4ea9cd2-f3e2-39ce-bb27-efdb01aa3606 | -13.9744 | -46.3521 | 2025-08-28 05:40:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 45a26f78-bf8d-31de-a71c-9abec703ab09 | -6.896 | -43.6135 | 2025-08-28 05:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 212352d4-ee19-3218-80d0-a25641059d7d | -9.1339 | -65.788 | 2025-08-28 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 220.6 |
| c7ac55dd-1e1d-372f-af4b-e0a52f0fc574 | -6.8772 | -43.6152 | 2025-08-28 05:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 09ff1f4a-e7f1-3731-a975-88b203b71b4d | -10.8049 | -60.7644 | 2025-08-28 05:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| a37481c1-10aa-3b85-82e1-8380b97ec4df | -10.8047 | -60.7837 | 2025-08-28 05:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 4dc725ad-7c1a-38a9-a87f-37e341c08c5d | -9.1153 | -65.8073 | 2025-08-28 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 8818c3da-909b-3671-bd07-741e785c93b0 | -8.2893 | -45.1586 | 2025-08-28 05:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| d94f9ac5-08c8-3d2d-85d3-b031faf99733 | -10.4738 | -57.9366 | 2025-08-28 05:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 2e08e3b4-224c-3bc7-b843-6733dba9defd | -10.4736 | -57.9563 | 2025-08-28 05:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |


[Clique aqui para ver as próximas entradas](README80.md)
