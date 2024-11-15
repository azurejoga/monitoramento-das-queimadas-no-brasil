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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 566a33e5-1f7f-3dc3-b07c-023907ffe1f9 | 0.44593 | -50.92589 | 2024-11-15 04:21:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 960b6130-6ecc-386a-8d3b-e28482a2f3cb | -2.65081 | -46.1841 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f247566-f16d-3652-8f11-0f3d1206f286 | -2.6503 | -46.16484 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a79f106-d627-3a84-92da-6af47e4c4318 | -3.8913 | -42.55493 | 2024-11-15 04:21:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dbda00a5-0a4e-32df-9fc6-bd9285859e44 | 0.00627 | -51.22324 | 2024-11-15 04:21:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37098738-07ad-3311-b83a-bd37611666f7 | -2.7107 | -44.77677 | 2024-11-15 04:21:00 | NOAA-21 | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db792f19-9f01-3dd2-b649-f1094c8215f0 | -2.85436 | -46.62547 | 2024-11-15 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 073fe200-8217-3807-a8f2-d84638efd76a | -1.9088 | -45.44927 | 2024-11-15 04:21:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c2d8155-9354-3fa1-b5c7-6b50270a492d | -3.23505 | -45.37854 | 2024-11-15 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af49e9d5-8f8b-3a55-9e87-8bd0f7e2dda1 | -1.91022 | -45.44999 | 2024-11-15 04:21:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 122de75e-a747-3e90-97a1-40645c264541 | -3.13982 | -45.16501 | 2024-11-15 04:21:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d46c95fe-5a4c-3789-9e7c-6bb18366702b | -3.71363 | -41.69363 | 2024-11-15 04:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 1afbb37d-b435-3f4a-8fd2-124bd27d4db4 | -1.21258 | -53.56611 | 2024-11-15 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b84ac05-17db-3ba2-b861-e7e0b273dfaa | -2.66469 | -46.18212 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 570b65d1-b465-3395-9f54-ec3a499ff848 | -2.7885 | -45.95407 | 2024-11-15 04:21:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e775324d-5097-3847-9b17-f8cff7bed48d | -4.10427 | -38.73749 | 2024-11-15 04:21:00 | NOAA-21 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 951f9962-6612-3079-a97b-f6ef4f337595 | -2.72065 | -44.77831 | 2024-11-15 04:21:00 | NOAA-21 | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 408237d7-35e4-3a33-8616-b0ee2203e626 | 0.11735 | -49.84588 | 2024-11-15 04:21:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8bf73a2-c523-300f-ac11-22054cd979db | -3.73561 | -42.19477 | 2024-11-15 04:21:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0f9fe8e0-49d1-3c8b-a393-15e13b28dd5c | -1.86654 | -44.77967 | 2024-11-15 04:21:00 | NOAA-21 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4fed2fc-86bf-3a91-856a-c0f834101d5c | -4.51408 | -44.07555 | 2024-11-15 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bbf92a37-74ee-3f9a-8913-2077833e0e3c | -3.72719 | -43.93112 | 2024-11-15 04:21:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4daae3b9-b4f7-3cb3-bfbc-47b83e80b50f | -2.3155 | -45.06157 | 2024-11-15 04:21:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0ca727f-0cfa-38ac-a717-c301538faa35 | -2.09682 | -46.32936 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c62f04c-93a3-38a6-af53-ba5d8f1eb8fd | -1.92296 | -45.56659 | 2024-11-15 04:21:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95d739a1-e5ad-32a7-a758-28dfaa3e43b4 | -3.53422 | -41.84299 | 2024-11-15 04:21:00 | NOAA-21 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 948976e1-25bb-3cb3-ae8c-45fbeafd3ee4 | -2.61981 | -46.82336 | 2024-11-15 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b44e3e92-c0b8-3344-a6f2-6a005514fd45 | -2.21224 | -53.71458 | 2024-11-15 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f7f936a-2bd2-30ce-86f0-67e754f1acf9 | -2.34371 | -47.2169 | 2024-11-15 04:21:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ccc6a0d2-dda0-3326-8245-5e70531f3abe | -3.61338 | -44.79053 | 2024-11-15 04:21:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 795a3571-ecc6-3899-8ffd-77d0f870b826 | -2.64401 | -46.16003 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d63fb44a-1979-3301-bd7f-8ae7329c59ba | -4.37639 | -43.67088 | 2024-11-15 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| add27788-0fa6-3372-a426-a992347a4bfc | -2.29307 | -46.45379 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4a279f3-cd76-34b1-a77b-a42cb4342009 | -3.87709 | -43.31484 | 2024-11-15 04:21:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54b7936e-d215-3e69-b40b-598cb9cb233b | -2.66173 | -46.18196 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad74d9ad-6c8c-3e56-b650-5912fb2a91fa | -1.81883 | -46.95767 | 2024-11-15 04:21:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54ba8848-d6ba-300b-9932-606f96b62e23 | -2.65257 | -46.17287 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdd8e4b8-b7f8-31c2-be7f-85f0cf99761c | -2.61919 | -46.8273 | 2024-11-15 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3863c804-b603-3d80-8d69-a2bfed3676d8 | -1.85461 | -47.82922 | 2024-11-15 04:21:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 429f08a7-6512-3f1a-8712-ad36925b1966 | -2.62273 | -46.8278 | 2024-11-15 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7d569d9-bd44-311d-8b4a-f0b261e06a2c | -3.88845 | -42.55074 | 2024-11-15 04:21:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 92d17ca8-bdc4-313d-a97c-3b9a69542dee | -2.31495 | -45.06508 | 2024-11-15 04:21:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fd04db9-b139-3160-818e-9ad985e089a7 | -2.61698 | -46.17501 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfcd5ec7-74ec-3896-a2f1-ff10b6afc4cb | -2.64737 | -46.18357 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 480922b9-cc1b-39c4-aae3-ff0555c75983 | -2.37572 | -45.63276 | 2024-11-15 04:21:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a974db7f-4f1a-3b4b-a079-0e1a6dea2caa | -3.8879 | -42.5544 | 2024-11-15 04:21:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7f76f89b-29d3-3fdc-9532-07e65f820d92 | -4.19896 | -40.68012 | 2024-11-15 04:21:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| ee5580cb-c067-3f32-86a3-0127ecf7bf7e | -2.60606 | -46.17716 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dc29373-1e5f-3287-8f98-837edd25dac2 | -2.2076 | -53.71242 | 2024-11-15 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f44212a9-d5ef-3a91-883a-8411da2d4461 | -3.09885 | -45.96803 | 2024-11-15 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05100807-59cc-3cb5-941f-072053806808 | -3.71714 | -41.69417 | 2024-11-15 04:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ec4664b2-a62a-3085-8c10-94292fa1e0de | -4.39533 | -43.7023 | 2024-11-15 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c1d63e2-82f9-34b5-b4a5-d31a068e5745 | -2.62629 | -46.82828 | 2024-11-15 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ac995ad-2b60-3c19-bf51-03d0a3526c66 | -3.79531 | -43.91039 | 2024-11-15 04:21:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af4c9a51-a7d2-3e2f-9b80-27f18005bd43 | -2.34009 | -47.21634 | 2024-11-15 04:21:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10a6be94-4349-3eaf-ae86-7c7ec8e84453 | -1.62385 | -46.08213 | 2024-11-15 04:21:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d221746-e48b-32fc-b713-f3c392f3ce0e | -2.78492 | -43.34191 | 2024-11-15 04:21:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| eb4622b8-4cb6-391c-871e-762bd5e9203c | -1.57501 | -53.80352 | 2024-11-15 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efff640d-eb7d-366b-b618-a47852f5f24a | -2.24289 | -46.29658 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d52cbc35-93e3-33e0-864e-856c6506cc6e | -2.30517 | -46.45494 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e85928a-fd5a-3ea1-a82b-fee84e0a5bd5 | -2.66349 | -46.18962 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86a86d0c-eda6-3dcd-a2c0-831a9911462b | -2.62328 | -46.17982 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e075e37-ca92-39f6-8033-84c5cdec5395 | -2.30107 | -46.45825 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c823afd-e19c-3324-b2ce-215e90768573 | -3.60298 | -44.4891 | 2024-11-15 04:21:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a0b80a58-ed6c-31ad-b980-f1551ba97cc6 | -1.69845 | -45.80965 | 2024-11-15 04:21:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55a3acfe-f7d8-33e8-b17e-9f3c20325262 | -1.36453 | -46.34592 | 2024-11-15 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 809aea42-4ca8-3294-a24c-5dbf107c95ef | -1.21629 | -47.47332 | 2024-11-15 04:21:00 | NOAA-21 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b5f145e-2653-3ebf-98f0-485510bac770 | -1.92965 | -46.28053 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a1d9b6c-627e-3d57-8b93-e40c5bb1b8dc | -2.58699 | -47.48069 | 2024-11-15 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53906c66-ddfd-3a53-983b-0813985743fc | -2.64964 | -46.1916 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc2e164a-dcdf-3946-a18f-346ef9b5ee14 | -1.85567 | -46.2855 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a12d1bc-40a2-3d17-8edc-dcad8320b074 | -3.792 | -43.90988 | 2024-11-15 04:21:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc1fea98-cf8d-3c6d-80fc-5fba8facd812 | -2.12526 | -46.48799 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95712fa3-11b3-3c7e-af4c-4fa867cab9bd | -2.63075 | -46.17715 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e15ce4df-95b6-339f-a578-e7a929f2159b | -2.32979 | -46.87059 | 2024-11-15 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c77605ad-f6c2-3328-800c-902a5e32cf10 | -2.28958 | -46.45325 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63d1d917-562f-3215-8cd5-dd6b1a5230b9 | -3.79147 | -43.91333 | 2024-11-15 04:21:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 62c3b0ad-439f-3bc9-aadb-a9ef6acb8a0a | -2.86837 | -45.05076 | 2024-11-15 04:21:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68f2acde-5343-3355-8ae5-4b084fd28b6a | -2.64334 | -46.18678 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ee9d24b-446d-3b7f-a779-97611da4d5e2 | -1.70675 | -46.15667 | 2024-11-15 04:21:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb1e9c6f-9e19-3e46-bdb8-8cb8f3ebdc7e | -2.59064 | -47.48128 | 2024-11-15 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86b4a3c5-e062-3de3-aae5-ea63eb08c5e6 | -1.46391 | -48.19796 | 2024-11-15 04:21:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 863fde86-c55f-3d2f-a526-d1c130c356cf | -3.10111 | -45.97588 | 2024-11-15 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e4b4966-7344-3ed8-8d07-822f8a3e2b76 | -1.93931 | -47.95852 | 2024-11-15 04:21:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f0ad545-e7e3-30fc-b8a5-d8e54b798942 | -2.56265 | -46.00667 | 2024-11-15 04:21:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b379c79-fc14-3873-8af2-74307b6ff5ba | 1.07185 | -51.13984 | 2024-11-15 04:21:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 363d8201-e317-3017-aee9-6781e7b032ca | 1.0735 | -51.15072 | 2024-11-15 04:21:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2f6fbe9c-7dc6-3f75-aaee-016885bf42c9 | -2.88242 | -40.3092 | 2024-11-15 04:21:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ce905870-4b03-35af-b985-a2d4cad7f13d | -3.14594 | -45.16955 | 2024-11-15 04:21:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49539074-eaa3-3127-9776-127f05bf015d | -4.13532 | -38.70261 | 2024-11-15 04:21:00 | NOAA-21 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 54230ac8-c9a1-3900-bbdf-f01190fc2308 | -2.30168 | -46.45439 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72c5abdb-9a93-3d01-85b6-4f54d2409f1a | -2.90524 | -46.85364 | 2024-11-15 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc6bf9fc-19d4-3e2f-a741-38b63e02e33a | -2.71456 | -44.77381 | 2024-11-15 04:21:00 | NOAA-21 | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95ba9862-81da-3670-b809-be7bede61d23 | -2.09744 | -46.32553 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b8e65bc-411f-3121-a95b-1b0c25e45825 | -1.68486 | -46.12263 | 2024-11-15 04:21:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cdb1d1bc-cc5b-301c-973f-47742126287a | -3.10168 | -45.97222 | 2024-11-15 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae737354-9380-3ceb-b690-7b66f966eb99 | -2.18817 | -46.15635 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4953dc61-33ef-3260-94c2-ccf8d0147f3e | -1.41929 | -53.47666 | 2024-11-15 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2d5d173-1150-3a38-bb06-57ccbfd0d99a | -2.21316 | -53.71332 | 2024-11-15 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d376eeeb-680d-3baa-bff7-ec2d3e733d4f | -1.98889 | -46.36782 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README14.md)
