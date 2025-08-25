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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23fe93e1-3e45-36b2-b495-6c9af103c8ed | -6.78942 | -44.33995 | 2025-08-25 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ade78ae4-072c-3889-a1bf-13cc64ccf49d | -4.77588 | -45.33054 | 2025-08-25 04:40:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 503115f9-7c74-340b-a144-e27add4427ea | -8.02283 | -44.98124 | 2025-08-25 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebbccc64-b384-3abe-941a-092d9f307971 | -4.17305 | -40.71724 | 2025-08-25 04:40:00 | NPP-375D | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 073fd683-e6f3-3845-a7e4-c92d7b94b2cb | -6.49064 | -43.42336 | 2025-08-25 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a1398c8e-7ac1-3c9d-abb0-3b0c39a17477 | -6.20745 | -44.13467 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d97ef923-2bd5-3ffc-87e5-e37522cc0340 | -5.8869 | -43.37909 | 2025-08-25 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63b4bc8e-fe88-39ce-829c-ee3c281ff7a4 | -7.59282 | -45.24007 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48d62eed-9cd2-3f52-97f1-cf0c9acb2d0b | -2.99269 | -49.10287 | 2025-08-25 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d423c0a-140b-3929-ab18-8dbc03840162 | -5.48807 | -41.41504 | 2025-08-25 04:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 746acd04-b5d2-3d1d-b847-fa011bb552ef | -5.75373 | -57.58244 | 2025-08-25 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f393f10-ad52-3d15-93f5-a65ac98beec8 | -7.50859 | -45.83601 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a85f09e-2535-3f97-99ca-a6af572c9935 | -5.10312 | -43.20466 | 2025-08-25 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43573f16-8d59-3a64-ae8f-43d0a68705d1 | -5.63479 | -45.15265 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e6dd5de-5265-35a6-a82c-9264c51ab59d | -5.10622 | -43.21317 | 2025-08-25 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| abf9f974-420f-3e05-9088-ed6613987037 | -5.74239 | -45.36296 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 799b3e77-e346-3379-933f-22b0f1a913d5 | -8.1767 | -45.06948 | 2025-08-25 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f0d42a6-b08a-3638-9bc9-d8ad94dbfae9 | -6.05485 | -44.44041 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53445e4f-d82e-3a1f-8fee-b2668eea0b60 | -6.50129 | -42.94954 | 2025-08-25 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf28e972-5428-342a-87d2-d71f5bb226d1 | -6.67919 | -44.41087 | 2025-08-25 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7bfb61f-f9c2-3d9d-bd08-16e83c0140b0 | -7.54313 | -46.02487 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 469063d0-7213-373e-ba44-bdf77da7a288 | -7.89736 | -45.89073 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb27ce25-4095-361f-a889-3658c89ef967 | -6.67812 | -44.41798 | 2025-08-25 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17be4f81-f326-3587-ac14-3f8b204c8423 | -4.77283 | -45.32556 | 2025-08-25 04:40:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6f8b16f-340f-3def-8187-531413360344 | -3.21711 | -50.58965 | 2025-08-25 04:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cafe209-7383-3ee8-966d-09e816c930c7 | -7.31476 | -44.53609 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9556daeb-8f3a-35c0-aec1-d78bfb2e2dcb | -6.16203 | -43.00584 | 2025-08-25 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 902af8f2-b187-35f1-ae45-7813eb08fb89 | -6.05602 | -43.68458 | 2025-08-25 04:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f65f312-1f23-3572-ab15-6dde532f2160 | -6.45228 | -44.61247 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1850268c-777e-3b99-8230-ebeb761e8693 | -5.75272 | -57.58834 | 2025-08-25 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cadc4dd1-a4cf-388a-9671-b4d7613a72bd | -7.3321 | -44.53483 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 816e5751-0ad2-3638-a970-3db0f1c9ff6d | -7.90508 | -42.54792 | 2025-08-25 04:40:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6975941f-e25f-3577-ac52-3769d96d70db | -6.20635 | -44.14193 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4504d2ed-2e48-342a-9e2f-4dc1dbef7239 | -2.07351 | -48.45554 | 2025-08-25 04:40:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5498305e-ed78-3d97-b397-3cc1d5956902 | -5.7515 | -51.70499 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83b886cf-697a-328b-9fae-419f59344e4b | -7.65805 | -42.67852 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 74fd3062-b4fb-34d8-943a-5d111b0353ba | -5.65516 | -45.14625 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3efcf772-98a4-3dbc-804b-daf58fa31fbe | -6.89487 | -47.93022 | 2025-08-25 04:40:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82363bd6-50b9-3f58-828d-0e435600277c | -5.74406 | -57.57775 | 2025-08-25 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 545039fe-a59d-32cf-a99d-191f9ca3b524 | -6.25432 | -43.8254 | 2025-08-25 04:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9e75454-2d83-329b-86c8-30c6523051bf | -7.17771 | -45.15999 | 2025-08-25 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 01ac5ea2-6896-3331-affe-90c40a093e06 | -7.28732 | -44.47012 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42123dc5-d5d4-3694-b920-0e274b6f26b7 | -6.20188 | -44.1376 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbb97c77-83ad-3c8b-93ee-014ee03c20b4 | -5.74865 | -57.58156 | 2025-08-25 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b300cd91-73cf-3219-b1e5-17696f272e08 | -5.73104 | -46.1504 | 2025-08-25 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9abfd109-70a2-3124-8f3b-967f89662037 | -4.31135 | -48.09679 | 2025-08-25 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f9ae90b-4dc8-3e29-b857-581d41ef30d2 | -6.18408 | -44.12374 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f03d1a2d-ea0e-3ae0-9abd-23a97e3a886f | -5.62636 | -43.45023 | 2025-08-25 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd7a89ce-1aec-35c4-87b1-5dd8236e015d | -6.77276 | -44.31235 | 2025-08-25 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c48af01f-8056-3f79-bcd0-10e5c9ead052 | -7.58895 | -45.2395 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e5aa70f-e01a-3f3e-a143-46cdbe165580 | -5.10253 | -43.20864 | 2025-08-25 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51231a4b-02d0-3fd0-bc41-6f22bed98b1b | -5.88629 | -43.38314 | 2025-08-25 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb56ce45-51f8-3286-8980-d702aeb1ca8a | -7.14629 | -44.16529 | 2025-08-25 04:40:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93d696b3-f1fe-3bf3-b6db-78399ea6eae3 | -6.19421 | -44.13958 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| baa066b6-10bc-3143-853b-f477a2983cc9 | -5.74307 | -45.35843 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 756e7558-a8f3-3902-a9b0-d1de7a20d495 | -8.38571 | -44.94613 | 2025-08-25 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa167d2f-7ae6-362e-8449-228221c11610 | -5.52316 | -52.0059 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f399b4a3-b3aa-3ff5-bb75-df6426e04a6c | -5.11109 | -43.20976 | 2025-08-25 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 21fb7bc4-5482-3704-a6fb-2605609abed9 | -6.03415 | -44.21016 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48b585e5-5c06-30d7-8692-a81320cb576a | -7.20564 | -49.61284 | 2025-08-25 04:40:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d0f1505-f57c-3bf0-93f9-0f78d978da19 | -5.73824 | -46.15149 | 2025-08-25 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 078e93b7-ddfe-34c3-9cf4-b852147864a4 | -6.03011 | -44.20951 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70986911-1e27-358a-9b01-48cbd7f926b7 | -2.4444 | -47.32594 | 2025-08-25 04:40:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f9d74b6-919c-3d22-a82f-16bd6ac6e14b | -7.69412 | -46.92848 | 2025-08-25 04:40:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f255193-d956-30b0-80d8-64863aec608c | -7.47291 | -45.02491 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c8595d4-fc14-3020-928a-835c1def1f20 | -6.89204 | -47.92604 | 2025-08-25 04:40:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a8c15ff-073f-348d-b43e-9e6f92c47bbf | -6.49589 | -49.90992 | 2025-08-25 04:40:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b18883df-2f69-3c22-ad25-13309aed7646 | -6.04067 | -46.29491 | 2025-08-25 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75f6d86d-cb0d-3720-bc61-cb26ff3a797b | -7.57349 | -45.23679 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 642c639f-14cf-3aa9-bcef-d6ef4e9d8e76 | -6.98418 | -44.13688 | 2025-08-25 04:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fefeeb7-5054-3426-a2fb-f3a7330f2886 | -5.74763 | -57.58748 | 2025-08-25 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6af4954b-24ed-3130-8a68-a72c0e6fe7e1 | -4.30801 | -48.09627 | 2025-08-25 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed4f2e74-f7d5-345a-8e2c-6799113c47d8 | -5.79338 | -59.22062 | 2025-08-25 04:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba9fa542-7aa1-32d0-a625-23c66a330bc6 | -6.79455 | -44.33339 | 2025-08-25 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2930b5f3-a736-379e-9455-b06c5f0b25e8 | -7.91366 | -45.88406 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f19d8bca-9955-3595-9521-8149ef77999c | -14.25648 | -48.0416 | 2025-08-25 04:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| deb062f6-6aff-39f1-a8f3-b9f4d9854555 | -13.43112 | -47.02221 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a082a090-353b-34bb-b409-16fa9391941e | -10.81968 | -46.38306 | 2025-08-25 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70299c77-d2a3-3155-ba92-3eb661f94d35 | -8.87003 | -62.45615 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 27.5 |
| a06c0612-f620-35c9-a2e4-504991c0c907 | -6.82272 | -58.9496 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a4221db-2007-3302-bd0b-908d6880d198 | -8.05876 | -47.30178 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b992a42-1707-357f-bb73-1f92ee9e0068 | -12.74526 | -48.10867 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f868e748-a484-3cdd-9aa8-57d5777b5245 | -9.17959 | -59.60856 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90d953e8-5514-325f-8fab-bc92f4afa438 | -8.21672 | -61.39274 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d3d2d10c-b3fe-3451-8784-f962db30eb1d | -9.47526 | -57.81878 | 2025-08-25 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8916a720-b7ea-3389-b9e6-3a2a87acdda7 | -9.21081 | -60.92376 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f8c3530-5bd6-3037-a3d7-ee3bd0b5d49f | -9.47332 | -57.82961 | 2025-08-25 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 72841678-7cf1-39fe-97e4-07820548bca0 | -9.70977 | -54.97872 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85a9a19f-5e12-322f-ad9b-e73b54545dd3 | -10.87501 | -45.23495 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01f527d0-07ea-3f81-998b-b4d9bddef77d | -9.54776 | -48.1413 | 2025-08-25 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd3c29a4-1dd9-3fe7-adf0-b6044a3d2886 | -9.21142 | -59.71215 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d6f5d55-2d6a-396b-bb69-e0fbb2880715 | -9.10169 | -61.4314 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b86255b-7e73-31a3-9c66-be01aae5ec20 | -11.2678 | -44.9918 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9ab7166-fa91-375f-a782-77e92c0bb0ee | -8.77445 | -46.72962 | 2025-08-25 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1ded172-d2b8-3bac-a235-4a497c6f8ba8 | -9.20828 | -59.48166 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c64f6ee-0e95-38b5-b9d0-ab466fe1e832 | -9.57628 | -55.36775 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1485ea86-9b0b-31c7-9c1b-b60e7b1707db | -9.2585 | -59.64232 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de5a0447-2c87-36e9-9663-79cf24404843 | -11.54218 | -50.47163 | 2025-08-25 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f57862e-7a00-3fd3-9cc7-a4e6e3a2d2bc | -9.47429 | -57.8242 | 2025-08-25 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 068dc4bc-3035-3777-bc9c-d75163ce2a75 | -8.88537 | -62.44746 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README41.md)
