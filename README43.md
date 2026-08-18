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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62e39328-a57f-30fb-af18-c90b399b040e | -6.76028 | -59.46088 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69c0d095-ce4e-3135-828c-bc08b09bbba1 | -6.10456 | -57.71665 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60d77035-a0a0-3301-a130-cad892910dcc | -12.00359 | -55.52566 | 2026-08-18 04:57:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff9be911-33d6-357f-8324-5f568f9fde13 | -8.89906 | -60.59163 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca92fce0-3c2a-33e6-a5de-428a592a98d4 | -8.08249 | -61.35906 | 2026-08-18 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75635e01-c293-33dd-b742-7f99b9edcfba | -8.58415 | -54.73473 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 253201da-b725-3328-9461-b9f32a259628 | -8.55365 | -55.31585 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aba5ca2d-4802-326e-8491-de4fbe78ad60 | -11.3402 | -55.27355 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 79a2f3c9-752a-3741-acd4-33fc6bed7d21 | -8.49096 | -54.86105 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 279bb823-8629-3bce-a628-e5d22223c64f | -9.19457 | -49.96908 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4f91bcd8-7514-32ba-852d-6a41f72871db | -7.88093 | -61.79819 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 623d9623-ee47-3196-9d99-3934c0db7079 | -12.37547 | -46.44664 | 2026-08-18 04:57:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b24ad5b5-024a-3813-9c78-90f0f04cbcfb | -11.50511 | -46.61102 | 2026-08-18 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8ac8f64-a9a9-3039-8a8d-5e1b79dbde50 | -7.39922 | -55.48469 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccb086fa-c552-3778-8f46-37b2918be018 | -9.1636 | -59.70094 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc5ec5d5-1129-3571-ab02-db8dedf00700 | -7.5632 | -55.56291 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d4453a8-22f7-3b77-b753-5d9c51fa8a3e | -6.84946 | -59.01857 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6dc9685d-456c-37bc-b75b-982cf43565e1 | -7.9117 | -61.74384 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c8a213a-10a8-36af-8b26-18beef99c1e3 | -6.76551 | -59.45715 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30727f23-ef27-3606-a944-12d2a03cb307 | -8.20946 | -55.01546 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e062fd6a-726b-3046-a941-10c3246ecdf4 | -8.56638 | -47.39737 | 2026-08-18 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 172e00bd-28c7-382a-8dfa-1fa28ecf6cc1 | -8.90027 | -60.59419 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7d804a5-b881-3063-a994-c8d8072e4301 | -11.36472 | -55.41983 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c701e754-4145-3252-8e79-30e2f628a90c | -6.70571 | -58.93918 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1984d3c8-fac2-3e3e-b8c7-de7eb62b8dd7 | -8.09537 | -61.34402 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32acfaf9-8904-3db4-9414-6682a80ba1fe | -8.58206 | -54.70472 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 362b6e5c-a23e-33c2-af9c-dbac497b91fe | -7.39224 | -55.48355 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf193523-f1bc-374c-9a24-2fa4829ddcd4 | -7.64101 | -55.64301 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15c9160b-0975-324b-9176-566d8284d5bf | -8.58706 | -54.71664 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5113237c-994a-383e-b339-920ba72bcf80 | -12.46451 | -54.17965 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a38d8a4b-4bda-3291-a86c-1e874e0aeddf | -11.32008 | -55.23717 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7838ac31-9f2b-32d4-93be-ac6d951a879b | -6.95779 | -59.04465 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d111d6a0-5478-3838-9e15-6844f6d1a8c9 | -7.4539 | -59.99868 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00d6b936-7efc-37ba-bc00-73d329fffe09 | -11.32475 | -51.41978 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96487dc1-feec-3499-87fa-a96a99720a5e | -11.71823 | -54.62075 | 2026-08-18 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a4bb454-ee4e-3856-b23c-7cbb20c32f53 | -11.24669 | -54.8271 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3386e08c-1bb6-3be7-8c41-4d3fdfd6fcb2 | -10.56288 | -51.97182 | 2026-08-18 04:57:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2326f749-d27f-37a1-83a9-79fabbda3fb7 | -8.55769 | -55.31266 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77f9e9bc-1343-39c1-a7ac-a83abbb13ba5 | -10.56171 | -51.95649 | 2026-08-18 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 82224383-1d33-3995-9d0e-ac4852b626ed | -10.05283 | -62.45823 | 2026-08-18 04:57:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 470a01cf-061c-30de-99a0-58c3b79d7ba8 | -10.28165 | -50.44323 | 2026-08-18 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08df81af-6269-34d1-b70a-192f7a52ae6f | -8.57742 | -54.73362 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 1373d21c-2d1c-347a-ae53-be4f9414151c | -6.95197 | -59.0267 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 121f3429-2726-3363-8bc5-19de6af9ac56 | -12.24667 | -45.87402 | 2026-08-18 04:57:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb9c01db-71b1-3286-b714-3d2c72bc3422 | -11.37146 | -55.42099 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4d52ffe6-6a9e-368b-a818-bcf04dbadb60 | -9.05591 | -57.06623 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b4ebe35-e829-30a2-a66d-902c445a4344 | -10.58105 | -51.967 | 2026-08-18 04:57:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5d28b50-d383-3893-b597-732d7104cf8b | -7.63129 | -45.7464 | 2026-08-18 04:57:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d41449b-af4d-3bc0-a63a-96d14de694d0 | -11.1928 | -49.68407 | 2026-08-18 04:57:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0776aa8f-ae7d-32f2-929d-958fe61d78e2 | -6.74897 | -59.18322 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 803b9f6c-67b7-3eef-aceb-fa491043bba7 | -7.43289 | -44.87237 | 2026-08-18 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ff2cf82c-eba4-34f8-8f95-03c353bee6f3 | -6.77443 | -59.45863 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4416425d-a073-3541-b8f2-e974032fbd7d | -8.56265 | -47.393 | 2026-08-18 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 100cab65-e97c-3bfc-8ba4-0a8b5631c43c | -12.90616 | -52.82928 | 2026-08-18 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbf1da0c-a42a-3bad-8568-45011491ac1a | -6.69362 | -58.9467 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3f4615f-c968-3110-a631-98c415d8bae9 | -8.35959 | -46.48119 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87e55b0f-8ab1-3589-b228-7bd7c2c78c6d | -6.99589 | -59.041 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edb58017-05f3-3357-b0ad-c9822aee4af7 | -6.78927 | -59.45224 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31f7f222-bba3-37bb-a303-b1c1ce73be44 | -8.62806 | -54.70861 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 832d1a34-99ce-3b18-a3a1-bd3e1066ece7 | -8.5629 | -54.71637 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01803b8d-ced5-38aa-a17d-5a5ae8938982 | -8.21201 | -55.02308 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e68d4ac8-012e-3cd1-ad61-6101dd4f322c | -11.53188 | -46.64196 | 2026-08-18 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad87b4a9-bd5b-3eb5-a3b4-4afebc195625 | -11.10247 | -49.9058 | 2026-08-18 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b42c9c1a-c973-3c6e-a07b-d372f777c135 | -10.27865 | -50.43844 | 2026-08-18 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd37afb4-52a2-39e0-b61f-0e7d1d71b0f6 | -10.29279 | -48.23882 | 2026-08-18 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39164308-98c3-3be1-9bdb-7fc1139e5833 | -6.95849 | -59.04054 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cb1f2ac3-f9a0-3f11-bb24-45fcee1bb6f9 | -10.4127 | -61.21256 | 2026-08-18 04:57:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d962ec9f-34a0-3274-956f-e79fde013248 | -9.16186 | -59.70658 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa1e3bf8-720e-3f00-87ee-096dfbbd3e45 | -8.4894 | -54.91332 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38810223-123d-35ff-8e63-864feb4a9de3 | -12.01303 | -46.4991 | 2026-08-18 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 220f122c-5cfd-33a4-9d6b-f2d775cfa879 | -7.88471 | -63.76202 | 2026-08-18 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f9ba59b-4ec5-3357-bcb1-1c93a7f263b6 | -8.5584 | -47.39228 | 2026-08-18 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d5a2bf4-ed62-39ae-8f2c-b10266e1d700 | -12.76558 | -48.43591 | 2026-08-18 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63e39be8-0060-3f70-b9bc-b3634228bcd0 | -6.68698 | -59.07299 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02a26224-9797-3824-94f4-01acca7da2f5 | -6.10168 | -57.73407 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74b120dc-1e82-3b06-aab9-95d5cec75928 | -12.46834 | -54.19833 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6135e59e-49c1-3561-bbf9-108a5190a849 | -9.98235 | -53.93688 | 2026-08-18 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c4fc4c4b-8c86-370e-acf4-a56a070ddd92 | -9.15894 | -59.67143 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c0cf0ba-d22d-3976-b111-f90472b67aca | -8.56801 | -54.7061 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3cee6845-62c7-3bd7-bc62-07ebc7f7e814 | -9.467 | -51.62805 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4577b8ca-0d7f-3238-8d12-8dd0a77a6e32 | -11.19888 | -54.8265 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84f80bb7-7972-30a8-a1fa-510d5b641317 | -10.41097 | -61.21573 | 2026-08-18 04:57:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40ebd1ae-9b20-35c5-aca8-f5da6c2557f0 | -8.67961 | -54.62461 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e071c54-8366-3184-bb77-2abc4c85ccca | -8.72124 | -62.90524 | 2026-08-18 04:57:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98bdcaa5-d421-321d-86f1-9ff0c5ed0997 | -9.19889 | -49.96527 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8b1c0d27-f504-31a5-80ff-14c3d502ad74 | -6.13512 | -57.73958 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f44fe412-06a8-3054-b275-de82b399e093 | -9.99392 | -53.94951 | 2026-08-18 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72279aaa-ed74-3e48-94f1-a4fbccb56a18 | -8.72666 | -62.90628 | 2026-08-18 04:57:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed3b11c2-9545-3218-be7b-5433b312e537 | -8.72601 | -62.90981 | 2026-08-18 04:57:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 548161ef-68f2-33eb-8b28-c5025da863bb | -7.12163 | -47.54319 | 2026-08-18 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d401d610-cff4-3b61-96e4-96ec91d1806e | -14.23287 | -45.41444 | 2026-08-18 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d5b4a0d-fd16-32b8-902f-5b167b45cdbb | -11.12734 | -46.4917 | 2026-08-18 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8aed2734-e958-3630-83d8-94952fff5946 | -8.10017 | -61.35112 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a5504234-4962-3ece-ae5a-3df8f2a211fd | -8.57591 | -54.7 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| e31708c8-fca9-3fe1-9a4e-144a0b8484ac | -8.52963 | -54.90108 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d6bb434-4846-3370-b695-b34011820ce0 | -7.38177 | -55.48185 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b6fe18c-63d6-3af7-8ba9-bfa2d9bd8dd0 | -9.73079 | -60.74556 | 2026-08-18 04:57:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04df1dcf-15bf-311d-a081-a708acf3034c | -12.47001 | -54.18777 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3ffbc5c-2e53-38b3-93c8-fac5af6ef8d8 | -6.96059 | -59.02822 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2284feee-6d41-3e16-81d1-59472cf0e106 | -8.95616 | -60.5667 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README44.md)
