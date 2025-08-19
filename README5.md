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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 848a8521-913c-39d6-bf4f-78667f4af4f2 | -12.9704 | -56.833099 | 2025-08-19 00:34:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a99405e8-091e-3e9f-be3c-fb079c0cf603 | -4.6032 | -43.321301 | 2025-08-19 00:34:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9cf2a4fe-6e83-38d4-87a0-9d12fc1a3a0a | -11.4541 | -47.320202 | 2025-08-19 00:34:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 834badaf-e0be-3e03-af6a-4d4f56e3a72e | -7.5879 | -45.435501 | 2025-08-19 00:34:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2426828-11a9-38a8-9b75-65487c4ab6ff | -6.2485 | -44.829102 | 2025-08-19 00:34:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8ae37c6-f82b-3688-9735-ffdb009e99dc | -3.4832 | -48.4426 | 2025-08-19 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9df8abc9-1c06-3f1f-bd46-165e18d9ceca | -11.8686 | -51.567101 | 2025-08-19 00:34:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a67b6c9f-b011-3357-b2b7-6678c0db3b42 | -5.9786 | -44.2957 | 2025-08-19 00:34:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91140ad3-7148-30c0-ae93-29458a71d4ac | -6.9635 | -43.615299 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| afd44fc2-bb62-386b-a3bc-959a543b3199 | -6.9298 | -43.604301 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7a0c7f18-6c0c-3aa8-85e1-a1c4f101b90c | -6.7546 | -41.541698 | 2025-08-19 00:34:00 | METOP-C | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f8c83226-5120-37de-9b48-ac1ce15fea18 | -12.9974 | -45.2118 | 2025-08-19 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9e28fb63-631c-3a29-8927-2f0d0cf9b7cb | -13.1793 | -46.8839 | 2025-08-19 00:34:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 81580a3b-0337-38cb-8a49-7ea3d54fe503 | -5.5541 | -49.069901 | 2025-08-19 00:34:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 513e4fc0-8ce4-3965-af5f-1ea1432706e7 | -9.1647 | -40.596699 | 2025-08-19 00:34:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| ac4032a5-fa79-30e7-8bde-19f9cba57545 | -13.2577 | -50.831902 | 2025-08-19 00:34:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5dc128a9-21ef-3a06-a1b3-f597e9da13ca | -21.5219 | -42.6637 | 2025-08-19 00:38:00 | METOP-C | LEOPOLDINA | MINAS GERAIS | Brasil | 3138401 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e9752def-1ef2-3d47-bc2a-d7ce39717005 | -21.0515 | -43.3214 | 2025-08-19 00:38:00 | METOP-C | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2239f35c-8390-3fcb-a4cb-f300261c4987 | -17.818399 | -44.497002 | 2025-08-19 00:38:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b2c8eaa2-c422-31a6-87c2-07e652c9ef9e | -20.2964 | -50.957298 | 2025-08-19 00:38:00 | METOP-C | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 98b3ae41-6194-3593-bc65-8fb5b2e25789 | -16.5096 | -45.097 | 2025-08-19 00:38:00 | METOP-C | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 95f6b6f8-ce9a-3d20-992c-15ca8e727024 | -16.4869 | -45.087399 | 2025-08-19 00:38:00 | METOP-C | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8fe62362-f676-39ec-9a51-a87187c85a39 | -17.492201 | -45.8587 | 2025-08-19 00:38:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 01985c5e-f12e-3308-a7ad-e78c802deaea | -21.868999 | -48.2029 | 2025-08-19 00:38:00 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6c276586-e6b8-37b7-8190-934ed52df1b4 | -17.5658 | -44.4748 | 2025-08-19 00:38:00 | METOP-C | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ed324f5b-f1fc-3ba1-859d-73c9b9c73825 | -16.4853 | -45.080299 | 2025-08-19 00:38:00 | METOP-C | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 83046f0f-7d66-3cce-b5da-b6c82729bf08 | -15.968 | -43.898201 | 2025-08-19 00:38:00 | METOP-C | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| fe63762b-8eb6-3621-86b9-9d5b8c8531bc | -21.4035 | -45.016899 | 2025-08-19 00:38:00 | METOP-C | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 85ec35a1-aca4-395c-9cdf-3ac3df404edb | -21.880699 | -48.210602 | 2025-08-19 00:38:00 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 57d353b9-171f-368c-8829-9d71f599a1d6 | -19.952 | -48.2043 | 2025-08-19 00:38:00 | METOP-C | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 882d7e68-1aa9-3198-9177-dd427834a37d | -15.9222 | -43.522999 | 2025-08-19 00:38:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c82436b1-c538-362b-9444-4326e0c82c86 | -16.491699 | -45.108799 | 2025-08-19 00:38:00 | METOP-C | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 087588f9-6afc-3fec-b057-7113e122efe9 | -16.501499 | -45.106499 | 2025-08-19 00:38:00 | METOP-C | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7e8fab47-9532-3d4e-92e6-da2bb6f9f6ab | -16.4837 | -45.0732 | 2025-08-19 00:38:00 | METOP-C | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e7ae8607-208b-3e7b-82b5-a9ec7e6f21f8 | -19.2033 | -46.8452 | 2025-08-19 00:38:00 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3b2383d2-ce96-3382-8022-9a0a0d4db275 | -21.2346 | -49.085602 | 2025-08-19 00:38:00 | METOP-C | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c8130837-e2ce-3a1c-9cde-6497114ffcbd | -16.499901 | -45.0994 | 2025-08-19 00:38:00 | METOP-C | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6c4f861a-1ccb-34d4-a27f-5fc4fe7829ad | -17.8899 | -48.615601 | 2025-08-19 00:38:00 | METOP-C | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e73ac34e-1899-3e15-bda9-74799ebd23bb | -15.9697 | -43.905499 | 2025-08-19 00:38:00 | METOP-C | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 14cf3e59-f6ee-33af-8680-e28be4d33d74 | -21.888599 | -48.198601 | 2025-08-19 00:38:00 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 80217e77-4e66-3ea1-904b-a3633d198a02 | -16.480301 | -45.104 | 2025-08-19 00:38:00 | METOP-C | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b5342335-e3e4-3486-8d28-1d35ea972a75 | -20.242901 | -44.179798 | 2025-08-19 00:38:00 | METOP-C | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d18463aa-2993-38bc-98c5-e1f86bac1d97 | -21.8964 | -48.186699 | 2025-08-19 00:38:00 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2bc49cd0-e8ba-3bfa-9050-0b92fc6fd2b8 | -21.401899 | -45.009499 | 2025-08-19 00:38:00 | METOP-C | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5b4261d4-56e2-38e9-ab7a-7fa111b7dadc | -17.8281 | -44.494598 | 2025-08-19 00:38:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 89ef1533-1705-3b9d-9873-2e98c71796d5 | -15.7538 | -46.611698 | 2025-08-19 00:38:00 | METOP-C | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3cedca68-dd6d-374d-959c-e501223e63de | -16.620399 | -51.349098 | 2025-08-19 00:38:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6bd88bc8-54b4-354b-9f8d-c94c58b973a8 | -17.8881 | -48.606602 | 2025-08-19 00:38:00 | METOP-C | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e12da554-65ba-3fc8-ab04-048c6079332e | -16.478701 | -45.096901 | 2025-08-19 00:38:00 | METOP-C | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f03b00ca-6c47-38a8-8e4d-49c940271df7 | -21.8867 | -48.188801 | 2025-08-19 00:38:00 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e91d9c28-2c0e-3589-9c8c-9f08f005130c | -17.3431 | -47.1689 | 2025-08-19 00:38:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 19c7b694-5367-333d-b2ab-b629a3192d7d | -21.870899 | -48.2127 | 2025-08-19 00:38:00 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bc506df6-c004-3803-bd66-b280ddb063fb | -20.3305 | -51.7033 | 2025-08-19 00:38:00 | METOP-C | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3de95366-b47d-38c6-9188-b26128fc82d0 | -17.564199 | -44.467602 | 2025-08-19 00:38:00 | METOP-C | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1e6d7e92-729b-3ae4-a6af-16357c7bf0bd | -23.782 | -51.705601 | 2025-08-19 00:38:00 | METOP-C | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3bb21a00-c4ba-3c40-8108-0d2eb37f9716 | -16.4755 | -45.082699 | 2025-08-19 00:38:00 | METOP-C | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4ebb87c9-aebf-345f-8175-15e90b44b96f | -17.410101 | -46.7132 | 2025-08-19 00:38:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f9b6b749-c518-31ba-ad16-318da5c8d4bb | -16.7225 | -47.628799 | 2025-08-19 00:38:00 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1ea3ee9b-8f71-3f7e-87e5-85af80f5c0cc | -15.7554 | -46.618999 | 2025-08-19 00:38:00 | METOP-C | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 12372639-c562-3ed7-9f3b-8f30ff7c55b0 | -23.772301 | -51.707401 | 2025-08-19 00:38:00 | METOP-C | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 06992fef-2b12-3880-9fe3-685686df10f4 | -22.8827 | -47.491798 | 2025-08-19 00:38:00 | METOP-C | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0dd26748-8642-3a9d-a83c-09bae647d7fe | -15.8423 | -48.1693 | 2025-08-19 00:38:00 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| 5a6a7357-9dff-3828-b106-bcaf58957955 | -16.5112 | -45.104099 | 2025-08-19 00:38:00 | METOP-C | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 98f7bfff-0442-3854-9005-3f4d4168ff2f | -20.3332 | -51.718399 | 2025-08-19 00:38:00 | METOP-C | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3d3ae7b5-5ac4-3186-bf89-22f1bfefaa5b | -16.481899 | -45.111099 | 2025-08-19 00:38:00 | METOP-C | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 558a7715-86f6-3281-a95f-c25be4f27ccc | -17.567499 | -44.481998 | 2025-08-19 00:38:00 | METOP-C | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 240f162d-e8fb-396f-8e33-3cbd201ee8c7 | -16.622801 | -51.361599 | 2025-08-19 00:38:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a86eef46-4e24-326d-9b60-4c0b3cf35f2b | -23.0914 | -46.276798 | 2025-08-19 00:38:00 | METOP-C | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2fa50759-2321-3596-9908-b2d765e43b15 | -21.8983 | -48.196499 | 2025-08-19 00:38:00 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| aa578d8c-1ced-37bc-b0a4-41433b94d818 | -21.878799 | -48.200802 | 2025-08-19 00:38:00 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 05a41b08-ef81-3351-9b30-63af57481d29 | -16.488501 | -45.094501 | 2025-08-19 00:38:00 | METOP-C | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3121128d-fa67-39e5-b930-87df135e19ac | -20.613701 | -44.741699 | 2025-08-19 00:38:00 | METOP-C | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a8a00137-46b1-37cb-a4e8-1b21107ce5f3 | -20.244499 | -44.187099 | 2025-08-19 00:38:00 | METOP-C | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dfb43fe5-3a1a-3938-b754-3235acab2b45 | -21.400299 | -45.001999 | 2025-08-19 00:38:00 | METOP-C | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 77136020-220f-32dd-ae9c-7e081b43ca76 | -23.775101 | -51.724602 | 2025-08-19 00:38:00 | METOP-C | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 79f0091a-3ca0-3f3a-9917-494cd6d3f9e4 | -16.4771 | -45.089802 | 2025-08-19 00:38:00 | METOP-C | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c7d66b89-964c-3c14-844a-f5fee305facb | -22.884501 | -47.501202 | 2025-08-19 00:38:00 | METOP-C | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd234b19-2775-3084-ae98-6747c1615298 | -21.049801 | -43.313999 | 2025-08-19 00:38:00 | METOP-C | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| df2fb318-5c8d-363c-bf79-b7f359012e53 | -16.490101 | -45.1017 | 2025-08-19 00:38:00 | METOP-C | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 401ef0ec-baf4-3de8-afe7-1b4a3a91d4c0 | -15.844 | -48.177502 | 2025-08-19 00:38:00 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| d6d354ac-e617-3474-a26f-7db9ee17bff2 | -23.463301 | -47.1213 | 2025-08-19 00:38:00 | METOP-C | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a34b3076-d4f8-3539-8811-9fd6530291b3 | -17.419901 | -46.710999 | 2025-08-19 00:38:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d585d5e6-f00e-321c-af40-98653ab3cac7 | -15.7522 | -46.604401 | 2025-08-19 00:38:00 | METOP-C | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a0f174ba-786f-3c92-9e0f-071bc4f1aade | -23.465099 | -47.130501 | 2025-08-19 00:38:00 | METOP-C | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1860769e-64a1-3ad0-83f8-aeeb8c47e731 | -15.4047 | -49.5733 | 2025-08-19 00:40:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 222.0 |
| 596cb16c-23c3-3eb5-a894-966e12726d4f | -15.4052 | -49.5512 | 2025-08-19 00:40:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 7a4e781a-c492-3c47-a0cf-b7c754b265e5 | -4.0007 | -42.5149 | 2025-08-19 00:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| a247cd07-071f-35e8-b451-41720ed91216 | -14.9809 | -54.8158 | 2025-08-19 00:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 3f9e76e1-db8a-35ee-a978-794927f509cf | -5.557 | -49.0801 | 2025-08-19 00:40:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 9bcb5437-6951-3e45-8f12-8b53d4e31199 | -15.0196 | -54.8112 | 2025-08-19 00:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 8fce1125-7e56-3fbe-a69b-2b45d621b232 | -6.9339 | -43.5868 | 2025-08-19 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 0930cc98-1cf0-3699-85f8-b5ed93ea519b | -12.9971 | -56.8395 | 2025-08-19 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 1b945108-fb85-392c-8dc6-167f2236ba83 | -15.0389 | -54.8089 | 2025-08-19 00:40:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| f06825fe-a3cb-30db-a122-fc8d1f2ddb17 | -13.0162 | -56.8378 | 2025-08-19 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| bb50aaf2-3380-3d32-81ff-bbefe18bb6bb | -5.5571 | -49.0587 | 2025-08-19 00:40:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 10217be4-a63e-37a4-a81c-bb1e505f7d7d | -16.4863 | -45.0702 | 2025-08-19 00:40:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 86.6 |
| ceaee7eb-27fa-3f6f-8778-770f0f3636cb | -6.9527 | -43.585 | 2025-08-19 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| cf2c2787-cac4-3364-96cb-365982485c40 | -6.9712 | -43.6066 | 2025-08-19 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 80db8bb6-0473-35ad-bd69-dbaf5f515b04 | -8.9788 | -60.4964 | 2025-08-19 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 0d73097f-1131-3d2d-bee0-71fffff6c13a | -16.4857 | -45.0939 | 2025-08-19 00:40:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 133.6 |


[Clique aqui para ver as próximas entradas](README6.md)
