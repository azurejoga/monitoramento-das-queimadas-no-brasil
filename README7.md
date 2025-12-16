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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bce35bfe-e78f-3856-8c47-cc4c86617cc8 | -4.65604 | -47.81348 | 2025-12-16 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8d5c7bd-b435-3f54-805d-1b012b980757 | -4.65685 | -42.40551 | 2025-12-16 04:23:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 64a7db1e-c32a-3ab9-9f75-ec8b1945464b | -5.02613 | -42.65466 | 2025-12-16 04:23:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 877f5126-01e2-3ca7-8e11-aca1357e51a2 | -2.79408 | -51.41154 | 2025-12-16 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbac4fd2-bd0b-3bb3-92d9-4748d3be296d | -8.08381 | -35.24833 | 2025-12-16 04:23:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 95a4c8a0-1834-3328-a94e-2bf994a58c70 | -3.65728 | -47.55431 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1d11592a-76a9-3bb9-bd86-144b7f02bd8e | -3.94301 | -47.00301 | 2025-12-16 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 131a80a0-f39a-3dfb-a76b-8a8e57e54d1b | -3.95968 | -47.18297 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c9bf4f9-3a9b-3c02-a5af-09ada0e0a4d3 | -3.35504 | -46.86086 | 2025-12-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3217bed-f6e9-3c34-8800-9741ac9621aa | -4.07571 | -43.69011 | 2025-12-16 04:23:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2780e7f-3166-344f-aa70-eaff16d11dc7 | -5.94113 | -44.45924 | 2025-12-16 04:23:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 371b54de-80eb-305f-a396-45d3658ff576 | -5.39477 | -44.68511 | 2025-12-16 04:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f4a944f-79e6-3ead-8264-d96e29ba08dc | -5.19215 | -44.29545 | 2025-12-16 04:23:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 962102fb-3048-3970-accb-827aaae9e11e | -4.08236 | -43.69114 | 2025-12-16 04:23:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5b12c4c-a2e6-3fef-ac3d-2e75e92a525f | -2.80521 | -49.12523 | 2025-12-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 191c4a81-9c17-3a29-a934-e48b91188679 | -4.63119 | -47.94326 | 2025-12-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02188ce5-de8f-3e05-9618-30e3315befdf | -3.02495 | -49.05092 | 2025-12-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e87fa58-336c-3f63-95d0-fa5e2f844cfd | -3.6595 | -47.55721 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 400b8f45-e5ec-3b5e-b8bc-7506df207cb0 | -4.65801 | -42.39805 | 2025-12-16 04:23:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 35d56a42-39c0-3933-9d06-8b44bc362a3c | -5.94357 | -44.89311 | 2025-12-16 04:23:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 076d513c-a323-3d5c-9859-e4a137b0591a | -5.11265 | -43.29009 | 2025-12-16 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77416e99-d4fb-3822-b05b-7e3945a36961 | -4.66087 | -42.40231 | 2025-12-16 04:23:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2df4ad8b-4e2e-3bbb-987c-3100a3f1fca4 | -4.75866 | -45.78794 | 2025-12-16 04:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d5e29ca-afef-3e8c-b246-ed05364ed575 | -2.78931 | -51.41073 | 2025-12-16 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf2aa37e-e1c2-351b-80c4-4bbd09277a49 | -2.80871 | -49.12947 | 2025-12-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 96b12f5c-d66a-3253-b012-fd00f89b10d2 | -3.83515 | -44.82927 | 2025-12-16 04:23:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ba78195-c728-39f2-a375-3dea99b71806 | -4.20243 | -44.49681 | 2025-12-16 04:23:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea70b8a8-5bb0-34ca-8014-5d827ab71082 | -6.45243 | -39.7902 | 2025-12-16 04:23:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ea2fd84c-2568-3347-b4e8-1ad773c7ab1c | -7.14455 | -40.09729 | 2025-12-16 04:23:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c054e276-2b31-3646-b02b-cd3e036e8ab4 | -5.59023 | -44.88311 | 2025-12-16 04:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dcb91dcb-3fda-3abe-9089-3cb8d852b231 | -4.24917 | -39.23439 | 2025-12-16 04:23:00 | NPP-375D | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 23c01f1d-fd41-374b-ba7d-7cda85150d7e | -3.17986 | -48.02837 | 2025-12-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2c04cce-f7a8-3950-8ac2-95fe2441d07f | -5.08633 | -37.62791 | 2025-12-16 04:23:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1c43252a-06ae-3b39-9e59-894f937e0666 | -5.01883 | -41.27433 | 2025-12-16 04:23:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 25dc63be-647a-3c4e-be31-897159635391 | -3.93946 | -47.00244 | 2025-12-16 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da283f2c-d17e-359f-9633-28b109d1d030 | -4.07289 | -46.1445 | 2025-12-16 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78ce5c99-d7de-3c99-8c9e-f382d0efeedf | -3.6602 | -47.55293 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 80541dbf-ecf4-352f-ab62-a855503d3ff6 | -3.2983 | -48.82547 | 2025-12-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72a1a78f-9c46-3abb-a12b-1ad9ad85ba59 | -3.03 | -47.09138 | 2025-12-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a996816-a7c3-3936-8204-b75597ca23d8 | -2.92644 | -48.23179 | 2025-12-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5795a1ff-4422-39ce-90cc-e876bbc5301e | -3.15407 | -48.13838 | 2025-12-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63255584-1696-3cd0-beb1-7b800bec3a16 | -3.65147 | -47.56021 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56c488ce-55ee-3dad-b1d0-dbf660ae6282 | -4.75073 | -47.50712 | 2025-12-16 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a21236b4-0e63-3d56-a1f5-28df8d829e44 | -5.75992 | -40.50121 | 2025-12-16 04:23:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e0be87e9-24f3-3e6a-b194-0d42e523c799 | -3.65226 | -47.56222 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8883f1c9-1350-3da5-b4c7-37ca3aa31bbd | -3.02379 | -49.05803 | 2025-12-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1c922ade-0708-3979-b44f-125fbe903940 | -4.75346 | -48.23731 | 2025-12-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24c3a744-b657-3f2b-b47a-0592d7a3688d | -5.48732 | -45.38081 | 2025-12-16 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f164725-6bb3-3920-a21b-69e5867d2ce8 | -3.56485 | -47.17464 | 2025-12-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1ed405d-8905-3c42-9baa-dacd5172fec7 | -4.63391 | -40.55795 | 2025-12-16 04:23:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b247d888-6645-33ef-920c-3bb6bde516d8 | -3.02842 | -49.05514 | 2025-12-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 799406a3-e87e-383f-af3f-1d597f552982 | -4.07904 | -43.69063 | 2025-12-16 04:23:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| afe5213f-cf2a-30f6-be17-423f8bbd8169 | -3.80098 | -49.03312 | 2025-12-16 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea849de6-5e5f-3d23-8953-4b01aa75d515 | -4.9049 | -37.42941 | 2025-12-16 04:23:00 | NPP-375D | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1cf8b676-aa24-3772-b613-38dd76b16f6a | -3.6566 | -47.55859 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dfce4f6b-8f71-3d4b-8bb0-a7747a8bd339 | -5.02217 | -40.35899 | 2025-12-16 04:23:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f14521b2-ff8f-3b19-958f-78831838a755 | -5.25132 | -44.36831 | 2025-12-16 04:23:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bac5b48c-9eba-3c25-a6ee-a4bb31caee1c | -3.85064 | -41.93423 | 2025-12-16 04:23:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d26abae5-8ae8-31ee-8529-f313e5b61988 | -3.66026 | -47.55924 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 49a43bf6-43e6-3994-ac21-82c1dff405cc | -5.1132 | -43.28653 | 2025-12-16 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| afca1be6-7b5f-3b7e-9541-04e6dc4e42e9 | -4.35502 | -46.14653 | 2025-12-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dfc31fb6-6638-34d3-b345-95a84142ce2e | -5.94412 | -44.88965 | 2025-12-16 04:23:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35531baf-4b80-3fd7-bf34-737e6d55d8d2 | -7.14658 | -40.1664 | 2025-12-16 04:23:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b258322c-3046-39d0-b496-10d1b73a210c | -3.83848 | -44.8298 | 2025-12-16 04:23:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ddb9e43-4695-37a3-8b15-ffbf4805d64e | -4.90576 | -37.43249 | 2025-12-16 04:23:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 864dee23-e8e0-3dd4-82d2-6486dfac2f24 | -3.95118 | -47.18996 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a75e3ad3-8037-3aa6-ae44-c3ba4f0581b5 | -6.33109 | -46.32962 | 2025-12-16 04:23:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4d00c8b-09f2-3213-9411-3bfdd209e366 | -5.02182 | -41.27907 | 2025-12-16 04:23:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b2403403-03f3-3f65-85c8-3ce161f7c2a9 | -5.08643 | -37.62632 | 2025-12-16 04:23:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ff99f74c-0c82-32a2-9025-e60a3f122d82 | -5.59355 | -44.88364 | 2025-12-16 04:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 84a1f301-7f12-3b88-883b-20d6543784b4 | -3.35149 | -46.86029 | 2025-12-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fda6503-ce85-3c5f-86d4-8f7fe5bb4a86 | -4.90648 | -37.4277 | 2025-12-16 04:23:00 | NPP-375D | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7ba7f880-d458-360a-bfe7-1b3b8a259095 | -4.07849 | -43.6941 | 2025-12-16 04:23:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5f806a2-44fc-354a-8d0a-3ab4d4f673bd | -3.02437 | -49.05446 | 2025-12-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ccc962b-5508-3768-9380-5696df1bc3ab | -3.65654 | -47.55235 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f2a2254d-ef10-3c63-bbf2-ae60c4c827af | -8.08431 | -35.24449 | 2025-12-16 04:23:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9b21ee3f-9786-3df3-be2e-3ab201b29cf5 | -4.66029 | -42.40604 | 2025-12-16 04:23:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f6105996-1de1-3ecc-8dc6-0967137ca36d | -5.11602 | -43.29061 | 2025-12-16 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2b733b5-5aa7-3a21-9878-09799ee087ce | -4.11643 | -47.29499 | 2025-12-16 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c1f4fad-e3a4-3f4c-a907-064c7d43fd48 | -5.11657 | -43.28705 | 2025-12-16 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b93883b-8389-329c-a2fe-e61b14a7dab3 | -3.34669 | -46.82269 | 2025-12-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7423fa25-06ae-3eb6-89bc-55907d2848ab | -5.28107 | -43.64243 | 2025-12-16 04:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cf6102a-cc36-30a1-99d6-d58a05095206 | -3.40122 | -49.214 | 2025-12-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c8e86eb-ea30-33c8-83c3-2d1f51d570f3 | -5.27772 | -43.64191 | 2025-12-16 04:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce7f4a60-7082-312d-ae68-0672f0f6bbf8 | -4.40917 | -42.33434 | 2025-12-16 04:23:00 | NPP-375D | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5399ab61-fcd0-385c-b38e-08362e22f133 | -5.59078 | -44.87965 | 2025-12-16 04:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 444a5432-3100-3ed0-843d-1cca135416ed | -3.65592 | -47.56287 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ece064fe-34b7-3581-a81e-bae0e916124e | -4.25567 | -39.24633 | 2025-12-16 04:23:00 | NPP-375D | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| beeaba17-6d64-354a-9fbd-43ae031c703a | -5.5809 | -43.7568 | 2025-12-16 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae0d8286-2ff8-3f4c-8f0b-8aeb189c550f | -7.41362 | -39.46498 | 2025-12-16 04:23:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 20b7902d-8057-35dd-af17-53e93d076350 | -4.6319 | -47.93895 | 2025-12-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b99bef9a-85c2-3664-8e1f-89f169a41513 | -3.95052 | -47.19401 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96004633-2e37-3058-ab35-d8e2c27b9639 | -4.65743 | -42.40178 | 2025-12-16 04:23:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b315d60e-3564-3d2e-8cfc-e357d261f9aa | -3.18365 | -48.02899 | 2025-12-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f358033-6f55-3740-b22b-001186e14b86 | -3.65795 | -47.5501 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fea2ff0-3a9a-3424-80b2-9ae91cb903e9 | -5.19547 | -44.29597 | 2025-12-16 04:23:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc55a212-496a-3c93-8074-0254f3bc21ab | -3.65361 | -47.55372 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06aecedc-1c14-3897-8f83-91e78b9e9355 | -2.80463 | -49.12881 | 2025-12-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb31f757-ffad-36f5-82b9-832695a274a6 | -4.99244 | -44.23169 | 2025-12-16 04:23:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 433022f0-fd56-3eaa-9916-140e0d09b60a | -5.1927 | -44.29199 | 2025-12-16 04:23:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README8.md)
