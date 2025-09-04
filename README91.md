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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51510022-0d2c-3abd-b943-9c9d97186e8b | -12.97727 | -54.77892 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0946b1fa-a59f-315e-a43a-04c6c1305d3a | -12.63016 | -56.99048 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f29416b9-7082-3499-8c93-1ad070a4eb59 | -14.54947 | -48.07381 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 19227684-24ae-3c84-bb9f-168f63a87c77 | -13.10434 | -57.11665 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| a0df52bf-160f-361d-a9eb-a3a7f11fceb0 | -15.15216 | -52.379 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0e341ae-fe87-3c40-84fd-df23b9a89355 | -12.81487 | -47.67014 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51d97bfc-4e6b-3faa-9ac5-104315316202 | -10.24576 | -61.77018 | 2025-09-04 05:18:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c50e96c-62b5-338e-b5dc-e0e36c595b66 | -13.09339 | -57.115 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b08c0d49-2d15-3a58-bdd9-2a217a4b0c1d | -11.58703 | -52.11694 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff701efc-c903-3d33-96f0-31723d22977e | -17.03855 | -47.14671 | 2025-09-04 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9eb47102-6dda-3414-b3b3-85d5fa70ba70 | -12.90231 | -48.05318 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 803162eb-9fd8-3d68-bd61-ceba0782a06b | -12.23805 | -50.15106 | 2025-09-04 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52b34111-24dc-3ae4-a585-81c18cf2723d | -14.53676 | -48.0666 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cb705e1b-b293-3977-9410-3ae17c7af78f | -13.73038 | -46.9248 | 2025-09-04 05:18:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8effa78b-41f7-32eb-bc5f-b55d50322e7b | -17.04171 | -47.14453 | 2025-09-04 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 169060bf-11fd-3c73-a5d0-5e950973e672 | -12.97253 | -54.7823 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 536ac5b7-43d6-3c54-9bb0-7982b24cefe4 | -15.55245 | -48.41565 | 2025-09-04 05:18:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6a4108e-3354-329f-88d1-22ee2921fc3a | -13.57172 | -48.13288 | 2025-09-04 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5deaaa69-9e19-314a-9404-177643b7cdb5 | -14.58829 | -48.02299 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4f2168bc-8f28-3d24-83bc-4878df2a1351 | -11.53287 | -54.41179 | 2025-09-04 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cfdbc8f-241d-3a6c-a01c-cba711bc6373 | -14.81938 | -48.20985 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 027c1724-b451-362c-be45-2a3191e96ebb | -11.61593 | -47.77711 | 2025-09-04 05:18:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 87ff175d-e282-3a70-a513-90015af7cc1b | -11.20105 | -55.02684 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c83e083b-5dcd-3161-a6ba-c71b936c90a7 | -12.2442 | -50.14787 | 2025-09-04 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f068ab7-9dd2-3b79-b38d-d1b4b38b0b81 | -12.96628 | -54.76535 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebed1c2b-b094-3216-9981-5661dfe0ff94 | -15.02668 | -50.08848 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e1854f0-7c95-3b64-862a-27b3c29a9da1 | -11.64278 | -52.20544 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01e56bf5-caf8-380c-ae27-4f5ed6a07553 | -14.75817 | -48.087 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9dbcb4ae-3e45-3361-be73-83fd4238ed5c | -15.46696 | -53.01551 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16326b6e-c1ea-308a-bf37-3c049fc0023c | -12.45733 | -48.08658 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 81ab7b8f-4639-3fd8-861b-31fd8681d136 | -12.47755 | -48.08337 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87458bc5-7ce1-31d5-9b87-d933312c5192 | -12.50636 | -48.06119 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07b40fa3-53eb-35a3-9fa6-1b4cd99f616e | -11.59667 | -47.77913 | 2025-09-04 05:18:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 272be552-36cd-3bc7-9831-75bb91fcda5c | -12.46389 | -48.08802 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9a2ad16f-288a-3b2e-9c0d-6d879a8770a3 | -11.31772 | -55.22446 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e28cc20b-bb6a-39c0-8ed2-0a8bb333b5e7 | -13.73572 | -46.94139 | 2025-09-04 05:18:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e0c9419-ff5e-3f28-a692-2328c81885be | -15.61003 | -52.88441 | 2025-09-04 05:18:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a2a33e0-951d-37ef-8604-a6dec7174692 | -11.90639 | -46.66134 | 2025-09-04 05:18:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 133113cf-82fe-3288-be62-37c47c65249c | -13.56522 | -48.13165 | 2025-09-04 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c7b394a8-b73c-303b-b06a-60b3e10f3e48 | -6.7319 | -58.7276 | 2025-09-04 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| c6fafaf4-d113-3e82-8a70-9e17ade8d16c | -6.7833 | -63.1286 | 2025-09-04 05:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c9431747-e2f3-359d-a9e9-4f105d106625 | -6.7504 | -58.7268 | 2025-09-04 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 100.8 |
| add3d7d0-a413-378a-9a5c-7574f1f285ba | -4.9951 | -56.256 | 2025-09-04 05:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| d635d157-59c7-3179-ab07-ab7776395e21 | -12.9009 | -56.9287 | 2025-09-04 05:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 4453e970-aa32-3164-88cf-6ca1ef21cbe5 | -6.7649 | -63.1292 | 2025-09-04 05:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5204ba7f-6881-36b3-a75d-ce893244eba8 | -13.1079 | -57.1109 | 2025-09-04 05:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| e95546db-2703-3946-a5f8-4533ba3ec477 | -21.94475 | -50.51988 | 2025-09-04 05:21:00 | NOAA-20 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 38be83cd-7512-363f-9e59-9cb2c4c3a674 | -21.95098 | -50.52018 | 2025-09-04 05:21:00 | NOAA-20 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f476b3bf-9cd4-3d33-9935-3f3059f57a14 | -19.23643 | -48.68301 | 2025-09-04 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3c9d1f2d-2283-3c0d-bc3b-ea8dfdf8092b | -18.13811 | -47.92079 | 2025-09-04 05:21:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76a90326-3d53-31c9-9bc2-3a59e6d1aeef | -18.13721 | -47.92037 | 2025-09-04 05:21:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bc46f0e-3429-35ef-8c20-b9bd2ec47435 | -22.26397 | -49.55804 | 2025-09-04 05:21:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2d8da752-8b56-316b-b94a-1fb1b7e8eb14 | -20.09744 | -50.01336 | 2025-09-04 05:21:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| e8428bf8-6183-3aea-aadf-7033c1966577 | -20.88324 | -51.59134 | 2025-09-04 05:21:00 | NOAA-20 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3ddaa4e1-7a1c-30a1-b8ef-219c1ce753b1 | -19.69695 | -49.35126 | 2025-09-04 05:21:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7ebbc2db-3da9-37fd-ade3-e8606251fe00 | -20.09791 | -50.00809 | 2025-09-04 05:21:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 7c0cd9df-2f8b-3383-a2b5-44a350017a59 | -19.68261 | -49.36239 | 2025-09-04 05:21:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c2c7b721-186c-32a2-8e98-0420654b6aba | -18.13779 | -47.91341 | 2025-09-04 05:21:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 186e7ed9-9a69-3ce1-925b-223a9cdbe761 | -20.88362 | -51.58733 | 2025-09-04 05:21:00 | NOAA-20 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0ac369a1-96e0-3a8e-b413-18d9e71474a7 | -20.10419 | -50.00878 | 2025-09-04 05:21:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bf9fbd4e-faa2-348c-91fa-2b66ff22e9fc | -20.4698 | -54.40008 | 2025-09-04 05:21:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2824bf0e-1e83-329f-a65d-5089204d857b | -19.69708 | -49.34642 | 2025-09-04 05:21:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 008891ca-cf97-325e-8e96-2cf662caaa56 | -19.69659 | -49.35213 | 2025-09-04 05:21:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c043c3a6-8b2d-3c79-bcce-89530b8b66c8 | -20.51921 | -54.70458 | 2025-09-04 05:21:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5d8e7fb-a147-3e5c-b28e-4830f5382303 | -18.13873 | -47.91387 | 2025-09-04 05:21:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50efa0fa-10eb-383a-bfb0-ed91ca19a17f | -6.7319 | -58.7276 | 2025-09-04 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| d95ee1d9-4379-38bb-9c42-3e4042b3dddf | -13.1079 | -57.1109 | 2025-09-04 05:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| eb71078c-507a-3df7-9e15-3a0237d5734f | -4.9951 | -56.256 | 2025-09-04 05:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 85a4ca9d-5e62-3388-b24b-ff512eca46b5 | -11.6836 | -57.3518 | 2025-09-04 05:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| bef4e2df-1712-38c8-82b2-761f8117d628 | -6.7503 | -58.7462 | 2025-09-04 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| f3b88b9e-ba36-39bb-b563-ec9f034fdf75 | -6.7649 | -63.1292 | 2025-09-04 05:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| ae92a715-4a2b-3da3-8524-5d6841e3aedc | -6.7504 | -58.7268 | 2025-09-04 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 436b3c14-7f50-3fa0-93f0-b75f75777667 | -11.6836 | -57.3518 | 2025-09-04 05:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 61f1d35a-83b4-31bd-946d-77e207eb1780 | -4.9951 | -56.256 | 2025-09-04 05:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| b9563180-9f0e-3b20-b98f-966529d10d73 | -6.7503 | -58.7462 | 2025-09-04 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 4b435c60-b29c-39a9-aefc-8826e2f5779b | -6.7504 | -58.7268 | 2025-09-04 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 8c58dca3-ff0b-3200-8e3e-351d6c7f037e | -5.0135 | -56.2553 | 2025-09-04 05:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 97d95d77-33ba-321b-bbf4-f87c97b095a7 | -13.1079 | -57.1109 | 2025-09-04 05:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 600929c4-d036-3681-9a9c-3361f82c3957 | -6.7504 | -58.7268 | 2025-09-04 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| bd573bb1-150e-3388-8f7c-3532f9964401 | -6.7503 | -58.7462 | 2025-09-04 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 5bb66bbf-3cc2-3089-9935-7da7e2d36f4c | -6.7319 | -58.7276 | 2025-09-04 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| e04dfde7-270a-3591-a08a-db5cc585c80d | -4.9951 | -56.256 | 2025-09-04 05:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 8564aa34-d319-3e9b-8dc1-14696bac6d11 | -8.52277 | -51.3172 | 2025-09-04 05:53:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 6512be06-2944-3b35-bc71-c476ee613f6c | -6.88416 | -45.56119 | 2025-09-04 05:53:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d9b48779-9f92-36d7-baf2-ccdfcd8aa408 | -5.9709 | -44.11991 | 2025-09-04 05:53:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f7dd11a5-c40e-3791-88c2-b30c549c1ea3 | -8.53502 | -51.3105 | 2025-09-04 05:53:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 0da35aa0-a0a2-3dac-8a6b-7011bc736ec1 | -6.2286 | -43.55259 | 2025-09-04 05:53:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 127ad307-16ed-35db-b30a-98ba4807fc22 | -6.12272 | -42.93647 | 2025-09-04 05:53:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 0a205fb0-34e2-3c56-89d6-2b0e2ac7198c | -5.98145 | -44.11172 | 2025-09-04 05:53:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6e1b2e5d-b8b1-32f0-be87-30cdb5914e3b | -6.78702 | -44.0942 | 2025-09-04 05:53:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a905b3cc-8c2e-3fbc-8687-95cf17423b74 | -7.04732 | -43.26432 | 2025-09-04 05:53:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| af0ffef1-b729-3234-b575-d58d3e5b1dd1 | -8.52381 | -51.30896 | 2025-09-04 05:53:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 95c07391-355e-3964-b350-6b15c9b343d5 | -6.86251 | -44.27104 | 2025-09-04 05:53:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7804a0cc-da46-3160-959b-ad39ce54f7db | -6.12114 | -42.94755 | 2025-09-04 05:53:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 1d053728-f0a2-3af0-afbf-04a70ca517a0 | -5.68763 | -45.59256 | 2025-09-04 05:53:00 | AQUA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a3999bf6-5bf7-3ebe-98d1-92230c94871a | -6.02458 | -46.67738 | 2025-09-04 05:53:00 | AQUA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e0c59e6d-953d-3a7e-bb2b-3bd282806cec | -7.68537 | -48.73486 | 2025-09-04 05:53:00 | AQUA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.2 |
| dcd69a44-cbf8-31de-bc74-a936ed61bed6 | -6.24789 | -42.63561 | 2025-09-04 05:53:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e3f98eea-12c8-3e34-96e3-e3ec06ed4b94 | -5.70819 | -45.15387 | 2025-09-04 05:53:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f5330650-fce5-3f48-a509-eddfde973b0f | -8.03874 | -45.37513 | 2025-09-04 05:53:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |


[Clique aqui para ver as próximas entradas](README92.md)
