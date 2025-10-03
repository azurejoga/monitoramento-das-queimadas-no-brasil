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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b39d378-fbd6-3fe3-a671-e254faa7073f | -5.63612 | -43.90674 | 2025-10-03 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 341b137b-7aa3-3bf8-8f14-d34c42a74503 | -7.52726 | -47.28722 | 2025-10-03 03:42:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c23a6970-b0ed-3dcc-a12c-7576e33333bb | -6.04326 | -44.61526 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 60faeb2b-2b20-3653-b0a7-2f0b950a500d | -8.30346 | -44.84939 | 2025-10-03 03:42:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2e06e05-ae13-3af0-ad5e-7e4fdd212494 | -5.19122 | -45.42175 | 2025-10-03 03:42:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47ff9e02-f96a-30ba-89be-c3f56624a4bf | -7.28762 | -45.2581 | 2025-10-03 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e5bf2661-624d-3050-826b-8fd5fd7d1eec | -6.35376 | -43.44194 | 2025-10-03 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dd31116-12c6-3527-a78f-cd060d0b2723 | -6.67548 | -42.8288 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e75c728d-d818-3a36-b32a-df0d3a4718c9 | -6.0487 | -44.6161 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d2508aaa-1d6f-3790-ba7a-a3744e2c015f | -6.67286 | -42.78708 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5066274a-e61e-3911-9acd-ce3839253a57 | -6.68891 | -42.83611 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| bea3ab31-34b9-3281-89eb-ff1825f34234 | -6.6825 | -43.71472 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6c8f2c4-d7d0-3d80-b274-91e2709d515e | -5.35462 | -43.75035 | 2025-10-03 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a47e97e3-e6ff-347a-bd38-5d3aaf765a65 | -5.18546 | -45.42062 | 2025-10-03 03:42:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ee2d6a4-afb1-38bf-b5af-02bfb3d7d7f8 | -7.72735 | -46.23237 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5f79cb1-751f-32a6-b354-fd9b1a8ed3cb | -7.78366 | -47.37694 | 2025-10-03 03:42:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 222e9781-f0aa-33b2-99c2-3ed6523e636a | -4.61488 | -43.15633 | 2025-10-03 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2a4fabb7-5929-3ddb-9476-57b23d22eb87 | -8.47962 | -44.5918 | 2025-10-03 03:42:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22baa693-67e5-394a-9604-aa64da2e4870 | -7.75743 | -46.26049 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 69550f21-b0d8-324c-9233-79c6e7e76ad6 | -4.65677 | -45.7821 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 14203844-aacf-32bf-8cb3-51b54e3c1182 | -7.7857 | -42.5688 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| a1632768-f166-31d0-be78-eb6be6ff639d | -6.36056 | -44.75751 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 247022be-0ee7-3d17-9816-f3bda52a7013 | -6.28734 | -44.05214 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bebef9d4-ec9d-3b35-abad-c94779bdeabe | -5.31583 | -45.28523 | 2025-10-03 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad5e1783-5279-3d76-b7f2-4ba6118feb79 | -5.16697 | -46.05581 | 2025-10-03 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fd30c4e-122b-3129-8189-a18f58678cf6 | -8.21881 | -45.54644 | 2025-10-03 03:42:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da581964-4356-39db-84dc-b0ba56359bba | -7.25321 | -48.4866 | 2025-10-03 03:42:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7f8a5250-8ca4-3f53-a661-f75876ae1dc5 | -5.01221 | -37.3596 | 2025-10-03 03:42:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d5637ab5-2d7f-35b1-8e47-0cf3b0e2b575 | -6.29952 | -43.91098 | 2025-10-03 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 596b962d-d448-3499-9268-35c3040d569f | -5.64079 | -43.91077 | 2025-10-03 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 54d5b865-825a-3b08-a192-9f11a1f0e3d5 | -4.64922 | -45.79016 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42754c5d-46bf-3f52-9393-7a2d5e7966d3 | -4.66737 | -45.792 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| b638c90a-e815-3d5a-9b40-b10c36004252 | -8.30289 | -44.8526 | 2025-10-03 03:42:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60af8a2e-2f31-3747-9834-1bf6f30353f9 | -8.61323 | -39.07942 | 2025-10-03 03:42:00 | NOAA-21 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 16fa46a4-a4bd-36cd-85fa-b0c632ce3336 | -4.64998 | -45.78578 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3d3f2f2-e907-37fd-a101-d36d278ae2ac | -7.73472 | -46.25248 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e968388e-737b-3d83-8b57-66dadfd3a5f2 | -4.64848 | -45.79447 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72125633-d669-3aef-b73e-1e5baf819740 | -6.40955 | -43.83885 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d226773-1f11-3553-8648-13a42d53420a | -7.88969 | -47.35106 | 2025-10-03 03:42:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 103094fb-b5f8-3c89-a332-03a84f785421 | -7.7522 | -46.2235 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b91accac-a7ba-32d1-9310-b493279058d3 | -8.21814 | -45.55013 | 2025-10-03 03:42:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8eb94702-70b5-38d1-b734-d0f1aa8b7a14 | -6.70883 | -42.81126 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d7f39f12-fe7c-369b-a7af-4bb0c9b58680 | -4.65078 | -45.81688 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2cbe7691-5164-373c-a28c-428707346335 | -7.73977 | -46.25785 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e1fe1b3-14f3-33bf-b754-7b2dcf791203 | -7.75459 | -46.24315 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 2e47007e-79b0-3be7-80bb-ab011f2cacca | -7.75197 | -42.57277 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a5a32d00-6023-3db0-b39b-ef6dc35da824 | -3.09302 | -47.01332 | 2025-10-03 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 03c705b9-78d4-34c0-ae47-2b51eb5ff5d4 | -4.04741 | -40.50536 | 2025-10-03 03:42:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7efe5b67-404c-3768-a391-0ccd442e8bba | -7.30295 | -45.26807 | 2025-10-03 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f638ffa-4106-3b72-a90e-5e442b6c7913 | -7.32644 | -39.31878 | 2025-10-03 03:42:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 433ab6f1-700c-352f-b0f8-0ec572ad9adf | -6.87958 | -45.48086 | 2025-10-03 03:42:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d82f630-ab35-3371-a53d-a664bc707be8 | -6.78776 | -47.16389 | 2025-10-03 03:42:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3b623d41-b863-3c55-81e2-b09d9cc23ffa | -7.71431 | -46.20428 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 82ab05f7-4770-33cb-b3db-0d6a7dfbc51a | -7.71525 | -46.19521 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55df8568-3144-3ab6-be0a-7c7243bf2b16 | -7.05913 | -43.22675 | 2025-10-03 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 06dab058-dc0d-3a60-9b5e-4721ae306132 | -4.65685 | -45.81743 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca1163ec-83b6-3983-a587-10efe336b855 | -7.29654 | -44.18364 | 2025-10-03 03:42:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94f00d06-a147-3b9e-b9ce-0fbe2fbdce89 | -8.44961 | -41.89704 | 2025-10-03 03:42:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 0b9573b9-7bbb-37ae-bc7e-07d3a6ef6a3b | -7.75723 | -46.22893 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2671ea1-26a1-36aa-ba9e-323ce3e712aa | -6.32759 | -43.88529 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a5d4db9-59dc-3a45-b796-38589859863b | -6.68411 | -42.83556 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 210dbb12-a25b-3093-8afe-2ce5451ccec6 | -7.71378 | -46.20305 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c8ff7e55-bdc4-3d0e-a8c1-b585aabc8368 | -3.09607 | -47.00655 | 2025-10-03 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 660b8807-3b64-350e-b6f7-55aabe8bc55d | -4.64699 | -45.80312 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24b28e0d-37b6-3f2a-97bd-cc302ffbf092 | -4.01277 | -41.79568 | 2025-10-03 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6f24f8d0-5b43-34be-9d6a-6f5817dc671e | -6.70793 | -42.81633 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1484f597-488d-35b6-bc51-714043887493 | -7.75984 | -42.55484 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 08fed192-fb52-3d23-b6dd-38690d281d3d | -6.95357 | -45.34601 | 2025-10-03 03:42:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6bb4d3c5-2c3d-3c95-9915-a93f16962149 | -6.64687 | -43.59608 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 638f2c1a-a0c4-36ad-ae1c-e5046237213b | -7.7528 | -42.56804 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| fc07125b-a33f-3305-8006-f947dfce7a50 | -4.39378 | -38.41326 | 2025-10-03 03:42:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| beb0da35-e68f-3a2c-a98b-d161e2ffd09a | -6.75964 | -44.80762 | 2025-10-03 03:42:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a476556-7e7d-3b14-800e-bf811fa6e6a7 | -7.76406 | -42.58463 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 445d04a2-3408-327a-9fc0-3e9503f8a02f | -7.90373 | -43.52426 | 2025-10-03 03:42:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9f095b67-95f0-32a0-a15d-1a1dab310fcc | -8.23524 | -39.02859 | 2025-10-03 03:42:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 96ddedb8-5084-3133-987f-5e2d524f6c9e | -8.58798 | -41.06475 | 2025-10-03 03:42:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 016e0929-1888-3b7b-b853-fc7a0a5ec55c | -6.05534 | -44.60994 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3107791e-7f2f-39b7-91b1-570b2e9d8dc5 | -6.47936 | -44.21909 | 2025-10-03 03:42:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4c7f72a-073d-3b70-9e98-105ae16cb7e1 | -5.98693 | -43.47804 | 2025-10-03 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 412acc71-1372-34a3-97a5-62b07a36063a | -4.67472 | -45.80179 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1ab3b4c5-61f0-3341-9d4b-fe205652fe46 | -3.09204 | -47.01896 | 2025-10-03 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 865fd5d1-6ca3-316d-86b9-3613a69c0fc3 | -7.76437 | -42.60987 | 2025-10-03 03:42:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 1f7f5a6e-ef10-354f-8faf-21e4004e1269 | -6.04747 | -44.62318 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8b2c6703-f80f-3cb9-bdff-5c6bb46d9c22 | -6.04923 | -44.64531 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0f863201-56a4-3dfa-9f73-efc9bf266904 | -6.05355 | -44.6203 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f9e0e2a-6952-3eb3-ba72-ad934c9b3c42 | -7.76864 | -42.58545 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e0954cc4-ab73-3ec7-8809-423d1cd10934 | -3.84306 | -41.56813 | 2025-10-03 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 2bc8fcf9-662e-3777-892a-c057d55c73bc | -4.66878 | -45.78377 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 16ece4fa-5e45-399d-841f-ecfa560215d1 | -6.55285 | -43.89526 | 2025-10-03 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb25e18f-a91d-33ad-a111-93ca9ab0cf73 | -7.1586 | -44.99449 | 2025-10-03 03:42:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3cd26c89-b75e-3282-bdad-12884600ccdb | -4.66286 | -45.81831 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 20d4add7-ac65-3ed0-94da-3194b1ad242d | -7.31688 | -42.8812 | 2025-10-03 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b6548ae0-2b55-355e-aef5-ad6d62c34c36 | -6.35229 | -44.29824 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b61c33cb-38f3-3485-ba96-543485f2eb06 | -4.66712 | -45.8098 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 8de4f0a2-f791-35eb-a2e1-eff5dcb44935 | -7.15796 | -44.99807 | 2025-10-03 03:42:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a2435d2-ce18-32e5-8b66-056c3c5fbc16 | -7.77638 | -47.38113 | 2025-10-03 03:42:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7e871c8-28cd-3623-9b30-953a51c79bba | -6.5158 | -43.94176 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6adc3d8b-eb2f-3202-a354-e4a656bd31d5 | -6.03473 | -44.63224 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f4c6e6e-621f-339d-acfc-3bdb6b514421 | -7.316 | -42.88631 | 2025-10-03 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 84fbf97f-9443-3c60-ac5a-87e604b3ab59 | -6.41505 | -43.93025 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README18.md)
