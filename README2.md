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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53f137bc-2885-38dc-90b5-561f5766d9ce | -10.12668 | -52.19124 | 2026-06-17 00:05:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3da0dd2d-970e-30fb-ae31-09f487654970 | -10.12493 | -52.1771 | 2026-06-17 00:05:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 2b8a1219-6791-3b59-87d9-de1349759a6e | -12.16841 | -52.78717 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 650.7 |
| ab864c6a-8424-3b34-8cd5-eb556587ef39 | -12.19263 | -52.82998 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d75870ae-b113-3970-b778-d806e08b256f | -12.17491 | -52.78078 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4030.2 |
| 6281be7c-a4ab-377b-bfa6-70487f41b0c0 | -10.59839 | -44.32097 | 2026-06-17 00:05:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| af567051-903d-394e-b3f9-84483a976cac | -10.97909 | -47.7393 | 2026-06-17 00:05:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 3b2cef8b-0f19-318a-8acd-17752896a879 | -9.21622 | -47.9084 | 2026-06-17 00:05:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b7bfb065-c077-32f9-b87a-1c0192813497 | -12.23035 | -52.84264 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 6bb9f306-65a7-3635-9e70-0e7074fe466f | -12.22428 | -52.7916 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2511.2 |
| 81958ed4-826b-3387-869f-df9e7b4810f5 | -12.17254 | -52.82096 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 379adbd3-76fe-3bef-a9d8-e4260ce99af2 | -9.20862 | -47.91854 | 2026-06-17 00:05:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b0a241c0-949c-3770-9d73-8ae4a21c0595 | -12.19839 | -52.83489 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 009ea8df-dccf-378d-b3ae-8965bb2faa22 | -12.08565 | -54.61819 | 2026-06-17 00:05:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 285.1 |
| 5f80c342-bc26-39f5-9850-71f8e9d20b1c | -10.62954 | -49.02839 | 2026-06-17 00:05:00 | TERRA_M-M | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7f24c24d-7548-3bb9-9563-beeb7c25cb98 | -10.55876 | -46.24084 | 2026-06-17 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ad5b05c3-d8af-353b-9aef-37e3410622e3 | -12.1788 | -52.81458 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 235.1 |
| 5206f17b-625a-34e4-bf8b-60f24fa23e35 | -11.39562 | -47.81369 | 2026-06-17 00:05:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1f7b8d70-fc24-3ee1-8a8b-b28780c9518a | -12.16637 | -52.77049 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 368.6 |
| e2c353a6-13b2-3f70-9456-ef23b4629f77 | -8.94218 | -47.00068 | 2026-06-17 00:05:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1d38f4ac-d05c-39fe-a858-2201adaa72a3 | -10.16195 | -56.62197 | 2026-06-17 00:05:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| c2630b88-d4c8-3b09-b152-bf0b0700aa27 | -8.9679 | -46.98139 | 2026-06-17 00:05:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| adb378fb-1881-3316-8d56-55c94cb6b959 | -12.19003 | -52.76753 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1769.2 |
| 26272cda-d93d-3ca9-9db8-d58cc0833e44 | -12.14676 | -52.80709 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 93c30aa9-a615-3f57-a81f-db91b637ff02 | -12.23818 | -52.80707 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 0fadc7f0-e517-3452-80c7-29c7f329e9b4 | -9.32558 | -45.48641 | 2026-06-17 00:05:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 2e22906e-a219-33b1-be43-64b8eefb8689 | -8.97046 | -46.99959 | 2026-06-17 00:05:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 12cc8007-261a-337c-90a7-1716475ff917 | -12.146 | -48.46393 | 2026-06-17 00:05:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 677ca572-73be-30da-b904-fa0b92291e02 | -10.98032 | -47.74825 | 2026-06-17 00:05:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a4ff68c4-e545-366c-84b6-71e1723b0161 | -12.21442 | -52.81004 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| af0cf146-4406-3e05-bdc2-c56099a938ca | -12.15374 | -48.45333 | 2026-06-17 00:05:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 74c38363-66a6-379b-82c8-f74e8d6301e9 | -10.77624 | -54.10877 | 2026-06-17 00:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 6b473683-2ae3-38b7-add0-1c633e41bb9e | -11.88654 | -43.82375 | 2026-06-17 00:05:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 752abed0-4ebb-3a5f-b6f6-624682ca6415 | -12.18025 | -52.78568 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4031.0 |
| d4720d51-3e8a-36d3-9e95-92ac0f5277e4 | -10.55743 | -46.23146 | 2026-06-17 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 7c8bde8d-03b1-3331-9e6b-27b55d2b0af2 | -8.95261 | -47.0022 | 2026-06-17 00:05:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 00ef346d-d763-3833-86c2-02231254f98f | -9.2074 | -47.90966 | 2026-06-17 00:05:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 308f2d83-b7ed-3d2f-b871-153cc97747b9 | -12.23412 | -52.77327 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 202.8 |
| 07cc7787-a6e1-3369-9e7f-3661cebe3275 | -12.18233 | -52.80257 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 429.9 |
| 4d9dc5ca-026f-35ce-89ef-fe0c0af08bde | -12.21242 | -52.79309 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 253.4 |
| dde6aa24-7638-3e50-ade5-2883fe443d0f | -5.59332 | -43.50896 | 2026-06-17 00:07:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 8501f9b0-e35b-334e-a675-0f61c27c09b8 | -3.72856 | -49.27681 | 2026-06-17 00:07:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5935e6b3-6634-3ecf-b5e7-f42117e1e148 | -7.84473 | -48.39103 | 2026-06-17 00:07:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3c213e28-79c8-346e-acb4-dc9dec161240 | -6.63528 | -44.58727 | 2026-06-17 00:07:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 15c5ab8c-50a0-37df-99fb-bb35e3bb405d | -7.84594 | -48.39988 | 2026-06-17 00:07:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6b304580-cb62-3dd0-a63c-ce138c8a48b8 | -8.27263 | -48.2183 | 2026-06-17 00:07:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7f365f3d-f3f1-38cb-96f2-48e99f43e0f6 | -5.58983 | -43.50381 | 2026-06-17 00:07:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 87a037c5-e27a-35f4-aa4c-38bbead7dc7a | -6.17482 | -48.50263 | 2026-06-17 00:07:00 | TERRA_M-M | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 41ba5658-5508-3e65-895a-5b772809fe3d | -3.51297 | -48.04256 | 2026-06-17 00:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 578fce72-0a00-3ac3-87ec-5fb4ff694853 | -5.13812 | -47.99646 | 2026-06-17 00:07:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fd4fe8d1-79ab-3819-85c5-0eabf3e69064 | -7.37305 | -49.85849 | 2026-06-17 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8de67027-c74e-3abe-a6dd-2876eed1f52b | -8.18966 | -46.75819 | 2026-06-17 00:07:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 08e2b362-c967-32a4-9533-08bca45cf3fb | -4.35852 | -47.76004 | 2026-06-17 00:07:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 3ea50a5f-86d9-318e-864d-ad032a9d3ebd | -5.79908 | -45.10044 | 2026-06-17 00:07:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7cbf4e1d-8eb5-3964-9caf-d4dbea17e5db | -5.79568 | -45.07663 | 2026-06-17 00:07:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 163.4 |
| f2035fa9-6d71-3bf6-8135-eb7f42084964 | -5.84195 | -43.48584 | 2026-06-17 00:07:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 523f2fe0-6f70-34e3-a9f4-1a3caa23d1c7 | -7.63452 | -50.02828 | 2026-06-17 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b1576ed0-597b-334b-8835-fa029b7496e5 | -4.35981 | -47.76917 | 2026-06-17 00:07:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| c223cc10-e27c-3636-a151-068c20aea4fd | -7.35483 | -49.861 | 2026-06-17 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 431bce2f-dbff-3346-8eda-7eb1ee899114 | -3.51172 | -48.03355 | 2026-06-17 00:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| f50acb9c-28fb-33b3-99a0-4cf7704adf92 | -5.79738 | -45.08856 | 2026-06-17 00:07:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| ce4604ca-748d-36a2-930d-99ff632f76b2 | -5.79395 | -45.06455 | 2026-06-17 00:07:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 577d03ae-ec1e-3e30-b861-148fa2791b87 | -6.973 | -42.88424 | 2026-06-17 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| e26d8507-c8c9-3781-acc0-939a442df588 | -8.56947 | -45.99552 | 2026-06-17 00:07:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 4b8d75db-1ee6-3618-87c6-c18f58d570a8 | -8.28146 | -48.21705 | 2026-06-17 00:07:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 50bc487c-93b5-3d45-9318-e8f589ff8fba | -6.28973 | -43.64036 | 2026-06-17 00:07:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0f2244c2-f6c8-3540-8076-5635e8206f94 | -7.75941 | -47.56389 | 2026-06-17 00:07:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f9161fd3-2902-392e-af05-49415e59a6a2 | -3.79845 | -49.18 | 2026-06-17 00:07:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a779043a-e24a-354c-8158-7b940a5bf363 | -7.8359 | -48.39227 | 2026-06-17 00:07:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 32c54446-f2d9-39d1-9346-cc0b9188bc31 | -8.6811 | -47.84042 | 2026-06-17 00:07:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 116438b5-b6ca-3b55-9e31-34a9bf7d0d9d | -5.11067 | -43.75591 | 2026-06-17 00:07:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 412fa4fe-21f5-33b9-9f7c-fc0a5c4a10f1 | -8.20002 | -46.76621 | 2026-06-17 00:07:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 535ef920-a119-3a71-8431-137468ae75b9 | -4.34982 | -47.76719 | 2026-06-17 00:07:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 5ce93de9-8b3a-3a26-964b-7524e057cf8d | -5.38832 | -49.28633 | 2026-06-17 00:07:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ca404196-26ea-345b-8b30-9e82b53e0509 | -8.56803 | -45.98554 | 2026-06-17 00:07:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4ee00dff-d981-327d-9980-b86a83ff2e95 | -7.35611 | -49.87047 | 2026-06-17 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 473401b6-03d0-34c5-9b8f-6f96c812eba1 | -8.68233 | -47.8493 | 2026-06-17 00:07:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 5f022faf-e5f8-3424-9f30-4668f417acb8 | -6.63341 | -44.57438 | 2026-06-17 00:07:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 46875780-a0cb-3246-a036-f6c0713559af | -7.63323 | -50.01861 | 2026-06-17 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1723b94e-ddeb-3d61-8218-54c582f6c764 | -5.91496 | -45.55087 | 2026-06-17 00:07:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 51969aa3-e688-3147-96a6-da3d602e4458 | -5.21816 | -47.51697 | 2026-06-17 00:07:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c719e08c-93ff-30dc-b62c-4ff983cb0e38 | -4.34855 | -47.75802 | 2026-06-17 00:07:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 12fdbf8b-12f1-39d3-ae46-8c7fae6a7798 | -6.14958 | -48.51517 | 2026-06-17 00:07:00 | TERRA_M-M | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 584cbe7b-79e9-3f51-bcc0-c8c9b85139a9 | -8.17175 | -49.50233 | 2026-06-17 00:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 426e9b6c-990f-3b1a-877f-56bef6f11dd3 | -9.3048 | -45.4581 | 2026-06-17 00:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 49.7 |
| b37fbc78-4c79-364c-832f-9b0c167b4fbe | -9.3045 | -45.4809 | 2026-06-17 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f25dad27-81fa-384f-a767-5c5708a34c6f | -5.7945 | -45.0586 | 2026-06-17 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 98cb4958-52ad-3d42-a5c8-fcddc164919d | -10.5637 | -46.2135 | 2026-06-17 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| ff382786-d605-36aa-a76f-1a60e91ff676 | -4.3588 | -47.7636 | 2026-06-17 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 115bedc3-8fd9-359c-b94f-25513e79baa9 | -5.7943 | -45.0813 | 2026-06-17 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 6fe44594-79da-3761-a53f-cc17d91a1382 | -10.5634 | -46.2362 | 2026-06-17 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 40328e9b-70d4-36d1-8c7a-651ac8cfcaaa | -12.8354 | -44.3657 | 2026-06-17 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 349bba1a-f52b-3bf6-a7da-48bc50a7e934 | -9.3234 | -45.4787 | 2026-06-17 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 7226a341-573a-341b-ba6e-ee013154a146 | -12.0756 | -54.6131 | 2026-06-17 00:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 135.2 |
| bb8f80e8-1c41-3fe4-8a7d-78b49525aeb9 | -9.3237 | -45.4559 | 2026-06-17 00:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 9fbd71b1-05ef-3f3b-bd1d-7a913611ac58 | -12.8548 | -44.3625 | 2026-06-17 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 881b39c8-6cde-3ac6-9563-e4f8bc628f01 | -12.0945 | -54.6113 | 2026-06-17 00:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| dae9b624-171a-35df-a5cd-e3b59aef0a41 | -12.0758 | -54.5926 | 2026-06-17 00:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 2bcf44ce-c2ce-38ed-8461-079ca0314882 | -12.8354 | -44.3657 | 2026-06-17 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 23839600-60ac-39f1-ae38-040f4ccde25e | -12.0945 | -54.6113 | 2026-06-17 00:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 125.2 |


[Clique aqui para ver as próximas entradas](README3.md)
