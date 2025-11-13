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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7962099-93d3-329f-9c65-95659008e560 | -4.06823 | -54.11159 | 2025-11-13 05:03:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 203b3c4c-3997-3e42-b666-0b3603b7e5f4 | -4.61253 | -49.29023 | 2025-11-13 05:03:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c46513fc-7d83-3454-a4b9-a1145281a9b7 | -6.15678 | -48.05149 | 2025-11-13 05:03:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f4ce2de-f77b-36bd-8d5f-f9423ad79f03 | -4.45789 | -46.5595 | 2025-11-13 05:03:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 351a31f7-0bc7-3c8b-b006-4d777a47a475 | -3.24227 | -52.91798 | 2025-11-13 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 623b9fb7-49db-3950-a0d3-1c54b994dcda | -10.77935 | -48.14397 | 2025-11-13 05:03:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f921896d-59c1-3c0c-bb4c-bc1798495fb3 | -3.86067 | -49.79286 | 2025-11-13 05:03:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5d642c4d-5ac5-33b5-ba52-b72a8d70ba69 | -11.00621 | -49.04302 | 2025-11-13 05:03:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7f230c4-5bc6-368c-b39e-08bea45b34b7 | -9.64403 | -44.54745 | 2025-11-13 05:03:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c73ff34e-d5d5-3184-87ad-80999e1669da | -4.10283 | -48.0159 | 2025-11-13 05:03:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b55133ec-f6a3-3e34-8110-c1ad6e5be9d7 | -3.86839 | -49.79768 | 2025-11-13 05:03:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a0902be-7e5f-3ebb-8985-6dfe45c447b0 | -6.1616 | -48.05227 | 2025-11-13 05:03:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 310782b0-8410-3719-8bff-e9bdc4bace41 | -4.20145 | -50.0939 | 2025-11-13 05:03:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37a6bd9e-06d9-3c00-965d-f9c81b316256 | -5.83824 | -47.56427 | 2025-11-13 05:03:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8085e24-4a42-3761-a1bb-c8e3713c33e5 | -5.35681 | -46.75991 | 2025-11-13 05:03:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31f1e69a-7b8e-3869-8401-c759a6b3e463 | -4.7109 | -46.44336 | 2025-11-13 05:03:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| a4cc7d09-46d1-3b1f-a163-9f311562b1b8 | -4.64012 | -48.74982 | 2025-11-13 05:03:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 177e6f26-b8c6-34ff-90da-656c52b46d08 | -4.20795 | -48.56937 | 2025-11-13 05:03:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d445b3ad-ccd5-38fd-8925-a1525b09277d | -3.86424 | -49.79716 | 2025-11-13 05:03:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41b00415-7755-3bb6-9a8c-2b3b443536ef | -5.35635 | -46.76311 | 2025-11-13 05:03:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f731139-82f9-3b14-abe4-ba31e7bfa0e2 | -5.72452 | -44.83694 | 2025-11-13 05:03:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 555f0a5b-b20b-367a-9836-35f30c5178e3 | -9.62944 | -44.56083 | 2025-11-13 05:03:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 80da5d1e-5fc2-3915-969f-9d114e295a4e | -9.62727 | -44.56077 | 2025-11-13 05:03:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7ef94b07-0dc9-36a5-99bc-057d1bd12d37 | -4.20727 | -48.57401 | 2025-11-13 05:03:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 31d9b81c-d526-355f-8642-efd821d12684 | -9.62793 | -44.55556 | 2025-11-13 05:03:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 471279c0-f181-3de3-aeb6-2d408885dfc1 | -4.84687 | -49.26509 | 2025-11-13 05:03:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27e715de-3c66-3340-b370-db45f49fba76 | -4.74566 | -49.89675 | 2025-11-13 05:03:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29a6a929-aee4-35b9-bd1d-f3dfb0c43426 | -9.64339 | -44.55272 | 2025-11-13 05:03:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53abafe2-57e5-37ba-8cea-17dafd2c664b | -5.0952 | -47.46741 | 2025-11-13 05:03:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88883fab-f778-3eaa-91e1-5f421ae22251 | -3.08074 | -53.10055 | 2025-11-13 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdfe5ac7-6315-3dfe-ae68-cd4c47edf8f2 | -4.8944 | -48.9704 | 2025-11-13 05:03:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f848c797-e874-3bd2-a213-11a0de0c7b58 | -5.3881 | -46.76451 | 2025-11-13 05:03:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8ffd1b1-e70d-32f8-aca4-846634be1fc2 | -10.6307 | -45.24672 | 2025-11-13 05:03:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69fe3faf-6983-3ea8-bab0-ede56d4ecc90 | -5.32515 | -45.1954 | 2025-11-13 05:03:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4675abae-e415-3c49-be04-14e8160120f1 | -5.03891 | -49.97824 | 2025-11-13 05:03:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d203fdf-58a7-3535-845c-8aff80e7694b | -5.08384 | -47.93312 | 2025-11-13 05:03:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c6bff08-5b86-3950-b884-23c0aabe1799 | -4.0121 | -48.80287 | 2025-11-13 05:03:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4b468910-e917-37ad-a669-bc6b9402d8cc | -3.89823 | -52.11731 | 2025-11-13 05:03:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb307295-7ccb-3082-829f-ed1ef71f1260 | -9.19853 | -49.47891 | 2025-11-13 05:03:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 117f25cc-e2c9-3a7d-830b-3c6a764ab018 | -5.67784 | -46.01225 | 2025-11-13 05:03:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91d1fba0-63da-313c-8ca8-f3e313426ec9 | -5.57916 | -47.1039 | 2025-11-13 05:03:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a5e84830-b4ba-363d-be65-f83309c1fa46 | -15.22361 | -51.126 | 2025-11-13 05:05:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bb79009-cd81-3060-ba13-4dad0af03e26 | -12.9991 | -49.79236 | 2025-11-13 05:05:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6d572a7-a9b4-3f26-a6ec-04da1ad706ea | -12.06131 | -48.21789 | 2025-11-13 05:05:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e4afd3d-1d38-393c-9e69-128015d3393c | -15.17259 | -51.27452 | 2025-11-13 05:05:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b29ca6b-ffac-319e-874f-152a18fa5b8c | -12.59261 | -48.33195 | 2025-11-13 05:05:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d82bd7f6-04f2-371a-ac99-112feff3968b | -12.66133 | -46.753 | 2025-11-13 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| f6440d09-d619-365f-a5f6-8ff51da6d456 | -12.65572 | -46.75489 | 2025-11-13 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5176ed54-dd9a-3160-9030-ea16fa8be4cc | -12.6509 | -46.74584 | 2025-11-13 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 23fe3720-7628-3e06-98c2-bd9bc6a5f6c1 | -11.73322 | -48.53836 | 2025-11-13 05:05:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1329d5c7-ca5a-39f2-ba1d-2885fa9edbdd | -12.06214 | -48.21147 | 2025-11-13 05:05:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b294e9e8-ec64-370d-8b1a-a83a50215ccb | -12.64977 | -46.75161 | 2025-11-13 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 17c46c81-383f-3938-be8a-61c0690fb086 | -12.59741 | -48.33593 | 2025-11-13 05:05:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b635ab5b-50dd-35d5-b776-76ae473a5007 | -15.16875 | -51.26948 | 2025-11-13 05:05:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6a2fbac-b96b-31db-b895-100fe9d2a713 | -12.66198 | -46.75147 | 2025-11-13 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 427d9244-6a78-350f-99aa-c6f522a557e5 | -16.88241 | -51.6539 | 2025-11-13 05:05:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff8ccab3-cee7-33e1-a44d-04c679c678f1 | -16.53097 | -52.77464 | 2025-11-13 05:05:00 | NOAA-20 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 641278c3-44d4-36bf-8fb1-04f70f5e4e45 | -12.06173 | -48.21469 | 2025-11-13 05:05:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5c7c6f55-0f27-3519-ad01-a48b4d6f0261 | -16.27724 | -52.93476 | 2025-11-13 05:05:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc69d686-54d8-3d50-8e83-6bee763474cb | -12.06251 | -48.21518 | 2025-11-13 05:05:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8c4d4b80-5c76-3ff3-867f-13c25d9a6694 | -15.4952 | -52.80635 | 2025-11-13 05:05:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2347b93-37a0-3f5a-a004-a362540ff028 | -15.16817 | -51.27392 | 2025-11-13 05:05:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 417ec26c-9a72-301b-a00b-cff709ae73bd | -16.98584 | -51.60891 | 2025-11-13 05:05:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2283bc81-d18e-3a30-91bd-22a173629c03 | -12.4184 | -54.48326 | 2025-11-13 05:05:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec921160-a381-3855-aeb1-f2305d8b7a34 | -17.32244 | -46.50511 | 2025-11-13 05:05:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2955b588-4105-3368-be11-8477e6ef892e | -12.06291 | -48.21196 | 2025-11-13 05:05:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 229d40cf-04b9-31e0-b7de-f4d9a91aa03f | -14.86842 | -52.8666 | 2025-11-13 05:05:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7de3722e-d760-3b34-90c7-8b0637e1c35d | -11.09952 | -54.09442 | 2025-11-13 05:05:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4290208e-46ed-322c-9335-e2e63f006860 | -12.66246 | -46.7473 | 2025-11-13 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fb037ee2-6f26-37e7-8426-e6928638e678 | -12.41516 | -45.79641 | 2025-11-13 05:05:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 136c64cd-31ad-39fa-86a7-ada0894896b4 | -12.66183 | -46.74884 | 2025-11-13 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9e857514-eecf-366f-92f9-2a5e4748796e | -11.7336 | -48.53535 | 2025-11-13 05:05:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0c74fc80-2f86-3f5f-bc99-9e8ae8f8c1a1 | -12.65078 | -46.74322 | 2025-11-13 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 413007ed-2895-3f9f-971d-4e199a702839 | -12.41781 | -54.48727 | 2025-11-13 05:05:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5edb3ccc-d311-37ff-bbf9-e7c91d6913c6 | -12.65027 | -46.74743 | 2025-11-13 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e93b3774-fd49-33e5-9865-c6d11f30b331 | -12.6676 | -46.74963 | 2025-11-13 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2cf0deba-5fd4-33e6-9b64-a75037931135 | -12.66823 | -46.74812 | 2025-11-13 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 62e33b19-cba1-3f12-851b-9f691dc1c48f | -12.41488 | -54.4827 | 2025-11-13 05:05:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ca48d81-b850-323f-b2d3-4ae2156ceedb | -16.88246 | -51.65236 | 2025-11-13 05:05:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c16470a1-45e5-3236-8b1b-f1b0b252669f | -12.6615 | -46.75566 | 2025-11-13 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| e8fd853c-ad9c-37de-82d5-72c4097448d5 | -13.77943 | -49.39877 | 2025-11-13 05:05:00 | NOAA-20 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 537795ea-0b18-3daf-aa47-e91652f23825 | -12.6562 | -46.75072 | 2025-11-13 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3144a8a1-96d6-37d9-a2df-013ca4748134 | -16.88631 | -51.65747 | 2025-11-13 05:05:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f2ce78b-83d3-35f5-bcaf-b915c3f322a3 | -12.64449 | -46.74677 | 2025-11-13 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94192203-8a45-356d-b614-75539bb34f40 | -12.5978 | -48.33275 | 2025-11-13 05:05:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21266801-92c1-36f2-8af2-d116b3359fe3 | -12.99844 | -49.7975 | 2025-11-13 05:05:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b17d195-593b-37dd-9afb-67691a670bf3 | -12.66081 | -46.75719 | 2025-11-13 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| a69084ed-2f6d-3650-97f0-84993892fa3e | -12.65042 | -46.75003 | 2025-11-13 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 95da7c79-08f7-3db5-be58-f330cd0cc2b0 | -17.32298 | -46.49987 | 2025-11-13 05:05:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 317013ae-b680-3465-8ec6-b5d329f8828e | -14.67831 | -51.89115 | 2025-11-13 05:05:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9cdaa02-1e16-3110-98a7-bd0d2c2b6b66 | -21.89362 | -56.74143 | 2025-11-13 05:08:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| caa85d87-1815-37ac-982a-e7611bcc9542 | -20.60469 | -55.80764 | 2025-11-13 05:08:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c31bc62-ebc5-3154-8a5b-22a6bef7cff3 | -17.53281 | -53.71598 | 2025-11-13 05:08:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92af287a-de7a-3846-805c-21a4a89e6324 | -17.55996 | -54.02319 | 2025-11-13 05:08:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c375ab3-0a4c-35fd-8ce6-a4ea1d2e4621 | -17.5367 | -53.71656 | 2025-11-13 05:08:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf287ae0-5aa5-321d-aaf5-4f37ffefe816 | -21.89011 | -56.74088 | 2025-11-13 05:08:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| eb07f00c-5e5a-347a-934a-62681fbd547d | -21.90124 | -56.73835 | 2025-11-13 05:08:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 05e72a00-9d6e-3b9e-af15-27b69d6778f0 | -22.73204 | -44.8496 | 2025-11-13 05:08:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8f847a11-a67e-3bfa-b93d-8be0c1a05410 | -21.8907 | -56.73666 | 2025-11-13 05:08:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ef6f545f-dcef-3200-bb51-02a7ad7de39d | -17.53738 | -53.71154 | 2025-11-13 05:08:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README38.md)
