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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a98e92f-2fd1-376d-9688-c06bdadc5b2d | -9.0024 | -47.37838 | 2024-10-25 16:52:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f7ec37c5-ecf5-3632-98a8-687def709730 | -9.00178 | -47.37446 | 2024-10-25 16:52:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c046300f-b148-30ae-adfd-6aeff5e529b0 | -8.97401 | -47.2901 | 2024-10-25 16:52:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60117b53-362b-3deb-b607-c2f2b17a1510 | -8.96987 | -47.28678 | 2024-10-25 16:52:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43ccb6da-275f-3252-adfb-acec8523035b | -8.92102 | -47.31899 | 2024-10-25 16:52:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 998b1b5f-add2-3e74-bd19-9f42a446c194 | -8.92039 | -47.31505 | 2024-10-25 16:52:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a04f6b6c-b2f8-363d-9ff9-7cabf8322c71 | -8.8891 | -47.29986 | 2024-10-25 16:52:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc00e8e1-213a-3361-a748-6ad8ec48d77b | -8.8883 | -47.29988 | 2024-10-25 16:52:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36fa74ec-1249-3dc3-93b1-f08daa42c04f | -8.8027 | -47.26102 | 2024-10-25 16:52:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fea30551-421c-3706-b22d-691f30268f15 | -8.74847 | -47.19489 | 2024-10-25 16:52:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a137f245-2dde-3186-a11e-06582ce874b1 | -8.64128 | -47.27356 | 2024-10-25 16:52:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7288864-2157-37c5-b401-dcd1b2bfd7b7 | -8.63711 | -47.27012 | 2024-10-25 16:52:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d0b3066-9df2-3fe5-9c4f-52eea987ad77 | -8.57728 | -47.16867 | 2024-10-25 16:52:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ebb96ddb-8979-349d-a884-05d40346e446 | -8.57233 | -47.11551 | 2024-10-25 16:52:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| abfd3ebe-1767-383b-95ba-01f5471c2f6c | -8.65145 | -48.02409 | 2024-10-25 16:52:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a188067f-28e4-38a5-bc4b-a4cd5ce4cb82 | -8.61628 | -48.15584 | 2024-10-25 16:52:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c57b9b49-ee02-37f5-8b40-07b68e332806 | -8.58806 | -47.86828 | 2024-10-25 16:52:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c9b4b662-9dff-353e-87da-38874a43ae6a | -8.51311 | -48.21386 | 2024-10-25 16:52:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 741d2873-afce-35d4-9839-17d7d0437461 | -8.23742 | -47.67277 | 2024-10-25 16:52:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 394689d4-96b3-3162-87da-058e50c03b65 | -8.23694 | -47.86974 | 2024-10-25 16:52:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| f5b82db6-acf4-39f2-82cb-4890d1aa2c66 | -8.20335 | -47.63847 | 2024-10-25 16:52:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a5ed31d-77ce-34b4-93dd-496d0917d73e | -8.11916 | -47.63564 | 2024-10-25 16:52:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 929f6158-cb83-317c-ab32-8d08213e21a3 | -8.0984 | -47.70671 | 2024-10-25 16:52:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 63230bc6-f67d-3dc0-8bc4-cfebc8f4b12b | -8.21444 | -47.14663 | 2024-10-25 16:52:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| e4d4816d-cd29-39e5-b83e-e91b481aea57 | -8.21225 | -47.15089 | 2024-10-25 16:52:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5ce50a3-0d88-3380-9cc0-f93e8565d3b8 | -8.10781 | -47.45207 | 2024-10-25 16:52:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dbfbeeef-294e-3314-9057-6b02b598d796 | -8.10717 | -47.44806 | 2024-10-25 16:52:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3fd0faaa-6e38-3086-a072-a6b195f812f5 | -2.00619 | -48.53069 | 2024-10-25 16:52:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 50652860-75cd-30bc-9723-e8a8149ae3b7 | -9.55286 | -48.30879 | 2024-10-25 16:52:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ebd980d-124f-372f-a9c7-670e09024286 | -9.33498 | -48.54846 | 2024-10-25 16:52:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eff5776a-71a0-3d19-96e3-e0b0ff31624e | -9.44985 | -47.76781 | 2024-10-25 16:52:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a1a51666-ee04-3efc-95c1-fe98f5beae1a | -9.44564 | -47.74139 | 2024-10-25 16:52:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35bc6d95-3b2c-3f8c-af3f-2b2017efa4ac | -2.09798 | -48.42102 | 2024-10-25 16:52:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c46fb5f1-c526-3387-bd74-5138b990a926 | -2.03177 | -47.89545 | 2024-10-25 16:52:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e8b56156-67aa-3253-b540-6cdf531d2232 | -2.01759 | -48.51711 | 2024-10-25 16:52:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f1f76bdd-1c4d-38c3-afa5-75a364303bfc | -2.01548 | -48.59145 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 4e98a9d9-04ae-3a68-b0b2-d8ba4cd1d773 | -2.01436 | -47.78567 | 2024-10-25 16:52:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 93ba6412-017b-3a87-9fa1-24c6de5ae361 | -2.01402 | -48.51766 | 2024-10-25 16:52:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 56c77b07-cf3b-300d-9c92-ae601b34292d | -2.01366 | -47.78125 | 2024-10-25 16:52:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 12e84155-9b29-3c27-96a8-b1f87b2d9354 | -2.00976 | -48.53012 | 2024-10-25 16:52:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 506678ea-5887-358d-b689-03e2d785a6c9 | -2.0088 | -48.53094 | 2024-10-25 16:52:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| e3f7ef87-b24e-32fb-bb91-bbd783560728 | -1.99218 | -48.487 | 2024-10-25 16:52:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c0b79fff-30b0-3341-bbc9-331355d5df18 | -1.99156 | -48.48291 | 2024-10-25 16:52:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 97f35638-7e14-3774-ae33-9563b680ba43 | -1.9886 | -48.48755 | 2024-10-25 16:52:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f0b6d9de-cf6e-35cb-9db2-26a58184c2f1 | -1.98797 | -48.48347 | 2024-10-25 16:52:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b258497a-715d-32af-b590-deef7dbf3ce8 | -1.97668 | -48.64688 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ed8c88cf-5b0f-34a9-a358-5f0b30b3f894 | -1.95557 | -48.74422 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 62decd78-03ab-3ef0-944f-298d9298fd76 | -1.95348 | -47.96889 | 2024-10-25 16:52:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8890c6de-2252-3e33-a552-5e03df48ae6e | -1.92693 | -47.96287 | 2024-10-25 16:52:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0923ae6c-7780-3c78-acae-e23bb3935c37 | -1.92634 | -47.96417 | 2024-10-25 16:52:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a70a7385-9669-3b04-b308-4a8886cf173d | -1.87544 | -48.55404 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5b9bb505-fac9-30f5-a145-9b443ee8d8cd | -1.87186 | -48.55459 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| af95d0d6-8278-358b-b14a-9e19d5cd9271 | -1.86154 | -48.60596 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| d07d284d-4dbb-3220-b423-6ad3df747741 | -1.85601 | -48.15859 | 2024-10-25 16:52:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 565427d3-dc39-3b8f-8bb7-a22b53898486 | -1.82546 | -47.45034 | 2024-10-25 16:52:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1adacba7-fb02-3119-8980-addbdd3153f8 | -1.76931 | -47.74176 | 2024-10-25 16:52:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1689ca82-b3ce-394e-90ed-68a757464d9e | -2.92301 | -48.95638 | 2024-10-25 16:52:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d66d6714-cf74-3798-8d84-1a514e971e8b | -2.871 | -47.8441 | 2024-10-25 16:52:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f688ee33-844a-31ca-b6fa-f90667b3cbc0 | -2.79133 | -48.69113 | 2024-10-25 16:52:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 905a41f5-e5aa-318d-8f77-e65af2937343 | -2.53 | -47.36805 | 2024-10-25 16:52:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 4b8d714d-e665-3913-abf9-da2628e8c566 | -2.52622 | -47.36862 | 2024-10-25 16:52:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 98196eef-19b9-349f-a20b-e8a2c42d7ef7 | -2.34887 | -47.49987 | 2024-10-25 16:52:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| a622a9e6-921d-31ac-8720-1afa10541913 | -2.34816 | -47.49534 | 2024-10-25 16:52:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 59bdffee-9d56-3e47-933a-8244e7a3845f | -2.34511 | -47.50045 | 2024-10-25 16:52:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3540624d-ed4d-37cb-9ea9-5a4bedaeaf1a | -2.3444 | -47.49591 | 2024-10-25 16:52:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c5a5824e-ef20-3a96-bdde-5d273f7fcdf6 | -2.44811 | -47.82127 | 2024-10-25 16:52:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 857f429b-f9c9-3b1c-a951-5078c4946da2 | -2.44744 | -47.81688 | 2024-10-25 16:52:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e1eb8b09-334a-3bba-9d5f-ce4d47de7175 | -2.44681 | -47.81795 | 2024-10-25 16:52:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 6c67f9c3-cb7f-3411-ba01-58cf065ae79e | -2.44375 | -47.81747 | 2024-10-25 16:52:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 21c2c470-f4c7-36c1-a3fe-0f0aa2728640 | -2.44313 | -47.81857 | 2024-10-25 16:52:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c33f5f4f-a58b-3498-b080-d7b3c7906e2f | -2.39636 | -47.77999 | 2024-10-25 16:52:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 23b75b13-1ba3-3b54-9123-46ca34ea018e | -2.35038 | -48.83809 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 51ef2e86-0926-3182-9a67-aceaaa60ea8c | -2.34688 | -48.83865 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 78ebd5ba-bf84-39c6-9874-df5c5cd5c35e | -2.29692 | -48.49205 | 2024-10-25 16:52:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 0ab385e9-76ae-3d90-815b-3aeed019e321 | -2.17807 | -48.56727 | 2024-10-25 16:52:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 0611f9e4-3667-371a-9702-bcdff0581014 | -2.17744 | -48.56325 | 2024-10-25 16:52:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e4633acf-c63d-37b4-ba3c-4481be3ded5a | -2.17389 | -48.5638 | 2024-10-25 16:52:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| cda7c8b0-477f-3783-8af8-4f78ae0b2542 | -2.15201 | -48.70237 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 0e4cd9d2-2167-30ed-89ad-95ba391842d9 | -2.10508 | -48.77432 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b437e6d5-8715-3b42-9fab-8948ac4ae950 | -2.09712 | -48.81594 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a3615042-5d96-33c1-9bde-953637fd061e | -2.09361 | -48.81649 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 46d13247-27b4-32e5-a3aa-76b3c3753858 | -5.07655 | -48.16593 | 2024-10-25 16:52:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 72bd4f5e-dfc5-3fee-b8bc-c59855f9d01f | -4.92794 | -48.56185 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4fd6dff2-8fbe-3310-9608-2a737ab5e70d | -4.89549 | -48.64866 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f62b74fd-fdd6-3348-b40a-ccfa9f065155 | -4.88633 | -48.65788 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7d948226-b6fc-365f-b1d8-ee5ee93cda7f | -4.87313 | -48.66379 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1b875ffc-3753-3e5d-a1f8-ead2d10aabde | -4.83923 | -48.5172 | 2024-10-25 16:52:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0072c5b6-deba-3353-a4c3-81e0baf2d72d | -4.83873 | -48.61874 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1c107fa4-613c-34ea-bad9-457ac47eb1b9 | -4.83723 | -48.51736 | 2024-10-25 16:52:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cc45a072-68be-35f5-ad72-f09396ccdc25 | -4.50186 | -48.22193 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6d1df426-a9ac-3f57-9ca6-92b98b4b3394 | -4.49354 | -48.21509 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0b7ff01d-2515-38ee-813b-96af0c6644e1 | -4.49064 | -48.2196 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e7dd8181-0a8e-3f8d-9ebb-e4166578f12d | -4.33918 | -48.63768 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8d79aa1b-6e05-335c-8b82-d48c1617cab7 | -4.3357 | -48.6382 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 23e6091f-a04b-3e87-b23b-c57ecf4be03a | -4.3351 | -48.63438 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5f3dd2a0-e48e-3b47-a6c6-57c653689222 | -4.33223 | -48.63872 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fdc1e1ee-2faf-3ebb-b7ad-0873d2d48fda | -4.33162 | -48.6349 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1d3a1181-9022-3765-bf54-ea14c6f3c37a | -4.25251 | -48.5521 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4da7dd7a-f6fc-3257-8a91-156fac40e9b8 | -4.25191 | -48.54824 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d607b90b-1c17-324d-9853-213f1dd8e80c | -4.24902 | -48.55265 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |


[Clique aqui para ver as próximas entradas](README150.md)
