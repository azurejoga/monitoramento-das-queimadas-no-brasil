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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bef6a66-1a7e-34c0-8fd1-4b59c559dfa5 | -7.99449 | -46.34562 | 2025-09-08 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9a6ed46-8306-34ff-b438-02cdcb0a43d7 | -5.25201 | -57.12641 | 2025-09-08 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 41c5bee7-6865-36cc-a04b-b7255443897c | -9.55367 | -53.59478 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 512840c7-f8f9-323b-becb-ed8de16a50c4 | -5.21895 | -43.70217 | 2025-09-08 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4d6fbd2a-4d9b-31d5-85a0-903244b865aa | -6.92243 | -44.34412 | 2025-09-08 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47ec20ba-19c6-3b3e-a7dd-86784abaac9a | -5.94673 | -45.74767 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8ea72e8-b6ff-3ab2-ba98-fef37acde292 | -7.40774 | -61.63268 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ef079928-4e5b-39c7-9f5c-1ac48c1bd5d6 | -9.96405 | -51.19631 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ff721018-b0bd-3143-aad6-e8f5de560c4b | -9.05168 | -50.46576 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 90ca943d-cc74-3aa4-aa32-37a1b35f2ba2 | -8.03752 | -44.05917 | 2025-09-08 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d539c6a2-b5c0-3d77-87e6-6cd3a818a8c0 | -6.38806 | -42.60705 | 2025-09-08 04:51:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c5c627ea-8e9f-3521-8809-1c471dd255d6 | -7.75659 | -50.72927 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 123d692b-773f-3eed-b8c5-129bc1f25325 | -5.28934 | -43.43536 | 2025-09-08 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b7d4202-25ae-3ae9-b151-93fde6cf92f6 | -3.92568 | -56.06233 | 2025-09-08 04:51:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d48a6b9-cd3e-3eca-9be2-ee9f09355d29 | -9.46115 | -56.04765 | 2025-09-08 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e334c4aa-9a8e-3de3-9cba-e4f80beb5483 | -8.46505 | -45.02837 | 2025-09-08 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff4f446b-a5bb-3c5b-969d-81e54a0c4d71 | -9.62773 | -55.36728 | 2025-09-08 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e867248b-4ae0-3606-9635-b93c687fdbd5 | -6.1979 | -43.60653 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7227d951-a5ef-3537-bf0f-60ab5aeabc13 | -8.61656 | -40.19885 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5c444e14-6586-33f8-acf3-661f9543c03a | -8.18774 | -50.14574 | 2025-09-08 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 514b66fb-c8e9-3fc5-abdb-48b9c7d5fd27 | -15.83231 | -52.30154 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc2cf764-db58-3ceb-b5fd-e8f11d9adf0f | -13.27174 | -51.77864 | 2025-09-08 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e05d54ba-d8b7-310b-837b-8182682dd0d4 | -14.28068 | -48.94368 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c7831e9-6a1c-3f53-89f0-3dd266123cfc | -14.52737 | -53.97485 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5dfa3a4-7b96-3520-8800-034cae19546b | -16.54029 | -45.10676 | 2025-09-08 04:53:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 573a702c-925c-3d30-b37c-6d8c21f76ba2 | -15.84089 | -52.26637 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f3886dd-c153-3c86-a2c4-55b3d3605a09 | -15.1223 | -52.35843 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2fdd0d54-ddcd-3de3-975d-c5f0954335fa | -13.28811 | -51.74036 | 2025-09-08 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ab3f4cf-8390-3136-9af5-2dec84d5675a | -11.21391 | -55.01235 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f5d8997-8b4d-3b8f-a736-670cccc46016 | -11.1972 | -55.00965 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1fc96f75-d5ab-3bbb-a9cc-0924cee6c470 | -12.94437 | -54.76838 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3903000-a78a-370f-82e1-09c293dd43f4 | -11.03003 | -52.03621 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a5914409-afaf-394d-bd3d-a53968e4bbdf | -11.03398 | -52.03302 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18c81251-372e-3099-98d8-38c56aba1771 | -15.8301 | -52.26198 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20f7589b-1f85-3581-a52c-4adb63c012fb | -12.93001 | -54.77328 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a271ae5-f5b8-3a0c-b5e9-0da6a28540ea | -11.41071 | -50.38351 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 91a24b06-b59b-3656-b844-ff07f73e1fd0 | -10.08757 | -59.16534 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abe02cec-1a9a-3d06-be64-00c4c1ff67c1 | -11.11074 | -52.05968 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04c43736-5ebc-3fd7-bf3f-43aa916b0687 | -12.47511 | -53.83606 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6498b2d8-e1b4-301b-b1a9-f00ba8a85e20 | -17.57597 | -44.54469 | 2025-09-08 04:53:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c45bfc3-642b-31d3-8e2e-584373079b96 | -10.42809 | -59.60575 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92487dcd-9e37-3dc8-96ef-b77ee6c40b78 | -16.33787 | -52.92768 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 53687004-1434-3c9a-9f76-a098e82e5694 | -15.82898 | -52.26971 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0c0ec929-8aea-335a-a3e1-c9967c563aa9 | -9.62314 | -64.2062 | 2025-09-08 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db2741a5-64bf-3a8a-a51c-533e7743cc92 | -11.20504 | -55.00355 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dd743680-06ec-3b4b-99fb-dce84ffa61b5 | -16.4171 | -47.8222 | 2025-09-08 04:53:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 698884b4-5714-3e58-835c-a3ca0b66a09e | -14.71202 | -60.25521 | 2025-09-08 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a06786b2-2936-3f05-8114-9a2160aa7c1f | -15.83076 | -52.28208 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f2aa873-4167-3f32-8a2a-071acd112114 | -12.19697 | -53.91706 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d6884f0-98f3-3738-9bbe-c0e759a25c05 | -15.74377 | -53.59729 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9e5f6e9-1f6e-3c47-af76-23ea182a4543 | -14.51074 | -48.79921 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f2c54d1b-08b7-3bbf-ad7c-8e6e63ddb122 | -12.63225 | -56.97058 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 657cf1f7-5dcf-3844-bc39-1c71564c3f8c | -13.8128 | -46.28564 | 2025-09-08 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e3fbeb9e-df1f-3e86-b74e-1944a4908f24 | -14.22219 | -53.34687 | 2025-09-08 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9670bcda-7056-371b-8ad3-7779253699b7 | -14.80976 | -48.1782 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1452dd3d-1b19-3190-a471-3287ad67a643 | -15.43033 | -49.91896 | 2025-09-08 04:53:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bff69d68-bfc8-3abf-ada6-c0b416f1c042 | -12.87204 | -47.97959 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f89bb8f-5c25-34f2-8805-d434d01166bc | -16.33844 | -52.92375 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fb8a9e8-78f9-3fe6-a3b5-6b29301c0677 | -8.88315 | -64.22146 | 2025-09-08 04:53:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f9b1b641-234b-3ca3-b0f4-6dca8e38f8dc | -10.8852 | -55.71714 | 2025-09-08 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ef0a937-463a-33f4-ac39-dcc22c2048c9 | -15.96589 | -48.11 | 2025-09-08 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2c5b6776-4d00-3c58-b5ca-a1d518cfaa55 | -10.3499 | -57.50735 | 2025-09-08 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7511803-f0ce-364b-807a-8df3e6d92a4d | -12.19916 | -53.90302 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 348899ee-bd03-394c-9056-e0c6feb9ab26 | -11.4956 | -55.50562 | 2025-09-08 04:53:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b81914d-6217-3d93-8778-7eaea33d61f6 | -14.8791 | -55.8229 | 2025-09-08 04:53:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71440c9a-99c6-3a3e-9e4d-42b23d35c2a4 | -16.91275 | -45.8086 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8702f73d-097d-39e8-870b-a9db7fe8cadf | -15.50664 | -52.77089 | 2025-09-08 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88dc9c88-a6de-3ef8-910d-f83ef012021a | -12.8151 | -47.99655 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99e185de-5339-3ad0-af09-32332d4def38 | -12.62385 | -56.97742 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6f01bd7e-5e33-3999-987c-440380488dc5 | -15.25083 | -53.79973 | 2025-09-08 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d854478-5f77-31fb-bb80-f053d7e40b2a | -15.25959 | -52.37974 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 595239d2-e2a7-34ca-b5ba-1b1553addd0f | -13.64111 | -43.81297 | 2025-09-08 04:53:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 236da19f-6e1a-3520-b964-8768ea067053 | -12.62316 | -56.98147 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 29b9ea8e-1d99-3fd7-ba4d-ddb59f328ac2 | -12.00513 | -47.77361 | 2025-09-08 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 20ec58a2-faa3-34b0-bbce-42b34edd7547 | -11.19444 | -55.00552 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 26c76e50-1cf7-38ac-be4f-7c890b1935a3 | -15.72997 | -48.37572 | 2025-09-08 04:53:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 711bab32-61eb-308a-b6b6-3bdb63c264fe | -11.41134 | -50.37914 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| b3fb2dce-3b8b-3064-91cf-25a926bcbfbb | -15.83737 | -52.26588 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d85bbdc3-d982-3fc1-a271-53d1ccdaa403 | -16.62443 | -49.31194 | 2025-09-08 04:53:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cabc7ffa-7535-300e-9b4f-6e795823e66b | -15.72529 | -53.53745 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6808771a-8f01-3d3e-90ec-9644afc512a6 | -12.62601 | -56.98611 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ca4a75d6-2d53-3e1c-af8f-85d56c7cf248 | -16.91312 | -45.80522 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0e932661-c81b-3067-b062-bd23e89d5feb | -17.26152 | -46.6988 | 2025-09-08 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcf8762e-3373-3fd8-ac0c-4c8e12ffc118 | -16.95572 | -45.76152 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1594a59b-52e8-3629-955a-85f822d30b39 | -11.41438 | -50.38406 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| a90ce575-1816-34c9-b806-a8f67bdfe147 | -9.47851 | -60.49841 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48c9ad9f-f907-3365-8c8b-d700fd232e47 | -13.82465 | -43.85986 | 2025-09-08 04:53:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e9ef358-56db-3c0a-ae4f-ec0b24a26e50 | -15.73426 | -53.56924 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9531cd1-4177-30d2-a1ab-9efa83259258 | -9.13199 | -65.95942 | 2025-09-08 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ae32ac8-6d64-36a5-a080-153fd9052cc3 | -12.83579 | -52.944 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af7e74bd-3f62-37ba-b427-68a88d8eb3a9 | -15.74376 | -53.57464 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df57d4b7-5487-39d9-b6a3-d2ff09660582 | -12.94376 | -54.79369 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 697371e0-5eee-3266-9c95-60462112714c | -17.16266 | -44.44087 | 2025-09-08 04:53:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd941645-05c5-3877-a610-b0e4a2fb812d | -9.63128 | -63.10146 | 2025-09-08 04:53:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad7f6af4-53b7-3e0a-8e05-cabeb26f2c4a | -10.87837 | -55.71605 | 2025-09-08 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2363dcad-669d-3aa0-9850-aeae66d21839 | -11.83055 | -46.76249 | 2025-09-08 04:53:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 037f69c5-8762-3408-9bee-9a71bf2fd321 | -14.78166 | -48.11543 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24517e4b-cd9f-34e7-bb50-8af958c19a05 | -10.96742 | -56.20543 | 2025-09-08 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3a01e93-a250-39b1-8ff0-8fecefff81b8 | -14.50603 | -48.80247 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4a2d60a-2234-31aa-8a5b-c717b692d5a4 | -15.38389 | -53.95082 | 2025-09-08 04:53:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README64.md)
