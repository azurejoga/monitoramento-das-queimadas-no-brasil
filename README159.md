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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 599af4a4-add1-3542-bc02-44cad9ce1339 | -16.8684 | -55.9103 | 2024-10-01 07:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 49.0 |
| 54a8356b-9dd2-33a2-b0ff-65819230ee8f | -16.8488 | -55.9128 | 2024-10-01 07:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.1 |
| ecf7c021-fa18-314d-ad20-a7867138934e | -16.8292 | -55.9152 | 2024-10-01 07:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.2 |
| c5022c69-cd57-32d5-86ec-97f6797787b9 | -17.0898 | -56.7297 | 2024-10-01 07:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.5 |
| c74b4eba-947d-392c-91ca-bcf259096b4c | -18.6977 | -57.3123 | 2024-10-01 07:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 6b112e3f-6cd6-3afd-9e0a-f5e709893533 | -18.6973 | -57.333 | 2024-10-01 07:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.8 |
| 209a4d19-6352-3d35-8437-2eb193300da6 | -21.5871 | -47.8591 | 2024-10-01 07:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 82f01283-9e6d-321a-9d65-9d5494131d81 | -22.3713 | -49.3011 | 2024-10-01 07:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.7 |
| 5ca3ce5e-0f62-3e30-ad05-502b15dd08ac | -22.3707 | -49.3244 | 2024-10-01 07:57:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 173.6 |
| 63057112-1138-35c1-aac7-64fec66e9919 | -2.85 | -50.72 | 2024-10-01 08:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43892d22-d295-3c8b-9e15-c5942c39a2d3 | -2.88 | -50.73 | 2024-10-01 08:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99585f8c-9498-3676-a83c-37e99a40dd52 | -11.6743 | -64.9983 | 2024-10-01 08:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 5f318809-3352-3714-ad7a-1e0f3bc6b097 | -11.6556 | -64.9802 | 2024-10-01 08:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d1750bef-8591-3bdd-a491-766b3a1415ed | -11.6555 | -64.9991 | 2024-10-01 08:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 3ebe7c1c-187a-37ab-a19e-8215f4988550 | -12.98 | -51.3213 | 2024-10-01 08:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| ab3d6837-db7b-33ae-8db2-7660697e93fc | -13.0204 | -51.1884 | 2024-10-01 08:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 0c67ae64-fb15-3dc7-a652-a027803c0a0c | -15.1934 | -49.4304 | 2024-10-01 08:06:31 | GOES-16 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 43.0 |
| ae14f3dc-aeba-35a8-a4be-f22c7ceecc67 | -16.7079 | -57.3696 | 2024-10-01 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 137.1 |
| 56546b95-c86d-3692-a066-8735c53edcf0 | -16.6515 | -57.233 | 2024-10-01 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 7eec3cbc-1ea4-3d20-acdf-a13913fc2b6c | -16.6512 | -57.2535 | 2024-10-01 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.5 |
| c5a29c43-473b-3598-99cf-7acecda3dda1 | -16.6319 | -57.2352 | 2024-10-01 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| d15040b5-0132-3eb6-a9ad-bd5b88320a86 | -16.6316 | -57.2557 | 2024-10-01 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 0e9b47be-3404-321e-92ad-05f17e7cc5ac | -16.7082 | -57.3491 | 2024-10-01 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.2 |
| 53710572-1652-3614-acf5-bb6fb5d8e95b | -16.7275 | -57.3673 | 2024-10-01 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 76afd1dd-b204-3c77-9de1-4932036c3f25 | -16.7076 | -57.39 | 2024-10-01 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| e03c8eac-0107-3316-b658-69f023f6d0dd | -16.8292 | -55.9152 | 2024-10-01 08:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| fd3421db-55c1-3d6e-a537-5889c408df4c | -16.8488 | -55.9128 | 2024-10-01 08:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.4 |
| cb92ce9f-1a1a-3050-9e0f-3d5e6fbfc5f3 | -16.898 | -57.7153 | 2024-10-01 08:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.0 |
| e833b4ef-ed68-3349-91fc-7cd49f3a9e02 | -17.0898 | -56.7297 | 2024-10-01 08:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| b82d8dda-72ee-3fff-b0f2-1e818379ef63 | -17.1574 | -56.2052 | 2024-10-01 08:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 557977b0-1100-34e0-add6-8f28b6193fa4 | -17.1577 | -56.1844 | 2024-10-01 08:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 4f4cda00-9d79-3f92-bbed-9b57d3ceaf77 | -17.1581 | -56.1637 | 2024-10-01 08:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| c0b3311f-cb57-31b6-853a-2dd3d260fe5a | -17.1771 | -56.2027 | 2024-10-01 08:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.0 |
| def018c4-6ca3-3e19-b9ce-5fcaa9de37ef | -17.1778 | -56.1612 | 2024-10-01 08:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.4 |
| 7cfa3faf-4c23-3507-bd23-ca18a28806ea | -18.6973 | -57.333 | 2024-10-01 08:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.7 |
| e7fac1a3-f828-3c5e-a680-3debb2422c77 | -18.6977 | -57.3123 | 2024-10-01 08:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 7b078635-1dc0-3a37-b243-0b00f7c38779 | -21.5871 | -47.8591 | 2024-10-01 08:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 6b9e0c98-2a16-3c6e-91db-80e7f25929d8 | -22.3707 | -49.3244 | 2024-10-01 08:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 145.5 |
| 2ad824c4-725f-3897-9097-18760bc3395e | -22.3713 | -49.3011 | 2024-10-01 08:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.0 |
| 0f2a8936-b129-37b0-96cc-4521e315ff58 | -11.6555 | -64.9991 | 2024-10-01 08:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3476dafc-4e43-34be-8d73-0b17ad4599f0 | -11.6743 | -64.9983 | 2024-10-01 08:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 2996693a-7224-3d2f-bf58-7316b9d1f916 | -13.0204 | -51.1884 | 2024-10-01 08:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| d350360c-f6f4-38cf-bdab-257853bc6229 | -16.1542 | -55.4194 | 2024-10-01 08:16:37 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 133d2791-85f8-36fa-b864-9f8228158c95 | -16.6316 | -57.2557 | 2024-10-01 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| cc7adb23-db5e-3180-9b35-7ed7c7e0d850 | -16.6319 | -57.2352 | 2024-10-01 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 3eee7e30-bd4f-340b-990e-4464a5eec932 | -16.6515 | -57.233 | 2024-10-01 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| 7e51ba31-7032-300f-ba25-cf9cdcb974b4 | -16.7079 | -57.3696 | 2024-10-01 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| b0139183-1b74-30f7-a6c1-b4550adfdb91 | -16.7275 | -57.3673 | 2024-10-01 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.5 |
| 9ed4c2a4-1c20-33dd-a3e1-47bb885d6706 | -16.8292 | -55.9152 | 2024-10-01 08:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 49.2 |
| 05472483-5749-3f23-8c8a-56aff11caf03 | -16.8488 | -55.9128 | 2024-10-01 08:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 30636e62-828a-3bc5-992c-139f61be4ecf | -16.898 | -57.7153 | 2024-10-01 08:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.2 |
| 43d16385-6eca-33bf-b370-8c4548bd2b00 | -16.8983 | -57.6949 | 2024-10-01 08:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.2 |
| cdaf49e5-0e92-3de4-9435-9e34af5a6709 | -17.0898 | -56.7297 | 2024-10-01 08:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| c34d618a-6279-3a72-b6ce-f742da515bee | -17.1574 | -56.2052 | 2024-10-01 08:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 0d1aae81-abaf-3d54-b63f-08c52bfe9406 | -17.1577 | -56.1844 | 2024-10-01 08:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 73.9 |
| 809f23e0-4df9-3511-aa8e-bddba24d438b | -17.1581 | -56.1637 | 2024-10-01 08:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.8 |
| 32f9ace6-88ce-38ee-aa75-82d5c130b574 | -17.1771 | -56.2027 | 2024-10-01 08:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 2ed4afa9-a694-3308-afce-f54a87cd774f | -18.6977 | -57.3123 | 2024-10-01 08:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 7723c7bf-5118-33fe-8f36-c37f18f78df2 | -18.6973 | -57.333 | 2024-10-01 08:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.4 |
| c44a36f7-81e9-3b11-84dd-d3d59720f4f2 | -21.5871 | -47.8591 | 2024-10-01 08:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 61.9 |
| b78eb4b6-c25d-3d37-8f80-19d8348fd93e | -22.3713 | -49.3011 | 2024-10-01 08:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.4 |
| 062711db-e2eb-39a9-8a49-8d606b5e406a | -22.3707 | -49.3244 | 2024-10-01 08:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 136.1 |
| 279d227c-ac55-3a8c-8bd4-152df0b61d90 | -22.3498 | -49.3293 | 2024-10-01 08:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.2 |
| a8f90196-4690-3d2a-a5a8-77ae149d7dda | -11.6743 | -64.9983 | 2024-10-01 08:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 56e63df8-e972-342c-952f-bbb907e6dcd0 | -11.6555 | -64.9991 | 2024-10-01 08:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 9a6f0e02-f42a-3e8b-8261-844cb8dd246e | -13.0009 | -51.2122 | 2024-10-01 08:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| a9aa7f4f-60c4-3643-a9f0-9c4c59aa975d | -13.0012 | -51.1908 | 2024-10-01 08:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| d94de9fe-e4dc-3509-b6a9-fc119e021be8 | -13.218 | -48.5797 | 2024-10-01 08:26:20 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| c036068a-58a4-3053-8beb-0a10313021f3 | -13.0204 | -51.1884 | 2024-10-01 08:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 9f4721cf-9df6-3661-b1c5-85b6fbfed6fc | -13.02 | -51.2098 | 2024-10-01 08:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 5970135d-11d0-3c92-996f-1c6398c3bad1 | -14.7596 | -48.769 | 2024-10-01 08:26:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 43.4 |
| ff93e707-69ab-3055-81c5-d20f17b839f4 | -16.1542 | -55.4194 | 2024-10-01 08:26:37 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 1016452d-0a89-3123-be2b-f5b2281f0fb1 | -16.7275 | -57.3673 | 2024-10-01 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.5 |
| 744e3692-8460-3c7d-97ef-ac170283df1f | -16.7079 | -57.3696 | 2024-10-01 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| c36fc5a6-c739-37d3-8d22-d085a5d1f05b | -16.6515 | -57.233 | 2024-10-01 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| f33f1619-9301-31ba-b83f-724cf3e6a6ce | -16.6319 | -57.2352 | 2024-10-01 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 12cbc258-c5af-39c0-9491-e5256469769f | -16.6316 | -57.2557 | 2024-10-01 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 38faf707-59b0-310d-8d12-44e86ad7c8e0 | -16.898 | -57.7153 | 2024-10-01 08:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.4 |
| 3b6bf971-7740-3282-9325-a3c4b3149505 | -16.8488 | -55.9128 | 2024-10-01 08:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 609e101b-b988-37bd-8bf6-25e9d485bb92 | -17.0898 | -56.7297 | 2024-10-01 08:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.8 |
| 7166a734-aa02-398a-a445-d1236d167131 | -17.1771 | -56.2027 | 2024-10-01 08:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 76d3e82e-8dec-3565-8264-813b19ddd21b | -17.1581 | -56.1637 | 2024-10-01 08:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| bf6a8b9d-ecd9-314f-8bca-7436f293bb64 | -17.1577 | -56.1844 | 2024-10-01 08:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| b6871ecd-fdc5-3075-8434-8dd46c972cd5 | -17.1574 | -56.2052 | 2024-10-01 08:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| bbf1cf9a-63f7-3fba-a37e-7d107459084c | -18.6011 | -53.0412 | 2024-10-01 08:26:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 5fc9cce9-3ddf-3b3c-a495-e065b82c74ec | -18.6973 | -57.333 | 2024-10-01 08:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.1 |
| cdf2ac0a-e22f-3118-92e7-c19625dfe74b | -11.6555 | -64.9991 | 2024-10-01 08:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| bbf8ea96-acad-36c0-ad2f-6fe0c3495361 | -11.6556 | -64.9802 | 2024-10-01 08:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.2 |
| d53e4a14-84ce-3744-a400-0bc0d555b2c4 | -13.0204 | -51.1884 | 2024-10-01 08:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 5afcb5f2-d190-3c2a-8018-a4c8e08f5de8 | -16.6316 | -57.2557 | 2024-10-01 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.1 |
| f6b396ce-7c97-32d4-955a-5f4f3a401c37 | -16.6319 | -57.2352 | 2024-10-01 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.2 |
| f52cc59e-eba9-3734-8ba7-836b0aa637cb | -16.6515 | -57.233 | 2024-10-01 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| f7e95db0-178b-3979-a52d-8f7921d4b398 | -16.7079 | -57.3696 | 2024-10-01 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 30e9c455-3255-328c-8bdd-641794bf80d2 | -16.8292 | -55.9152 | 2024-10-01 08:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 50.7 |
| dc1509ec-fcf8-34f8-aea6-c5449519f8d6 | -17.0898 | -56.7297 | 2024-10-01 08:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.8 |
| 7a78e10c-b876-3478-a312-94b51743b02e | -17.1574 | -56.2052 | 2024-10-01 08:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 9bf1975d-66d1-3a6d-b0ab-521465b4b9a0 | -17.1577 | -56.1844 | 2024-10-01 08:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.6 |
| d1545095-9f8c-37e0-a7f4-a3af89c79324 | -17.1581 | -56.1637 | 2024-10-01 08:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| a599b8ed-568a-379e-bb81-deeb6505d663 | -17.1767 | -56.2234 | 2024-10-01 08:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 646f7891-0cc0-335e-a741-539b09510f6e | -17.1771 | -56.2027 | 2024-10-01 08:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.5 |


[Clique aqui para ver as próximas entradas](README160.md)
