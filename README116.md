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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a54b578-d33a-3e59-b677-50f149df376d | -7.81336 | -49.43215 | 2024-10-25 12:51:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f3a1d0a6-ee0c-350c-a69d-67271f4d8108 | -7.59343 | -49.61499 | 2024-10-25 12:51:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cc47babc-ea72-3c52-a48d-bcd5e7c0b0e5 | -7.49208 | -48.59769 | 2024-10-25 12:51:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c6f61366-dbb7-3ff2-a1d1-98e6c5e03e19 | -7.48315 | -48.59644 | 2024-10-25 12:51:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f55c0bf1-fbb7-361f-ad26-3082b191f34f | -6.6048 | -48.48456 | 2024-10-25 12:51:00 | TERRA_M-T | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 5c9241b6-03a1-34d4-b0a4-ac3fae8aefed | -6.59589 | -48.48332 | 2024-10-25 12:51:00 | TERRA_M-T | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 19.3 |
| e137cc58-a95d-3f57-ae47-ed1456b069d6 | -8.09649 | -50.09497 | 2024-10-25 12:51:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| bf8f205c-c6c5-3669-b3a0-d7dee5da2f36 | -8.0245 | -49.63482 | 2024-10-25 12:51:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c7f3bf04-8ae1-37b5-96d2-7a2849525fc2 | -8.9812 | -48.81393 | 2024-10-25 12:51:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 896a951d-6bf9-3884-954e-5a2fa65830a8 | -8.97991 | -48.82299 | 2024-10-25 12:51:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b418c6c3-10c2-391b-ae27-b4abb346dce1 | -8.96661 | -49.10649 | 2024-10-25 12:51:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 65e0263d-fbbc-3727-905a-a079f3452f85 | -8.93102 | -49.10145 | 2024-10-25 12:51:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 71ab6656-854a-348c-a854-52b2313ec2d5 | -8.92212 | -49.1002 | 2024-10-25 12:51:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d9cead35-55c1-31bb-9667-dd1e010ce323 | -8.58042 | -49.2278 | 2024-10-25 12:51:00 | TERRA_M-T | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5dc2a9fc-6884-360d-a2d7-6ef8c9dc4a4c | -8.54394 | -49.55578 | 2024-10-25 12:51:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| f4cb05ce-153c-337b-a921-1ca011d18e29 | -8.71672 | -49.94763 | 2024-10-25 12:51:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 8a9c1c4e-40dd-39f9-8e3e-573bb947c1ec | -8.37883 | -50.118 | 2024-10-25 12:51:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9fcb35ba-68a4-3ad8-b03e-16d45ce896bf | -10.37195 | -49.91505 | 2024-10-25 12:51:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 5b94f43a-69b0-3b14-ade6-ef9cefb0067f | -9.58388 | -49.56372 | 2024-10-25 12:51:00 | TERRA_M-T | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 9ea29cf2-7bd1-3d31-acb1-8be74c0b34e3 | -10.8785 | -49.53339 | 2024-10-25 12:51:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 33a5524b-16ae-3381-9d2b-5da31b37714a | -5.1092 | -50.71447 | 2024-10-25 12:51:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f75e353f-83ff-3448-a9a9-33b8b7317ec6 | -7.43679 | -49.99614 | 2024-10-25 12:51:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e51d7263-97ce-30e9-8d95-9bba88d2587b | -7.35855 | -50.02478 | 2024-10-25 12:51:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 02bf5aa9-4225-3bad-8a5d-fe0a3abfa294 | -7.22471 | -50.24825 | 2024-10-25 12:51:00 | TERRA_M-T | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0c614b66-bd6d-30ad-abc4-af060f4e699e | -6.90039 | -50.32272 | 2024-10-25 12:51:00 | TERRA_M-T | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 188985f7-a784-3ce9-8b10-6eefc8225d24 | -6.80249 | -50.23691 | 2024-10-25 12:51:00 | TERRA_M-T | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0b2dd5de-537c-3c30-82ca-4951a26a029d | -6.68375 | -49.97598 | 2024-10-25 12:51:00 | TERRA_M-T | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| cd2fe384-0ac0-3820-8d29-8dfe6b3767b8 | -8.87901 | -50.54157 | 2024-10-25 12:51:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 6865981c-0a8d-3901-815e-3d37fef87f8c | -8.87766 | -50.55067 | 2024-10-25 12:51:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 531d528f-584d-35fa-9207-53b63e112643 | -8.335 | -50.41584 | 2024-10-25 12:51:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f9b68706-0706-3afa-9cc5-a118c7c9f2d0 | -9.6687 | -50.81575 | 2024-10-25 12:51:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9fc83eb4-eaf5-33b5-91ff-a49edbf7146a | -9.48588 | -50.8045 | 2024-10-25 12:51:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| fb3ca212-41a2-3601-a282-43653af641b8 | -9.48452 | -50.81369 | 2024-10-25 12:51:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 78a8c95b-063f-3033-a8db-992481bff394 | -9.48315 | -50.82287 | 2024-10-25 12:51:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 75afbd88-d99d-36b3-aee2-9fa92866d4d3 | -9.47689 | -50.80318 | 2024-10-25 12:51:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| c0dbb63b-fb2e-3944-a5ac-a4588ccb20a2 | -9.47553 | -50.81236 | 2024-10-25 12:51:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 5520ef93-8236-3003-9b80-a840e624e95b | -11.01556 | -51.49947 | 2024-10-25 12:51:00 | TERRA_M-T | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 04afdbca-5aa6-3e15-9376-b25fe4c586fa | -10.51127 | -53.49343 | 2024-10-25 12:51:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 42b38c91-a2ae-386a-85df-75dab0dc1c02 | -9.51243 | -54.66251 | 2024-10-25 12:51:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 84581709-1f48-3524-bd82-cc8a5742d9e6 | -10.79279 | -53.85265 | 2024-10-25 12:51:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3487bddb-fcc9-3e32-a18b-9ceec001c658 | -10.66745 | -54.06296 | 2024-10-25 12:51:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| a9b7f53c-7f76-3b46-8a5b-f02427c2c66f | -6.32263 | -58.29396 | 2024-10-25 12:51:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| d2e74f58-b226-3e4b-805c-d2310541b384 | -17.80332 | -41.08178 | 2024-10-25 12:53:00 | TERRA_M-T | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.4 |
| 63ae8e3c-c2cd-3adf-93be-d46356929ede | -17.80038 | -41.07676 | 2024-10-25 12:53:00 | TERRA_M-T | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 57.3 |
| dc0676a3-ce88-314b-beb8-ea26b5f9498f | -16.31013 | -42.56452 | 2024-10-25 12:53:00 | TERRA_M-T | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| b2819746-c993-33ce-8117-4ae8432122ac | -13.57429 | -43.42018 | 2024-10-25 12:53:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 35c06cc8-0751-321e-bb1d-31b8dc6cd6aa | -13.06879 | -43.00939 | 2024-10-25 12:53:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 33.5 |
| f8df5513-41ca-365f-9290-c13c3a4825be | -12.99626 | -43.02583 | 2024-10-25 12:53:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 103.9 |
| 84d2c690-2928-313b-93ac-8e55800b31ce | -15.52706 | -43.12834 | 2024-10-25 12:53:00 | TERRA_M-T | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 8235a5d4-b2fa-3cc9-b7d5-56f0e5f1b40a | -12.91762 | -44.3577 | 2024-10-25 12:53:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 891b1c78-512f-3288-96f5-bcda444b9e86 | -12.90702 | -44.36192 | 2024-10-25 12:53:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| ec09ee31-9aee-3c9d-9bc7-fc02229da9ec | -12.90516 | -44.35602 | 2024-10-25 12:53:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |
| f990b91e-1ecd-30fa-a99f-58eed180a33d | -14.28426 | -43.93491 | 2024-10-25 12:53:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 822c31ee-99cf-3d5b-9d3f-7e31512951ec | -14.14332 | -44.25145 | 2024-10-25 12:53:00 | TERRA_M-T | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| d7158f31-12e9-33ef-88ed-f11c53675181 | -13.83722 | -44.19834 | 2024-10-25 12:53:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 5de54069-c5df-376a-bf76-5faef0e0a0c1 | -16.64558 | -45.14257 | 2024-10-25 12:53:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 639afade-ffc3-3995-89b3-0f9ecdd7608f | -16.64345 | -45.13652 | 2024-10-25 12:53:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 50056af5-882b-35a9-93fa-b920ef2dfaff | -12.90584 | -45.07961 | 2024-10-25 12:53:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 85e782f6-b926-3d9b-b065-27ccba50278a | -12.52668 | -46.8097 | 2024-10-25 12:53:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 5daaf9d7-86d2-37d8-ab08-81dce9fc92d5 | -12.22171 | -51.07813 | 2024-10-25 12:53:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0927148f-da71-351b-898c-3aaec3d10c9e | -12.80246 | -51.70116 | 2024-10-25 12:53:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 18af1f49-d41e-3bf3-84d2-14c9caa37609 | -12.43011 | -51.3535 | 2024-10-25 12:53:00 | TERRA_M-T | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0803e1cf-0852-3bdc-b6eb-006f837b4728 | -12.42156 | -51.34576 | 2024-10-25 12:53:00 | TERRA_M-T | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d87e2424-7295-3ea8-bc82-9995a074ae41 | -12.22673 | -54.46154 | 2024-10-25 12:53:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 95bfd8cb-13de-34fa-8c75-afde380e909e | -12.15672 | -54.55928 | 2024-10-25 12:53:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 20bb4874-3b59-3d1e-88a9-641d78ab8417 | -12.06752 | -54.74886 | 2024-10-25 12:53:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 9af616ee-70c9-335e-81b5-14fc8ab32644 | -12.06531 | -54.7628 | 2024-10-25 12:53:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 6bd02c46-e141-31b9-823c-10b8a15e7c31 | -11.99816 | -54.60435 | 2024-10-25 12:53:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| cacd5bb5-7223-31fb-9f48-d562c82efc4d | -11.32832 | -54.47911 | 2024-10-25 12:53:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 6b5712b4-21a0-3736-acbd-85cedf9570cc | -12.60593 | -55.20557 | 2024-10-25 12:53:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 0c973381-41a1-3920-9452-e94a04c474dc | -12.50566 | -54.75364 | 2024-10-25 12:53:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| b1cd7bd8-b949-3d3f-ae5c-c7ed8aa69462 | -12.46706 | -54.71906 | 2024-10-25 12:53:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 625032a5-ed2e-3c1d-88e8-6e01c84ab4ff | -16.54952 | -57.22474 | 2024-10-25 12:53:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.9 |
| 93d64cbb-fca2-355a-b8dd-7e13d5a14b7d | -17.30675 | -57.29422 | 2024-10-25 12:53:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.7 |
| 7cb37dc5-1d00-33a9-a2e8-595558988823 | -17.30179 | -57.28735 | 2024-10-25 12:53:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.0 |
| 80fc7fa6-2f97-3110-9eca-f39169d7ae17 | -17.2531 | -57.5004 | 2024-10-25 12:53:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.1 |
| 7f81bc1b-e409-37a3-a3bf-b401639b02f4 | -17.24237 | -57.20407 | 2024-10-25 12:53:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 5ad83070-2896-3be4-9304-0f0762c95da1 | -17.23933 | -57.22147 | 2024-10-25 12:53:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 380.6 |
| fdba8c07-95f6-3ca1-ad40-dad5a5801870 | -17.22744 | -57.21925 | 2024-10-25 12:53:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 858.5 |
| 006e27d4-d8a4-3979-b010-755d584240a2 | -17.22437 | -57.23669 | 2024-10-25 12:53:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 391.9 |
| 43817522-e888-3e7a-aea7-2fcfb23d6a5e | -17.22248 | -57.21144 | 2024-10-25 12:53:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 01ad1569-bd1f-3e18-b6a8-d612a647c897 | -17.22129 | -57.25418 | 2024-10-25 12:53:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.9 |
| 3da64abf-b9d0-3855-868b-cd70ecf1e1f3 | -17.21953 | -57.22891 | 2024-10-25 12:53:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 240.3 |
| 620e88b4-f37e-3ccb-8637-a243542f221b | -17.21658 | -57.24643 | 2024-10-25 12:53:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.6 |
| 033adfbb-834f-321c-9459-5d202c825118 | -17.19118 | -57.28492 | 2024-10-25 12:53:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.5 |
| 6a981dea-0012-3b15-ac38-d2050234246d | -17.18368 | -57.29486 | 2024-10-25 12:53:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 9680ed6e-c209-3b1b-a32b-d47bd52ccdf2 | -17.08262 | -57.41803 | 2024-10-25 12:53:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 73100683-d905-36d2-afa6-a02c04c0da06 | -17.00368 | -57.34045 | 2024-10-25 12:53:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 90afa480-325e-3116-a40e-4993ba010a56 | -17.00062 | -57.35844 | 2024-10-25 12:53:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.5 |
| c391439b-6e7e-378e-ba5e-127c8f20d2fa | -21.47598 | -50.49312 | 2024-10-25 12:55:00 | TERRA_M-T | BILAC | SÃO PAULO | Brasil | 3506409 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 478dfb4f-ebb1-3ddc-bf3a-7fd97e3a17bd | -21.47458 | -50.50347 | 2024-10-25 12:55:00 | TERRA_M-T | BILAC | SÃO PAULO | Brasil | 3506409 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 066b55fc-6904-3fc2-9881-6bc3275ab431 | -18.33289 | -56.23899 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.5 |
| bab92f0c-62fc-3a45-9a18-911c6f799795 | -18.32096 | -56.17832 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 1e5cf3c6-7523-3266-9afc-3775b81e248f | -18.31866 | -56.17125 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.4 |
| c695c021-e647-3a3d-a745-8e709d04707a | -18.31018 | -56.17636 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.1 |
| 4571489a-26f3-3b0e-a8b0-66e12845e4be | -18.3088 | -56.24931 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.4 |
| 23436cfe-6d0e-33e1-9d32-50cbb2b755d7 | -18.30788 | -56.16928 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.2 |
| 46c1a5d9-2eae-34c1-a914-a8714ba0deb2 | -18.30698 | -56.24231 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.0 |
| ff68be3c-e71f-3e8c-baa7-9350efcb6315 | -18.30462 | -56.25663 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.5 |
| 4148776d-cb18-3b2f-948d-5446d1704ee2 | -18.30288 | -56.21885 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.7 |


[Clique aqui para ver as próximas entradas](README117.md)
