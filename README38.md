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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 766eb194-2e93-3da7-89a9-c51fd3e8c91c | -7.43848 | -44.78416 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1ae7597-5a70-3340-a212-78fca8be6515 | -6.67336 | -50.89497 | 2026-09-21 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dcbbe767-2fde-33cc-8080-6f2eef871906 | -6.02493 | -46.63449 | 2026-09-21 04:19:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9f87ddf-3f3c-330f-906d-6dd59f458528 | -9.44548 | -45.39585 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 64ac4bfa-6c81-3475-b869-1cca30a7d6ee | -7.44929 | -44.73832 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6198123c-e60b-361e-99ec-ed8234272351 | -8.31068 | -46.00275 | 2026-09-21 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3563c223-2e45-3209-9250-3c2eda8dc9fa | -7.24354 | -55.61416 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1b6ea6f8-018d-3433-94c5-4851b3dd20b3 | -7.59522 | -43.4393 | 2026-09-21 04:19:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9372bf54-d506-3357-9ee5-a96f028e4a4a | -4.09399 | -52.12676 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80e59daf-35d0-31b9-a5fa-573415313b19 | -5.92649 | -45.99937 | 2026-09-21 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57826fad-4a48-31d2-821e-0f524ed6cbcc | -7.70555 | -49.37101 | 2026-09-21 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dbbf0aae-e4fd-3feb-8bc4-1d6614f09619 | -2.9117 | -54.18902 | 2026-09-21 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4411bb7b-5414-3c69-9d78-585af10383bc | -6.26841 | -41.65416 | 2026-09-21 04:19:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 06208d34-1a9a-3f1c-a934-641860d8f349 | -2.17116 | -48.32418 | 2026-09-21 04:19:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b1e92a7-ab1a-355a-8b72-3af51d8ed6ed | -8.37113 | -45.63321 | 2026-09-21 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4bf312b-c7cf-37c4-9194-761575cf3687 | -9.25595 | -46.18596 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 198ddb40-6d8f-367a-8669-2de7a9821ba7 | -4.68482 | -40.1436 | 2026-09-21 04:19:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b87cf8fd-905f-3e51-b1bb-a4903f04ea0c | -9.45895 | -45.39808 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 24617cba-9042-38cf-b424-1014e570ce9b | -2.82336 | -46.71149 | 2026-09-21 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28ac17cb-76f2-3176-bf3e-2697ad639f57 | -7.29732 | -46.78265 | 2026-09-21 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e141fae0-2aaa-3668-93d5-13e1cf597a1d | -8.77024 | -44.29708 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32fb5554-160a-38b3-a28b-05dc0d9d94dd | -3.43715 | -50.60385 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46571012-68db-3dfb-9430-0af996bb0bef | -9.44429 | -45.40313 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8d1f6373-da6f-34f4-9563-43a50c55e1be | -6.57253 | -42.55785 | 2026-09-21 04:19:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| bfd1bcbc-2a0e-3332-859f-1dd667430976 | -3.87549 | -38.43717 | 2026-09-21 04:19:00 | NOAA-20 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 686e5025-52ff-3b0e-a1f8-81658de704d9 | -9.57076 | -45.46471 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5c76be0-c439-31dc-8445-fb4d51b0e41c | -6.57864 | -42.56234 | 2026-09-21 04:19:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 68ea0ee9-900d-3784-896e-4c0021e505c0 | -3.1645 | -50.82274 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cf169cc-6dac-366b-8369-79fe31232f2d | -7.44536 | -44.74137 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 027ca74d-2fae-3289-a7ad-e51ab5c36cf7 | -8.23356 | -50.78774 | 2026-09-21 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 56bc445f-419e-36f1-b4b7-0a888945d21a | -4.11648 | -46.39277 | 2026-09-21 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bae41ce-8b96-3e52-bad7-b0af6d909d51 | -7.08218 | -46.28901 | 2026-09-21 04:19:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c5f8472-7dd7-3ba2-9801-c506a9bed744 | -5.84888 | -53.53931 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a14c6d4-c152-31df-866e-ad811919c8c4 | -7.30803 | -42.26346 | 2026-09-21 04:19:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 505b1c9c-1b7d-316b-ae76-231a463be3d1 | -2.6387 | -54.69286 | 2026-09-21 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e91e5b30-986c-300e-bb1c-29f5f75917c2 | -7.13065 | -42.07451 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8841f274-4f7e-397c-ad97-ae772d85cc63 | -6.97336 | -42.57717 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8c4e6835-0eab-3320-a168-6c944c1be4ca | -3.99702 | -43.22859 | 2026-09-21 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e68b7807-59f6-3095-9d74-8c31364af682 | -4.68275 | -46.41321 | 2026-09-21 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a1533f3-ca35-335d-93f6-892aba94415f | -7.31139 | -42.26397 | 2026-09-21 04:19:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c94feefb-e519-3276-b024-541e325bb96c | -6.6639 | -50.89302 | 2026-09-21 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 347a28ae-bf03-37cf-9b7e-5bbe37220ba1 | -7.57021 | -57.67899 | 2026-09-21 04:19:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2d820d25-4b73-3193-8828-30f1e59b236c | -2.46193 | -49.22295 | 2026-09-21 04:19:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24c8646d-6fbd-3b08-becf-de565ec58e35 | -3.38368 | -50.44289 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24d4fd50-c82e-322a-a666-eb1aec90f7b7 | -7.23705 | -55.61346 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3d8f7643-fd0c-3207-9a50-e7ee50e77a62 | -7.32458 | -55.61108 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5b717a4e-75b0-3605-a197-843f2f4c44c2 | -9.45875 | -45.42047 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e9a2a71-7f9b-3c0a-bfa3-6386e01faaef | -7.29654 | -46.7649 | 2026-09-21 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2b069ba-e6e8-392b-936a-664ec1002ce9 | -3.38624 | -50.44196 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92da9104-d583-307d-8557-44dd8cd5e361 | -4.34954 | -55.65608 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1231f71c-b8d1-37dc-ad08-7e04cb6761b4 | -3.64317 | -40.58249 | 2026-09-21 04:19:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 68972d37-8c0d-308c-894a-dafe463fe006 | -7.58662 | -46.72969 | 2026-09-21 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9400a2cd-a20e-3787-b551-950c04822992 | -7.24973 | -55.58706 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f233990a-29e2-3dc8-ba22-615caca908c6 | -6.83222 | -45.56023 | 2026-09-21 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bda8c45-5c74-354b-89e8-f8065a8a13fd | -6.47051 | -48.44559 | 2026-09-21 04:19:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ac34925-1a9c-3046-badc-884a97d4f824 | -7.31533 | -44.19547 | 2026-09-21 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27fb1032-61a7-3555-94e2-e26d66203d98 | -6.47014 | -42.7772 | 2026-09-21 04:19:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d37a3af3-0a3a-34ae-9381-abe1c4fdd531 | -9.10021 | -44.69976 | 2026-09-21 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e5be275-9b87-34b2-af40-a3e7edafe1ec | -9.45102 | -45.40425 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 639c4039-3288-382f-97c8-55ab7694cc99 | -5.87616 | -51.58873 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c52c3d8-e7d6-3c26-b73d-89a394a8847e | -8.30658 | -46.86604 | 2026-09-21 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75f0d531-53d6-3d0f-bcac-627a0bb6f09f | -7.34037 | -44.4626 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ddc30e5-d839-32da-914e-c66c3ee74ab3 | -7.20676 | -44.08847 | 2026-09-21 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6374d17a-f12b-37fa-aefa-6ddb9f13ea9b | -7.424 | -44.76722 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f31f919-bec5-3b01-ab6d-a1cc56a5c9b0 | -7.32032 | -55.21281 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e26e5eea-8598-321f-b6ae-017bbc49179c | -9.46946 | -45.41842 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8291bd2-aaa1-3e29-80a1-e883ce2f73f5 | -3.87539 | -40.75373 | 2026-09-21 04:19:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c86da509-02d8-3542-be13-ab331508cc15 | -7.42285 | -44.77435 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| db05c8d8-10e5-3da0-b630-3237319fbb0a | -9.44191 | -45.41763 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2ee0aaf-85d7-382a-998b-6e62d7eba36a | -7.48066 | -45.47847 | 2026-09-21 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6576ec23-3695-337c-be5f-da5c28a0dd98 | -5.8402 | -53.52129 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6225e913-1370-3b7d-ac6f-9cd0c7eda064 | -7.40203 | -46.15042 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 26221365-88b2-38d4-bac0-d17c5c2f1f82 | -6.90542 | -41.70219 | 2026-09-21 04:19:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b9ac827e-e3f7-32b8-9b0b-61d53134b620 | -9.44222 | -45.40685 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3a7758d-d1df-31ff-a2ec-0760e5974d1c | -7.57873 | -57.67327 | 2026-09-21 04:19:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1e05be6c-3f4f-3bf9-a755-40ec19c6cbd4 | -7.24609 | -46.90984 | 2026-09-21 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e360e765-cf7c-3341-bac7-ea8091134cf6 | -2.16686 | -48.32347 | 2026-09-21 04:19:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d99b8de-6a8a-3110-ab35-c2ff159cde68 | -3.99979 | -38.98558 | 2026-09-21 04:19:00 | NOAA-20 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 10426c39-7f32-3955-9160-d523fa590294 | -2.19405 | -48.374 | 2026-09-21 04:19:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a9a2af6-cab3-338e-95b4-3805b2ebf103 | -7.88492 | -44.84117 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46aebedd-8106-3787-b898-51d58099735d | -6.89523 | -41.70057 | 2026-09-21 04:19:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f86a9a69-5155-3790-a135-98e3d60009ad | -2.67835 | -49.02553 | 2026-09-21 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca6dbd55-13fd-3995-9dc1-0245cab13b24 | -8.78972 | -48.73811 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1b2339d8-bc5d-3b9f-be7c-d488218588c5 | -8.4512 | -46.40466 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c79f9244-8be3-38e4-beba-34c2f9853861 | -8.28536 | -50.92714 | 2026-09-21 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2cf5f39f-3136-36b5-b9fb-515fda73467b | -6.40124 | -45.19264 | 2026-09-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ee2b752-da45-390c-9dd1-1241d902c93e | -8.77579 | -44.28365 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ee18a09-d751-3880-8fee-2a849b56f236 | -6.99543 | -42.19995 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9a86e29f-1ae2-3c23-9491-ce545b166912 | -9.44289 | -45.43275 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c9b44e2-b2ae-3480-bb3c-54f255ad24bb | -7.5497 | -45.42097 | 2026-09-21 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc093eda-1afd-3e53-9570-fefc5013642f | -3.60888 | -54.05171 | 2026-09-21 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 878bfaca-7af9-3bcf-8802-5e476379f91f | -7.11942 | -43.56946 | 2026-09-21 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a600c49f-5939-3297-9918-161d374df706 | -6.20395 | -53.56213 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d76dda1-3538-3539-8ff1-1100349d83db | -7.24778 | -55.59733 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| adb40f15-f3ee-3085-b9ea-2fa0d079f825 | -6.36393 | -43.36356 | 2026-09-21 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 146fed13-f7eb-363d-89ed-d83be9ad356c | -7.71761 | -49.40173 | 2026-09-21 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac809bf9-2445-39a6-86ec-020756eb4656 | -4.68775 | -40.14806 | 2026-09-21 04:19:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3aae6042-49ad-3774-a12d-a025a26a82a8 | -6.9819 | -39.88949 | 2026-09-21 04:19:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d672567b-22ff-3227-94e8-a78f2f7dfcc2 | -7.76501 | -44.82561 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77063bb4-3fcd-3f2f-b488-64b2f844dd52 | -5.15757 | -42.74371 | 2026-09-21 04:19:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README39.md)
