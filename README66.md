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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d04f27c6-9cc9-34ae-a88e-a63906c06459 | -9.31614 | -50.81295 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 60bb47b8-b7dc-3b03-b31e-68683c04093e | -9.31557 | -50.81606 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d7fd7e6b-7f38-374f-82c9-ca95180c269e | -9.31546 | -50.78787 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67dfbd25-9e7a-3aae-b1a0-a14ced6442f9 | -9.31492 | -50.79084 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4f91882d-295b-362a-869b-70dfc11a9330 | -9.31438 | -50.79379 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 20f56b0c-0ff5-37ff-8eaa-d4ab720a9305 | -9.31386 | -50.79665 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f631814e-dd29-301c-abf0-212477454dbc | -9.31335 | -50.79943 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c18e1e30-d933-3003-8433-0c1f49a86bb2 | -9.31284 | -50.80221 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5b9e219-00c5-33de-b168-75614f93ad3a | -9.31229 | -50.80523 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 009839cd-90c3-3438-b976-dc6f78997a02 | -9.31168 | -50.80857 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c900dfb5-55fa-3a7b-90f2-fc59fc180774 | -9.31106 | -50.81194 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 59a0e9b7-6b39-3a48-94e7-5748b93ec277 | -9.31048 | -50.81509 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d38864f2-b22a-3493-8be1-60caf020b5ce | -9.30983 | -50.78992 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70238742-1096-3beb-a3bd-69cfa13a8f4e | -9.30769 | -50.80159 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a59e405-72b7-3a50-a53f-d1926a8fd7fe | -9.30714 | -50.80458 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e4e9d43-a088-3af7-b2ec-392e59a1349a | -9.30656 | -50.80778 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e855996-4089-3197-a218-6e3949f0b4f6 | -9.30596 | -50.81102 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff1eada1-fcf4-3fe3-a467-50c460ebf64a | -9.30539 | -50.81412 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1e10848-bf39-3d5f-a8d3-9576c63ed567 | -2.86356 | -50.72285 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0677a7a5-c9c0-3acf-84ab-f79a925a124e | -8.91556 | -41.14033 | 2024-10-04 04:08:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.1 |
| dc78a5a0-ea0d-359c-9829-dfa095f53b3c | -6.83635 | -42.82719 | 2024-10-04 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 002c0e53-9223-3553-a2a5-0c86045bc4e3 | -6.83357 | -42.82313 | 2024-10-04 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d48ce621-19e8-3519-afc0-7b3a16652c07 | -6.83023 | -42.8226 | 2024-10-04 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f380ab39-a3a1-323a-84db-bcd0034b0c45 | -5.4976 | -35.56647 | 2024-10-04 04:08:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3f8119c7-f939-3974-96b6-d6f36dab24d5 | -5.46078 | -35.55313 | 2024-10-04 04:08:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3c705b8e-354b-3e27-b088-c4f24afadfbe | -6.8875 | -35.4925 | 2024-10-04 04:08:00 | NOAA-21 | GUARABIRA | PARAÍBA | Brasil | 2506301 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ba606587-2caa-3a7d-b46e-b9c75dd19b0e | -7.33471 | -35.19215 | 2024-10-04 04:08:00 | NOAA-21 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 975130e2-9786-3351-9720-e6e7014083b3 | -5.38349 | -36.81894 | 2024-10-04 04:08:00 | NOAA-21 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fd64b8c4-2b57-3a6e-93d6-e6e891892cd0 | -6.66921 | -37.39614 | 2024-10-04 04:08:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 56753c4d-c587-38b3-832a-8f5a0530c5be | -4.86627 | -38.43363 | 2024-10-04 04:08:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a06d425f-ad68-3a51-ae06-07a5d0a79fb0 | -4.72161 | -38.45703 | 2024-10-04 04:08:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ba168ba8-6a56-3f0e-b033-195a2129f016 | -4.72101 | -38.46095 | 2024-10-04 04:08:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3c1b6f8a-79ea-348c-b852-fdd700afd13c | -5.17785 | -37.99899 | 2024-10-04 04:08:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5d0c1257-a0d2-3c59-ba16-1b4212205866 | -5.16762 | -38.14132 | 2024-10-04 04:08:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3e373f5a-4469-324f-b9fe-3be6ba58c4c0 | -7.30535 | -38.13789 | 2024-10-04 04:08:00 | NOAA-21 | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ff20b2cf-5c50-3b3a-8361-d03df4773fa0 | -7.30469 | -38.14225 | 2024-10-04 04:08:00 | NOAA-21 | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 150f2b1c-48a2-30fe-b62c-c94d97d37fe0 | -6.86294 | -39.61436 | 2024-10-04 04:08:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c1615ff1-a3ba-3357-a10e-9b4f32e77813 | -6.86237 | -39.61806 | 2024-10-04 04:08:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fc213e32-5fc1-301f-aa3c-ac21dbb436a7 | -6.8618 | -39.62177 | 2024-10-04 04:08:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 581c75ae-b972-3d3b-aefd-35c1222eed05 | -8.38513 | -40.30282 | 2024-10-04 04:08:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4d7bdd97-735c-3292-88f7-f9e0a52aefcc | -8.38456 | -40.30648 | 2024-10-04 04:08:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| df37f2c8-4f50-385b-9186-62b2c74e31db | -9.15682 | -43.15728 | 2024-10-04 04:08:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d730d39e-93c2-3671-9b69-41dc028720b4 | -9.15625 | -43.16084 | 2024-10-04 04:08:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6a33ee4d-6c93-322a-9942-7d993defe6ca | -9.15292 | -43.1603 | 2024-10-04 04:08:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7c71e40d-0688-3120-8adb-80122fe485e8 | -4.68728 | -40.6804 | 2024-10-04 04:08:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d40a6760-ef85-374a-bea7-d43f78a445d9 | -5.16549 | -41.29801 | 2024-10-04 04:08:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1c1fb20c-d813-3596-9cfc-c10a0842ef6d | -5.16495 | -41.30145 | 2024-10-04 04:08:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dfbbd148-c467-3953-bbc4-4992c76a868e | -7.35001 | -41.9496 | 2024-10-04 04:08:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1d2799bb-c59f-33c6-9fe9-3f7db35d7f39 | -7.34671 | -41.94908 | 2024-10-04 04:08:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 30c1a7dc-b89a-3f23-9c5c-68aaffbca760 | -7.34617 | -41.95254 | 2024-10-04 04:08:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e8407125-fb8d-3766-bfef-056c390e3956 | -6.89794 | -41.77497 | 2024-10-04 04:08:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 15f59a9a-cb49-3c8c-a7df-7fefe5678336 | -6.84459 | -41.80893 | 2024-10-04 04:08:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0c1b80f5-570f-3c5d-bf9b-9a5884154708 | -6.52136 | -41.94135 | 2024-10-04 04:08:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a7f0011c-b4b6-367b-aa79-da27d97df149 | -6.52082 | -41.9448 | 2024-10-04 04:08:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 48eb0698-703d-3968-b3d2-528e2efc677b | -6.52027 | -41.94826 | 2024-10-04 04:08:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 10ccdafc-bd18-3e6b-8440-711ff2455482 | -6.51685 | -41.94419 | 2024-10-04 04:08:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c6f9cd9f-714e-3049-9398-cc2a6f15a5a9 | -6.51409 | -41.94023 | 2024-10-04 04:08:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 078781d5-f9f4-3c9d-ac0c-b80e35102bb2 | -6.51354 | -41.94368 | 2024-10-04 04:08:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cd0697cf-dd93-3cac-aece-b6a5bf63dad8 | -6.49575 | -41.38562 | 2024-10-04 04:08:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0f602184-8b1f-332b-8ad1-1f82b996aa43 | -8.43392 | -41.93857 | 2024-10-04 04:08:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 97e871bc-e8b3-39c2-8155-41ce68e79503 | -8.43338 | -41.94203 | 2024-10-04 04:08:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f50998e8-4d27-38f7-870e-bd49473db813 | -8.42953 | -41.94497 | 2024-10-04 04:08:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 43ad0070-d809-32fd-ab1e-729da681e6fe | -8.42569 | -41.94791 | 2024-10-04 04:08:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 25edcae2-67c8-3697-aac7-e4f7b9c8457f | -10.23484 | -42.38839 | 2024-10-04 04:08:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ba750577-30a0-35ec-a687-cf1495e5a18a | -10.2343 | -42.39188 | 2024-10-04 04:08:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9410414f-447c-350a-8180-ad6481ef06fb | -10.13302 | -42.42927 | 2024-10-04 04:08:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 448378ad-0e76-30f1-a6d5-74e815a5c140 | -10.12972 | -42.42874 | 2024-10-04 04:08:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2a1ecfe3-0111-34ee-800b-cc435dedfc03 | -11.04456 | -42.01746 | 2024-10-04 04:08:00 | NOAA-21 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5522edeb-cfbf-3466-a9f0-45997cccf18b | -11.04402 | -42.02097 | 2024-10-04 04:08:00 | NOAA-21 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 31dc9675-0dfe-313c-925f-ab2000764db9 | -3.3787 | -42.29075 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 5bcc2aac-0553-3ccd-b2f3-26c21b2d0b94 | -3.37813 | -42.29433 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 85.2 |
| 33016ff1-b2bd-3318-a511-c0510bca88a7 | -3.37533 | -42.29022 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 825d0828-ac4e-3a8d-9d15-bbd522ccb0e6 | -3.3742 | -42.29738 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 85.2 |
| 479ead72-df34-3ae2-b033-742367bbdc39 | -3.37253 | -42.28611 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 30ae9c52-8bd4-3d68-ba62-8f711d67c3d9 | -3.3714 | -42.29327 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 31.2 |
| dda14144-cec8-3664-b966-48ea5fa78af2 | -3.36917 | -42.28559 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 16b09c2e-4b3d-3961-bf89-50ad3ee5a65b | -3.3686 | -42.28917 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 95.3 |
| ddfd20fc-6b70-3045-a74e-9019b0ccbc58 | -3.36804 | -42.29276 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 31.2 |
| 6e74939a-1cb4-3502-a48c-34d4e897f462 | -3.36524 | -42.28866 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9f41da93-1fdf-35ff-8853-d57a74d4f30a | -3.36467 | -42.29224 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ed5cb814-15e2-34da-86c0-fc52b07723ae | -3.36187 | -42.28814 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 04122472-f224-3db7-999c-4d1beba4e13c | -3.41066 | -42.28479 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1c482f70-a645-3b59-aa60-320e2b844273 | -3.4073 | -42.28426 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| df940180-6992-39dd-865a-d26d5dde99bf | -3.40674 | -42.28784 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0ab7a4d3-ce04-3d94-abe1-4f6d9178adc1 | -3.40394 | -42.28372 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 47baf695-dac8-3ca8-b569-40447c3e51dc | -3.40337 | -42.28731 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0be7e281-854a-3074-a761-ec5a47451070 | -3.3759 | -42.28664 | 2024-10-04 04:08:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f68c8b37-d79a-344e-8614-135352420ba1 | -4.40993 | -42.1404 | 2024-10-04 04:08:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 62651a64-52b5-338e-a3c2-52a540fa07fc | -4.88601 | -43.19672 | 2024-10-04 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 738960f4-ae04-342a-8696-34807dfa5ba0 | -4.8184 | -42.7609 | 2024-10-04 04:08:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6379ff11-e3fc-374b-a5fb-f1572bf20aec | -4.81782 | -42.76452 | 2024-10-04 04:08:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a28e7e14-1dbd-3811-b867-6c175bbc5f9b | -4.81444 | -42.764 | 2024-10-04 04:08:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 55fc7bb6-6542-316d-8f85-9760282d76b7 | -4.81387 | -42.76761 | 2024-10-04 04:08:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 964149e0-7075-381d-af4a-5bda0a58ed2c | -4.81048 | -42.76709 | 2024-10-04 04:08:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9a128303-d918-3d9f-8903-058e5b2f4254 | -4.80991 | -42.77071 | 2024-10-04 04:08:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c06e95f1-2390-3254-b7da-c495346f2e17 | -4.71543 | -42.78928 | 2024-10-04 04:08:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0004a3db-ee7b-38c3-95a5-d96325a0c7bf | -4.46503 | -42.88475 | 2024-10-04 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49b20bc8-82a5-36cc-b8a8-a1ecb3f023a6 | -4.46104 | -42.88789 | 2024-10-04 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2d0b0d3-8fcf-3f22-9140-0138bf188026 | -4.45764 | -42.88736 | 2024-10-04 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bffb0f3a-363f-33da-8c9f-957d5d39425d | -4.45706 | -42.89102 | 2024-10-04 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README67.md)
