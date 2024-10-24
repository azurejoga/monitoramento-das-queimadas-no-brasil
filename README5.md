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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f25900b-b73c-3dbb-b11a-4c25bcb0a6ea | -4.5574 | -45.7905 | 2024-10-24 00:55:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 7731b585-1510-399c-b59b-d96f0a109757 | -4.6588 | -44.61 | 2024-10-24 00:55:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 5995305a-9bd3-30bc-9dbc-914776554cae | -4.6775 | -44.6089 | 2024-10-24 00:55:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| fadf1f8e-b726-382f-ba83-46c29c2ff8d0 | -4.8423 | -45.0309 | 2024-10-24 00:55:34 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 342e9d91-a76d-3171-82a9-d316ca4742bc | -5.2935 | -47.0129 | 2024-10-24 00:55:36 | GOES-16 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 8e279419-539c-3af0-add5-ec23e0ad4a1e | -6.7238 | -40.4754 | 2024-10-24 00:55:44 | GOES-16 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 59.7 |
| f05333f2-f819-305b-8fb6-89a3a7d99842 | -6.7425 | -40.4981 | 2024-10-24 00:55:44 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 9984108a-1a58-3093-8262-f1d97cd3b831 | -6.7427 | -40.4735 | 2024-10-24 00:55:44 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 125.8 |
| 2e396eba-4a32-3316-9604-e3d4d14185fe | -6.9272 | -40.8466 | 2024-10-24 00:55:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 108.3 |
| 70c61796-bff6-36ff-b1f0-c5b33e8bd6f7 | -6.9461 | -40.8447 | 2024-10-24 00:55:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 175.1 |
| b55e4b98-0791-3468-8f30-2efa3c0f72bf | -10.0144 | -47.4639 | 2024-10-24 00:56:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 5fc6a135-7713-370e-93b2-5a1e7a9fabf6 | -10.0147 | -47.4417 | 2024-10-24 00:56:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 31aeaaec-3562-35da-a869-92930b16023c | -10.1969 | -53.8822 | 2024-10-24 00:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| e8afaf78-7c53-3622-8b5a-4ca685b33815 | -10.1971 | -53.8617 | 2024-10-24 00:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 9902c894-c986-3b72-ad13-5b48ae5c2124 | -12.6914 | -43.8484 | 2024-10-24 00:56:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 1858ac2e-1160-3d9e-bc5d-65a7bf5a5976 | -12.6918 | -43.8247 | 2024-10-24 00:56:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 0b745c49-5e44-302d-85d8-6786c7ef2aa8 | -12.3783 | -63.863 | 2024-10-24 00:56:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 289ab6d4-3a9a-3cad-b442-3fec5b73836b | -13.7417 | -54.0682 | 2024-10-24 00:56:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| d9418aa0-3272-3895-a76c-e2d6a3e83d82 | -13.742 | -54.0475 | 2024-10-24 00:56:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 115.2 |
| eb9d7f18-73be-317d-90da-efda0677aeb1 | -13.7609 | -54.0661 | 2024-10-24 00:56:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| c1e4e4a4-b3c0-3dd1-94ad-e57528daab19 | -13.7612 | -54.0453 | 2024-10-24 00:56:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| d4b221eb-def8-3af9-a011-bfa12b7eea26 | -14.9145 | -45.1224 | 2024-10-24 00:56:29 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 13119ebc-4d90-3ff2-94fb-2b25dae11f6e | -15.5389 | -50.6688 | 2024-10-24 00:56:33 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |
| f1dddb59-113b-32c4-84e2-caddbe119381 | -15.5584 | -50.6658 | 2024-10-24 00:56:34 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 636f6d0e-c046-3922-9e51-3573fa047cf5 | -15.5589 | -50.644 | 2024-10-24 00:56:34 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| a6340d9b-49bc-3780-8295-0d4058b49ad5 | -15.578 | -50.6628 | 2024-10-24 00:56:34 | GOES-16 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 94108794-80c7-392e-8d78-b0ec77aea90d | -16.9596 | -57.5245 | 2024-10-24 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.6 |
| dd3067ea-5950-38a9-b2b8-12b162c2ec19 | -17.0207 | -57.3743 | 2024-10-24 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 1c45e6d9-4983-30e7-85ec-63aa5033fd37 | -17.2383 | -57.2462 | 2024-10-24 00:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 4d9c5bf8-3f0b-3f00-98c4-9c962512f803 | -17.2579 | -57.2439 | 2024-10-24 00:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| d6a403f2-25bf-3eff-a34c-583fde04d21b | -17.7637 | -57.5732 | 2024-10-24 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 09e64029-7ec5-3d41-bc58-a477820b8275 | -17.7831 | -57.5914 | 2024-10-24 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| a6531b91-9fac-3d87-89be-6331d2568860 | -17.7834 | -57.5708 | 2024-10-24 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.5 |
| db160eee-071e-37d4-ba7c-489272b702f4 | -17.7841 | -57.5296 | 2024-10-24 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 5125b5cd-4b95-3c6c-9208-4c0255b739ce | -17.7844 | -57.5091 | 2024-10-24 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.9 |
| cb8072e5-98c8-315d-b8c8-12339099ad04 | -18.0639 | -57.3101 | 2024-10-24 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.9 |
| 9bd2202b-56d6-319b-8f29-d761018cd51f | -18.0837 | -57.3076 | 2024-10-24 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.9 |
| f9e7333f-43dc-3d25-87b2-7c075d353a0c | -19.548 | -56.6143 | 2024-10-24 00:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 060439b2-693f-37c5-95e7-cdfbb9c94d2e | -19.5681 | -56.6114 | 2024-10-24 00:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 5eab098e-8da1-3489-b2be-85219e88fc9c | -23.795 | -55.2753 | 2024-10-24 00:57:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 69.1 |
| 8d377520-dcd3-3d62-9efc-bdd0b57ebd00 | -23.816 | -55.2713 | 2024-10-24 00:57:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 96.2 |
| 7633fd2e-c13c-377f-b1cc-e3a33091e7f9 | -1.4945 | -54.1962 | 2024-10-24 01:05:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 22aee3bf-815c-3622-854e-7ebcc9ce466d | -1.4945 | -54.1761 | 2024-10-24 01:05:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 11efc969-5edb-3694-835a-d1782c301a72 | -1.5878 | -53.3089 | 2024-10-24 01:05:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| ed4f0a36-c5bd-3429-a156-c2b78645ec0b | -1.6062 | -53.3087 | 2024-10-24 01:05:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 7aeb4fc9-f408-3ddf-96ae-e9f286434894 | -2.9578 | -50.4198 | 2024-10-24 01:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| b36cdb4f-3c52-3b17-b58d-e75f409ef1bd | -2.9763 | -50.4193 | 2024-10-24 01:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| d050236d-3c40-3ebb-a532-6eb4e6948f1c | -3.1607 | -50.4556 | 2024-10-24 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| a9423b52-3b61-327c-a76d-4cb6cfa093d9 | -3.0745 | -53.8252 | 2024-10-24 01:05:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 1266b2d0-f423-3a0b-beca-1a2bba34bfdf | -3.1101 | -54.1661 | 2024-10-24 01:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| d4bf732f-d67a-35c4-a84e-4d65dbfb3cd0 | -3.1102 | -54.146 | 2024-10-24 01:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 752df952-8b94-3ae8-bc77-816e293234b2 | -3.1606 | -50.4766 | 2024-10-24 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| ac789414-e93e-3c23-958f-24b23edc622e | -3.7066 | -41.6997 | 2024-10-24 01:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 21070228-45a0-30ee-8811-ccb280c9cf90 | -3.7068 | -41.6758 | 2024-10-24 01:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 123.0 |
| 693ae384-9884-3dfe-b08c-bbf6faeff574 | -3.6612 | -54.2715 | 2024-10-24 01:05:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 4fca8df8-a111-3534-9ebe-9bfadefc2269 | -3.7254 | -41.6987 | 2024-10-24 01:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 995727e1-f0ba-359e-9be3-d22b7173abb4 | -3.7255 | -41.6748 | 2024-10-24 01:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 119.4 |
| 32630410-32e8-3c6c-b79c-dc884dc5bb58 | -3.6613 | -54.2514 | 2024-10-24 01:05:27 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 79ad2f63-ca6d-329a-b93e-a0949d51cabf | -3.9396 | -46.4229 | 2024-10-24 01:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 00bf75c9-4235-30b1-993a-f5c8dae45d59 | -4.5698 | -43.9967 | 2024-10-24 01:05:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| ae903a24-391d-3cdb-af16-ced10ba52d0c | -4.6588 | -44.61 | 2024-10-24 01:05:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| c608be00-172a-38e4-971f-1b8b8adc799e | -5.2935 | -47.0129 | 2024-10-24 01:05:36 | GOES-16 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| c5a18070-d4e8-3566-adfb-d2d8b9001a15 | -5.4373 | -47.6833 | 2024-10-24 01:05:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| f6e2c720-e165-329d-b0e0-b8afbe3c9720 | -6.7238 | -40.4754 | 2024-10-24 01:05:44 | GOES-16 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 83.0 |
| acbcfab5-90a7-3384-8883-c14ab5f9c697 | -6.7427 | -40.4735 | 2024-10-24 01:05:44 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 7fd9048f-6511-3c54-9e7a-d081cb4668eb | -6.9272 | -40.8466 | 2024-10-24 01:05:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 116.3 |
| f89ca01b-b29e-39e4-b83d-612f5b1616e4 | -6.9461 | -40.8447 | 2024-10-24 01:05:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 120.1 |
| 05d1455d-cb59-3a2c-b198-d49014d40cbe | -7.481 | -63.5577 | 2024-10-24 01:05:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 23a89b30-4bbe-3a68-9d08-5a2a609a92f5 | -10.1969 | -53.8822 | 2024-10-24 01:06:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 2bd2c64e-55d9-396c-91d3-9f8ac1335a54 | -10.1971 | -53.8617 | 2024-10-24 01:06:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 75603fee-53f1-3025-9124-df89e3afe718 | -12.6914 | -43.8484 | 2024-10-24 01:06:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 8619dc5e-227f-378a-aeeb-0dcaadfd84eb | -12.6918 | -43.8247 | 2024-10-24 01:06:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 5d4f82d7-9d7b-3c6a-83ce-f902bf3556dd | -13.7417 | -54.0682 | 2024-10-24 01:06:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 51da72c8-48e9-30a2-838c-c37a12401a83 | -13.742 | -54.0475 | 2024-10-24 01:06:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 3d37df63-e58e-3bba-8f9e-6bf5afa26ef6 | -13.7609 | -54.0661 | 2024-10-24 01:06:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| c9508e55-c422-3635-92d5-98065fb65cab | -13.7612 | -54.0453 | 2024-10-24 01:06:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 3136a2ab-1453-3dff-8d30-8f72bfaf0fbc | -14.9145 | -45.1224 | 2024-10-24 01:06:29 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 63.2 |
| b32da257-e751-3f30-9bd4-ff38ada05590 | -14.9341 | -45.1187 | 2024-10-24 01:06:30 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 65.4 |
| d98bc54f-b09f-3153-865f-a3e70be85c5c | -15.5584 | -50.6658 | 2024-10-24 01:06:34 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 120.7 |
| f9eaa874-ad0c-3791-8418-8cb65a2a0e32 | -15.5589 | -50.644 | 2024-10-24 01:06:34 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 99.2 |
| c4c102da-caa7-3276-83d4-78a9a6fd5751 | -17.0207 | -57.3743 | 2024-10-24 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 908cc044-f0a9-30f9-9477-d96b82619d8a | -17.2383 | -57.2462 | 2024-10-24 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.3 |
| b3db7dd2-4981-34d3-8e90-7b47e4a9e7b8 | -17.2579 | -57.2439 | 2024-10-24 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| a2f8e371-e254-3f19-911d-a421e8e04998 | -17.7062 | -57.4774 | 2024-10-24 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 26ea5c1f-7d8e-3b22-bd1c-bae42047773d | -17.7637 | -57.5732 | 2024-10-24 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 7cae44c4-df1f-3473-aac2-6b25b81c05b8 | -17.765 | -57.4909 | 2024-10-24 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| e5a07f89-ce61-3c72-bc82-8d1ec4d98568 | -17.7831 | -57.5914 | 2024-10-24 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 69eb6219-b3fc-3a96-8693-2c31b3cacc74 | -17.7834 | -57.5708 | 2024-10-24 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.5 |
| 204e765b-da71-35b9-8813-738a7c03bcdf | -17.7841 | -57.5296 | 2024-10-24 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.0 |
| 16450b45-5dfd-3e1f-b3ac-f69fdc332c2f | -17.7844 | -57.5091 | 2024-10-24 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.1 |
| fded0eba-a542-3124-93f6-4871f2e64a4d | -18.0639 | -57.3101 | 2024-10-24 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.9 |
| 04d29ecc-0412-37bc-b171-b03ed36be403 | -18.0837 | -57.3076 | 2024-10-24 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.7 |
| d708f709-2dee-34ae-9df3-9b84f1720b7b | -23.795 | -55.2753 | 2024-10-24 01:07:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 55.2 |
| b83304ea-e11e-3309-9215-138a4b9d1a1c | -23.816 | -55.2713 | 2024-10-24 01:07:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 117.3 |
| 8b9424cd-948a-3017-8058-658d9fa6d5e5 | -1.4945 | -54.1962 | 2024-10-24 01:15:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| ef683503-0e5a-332d-a848-56e8a160f5ea | -1.4945 | -54.1761 | 2024-10-24 01:15:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 9563a183-bafa-3da3-b634-7117933a471e | -1.5878 | -53.3089 | 2024-10-24 01:15:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| e66596c6-ad63-3881-a40b-c4c617fef08b | -1.6062 | -53.3087 | 2024-10-24 01:15:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| d8a63ce9-7194-33df-9da5-4fcb0be29159 | -2.9578 | -50.4198 | 2024-10-24 01:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| ed8e818e-779b-3883-ac09-aa77a17bdf4f | -2.9763 | -50.4193 | 2024-10-24 01:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |


[Clique aqui para ver as próximas entradas](README6.md)
