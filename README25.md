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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edf169e6-e044-3936-bd8a-ef622ed219e4 | -2.96361 | -54.0885 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ab82e20-5320-3470-b16b-1944a1186467 | -3.49158 | -54.67965 | 2026-09-27 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 234ee8a8-528d-3846-8706-26caedabf234 | -4.56232 | -54.94903 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0bc6805c-c2e5-38ae-a054-e65ca9eb4df7 | -5.17063 | -56.00872 | 2026-09-27 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2498eea7-ec33-3832-9c7f-04d2200a7205 | -6.83912 | -43.51703 | 2026-09-27 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abeb46a5-1519-3431-a448-77aebf361e52 | -8.34892 | -44.13167 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 511f90c8-df1a-394d-bd0f-07a0b8e7046b | -7.60036 | -55.0553 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20bf2277-785a-3e8d-be95-cb57c841a8de | -5.73276 | -45.06416 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43877b56-36ee-39f8-87aa-129df7408dc9 | -2.91678 | -54.1849 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce06a3d7-ba81-39b8-896c-38069cb33cb0 | -3.03596 | -54.69437 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29d1cfde-5a19-34ed-a364-b87d2048a304 | -4.54811 | -54.9708 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 02301015-6926-39f0-9433-e121b0cdaafa | -8.35264 | -44.18658 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 2dc858d8-8da8-34ae-a19a-68e388e2ea2e | -4.35897 | -50.31927 | 2026-09-27 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 154b1aa6-b20e-3230-8b8c-84003e13d62d | -4.84159 | -42.89371 | 2026-09-27 04:51:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 06dff8d6-eb22-391f-a7cb-5553f949bf45 | -3.22196 | -54.32048 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76b474ba-2e89-3e54-8278-595f702fc33f | -8.34991 | -44.17203 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 237.5 |
| a602b718-d70c-3861-a560-e68b655e2cd8 | -9.31451 | -47.62913 | 2026-09-27 04:51:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 05df90c4-c41d-39b7-acfe-1a2a31b93229 | -1.83845 | -54.72079 | 2026-09-27 04:51:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| bdf2d7ad-4629-36d6-b9db-fc816aa7c07b | -8.34822 | -44.17912 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 98537e74-14fc-3168-beee-62b2c604c3a0 | -4.49742 | -54.951 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 1cc7e562-6a28-3e51-908a-cbdae4c8d90d | -3.67459 | -50.8414 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 117ffe2a-9b66-3796-ad77-924f40896dd1 | -8.34993 | -44.16587 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 304.2 |
| 2c4f4901-5666-3ce1-9045-71991dfc9c40 | -7.35299 | -42.0767 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3daa881d-075f-3b91-b802-ef50f352261d | -6.13997 | -53.05474 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9e1edf7-b20e-3a53-89f5-5d569b32ac16 | -7.29069 | -43.30838 | 2026-09-27 04:51:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2818ba35-4bd9-337c-a18b-48a6a66fa17a | -6.17476 | -44.59354 | 2026-09-27 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6db6a56-0dc2-3b0b-a584-a865e039486a | -1.74078 | -55.2432 | 2026-09-27 04:51:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68e75815-18be-3f8f-a97e-203d0fc7e5a2 | -4.15463 | -54.15034 | 2026-09-27 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e65872db-5472-3fc7-8d60-86e07480a70b | -8.04471 | -54.89062 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d0fa91b-c7f2-32d6-88b3-2627a05fac20 | -8.02776 | -54.88792 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 538ca767-80f8-32fa-a912-58f55625424c | -7.49778 | -55.01612 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 394b49bd-a58d-30f9-8b60-d4db55833c03 | -4.44474 | -55.02782 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f06d0af-806b-34e6-8014-6170f2a2e831 | -2.86187 | -54.13384 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 263e8e89-a371-39d4-9456-4ca7f26b562a | -2.83913 | -51.35807 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d3f7898-f202-33cf-a4a9-8afdc646367d | -8.48142 | -54.92714 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe3d1dbf-8520-3d9d-baf4-c6d280032f2c | -8.35164 | -44.15255 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bd069894-278d-35c3-ac94-e558a84afcfe | -3.11768 | -45.43787 | 2026-09-27 04:51:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b495631e-8785-35e1-b0e1-59944ba08f32 | -2.65939 | -56.5461 | 2026-09-27 04:51:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66388171-26aa-30d5-9a5a-0dedb6a485f4 | -8.36269 | -44.1507 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 628d8b39-e5d5-31a1-9cc1-c780f06ac139 | -9.15542 | -46.76263 | 2026-09-27 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d9f97e1-3208-3330-ac7b-796a2da23945 | -6.64194 | -59.94522 | 2026-09-27 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 196454cd-1e83-3c72-ad0a-7b5c0ba99cc6 | -2.82983 | -50.47474 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a698be1-e936-35fa-9edc-1ff4a4365810 | -6.69559 | -59.96446 | 2026-09-27 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4046f04a-5961-3156-ac35-717b63e5da32 | -7.4966 | -55.02356 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 194266fc-4877-3364-b020-8f0625082e81 | -4.09726 | -54.88735 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab0a18e5-0c68-3597-8b96-5252998ec5bd | -8.34464 | -44.16504 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7f66af1-59a6-3e0e-910a-8faa55407c8a | -7.27795 | -55.57639 | 2026-09-27 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c261f6ae-9296-351e-b51e-611b721f11b1 | -5.74278 | -45.06123 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6e8750d2-5823-3e2e-bae0-e560bc54cb75 | -8.34687 | -44.1547 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e93a46b-45e0-36eb-9ab6-06e0ae77c378 | -8.59693 | -54.64821 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a3ed3179-e5c3-392b-96d2-9d7738105c92 | -3.8027 | -51.02124 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 75c19c97-800e-37e9-aef2-8446cace2799 | -6.63735 | -59.94434 | 2026-09-27 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a43d0f9-acdb-33d1-b674-af5c06bf7bd5 | -4.58467 | -54.92096 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d409840-5af8-3912-b870-8122f21027c6 | -8.47128 | -54.92546 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a56295b-699c-33ee-98cd-486c5e88da0c | -6.05322 | -53.6066 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbc35774-eac5-33ca-a4f3-a298b8d22085 | -3.31447 | -52.54139 | 2026-09-27 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4708a80d-8153-32c1-a2b5-96a585160a01 | -2.56288 | -48.26004 | 2026-09-27 04:51:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0884fff-5dc8-316f-a723-c85e70dde598 | -8.24569 | -43.78619 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 86d703e3-eced-3505-9ab8-b1c20664630a | -5.74791 | -45.06099 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8bf661ea-94ad-3f89-a585-895f66205e60 | -2.14851 | -50.89897 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa8aa403-68cf-3aae-8245-3ea4f19875ab | -4.27232 | -55.13157 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 192e1253-34c9-39a2-b799-814e02559707 | -8.35035 | -44.16255 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 1d304b96-ee48-3515-a8c7-592e4929d52b | -4.14379 | -48.21984 | 2026-09-27 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 26a93331-f1d3-3061-b552-4796da07d428 | -2.06458 | -56.8736 | 2026-09-27 04:51:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2748db74-ade6-3480-829c-76d2d9c333c7 | -5.67909 | -50.09563 | 2026-09-27 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c1331313-f38e-39d2-8822-d280e942c2ee | -2.95675 | -54.08743 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3e4fb01-48f5-316e-acbc-ea734afe59c6 | -3.29742 | -54.68996 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66ad4429-9cdb-369a-969e-5f2bfe97b00a | -6.87769 | -55.55901 | 2026-09-27 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0958fcb-a836-3d11-b283-2f8b4f3b00a1 | -3.96849 | -50.71751 | 2026-09-27 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22c30809-02a0-3128-8350-d9169a644f3c | -2.50907 | -56.22324 | 2026-09-27 04:51:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b996cfa-c261-313d-a470-93aca455eb5d | -6.06977 | -57.83182 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e3aff5c-e2c3-326f-8b1e-f9e1f6209b0a | -8.09161 | -54.74849 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70adfe4d-cd0b-3ed2-8d53-75ab12f49170 | -1.74446 | -55.24374 | 2026-09-27 04:51:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64a97827-f6e6-3404-b791-79e3a7f2d5a7 | -3.69778 | -51.37115 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3d0b0575-6960-345a-9d13-9dc9f2980f1d | -4.56383 | -44.07902 | 2026-09-27 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37878f23-9255-3882-9cfd-fae0670cc73e | -6.056 | -53.61062 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f21eacb2-bee6-31c5-838e-9b35a5f71241 | -8.81743 | -50.48154 | 2026-09-27 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bc88238-93df-33d2-8cde-61c750974c16 | -8.34384 | -44.13726 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f263540c-6a03-3a81-8dfc-8b249c81fde1 | -3.80554 | -51.92554 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 980aa6c2-3118-3464-bc85-d56286d289dd | -3.07395 | -54.41053 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42139fe3-a844-3f87-859a-46d3da7ce572 | -6.07138 | -57.82838 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a1668476-4502-3d85-b5bc-3b5b02922320 | -2.78993 | -57.68917 | 2026-09-27 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 942c7a58-aea6-3d97-b4a9-957c1e150763 | -7.69107 | -54.75538 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95be462f-469e-3fef-bb56-d97191da4ba0 | -6.0571 | -53.60364 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f1d82f3-951e-30e6-ab48-8c556e8c879c | -6.84207 | -43.50917 | 2026-09-27 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e1b4eb4-b657-3cc5-91ab-87e0ad55cc00 | -2.89142 | -49.48472 | 2026-09-27 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7cae1b6b-c294-3b6b-8529-ff894f00f3ae | -3.22422 | -54.32859 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a7ebeba4-f870-32e4-904c-9fd71a7ba71e | -4.28997 | -48.61662 | 2026-09-27 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31e5e8b6-bf94-3e1d-99f7-8c13f26e3405 | -8.03115 | -54.88847 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aa6d367c-585b-307d-a87d-845d3a11423b | -2.89088 | -54.19244 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0d16fd1-b4eb-3041-a15a-9ae5b206b8b8 | -3.07576 | -54.39912 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af47ea2b-954d-374a-9c11-388b50e28518 | -3.939 | -50.5393 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99de8c22-9339-3122-b7c2-40f0ad0fbd55 | -6.07035 | -57.82824 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e300c2c6-f8a7-3d55-b969-00b28ac37b18 | -2.92325 | -45.50895 | 2026-09-27 04:51:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fee384a9-2896-32d5-ba2f-de167227abd2 | -8.36582 | -44.16819 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 5db6ccf5-19ae-3147-ac6c-3d966be8965b | -1.90595 | -52.08477 | 2026-09-27 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc9c128a-521b-39fb-8ccc-c7b63e5ad48c | -6.01546 | -53.8891 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b889c908-ac31-30b6-b375-fc97ba510832 | -6.83961 | -43.51355 | 2026-09-27 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73334c21-c5e2-3f10-a8ce-60f382d80cab | -9.3182 | -47.63371 | 2026-09-27 04:51:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74283103-5d28-3aa1-a341-c97ae2735798 | -4.50569 | -54.94425 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README26.md)
