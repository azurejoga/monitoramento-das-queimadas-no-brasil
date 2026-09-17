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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf0afa37-61d9-38bf-91d4-756fe3e1516c | -9.46599 | -45.44866 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bbdd5c82-fb66-3397-b826-e7d8ccb928b0 | -6.69573 | -56.41115 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5722b8d5-1325-31dd-9e89-32fa2987ef90 | -9.84322 | -48.37983 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10366531-7232-31f6-9042-fb9f0c64aea5 | -7.13889 | -42.16538 | 2026-09-17 05:16:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2b0459c5-7eec-357e-b523-9e6efa00c89c | -5.1426 | -55.94264 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ed6c10a-1893-335c-85d2-cc57616d79d6 | -9.95133 | -45.29961 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fbb045a-12be-34ba-8ef0-28814cfa8e90 | -2.07245 | -56.43068 | 2026-09-17 05:16:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8ca311c-89da-3cfa-9a2c-d871a113c046 | -8.32938 | -51.3104 | 2026-09-17 05:16:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 321a3fd2-f576-368b-aca8-320e34a05ef5 | -3.81089 | -55.88833 | 2026-09-17 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7410773-e2a4-3f24-bd92-98271e32e444 | -4.54785 | -42.94357 | 2026-09-17 05:16:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0194edb-f82f-36b7-9f90-bdcb206093a0 | -3.80511 | -58.89436 | 2026-09-17 05:16:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fb58264-872f-31ce-91ed-e46978c91b89 | -8.25335 | -42.16465 | 2026-09-17 05:16:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c01a3c9f-cc32-396d-aed8-3dc2376803bc | -8.49656 | -57.64354 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ba5cb0c8-0e3a-3da6-9cef-97fa816521ed | -2.97171 | -54.15736 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 987e3bbc-b630-3dda-9f98-08b3be945d77 | -5.46468 | -44.95393 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c604707-1027-3a16-97b3-95df7adda2b1 | -9.81816 | -46.49568 | 2026-09-17 05:16:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41a3c730-889e-3318-bda0-cda3901dc984 | -3.26332 | -54.52138 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f53b2f69-84e7-32e4-ba6e-cc66e5194f63 | -6.10456 | -57.6342 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23e60191-4cbe-3d15-960f-eb09dbe348a1 | -3.33744 | -56.94981 | 2026-09-17 05:16:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c16c27b-5b2b-373a-8a01-d516102d5452 | -3.57842 | -54.55944 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c85f15be-cb75-37df-b7e7-fd9d139a5a73 | -5.83953 | -52.09497 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00af08a5-595d-330d-a95f-0b1915225a98 | -3.2617 | -54.27108 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8089a429-5fc5-3b14-bb51-60035e89f7bc | -5.83683 | -52.11254 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd655673-f0a3-3f0c-b716-f85061ee6047 | -6.13736 | -57.69298 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e90c158d-bda8-39b5-9b81-495d8f2a1d6d | -4.14262 | -54.4151 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df485182-03f9-3d17-995f-71b51c389d15 | -3.07387 | -51.2023 | 2026-09-17 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0440e328-aef7-3a15-89e3-1f21fde70c5d | -5.92784 | -51.6455 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9c5e43b6-0660-33e6-aab4-8d50bb84cc11 | -3.49044 | -54.71323 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 238af61f-f39c-3b07-acae-ff5ad90cc8ef | -8.49715 | -57.63992 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 663f5622-666f-31e4-8147-f0d016dc0c02 | -7.08242 | -42.09332 | 2026-09-17 05:16:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| de264135-a17d-37be-ba94-ccc73a17704c | -5.14704 | -55.93623 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 979a2f14-e9ff-3b5b-b082-02a6aeeb0747 | -6.83681 | -55.75242 | 2026-09-17 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27d5153c-3e79-31f7-a980-102fd4b73178 | -4.53857 | -54.93106 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6c3e2a6f-4c10-3722-abf1-ac3a305f28ab | -6.79504 | -59.17697 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b31a37e-0973-3168-b602-0487bcc6146f | -7.00411 | -43.32792 | 2026-09-17 05:16:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c0ef5d39-a3c7-3fe5-aece-174e0b7c6731 | -4.53469 | -54.93401 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9df5c76c-7826-3bc2-b1f7-3deeb370512d | -3.17864 | -48.58155 | 2026-09-17 05:16:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b56bb6fd-e0b2-3f8f-8be5-2840faca2668 | -4.53421 | -56.08574 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45947f03-1e78-3073-94e9-993cab97fb46 | -6.75484 | -55.84636 | 2026-09-17 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb54d783-c893-3fd6-a78d-65b744d10521 | -7.94915 | -54.89169 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 929b6c88-7797-30ac-a081-541d5ec0e829 | -9.11557 | -45.72347 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 292b0810-b66a-3a3f-9da7-0d5e474268d2 | -4.18954 | -49.28984 | 2026-09-17 05:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 35eed678-3c34-3e3f-9648-dba8c4ac6b9b | -8.90357 | -43.88501 | 2026-09-17 05:16:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 89b7f71f-2d36-3a4c-ac7a-68b0c13d5711 | -8.78597 | -46.90667 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b3a29b4f-899c-33f3-a30e-e772e5ff8b8b | -7.27279 | -44.21421 | 2026-09-17 05:16:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb29352f-c771-335a-9b6a-4afef6df27b7 | -5.86489 | -52.05375 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbb53f96-7c14-3975-bd9e-f5e5fa3ed155 | -6.80096 | -59.18668 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77eb6be3-7013-3053-bfe7-f2e0f41dd233 | -8.56163 | -44.55418 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a1e76b99-01ee-3f41-9202-e6eec74ce902 | -3.7086 | -51.11159 | 2026-09-17 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9bec51de-b209-32bc-9ca1-bc510806aa7a | -2.89807 | -54.1784 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66b1c465-1d0d-375f-80fb-d02bbea88bef | -9.96691 | -45.32526 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f683e922-e07b-3d87-b7e0-77c5c9b760eb | -6.11855 | -51.70715 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ba766c3-ae23-3380-a7ce-614735aad916 | -4.81067 | -42.89621 | 2026-09-17 05:16:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| fc530f57-fbdd-3148-9ff0-02497a9e8a2d | -7.46182 | -46.84007 | 2026-09-17 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f32d3fa-c690-347c-bda4-4b9eee6d67ca | -3.50537 | -53.20413 | 2026-09-17 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c516051c-048a-3ee6-95a8-3666e3cbbb8c | -3.37993 | -50.83735 | 2026-09-17 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54e832e9-731a-3049-a796-255d94117b60 | -9.12427 | -45.72766 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2efb0e29-be13-3e45-8b09-6a8b6008a411 | -8.55865 | -44.47564 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8e0a401-e6db-3174-9e36-7ae17659735c | -4.37749 | -55.02662 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08acd974-1bb9-3dce-b515-beb3f5907d50 | -5.90491 | -52.09824 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6e5446a-c6c3-3345-ad93-c2e5007d3d69 | -3.8163 | -58.89619 | 2026-09-17 05:16:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 457217c2-384e-3789-b8a0-de7cebbbd3e7 | -3.73162 | -55.9441 | 2026-09-17 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 321c6ef6-895c-3df3-aa6e-6bcbadc90dce | -9.85245 | -48.38746 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd0d6ff0-b558-3474-aaee-1442a9338cf3 | -6.02858 | -59.93404 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4dee43f7-d63d-3df2-97d0-16a04dc43b33 | -6.81535 | -59.16644 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c40360c6-07a8-3595-baab-0a70ae3f8f46 | -2.83547 | -56.72485 | 2026-09-17 05:16:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 06bbcf49-a1fb-3a33-a2fb-936da5a911e1 | -5.63451 | -44.80879 | 2026-09-17 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2017f4e0-7237-3137-9468-933ecc1ed9a8 | -8.26795 | -42.16611 | 2026-09-17 05:16:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b561a40b-4fc9-3016-9c45-1059ceeee4b3 | -2.87869 | -51.87685 | 2026-09-17 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d8f98b4-48a8-31c8-a830-1c53c5b2deaa | -5.97614 | -55.36019 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fa94909-b3e4-34f6-bb0a-27b243040902 | -7.36565 | -44.47862 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 436f2501-8148-3443-83b6-86408c1ea717 | -6.14484 | -52.75113 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 185aa189-b0c0-3a74-8c2e-a1f8b81b855e | -4.53356 | -54.91961 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 528995c7-fb85-3b9e-a1ab-38673d093e96 | -7.38677 | -44.51251 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b131a3ab-e8ac-3a7d-9d3d-1bcbb059d625 | -5.40369 | -49.19845 | 2026-09-17 05:16:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 942c27d4-3ab2-3111-a415-c3e9e6565946 | -2.90865 | -54.17648 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec060945-fbf0-3bc7-ada5-65359078db9f | -4.49536 | -55.49879 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99b242c3-2548-37c6-873d-0355804d43aa | -4.4504 | -55.20819 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3522f15a-c2c0-312f-a78a-8e7bd00cc24f | -9.46755 | -45.44616 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ddccad38-3beb-3f73-8f92-e202a6df1491 | -8.47504 | -44.55443 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0b794569-848b-3746-9d77-2ae9cb448ac9 | -7.58119 | -44.92772 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bee0ac6-846f-362a-898b-120f5da81e74 | -3.66052 | -48.96632 | 2026-09-17 05:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 830ff9ff-201e-3b9e-bd42-4b4f17d55006 | -2.90196 | -54.17543 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 275877f9-8404-3830-b55c-e266f0cdaddf | -8.48701 | -57.63822 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| aeb83751-ef3a-3a45-807e-258032a4a23f | -7.3036 | -64.67571 | 2026-09-17 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d03f3dd1-0e21-34bd-959e-69b1bf7c53fc | -8.39644 | -42.20597 | 2026-09-17 05:16:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 680a0611-3a0d-3ef9-b147-9a8ed01ebff5 | -3.42893 | -58.195 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06740a0e-849c-349b-bce5-1790177d5823 | -6.36632 | -58.28481 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d1b23e8-8ff2-3d4a-91ac-808505421d41 | -6.35111 | -51.77602 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6b00e317-89d7-3186-9763-7e2ab53b3b95 | -3.02659 | -51.3327 | 2026-09-17 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44ebccc8-26e5-3e1b-8407-8db1f0b2de22 | -3.33415 | -59.82352 | 2026-09-17 05:16:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04663496-bc61-3769-bc6a-1a261331cb5e | -2.91255 | -54.1735 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f56cc78e-91f1-3d5a-99fd-389e749aa1e2 | -6.90568 | -59.02634 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c364655-e774-3f1c-bf46-98e8150f12d1 | -3.48601 | -54.71963 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c6241729-e73f-38c3-8dc5-a4ab1e3e449a | -4.51147 | -54.97301 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7ffbabd-36cb-3449-b9ed-a148fbbd5b97 | -3.26279 | -54.26409 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69363d6d-87fe-3601-b860-7f9e5d87a7a1 | -8.37076 | -54.73415 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 444f9686-18cb-3c01-a457-71bdb4633027 | -4.51585 | -54.94528 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73eb64dd-c7cf-3b65-8d73-de470d6b0360 | -6.80885 | -59.18283 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 831e9967-9dcc-381d-9af8-bd6ba38694f7 | -9.5667 | -46.57792 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README62.md)
