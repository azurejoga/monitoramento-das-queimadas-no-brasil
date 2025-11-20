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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2585feaa-fb82-35f4-bf8a-14af074e9e5c | -10.88739 | -47.63374 | 2025-11-20 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf20c350-66dd-312c-8195-3c6010a8b8cf | -11.2622 | -48.49034 | 2025-11-20 04:12:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cc94f716-2f3b-3075-b027-c7d165ad3bde | -11.25796 | -48.48958 | 2025-11-20 04:12:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5196846-cc3b-3db7-884c-ed60462989da | -8.78988 | -35.14735 | 2025-11-20 04:12:00 | NPP-375D | BARREIROS | PERNAMBUCO | Brasil | 2601409 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5f448278-4f25-3e27-888f-20a04c74ee32 | -6.2288 | -48.06553 | 2025-11-20 04:12:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6edbc8b3-355a-39d6-84f6-91c5a6fbc35a | -9.70698 | -49.93961 | 2025-11-20 04:12:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc1689b1-8e7a-3c11-8bfa-6f9cba4ba08e | -10.35775 | -48.90787 | 2025-11-20 04:12:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| a8c8da37-98af-3a44-ac61-d5cb231a693d | -10.8856 | -54.14364 | 2025-11-20 04:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e26e070-d0ad-336f-b44c-a4e6dbb22a0f | -6.2393 | -48.05812 | 2025-11-20 04:12:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68990cc2-5260-362b-a04e-b1844a804211 | -7.55594 | -47.58062 | 2025-11-20 04:12:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de7ef609-770f-3ae6-9742-44b699f7b735 | -10.66523 | -49.72067 | 2025-11-20 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42995f6d-c541-33f3-a15e-efc6b2afd30a | -10.66704 | -49.71085 | 2025-11-20 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5155c976-be48-3699-8c0e-55850462c019 | -10.36821 | -48.90066 | 2025-11-20 04:12:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 23d846a2-a261-3b9e-a780-3f3193c9aa20 | -10.84303 | -56.96345 | 2025-11-20 04:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5df8c306-ea94-3c7e-b537-1c6ac63c3037 | -10.84484 | -56.95933 | 2025-11-20 04:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| debe8e2f-7d38-3232-8903-cccb41b54dc8 | -16.29629 | -52.93618 | 2025-11-20 04:14:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0539286-cb85-38eb-a569-959a6d9afa52 | -17.67886 | -42.44047 | 2025-11-20 04:14:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5839c18-d6ce-3ed7-8bf5-f7b62bf56b46 | -18.18848 | -47.65244 | 2025-11-20 04:14:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a58f416d-b7e6-3939-a160-37950c22ebff | -14.47162 | -46.97647 | 2025-11-20 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd898931-ec44-3462-b406-f62eabbc39e2 | -17.61476 | -54.18007 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8aa7ab5c-ec3c-3795-991f-7f459e469f3a | -13.69608 | -48.43241 | 2025-11-20 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 208871f1-9abe-39ad-8ccc-7c908d5a75dd | -14.66495 | -46.52379 | 2025-11-20 04:14:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e219d3ff-db79-372e-a5a8-dea2f5ab4b61 | -14.95162 | -47.33904 | 2025-11-20 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e1a67c5-8e62-315c-9fa1-6ad5f2b29b4d | -19.79393 | -46.07717 | 2025-11-20 04:14:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a0c99b3-9dd4-3b0f-a2cc-e514d577c0c0 | -16.29643 | -52.93641 | 2025-11-20 04:14:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2762282-0f8e-3bb6-acb2-42d6f41fbc42 | -19.08132 | -41.75858 | 2025-11-20 04:14:00 | NPP-375D | CAPITÃO ANDRADE | MINAS GERAIS | Brasil | 3112653 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e035b38d-71a4-3c46-a1c6-4d69ada3d2f4 | -19.24862 | -46.44976 | 2025-11-20 04:14:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1b1c7883-e936-326e-8c16-120bb7dcfb98 | -18.12367 | -54.52567 | 2025-11-20 04:14:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d43029a5-0dec-3613-ac02-52ae62e3b19f | -13.36576 | -47.661 | 2025-11-20 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 175bc6f8-e682-37fc-8f48-5ce03d82692a | -14.53039 | -48.6194 | 2025-11-20 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57b8a204-6bdc-34b4-856e-ccc41637e6f9 | -12.9467 | -47.71851 | 2025-11-20 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18b6c8ee-5437-35b7-ae3f-72fa51219d2f | -15.78765 | -43.35703 | 2025-11-20 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 28.1 |
| f8327d9d-58a8-3933-aba4-89225e98b6bb | -17.53681 | -53.70508 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f94c7d35-8eee-332b-a5a3-7bd0a1088ade | -14.62032 | -47.19484 | 2025-11-20 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a69e4928-f776-36ec-82d1-e750766cf5ff | -12.88122 | -50.153 | 2025-11-20 04:14:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 820241b5-5787-3615-825c-aa57bc328e5a | -13.92769 | -47.47717 | 2025-11-20 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b3f4cef-f371-35da-a812-8a19b5df6390 | -17.53718 | -53.71692 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8031933d-46a6-37dc-bb27-7167070368c0 | -12.94189 | -47.72289 | 2025-11-20 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fbf3a01-f8c6-3a0f-adf5-068571ff4e38 | -17.17557 | -43.29972 | 2025-11-20 04:14:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1afa02ad-48af-3ef5-af1c-629104c98e9d | -16.29565 | -52.93925 | 2025-11-20 04:14:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b79281d2-a6b0-3707-8578-58fe0371a425 | -19.7973 | -46.07781 | 2025-11-20 04:14:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f06dc43-3fd5-3fb2-a5ac-024cb24f2964 | -14.55405 | -48.62749 | 2025-11-20 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a19fab85-9ba5-36c2-bc33-ec6cddbc30bb | -15.05805 | -48.30824 | 2025-11-20 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b351140a-f3bd-300c-963e-040882453956 | -13.92855 | -47.47228 | 2025-11-20 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3876849d-2bab-39ab-84c6-e0df93f7a382 | -12.94593 | -47.71481 | 2025-11-20 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75a1a338-96ec-3242-bb87-d66cac323175 | -13.4876 | -46.71417 | 2025-11-20 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7cdb168f-d14f-3936-9008-e797aa8c1341 | -17.62257 | -54.19736 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9755e4d-9b5b-3f89-b129-e950277149e9 | -19.08191 | -41.75449 | 2025-11-20 04:14:00 | NPP-375D | CAPITÃO ANDRADE | MINAS GERAIS | Brasil | 3112653 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 694ae66e-f491-3be8-bfb7-d8e2515e959b | -13.0712 | -49.51453 | 2025-11-20 04:14:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7eb41685-c8c3-3549-bc46-552e4b0d96e2 | -19.56236 | -49.49943 | 2025-11-20 04:14:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f885c9c-a523-30fd-ba38-d5702d566bb0 | -14.51253 | -44.30269 | 2025-11-20 04:14:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ad52475b-c085-364e-8a0d-cda352f610f9 | -19.83484 | -46.93022 | 2025-11-20 04:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| becbd390-dcb1-3293-bf37-8e13d27dfcf0 | -19.9757 | -44.85488 | 2025-11-20 04:14:00 | NPP-375D | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a446bef-fc9b-3824-85ec-2f8684d3b3f3 | -12.94366 | -47.71263 | 2025-11-20 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e0db5c8-4019-3823-a05f-f9c505db68a4 | -15.54573 | -50.65966 | 2025-11-20 04:14:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6ca1a1b-80f5-33a2-a9dd-2ba7ee87d859 | -15.25705 | -53.66589 | 2025-11-20 04:14:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63eb6eaf-098f-32c5-a084-598fc2cff2fd | -12.69551 | -49.8109 | 2025-11-20 04:14:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fb3ccd1-1493-386a-af30-278dcd09ba23 | -17.18003 | -43.29301 | 2025-11-20 04:14:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 305dde2e-1f32-32ae-8ecf-eaa35669be3d | -13.90726 | -47.41447 | 2025-11-20 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82133fe1-e7ce-3734-9320-1fb8cf2d7739 | -17.53872 | -53.7097 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc152b3d-ee61-33cf-b780-752bc7b3ae1c | -17.53947 | -53.70618 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ebbb6a5-e7ff-3679-9df4-0ea3beb34811 | -16.45491 | -45.017 | 2025-11-20 04:14:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6390eabc-3f3a-3123-88ab-24fcf51e141e | -16.32675 | -50.05371 | 2025-11-20 04:14:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6423dd5-386f-3276-a019-ff1d011de9d0 | -15.5412 | -50.65869 | 2025-11-20 04:14:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 593d10f3-b8ec-3ef4-a4a5-383343658cf0 | -17.53607 | -53.70866 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca71d5cc-5162-36cf-9a13-ae903c2f6d2f | -18.91719 | -47.17274 | 2025-11-20 04:14:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3af2e810-709d-36dd-b10f-a6d860522f64 | -17.6187 | -54.18854 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3d760275-cacd-34d4-b598-d368cc1432bd | -12.62769 | -48.87264 | 2025-11-20 04:14:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db653782-e625-3f98-ad5a-1334f904bdd7 | -17.62031 | -54.1809 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17e7f255-8723-3231-bf3d-0f77b32a4daf | -14.63233 | -46.54132 | 2025-11-20 04:14:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9eeaf4e2-fdae-34c5-b2b2-162152878adb | -15.53941 | -50.66819 | 2025-11-20 04:14:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 7f28baa6-1014-33a2-a4d1-a5889a89cb59 | -18.12451 | -54.52167 | 2025-11-20 04:14:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 777a8109-c57e-33da-8b65-4c31c1abf6bc | -17.61705 | -54.19635 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f97cc419-a8e0-3911-a63b-b8663595be11 | -19.94382 | -46.99206 | 2025-11-20 04:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24240bcf-b80d-31c0-9d36-1c16b9015940 | -14.94866 | -47.33384 | 2025-11-20 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4896437-dfc0-3e4c-b328-ddc9a11823fa | -13.8729 | -47.40903 | 2025-11-20 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0721a4ff-bba9-3e91-b915-6d6d2e8941d0 | -17.50398 | -44.92611 | 2025-11-20 04:14:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48a5f770-a7ce-3d43-9ae3-b405bc64d590 | -12.91482 | -45.10672 | 2025-11-20 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d0cbd79-6255-3233-a618-9c9b22633b4e | -12.98372 | -49.80153 | 2025-11-20 04:14:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c900797-4c36-3115-a081-f06d0d4f509b | -13.72648 | -49.9076 | 2025-11-20 04:14:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7858097f-f7ce-3ddf-b350-5b4c57b78e0f | -12.80928 | -47.55994 | 2025-11-20 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86484887-2e32-3a09-91a5-8d47adc129d5 | -13.92682 | -47.48215 | 2025-11-20 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5681578f-40c0-3b6f-b8da-897af8338608 | -12.94108 | -47.7192 | 2025-11-20 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0dc924fe-4011-3b24-af48-61d0e75d47ae | -17.53073 | -53.70762 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19d27afb-3fda-3c26-8d30-7a56e8d5198a | -15.75219 | -47.78398 | 2025-11-20 04:14:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 368c671e-cce8-3f57-9282-6a8cf047660c | -17.53796 | -53.71326 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98c54004-8e66-3534-870d-45e2307e3a42 | -17.40804 | -45.90964 | 2025-11-20 04:14:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9684eb99-a9c9-3680-aec3-0812e2be86c6 | -18.12537 | -54.51759 | 2025-11-20 04:14:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b205e379-11af-3e64-87c3-93521b3e98c0 | -19.71267 | -49.86425 | 2025-11-20 04:14:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea977ccf-a3fd-3e89-a326-c9a05759336e | -12.43233 | -47.87782 | 2025-11-20 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7d79494-701d-3057-b0c7-a9feaa330867 | -17.86286 | -45.23442 | 2025-11-20 04:14:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d78ab5b6-c136-31dc-820c-f63a999ba11f | -14.54122 | -48.6289 | 2025-11-20 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 014b4a0e-8c13-3cbb-a525-936a01c96877 | -14.54189 | -48.62526 | 2025-11-20 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0762549f-a208-313a-9805-826fc0276dc0 | -12.94759 | -47.71336 | 2025-11-20 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcd49899-5a50-3381-a0e1-403ecdcb2a54 | -12.67903 | -46.7744 | 2025-11-20 04:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2be78585-1706-3890-840f-98a35f0438ac | -13.48469 | -46.70908 | 2025-11-20 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| ae0cb4cc-eebc-387e-ae45-26b9f368b392 | -16.29582 | -52.93946 | 2025-11-20 04:14:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc920f84-7b74-3162-8abb-3940830dfd10 | -17.61788 | -54.19244 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fdbede1c-5146-3f3b-b386-050e5cc55dcf | -13.69537 | -48.43632 | 2025-11-20 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fa30684-a34d-3cc0-a7e3-5ca4be443f78 | -15.54483 | -50.66444 | 2025-11-20 04:14:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 26.7 |


[Clique aqui para ver as próximas entradas](README8.md)
