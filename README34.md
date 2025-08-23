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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5a393b5-1cd9-306c-bfe0-ebc284d8be66 | -22.17819 | -43.28714 | 2025-08-23 04:04:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 902e89c5-7535-33a9-a99a-027e64bdb6af | -22.47465 | -44.27135 | 2025-08-23 04:04:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 9afd8418-03d5-3135-964b-603667eb5612 | -23.49994 | -45.99829 | 2025-08-23 04:04:00 | NOAA-20 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 45013145-7aff-3a80-b2c4-67503e4efaaa | -20.22533 | -46.71369 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1131485e-b653-3867-a83f-a907705c9481 | -16.33183 | -46.77424 | 2025-08-23 04:04:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58307a9e-420c-3154-9799-b6ab7fcccebe | -17.96455 | -42.9002 | 2025-08-23 04:04:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f3cfbb05-aef4-323b-8e57-76ea5c15e8d3 | -16.42089 | -49.15482 | 2025-08-23 04:04:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a81fff7f-3764-30a1-9ed1-090298e6f4c9 | -22.12362 | -41.38188 | 2025-08-23 04:04:00 | NOAA-20 | QUISSAMÃ | RIO DE JANEIRO | Brasil | 3304151 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 71873923-11c4-3bcd-b00e-c5b4989f8ef3 | -19.38569 | -41.44513 | 2025-08-23 04:04:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 02a380e4-9712-3d32-8efd-1b57a840c774 | -20.96902 | -49.7696 | 2025-08-23 04:04:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d9641f30-da8a-3050-b758-1e058f843637 | -17.3223 | -46.56724 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05a3e392-bee3-3936-88cc-8c5e6e98b5c4 | -14.6179 | -54.80908 | 2025-08-23 04:04:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c7dfd144-1096-3c18-a392-85449c7a35ee | -16.42177 | -49.15024 | 2025-08-23 04:04:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a3ef429-e469-31f4-a8e5-bc9cfc23c50f | -14.66673 | -54.93232 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bfa653f1-4457-3511-a450-7b165e424499 | -14.66269 | -54.91909 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c8952ff3-cad2-3dbc-a220-bafdf84704f0 | -15.03024 | -54.89768 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| aee4aad0-d940-3e45-89d0-fb43ed08c9fa | -17.80668 | -52.06823 | 2025-08-23 04:04:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73ee22ee-8865-3741-b6ec-cdcee523697d | -19.9474 | -47.49147 | 2025-08-23 04:04:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7adf1dd2-48c6-355a-a440-14ca07d29427 | -22.64673 | -44.59576 | 2025-08-23 04:04:00 | NOAA-20 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 581c30d2-01bc-317a-8086-48cac08e2811 | -20.34942 | -46.5185 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a0baa38-4bcc-30a5-83c5-224679a14a2a | -20.26876 | -46.68038 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0638fc3-a077-3190-adde-f5e9518ac3c5 | -15.02625 | -54.89148 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c556a532-17e0-3072-b20e-304051bb573b | -22.65588 | -43.5966 | 2025-08-23 04:04:00 | NOAA-20 | JAPERI | RIO DE JANEIRO | Brasil | 3302270 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d579d80d-6578-31e9-8655-db22c75af5f8 | -17.27699 | -46.77479 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6928f32-2c4a-357f-9809-214b8edf3e84 | -22.64077 | -46.66833 | 2025-08-23 04:04:00 | NOAA-20 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c6081faa-380a-3cc5-b104-a7c4778f3653 | -18.25775 | -45.57287 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f21ad45-a537-3bb1-a789-61ae7a4480d5 | -22.90075 | -46.38989 | 2025-08-23 04:04:00 | NOAA-20 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ec30a86a-76cb-35dc-b243-db3231067f76 | -17.62494 | -42.40539 | 2025-08-23 04:04:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4525f671-5912-38d9-aa75-98c43587b8ed | -22.62881 | -47.44562 | 2025-08-23 04:04:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e564b976-0d30-3b6c-9b9f-4747dbc29564 | -20.44302 | -42.12012 | 2025-08-23 04:04:00 | NOAA-20 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 927d5895-9c3c-3570-87a4-3f848e6c9458 | -20.34868 | -46.52272 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af4d5e8b-d5b7-3d57-82ac-fb00a4373ecc | -19.95989 | -47.50928 | 2025-08-23 04:04:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7a5aa09-b1a0-3905-a959-1b096db5bb65 | -16.39776 | -49.17881 | 2025-08-23 04:04:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9739411-5ecf-3c90-816d-ac9785312d5a | -17.40224 | -44.24446 | 2025-08-23 04:04:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3d32deb-f8f0-3110-99bc-d14ee0349637 | -17.27496 | -46.76439 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6098e3dc-96e3-3136-841b-4351927db1a9 | -14.75198 | -55.99411 | 2025-08-23 04:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8aa086a0-c8e1-3703-bec8-67cde93bf5b7 | -22.62687 | -47.43559 | 2025-08-23 04:04:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d45ad6c0-e0bc-3886-b24b-1c20db33de50 | -23.49653 | -45.99762 | 2025-08-23 04:04:00 | NOAA-20 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 09b009c7-43dc-3b4b-b800-7b09e7c6170b | -15.01624 | -54.87453 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8b3403b4-fadb-3ff2-b28d-f1f363294a9a | -20.01119 | -46.4343 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85bdd9fa-df50-3f01-9f7a-907ad4b25299 | -21.35524 | -46.64022 | 2025-08-23 04:04:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5c70d93c-fdd4-39d7-b256-182cf6cb2db2 | -18.29935 | -45.56366 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0a7144d-1e5f-3c13-bc37-499e81ab82a0 | -20.26953 | -46.67606 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38d9fbd3-0423-3f09-801c-22182730aaf4 | -22.15308 | -44.59731 | 2025-08-23 04:04:00 | NOAA-20 | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 09b9c57f-6096-3ada-8c58-e66bf8ee4e7e | -17.58484 | -46.55556 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| de7079dd-59e9-37bc-812f-49fd37e6925b | -15.01656 | -54.89778 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bb35bcad-9b86-3747-8eae-c32e6dcda10d | -21.38982 | -46.99387 | 2025-08-23 04:04:00 | NOAA-20 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28e2a346-1a41-36b8-9542-613c2295134b | -20.44131 | -42.13158 | 2025-08-23 04:04:00 | NOAA-20 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| bbccdf40-2ec2-39ed-b2cb-8f0494dad149 | -20.08935 | -47.73623 | 2025-08-23 04:04:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 44879792-fdd2-3c8f-a809-0fce1cad4a27 | -17.04935 | -47.13516 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c61861a-d88d-31a0-bf06-2f273b4b9464 | -15.02468 | -54.89195 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 46421139-51ab-3fd3-8a0e-d44c98fc8959 | -23.24789 | -45.97147 | 2025-08-23 04:04:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2028030d-5f0c-35b9-84b0-19e328b62c83 | -19.38287 | -41.44078 | 2025-08-23 04:04:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 33acbd77-bcb2-3e09-acc4-dbb6462a442f | -15.06171 | -56.40238 | 2025-08-23 04:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a064267-f2d4-3b7e-beb2-5f9f5dfa4498 | -22.9787 | -47.04221 | 2025-08-23 04:04:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1d194943-9762-3e61-bda3-d59fca9aed51 | -23.49927 | -46.00231 | 2025-08-23 04:04:00 | NOAA-20 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2f9d6965-405c-3c2d-ba12-8ffd6ed2ace3 | -16.41733 | -49.14932 | 2025-08-23 04:04:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3ed81d2-e4ab-3905-a23b-d6f20252dd77 | -22.47949 | -44.28378 | 2025-08-23 04:04:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 461b71f9-d3e6-3d94-87ca-577229044a70 | -14.66671 | -54.92252 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 87097823-9206-3bc6-a4e1-43911384039f | -17.58029 | -46.5595 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b23001fc-e480-3072-a48f-1ecc54e40147 | -16.23308 | -48.75967 | 2025-08-23 04:04:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c679dde-bbe0-30db-9a98-694f13a8e233 | -17.27032 | -46.76836 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 85387561-8ed9-36b6-99b0-4aadd792578d | -15.0148 | -54.87486 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 04a40c35-ae1c-3099-8166-bc07863f2477 | -22.90001 | -46.39407 | 2025-08-23 04:04:00 | NOAA-20 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 630b4baa-196c-3745-b044-fd0d44087c82 | -17.26477 | -46.77729 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 70b7f66c-64ef-3dbb-adc4-c0d74c11ba4d | -17.81123 | -52.07261 | 2025-08-23 04:04:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f150b6bf-ed7a-3f7f-88a6-af9448471f81 | -22.16275 | -43.27669 | 2025-08-23 04:04:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c9f2fe23-590d-3a41-96fa-bc44238e1e79 | -20.35307 | -46.51879 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82b3c1b5-a179-3424-990c-ba6643453c26 | -22.18707 | -44.55692 | 2025-08-23 04:04:00 | NOAA-20 | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7fa30115-86e3-3538-ba54-4cc1229a08ff | -18.68178 | -41.19263 | 2025-08-23 04:04:00 | NOAA-20 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c2f8bf8b-8eea-3c1f-89f9-eaded662614b | -22.53456 | -43.72174 | 2025-08-23 04:04:00 | NOAA-20 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 39e918e5-0e9f-3cde-b687-a67bfa30d365 | -20.25574 | -46.62768 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e885d0db-05c7-34d9-89f4-3f82ce976b88 | -17.70194 | -48.49312 | 2025-08-23 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cbf7836-3b16-33d4-9d14-3aab63fd56ea | -20.09233 | -47.76333 | 2025-08-23 04:04:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3449deb-fa54-3580-a401-70bc2d1dfaa2 | -20.27314 | -46.67676 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5023afb0-8f39-3863-9bad-c4684c161941 | -19.74458 | -45.98432 | 2025-08-23 04:04:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91bf62ce-1ef2-3225-b1ae-0b05a39ceee6 | -22.17213 | -43.28222 | 2025-08-23 04:04:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e056b9c7-4d45-3266-9f34-0bc3500424c0 | -18.25142 | -45.5674 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5359d41-f704-343c-970f-e1d7adbf583f | -17.6956 | -48.50398 | 2025-08-23 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7767b93-d678-3164-8820-48acb4168f1f | -18.28313 | -45.57336 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f99225d7-0584-3990-b412-2657ba970475 | -18.25215 | -45.56324 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ea0bad9-f0e7-32a7-8cbe-9bd317ed6a86 | -18.86841 | -47.38654 | 2025-08-23 04:04:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a6a5a61-cda9-313e-9b04-1b28e0426c9d | -22.62602 | -47.44022 | 2025-08-23 04:04:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bcad590c-1020-387f-9202-820e09bbf666 | -23.31377 | -45.5395 | 2025-08-23 04:04:00 | NOAA-20 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dc5a3bbe-9ebd-3a81-9256-386b49b08e51 | -23.25766 | -49.50611 | 2025-08-23 04:06:00 | NOAA-20 | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| bbb8904a-addc-343c-8a76-52cdd59fe338 | -23.49123 | -47.6296 | 2025-08-23 04:06:00 | NOAA-20 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 73e843bd-d4f1-327e-8873-f1d0b45be4fc | -23.89963 | -47.53786 | 2025-08-23 04:06:00 | NOAA-20 | TAPIRAÍ | SÃO PAULO | Brasil | 3553500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 35708d0a-227e-3ff5-8cef-85fa5e0391f9 | -23.49205 | -47.62507 | 2025-08-23 04:06:00 | NOAA-20 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e8ecc68d-794a-373f-9bdc-eee28df05f72 | -24.66638 | -49.44142 | 2025-08-23 04:06:00 | NOAA-20 | DOUTOR ULYSSES | PARANÁ | Brasil | 4128633 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 6ed5f02f-a64a-3291-ae8a-2eaf7645c252 | -25.16516 | -50.07573 | 2025-08-23 04:06:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b3b8ff04-fb97-38f9-8fef-a13d6149de43 | -25.16554 | -50.07489 | 2025-08-23 04:06:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 60280297-a636-3460-8901-3827a49f6bd9 | -25.56652 | -51.06007 | 2025-08-23 04:06:00 | NOAA-20 | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c52f5405-445c-3676-a5ab-ed81015bd34e | -23.16097 | -48.74007 | 2025-08-23 04:06:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b24f5e13-18aa-313b-bc62-656d520cbd39 | -25.14642 | -49.53702 | 2025-08-23 04:06:00 | NOAA-20 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a85fc216-4ced-3604-a344-37b536ed2789 | -25.16954 | -50.07591 | 2025-08-23 04:06:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7456fec6-bf6f-3fc1-9ed7-e0a802bd1df3 | -24.90955 | -49.27262 | 2025-08-23 04:06:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 359fc4c1-2f4f-3e4d-a55a-6a80cd37286d | -24.67026 | -49.44241 | 2025-08-23 04:06:00 | NOAA-20 | DOUTOR ULYSSES | PARANÁ | Brasil | 4128633 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c2e5f23b-b16e-3840-b86c-0c7303bc6de7 | -25.16876 | -50.07981 | 2025-08-23 04:06:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c2cff3a2-d4f2-366e-8b3b-9c0852a679dd | -23.49485 | -47.63036 | 2025-08-23 04:06:00 | NOAA-20 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 23200ea6-b0c2-3c08-a2f0-4b847423eaeb | -24.90848 | -49.27816 | 2025-08-23 04:06:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |


[Clique aqui para ver as próximas entradas](README35.md)
