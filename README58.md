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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| adc327d5-e242-3d7d-aea0-e3e73799fb05 | -17.37143 | -52.91996 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d4a771f5-583a-35c3-8fc2-ed0d98798d8e | -19.86245 | -44.93486 | 2025-09-12 04:08:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59d74a42-ee12-3c61-bc25-f15192d193de | -19.70409 | -44.22691 | 2025-09-12 04:08:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 249a6efc-3e59-38d1-be4f-4e9b662478ab | -22.61149 | -47.28154 | 2025-09-12 04:08:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dd40af0-02bd-37b0-8d55-3271bd3d0036 | -23.11726 | -47.49141 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 64307b66-57c2-3e55-a7f2-9d23fbf81d56 | -19.10537 | -43.18005 | 2025-09-12 04:08:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5d6e8ec9-e463-3e44-bf32-3d967a2cca97 | -21.17226 | -45.10785 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 25008dbb-f3c9-3723-94b2-3fc369ccddf6 | -12.9292 | -54.7538 | 2025-09-12 04:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 1f281f95-4b2e-3cde-a43b-6b76601661f1 | -25.05455 | -51.89135 | 2025-09-12 04:10:00 | NPP-375D | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 3c64b0aa-87a6-3bc8-a9db-c939a00e9fed | -27.41144 | -48.94959 | 2025-09-12 04:10:00 | NPP-375D | MAJOR GERCINO | SANTA CATARINA | Brasil | 4210209 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 73a9b1ed-e657-3612-b468-d8f1740c5a76 | -27.68561 | -48.75241 | 2025-09-12 04:10:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| aea1ea83-3b72-3b22-b834-58b7ad303a13 | -27.41464 | -48.94752 | 2025-09-12 04:10:00 | NPP-375D | MAJOR GERCINO | SANTA CATARINA | Brasil | 4210209 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b8da1f2a-866a-349a-8a60-084020dc002a | -27.45628 | -48.45214 | 2025-09-12 04:10:00 | NPP-375D | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5a0a7241-59d5-3abd-baf9-edf1cd0c70f5 | -2.8368 | -48.84027 | 2025-09-12 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5626a651-c813-3f16-b65e-3c3264b0bf86 | -3.21869 | -47.12638 | 2025-09-12 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b402d733-2143-3096-82a4-6b9e7836eb1f | -3.25748 | -48.45286 | 2025-09-12 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bbd4af47-438f-34fb-91f2-247147141bf7 | -1.76162 | -54.84259 | 2025-09-12 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5903150-15e4-3519-bcc9-c81682eecded | -3.67637 | -47.48888 | 2025-09-12 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a43a4fdd-1527-3016-81e5-c0517814d0bf | -2.98497 | -49.29482 | 2025-09-12 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2bad352-8d71-3306-97e4-56d0e47b461f | -2.74376 | -48.69694 | 2025-09-12 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ac6164d6-828c-3ea9-bb4a-e80cbb46e97d | -3.48287 | -50.71305 | 2025-09-12 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b541235d-2710-3877-9e99-0034193d3543 | -2.63055 | -46.83192 | 2025-09-12 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 266b1ddd-6335-339b-868d-4f174b6c3fcb | -3.67295 | -47.48834 | 2025-09-12 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6126e041-20de-3ed8-b961-43e75bdef117 | -3.89736 | -40.9217 | 2025-09-12 04:23:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fc57f22f-f795-3c82-b574-61bd4d70ca2c | -1.97789 | -47.98344 | 2025-09-12 04:23:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da4b5164-4eda-3ce2-8b44-1236129a0380 | -3.42126 | -49.04717 | 2025-09-12 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f07a071-2832-3f04-8efa-6f183e01fcfd | -2.91436 | -48.63286 | 2025-09-12 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8eccfca3-217d-3df1-b796-71ca5826a63a | -3.31711 | -50.07884 | 2025-09-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c616c052-b317-3229-bda3-480093bb7a6e | -4.43844 | -38.4555 | 2025-09-12 04:23:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d79edd36-721d-320e-84e2-4cad9a58a2b1 | -3.83422 | -48.94761 | 2025-09-12 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53924d22-9619-3559-a5de-58ae2224260d | -2.4393 | -47.33173 | 2025-09-12 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73b4b9cd-efa2-30e5-b460-5bbfb3311f5b | -2.95115 | -51.66503 | 2025-09-12 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 514dfd8b-2f3a-3b0b-8f38-5c3245846b1b | -4.08262 | -48.04322 | 2025-09-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 863865b7-a52e-3007-9694-4d1435710089 | -3.11631 | -43.27269 | 2025-09-12 04:23:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cae85bbb-c52d-3b08-8a8d-dcdde26b7906 | -2.63111 | -46.82835 | 2025-09-12 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5a7d809-3924-3a9e-abdf-41b421a9effb | -3.2153 | -47.12585 | 2025-09-12 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46cf0122-651a-3a64-aaf7-7aab408d3555 | -1.36693 | -54.12754 | 2025-09-12 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 283033e1-db50-3d1e-afc2-3cb9f3f2e496 | -2.79697 | -43.77256 | 2025-09-12 04:23:00 | NOAA-20 | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a8a48766-ecf9-3d8d-8b80-cb070f027330 | -1.53394 | -47.56148 | 2025-09-12 04:23:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df6faa53-ce62-35dc-944f-632561d17002 | -2.43989 | -47.32801 | 2025-09-12 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 760658e8-56fe-3625-87a9-9254b6f87a34 | -3.1453 | -44.42999 | 2025-09-12 04:23:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d0a757a-d1dc-32a1-9752-5eb633cd8fd4 | -3.21811 | -47.12999 | 2025-09-12 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 585787f9-aed2-37ba-a243-1d6eb10f8993 | -3.21473 | -47.12945 | 2025-09-12 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f13848a8-1988-3631-a7cf-4c1b162b9825 | -1.53454 | -47.55763 | 2025-09-12 04:23:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 062cbc0d-d83d-3e34-8658-d77d0e6492a3 | -3.67978 | -47.48943 | 2025-09-12 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 57e7cefa-0b27-3d1d-a855-a88efe0c4d56 | -1.86149 | -47.98605 | 2025-09-12 04:23:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0415fbd3-62a4-392b-9dc3-7b66a1db03ad | -4.14497 | -46.14697 | 2025-09-12 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8cdb129f-4a71-31ed-b491-e8a71d0d4866 | -3.32101 | -50.07948 | 2025-09-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9fcfe06-4e5e-35bf-8f70-9be6b5ad71b0 | -2.76924 | -48.3548 | 2025-09-12 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f652c5f-15a0-3372-a1a0-0c8238effb09 | -3.14195 | -44.42947 | 2025-09-12 04:23:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8f91e2d-c470-365d-bacb-079d2e4be990 | -3.26662 | -50.02036 | 2025-09-12 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 427d1e78-c128-3829-ba0c-80cd701b33cf | -2.82225 | -47.43613 | 2025-09-12 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8355e98-0671-3e5b-9768-673fc6eaa1fb | -2.62604 | -46.83856 | 2025-09-12 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f954e319-9895-3f07-982f-053bea919d09 | -3.83355 | -48.95182 | 2025-09-12 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ccb9eee-6582-33e1-8dfd-0c739b83b9f3 | -3.6931 | -49.10483 | 2025-09-12 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46566088-817d-36d6-a682-f10b568aa6ef | -1.68797 | -48.05456 | 2025-09-12 04:23:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b9c7f27-f28e-33f7-af55-f1bf085321fc | -3.67519 | -47.4962 | 2025-09-12 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aa44376e-c3b5-3ccb-845d-e7a38b4344ee | -2.07666 | -47.14386 | 2025-09-12 04:23:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a20f914-a135-3183-93f6-a7ceaad85558 | -3.35099 | -49.81695 | 2025-09-12 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6408883e-50ca-392b-879c-2c503c0e1adb | -3.72118 | -50.94089 | 2025-09-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 734f1d03-fecd-3b8e-8292-4159b8522178 | -3.41431 | -52.82848 | 2025-09-12 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 715d0793-596e-38ef-8f68-b489fa0c52b4 | -3.72177 | -50.9372 | 2025-09-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aabab3b7-ddca-33bb-a09f-8fa6d2b47f46 | -3.89575 | -40.92379 | 2025-09-12 04:23:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f001a1ee-bf66-3037-a23c-e80c60637932 | -2.62267 | -46.83803 | 2025-09-12 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8dd77688-167e-3c30-ac0b-a553dc707423 | -3.69221 | -49.57446 | 2025-09-12 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f54f932-118d-3d79-bc2a-a428820ffb8c | -3.69378 | -49.10055 | 2025-09-12 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d13572c1-270f-3cf2-80ca-00e88361b806 | -3.12335 | -48.09068 | 2025-09-12 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09b6d9da-a827-38ec-b00e-9cdb3627a612 | -5.07515 | -41.15378 | 2025-09-12 04:23:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7d23cda3-1dce-32c2-bcf6-3dde362501d8 | -2.98871 | -49.29543 | 2025-09-12 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1ec7a2d2-2a22-371d-940a-5b61905b5385 | -1.97852 | -47.97946 | 2025-09-12 04:23:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4381a59e-62ac-3651-8c94-c12c97776991 | -3.41247 | -52.82649 | 2025-09-12 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 470afbdf-b18f-32f8-91a3-92d1fd78fbac | -4.34851 | -47.47373 | 2025-09-12 04:23:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d6d4f30-6a8f-3301-84eb-7ce5b8d778f8 | -3.25976 | -48.46155 | 2025-09-12 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1fd98310-3858-3ae8-bf3a-c5f30deea2a8 | -3.68845 | -49.57382 | 2025-09-12 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| efc68752-16d9-3dff-9948-a10dbd2ffdff | -4.04219 | -49.07635 | 2025-09-12 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 187d74d5-5c5a-3fc1-8f68-36e0b56ba786 | -2.35447 | -48.41483 | 2025-09-12 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| affc24fe-bde7-380a-86ff-6c4135f18426 | -3.48228 | -50.71663 | 2025-09-12 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb39dcce-ffed-3c9a-972a-5c275eae3383 | -3.2215 | -47.13052 | 2025-09-12 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 9011a837-17b1-3356-ad77-78cdf79d633f | -2.98875 | -52.62789 | 2025-09-12 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01efbf58-2ea2-3331-8436-f93f910f3eaf | -3.60027 | -51.52942 | 2025-09-12 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2e5fb733-6349-3d0f-ac92-207ed424a520 | -3.49293 | -49.04564 | 2025-09-12 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71349ec2-30e8-3738-a47e-8bae7979a5f8 | -2.91944 | -48.63265 | 2025-09-12 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 033de705-7daf-3285-b12b-f0a9be017ddb | -5.08309 | -41.15515 | 2025-09-12 04:23:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f0f4ca12-38ee-312f-95cd-c8ec3c3f95a7 | -2.92698 | -40.41713 | 2025-09-12 04:23:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 91297e07-c635-3076-b4d6-3d79d72f0f7f | -2.07325 | -47.14331 | 2025-09-12 04:23:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cdb3d7c-5aa6-37b1-aaab-04d4d2e18696 | -3.94511 | -49.40008 | 2025-09-12 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e25d635-1fbd-36dd-a7a0-e46f70304840 | -2.72932 | -48.38247 | 2025-09-12 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c747129a-9269-39e6-b40b-4c8134a7277b | -3.25684 | -48.4569 | 2025-09-12 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2a6620ba-0292-3a2a-8f33-5cb9652f47e9 | -3.68577 | -49.10366 | 2025-09-12 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3235b48-4889-3434-88a9-d5da9e69e83e | -2.91584 | -48.63207 | 2025-09-12 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b9aefbd-fa7d-3f8d-b65c-c158779280d3 | -2.91797 | -48.63343 | 2025-09-12 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f84d0346-2e65-3be6-89f8-61f06b7b46df | -3.44909 | -51.62949 | 2025-09-12 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 501717b6-672d-3451-867f-23c0a135d522 | -3.82992 | -48.95122 | 2025-09-12 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d125fd10-4530-3c99-88f8-02d8feba06ce | -3.21754 | -47.13361 | 2025-09-12 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| a77e358d-3bf5-3b32-bbaa-e267ea9d75b8 | -3.2604 | -48.45749 | 2025-09-12 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7860b3ac-f982-33d0-85b2-ee2e2a433480 | -3.22207 | -47.12691 | 2025-09-12 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 800f5e4d-9868-3c4a-a9e8-c67fcc2727a8 | -4.04182 | -49.07805 | 2025-09-12 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e516ae29-ad33-3420-a5bf-dff96ccd04fd | -3.68943 | -49.10425 | 2025-09-12 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96931342-8d64-386f-a90a-320c9d567ebe | -11.67876 | -46.58605 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd35dc25-1eb2-3ecb-be22-b88735f2000b | -11.51892 | -50.39615 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README59.md)
