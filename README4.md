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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b8ab3fb-8d22-37c2-81c4-c0594034457a | -14.90006 | -52.45398 | 2025-10-25 00:33:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 57951dda-2c98-388e-b1ca-3b4a9b18456b | -18.1811 | -51.76363 | 2025-10-25 00:33:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d9f18b00-9a95-3423-832c-6846e5c4776a | -10.41564 | -48.05032 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55f49710-2785-3195-9253-cfe74890b6a1 | -10.93315 | -50.4064 | 2025-10-25 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 4fc280c5-5823-3755-97fa-6efb9ba3c0f9 | -11.57945 | -49.53727 | 2025-10-25 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e40713c7-41d2-3300-b97f-0d5bf44fe316 | -17.2937 | -47.16055 | 2025-10-25 00:33:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ced49261-baf3-3d2e-a31a-548b7774071b | -17.3819 | -46.16472 | 2025-10-25 00:33:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 73974b4e-bc9f-3ee0-8a12-6e89082c1ac1 | -13.30725 | -47.44941 | 2025-10-25 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5f951cc7-ecea-3486-b61d-249530e1cc89 | -15.22661 | -47.93207 | 2025-10-25 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 193a04eb-4aff-3f9c-8f31-fff837175eaa | -14.36071 | -51.8064 | 2025-10-25 00:33:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 393970d0-ba6d-3e13-883a-2efecfcb7881 | -14.18335 | -47.32124 | 2025-10-25 00:33:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cf18baae-1d23-32a1-8d06-9349e90f2e13 | -12.22973 | -43.31752 | 2025-10-25 00:33:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ba03e622-16f0-3a40-a9e0-13dc096a4495 | -12.38118 | -49.9508 | 2025-10-25 00:33:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e992159c-1875-3a0e-b712-e032d2db8217 | -15.44503 | -48.57735 | 2025-10-25 00:33:00 | TERRA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 64cb2158-8eca-3cde-8864-32e43e794ba6 | -10.60951 | -47.85928 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8aa745ae-41fb-3e25-8866-a24042073e7f | -10.74513 | -47.90245 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cb38bc99-71a3-32b2-bac5-a9d80d762843 | -14.38603 | -51.52465 | 2025-10-25 00:33:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 65a95b8d-5cd8-32e7-acd5-33c27ddb9c77 | -10.56384 | -47.98813 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f6fe8569-9a12-3ee1-b605-a58f70548b0b | -11.13081 | -48.35537 | 2025-10-25 00:33:00 | TERRA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 20aae2e2-3e72-3af9-b2b9-c145942dfb66 | -11.00601 | -49.85119 | 2025-10-25 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 21a9b807-1b38-394c-af1b-467c35fe66bf | -10.90997 | -47.89347 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3d8792d-da98-3d84-a037-62ca36a9ec23 | -10.25063 | -47.99329 | 2025-10-25 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 1ef19e76-356b-36f2-9949-4c5314470226 | -15.19554 | -44.07778 | 2025-10-25 00:33:00 | TERRA_M-M | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 95e8a7da-f5ec-32a5-a08f-8465fb901d65 | -4.82722 | -50.93745 | 2025-10-25 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c6a3d371-4544-30fa-be3e-196e44562787 | -6.41784 | -46.19199 | 2025-10-25 00:35:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| b7d81ced-b7e2-3d4c-a5c8-82dce8b324ba | -4.961 | -47.59422 | 2025-10-25 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 77472838-b910-365e-b8d9-dbec09f71cb4 | -3.92263 | -47.69296 | 2025-10-25 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| ac6a6293-1435-3471-9bcf-f9d3f2e2d3fc | -6.24445 | -46.39661 | 2025-10-25 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 95ae5141-27e4-3c7e-93ec-45f506982e20 | -8.72365 | -48.01416 | 2025-10-25 00:35:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8b8dc9a5-8886-36a9-ae11-69331bf416f2 | -4.87376 | -47.53148 | 2025-10-25 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 32dd667d-48fc-35c6-8898-c9ce07550938 | -3.91299 | -47.69434 | 2025-10-25 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6d5ee9da-902e-3192-b0a7-073e4f5dd1d0 | -4.70539 | -46.42989 | 2025-10-25 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6fb0cfd6-6545-3181-97ba-12f62c73f34c | -4.22798 | -48.61696 | 2025-10-25 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 290ce862-8937-329d-b723-63ca404be104 | -3.98598 | -50.52367 | 2025-10-25 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| ab0ba6a1-c9b6-3b78-821e-637506fab04e | -3.01737 | -45.39139 | 2025-10-25 00:35:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| fd23f736-d2ce-3b8b-9659-bbf89057b9db | -6.54118 | -51.96116 | 2025-10-25 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 259960f2-07db-3c50-b070-b3c4ec866d3a | -6.8641 | -50.74784 | 2025-10-25 00:35:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 97dbb520-3875-3137-961b-ed3d2bcd5a78 | -4.87531 | -47.54212 | 2025-10-25 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 35708ee7-9861-3ebc-9372-b144c31f7d64 | -7.99471 | -49.25211 | 2025-10-25 00:35:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b689cf95-855e-3b3a-bc97-f2cd44589b77 | -6.88853 | -43.61736 | 2025-10-25 00:35:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 53ee61a1-b7da-3221-b850-c23791cc706b | -9.95719 | -48.26055 | 2025-10-25 00:35:00 | TERRA_M-M | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2e2cc5bd-30c6-3aab-9d99-58fbe616bbf3 | -5.11063 | -48.66623 | 2025-10-25 00:35:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| f9767916-8ef3-35dd-870d-225458dbec11 | -7.03318 | -49.30334 | 2025-10-25 00:35:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c224d734-607a-3b79-badd-bd4933d5a2cb | -4.70492 | -46.44941 | 2025-10-25 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 2c626fc4-7282-3c2c-b13c-4afc5f8f4660 | -4.87254 | -48.41413 | 2025-10-25 00:35:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 01926f48-f300-3c06-a62c-6de05445959a | -4.5578 | -46.6887 | 2025-10-25 00:35:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 33.7 |
| b0f5decf-b97f-3d51-b870-dd1eaba05f75 | -6.79577 | -46.45887 | 2025-10-25 00:35:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| acfe0a64-2a26-3379-a7fb-3a9e325f8430 | -6.65095 | -43.61487 | 2025-10-25 00:35:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c6df7c5f-87c8-37ea-b879-3a4d0a186d5c | -4.61994 | -50.50882 | 2025-10-25 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 848f0098-5da7-34e7-ba5d-c7ff3e75f5c4 | -5.70719 | -49.3059 | 2025-10-25 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 42ae8d1c-7168-3b08-abdb-255fddd59e2b | -4.28968 | -48.26743 | 2025-10-25 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 5dcb22f4-81bc-3946-a2e7-a7fecc344a80 | -6.97432 | -46.41978 | 2025-10-25 00:35:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 71dfb00b-2bc8-35af-989a-3d11b3a6929c | -5.64899 | -45.98247 | 2025-10-25 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2dee145e-760a-32d5-ab94-f31aae98d567 | -5.45757 | -45.40914 | 2025-10-25 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 6ad99075-e045-384e-84e3-1158caae1838 | -8.31558 | -47.86487 | 2025-10-25 00:35:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| f32fbff8-af19-3929-bdfd-500c1ba684e6 | -6.91955 | -45.17271 | 2025-10-25 00:35:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d6fcd072-3abd-37e4-8dc5-831f288247d2 | -4.90474 | -48.97206 | 2025-10-25 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a2f609e9-9cce-382f-8370-a78cadb7c01c | -8.28079 | -46.87106 | 2025-10-25 00:35:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ffd2d052-afbc-3477-a24d-a9daf59cca2e | -9.57313 | -49.68139 | 2025-10-25 00:35:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| c5359333-eff6-3b05-b85e-efa517536078 | -7.79517 | -45.40371 | 2025-10-25 00:35:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 4cdee5e7-6117-3170-b5eb-e6cf4dd3ffbd | -5.33137 | -44.70742 | 2025-10-25 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4bc4c309-a74f-38ea-977e-1d099fd38264 | -6.71205 | -44.63534 | 2025-10-25 00:35:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 54fbb458-5fca-3464-aef0-add1a3352848 | -3.9872 | -50.53247 | 2025-10-25 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 80aaf283-e663-3137-b6c3-3c0b6adc6a91 | -8.57278 | -48.51415 | 2025-10-25 00:35:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4d3897af-a4f0-303e-b14c-2d7914839efb | -5.37467 | -40.72167 | 2025-10-25 00:35:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 2136e1b0-3d9f-3310-bff7-2ee7da8b0d73 | -5.02351 | -47.15573 | 2025-10-25 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 5f0608c2-b422-3c4c-80e5-ec74fc956980 | -5.47721 | -50.1745 | 2025-10-25 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b8c81786-7049-3eb7-a6cd-0aa4e023e573 | -4.83487 | -50.92725 | 2025-10-25 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f445cbc9-e920-30c3-a4da-4b24feac977b | -9.09111 | -47.81113 | 2025-10-25 00:35:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d45bfa49-d281-3058-be14-af74129fd353 | -8.56387 | -48.51544 | 2025-10-25 00:35:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5e328874-047f-3d0a-a084-3cb6a1a7b2d8 | -6.96277 | -43.5024 | 2025-10-25 00:35:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| ee775a23-a097-3544-a615-53dccef2026f | -7.56511 | -47.11831 | 2025-10-25 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 1605e223-b54d-3821-a4e9-770e73e04e16 | -9.28488 | -57.55657 | 2025-10-25 00:35:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 792dd88c-2e9c-3f5e-8a99-7c97b3b966be | -6.02239 | -48.13835 | 2025-10-25 00:35:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 04086654-9ac2-3610-bf38-7cf3df06fe0c | -4.60474 | -49.59057 | 2025-10-25 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e1cbb2a5-0a4f-3749-a111-e4da1d6b599f | -5.64704 | -45.96951 | 2025-10-25 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| aa581950-961a-35ff-9383-6e521dcecd9f | -6.91746 | -45.15901 | 2025-10-25 00:35:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 295e21fe-62c4-37ec-b656-e49a305cce34 | -6.59837 | -44.32674 | 2025-10-25 00:35:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b5470532-370c-3fc8-882e-add9a7c03bbb | -4.09809 | -51.06084 | 2025-10-25 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3c31b36c-13cf-3b30-9509-1c8443838a61 | -9.28414 | -57.55144 | 2025-10-25 00:35:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| ae61d4d9-4e17-34a3-ab85-8564df8610aa | -4.27215 | -50.51287 | 2025-10-25 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| ad8118d4-0f85-32e5-b65c-413c4aad363c | -6.91651 | -45.16474 | 2025-10-25 00:35:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 539877b0-0ba3-3890-aaab-b0ddccb49961 | -5.14617 | -43.72819 | 2025-10-25 00:35:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| c4d4cedf-8540-3c6e-8cf6-541ca0389ccd | -6.41919 | -46.18558 | 2025-10-25 00:35:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 15cf7dc9-cd8a-3d98-a15d-12dd028a80ca | -8.30948 | -48.6078 | 2025-10-25 00:35:00 | TERRA_M-M | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 696fd3cf-a51f-3041-8254-95f1e9cf1092 | -9.32868 | -45.18395 | 2025-10-25 00:35:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 362bb86c-62c1-3274-8375-7b455da1a90d | -9.18132 | -48.8476 | 2025-10-25 00:35:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ea62d286-22e8-385a-abe8-e5bd4050420d | -4.71347 | -46.43561 | 2025-10-25 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2e7d8eb2-5e90-30a4-82b9-a73c9a42d6d2 | -6.01455 | -48.14927 | 2025-10-25 00:35:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7cc10aa1-7b99-3af1-b9ed-5d4ed3f5c9a7 | -6.55576 | -43.24918 | 2025-10-25 00:35:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 6a683ff7-320a-3988-b538-10b99ccf058d | -6.32253 | -49.15688 | 2025-10-25 00:35:00 | TERRA_M-M | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b8c488df-660b-3280-9817-1c77e56fbf6d | -8.12016 | -55.08673 | 2025-10-25 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 1fc24a40-adf1-36c8-a23d-eada19f47ff3 | -9.32014 | -45.19865 | 2025-10-25 00:35:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 525b1660-e0b5-34c5-97bd-9bbe83fa8291 | -5.64239 | -45.97651 | 2025-10-25 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 36e72097-ccf0-3e8e-869b-d332a9714d35 | -4.88538 | -46.05856 | 2025-10-25 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 92a329a0-a715-3e68-a039-23c8a4614243 | -9.4543 | -49.75036 | 2025-10-25 00:35:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ba84c1b5-e672-3e2c-9e2f-1b04ab4668fe | -8.00879 | -46.70064 | 2025-10-25 00:35:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 72fa3309-3254-38db-bbb7-112ffece162c | -9.32165 | -46.98489 | 2025-10-25 00:35:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| ff793daa-5828-3ffe-b098-d4bc6b0da739 | -4.20195 | -48.36568 | 2025-10-25 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 06bc1722-2b4f-36f7-953b-0ecbb0c43088 | -8.71535 | -49.60407 | 2025-10-25 00:35:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |


[Clique aqui para ver as próximas entradas](README5.md)
