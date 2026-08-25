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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 312f82ff-f0a8-3891-b8a4-879782dd3435 | -10.37544 | -45.05889 | 2026-08-25 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| a578d8a5-1b0c-307c-a970-61c6caa6b779 | -7.43659 | -43.10642 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b2707637-0322-3cae-a525-54b65596e2d3 | -6.16674 | -53.50497 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eff80a91-6e42-3a48-8057-59e1fdd23aaa | -6.18289 | -55.44073 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1f2bfb46-34c6-3e64-9b5d-a461fa175f38 | -7.29128 | -45.36388 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 042b4181-0d9b-3883-8fa8-1fb77abf0b73 | -6.82311 | -58.65736 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 906bff80-8d89-3b55-9e66-36fdf296ef7f | -3.04429 | -48.98025 | 2026-08-25 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b7f7e23-fe47-315c-86f1-afafd0879968 | -8.93166 | -45.7307 | 2026-08-25 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1fcd66c-627b-3cd8-a3fc-1c217d53c86a | -6.17781 | -53.53276 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edd92dbb-0004-31a6-88eb-6d4cadc12743 | -5.79888 | -43.64499 | 2026-08-25 04:25:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d7234fdd-972e-38e2-9bb1-ceab35db068b | -9.05052 | -50.80436 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a918e38b-315b-3f0d-972d-c4869eb9d0c9 | -6.84307 | -52.50412 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b415603e-3fa3-3280-aba4-02f4725bade9 | -4.7689 | -41.79922 | 2026-08-25 04:25:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b1a3741a-d4e1-3dd9-8d41-aefa7f117beb | -8.15675 | -46.70258 | 2026-08-25 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b33fc0a-b4fa-3210-9259-81e15612554e | -7.64983 | -42.72493 | 2026-08-25 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5890b69a-1167-302e-859a-f0b8916ff22a | -3.00805 | -51.05481 | 2026-08-25 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3a49edf-1403-3584-87ef-290d3042a97d | -6.51428 | -55.22303 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04810cd7-1b52-3bf4-8491-3154dbaa64fb | -7.90256 | -46.38561 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24e9715e-2b58-3484-9c72-b8dfbeece957 | -7.27634 | -44.07732 | 2026-08-25 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 14f5bcd9-6bc1-3632-a614-98a7c16a8b9a | -7.44577 | -43.09242 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b07ab726-aaae-3569-ac97-0717f9a98852 | -8.20329 | -54.97722 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 384d8ab7-43e1-39cc-aa8a-93810ceffc6e | -10.30677 | -48.20256 | 2026-08-25 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cabcfa2-4b43-3b0f-9350-13f66b0a903d | -8.13223 | -47.51711 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36948d98-d753-3b35-b486-1f6254ba0e75 | -7.28062 | -43.00678 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1fcdd0f2-3125-3036-a9c6-190d8fe2d429 | -6.20483 | -53.49931 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c794aafb-ef2f-38c4-ab69-5fa32c469552 | -4.43437 | -43.40477 | 2026-08-25 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80089f0b-232a-3d47-9ff6-d8df921aa5b7 | -6.59158 | -49.62126 | 2026-08-25 04:25:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3ee721d-b54e-31da-929c-36b8820d84fb | -3.53739 | -48.18376 | 2026-08-25 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb8b472f-e2e7-3c36-bea3-773146773993 | -7.89608 | -46.34063 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a267db6-3e9b-3b6b-82e7-687352df42b5 | -8.08411 | -47.53716 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 639b7c35-b275-3a17-847b-03c8f16508e4 | -6.54474 | -55.08596 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9cde7c2f-d794-3a13-8561-73fc9bf11305 | -6.40766 | -51.70829 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c2174408-c60e-3743-9e8c-0fa41c4667ea | -10.37101 | -45.06543 | 2026-08-25 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 29048588-bc83-308e-91c8-7baf1a98fe2b | -6.62614 | -58.49571 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b84025c8-2d2f-37ca-bc10-bc061e19b069 | -6.78097 | -42.77453 | 2026-08-25 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 01783190-75ab-319d-9239-2be77915ef6e | -8.08439 | -47.51355 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a2f308e-c80c-35c3-8879-ba24965c0971 | -9.64041 | -48.32674 | 2026-08-25 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3417a91-13da-360c-a686-d427ae652bcd | -7.15116 | -44.50993 | 2026-08-25 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c11aabf-b2bf-3d81-b45f-cc27989fdaf3 | -9.65164 | -48.32454 | 2026-08-25 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fcb2e0c7-d3ae-3156-b3ba-ed9f2f18c227 | -6.63482 | -58.49557 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| bddba64b-9e42-3e75-9393-b244373c190e | -4.65466 | -43.12973 | 2026-08-25 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8aeaa4e3-4de8-3148-85bd-814f9cb2f14f | -6.17723 | -53.47528 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3f173b6-592c-369b-b615-9b705ae91d12 | -6.35899 | -54.75909 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f71c9cc4-903f-3b66-8c90-64510afa5aa1 | -5.91888 | -43.6385 | 2026-08-25 04:25:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0e07c899-27f3-33f0-8f1a-3fb9b1dd97ca | -7.25175 | -49.85979 | 2026-08-25 04:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d706f109-b514-362e-9707-f7ef924dccc7 | -7.38475 | -45.99008 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a0e2ef6-635a-3dde-ae33-1b8d376dabcc | -7.34901 | -55.66468 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bdf2c6b-8777-3fc0-8b40-f82268eca1ce | -7.28077 | -44.07077 | 2026-08-25 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 587940b5-c993-3762-899c-cfae700f9359 | -6.80997 | -42.66796 | 2026-08-25 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8d0205a1-3d76-3c54-b48d-077a4449f4df | -4.43716 | -43.40881 | 2026-08-25 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3a5829e-9349-3048-aece-5a41e564c312 | -8.61358 | -47.15101 | 2026-08-25 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6f65173-66ad-388c-ade6-7153d096562a | -7.06632 | -45.00466 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff98a320-d9f6-3ea2-8010-5962575e0b48 | -6.33805 | -54.74767 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff233d07-5b1c-3cb6-b201-0b649a490911 | -2.5049 | -51.81806 | 2026-08-25 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c29fdf2d-48d5-3c22-a2e7-4c6eaaf105b7 | -6.14835 | -57.93937 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5e18be9b-f6b3-328d-9235-14dea86163e6 | -8.92889 | -45.74813 | 2026-08-25 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae01cb1e-72cb-36cf-88c0-3eecaedff01a | -7.25725 | -45.85471 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8ef2a176-bf4b-3a2a-aa87-7a45bdfb8e16 | -7.25155 | -45.37884 | 2026-08-25 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ae9149ef-3cea-362d-9fb5-352a00e000af | -9.05119 | -50.80043 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 139040a5-ccc8-30f0-bca4-0bbe0a63f186 | -6.63361 | -38.73638 | 2026-08-25 04:25:00 | NOAA-20 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0eb4487-d155-3f1c-81d3-1157abd5c4f7 | -6.3333 | -54.75154 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d72d6eb-1b81-3693-b110-2ae69ec1e07f | -9.46269 | -40.32822 | 2026-08-25 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 260ceea7-a09e-3ae9-bea3-0dcb21a76e02 | -9.065 | -45.20995 | 2026-08-25 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7278090d-d55b-3c2b-ac71-f7d78eedd7ca | -8.06996 | -44.64819 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a9f76fcf-d5b7-307a-8285-a9e9d8fe3849 | -8.76598 | -45.78949 | 2026-08-25 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e214b38c-44f0-35cd-9045-379cded62b48 | -6.84218 | -52.50912 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13971ed2-6c99-372c-ae6a-46b6241f02da | -7.49551 | -55.35956 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95fea1a5-c712-3c2a-99f4-4fb714f29494 | -7.25837 | -45.8477 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b178f08b-7cdb-373c-a12a-c0a3bcced5c5 | -7.30195 | -43.00148 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fe821ba3-0a86-3de0-b44d-2e32a7563621 | -7.25337 | -45.85768 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c4e250f3-af1e-3fd6-91bf-880aae331916 | -7.48384 | -46.09307 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96e820df-186c-3f22-a411-a10ec4fb9afa | -4.21792 | -54.56456 | 2026-08-25 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eefa29eb-2ec7-39fe-8a43-23ec3d1d418b | -6.17968 | -53.49162 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c138b17-6e38-3ca9-a5f8-3b65ad27400b | -9.65584 | -48.32111 | 2026-08-25 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a9b3634c-c9b8-3266-ad12-ead5095a36db | -7.43661 | -43.0833 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 52112685-b72e-3a1b-80e5-db3d5d7ecbe1 | -9.6928 | -46.0503 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fd883a8-1a74-3b44-bdb4-db5830a6899e | -10.36879 | -45.05783 | 2026-08-25 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 0d39d87c-7559-3646-a3d0-4674709a3c89 | -7.19366 | -42.7529 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 122c4bbd-cee4-3b8d-88de-acb2733d277d | -7.44519 | -43.0962 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1ef6814e-0937-382b-8cfa-4cb12c24f022 | -7.30126 | -43.00998 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e8dd9b28-bcbc-329a-a2ec-04cec44d127c | -4.12669 | -49.45501 | 2026-08-25 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ffa5a2db-c2dc-3fee-bd55-9ad3d58af4ab | -7.89054 | -46.33241 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 28ac54e3-8f60-3cb1-a539-7215aa0ef7c3 | -7.2554 | -45.3759 | 2026-08-25 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e59a798-f76a-3eb2-9077-2854aa8db502 | -8.5691 | -54.87703 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20423ebb-80ee-304f-a498-db6e01c9a60f | -5.75743 | -48.67369 | 2026-08-25 04:25:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 26b8db27-cfac-36db-9129-73f56e43b01a | -6.83362 | -52.50216 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| effc38f5-66c7-3702-b816-d7e7dd1c4d39 | -10.05415 | -48.45507 | 2026-08-25 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e198ffe2-a29c-375e-b94b-cb128b3cb62e | -6.39122 | -43.83512 | 2026-08-25 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9723d1ef-6bdf-301d-b847-a3ad4f48dd44 | -9.97884 | -48.32005 | 2026-08-25 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 12102b8a-a4b2-3a3a-a26e-58cb231ed6df | -6.14615 | -57.94514 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f5629621-a5d2-369a-92dc-63d2105207ff | -7.28025 | -45.36923 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71328bfe-373a-3964-9af6-b8b414507c36 | -8.0528 | -42.04788 | 2026-08-25 04:25:00 | NOAA-20 | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f74673b7-0f5e-30b3-8f94-4ed2dbacd597 | -7.13401 | -42.79478 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0150ffbd-d61a-3057-ab56-ace727eb971f | -9.97118 | -48.32271 | 2026-08-25 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e24e9c54-191e-33a8-b0d6-e639067b5eb4 | -8.08101 | -44.64278 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b949e04f-66ed-36b2-9f7d-f31e2181dd18 | -6.80775 | -58.66169 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a0a45429-dd89-3cda-aa3c-adf6429b16f2 | -7.27967 | -44.07784 | 2026-08-25 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3bf5cf4-a058-3d10-9a63-c1fdc7479d76 | -6.35141 | -54.76924 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16b15163-3138-3b04-9585-12e6ef4c9b1c | -7.76029 | -46.15209 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80c94ad0-91a7-3cb5-b874-b37c5980fc5e | -5.66827 | -44.41449 | 2026-08-25 04:25:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README32.md)
