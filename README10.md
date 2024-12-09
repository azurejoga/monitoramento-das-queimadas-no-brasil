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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42528f41-e449-3a8b-b9ec-9d623946a3e7 | -6.88498 | -47.24084 | 2024-12-09 04:18:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d77d88bf-31b8-3dae-864e-058c61fb9d23 | -6.97077 | -34.92529 | 2024-12-09 04:18:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 3e423c1d-f728-350f-b4e5-c8b9d382098c | -7.59778 | -46.62986 | 2024-12-09 04:18:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f376dbc9-9169-36b3-87e4-869c5e3e9514 | -8.09214 | -46.03584 | 2024-12-09 04:18:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ca37863-60f8-3790-ba8c-7c2039e0814d | -8.7784 | -48.06709 | 2024-12-09 04:18:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86c5b2d4-882b-320e-977b-ad59bc38fe48 | -5.33022 | -45.43642 | 2024-12-09 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05fab7b2-0e24-3a1f-aeaa-add2761c184f | -5.73271 | -44.37343 | 2024-12-09 04:18:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18f394c6-d3db-3932-8d75-bfb43a587e1b | -6.09074 | -45.67725 | 2024-12-09 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b8571b67-8cf3-3590-8972-4617c1e0f017 | -7.74453 | -35.26638 | 2024-12-09 04:18:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b9cee51a-8299-3c3d-bd5a-684165e593dc | -10.40024 | -47.30099 | 2024-12-09 04:18:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28340400-26b7-3158-b82c-96892b31d6ae | -7.5228 | -39.26596 | 2024-12-09 04:18:00 | NOAA-20 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d56d017a-28cd-3aaf-b695-ba240dfbd0fd | -6.30735 | -47.29392 | 2024-12-09 04:18:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 946faceb-6497-3992-aef6-cc08d312da7c | -7.75057 | -35.26774 | 2024-12-09 04:18:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 22ec17fb-6ea4-3871-a856-db3bac58e31d | -7.80652 | -46.22553 | 2024-12-09 04:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a764f8bd-544a-3c2a-88ce-642b6e81ed59 | -6.9637 | -34.919 | 2024-12-09 04:20:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 136.1 |
| 57774b3c-a80f-33b1-a985-bd3feff7d2ab | -6.9828 | -34.9165 | 2024-12-09 04:20:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 84.6 |
| 2eb1fe4b-bf70-39fd-9674-0f2ca03ad501 | -12.28229 | -45.50401 | 2024-12-09 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26fb0b7f-8eab-39a4-997a-ccfc90243c84 | -13.06901 | -48.32883 | 2024-12-09 04:21:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6dd95b7-eec0-39a2-9873-80c0108c64d5 | -10.42761 | -51.82779 | 2024-12-09 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 675a9494-59fe-3fdd-9ac9-cff0f5cc98ce | -10.91711 | -48.93343 | 2024-12-09 04:21:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 268f3bd0-06e4-3abe-8d04-c08a33a7a9f8 | -10.83642 | -56.62751 | 2024-12-09 04:21:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0f65d11-c04a-36bb-a7b0-1f31d391e926 | -14.73626 | -51.38552 | 2024-12-09 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26d9dfcb-7131-3389-bd8e-da9654b1a661 | -14.19948 | -44.72012 | 2024-12-09 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c43d7a80-6eab-3c7b-9ffc-84d94e034b30 | -12.78625 | -54.22557 | 2024-12-09 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 04dbdeb3-1f0c-3795-ba9a-92194a6b0339 | -12.40591 | -49.67981 | 2024-12-09 04:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fda34be5-c666-38f2-b7c8-12a566ac999c | -11.20386 | -53.82114 | 2024-12-09 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d88e26a-a957-3442-b1b2-69544dcacd7f | -18.09786 | -47.34468 | 2024-12-09 04:21:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8618dd0c-8328-353b-ae85-0c5de622b8f3 | -12.36402 | -45.93606 | 2024-12-09 04:21:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23e3cc11-7c17-3c18-8179-b96c5348d47b | -11.20778 | -53.82763 | 2024-12-09 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6471bf4-0562-3156-96e4-f43607298271 | -12.78428 | -54.22909 | 2024-12-09 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38ef0a1b-610d-35f8-8e74-12b4c43d75ad | -10.41615 | -51.89174 | 2024-12-09 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b52821de-1014-30b9-b2f9-7028661764ed | -18.67078 | -42.83025 | 2024-12-09 04:21:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 567ed50b-b1b9-3bf5-8509-155725d225af | -11.89104 | -46.93963 | 2024-12-09 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1ce3676-efda-3d43-bcc5-1345e06fd45a | -14.97513 | -44.42006 | 2024-12-09 04:21:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6484209-31be-340e-8042-15c72e676f4d | -15.97459 | -42.24986 | 2024-12-09 04:21:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0e400d05-8c9f-3a50-a420-c47ffccee101 | -18.67132 | -44.59591 | 2024-12-09 04:21:00 | NOAA-20 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 330b7993-71fe-3f05-8790-c938d45e5b8d | -17.46445 | -47.01126 | 2024-12-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3292945-b4a2-33c2-8aa6-c232d1fb905d | -14.9757 | -44.41621 | 2024-12-09 04:21:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0468d7e8-3146-33be-945a-729876f3a64f | -10.92075 | -48.93405 | 2024-12-09 04:21:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8aa7058c-771d-3c40-a938-0903297fcca3 | -14.97972 | -44.41289 | 2024-12-09 04:21:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55d74a22-94ff-32c7-b167-f9b925bb768a | -10.42838 | -51.82352 | 2024-12-09 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8b98542-5082-3cdb-8580-67f87f3a7f90 | -13.26672 | -51.1045 | 2024-12-09 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50ea8d14-5916-332f-a7f0-e19edc84040f | -12.86698 | -43.73598 | 2024-12-09 04:21:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6ebe8af-66cd-31a7-8a16-e51562bb1442 | -16.54676 | -52.45833 | 2024-12-09 04:21:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff78bd32-4eae-3ff8-8da5-8a67b966edc0 | -10.83554 | -56.632 | 2024-12-09 04:21:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dbec370e-4843-350c-88c6-97eb14bdff5e | -12.79026 | -54.22435 | 2024-12-09 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9d49c38-8f27-3b1a-8ca2-8edb2f7beb42 | -13.25747 | -51.08732 | 2024-12-09 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d151da2c-76c0-30c2-beab-73809cc0b751 | -15.9753 | -57.17837 | 2024-12-09 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 93e83919-9e24-3f2f-b025-e1a14e6a5301 | -17.46388 | -47.01487 | 2024-12-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdac7bdc-43b4-3532-876b-20f55cb173a4 | -15.08009 | -48.94412 | 2024-12-09 04:21:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fab73aa-f364-39b1-b5f6-ea1721f23f1e | -14.97628 | -44.41235 | 2024-12-09 04:21:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3d03fd4-8b18-3bc1-bc25-afc78e52c4b1 | -17.46113 | -47.01069 | 2024-12-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06100378-4aa1-38b2-b0ae-5c0cb6eaa475 | -10.42054 | -51.89257 | 2024-12-09 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60d736f6-ceaf-399a-989c-d4a373e1f599 | -15.186 | -43.75196 | 2024-12-09 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| df1331dd-4762-3114-a070-d2f7f5a18f1c | -15.87608 | -51.14941 | 2024-12-09 04:21:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c94cac5b-3ca1-3b5d-84fc-786dfc7bf486 | -10.91638 | -48.93771 | 2024-12-09 04:21:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ca1e1826-403d-38a6-9bd7-66cb4ce9633e | -13.27071 | -51.10524 | 2024-12-09 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8bf97ac4-0b36-38e4-8855-ba40bdebb4c7 | -12.404 | -49.6817 | 2024-12-09 04:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e980bac-d5df-3c4f-87a9-d4769c64c08d | -15.83798 | -45.1713 | 2024-12-09 04:21:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9602dbdd-9d8f-342e-81b9-0ddd0e94647f | -18.3048 | -47.19408 | 2024-12-09 04:21:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 884ba4ce-b099-383f-883b-543e0676d716 | -19.37036 | -43.74582 | 2024-12-09 04:21:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 71e6f793-f0b5-3fc5-9463-103637d87a9b | -13.26735 | -51.10097 | 2024-12-09 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 441bfed6-9b5e-37f0-bd29-2fa0fa1fda3b | -16.20811 | -48.21586 | 2024-12-09 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc99b127-8849-3a57-a2ca-5921a8c98ffa | -10.38238 | -52.00341 | 2024-12-09 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6b377ba9-e5c6-323f-aa98-f114ca337e26 | -12.78533 | -54.2234 | 2024-12-09 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19a53997-eaac-3c16-8d2a-6ee0edbae9aa | -10.83466 | -56.63649 | 2024-12-09 04:21:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72880476-ff28-3312-832a-d28f9f2b2309 | -11.90786 | -44.39055 | 2024-12-09 04:21:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 19771a49-129f-3849-a215-dfeab05edf19 | -15.07661 | -48.94352 | 2024-12-09 04:21:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bd38255-9370-3b9e-92e6-7ba456b9a7e2 | -12.2856 | -45.50454 | 2024-12-09 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c486e95f-b224-3566-b125-bbab10490bce | -17.67628 | -42.74473 | 2024-12-09 04:21:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28401c59-2126-344e-8f5d-8cfee5802dde | -12.40476 | -49.67717 | 2024-12-09 04:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5f0ec04-6a1a-38db-b224-bbc4f9fb9da6 | -12.78921 | -54.23006 | 2024-12-09 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0992d2b3-ab63-3da5-a2ce-1dc0395b4004 | -10.424 | -51.82272 | 2024-12-09 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11734f78-4d8c-3864-b78f-eaa9a50a1559 | -18.08004 | -45.28694 | 2024-12-09 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13f1844c-3882-301b-9553-10ed526b1987 | -12.68503 | -46.75746 | 2024-12-09 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eebaefc8-a19a-3a2a-bf36-291c5a324079 | -12.27953 | -45.49996 | 2024-12-09 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6bf3c09f-859f-3717-9c9c-5e9e3a1a824f | -12.68113 | -46.76046 | 2024-12-09 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb4a35ad-811a-31ab-a428-62bbc1428454 | -12.28339 | -45.49696 | 2024-12-09 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| adb18e8e-5e52-39d8-83aa-d306ed2c408e | -12.40219 | -49.67916 | 2024-12-09 04:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61736653-93f7-3908-9bfc-b0a074d259f4 | -17.46606 | -47.02265 | 2024-12-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7b296f92-54e6-38b4-bc53-84eaa5281e8d | -17.77959 | -42.80782 | 2024-12-09 04:21:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa29a6d9-9fa3-3631-bb4a-a983f3c27ffd | -15.80054 | -48.15342 | 2024-12-09 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8b26662d-13b1-30e7-a518-b744650c4ac9 | -17.14921 | -43.2175 | 2024-12-09 04:21:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62d71a0e-f1ff-30be-8a81-f2399dd10e2f | -15.98251 | -57.1718 | 2024-12-09 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 349a6e10-b341-3c72-a053-3ae66e780be4 | -15.97871 | -57.17582 | 2024-12-09 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41b52933-1d69-3d3d-b9c2-1e17f0a3e8f1 | -12.36731 | -45.93655 | 2024-12-09 04:21:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d698fb6b-7f1c-3981-8fa3-ea549ad816a7 | -16.54266 | -52.45753 | 2024-12-09 04:21:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2294f08-4ce1-3974-9de9-6e8f1433d030 | -12.78414 | -51.5098 | 2024-12-09 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9650fedc-cb54-37cf-a0a5-60b20f17857b | -15.97954 | -57.17192 | 2024-12-09 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ffab90d-2e5c-3bb0-97fa-a1fde8b5a014 | -15.97611 | -57.17444 | 2024-12-09 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3ecc9219-4a0a-321b-a7aa-1f7dda3ecd89 | -12.28284 | -45.50049 | 2024-12-09 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b54d29e-eb92-3989-80d4-561955ab3c11 | -15.56936 | -47.85604 | 2024-12-09 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f54a8c97-e646-3d52-a42c-b516929ecf8d | -12.68445 | -46.76102 | 2024-12-09 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 020e74d6-9326-3e33-b56e-ff7163f687b0 | -10.82958 | -56.63087 | 2024-12-09 04:21:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2166fc4a-ead0-307f-84ee-204ff9d162a6 | -15.97692 | -57.17051 | 2024-12-09 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84476c00-cb8f-39e2-ba14-d201e6380402 | -11.49969 | -54.28166 | 2024-12-09 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2fdae72-a190-3ded-ae68-776551aa398d | -16.34823 | -43.69569 | 2024-12-09 04:21:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 240f5eea-29ad-3f0b-984d-267b3cb90e2e | -11.88231 | -54.6895 | 2024-12-09 04:21:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99532051-e23e-306a-91a9-bb1cdf95ae40 | -15.98514 | -57.17318 | 2024-12-09 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f9e757b-d246-32c9-a190-3c5f5e54dfe2 | -17.46663 | -47.01904 | 2024-12-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README11.md)
