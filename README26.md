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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d2e336d-7bb2-3dae-987c-19913d5d9357 | -6.13862 | -43.96843 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ea4b4f1f-3719-3eb9-93ab-0d47a72c6d5e | -2.7948 | -48.57549 | 2024-11-06 03:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab44a077-613c-3c36-9a81-a68b194567a3 | -6.49287 | -44.6792 | 2024-11-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4060ac42-6a63-32ea-b0ff-059eccafc740 | -5.89874 | -39.61091 | 2024-11-06 03:49:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f2e325e3-7b16-3cf5-b208-91e990926654 | -6.0105 | -38.66028 | 2024-11-06 03:49:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 36664f60-4824-367b-9fff-9695a044ebc7 | -4.13429 | -43.57341 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0d7da805-4ad3-33f6-aa81-42c9950c1ce5 | -7.42141 | -43.77816 | 2024-11-06 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e861a68b-5d03-3ce6-80a8-5c9811081adc | -4.36621 | -45.76313 | 2024-11-06 03:49:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4ee8390-9026-304d-80ec-759571117ecc | -4.00273 | -43.25288 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5938e745-6e7b-344c-8c39-21c8f4a77b49 | -6.13989 | -43.97005 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 11165866-f352-35e6-af34-b351ce8ab397 | -2.84427 | -49.47801 | 2024-11-06 03:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 8e49e7fa-4ca7-3406-be2b-336741cae063 | -6.32819 | -39.51346 | 2024-11-06 03:49:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 37ca2500-1e3e-35aa-ac9b-3aef57160d99 | -7.29044 | -38.9368 | 2024-11-06 03:49:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9f515bec-564b-3c72-8c2f-8e54e4357142 | -9.04206 | -35.44282 | 2024-11-06 03:49:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 06988507-0afe-3853-86a9-770f6ec1bb80 | -7.26018 | -38.951 | 2024-11-06 03:49:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ec5f40e3-5c6f-3016-a110-4ba6858618d4 | -4.8208 | -48.56139 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 70a6b53c-b9a9-3cdc-9019-c5c5f7d276d6 | -3.20626 | -49.22858 | 2024-11-06 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b50575d-e66d-34c0-b4f9-51135865a0db | -7.36057 | -42.46773 | 2024-11-06 03:49:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 65dfff4d-8413-33fb-bbbb-8b1630c39d9a | -3.7409 | -50.07 | 2024-11-06 03:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 631a5e7e-31a9-3fef-8d6c-a79c8085c6d7 | -6.50015 | -47.4946 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 8d9fa959-80ec-337c-9368-2ad966cbd59f | -6.4958 | -47.48504 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 75b9280f-4c01-39c5-957f-88a8732d29b9 | -2.7861 | -48.57487 | 2024-11-06 03:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b80368d7-14dc-382f-98d5-d40369489130 | -4.30044 | -46.35151 | 2024-11-06 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 289f3009-e92d-33e8-8c43-21bc1b0acfed | -7.37669 | -43.51147 | 2024-11-06 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8646a9ed-a75a-3da1-a79d-0e29eadfa4e1 | -5.71828 | -43.81479 | 2024-11-06 03:49:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7488be27-1142-3baf-9246-ebc8317db4b4 | -7.33813 | -35.0729 | 2024-11-06 03:49:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 945eb4de-26a0-39b0-b36d-0732fc7cd059 | -6.61645 | -43.69109 | 2024-11-06 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ccd3332-f74d-3e26-99f1-ef763fe36478 | -3.96105 | -48.15621 | 2024-11-06 03:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0d9d27a-f448-31b3-9685-74517329a3ce | -4.68275 | -46.39756 | 2024-11-06 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2b529af3-5654-3dc0-a71d-ae910f63a5e7 | -6.48803 | -44.67829 | 2024-11-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ba4c660e-ed1a-314c-bed0-3feb56faf761 | -5.63702 | -44.18575 | 2024-11-06 03:49:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a03b791-40e5-3bcb-8ad2-5657dbb893f1 | -5.02273 | -43.6036 | 2024-11-06 03:49:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a691b47e-ac02-35e1-bed5-ad793e17bb2d | -5.42779 | -46.41822 | 2024-11-06 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca6bd220-ccaf-3c33-9fdc-c2d465c6dfdf | -4.68345 | -46.39352 | 2024-11-06 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b1cd64bc-3950-3c59-a19c-50c92ae3f1b4 | -5.56231 | -43.70257 | 2024-11-06 03:49:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40c34963-a13b-3f44-ba3c-af1c6fdb0b24 | -6.75411 | -39.25898 | 2024-11-06 03:49:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cb346e10-0b4d-3b13-8056-a387889143f0 | -8.50602 | -42.08828 | 2024-11-06 03:49:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| bfed2ac9-ae48-31ed-a5da-9ffef77c8419 | -5.15497 | -43.77359 | 2024-11-06 03:49:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3ea7b48-329c-3a1b-980c-05310a85e89c | -3.54426 | -44.62901 | 2024-11-06 03:49:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27407e1f-aee1-3dd6-8d38-125b974a2d02 | -4.13267 | -43.58334 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 837785dd-9f5a-3071-950a-6180a846546f | -6.67023 | -37.45531 | 2024-11-06 03:49:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 059fbd97-7884-3a36-8864-55d1c9865c34 | -8.49809 | -42.08715 | 2024-11-06 03:49:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0c486f63-65eb-3f89-80d9-3f1529f1848f | -3.5518 | -47.38295 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 119913f4-f4f2-35eb-ad2c-c18ab9162b35 | -6.66969 | -37.45878 | 2024-11-06 03:49:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9be1474b-bde2-3775-a0d4-3225f9cec6b0 | -4.77267 | -48.68133 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| feebf3e0-edc0-304d-8233-d80413e75bd6 | -4.81989 | -48.5665 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76fbb315-f832-33b1-ad53-9e9bfd6fa167 | -6.13354 | -44.70313 | 2024-11-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dab6beb2-0fe5-3938-8cdf-2d85df81dfa6 | -3.96649 | -48.16247 | 2024-11-06 03:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4671342-c4d9-3470-a162-c9c1062c3052 | -3.07006 | -47.76989 | 2024-11-06 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 725e02b9-99e0-3bbd-8823-6ef0df050591 | -4.65631 | -43.81799 | 2024-11-06 03:49:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a5918d3-1dea-3ef6-bc04-57329e9c61fc | -9.62696 | -35.8685 | 2024-11-06 03:49:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| c7485316-901c-3ec2-8176-138263983965 | -4.68908 | -46.39432 | 2024-11-06 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b9bb6c3-f164-3fe0-96e7-b0d4860678f1 | -4.12879 | -43.57764 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| bd7b9b86-a6be-37b4-b974-bdf6ef135c88 | -4.38198 | -45.80144 | 2024-11-06 03:49:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 942ada0b-0559-3f5d-b91f-d9d4dd57ae28 | -3.53957 | -47.38131 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 9a059148-34e5-335a-839a-0986b95f9572 | -3.28542 | -45.45146 | 2024-11-06 03:49:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce630261-fbe4-3ef1-84e0-0e314d9c1d96 | -3.54402 | -47.39185 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 068b82d6-de90-34d3-9c24-a42895ece041 | -5.58791 | -35.82135 | 2024-11-06 03:49:00 | NOAA-21 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0eff4aaf-925f-3411-9847-5977279285ab | -4.68978 | -46.39028 | 2024-11-06 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 622fb528-9175-393a-b133-a6220b9da171 | -4.58985 | -45.49881 | 2024-11-06 03:49:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 447dd34e-55e4-3156-8eb7-17a745960749 | -7.01674 | -39.99437 | 2024-11-06 03:49:00 | NOAA-21 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 433a5b42-d139-37e3-97af-22dca60829bc | -4.65886 | -43.82142 | 2024-11-06 03:49:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6fb54b06-e8b8-35a7-bd16-c0b4cf394825 | -4.55384 | -48.01151 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| a0be2f7c-c3e3-3e09-bf1c-ff1c8773a1db | -4.12328 | -43.58197 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 2e4573ac-0c4f-3644-a342-94140bbee913 | -4.06168 | -50.01994 | 2024-11-06 03:49:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd96f38b-fddd-3a6d-9efd-04b68ef0c836 | -3.54033 | -47.37689 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 0c102ff0-0930-37f3-8bf9-fdeae3f825aa | -10.57917 | -37.03117 | 2024-11-06 03:49:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 85bfcedf-4677-368b-8e42-a10c6c5ec19a | -6.10648 | -43.9697 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 087c91b6-c5d0-30fc-9767-775f3403d05b | -6.50157 | -44.68665 | 2024-11-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 1f7601f7-1396-3436-8bba-a7b0b0ff6c16 | -5.02733 | -43.6045 | 2024-11-06 03:49:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4d7a2b23-b993-36eb-a808-c67ae283a338 | -3.5249 | -44.72639 | 2024-11-06 03:49:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fab3e573-c035-39e9-9bd8-6705a1893331 | -7.50101 | -40.53093 | 2024-11-06 03:49:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 682dc4f7-85c2-39ac-95ee-406c5ddadf06 | -4.13816 | -43.57912 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| d13ccff6-28c1-3258-88f8-3e125bf34651 | -3.54317 | -47.39684 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ea4e829-7b3e-331e-97d3-b9dff85582e5 | -4.5571 | -48.01959 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e67329b6-de84-3153-aa38-5e5a95838f3a | -6.49435 | -47.49329 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| e1b4550e-3c28-3525-989b-d96d69b1d313 | -7.24743 | -40.0656 | 2024-11-06 03:49:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dc5e6777-9553-30ec-a4c7-c53da621b950 | -2.84318 | -49.48458 | 2024-11-06 03:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f035ce5e-43e0-398d-9f00-dbd80af69818 | -4.58887 | -45.49914 | 2024-11-06 03:49:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 038ce69b-191d-3490-ad99-9aa0dca61496 | -3.21181 | -49.23158 | 2024-11-06 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 01236fa5-3c2e-318d-9474-12f0c86a8a31 | -4.69855 | -45.64705 | 2024-11-06 03:49:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11c92460-f7d8-3622-a2a1-dca15d0ecd03 | -4.56093 | -48.0076 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5c537cb1-dad2-3573-8b33-4b15e1a78a88 | -7.2261 | -42.8847 | 2024-11-06 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 137a0a46-c8b1-36bc-9e78-c57e8311cfa9 | -5.54438 | -44.32883 | 2024-11-06 03:49:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ac22b2c-f966-366c-b64d-694a7e68e4a5 | -7.83426 | -35.0377 | 2024-11-06 03:49:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 3529daac-fed3-3404-a64c-478f655c8d57 | -5.93702 | -43.77348 | 2024-11-06 03:49:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 218ce92c-e20c-3bbd-9cb9-dfb3e65b3622 | -6.3369 | -43.39841 | 2024-11-06 03:49:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4bb8a74-d9f5-3b6c-83b4-0d819200928b | -7.50039 | -43.84242 | 2024-11-06 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7bc887f7-b3eb-3e1a-b241-fe432ccf1f95 | -6.53029 | -44.46289 | 2024-11-06 03:49:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd43f8c4-cb2b-3f2a-9ff4-a1940e6d2e53 | -5.66386 | -45.93808 | 2024-11-06 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 63fc4623-61c5-3261-971e-f9c0ba624f29 | -7.04273 | -39.25239 | 2024-11-06 03:49:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fa7468ba-3378-3c45-8533-5acb90d95bc5 | -9.86839 | -44.97252 | 2024-11-06 03:49:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d93a88f8-07b8-3e1f-b088-f014e08da6ca | -6.93661 | -47.79191 | 2024-11-06 03:49:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3dde81e5-6ede-3db0-baaf-5403072bd8ad | -5.7443 | -35.55776 | 2024-11-06 03:49:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 36f5ecea-c4e4-3519-bdce-46818ea0f691 | -3.97286 | -48.16336 | 2024-11-06 03:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b287787d-e3eb-380c-aa22-ec2ade44c74e | -5.54336 | -44.3308 | 2024-11-06 03:49:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70dac9f1-338f-3862-a0aa-53395b65814a | -3.21289 | -49.2251 | 2024-11-06 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f99c86e5-766a-386f-a1d2-bc241f1ddfab | -6.05397 | -39.43782 | 2024-11-06 03:49:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c616a83a-f29b-3031-b585-3e7a04cc253c | -5.66444 | -45.93469 | 2024-11-06 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 652cbab8-c0d8-3768-900a-f4e7d7bd5a1e | -6.12431 | -43.97748 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |


[Clique aqui para ver as próximas entradas](README27.md)
