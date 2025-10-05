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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95ae6951-6df6-397a-beb2-0543421afcee | -8.51887 | -50.02822 | 2025-10-05 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ab606d8-8bbf-3f26-8b1f-a3e080484006 | -11.79463 | -48.91712 | 2025-10-05 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43b78c56-b80a-393b-a937-e8b0f92883b2 | -13.09726 | -47.83199 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c849483e-5bca-3eab-9618-8cccd2a1ed69 | -11.45921 | -51.51586 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79579996-9018-3491-9285-f8802bfe8b2d | -10.65846 | -47.79408 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b0652db-d54c-38d3-8f02-0eedc5dee637 | -8.59359 | -46.29872 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a5c8f756-df73-3101-9732-b3d49fe609a4 | -10.46315 | -57.50637 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fb6b4b6b-95aa-3a8b-b5d1-f446fdee072a | -11.9558 | -51.4927 | 2025-10-05 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f06e73f6-7867-3ef7-af47-b5cc1853b36b | -12.27005 | -53.92698 | 2025-10-05 04:46:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0015806c-7438-39f1-9f64-445a45247def | -6.64197 | -46.9637 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 43ad46de-7c0a-3bbf-8386-38f67f0475a2 | -6.23081 | -46.91672 | 2025-10-05 04:46:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a667f1d7-b3c7-3559-837f-b74433a7a652 | -13.13449 | -50.88839 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c173da17-d3b0-3136-9742-d9f4683b99df | -8.52215 | -47.21338 | 2025-10-05 04:46:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aef26d21-279c-367e-a536-97633644f902 | -10.6609 | -58.76168 | 2025-10-05 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b51ef53-4e52-35a8-8100-537f3d687b75 | -7.7257 | -46.31797 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a8445cb3-a95d-3803-8670-a0dd3a028a38 | -11.31936 | -53.96312 | 2025-10-05 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a3ca315-8858-3eb4-8540-0c1f5e9ded58 | -13.34997 | -48.05925 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fbbb276-38fd-3bd1-a2fe-de7ba0311f9e | -11.78292 | -47.94098 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3fdc3725-bdd5-3ccc-bb25-9fc65db25e16 | -6.61066 | -43.71808 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b07e4763-7506-3d6e-b240-3ae003e5edb4 | -11.83312 | -45.08591 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5b3ba7c1-be7b-3e3b-a935-71fff257360b | -13.30926 | -48.1245 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6756ef0-3406-37b5-b66e-93acabf95e37 | -9.88343 | -46.25578 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f872c51c-d207-3a8b-bfe9-b7afa780856a | -6.99512 | -44.21144 | 2025-10-05 04:46:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 97f0132d-a8ab-389e-b389-fc3b90a7aac8 | -11.63488 | -45.05795 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94afa083-1159-37f7-89c5-2e4815b0eafd | -14.01659 | -44.92732 | 2025-10-05 04:46:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a5fd100a-28ae-3c68-bfff-2d8071a036d0 | -6.61021 | -44.31643 | 2025-10-05 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6229f882-ebbc-33a2-9ac4-592fdd67c161 | -7.6318 | -45.48729 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| df5584c1-b640-35f3-a464-aa06dd4a934f | -13.08079 | -47.92046 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bed6995c-c63b-3970-b2a2-f961c463317d | -8.58493 | -46.30105 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3ef3f827-9769-32a7-a238-e669a1a0dbc8 | -7.25157 | -46.95558 | 2025-10-05 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0c290426-e999-33e4-bfac-9fcb83967a05 | -8.61056 | -54.96918 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7a4525f-0318-37a2-b5d4-1931775d2e08 | -7.43958 | -46.52156 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 46b10160-40f0-3b2d-ae0c-88286147c479 | -13.29072 | -47.58593 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0922c00d-f177-324f-b890-134627a09df7 | -13.26732 | -46.47446 | 2025-10-05 04:46:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| affd8dd3-ee44-3c84-9bf3-a729bfa1f3a9 | -11.07042 | -47.88777 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92fce251-68d3-3bf8-b04b-68decda149b7 | -11.01863 | -46.70174 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e66bd6c0-b53e-3ce7-9247-d997f2cf2096 | -12.30416 | -55.12067 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd82232c-5efe-3956-acf6-a4d207451c6c | -9.11361 | -46.70635 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cec992bf-0b88-334f-9956-bbda7d543622 | -11.12117 | -49.86355 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afcbf84f-dd80-3b8c-8b6b-7b55045b14ae | -13.85678 | -43.99292 | 2025-10-05 04:46:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 53c4e1e4-d1e1-34be-bb60-b6cd3e0e3182 | -12.86589 | -46.8593 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91d9cf60-07f8-3087-a1ea-08ab58ad8168 | -13.32177 | -47.56831 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66b3a799-7ca6-36fd-a899-1a496bee294f | -12.07577 | -45.15522 | 2025-10-05 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82ffd892-c5e7-36a4-83e0-f4cf46689913 | -13.47315 | -47.28128 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88ff725a-649f-39b2-881d-159639d94290 | -12.31366 | -55.13368 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 112ad972-ef45-3af9-ae28-532710f829f0 | -11.9497 | -51.48814 | 2025-10-05 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7940fad-92c0-3882-8990-5991727d2124 | -9.78136 | -47.73355 | 2025-10-05 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41dfdd92-6193-37b2-97fd-2b8d11d588da | -10.01175 | -48.2906 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ab617aa-c259-3aa0-b9a3-45f11e23b729 | -13.3337 | -48.06203 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d557d8e-1f72-3d72-8fa5-58896a067100 | -12.46763 | -45.52536 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 78e2f6cd-cdf2-3340-9db8-9232bfa0d632 | -11.23722 | -47.80589 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea741d09-06cd-3e6e-9fbd-a3f01e79a4b7 | -7.52305 | -41.2696 | 2025-10-05 04:46:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6183a715-9eb9-3355-bc9a-1eeb59131fe6 | -9.29209 | -45.66658 | 2025-10-05 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b0606b7-9b2a-3cb3-b226-cae1ba8d2d37 | -10.5848 | -48.69559 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ca5dee4-e6fb-3b0a-92e9-1e56b5cbba18 | -6.28033 | -46.35966 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ffb6990-0151-32f6-9163-087b2cb52de0 | -9.65006 | -45.85011 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8a91bd7c-047b-331d-810f-535422f23892 | -11.09402 | -47.88634 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5bd04394-5784-3ccd-9359-190f3617baee | -12.9754 | -51.0415 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 032da5aa-31d6-3220-892b-1fc821018225 | -8.54464 | -46.32187 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d9439f12-c457-3092-8f59-36600e94cbe7 | -13.25267 | -48.47955 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ec99609-b347-363c-8219-681ad3e1796c | -6.89871 | -52.19334 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e878f91e-dfd6-34bc-8675-cfdbc5df14cf | -8.6244 | -54.97595 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae34c346-fc9a-3fec-97e5-3b89bfcae0c3 | -13.4322 | -47.27505 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68f6dc5a-e912-3804-bc59-6b6e84755911 | -7.16319 | -46.2107 | 2025-10-05 04:46:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec897c14-005f-37dd-9c57-43385671f9f8 | -6.46038 | -44.5798 | 2025-10-05 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 95b6ad0d-942d-3b4f-880e-44c03d79f2ff | -7.34233 | -45.21292 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b094681-956a-3563-af8c-9df1204f66a0 | -11.09471 | -47.88148 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a3a17e3d-f00f-3c7f-bd07-f4d6d5cca126 | -13.27138 | -47.6081 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b176d061-296e-3fcf-8cfa-a7da79040314 | -12.48719 | -50.24509 | 2025-10-05 04:46:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b18107b-8604-3242-94ae-ad29da9612aa | -7.6986 | -42.58543 | 2025-10-05 04:46:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2d31a6df-4e5e-3c7b-af72-eae297e44b77 | -10.39861 | -45.40854 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed08a8d9-8521-3948-9457-313f7081485b | -8.53845 | -46.33585 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1f6cc8ec-5381-37be-b978-0cb5a49422c5 | -7.47228 | -42.63523 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fcf611d2-d582-3d37-9da9-e7b492bb496f | -11.81705 | -45.06434 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4c1f9c8-6f36-3877-b73f-d92fb54c52d5 | -13.1591 | -47.9621 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2a1fe060-f349-3dc4-8f6d-647280f1ec5d | -13.09255 | -47.92387 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cfc844f5-e1e1-33be-a626-546c92495dc7 | -9.80397 | -48.28011 | 2025-10-05 04:46:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 753e192c-d018-398d-87cf-ba3e59738771 | -13.27492 | -47.61213 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1e6f72a9-9c46-3958-86d2-41e9ddf470d0 | -7.79608 | -48.04712 | 2025-10-05 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e09364d5-bf07-34db-a453-36d23dc17f1a | -13.08365 | -47.90016 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e53a7daf-79e7-3bba-9efc-a72f21eeee56 | -9.36231 | -46.24259 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef761f1f-8e97-3628-80a3-ffd49395abf7 | -12.98214 | -51.04257 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 12f8c4d7-618c-3d52-aa6d-7e40cffc7a21 | -13.31929 | -48.08019 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d396806-74f8-3672-89be-2609ffb5502a | -6.73723 | -45.95593 | 2025-10-05 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 076fc17a-11f5-354f-b5fd-633b8161cc73 | -8.54641 | -46.28101 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4382c1e2-5fa7-3b70-99cc-cfbf1a7f9b52 | -13.27504 | -47.18118 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc4d3cd5-bffa-35cc-9692-d5492eb59df5 | -10.94653 | -47.0478 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b6dd04b-1694-3f0a-b8cf-c9fcf4dd1851 | -11.82837 | -45.08603 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a07c2d2f-273f-3ed2-bbfd-d045413eb892 | -7.0301 | -42.76988 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 65c281ec-3805-370a-bb45-2228ba22df6e | -12.14424 | -50.26499 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df1bccda-4134-3694-80dc-7ccb8bfa7e60 | -10.35446 | -48.16662 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 26e7d618-a866-3c45-9395-c86573ce8877 | -8.55208 | -46.27071 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8ce2c476-fde6-3d74-abbf-b11d4914bcd3 | -10.45208 | -48.37416 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c37f4f0-adad-3a68-b2cc-b689afd229f1 | -8.56179 | -46.26137 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2c519fb8-e3d8-3397-a74a-f666ddeae7a9 | -10.10375 | -48.33015 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| da8faf3a-c1dd-35bd-a3ca-193f7057fa7d | -7.64454 | -45.4892 | 2025-10-05 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d202bf44-09f7-3b7c-8afa-b94f53f0331d | -11.09322 | -47.75343 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9c99542d-837a-3ada-bded-2284eecde696 | -12.02206 | -49.7176 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54c5ac8a-bf04-3e43-8184-5f6260eee933 | -13.48443 | -47.22924 | 2025-10-05 04:46:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8fbbc4a-6221-31d2-b168-c9dc0748861b | -9.28353 | -45.66502 | 2025-10-05 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README98.md)
