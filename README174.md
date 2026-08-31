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

## Dados Diários - Página 174

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2dcdfca-8435-3f9a-b7fa-748fdf48f022 | -1.15126 | -46.45462 | 2026-08-31 16:52:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| a3ddf97d-3d14-3850-904f-257a68994363 | -4.95997 | -55.83022 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 11af874f-287a-302d-8222-59956aa4f93e | -1.28732 | -47.93737 | 2026-08-31 16:52:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa68df7e-94d8-3de0-9ebf-b7312f5c786a | -5.86358 | -52.08235 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 274c70af-6e36-33ed-8d75-b7d613619439 | -3.57159 | -55.41493 | 2026-08-31 16:52:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8baddeb7-87de-3e53-9060-0448861fd9ad | -3.4492 | -47.26853 | 2026-08-31 16:52:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f7f722f-0e93-3b08-a116-5ae438138ea6 | -5.57634 | -60.2298 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b646264a-fd17-3073-9055-156ac2b0d7ab | -2.64525 | -43.44956 | 2026-08-31 16:52:00 | NOAA-20 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 2e5d8484-4504-354d-8085-80f03a816e2c | -5.85234 | -52.07986 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 61225343-a418-342e-937e-3aec49adb39c | -1.15342 | -46.76741 | 2026-08-31 16:52:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 58af1516-83b4-30f2-8350-e6774e1040d8 | -1.20493 | -46.76466 | 2026-08-31 16:52:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| d94cff0b-62c9-3a7d-9520-033a9406ff53 | -5.9094 | -52.39298 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 22ce82d4-6d75-3532-a5f4-2777d9e9b12a | -5.96236 | -57.67606 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f07619a2-6717-359c-9eb2-bd4c8ffd222a | -6.35449 | -55.86314 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ff56ede7-2213-3fec-8879-57eac9c94856 | -6.261 | -53.67725 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 989873cc-019e-33b9-ada5-fe3f7abaa04a | -3.26363 | -58.23742 | 2026-08-31 16:52:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 5f7d91d2-122f-3537-b089-920bcdf4a852 | -4.90511 | -43.45935 | 2026-08-31 16:52:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 181db58a-a5e6-3b4c-907f-a6b517492900 | -4.64901 | -55.8541 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 865207af-502f-3406-8944-27e5cb72a9ed | -6.21939 | -53.58351 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 85edeecc-e6d1-3ca2-a48e-a5a44284127e | -2.36963 | -44.44719 | 2026-08-31 16:52:00 | NOAA-20 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 57374922-0af3-3736-a188-ed3f1e540e72 | -6.41327 | -54.7606 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7842fd33-4446-3c77-b2f4-48e3f97a7076 | -7.29693 | -60.57795 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 9790d0e1-cb16-3e93-a301-fcd73498f04c | -5.85589 | -52.07935 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 96cc9526-bfb8-3735-8883-18a8a74cf2e0 | -2.26854 | -47.86988 | 2026-08-31 16:52:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f0738ea3-9e4c-3b3e-86e4-c578726b0c1b | -5.5698 | -60.18107 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5fad3943-1db2-3108-bbe7-e01c0849e0eb | -3.34292 | -59.42441 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 83a8eacd-4361-39f6-bc65-9c00d36461d6 | -7.29763 | -60.5832 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| be02fdb2-0865-34a4-b28d-67b28d3b7b71 | -2.56599 | -47.19968 | 2026-08-31 16:52:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8ce2e72f-37d4-3736-93e5-8ce66c022ff9 | -3.34396 | -59.43162 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b41ed58d-242b-3bcc-8792-ceb0c0d98361 | -5.88596 | -52.06211 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| d9fd15bf-a403-35fb-9e74-45b688c076e5 | -1.82664 | -47.75294 | 2026-08-31 16:52:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54e5cc7e-4f79-3793-bd50-db8856044656 | -1.85491 | -44.89725 | 2026-08-31 16:52:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 104ecb04-bab8-3be1-af4b-d857c310b281 | 0.18659 | -60.49983 | 2026-08-31 16:52:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 58f9c84e-5ec4-354c-8cda-54e86dc4c996 | -7.34165 | -60.59697 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| fbe31eba-644f-3ee0-9511-9b7af8c41679 | -4.44044 | -55.44681 | 2026-08-31 16:52:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 35aba16b-2c9a-307b-abab-3b9f9182354e | -0.80501 | -49.20158 | 2026-08-31 16:52:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d8e53c54-3d92-3d31-a345-96dd427a7fc7 | -5.94987 | -57.68378 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 76dddf19-069f-3a73-8608-10c5250b42a0 | -3.38726 | -59.38116 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 80f0433e-a601-345b-ac8b-7f2277500791 | -1.95213 | -44.59848 | 2026-08-31 16:52:00 | NOAA-20 | CEDRAL | MARANHÃO | Brasil | 2103109 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 7e5d6cf0-0e97-30b4-803e-151b523e2b5a | -5.85944 | -52.07886 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1b7e121b-dfb2-39bd-94f3-39785cb38c74 | -3.76893 | -59.3329 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 94ab16ec-f57a-3047-b518-7d1e3cc416ec | -7.3126 | -60.56963 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| fa14b263-face-34d6-b55e-dc3440e10e53 | -5.9643 | -57.67574 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e87ca45b-46b0-38ee-8c44-9adc935b3521 | -6.21868 | -53.57869 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a4c68aaa-8d48-3e5b-8f1b-96b13a5281a4 | -5.86121 | -52.09085 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c0259418-a494-38ea-957b-16bca3b6fcfe | -0.22746 | -49.08715 | 2026-08-31 16:52:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0c87561b-01eb-3d17-874b-86aa1fca2750 | -6.31355 | -61.93168 | 2026-08-31 16:52:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 34a82204-19e0-3f7f-b448-a79fb18c3d0e | -2.28797 | -49.09144 | 2026-08-31 16:52:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2af7669b-efb4-3c11-9bc1-97b440d65762 | -3.77807 | -44.39367 | 2026-08-31 16:52:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 29adc517-0f46-3a7a-8356-2dc9f568dd1b | -4.31145 | -49.09543 | 2026-08-31 16:52:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| cf4a8f33-4c90-3aaa-84de-e5eb94c70bcc | -5.72431 | -53.72524 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b295fe3d-2742-3c4a-ab84-5b3da196907b | -1.70102 | -45.79587 | 2026-08-31 16:52:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5023a3c8-2e04-391b-9949-fe25966ba346 | -7.30317 | -60.57684 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| d59c1fb1-1863-3a32-8cb3-868b78619c12 | -5.95071 | -57.68973 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| a061b7c8-c1fe-32e7-831f-9d14a0829845 | -5.25936 | -55.91009 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 245bbeb0-01c6-30df-bfe7-68fea24c608a | -5.28205 | -47.69028 | 2026-08-31 16:52:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 571aac67-0247-3362-9de1-deea8b513f9b | -7.30249 | -60.57171 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 1ae9367d-b232-3d64-bef8-e71b66748616 | -5.94603 | -57.69336 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 33c38d95-e408-3056-a673-7fda9335b9db | -3.42293 | -43.37897 | 2026-08-31 16:52:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 22c62446-a4df-3146-a39f-5f924781012f | -5.24977 | -55.90665 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 2018d43b-6c46-35fa-aa41-bd7fdd37bcc2 | -6.25005 | -55.43142 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 888019fd-76a6-38b2-8a94-4826f5401ee2 | -3.66091 | -58.90791 | 2026-08-31 16:52:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8ea354bc-eda1-39d2-adcd-a6358dded75c | -6.2148 | -53.57921 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6352b570-883d-395a-9376-4ffeee98078f | -3.32251 | -44.72088 | 2026-08-31 16:52:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19211834-e45c-3782-a76b-60f40ce54d73 | -3.04205 | -57.4087 | 2026-08-31 16:52:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 6608955c-19ac-3cbd-9ada-0f5de536f67a | -7.19003 | -60.66675 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ef467a47-cdac-3ea4-8f07-e4cfc2c6c006 | -2.19143 | -46.80147 | 2026-08-31 16:52:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd383fe8-12d2-364f-a246-97316ecdb5dc | -5.96519 | -57.69701 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c02d7b77-5a42-3b20-b2a4-505233d1297a | -6.9439 | -59.61972 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c689ff0a-d08f-35e2-9a56-8a5000cc5f05 | -4.96364 | -55.85622 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| e8383fe7-68ed-3f55-b8a7-3894a56e1a57 | -5.95541 | -57.68617 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| cd4d14e2-8ba7-3b58-bdcc-aa0ec316b1ce | -3.76342 | -59.33369 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fcff1f1d-75f4-3d72-af7d-470f25f688ca | -5.8748 | -52.15826 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 193ddd68-68fd-3f82-8ce4-0d9b0c27f4a7 | -5.88005 | -52.07113 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| e1d67d9c-b28f-3b8c-aa64-853da6444a22 | -3.41121 | -61.34013 | 2026-08-31 16:52:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 754023fd-21ba-3746-91d0-a4e3661b6a4f | -5.98353 | -53.61185 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9fa1c587-17b4-35ea-95f7-2ea51181d9c7 | -3.90203 | -57.49962 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 055f0e8f-eac4-3652-b71b-e85038cb4622 | -6.83138 | -59.57369 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c11c8e7e-6c26-35d9-973f-0bc3cf2d2981 | -5.87895 | -52.16172 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 91f079b3-2d11-3425-a64e-28673043caa6 | -6.29521 | -53.57975 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 625ab20b-a43a-3243-9957-b406eae08e8d | -6.12391 | -57.6925 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8236d4c3-9c30-3dcf-92b8-6f68fa363944 | -5.91362 | -52.39661 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| cded9a97-f0ac-337c-9893-3e9ea3b6fa07 | 1.37299 | -50.7477 | 2026-08-31 16:52:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d816ae7b-fd8e-3b00-9305-278607bba4ed | -6.20705 | -53.58028 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f05d6665-a68f-3f48-8555-f37ca88ed3b4 | -5.88074 | -52.14918 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| be931668-c55f-3208-97f8-6623c4672962 | -6.10581 | -57.86626 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 56f1614a-d68c-3aa2-bb1e-58434c97a97f | -5.58354 | -60.23783 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 997be05a-11b0-38c9-a79c-b63416418064 | -7.22147 | -60.66194 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0a4ad512-f747-3e4a-9350-f96c469f9600 | -6.0783 | -57.65108 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| efb8d6d9-2370-3aa2-b8a3-15fb2201ea76 | -6.14137 | -53.53534 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a9ba83a0-d34d-33be-890e-8a789c05d22e | -5.25104 | -55.91544 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 2b721638-8a32-32fa-9a20-0181ae7dbebf | -5.9639 | -57.67292 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3f49bc48-fb70-35cd-afa5-ef4cdceb1ef6 | -6.3037 | -57.80024 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| dd636d7c-5dbe-3267-8229-907baf734fed | -6.59907 | -58.61284 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 617839d2-ae34-327f-9fd4-5dec2754a1aa | 0.1872 | -60.49602 | 2026-08-31 16:52:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 52048441-540c-3fd3-add6-4581af6a0071 | -6.86525 | -59.47617 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| acf6274e-9b85-3d47-8617-1e495e08e857 | -6.29591 | -53.58461 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 2479c9d1-24fa-3352-8768-169fb917aaf5 | -1.53244 | -45.41235 | 2026-08-31 16:52:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e5f5446f-5c16-3cd5-a237-0b3c76dbd89d | -6.26155 | -53.64937 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8c09340c-8f8a-3c32-a4f3-b0c7bf96d13b | -7.19066 | -60.67149 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |


[Clique aqui para ver as próximas entradas](README175.md)
