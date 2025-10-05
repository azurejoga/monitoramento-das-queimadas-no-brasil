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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dbd845d-ca0f-3685-99d6-13f2965f5008 | -6.40335 | -43.0397 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| f9b219a1-aa03-3ab3-aec8-8503ec1235f7 | -7.15697 | -46.09089 | 2025-10-05 00:35:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 00caaf82-1180-31d8-8065-784ecb80e183 | -8.84623 | -49.95483 | 2025-10-05 00:35:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 28b4a684-2867-34c6-abf8-fdee8109cf20 | -7.69765 | -46.22747 | 2025-10-05 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 14d3d585-47a7-38f6-9afb-93d953c70544 | -6.25325 | -45.37629 | 2025-10-05 00:35:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 6064e682-ea95-35ef-9ef0-43f1877d5fbc | -8.74432 | -49.0796 | 2025-10-05 00:35:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d50fdb59-b15e-361f-8d42-a715afea4d46 | -7.7816 | -42.60317 | 2025-10-05 00:35:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 5383a984-e9d8-35fd-ae37-b51085452660 | -4.43725 | -43.22927 | 2025-10-05 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 0115ced0-6732-395d-a71d-1215790fee48 | -7.73355 | -46.3151 | 2025-10-05 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 8d64aa68-a9ed-3c2b-b325-c7a366cdbc32 | -3.60501 | -51.03931 | 2025-10-05 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| df55d85a-9e72-3cfe-8d89-21e29ab9b812 | -5.17759 | -46.21539 | 2025-10-05 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0537fae6-49de-32aa-af73-1be5e06b910d | -7.28752 | -39.26253 | 2025-10-05 00:35:00 | TERRA_M-M | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 46.2 |
| 5da4559e-c174-327a-af05-119388be26c6 | -4.70803 | -44.96321 | 2025-10-05 00:35:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 3bd9a1c6-9798-3a2c-86c9-e95ef6a47615 | -2.29766 | -48.00068 | 2025-10-05 00:35:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7ff1aeba-ca9e-37f3-bf11-195702b5b2c7 | -6.8714 | -47.23095 | 2025-10-05 00:35:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9ab740e0-c4e3-3ef6-9283-b1077873d5c3 | -7.02695 | -50.73306 | 2025-10-05 00:35:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7d036589-2f3c-393e-a754-5910045ea3bf | -6.43942 | -44.14643 | 2025-10-05 00:35:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| e68729db-98b5-3aa0-9e23-886bbf8fb81b | -7.0679 | -49.95028 | 2025-10-05 00:35:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4583a4c1-6d2b-3066-bf14-6e9df1cbd044 | -5.95268 | -43.52202 | 2025-10-05 00:35:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ad32c3d3-3d9b-3add-b165-e13516055aba | -7.05903 | -49.9515 | 2025-10-05 00:35:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| cbe8e932-598a-32cf-9cdd-af8570844ce7 | -5.84131 | -44.45513 | 2025-10-05 00:35:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 081629bb-9731-3788-bc0d-3ad87b7dd77a | -2.68457 | -48.39684 | 2025-10-05 00:35:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| ef231fcb-d6f4-3b21-ae40-a1abc8e31d93 | -7.79133 | -42.58131 | 2025-10-05 00:35:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 34e4fbb6-542d-32f9-a552-57c182757921 | -6.38468 | -44.62487 | 2025-10-05 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 932ea0c9-e1c9-3441-a373-f2d57986c453 | -6.87281 | -47.24077 | 2025-10-05 00:35:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 483b7673-f75a-3eb6-9a0e-8d0ab1025471 | -6.1573 | -44.64804 | 2025-10-05 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 2132f015-ccc8-3a96-9c4e-792fb9d1748d | -7.78188 | -49.84713 | 2025-10-05 00:35:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5077a8c8-1b49-3f06-96b4-8dc068918cf9 | -4.31869 | -48.08311 | 2025-10-05 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 90f7828e-87b0-3db7-b161-c23c67929305 | -6.21789 | -42.93993 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| b671db3f-519f-39c0-9812-03648f7df640 | -6.36122 | -43.91645 | 2025-10-05 00:35:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| efea04e1-4f03-31d8-89f4-1aaaf38ea6aa | -2.29626 | -47.99069 | 2025-10-05 00:35:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 78e83ae6-af3a-3ae8-a20b-ff6a13503d1a | -6.15297 | -44.61867 | 2025-10-05 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b21ff09d-144a-3d9f-be34-8d40b6e5c8f5 | -5.58467 | -49.02568 | 2025-10-05 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b5cf79b6-2ee1-37d9-a627-492d06326d55 | -7.06025 | -49.96048 | 2025-10-05 00:35:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 05b0ff42-8b55-3a92-a44f-4f93cae37c41 | -7.55171 | -47.27642 | 2025-10-05 00:35:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 974b666d-8325-377b-b4e1-ab49f46cd196 | -5.10003 | -45.19961 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5ebda185-f988-35df-8b68-2d36db392c87 | -4.76705 | -46.9106 | 2025-10-05 00:35:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| a1d4c2c0-2616-3708-b619-f5cac83eacd3 | -5.78336 | -42.93037 | 2025-10-05 00:35:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 0fdbb86e-af9c-3c9e-9308-0ddeac0ae8ab | -6.15045 | -44.67873 | 2025-10-05 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| e3b2d21f-bb95-301d-9b91-c1dcc282587a | -6.14615 | -44.64968 | 2025-10-05 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 248.0 |
| 45d1130f-977f-36af-a4ff-2d2d791171f7 | -6.24944 | -45.35033 | 2025-10-05 00:35:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6764bdcb-aa32-37a8-ba9b-c2986326892e | -7.45626 | -47.18786 | 2025-10-05 00:35:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 72d89edb-0992-31bd-ac99-f38c34361087 | -7.64238 | -45.49305 | 2025-10-05 00:35:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 814ee1d3-2be5-3853-b98f-8c26c8fbcfe2 | -6.25136 | -45.36343 | 2025-10-05 00:35:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 48fdff8e-9ce2-3ec4-8459-a922f40ea0e6 | -5.77166 | -45.79171 | 2025-10-05 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| f8e66aad-f7ba-33e9-8d86-4b7a662679de | -4.6409 | -43.18592 | 2025-10-05 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 578.2 |
| 1aec1c52-57e6-3b64-9fea-72b5ad121dd3 | -7.80905 | -44.53358 | 2025-10-05 00:35:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 86ab33f9-5834-355a-8ef9-c200f8cdfae9 | -2.60384 | -49.40555 | 2025-10-05 00:35:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b14fe459-2d1e-30a9-8ae6-1821a05865f1 | -6.40129 | -47.29973 | 2025-10-05 00:35:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1157bd2b-edc4-3d66-ae6c-4170acbaec2b | -5.22783 | -43.70581 | 2025-10-05 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3ec1df8f-87e5-3266-9222-a64c2424c64d | -3.6152 | -51.04708 | 2025-10-05 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| e35f06f9-5452-3f5a-9688-5c2b40ce4e3d | -6.23212 | -44.37974 | 2025-10-05 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| a6bdf2e6-d054-36fc-8fa1-02f1d25a1480 | -3.84587 | -41.55232 | 2025-10-05 00:35:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 29.2 |
| 5ca80059-5836-3352-bd20-fd32305532ed | -8.62474 | -50.01664 | 2025-10-05 00:35:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e09cdb9e-5e6f-363d-8cbf-487c1eb517f2 | -6.68417 | -50.18097 | 2025-10-05 00:35:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eeba6de9-4d8d-365a-97ab-f281da3b7ec2 | -6.40626 | -43.05926 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 354.0 |
| 6de1270b-3d7f-3937-9bdf-aae7d7693eda | -5.30281 | -44.32738 | 2025-10-05 00:35:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8340aa68-d481-3685-92d0-235d0d9082b5 | -6.60866 | -43.72292 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| bd4cba3d-be16-34fb-b4b2-cafbe41fa514 | -2.89952 | -48.07943 | 2025-10-05 00:35:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 0c9848fd-a7c0-31b0-b505-10c20f11798d | -8.34061 | -49.49421 | 2025-10-05 00:35:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| a1a844a6-df12-3343-a174-1b5beec8dd03 | -5.2315 | -49.07322 | 2025-10-05 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 2142191e-276a-31f8-a3a9-5b1d3361c24b | -5.98721 | -51.88863 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e07f57c7-b4af-3d6f-814e-4dafe6f805b1 | -6.21492 | -42.91983 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 837eb1c7-e54f-36bf-9e4e-64ae60ae7ee7 | -6.42862 | -46.01594 | 2025-10-05 00:35:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cef02281-89ab-3cc4-9857-d392b61896c5 | -5.64443 | -43.91459 | 2025-10-05 00:35:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 304.7 |
| 9372380e-7000-3ede-8836-81a1e1ca6a0f | -6.40985 | -43.07276 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 7c2b5f57-66a5-3f12-9a64-b6c6c65e5a75 | -6.91225 | -45.06771 | 2025-10-05 00:35:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| b4f54f6e-6057-3f30-b756-2f24b6a22bcc | -6.14833 | -44.66438 | 2025-10-05 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 941.7 |
| 548b483d-d315-3d76-86a8-99bbc1ae7501 | -6.2881 | -43.91104 | 2025-10-05 00:35:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 3fe67ba4-d21c-3ca8-ad13-222c1ce5c40b | -7.78922 | -44.55036 | 2025-10-05 00:35:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 1f6f2035-badd-310c-8660-1ee368af2ef6 | -6.45836 | -44.57881 | 2025-10-05 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 2a675471-e590-38a3-9069-f954ab68a44b | -5.93437 | -43.31885 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| aff48e2c-1434-3def-9512-11184cb284c1 | -7.81103 | -44.54694 | 2025-10-05 00:35:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0738dc39-bd80-3e2f-bb74-bf8e59862d82 | -5.60771 | -51.73621 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a39204ff-c3d2-39cf-991e-8a3daea8c267 | -5.84195 | -42.88039 | 2025-10-05 00:35:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| e42bda0e-99d2-3355-a674-7857f6df6e97 | -4.45319 | -43.24754 | 2025-10-05 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| afbc2eed-4938-356f-b67c-d4197d65ac0b | -5.64699 | -43.93151 | 2025-10-05 00:35:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 835b6389-8429-3dc9-a744-0c1b61fc1ca0 | -8.84498 | -49.94564 | 2025-10-05 00:35:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 048a61f0-0e1e-3a95-a9a0-8f26e3dc59f8 | -5.98961 | -44.37197 | 2025-10-05 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| cf47efc8-1d1e-3583-83db-acf0095ef121 | -3.84341 | -44.55048 | 2025-10-05 00:35:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| f66665ca-52b3-313e-b2f1-2addda1ce88e | -5.06765 | -40.46474 | 2025-10-05 00:35:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 58.2 |
| 66edbb35-29fe-32b3-bcae-e56f09fb0a87 | -6.09405 | -43.48878 | 2025-10-05 00:35:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| efc2f4d1-22b6-308a-bb23-c56a615ca58b | -6.16155 | -44.67696 | 2025-10-05 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 1ad3c9f5-d3c1-3b67-84a1-65ad319535b5 | -0.90494 | -47.55053 | 2025-10-05 00:35:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e84a7f2f-0cc5-3f0c-a9a5-d76658caaafd | -6.88065 | -47.22957 | 2025-10-05 00:35:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e7666363-5f05-3c30-bf37-7f67d1469f10 | -5.60006 | -51.1447 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cac4eda7-276a-33bc-82d9-e2fc649c84a3 | -8.23648 | -47.03735 | 2025-10-05 00:35:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 417cf227-f1b2-3d8b-b325-c71b6221f2be | -7.71915 | -46.28441 | 2025-10-05 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 482320aa-73e4-3e3c-af62-c6da5c877f40 | -6.4303 | -46.0275 | 2025-10-05 00:35:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| ebd57102-4b6f-3b60-aaa6-9adeacace22c | -6.61433 | -43.71534 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7295bf9f-7ea6-3fc5-99ad-025b1b0f0d4c | -5.60798 | -51.80828 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 27868d27-9c6b-3345-ba5f-6e34b5eeba27 | -4.13096 | -47.65704 | 2025-10-05 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7ef143d4-7e2f-3f42-be8e-1bfa5723d4ee | -6.01666 | -44.02171 | 2025-10-05 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| b618a1b8-13d3-3a83-9a7a-aa829ea14555 | -8.2211 | -49.14873 | 2025-10-05 00:35:00 | TERRA_M-M | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fb8c532c-6583-3c85-a4c8-e484b49a6d54 | -4.52549 | -47.08369 | 2025-10-05 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 136c03c4-2020-3962-b8f5-c34ead567f75 | -4.24737 | -48.56072 | 2025-10-05 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 80a674e9-247c-3324-bd45-99901732ab89 | -7.1553 | -46.07961 | 2025-10-05 00:35:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 0d2ebd40-efa5-3b47-ab05-837997892fbd | -2.89817 | -48.06967 | 2025-10-05 00:35:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 060bbbb9-8369-33ad-9d34-d91f6fb64a10 | -4.44031 | -43.24949 | 2025-10-05 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 4401adc2-2860-378f-84be-1bad67c2346a | -7.79811 | -44.53519 | 2025-10-05 00:35:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 48.4 |


[Clique aqui para ver as próximas entradas](README12.md)
