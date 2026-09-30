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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 265b8a18-0904-33b2-ba7b-9df70906bbe1 | -10.57511 | -50.84774 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f0bb0c9-3236-3c41-872f-aa6a1b20f07c | -3.1536 | -54.08002 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61770414-8a52-3738-ae4f-42a1a87a3c26 | -3.82847 | -55.79664 | 2026-09-30 04:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d6a9aee-6522-3f04-9907-6be85d811051 | -8.26849 | -54.75996 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bb83abe-9be0-3142-9628-ff325495f21d | -4.02581 | -54.1979 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3285b27-81b7-3cae-a05a-bc6bf4b2d71c | -9.07156 | -49.87304 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7b4d10d-0eaa-3784-9c27-8a0ccaa420a8 | -16.41945 | -43.3051 | 2026-09-30 04:53:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ef04315-0cc4-3bab-8849-96c1e6adac3b | -8.94808 | -49.78945 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9dc161cf-683e-3a5e-94b8-8d9e6f87f776 | -9.66392 | -45.11625 | 2026-09-30 04:53:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8e66b98-2c68-3d72-a7dc-76d4340040e9 | -4.02448 | -54.20033 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bd67232-d21f-36f4-8ec8-f13e69a2d20d | -3.87845 | -51.95955 | 2026-09-30 04:53:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e7460ac-91ab-37b2-8271-1f9602402c29 | -7.84353 | -45.82407 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a3ee6ae5-8e5f-3e93-9b3c-9eaad5a758ec | -7.35422 | -49.79565 | 2026-09-30 04:53:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba58a3cb-0d79-3a30-bf45-5a263668bf86 | -4.26807 | -48.55767 | 2026-09-30 04:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4bed8216-0fc8-3d44-8e14-1f41c6f8f566 | -6.41653 | -45.85814 | 2026-09-30 04:53:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e004484-c22c-3914-9bc0-c9cf2300d437 | -5.73372 | -45.16975 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c2ac0e23-b070-3ece-89f4-9eef735b7db5 | -6.48743 | -55.97359 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cea1bf5-0176-3d4a-abb2-5f2a718f3070 | -5.73 | -43.51083 | 2026-09-30 04:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7f00b4b-bfe3-3afc-9e3f-e4e08e91551b | -2.90036 | -54.09198 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| cfdcaca3-b6cf-37c3-8ddf-4c505e5cf94e | -8.72015 | -47.59232 | 2026-09-30 04:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffd9f390-4f1b-3a8a-8e38-43735b59b859 | -4.47807 | -43.65402 | 2026-09-30 04:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08244c29-5d4d-32fe-8849-e6df5086d1ce | -6.23164 | -55.65176 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2be1ff24-f386-32b4-95b7-c6b227ee0aa4 | -4.84634 | -50.68261 | 2026-09-30 04:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6032d2d2-1d0a-3b23-894b-52e80096e5d8 | -6.39921 | -55.20497 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9984074e-d43f-3d0e-8cb8-633c68250aed | -11.15819 | -44.77091 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a0b268c-7d3e-3f0c-91de-3ef78efd4637 | -15.2031 | -46.14535 | 2026-09-30 04:53:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1e4e30ba-2603-3eca-b916-ecf1463963f6 | -14.89606 | -51.86847 | 2026-09-30 04:53:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08b94ca1-2af7-37b2-a11e-55f3fe749ec6 | -2.89736 | -54.08697 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e6dbd605-653c-3723-a481-448e4ae154d5 | -6.14964 | -51.74045 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4723c66e-0d76-3235-9634-35f12500b6e3 | -12.12372 | -61.14859 | 2026-09-30 04:53:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 573c4475-6b47-31ed-950a-ca83a55fdfdb | -8.80941 | -47.17731 | 2026-09-30 04:53:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 530204ca-781a-3fbf-9b13-622a80d2b42c | -6.14046 | -53.26336 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22705b93-e422-3ad0-bbb0-4de8ecbaac8c | -7.83043 | -47.92784 | 2026-09-30 04:53:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 783d9b31-06f3-300e-8028-89271e957e06 | -4.54221 | -50.77964 | 2026-09-30 04:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ff84a1d-c0bd-3da3-b20e-d93b5c85ced8 | -5.09663 | -46.03931 | 2026-09-30 04:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe009864-d4df-38ea-a3f2-5272c6dcd27a | -11.39903 | -43.47138 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 25f624ae-88ba-3706-931f-9ee3a877314e | -7.51751 | -47.33423 | 2026-09-30 04:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66a69d27-81a5-396d-8d19-96dcc2c4defe | -3.51195 | -50.31339 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76dbda6f-7b4a-3a31-803c-6306be252a06 | -11.15749 | -44.77617 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01f252ef-524a-323f-8be9-2a52651c5b67 | -7.82615 | -45.82519 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e976f1fd-20c7-3320-a0e4-9ef1db2e4578 | -10.08984 | -50.31231 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93d5fd5e-5638-3582-981b-f69db0a355cf | -3.82297 | -55.90726 | 2026-09-30 04:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f43a5ec-8930-3378-8e79-364365dd7940 | -7.54829 | -55.03688 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 54446c9b-3759-31ff-a9f5-3dea1e87f463 | -7.07138 | -44.36546 | 2026-09-30 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 378c2858-d872-3992-814c-781725cf37eb | -9.81593 | -49.15147 | 2026-09-30 04:53:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca37568d-46f3-37eb-ac7c-45e3b902a817 | -6.78361 | -46.46641 | 2026-09-30 04:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bffdf25d-13f5-3be4-9069-7dcd23e329b4 | -12.89951 | -61.71263 | 2026-09-30 04:53:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97cb8599-4045-3927-9d74-4ce24f3ade30 | -8.31897 | -54.75418 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| acecfa8c-0a75-3534-9fa8-d8f1ec0435fb | -3.24901 | -50.81464 | 2026-09-30 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 20bdbd0e-0b21-3f60-a6b5-cef633ab330a | -6.34367 | -55.33128 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60a8e6de-122d-3dbb-ae10-f3bb64d46446 | -17.12675 | -52.13632 | 2026-09-30 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ed9b6d2-7076-3e17-814c-b46e5bf87acb | -14.50647 | -48.28334 | 2026-09-30 04:53:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55f126a7-6aca-369c-8cce-27ef2b4efd5d | -7.70035 | -54.79644 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39e0c157-3c0a-3525-ab7f-d80da5a99377 | -3.37962 | -50.95572 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ffc9d1cc-693e-302c-82e0-409e55482ecd | -7.50777 | -55.0303 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e4a331d6-3dd4-3682-98e8-4268c029859e | -15.09313 | -47.82895 | 2026-09-30 04:53:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcf9aa3b-b7ca-3215-b8f4-01aa2c00242d | -6.10785 | -55.69534 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5eafe48e-4716-3990-ae8c-f03ab73c13f3 | -6.07233 | -47.27708 | 2026-09-30 04:53:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ae4a8c3a-efc9-3537-9175-64689de08a18 | -12.12258 | -61.15465 | 2026-09-30 04:53:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1273309a-c4d3-3896-ac39-a51cddce26cc | -16.11284 | -48.32459 | 2026-09-30 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f2c6f8d-17d3-3730-8e08-b6ea453dcf9e | -8.84161 | -49.70804 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3a48f8de-0c0f-3e2c-9a43-9cb449a80c67 | -5.72294 | -53.4607 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5f1150f-9b1a-3d24-8863-bab7073c5f90 | -8.83817 | -49.70751 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3f425385-0780-3e81-ac03-61c8dc08d5dc | -9.78813 | -44.81447 | 2026-09-30 04:53:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bde5614d-4f06-3880-affb-d97117791053 | -5.10551 | -45.03849 | 2026-09-30 04:53:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f92d7102-e4ce-3147-a3d3-3325a16b226b | -4.80178 | -45.64437 | 2026-09-30 04:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52513fd2-12a2-3bf0-9528-e0de2f754d35 | -11.6777 | -43.50484 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64ad802e-e810-310b-b626-6691da34b400 | -6.70818 | -45.99022 | 2026-09-30 04:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18bd8e50-61c9-3082-aa4d-bcd2ecc7ddaa | -11.16966 | -44.79373 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b72a7539-8f6c-3099-866a-89deaf0aeb7d | -5.85957 | -51.7902 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8dbd660-136b-3b58-bffe-7583eaa4434c | -16.35591 | -42.58542 | 2026-09-30 04:53:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e95744cf-40f9-3eb5-a85a-9bbc5a20ba65 | -10.66717 | -50.74314 | 2026-09-30 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 009e1f82-ea99-3273-bd32-e8fcc99cacd7 | -8.00501 | -44.50197 | 2026-09-30 04:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57c56d7c-b900-3cdc-bad7-b7d6555f14c2 | -10.55721 | -50.87457 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dadca7c2-0d72-3f70-8932-6a0723af68c7 | -9.77087 | -44.81512 | 2026-09-30 04:53:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 35478926-164d-3d9f-9800-6afc845c2121 | -7.5137 | -47.33368 | 2026-09-30 04:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6665a604-c90d-3e0c-89ec-1c25e14f695a | -11.19403 | -45.12756 | 2026-09-30 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d63c1163-c395-3348-8df5-bdce59b156f5 | -8.60484 | -48.91321 | 2026-09-30 04:53:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3325b175-2fa2-38b8-9f5f-616d33599db7 | -8.21277 | -45.46539 | 2026-09-30 04:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46dd2002-7396-3b4e-abc2-9d45b82c16d5 | -6.12441 | -53.28086 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 276712db-57ca-3ec3-a864-c986f6d75bd2 | -16.86168 | -42.46583 | 2026-09-30 04:53:00 | NOAA-20 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6bed8c4a-bf81-3385-bd18-5e109864ca56 | -11.2568 | -43.54169 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4356a763-9401-3dc8-91ca-122a44200a7b | -11.63615 | -43.53656 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34fe06fe-8775-3136-9754-3d14dd7d32d8 | -3.96181 | -49.01204 | 2026-09-30 04:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97834489-7646-3822-9a72-08980862c2af | -6.43007 | -46.6666 | 2026-09-30 04:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c090e661-7d49-335b-8f6e-8537095370bc | -7.56006 | -55.03436 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8180652-054f-311e-8656-c17034c86b0a | -8.01002 | -47.45658 | 2026-09-30 04:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9af56aa-2236-34cb-92c9-9982162dcf0a | -3.83613 | -52.26615 | 2026-09-30 04:53:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44c6e0cc-ca5d-34c4-a902-e712a0347144 | -17.92032 | -44.40543 | 2026-09-30 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dd96a9a4-cddb-301d-91c8-478f121c7c18 | -9.92881 | -50.15087 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 240a88b7-b8a6-3cbd-a059-0277870624ba | -5.98264 | -53.55313 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93465646-cb75-3a75-adb2-ccea4fcf60cc | -7.07564 | -44.36332 | 2026-09-30 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a3d247e-02f3-37f7-87c4-19ffd4a97625 | -11.44457 | -43.44774 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98faa47d-46b1-3f39-9e8a-13c8136506c2 | -15.44284 | -45.68884 | 2026-09-30 04:53:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b662048d-91f0-383d-a86a-9b255dba9751 | -9.77552 | -44.8158 | 2026-09-30 04:53:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1adedd98-9c3c-3010-bb25-cbb53c9e4a8d | -9.36748 | -50.27431 | 2026-09-30 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d59ab09b-b8fc-3b43-a16f-99e5f0069edf | -11.63175 | -43.5295 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eadfd4ce-0b7a-3cba-ae97-bcdcfccf0602 | -15.75595 | -46.04121 | 2026-09-30 04:53:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c3c8fa9-0f81-3143-80e0-c05c945c53f6 | -8.95035 | -49.7975 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60c13284-09be-3eeb-9c66-280030bc8eb5 | -10.52103 | -45.37426 | 2026-09-30 04:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README44.md)
