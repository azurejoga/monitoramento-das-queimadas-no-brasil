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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a9fe748-3b19-3391-867a-edf3d659bf9c | -19.83939 | -45.01701 | 2025-05-06 04:23:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4a00010-7b2f-3fb0-a04f-f4e04cded939 | -20.06264 | -49.37075 | 2025-05-06 04:23:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e6b300fe-6a5b-34b6-96d9-3cf5b00f6b92 | -20.34858 | -40.35978 | 2025-05-06 04:23:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f5e4ec38-cc85-3e3a-8972-3f28807ef6c8 | -20.4195 | -43.55419 | 2025-05-06 04:23:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 56d37ecd-b2a5-3c0c-985a-921f961d8692 | -18.14729 | -47.8012 | 2025-05-06 04:23:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36237fe3-7077-337a-a821-1c8ccd8345f9 | -17.77711 | -42.81121 | 2025-05-06 04:23:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c137af83-11c1-39cd-9a2f-efd7baeba06f | -20.05926 | -49.37012 | 2025-05-06 04:23:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0e72896b-e45f-361b-8873-f825bb437def | -18.50049 | -47.60027 | 2025-05-06 04:23:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e2af46b-9ab4-3122-8468-90b76c5097d9 | -16.46511 | -48.9739 | 2025-05-06 04:23:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7f326539-6d49-3c7d-8bc5-9ccbee2996ef | -20.41564 | -43.55367 | 2025-05-06 04:23:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b7a498ed-2b67-39b6-8d98-dae0380e6dba | -23.52476 | -47.83637 | 2025-05-06 04:25:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2868cc7b-5d87-3dd6-9cdb-1ef396d4bf36 | -22.85696 | -42.98058 | 2025-05-06 04:25:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 989c0587-8897-3647-9301-3c0154c96292 | -25.1919 | -49.32794 | 2025-05-06 04:25:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2355230e-5e9d-3d57-b200-1f8eabba24dd | -21.82394 | -53.61481 | 2025-05-06 04:25:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f10af2ea-7cde-3c88-81dd-f4398f49c55c | -23.59473 | -47.4403 | 2025-05-06 04:25:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 97435c97-ae0e-302d-9423-750013690f9d | -21.03336 | -48.99034 | 2025-05-06 04:25:00 | NPP-375D | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| f5d59477-736d-3a5d-8f79-341a7956557d | -23.5236 | -47.84401 | 2025-05-06 04:25:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4c98c99e-da00-3025-8d76-ab988d5a03ff | -22.66751 | -49.80966 | 2025-05-06 04:25:00 | NPP-375D | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a46c12e1-b3e6-3782-b57e-6eb46221340b | -23.60234 | -49.01471 | 2025-05-06 04:25:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 21.6 |
| d13905ed-8107-37bb-bbcd-85a2e573e45f | -21.03397 | -48.98659 | 2025-05-06 04:25:00 | NPP-375D | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| b9d9f3ee-7326-3c8c-b9f7-1fd627343d0b | -23.40454 | -46.55741 | 2025-05-06 04:25:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f6864bef-81f3-3912-b955-cd21d6af963a | -23.60294 | -49.01093 | 2025-05-06 04:25:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bd9cbb33-155b-3210-98fa-b60a73082a34 | -21.19407 | -44.93744 | 2025-05-06 04:25:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1309d436-708d-34c0-9949-11c757f328eb | -22.67088 | -49.81031 | 2025-05-06 04:25:00 | NPP-375D | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 671b6b23-a60b-3b52-8c23-ddf7b9c7c16b | -21.24643 | -48.61769 | 2025-05-06 04:25:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f52cdba6-cfd7-3598-b352-79a02738d70e | -21.1803 | -43.98193 | 2025-05-06 04:25:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 36476000-c96f-3e74-963e-a89bcdfdb71a | -22.90726 | -49.69172 | 2025-05-06 04:25:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3ef40ac1-a695-3d54-836f-d19e1dfe5e73 | -23.51863 | -47.83133 | 2025-05-06 04:25:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5a3f4d6a-792f-3a44-9381-8ccb22aaee63 | -21.82411 | -53.61604 | 2025-05-06 04:25:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 605c8298-298a-36b3-8383-f63c0dfd5e4b | -23.04852 | -49.89631 | 2025-05-06 04:25:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 6125e6fe-4d9a-39fe-8d9d-83885648632a | -23.60354 | -49.00715 | 2025-05-06 04:25:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 08f3e14b-ac18-37f2-8909-af1aba68371f | -23.60414 | -49.00337 | 2025-05-06 04:25:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0e7ef25-ad71-3ff4-96f0-6d96fbee06e8 | -22.84988 | -47.11267 | 2025-05-06 04:25:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| baeb409a-f729-3bfd-a946-ec3543bacb89 | -21.36379 | -48.62716 | 2025-05-06 04:25:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 33b6b3d5-f582-3672-9488-3261a2c81ac0 | -23.52141 | -47.83576 | 2025-05-06 04:25:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 257bd083-6ab4-3d9a-96f8-da4bedac9bcb | -21.36712 | -48.62777 | 2025-05-06 04:25:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 120f8d46-68e1-3efb-88d4-2bfe5d10d91e | -20.99671 | -51.79158 | 2025-05-06 04:25:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ae670ace-8c66-3be1-9017-bf8ad4e6d468 | -20.76326 | -46.76956 | 2025-05-06 04:25:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76074bd7-06c7-3588-a1e1-62810038d065 | -24.24364 | -50.73979 | 2025-05-06 04:25:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5192ed27-1f4b-3836-b4b6-ddb0c253841b | -27.58181 | -50.85846 | 2025-05-06 04:25:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0095f630-1247-3a2f-9e5f-e45d60192cf6 | -21.72145 | -56.10791 | 2025-05-06 04:25:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a5e1a4c7-9bfc-3d73-91d3-c5ef896bb019 | -27.45582 | -48.45316 | 2025-05-06 04:25:00 | NPP-375D | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 60d6adfc-3444-392e-90e5-b1e99e195405 | -23.59901 | -49.01408 | 2025-05-06 04:25:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 07c59eaf-c2eb-32f7-b612-871db1442a98 | -22.78605 | -43.75645 | 2025-05-06 04:25:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b90463ab-f425-3fba-99ff-6a77e11dfbb2 | -23.52418 | -47.84019 | 2025-05-06 04:25:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9b41875c-c991-3ddf-a8bc-a3e471e4a681 | -23.60021 | -49.00653 | 2025-05-06 04:25:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2e165d8b-a521-3b93-b795-a97a5b0444cf | -23.03829 | -50.43909 | 2025-05-06 04:25:00 | NPP-375D | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3ab70bc5-53ab-3b77-af91-2500780a8757 | -22.04095 | -47.93555 | 2025-05-06 04:25:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb22c497-6991-333a-a3d1-a29f969e501c | -21.18278 | -53.18199 | 2025-05-06 04:25:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8022c629-6dc8-3045-b7e4-7ecb92f2ff13 | -21.72613 | -56.10894 | 2025-05-06 04:25:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a4fcb2ff-7da1-332d-b391-a703ca455ee6 | -21.72505 | -56.11419 | 2025-05-06 04:25:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 59b892c3-4e96-3f8b-a768-1723baa11902 | -23.52534 | -47.83254 | 2025-05-06 04:25:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b37867a7-939c-32df-8e1d-a7966f336e41 | -22.90186 | -43.75311 | 2025-05-06 04:25:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9814eb0a-581d-3140-bd19-1c131cd67797 | -23.59961 | -49.0103 | 2025-05-06 04:25:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a6c6c22a-f75e-3646-b512-83eda79723aa | -23.04516 | -49.89565 | 2025-05-06 04:25:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| aac1201d-b059-31a6-94a5-0df7f2b4ddeb | -29.39804 | -51.65475 | 2025-05-06 04:27:00 | NPP-375D | BOA VISTA DO SUL | RIO GRANDE DO SUL | Brasil | 4302253 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 68cfbfd9-76af-3d6a-9aca-cf54890af7d2 | -29.04786 | -51.23529 | 2025-05-06 04:27:00 | NPP-375D | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d9e31342-cee3-3d5d-bedc-355a6319bc77 | -28.17415 | -48.70335 | 2025-05-06 04:27:00 | NPP-375D | IMBITUBA | SANTA CATARINA | Brasil | 4207304 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 681e0527-a493-3612-ae63-ef3474ac0525 | -4.12363 | -46.67675 | 2025-05-06 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7eeecb8f-99c5-3753-be9b-7204265681c2 | -1.54922 | -47.80593 | 2025-05-06 04:42:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 414fc41a-83f6-3e03-a6b1-62ba342a63d9 | -3.85797 | -54.08017 | 2025-05-06 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0a95c6b-eaf6-38d5-85d0-140b59c71899 | -5.16252 | -45.1061 | 2025-05-06 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 94aec595-8fcf-3eeb-bf72-7812b3dc1fac | -2.63511 | -47.96433 | 2025-05-06 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5851527f-15f6-39aa-8e0c-f9ccc1fdf43d | -5.15834 | -45.10545 | 2025-05-06 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 96354822-fff2-33a8-8e12-d3eeabae3b2c | -4.11921 | -46.68066 | 2025-05-06 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ab78609-a10a-3124-9d4d-8f2104b8940a | -7.3575 | -50.81345 | 2025-05-06 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bc2b5fb-de03-3fb9-accd-571c535a7f3b | -6.69612 | -42.1321 | 2025-05-06 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| cb576acd-e6d2-3fd2-9a2c-1e23b9c18eff | -7.54958 | -45.87397 | 2025-05-06 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6131d2e-fadd-37e8-a99e-da2f6f4e266d | -8.20449 | -48.9844 | 2025-05-06 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51e6deba-5519-32ac-bfc6-5518b7fd8523 | -10.97557 | -44.4325 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 20ca843f-ddfb-3e88-8cad-476c2398583d | -7.55866 | -45.84116 | 2025-05-06 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d7a4d34e-6a62-3ae3-a5e7-fb1941463ee7 | -6.69659 | -42.12886 | 2025-05-06 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 6a353f95-06e1-3e20-a046-2b312f22f599 | -6.94794 | -42.7905 | 2025-05-06 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6b83e9ca-6fae-381a-8a91-38b450f1f213 | -4.12784 | -54.90001 | 2025-05-06 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8748dc03-1c25-3897-8c13-af4cbef9802f | -8.30528 | -48.05505 | 2025-05-06 04:44:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d79cc0a-999d-3311-bef5-745666dfc87e | -6.19266 | -48.04229 | 2025-05-06 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c5e3750-304d-32cb-9438-fea308373bd5 | -6.70124 | -42.13395 | 2025-05-06 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| ea968c1f-50ed-3086-8ff5-d18fc2e85773 | -10.98925 | -44.43958 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf5a7a0d-3106-3421-a957-214fb6c2e6c2 | -10.9798 | -44.43676 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 611247c4-3095-30cf-8aaf-e9432e0cc37f | -10.98051 | -44.43153 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1234ee64-bdc8-33cb-952b-7ea2393a4b42 | -10.34505 | -46.63636 | 2025-05-06 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e137f9c-6239-359a-8e89-6340fde5bc64 | -6.69642 | -42.13002 | 2025-05-06 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 174f2b8e-55fe-362e-b1a0-31acbc88b2fa | -10.97573 | -44.43091 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 00b583fd-0d24-3d58-a1bf-a1a117a81c26 | -7.55013 | -45.87029 | 2025-05-06 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a5a15da-2a0f-324b-95ae-b88bb8b48de5 | -8.31022 | -48.0471 | 2025-05-06 04:44:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1fe6942-ae33-3f59-b4c0-3dfc971dbe3a | -6.70185 | -42.12956 | 2025-05-06 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 9895cf79-d40d-371b-9259-6214a38b166d | -10.97968 | -44.43837 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0679af22-4474-3619-bd26-f2e4652390d8 | -6.94325 | -47.89946 | 2025-05-06 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7855c476-f5c3-3ff0-b9a2-8efd66f7209c | -8.30957 | -48.05136 | 2025-05-06 04:44:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f923cb5e-d707-35b3-9454-5d410db775bf | -8.30657 | -48.04655 | 2025-05-06 04:44:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6c51991-4ae2-326b-8e75-e027ec01bbca | -8.20042 | -48.98775 | 2025-05-06 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b6e3177-e807-3117-9892-39fa318f3a8a | -6.70138 | -42.13278 | 2025-05-06 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| bf060500-8700-3562-a806-d976228e574c | -10.97901 | -44.4436 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1daa937-2b98-3117-8d31-80e42eb2f855 | -11.00224 | -44.34356 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ded5255b-f657-3357-83f1-daf4fe4a543a | -10.98035 | -44.43313 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 919c523f-680b-37ea-b666-943f46125ff2 | -11.18984 | -44.50824 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 792698f4-56b0-360d-ab0b-4ac30f85401a | -10.98937 | -44.43795 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7836a077-5eed-32c5-b42c-17144da11a01 | -7.55921 | -45.83744 | 2025-05-06 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d1149bc-8919-3279-ba7e-8321f8a1578c | -7.55425 | -45.87086 | 2025-05-06 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93dcc3d0-fde1-3a34-b7ba-1812852c7834 | -12.17441 | -44.34174 | 2025-05-06 04:44:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README7.md)
