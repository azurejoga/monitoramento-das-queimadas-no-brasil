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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6cca8d8-bf2b-3d8e-bc18-9307d4e24b8a | -14.7981 | -48.7851 | 2024-10-02 04:26:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 993f2e98-ee37-35d9-9876-a261e18b5e50 | -14.7986 | -48.7628 | 2024-10-02 04:26:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| b5f57307-4f65-352f-be40-c672a28c1811 | -15.8933 | -57.1754 | 2024-10-02 04:26:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 2b3bb04e-cb08-38e3-bc1f-211ad8e5d5e8 | -16.0898 | -53.503 | 2024-10-02 04:26:36 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 3d3ac7de-678c-3244-8748-f09fb6e3a7c2 | -16.109 | -53.5215 | 2024-10-02 04:26:36 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| b673c01a-df8c-3921-927d-5fc2078be21e | -16.1094 | -53.5004 | 2024-10-02 04:26:36 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 6596dd25-7fbd-3856-89b2-19863e6b9ac7 | -16.4746 | -57.3144 | 2024-10-02 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 49368bd1-935e-397d-a450-3c3ebd7559fb | -16.475 | -57.294 | 2024-10-02 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 23973c9e-c32a-3ae7-b3e5-66833d4f0fac | -16.4942 | -57.3122 | 2024-10-02 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 91a149d2-b5fe-3d3b-a1cf-da3ac9171274 | -16.4945 | -57.2918 | 2024-10-02 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.4 |
| b0de3ae3-a4b2-3c65-87f0-56ebc6601b33 | -16.514 | -57.2896 | 2024-10-02 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| eef8f237-61e8-34d6-b1ca-1ef491396df7 | -16.6124 | -57.2375 | 2024-10-02 04:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.3 |
| fc2da462-cbbd-392d-a641-b4f995914972 | -16.6127 | -57.217 | 2024-10-02 04:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| e24305a7-58e4-306e-ab2b-c798328db998 | -16.6868 | -57.4741 | 2024-10-02 04:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.0 |
| ea580560-67c1-3b9f-be44-f82cba242686 | -16.6912 | -57.1875 | 2024-10-02 04:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.6 |
| a6295eb3-d2f9-3dd1-a533-52719ea8dbd7 | -16.6916 | -57.167 | 2024-10-02 04:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| 69ed2d5c-4225-351e-b03a-9bf23a1dd526 | -16.7063 | -57.4718 | 2024-10-02 04:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.3 |
| 352a8943-0c85-3234-a93a-cb5d360f3377 | -16.7108 | -57.1852 | 2024-10-02 04:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| 0eb09eab-4ea3-332b-90d3-f217d48968af | -16.7265 | -57.4287 | 2024-10-02 04:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.8 |
| 808b5a83-826d-3876-872a-fb1fb1ca68f3 | -16.7269 | -57.4083 | 2024-10-02 04:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| a5ff3337-7231-3ea8-8834-bc6de109fb47 | -16.7452 | -57.4878 | 2024-10-02 04:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.5 |
| 0bc85009-930f-3c52-9195-44299d394862 | -16.7455 | -57.4674 | 2024-10-02 04:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.8 |
| d786ffa6-3f40-36cf-a0bf-131a46a0bcff | -16.7461 | -57.4265 | 2024-10-02 04:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.2 |
| 6d3ac64f-f328-3cd7-82c2-78c36f9b7998 | -16.8096 | -55.9177 | 2024-10-02 04:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.4 |
| 8b7f8d44-c412-3ab4-a94a-44da69a21a64 | -16.8292 | -55.9152 | 2024-10-02 04:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 106.6 |
| bd6f6939-561a-3254-8ea3-aae06047b348 | -16.8295 | -55.8945 | 2024-10-02 04:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.8 |
| c266f20c-5967-3e6b-a160-b0f04f87c709 | -16.8491 | -55.892 | 2024-10-02 04:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| 5ffb4326-d388-3719-bef8-d1b01f9704f5 | -16.8695 | -55.848 | 2024-10-02 04:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 196.9 |
| e46354c6-35e8-3324-b067-a1838cd2a2bc | -16.8698 | -55.8272 | 2024-10-02 04:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 180.7 |
| ded892e0-2795-3135-bcca-30556ec83aaa | -16.8891 | -55.8455 | 2024-10-02 04:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 129.6 |
| 793f3fca-d40b-3b29-9e9b-e9597a0b6f25 | -16.8894 | -55.8247 | 2024-10-02 04:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 128.8 |
| 9a1774e5-85f6-39bb-ab43-0f409fed4109 | -17.0709 | -56.6908 | 2024-10-02 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| f5c07db8-fe8b-3f96-9424-6ee4d55a1057 | -21.3456 | -55.6841 | 2024-10-02 04:27:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 106.6 |
| c3b85ae2-5318-3e23-bb91-9981239272a1 | -21.3661 | -55.6807 | 2024-10-02 04:27:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 73.0 |
| dae8526f-65ab-3e13-adf8-bdb413c86be5 | -22.3713 | -49.3011 | 2024-10-02 04:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 218.0 |
| 1468b514-28be-361a-93d3-637959c5b464 | -22.372 | -49.2777 | 2024-10-02 04:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 213.5 |
| f5628d80-258e-337d-9a23-c9c9e904b903 | -22.3922 | -49.2961 | 2024-10-02 04:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 197.3 |
| 795b0b93-78a1-3082-9567-7ef722d03f25 | -22.3929 | -49.2727 | 2024-10-02 04:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 142.5 |
| 9e5e17cc-108a-3d28-b865-2aa4d9f52959 | -22.9014 | -45.0779 | 2024-10-02 04:27:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.5 |
| 7e70be87-1e3c-3613-9fd9-3cfb78a72c2a | -9.9554 | -64.8984 | 2024-10-02 04:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 787e2c73-a3ae-3bb3-81b9-3e56fc57a8b4 | -9.9553 | -64.9172 | 2024-10-02 04:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 8473ebb8-768f-3e4b-a03b-3a21227e7c0c | -9.9367 | -64.9179 | 2024-10-02 04:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| f11fef40-eec1-3d75-aba4-b83cb20132f2 | -10.867 | -69.495 | 2024-10-02 04:36:08 | GOES-16 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 106.2 |
| e429e463-c34e-3c02-84b0-3b2adc38d2da | -11.6931 | -64.9974 | 2024-10-02 04:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.0 |
| cbcb14f7-0870-3da0-9780-c7abf6effb1d | -11.6743 | -64.9983 | 2024-10-02 04:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 5a6bcdac-a6ce-390d-838c-4dac53acc414 | -11.6742 | -65.0172 | 2024-10-02 04:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| cd3a270c-7598-3d2f-bbac-bfe35afdcd70 | -12.6486 | -63.1022 | 2024-10-02 04:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| a7a8fa0c-7d26-3745-9efd-7ded342b498f | -12.6484 | -63.1214 | 2024-10-02 04:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 73084336-df6d-3150-b555-6112a3b28915 | -15.8933 | -57.1754 | 2024-10-02 04:36:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 6d9dd344-3955-3d59-9ee4-9c618ab7cb3d | -16.6127 | -57.217 | 2024-10-02 04:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| 10116c03-2da9-39d4-bc33-1f31963b3178 | -16.6124 | -57.2375 | 2024-10-02 04:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 64c9aadd-742a-321d-9d28-4c6a5253c3b2 | -16.514 | -57.2896 | 2024-10-02 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 73eabe18-ab78-304a-ab67-c95a0a7eca86 | -16.5137 | -57.31 | 2024-10-02 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 2213b992-dc3c-31c9-8dd9-05b457f741c8 | -16.4945 | -57.2918 | 2024-10-02 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 42ed4ca2-23dc-30d2-bc3a-f237a5e82c35 | -16.4942 | -57.3122 | 2024-10-02 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.4 |
| 06e1f6f7-512e-3e81-93b0-c31b387e02f2 | -16.475 | -57.294 | 2024-10-02 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| fc3ff067-3db1-3873-a4f8-7c98c700fe03 | -16.4746 | -57.3144 | 2024-10-02 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.1 |
| 8607952b-24b8-38f4-95ff-2dc499f14615 | -16.8096 | -55.9177 | 2024-10-02 04:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 3f709688-32dd-3309-b2ca-8e3d669470a7 | -16.7647 | -57.4856 | 2024-10-02 04:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.4 |
| e7e7fcb5-3fc3-3146-935f-1759a32f1910 | -16.7461 | -57.4265 | 2024-10-02 04:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.3 |
| 29196041-3867-3b3c-b619-69547eb56ebd | -16.7455 | -57.4674 | 2024-10-02 04:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.3 |
| 05f31b52-8764-340b-8de7-38ceea338fd9 | -16.7452 | -57.4878 | 2024-10-02 04:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.7 |
| 77c6dede-6d0c-3a06-8da3-b00d3e272139 | -16.7269 | -57.4083 | 2024-10-02 04:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.2 |
| a545f3cc-2a1b-3f79-ba26-52ad527a999e | -16.7265 | -57.4287 | 2024-10-02 04:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.4 |
| cf138098-7922-346c-8907-14d69c4af2ed | -16.7063 | -57.4718 | 2024-10-02 04:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.9 |
| 2fb8d021-2761-3bd8-b4f6-b1c4f74fd4c8 | -16.6916 | -57.167 | 2024-10-02 04:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 527fbdc3-b6b4-3a4c-b38d-bd5f68e73af8 | -16.6912 | -57.1875 | 2024-10-02 04:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.8 |
| fae3b874-3ce3-34de-8d0e-09e698d6eb49 | -16.6887 | -57.3513 | 2024-10-02 04:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.7 |
| 1591913b-f14d-3e64-8c77-912bec5e6ccb | -16.6868 | -57.4741 | 2024-10-02 04:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.0 |
| 67426724-14b2-35e8-805f-f0c8705ae86e | -16.6322 | -57.2147 | 2024-10-02 04:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.0 |
| dc3de45b-4a4d-3513-a853-364475828329 | -16.8292 | -55.9152 | 2024-10-02 04:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 104.2 |
| 534f0030-4ac3-3723-9c6c-2cc2301d84d8 | -16.9179 | -57.6926 | 2024-10-02 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.7 |
| bb6a0fdc-8834-3177-bde5-faa39cc886c5 | -16.8299 | -55.8737 | 2024-10-02 04:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 0dec4d0d-96c2-3484-909e-622bcbacf75b | -16.8295 | -55.8945 | 2024-10-02 04:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 123.8 |
| 3c828f66-aa67-3153-a1c5-85b66e6b0a15 | -16.8695 | -55.848 | 2024-10-02 04:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 166.2 |
| 48923a5f-aa17-3d97-bd94-da1b854a2bd3 | -16.8698 | -55.8272 | 2024-10-02 04:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 129.9 |
| 86f1199d-ccc9-39ed-8f25-126cca71da77 | -16.8891 | -55.8455 | 2024-10-02 04:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 161.1 |
| bae121e4-c02f-390e-be02-75edf8dbe6b9 | -16.8894 | -55.8247 | 2024-10-02 04:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 130.3 |
| 9e06efb7-f768-33e5-86fd-61af0ee45654 | -16.8787 | -57.6971 | 2024-10-02 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| e1f6f981-dc8b-3bbd-822a-0eb9bac7d187 | -16.879 | -57.6767 | 2024-10-02 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| ad09750e-78d7-3dfc-bac6-8bd06ad802dc | -16.898 | -57.7153 | 2024-10-02 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| eb806f31-5f3b-3c67-a6de-2481a82ee649 | -16.8983 | -57.6949 | 2024-10-02 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 168.6 |
| 412460ce-f732-3ce8-baf2-33044121c1b7 | -16.8986 | -57.6744 | 2024-10-02 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 86ded244-92f3-36b1-8866-89969daa9703 | -16.8491 | -55.892 | 2024-10-02 04:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.0 |
| c39e6264-08ad-3057-9db4-6f9898c6388b | -17.2364 | -56.1745 | 2024-10-02 04:36:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.9 |
| 20025637-29ce-3d78-9fa8-9ff1a1ae71ab | -17.2361 | -56.1952 | 2024-10-02 04:36:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.4 |
| 11f34585-4932-3568-91a6-1a84c80c1f47 | -17.2167 | -56.177 | 2024-10-02 04:36:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 477bcca2-2b69-3f8d-a49b-9492660dbf7c | -17.2164 | -56.1977 | 2024-10-02 04:36:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.2 |
| d8acd8d8-0bda-3ad8-9698-15d39e78e3b9 | -5.20523 | -37.63124 | 2024-10-02 04:44:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 307916bc-0fef-3be5-9cb9-aa2ef3ed1264 | -4.94468 | -43.68163 | 2024-10-02 04:44:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a70ae225-617d-3e83-97b6-5d47b49b358d | -4.94397 | -43.68636 | 2024-10-02 04:44:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f381bf2f-6c86-3e34-8d4e-d9e8a2f2646f | -4.78656 | -43.79864 | 2024-10-02 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5db41446-6dab-3ff0-9c4e-ec1a67aa1570 | -4.66554 | -43.7603 | 2024-10-02 04:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae8be68d-4b99-3ab6-87e1-eb4256db8638 | -4.66099 | -43.75957 | 2024-10-02 04:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fce5546-1a73-33c4-bfea-e02765379644 | -3.86246 | -40.78072 | 2024-10-02 04:44:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 84c39d2a-b35f-3fae-b28e-fc6a30b1cd16 | -3.86229 | -40.78259 | 2024-10-02 04:44:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2e0dceb8-139d-35bb-8993-91ec424036f8 | -4.84186 | -42.79572 | 2024-10-02 04:44:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 16b377aa-cb8c-33fb-b25b-a80156bcd5eb | -4.46537 | -42.88845 | 2024-10-02 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05707304-8725-3770-9ec1-4869b11606b9 | -4.46056 | -42.88767 | 2024-10-02 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a137c47-1fb9-37f7-96c1-8d20f8d99943 | -4.45977 | -42.89303 | 2024-10-02 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README82.md)
