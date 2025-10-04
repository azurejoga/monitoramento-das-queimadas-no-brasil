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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8aec9c81-13c0-38ac-964a-abad87dd48a2 | -5.62223 | -44.70154 | 2025-10-04 04:12:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04d6177f-04aa-3eb1-abda-4d9f96dd2f97 | -5.88645 | -44.25739 | 2025-10-04 04:12:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4a24fbc-c1f9-3542-b3e2-2bec3ac9357b | -6.2672 | -42.45533 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| a2e41903-739d-3763-973b-376694cf3eaf | -5.6737 | -43.56771 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c1f4809-9c8a-3c6b-8451-2a10aba59d1d | -6.88082 | -44.5033 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dce703a4-4ab4-3d33-83b9-b03fd354a05f | -7.4773 | -43.03304 | 2025-10-04 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fb621955-4df1-3cbe-828e-7d1dff79683f | -4.4275 | -40.76335 | 2025-10-04 04:12:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 81f11f84-c70f-3ad6-bad3-c0839fd176d4 | -6.6817 | -42.84339 | 2025-10-04 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 526a63bf-fbde-3239-980a-3cbe4783d9f3 | -5.48163 | -44.11269 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b470230e-9be1-312f-bb49-4b128c0fc405 | -7.16296 | -46.21468 | 2025-10-04 04:12:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75807a69-d19e-371a-a194-eebecd18fa81 | -5.84773 | -42.78961 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| da362538-ad35-333d-80b8-5193b40aaef9 | -5.83888 | -42.86934 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e3ecfd6c-f3f5-3511-8e01-5d48c35e7203 | -7.55702 | -42.39222 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3b2a5b01-1b7e-3d17-a5c3-306d6ed5b5bb | -5.47884 | -44.10858 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 78f8e42e-dc7c-37d6-8073-dbc9b1334707 | -7.72502 | -42.60189 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c801d81e-9e81-34d9-b9c6-22ddfaa3a25d | -6.07078 | -44.33474 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81032317-aef2-350b-a35a-54bd35bee86e | -6.38786 | -43.392 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c3660da-f45e-3c4d-adad-06d8999b3008 | -3.84754 | -41.57849 | 2025-10-04 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e92073cb-16e8-3b3e-becf-11b341a1e0c3 | -6.23988 | -45.34794 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce07aa29-976f-39d8-ae97-6e4fcbc8b14d | -6.36431 | -43.9034 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 68a70312-bf6d-3c95-9a2c-8ee8bfc9e15e | -6.00683 | -43.78197 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bcbf113-7570-33ef-a7ac-dce9588388dc | -6.67734 | -44.19979 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da041e95-a555-36ff-a8f3-18a994b63d81 | -7.05216 | -42.77763 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d08863d6-2222-329d-86cd-86e35712ee13 | -6.24623 | -45.35285 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| dfbed016-f043-33e3-a311-7425fdf8e092 | -7.72111 | -42.5834 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bd953d76-71d5-357a-bcd3-0be1f9fec6bc | -6.15448 | -44.11322 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf354e87-7950-31ce-a054-39b0881a550e | -4.45477 | -43.24211 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ba0178b-8f77-38b4-8f8e-bdaaf17d3284 | -4.61677 | -49.548 | 2025-10-04 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d541cd7b-0786-3ff7-b26c-d3aa47fb3706 | -6.77738 | -43.1211 | 2025-10-04 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d46d3eb-b857-3c03-ab0e-5dbe0a4d9c9c | -3.84585 | -41.56753 | 2025-10-04 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| c9c22f12-fc13-3e9f-90da-85efc658f7aa | -4.38114 | -41.9213 | 2025-10-04 04:12:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4b42146a-4787-3b45-ae71-f5075f9199ea | -7.01793 | -44.8539 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9e4d3bc-6526-3cf8-a4f7-e140156650ac | -6.10288 | -43.43235 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbaa6f2e-f0cb-36de-b106-c0eb98b94261 | -6.38462 | -43.60538 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36e7bc0b-78ee-3887-86a0-5e477f3e62e4 | -6.26775 | -42.45185 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 47619164-3500-3aa6-84c8-294e49ca061a | -2.68287 | -48.39185 | 2025-10-04 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6d27aae-d8d9-3f1a-833a-1d230c697f25 | -5.69395 | -42.83961 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 79d6dedc-5a60-3051-839a-72053d6e17a8 | -5.90598 | -49.30261 | 2025-10-04 04:12:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01a8177f-cf5c-38c4-a680-a6c2b26e0435 | -6.09073 | -43.48739 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ead742a5-18e0-3ce7-bbc2-aaf0e4c5cddc | -4.71429 | -46.13001 | 2025-10-04 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0e9320e0-fa27-3d9b-a7a6-49937055ae82 | -7.7905 | -42.57276 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7b621296-3f49-3d2b-80fb-95c8e3604245 | -6.37132 | -44.6231 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 72edf190-85eb-3ada-8d7c-31aac51067d2 | -7.33121 | -41.4441 | 2025-10-04 04:12:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 47ed09a4-140b-379f-a7c4-c0ff1f02a4ed | -6.02705 | -46.35131 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c02e1d50-4583-3acb-8d3e-450f3cf61f43 | -7.34636 | -44.34668 | 2025-10-04 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 52b77692-1adf-3ee6-9754-32d1ca497957 | -5.2824 | -47.52386 | 2025-10-04 04:12:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2f5e23ce-b938-35e3-b7a1-2e2fb91279d0 | -7.88765 | -40.89048 | 2025-10-04 04:12:00 | NOAA-20 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f79bd95f-fd96-3828-8679-bda69e0e8d86 | -7.02015 | -42.30864 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9dfa1d56-372d-3b44-a29b-2af7596fa569 | -7.80371 | -42.53176 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c041aa27-8888-3c47-89d7-54dec0bda371 | -5.81872 | -42.8876 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3837040a-d163-3811-aa0b-2e2ff3b7dc8e | -6.33988 | -43.45905 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01900035-5ff3-3b5a-b16d-1fb8b8fa502e | -3.30652 | -48.71255 | 2025-10-04 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f4286f8-2ddc-31e8-b210-512893b0e0a9 | -6.17097 | -43.92371 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff558188-8b67-3b9d-a6d2-c15b0e48e2bb | -7.56979 | -42.39779 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ebaafe05-d94f-37f7-96cd-981f955a459a | -5.08419 | -44.09433 | 2025-10-04 04:12:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a5317497-89ee-362e-aa3a-d6ee6fecb0ca | -6.66897 | -42.81658 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c715bf8d-0699-3bf1-b06a-a5a7bd3ff300 | -6.27106 | -42.45237 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 662d615f-6a2a-33f8-8c5b-9c6b0fbd6dd8 | -4.43817 | -43.23949 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d264c99-9514-343c-8ab1-e19d6c98180f | -6.37148 | -42.89385 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5d5ca81c-4b6a-3c52-bc88-2d9639f6a51b | -5.61186 | -43.23015 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ffed455-0b32-385d-9b54-f038f4485313 | -5.4895 | -44.10659 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 8769a7ca-5e01-32de-b304-c095de52447e | -5.93164 | -43.31249 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d706dfc-6674-3123-ab47-2e2c2090265b | -6.33488 | -43.89511 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38ebf2c1-b2be-3593-8bf2-8e26ec8d6239 | -6.59924 | -44.30082 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66a2ac5c-fa7e-38ec-ae25-345b52604141 | -7.79656 | -42.55577 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 45c9744a-8f36-3302-bf25-b47b8a791178 | -7.43516 | -46.46764 | 2025-10-04 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e746492-c138-3de6-97d7-785ed58ade81 | -6.06365 | -42.51884 | 2025-10-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b02a7c42-a188-36cd-97ca-95352b094c74 | -5.97832 | -44.14716 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 821e4b69-ffb2-3792-b285-84dcf34f3a65 | -7.78868 | -42.49701 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| beca3b5d-6fed-361d-8749-c1b5fdd2077c | -5.53912 | -45.15308 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| faa93dbc-b6de-3318-b4f5-5926a5654983 | -7.72857 | -42.59887 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e860a060-2419-3fc8-a2b6-44cb29c7e828 | -3.83311 | -44.55018 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba833db9-c1b5-3a11-b8d2-1bf7f3f11624 | -6.26741 | -44.04324 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ba19e0a-1dc2-3e47-9adc-dec8cab6f90e | -5.01677 | -43.66096 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78a8a71d-e3b9-347c-86fd-8ff9c64c958b | -6.66458 | -42.82297 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c43b243b-5c58-3cca-bf7f-6433867077e1 | -7.00765 | -42.30345 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5228031f-0368-30ff-9b5a-84971169b993 | -7.77453 | -42.60966 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4abb5bff-cebb-364e-bae2-370b3a07ee27 | -5.68847 | -42.85289 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9764c5c1-aacf-3847-9e03-afc668aaf26d | -5.14581 | -44.80722 | 2025-10-04 04:12:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b676295f-4af6-3ec9-b047-dbebbe38dc0e | -5.90672 | -49.29824 | 2025-10-04 04:12:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b49bcfb9-edda-3975-ae48-9d0c2f5afff9 | -6.64967 | -42.80998 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b61274f0-aba8-3254-9b30-ee82f25757fe | -5.49945 | -42.78032 | 2025-10-04 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 27e715fc-8efa-3741-a83d-7186eabea499 | -2.69091 | -48.39758 | 2025-10-04 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e671b9f3-44ab-3b2d-9b66-91333da1309d | -5.98306 | -43.60963 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22cae742-0ae5-3bc0-9db4-9e4deb5d5024 | -5.2491 | -42.96733 | 2025-10-04 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 3bc0697c-b2e3-31ef-8b37-88202353189b | -6.24748 | -45.34519 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 958f2d78-1468-3081-a0c9-dc72b5482112 | -6.71252 | -42.81987 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b5a26817-a2b1-36ad-82fe-2f76ed12254c | -7.47349 | -43.05724 | 2025-10-04 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4e3a66a2-187d-30ff-a2a5-f00310353527 | -4.70232 | -45.60186 | 2025-10-04 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 807b23aa-4f36-39e4-b7c6-6c570e79dfa4 | -5.65953 | -42.71399 | 2025-10-04 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2f487185-3d87-3fc4-86f5-e48a448a506f | -5.93936 | -43.3066 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b13a9569-7d9f-3898-b789-65d7da325e77 | -7.69841 | -42.57625 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0fe993fe-decc-372e-9809-b53b4d6e61a4 | -7.80426 | -42.52825 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8f0bb285-9105-32cf-b0ba-179aece427c4 | -7.04885 | -42.77711 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1a65ac27-0e0b-3027-bdd1-44e03f64459e | -5.49027 | -45.34449 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc8c614b-62f4-35b9-9ba2-acab0e02b5a8 | -5.40535 | -41.32359 | 2025-10-04 04:12:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 85fcc333-015e-3d5c-b53d-c81e51bcb31c | -6.67944 | -42.81469 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 059758ec-d223-3fef-88c1-8cc238c8f553 | -5.14236 | -44.80667 | 2025-10-04 04:12:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a23acb18-2ead-3f76-9f0c-8084882b9f27 | -7.00432 | -42.30293 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 90726152-0091-320b-b194-20927d965147 | -5.83463 | -42.8512 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README60.md)
