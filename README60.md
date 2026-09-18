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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f757640b-2733-3607-9b63-f90207895f5e | -9.15776 | -49.98985 | 2026-09-18 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac2eb267-a8f0-301b-8fcc-d1ea1af4c9b0 | -13.24612 | -46.91192 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 92a8b308-0240-327d-b071-24c02e6998f4 | -12.5549 | -50.72982 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 101e6cff-8dc2-3512-8555-ecc7b46727a5 | -10.63984 | -50.23668 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b3be6ec-535c-3c10-9f0d-833ca0685287 | -12.16803 | -46.99086 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 520587f9-794e-3d02-9a62-1525315e31dd | -11.27985 | -43.37428 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c534ae18-8a2a-3905-8737-9d9697fc4637 | -10.62589 | -46.06527 | 2026-09-18 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fc613dc-1a91-3b1f-b07c-9d93be7e6063 | -9.59331 | -45.87027 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e0f78bf-e177-348f-b0b6-33fe7e20424f | -9.3986 | -46.85828 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 569bfc48-3e81-350a-a9ae-61ded637132f | -8.92933 | -51.45979 | 2026-09-18 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cc2cb06-f45d-341b-8823-3c23c580689c | -6.33565 | -45.66955 | 2026-09-18 04:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e4420106-15de-3894-93ee-c0cf0fa16c58 | -11.55411 | -46.89501 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0ef6906f-3ea3-3470-b5eb-ea0b4e689e17 | -10.11702 | -46.2984 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bdf59fa6-ab21-3498-9f70-8a5ea46f6a23 | -7.19073 | -44.43925 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa9694f6-20c7-3b18-81e8-8058d35ff42f | -8.77924 | -46.90516 | 2026-09-18 04:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4b0bc559-689a-3c66-8920-35390d0660b5 | -9.93764 | -45.32338 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 946a2ec2-d50a-3b22-ae0a-f8c76ebc5623 | -9.48092 | -54.48107 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| be9542d7-f485-350d-96de-1e41553e8d6b | -6.93553 | -46.15451 | 2026-09-18 04:57:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1100ecf-562e-3cb7-87b3-06a04b1480fd | -12.4775 | -50.69149 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f86f8e4-e2bd-32fc-b72b-04a62fba7192 | -12.39316 | -48.47766 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| abf9d3f8-9227-3d94-96c1-454c97db6f0e | -6.51914 | -49.8874 | 2026-09-18 04:57:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c381361-a662-39d0-b2c6-3e20e97ae2a9 | -12.67808 | -43.9121 | 2026-09-18 04:57:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c879fbe4-e850-31c6-9eb0-0617ad59319e | -12.30906 | -50.74153 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65a4cbfe-35bf-3eda-86bf-85a515d77eb7 | -8.4878 | -46.88617 | 2026-09-18 04:57:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 20ded03d-ae97-38bc-8f89-0c6ff3b46874 | -12.5606 | -50.73839 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ca3c719-532a-3437-a8db-06410a198b2f | -10.65699 | -50.46717 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc384fed-61cd-33fc-ad6c-f83566643a77 | -8.54071 | -44.54922 | 2026-09-18 04:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 143c285c-d569-341d-b754-abd53f4233ed | -12.16789 | -46.97952 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb5e38f9-2e3b-34db-93f3-363f33f763f1 | -9.59443 | -45.86238 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59867c17-3069-34b9-b90e-a7f30ecb8e95 | -7.36422 | -44.4664 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 17a27c10-a214-3878-a84d-ec17b4ea8319 | -12.16378 | -46.97875 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fdf82a56-5a60-3608-9e0d-80480d787f1f | -9.95054 | -45.68639 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4a522428-d62e-39ba-bc63-31f2b1521957 | -10.32242 | -45.32473 | 2026-09-18 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0f80bc5-3be0-334f-9863-daf4800f0924 | -10.66497 | -50.27881 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4688ffdd-a21c-3225-9ebb-9c586cd9894f | -9.91393 | -46.54937 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40de0f3b-8972-3d34-b1cc-0992f3f7ef57 | -12.55832 | -50.73036 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af6999d7-c934-3aab-83f2-9776df6940ca | -9.56347 | -45.45115 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 977cbc30-b1ab-35c5-b360-8dd2956c6e21 | -10.11682 | -46.29971 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35f7cfcb-7b53-3834-89e5-918e7f7d03d2 | -7.81605 | -45.1044 | 2026-09-18 04:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46faf663-194f-3444-b86b-b1feee2c7548 | -6.17672 | -53.59018 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b63fe932-2fae-3233-9737-0136603b0936 | -6.33576 | -45.68646 | 2026-09-18 04:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b5189ef-cc73-3cc8-9c0b-77e20c69b21a | -7.36878 | -44.46708 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| da07ccea-d04d-39f3-bb7a-8df7bad221e7 | -9.9419 | -45.29194 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c6c66649-474a-3639-aa24-1d1ecb5660e8 | -7.79943 | -44.90898 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8a6f60b8-8011-3485-9271-c8ac89e89a28 | -4.7946 | -56.12433 | 2026-09-18 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 37740734-80a4-3fdb-aedb-00984625b778 | -6.78318 | -47.86414 | 2026-09-18 04:57:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5271456-b757-3f45-ab2f-ca6647938097 | -10.64497 | -50.226 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0bd4cec-1af0-3240-8194-ed05a3a86ad9 | -6.4321 | -47.24961 | 2026-09-18 04:57:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6513f773-e94c-3e2e-9fdc-e4b16fb6a638 | -4.51209 | -56.07794 | 2026-09-18 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6039b633-222b-3a67-9a7b-c969b9339206 | -7.87652 | -54.72285 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c69acc24-825e-3c92-8b5c-79ecb35ed932 | -10.41168 | -48.67562 | 2026-09-18 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76863e0e-5e1a-3b7e-bc55-45202671ae90 | -10.60316 | -43.33312 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db689bbc-787f-33e7-9bfc-074041bff739 | -12.45867 | -50.70005 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffbc6e31-369e-3370-9c23-ddb4ba0d0fe6 | -12.4125 | -50.70428 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a0c59dc-8f06-37da-aec0-aa296341e524 | -10.64726 | -50.23401 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d1a6ff3-3eee-3869-93dd-202c80059db8 | -10.09863 | -48.85571 | 2026-09-18 04:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88349f35-c8b1-3b3b-8a88-fd6590d407ca | -8.74292 | -45.40676 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6165b45-f448-34e1-92ed-594cfd0c4221 | -6.44279 | -44.94875 | 2026-09-18 04:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f3ecb34-38c5-3dbf-80ed-4d1e428f0253 | -12.32726 | -50.75966 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51e049b7-570b-37d4-849c-9ef123271855 | -12.2653 | -50.7537 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 773e0b42-431e-3d4e-b676-f2008956671d | -7.67286 | -46.09021 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d090d73-d2df-309f-bdaa-142afe7bdfff | -12.17315 | -46.97224 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 980071ad-b5ab-364a-bf6b-4607f5cb38fe | -10.66554 | -50.27508 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8b3e01ac-b29a-331d-a50b-29dd8342f639 | -8.71266 | -44.88389 | 2026-09-18 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48cf2a7d-31e6-3eb3-9f73-fcf8295b4934 | -7.67488 | -46.1055 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1752d32a-9850-3649-b677-4b12c72f5dc2 | -8.77995 | -46.90025 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b39d13d-7e94-310d-a35d-e6b9a325982f | -5.8679 | -52.05499 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5594e576-6c91-3306-bb84-49e4a17271ad | -9.91289 | -46.55663 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11cd6087-fc91-3625-a2b8-bb036f390e9f | -7.66171 | -46.08908 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23fffc9d-a103-3069-b435-9cb34e8ab9fc | -6.66011 | -50.92377 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70717bc9-8fec-3dda-a13b-227d4771e9dd | -12.55775 | -50.7341 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42e98daa-8459-3792-aadb-afc49e74e626 | -7.00866 | -43.63003 | 2026-09-18 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 090038c1-ac78-39ea-a6d7-3bd458a821a7 | -11.30863 | -46.77069 | 2026-09-18 04:57:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6c42046-96a8-342c-b7ac-1468ce16163b | -10.61275 | -46.55374 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e76b8f0-5443-3bed-9e98-2d143d1ddcb2 | -11.6388 | -51.58497 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 168ed586-7ff4-316d-93f6-40dc3a303cfd | -10.11635 | -45.65086 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a6d9b4ae-41ef-3a3f-9574-ace4b2044cd9 | -10.32944 | -45.30724 | 2026-09-18 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72bd9e10-b944-3daf-a38a-2057d1923c06 | -13.35742 | -46.29862 | 2026-09-18 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a98dae5-7c3b-364f-8931-e20460ade277 | -7.86388 | -46.4307 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0c8c6964-ff61-351f-a397-4ff24bd9cc4b | -6.32047 | -55.27386 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fef44ff9-e5b8-38de-bd87-b4b48d6e8ff7 | -10.63529 | -50.24361 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 847c1943-89f8-3f11-9526-26b2893a5ec2 | -10.67352 | -50.26868 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f150dc6-25ca-3317-a9c8-dd36e0155b39 | -10.02097 | -51.10351 | 2026-09-18 04:57:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69f2a74c-cbec-35a3-b394-ec0850210595 | -9.84711 | -48.39128 | 2026-09-18 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6abe8f1f-3671-3a1e-9907-716b5082c848 | -7.43514 | -44.55427 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65ab730c-3879-3c91-823a-e25ffdfddcb5 | -9.1886 | -45.69686 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e061e6d7-8997-37a8-b747-e0f295722b19 | -11.32677 | -46.76192 | 2026-09-18 04:57:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b95265c-33aa-3ecf-9aa8-4ea6f8e138a3 | -8.56121 | -44.89635 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4829742e-67fd-3be7-81d7-647fddac9b9a | -11.33967 | -43.97732 | 2026-09-18 04:57:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25afd88f-2696-3917-abb0-0ec687335075 | -10.53594 | -44.84674 | 2026-09-18 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f025067-5556-38d6-ba23-f52392aa4df9 | -8.47194 | -44.53577 | 2026-09-18 04:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 542fb2bc-6a1a-314d-8340-5396b600212b | -7.00312 | -43.6345 | 2026-09-18 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9a9af96f-0915-3c73-8011-2dcb00130dfb | -4.88108 | -56.06625 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcf054d5-4a3d-3a5a-8852-889cc48b71b3 | -9.60535 | -45.84715 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86f86efa-df8a-3b19-a715-b6c3fb9ce123 | -9.92385 | -46.50914 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99323e22-5854-3e29-bf96-d0fdc45d89ef | -9.74906 | -46.57894 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67a0ff0f-87fe-3fc5-bef7-4d594da6fdca | -10.79603 | -46.65626 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14a0107b-1718-3640-b614-7b35a7e3dae8 | -11.32513 | -43.39309 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c3e3fe8-1061-3362-aa6f-47a36f99996f | -6.66951 | -50.90745 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbd6f054-df3d-37aa-bd63-c39cb319e531 | -10.67524 | -50.2575 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README61.md)
