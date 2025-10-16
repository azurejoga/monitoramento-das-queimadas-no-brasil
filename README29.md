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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8390877-49e9-31d8-8692-6f02945c864e | -10.72042 | -47.58804 | 2025-10-16 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84f5d3ae-c130-3b49-be2a-795a0fdcfa3a | -11.74182 | -44.23085 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5170b22-6519-35b1-9d13-edfc303f597c | -10.13493 | -44.54563 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7f1b519-667a-35b8-aca4-839a67467317 | -4.66952 | -44.10806 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e2d911f-dea8-3d22-a99b-f92684df65cf | -9.58967 | -43.07193 | 2025-10-16 03:47:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 732c1e78-5161-3ce4-951c-80284e462e4d | -11.47836 | -47.63997 | 2025-10-16 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1988c317-2989-3789-b92a-5824872acc28 | -6.33229 | -44.31935 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 012fe3eb-4654-3336-b501-c34386307569 | -11.4504 | -44.01549 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 081ecfc4-d74d-360f-99eb-cd36dc1138d2 | -10.52244 | -43.37634 | 2025-10-16 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9c1663f-9503-38fd-83cc-49dd324659ef | -11.54818 | -49.92574 | 2025-10-16 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19bacad5-12aa-36f7-bcb2-78400642e446 | -10.27287 | -47.89212 | 2025-10-16 03:47:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16ba20e9-61f3-393d-9848-0652b53303bd | -6.42013 | -39.5984 | 2025-10-16 03:47:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5be3897e-1840-3759-9f16-75ef03b4f69a | -11.42847 | -44.13568 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62a09b5d-b652-3b55-aa93-358265538d20 | -4.37646 | -43.40024 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cdbafbf7-b10a-30bd-adfe-9c07b51dd97c | -5.72565 | -44.52333 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8fa0eee-19ec-39ef-954d-2944463bfd36 | -10.82436 | -43.94643 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c97955f-6bab-314c-8662-53e2aab34c85 | -4.3931 | -43.40638 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f731d74-08f8-3976-a584-fead7e2e3105 | -4.91405 | -45.97989 | 2025-10-16 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0d7b2019-1139-3f0a-895e-8e4debe1a60b | -6.13892 | -41.76537 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3cddda3d-5142-38e2-a7b5-ba1e6fe271d1 | -5.32594 | -44.8355 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a57e43e-1df4-395e-bb8a-fee1bcce2064 | -6.68016 | -40.03016 | 2025-10-16 03:47:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 71e8a8e9-e98d-3e88-a000-58fe074bd987 | -6.56576 | -42.96371 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b98a91e5-de93-3a56-ba92-ad8dd70ce13a | -10.83165 | -44.00652 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f7f5ac67-43ee-3fd0-85c0-6778ae5af26f | -12.66864 | -43.4371 | 2025-10-16 03:47:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5e20d99c-3a1c-3dfb-af44-45b636ac92a7 | -10.72669 | -47.58547 | 2025-10-16 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc5f6237-1980-391d-8bb0-b61c3fd34352 | -4.11102 | -48.03229 | 2025-10-16 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9a7932f-7b4c-3b45-8776-0ff393a133bb | -5.47857 | -42.93082 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0a7adf80-854e-3337-a019-fb5d4ffbc2a2 | -4.37594 | -43.39318 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 79d55c03-f34a-313d-8d36-db361c9b7f02 | -6.06323 | -44.31757 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 02b15b41-370c-3617-a4a8-70126e70b457 | -4.66647 | -44.0961 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 9c21c1cb-3e2c-3a51-8cb0-ba50385e9437 | -6.21098 | -41.55613 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f07fbe7f-3086-3168-b7d6-15bcc7b33a8e | -6.04186 | -41.91444 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 737f30d5-6c34-3fc2-b53c-cf1f10ba0df8 | -10.04856 | -43.83073 | 2025-10-16 03:47:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0763c917-1876-3917-a6f1-8ccc89a685db | -9.68626 | -44.52817 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f2fd97d4-0afc-30f9-9ede-fad3faf1bb48 | -5.42278 | -44.24274 | 2025-10-16 03:47:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d1c671d-79d5-3eee-ae6c-d4fa93e86ace | -10.66371 | -45.3159 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61eaebce-7e51-3317-b7b2-6710daea38b6 | -9.71035 | -44.52732 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 581ad42f-433d-3c42-81cc-c8a193ca494f | -4.63903 | -43.13318 | 2025-10-16 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3dc1d9a4-fe65-30ea-ba36-e00e81d53a76 | -4.35975 | -46.77676 | 2025-10-16 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4c0ddeb-b100-31bf-bcfc-b6be06045254 | -3.01225 | -45.37828 | 2025-10-16 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 36.6 |
| ba92c6ea-be1f-31cc-b15b-af6349f9a798 | -6.1567 | -40.90629 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b1b1421d-a0bf-38fe-b66b-021f66f0749b | -5.884 | -43.86699 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e759bdcf-1ff7-3b7c-8977-4d4ec49d6e4a | -11.58361 | -44.07915 | 2025-10-16 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f03ad0f-5c29-39f5-b22a-962c19cdbafa | -3.67949 | -47.63254 | 2025-10-16 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bf3d84db-4687-3744-8b90-c222c1a69cc2 | -6.13899 | -41.73977 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5d41a5f5-be56-364c-96fc-6be335d34df6 | -6.14468 | -41.78134 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bafec718-759c-30eb-a5e7-5250ae0c57a1 | -10.66277 | -45.29337 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfe2a092-2fe7-3006-a239-bd059b4c55cc | -10.13254 | -44.56417 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c893dfb7-d5fa-3d3e-a2cc-9035802e0116 | -4.36958 | -43.40243 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 584ba7a4-2036-32c7-8e51-851bd61b1927 | -5.40166 | -41.1479 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3f71664f-9491-3cbb-b934-5fba670dfeb8 | -10.12535 | -44.57791 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5142d79e-8a55-38d0-a59b-58c3e9f7400b | -6.36853 | -41.49188 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 26.1 |
| de313c0e-20ef-3c6c-87bc-9253189dce83 | -4.96051 | -45.10081 | 2025-10-16 03:47:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36fc845f-8165-3e57-aafa-da219d38ee40 | -9.7138 | -44.50764 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2301ea7e-f0fa-3d40-b138-c2f89de7dad2 | -6.14068 | -41.75484 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c747d2ee-a348-3def-816d-5738aabb4767 | -5.87903 | -42.80643 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7360d3c1-f2e1-3743-99fe-406f090b105c | -5.24039 | -42.00439 | 2025-10-16 03:47:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4251625e-02dd-33d3-a8a7-47a266399371 | -4.66741 | -44.09055 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 141b7e95-db50-3cca-aeb2-2eb0b4ebdfa3 | -5.42127 | -40.97743 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bcf54f7a-8074-3c12-8d5d-99e7606ac0e7 | -5.29888 | -41.17603 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d66c9551-eb2b-380c-8c50-9722c5c8bb52 | -5.47412 | -42.92997 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| da5378e3-13b2-3af2-aad5-fb18cd862024 | -6.17712 | -44.30176 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc15101b-e8a7-3d44-bbe1-dd51a262075f | -4.11005 | -48.02883 | 2025-10-16 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| f671c10f-99cd-34dd-a9b7-b00ece481018 | -5.1357 | -43.34443 | 2025-10-16 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27978a58-280d-3355-83b7-d11d8ea771a2 | -11.58003 | -44.07405 | 2025-10-16 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3be9e3f-ca0f-3e41-8fbd-84c64321fa1a | -6.221 | -41.55056 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1b346fcf-90c1-3881-b2a9-9812681a7a38 | -3.01535 | -45.39345 | 2025-10-16 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd803ca1-9301-3321-ae4c-5b8a7ec77847 | -6.52261 | -42.19476 | 2025-10-16 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ee5b2007-ac38-3409-9aa3-bd4fe978eb5b | -5.60115 | -47.4943 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d431323a-9900-34a0-911a-af4564355943 | -11.05433 | -44.78789 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15fcafc5-9048-3752-9d54-272254eb842b | -10.69764 | -44.43449 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2147ec9e-7090-3f95-9ea0-85160c275b0a | -5.05787 | -40.47003 | 2025-10-16 03:47:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 36b0f631-9d91-3045-a2f2-2d3b8d908d50 | -4.83311 | -45.65799 | 2025-10-16 03:47:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d993cb5a-8e44-3495-9c5b-38b234e8ce5d | -5.53534 | -41.33015 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fa82f8aa-48d9-37c1-a254-ab1b2905df38 | -4.37761 | -43.38302 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| b0f8421c-4131-391d-be6c-8cae72a9c6dd | -11.42731 | -44.06603 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85748482-41a0-3d89-a621-676379831baf | -6.17816 | -44.29592 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a494a8ee-80f3-3420-84ef-552d23eed701 | -5.87715 | -43.8501 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78955374-7a68-30f1-ae68-9c45c5384a16 | -5.33351 | -42.56092 | 2025-10-16 03:47:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8fe8afb2-e19a-35db-a300-1e91388ae46f | -11.49924 | -43.48104 | 2025-10-16 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3ca88cf-6b6f-3e46-8c43-1e87d5a284df | -10.27256 | -47.88934 | 2025-10-16 03:47:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 405f87a3-031d-35de-89c1-e65ba1a8948f | -4.39392 | -43.40136 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 1ec14744-9a3c-3133-ade7-d6463c8d4f1e | -5.34095 | -43.73785 | 2025-10-16 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7954f329-e7f7-3b48-ba03-9a766a865e65 | -4.3563 | -43.39507 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| aa8f2656-a859-3961-8e11-0dc461820110 | -6.13779 | -41.74697 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f764de7c-c035-319b-8e95-3cb068626dd8 | -3.28355 | -40.89237 | 2025-10-16 03:47:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a70ce458-1d08-39cb-8b7e-28beb2b1b6fe | -5.87685 | -42.81956 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fffc2326-07d4-3a66-a6de-8fdb9c174c1c | -10.80529 | -44.00182 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 454fd7bb-c981-3b0f-90b1-e454fa943e31 | -10.50829 | -43.38229 | 2025-10-16 03:47:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b46f70a-257e-3069-83cd-becc99a7d11d | -4.37561 | -43.4052 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 24a69e3a-f627-359e-ad7b-3deaec5b1619 | -5.46768 | -44.64392 | 2025-10-16 03:47:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c501d466-6434-363c-94c9-8df97ac1b7cf | -6.04064 | -41.9338 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 702be347-99ed-39a3-baaa-884ffd4cab05 | -4.5581 | -44.008 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e61d1fe-f825-3029-a080-5ad57702c314 | -11.13974 | -44.83596 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58d8e264-4ec0-3dbf-802f-56e0c0eea101 | -10.65011 | -45.25347 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e5ac3ea1-9fdf-3b2d-a01b-666188c0ec04 | -10.04058 | -43.82602 | 2025-10-16 03:47:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b465f74b-d87d-3c1c-a75c-39637ab5fdf0 | -12.64947 | -41.26952 | 2025-10-16 03:47:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9da33634-0484-343f-bbe2-37f25e8c37b9 | -3.15744 | -41.99488 | 2025-10-16 03:47:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 0.1 |
| f56f9d11-3732-3054-8fd7-51a0b83f87b2 | -6.55051 | -42.12987 | 2025-10-16 03:47:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5f0df625-fb6b-3f83-8eaf-c8e6fb8e6b28 | -4.10268 | -48.03337 | 2025-10-16 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |


[Clique aqui para ver as próximas entradas](README30.md)
