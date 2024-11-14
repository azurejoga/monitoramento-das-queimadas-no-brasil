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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4b8d281-759a-3d66-8073-d527d7750a9b | -5.3403 | -43.546001 | 2024-11-14 00:32:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14408eef-b0ba-3125-bfae-4ac15ad09c80 | -2.2642 | -50.663502 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b91ea79e-5674-3f77-a3a5-e539609e96ec | -3.7796 | -52.088402 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f57f9483-aa1b-35c8-9e2f-843e7ed26434 | -4.1435 | -46.2542 | 2024-11-14 00:32:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 95375712-e2b8-3c5a-935c-ddfc5c5d24cd | -1.2628 | -52.163502 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44f2b9ed-5765-388c-8f8c-1682cd5f4ede | -1.608 | -52.507099 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c5716b5-58b5-307e-8248-7b150aad68b3 | -17.561701 | -57.486599 | 2024-11-14 00:32:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 21d50727-36fb-38e7-8ff5-0d42b6eee872 | -3.7285 | -50.438599 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e92a999f-39aa-3712-94ff-8abe78c71b60 | -3.7812 | -52.0956 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 790d8183-d39b-3a75-840e-7915bca81ee6 | -1.6437 | -52.528999 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdf2f0b5-dbb0-35df-a5f5-68ad94a3ebfb | -2.8919 | -53.0439 | 2024-11-14 00:32:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d8fd9b7-fef2-3fdf-8d07-51d7dc66553c | -3.3417 | -45.415199 | 2024-11-14 00:32:00 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ac44da2f-9939-3f5a-a8db-51cef83d2fda | -6.8627 | -44.7533 | 2024-11-14 00:32:00 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05b25557-1dc2-3a91-bddb-7a61200561d7 | -1.3886 | -51.121899 | 2024-11-14 00:32:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05b728ff-5dc5-393c-b4fc-d11beefe873c | -3.4866 | -50.828701 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd77eeeb-9264-3a83-87ef-4910d710a913 | -2.6648 | -46.9874 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a1b960d-1b6f-3df8-9ddd-1bc33f3bf3cf | -17.5753 | -57.507801 | 2024-11-14 00:32:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6dbca128-b489-3bc7-b30f-d02df0f1fe4f | -4.4415 | -49.580502 | 2024-11-14 00:32:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6771fac0-f995-3cd3-9491-7437dbb953b3 | -3.4038 | -44.974602 | 2024-11-14 00:32:00 | METOP-B | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 74ecd7b6-9219-30a7-a85c-acc83e8b9130 | -0.8959 | -51.7244 | 2024-11-14 00:32:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7b1ee6d6-ccbe-327d-90f1-a644b25356d0 | -5.1908 | -44.347301 | 2024-11-14 00:32:00 | METOP-B | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1707fbca-5246-3475-ba33-9c20a42c42bd | -2.3436 | -51.976101 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b89bb005-eace-3d11-a8a4-5e6a5a41bf99 | -1.133 | -51.6791 | 2024-11-14 00:32:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3193aa55-4398-3c3e-8667-3344884008cc | -0.1991 | -51.513802 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 42732160-2ac4-3c94-bcbd-6d3a6ff00ab8 | -2.6529 | -46.980701 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bc77518-0333-3cb2-8893-d9ee095f225b | -3.409 | -50.3018 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff51015c-3e55-366e-9375-b5dd67f911a5 | -2.2042 | -53.696201 | 2024-11-14 00:32:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a6f6636-9e9f-33f0-ad73-db49fe3c37f4 | -3.0464 | -45.5172 | 2024-11-14 00:32:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c582a36a-e975-3451-ac92-a047838dacfd | -4.0355 | -47.214401 | 2024-11-14 00:32:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 28d685de-355d-31d0-ac94-0eeccd9b6351 | -0.1961 | -51.500198 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 05c0528d-e68f-384d-9ca1-a767e31ec297 | -3.9849 | -45.570301 | 2024-11-14 00:32:00 | METOP-B | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e7c010b8-002b-3358-8025-29f3f7229700 | -1.2783 | -52.461102 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e917ca35-7a74-3808-bd1a-0f2e9d592896 | -3.049 | -45.528 | 2024-11-14 00:32:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4826df42-e168-3d2b-98aa-5d051ac4951b | -2.4631 | -45.841499 | 2024-11-14 00:32:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 38082b96-9830-3baa-9e48-9e05b4fe9a13 | -2.893 | -46.860001 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcb370bc-5c35-39b9-8ac7-1af36d959451 | -3.7132 | -50.599499 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36424683-6025-368d-98ce-248b9c9729bf | -2.3112 | -50.6889 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a027d0d6-6e47-3e4a-935c-b2aa7d0290c8 | -0.2255 | -51.493599 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 41862d1e-9847-3dcf-9fdd-c8e3217d064b | -3.8802 | -52.262199 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1073682e-ec9f-37b5-b4fb-92ed980fa957 | -4.3874 | -47.2659 | 2024-11-14 00:32:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b0dcc61c-868e-30ce-aa57-94ccb189bf14 | -3.0176 | -45.659302 | 2024-11-14 00:32:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 244d1c89-855f-3687-b81e-cbc5c616cd15 | -2.689 | -51.863201 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 658b93d9-5e7c-3758-af79-76c77415941d | -4.439 | -45.354599 | 2024-11-14 00:32:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c073fc9a-471b-3129-8fea-69bf1882455b | -17.5889 | -57.528999 | 2024-11-14 00:32:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 28cbfc21-f42a-33f1-b41d-9629d1b4fc98 | -2.1063 | -46.527 | 2024-11-14 00:32:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63d11edf-f0c8-3e91-97b3-f0e8231f4a6a | -2.0199 | -46.913601 | 2024-11-14 00:32:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99a1dfa0-9772-3a99-b7c5-c1377213f848 | -3.1147 | -50.230701 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2159d09-578c-3747-89c8-d07c949352a5 | -3.7764 | -52.0742 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceb33483-2b67-31a6-8158-354e0f0c2487 | -3.0417 | -45.541 | 2024-11-14 00:32:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d6f0cbef-2d63-3b13-b2c8-bb5ea1048c15 | -2.697 | -45.562801 | 2024-11-14 00:32:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef38c7ee-d785-3b11-a265-5af26203a115 | -12.3117 | -47.505001 | 2024-11-14 00:32:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e5c0ceb-92b2-305b-b39f-229e11a0fc00 | -0.8585 | -51.970001 | 2024-11-14 00:32:00 | METOP-B | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 020e67d5-a63b-3c47-a8dd-2d7d4ed74c22 | -6.0452 | -44.043201 | 2024-11-14 00:32:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5fbf2a6b-8e03-3e90-8ade-331a107a3ddd | -1.3417 | -49.136902 | 2024-11-14 00:32:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e688245c-d240-3b49-a188-8778919c269c | -1.6082 | -52.233501 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2e9693e-ac3c-3040-803d-c4bf24d9bd9f | -1.2089 | -51.741299 | 2024-11-14 00:32:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1337cdb6-3083-3797-88f7-9427b46171b7 | -2.7177 | -53.185398 | 2024-11-14 00:32:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 037554d1-5eb7-3cea-a27a-1a30d0d7f108 | -2.5326 | -47.129501 | 2024-11-14 00:32:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e7533be-7add-3389-9545-b7eaf50e49b0 | -3.1526 | -50.580799 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7776db7a-5c95-3cb4-bdde-c8eef06981a0 | -3.1347 | -45.2766 | 2024-11-14 00:32:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dbef4d6d-2228-3a4c-a88f-008b0297ded9 | -20.6859 | -48.7971 | 2024-11-14 00:32:00 | METOP-B | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6c9de726-9458-3457-894f-7faef79d33d4 | -3.0465 | -50.339298 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66071ac9-219d-3bf7-8930-33b4f4e3f439 | -5.3356 | -46.019299 | 2024-11-14 00:32:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e3ee3d99-936f-3060-8966-f983159d32f5 | -3.8796 | -46.0928 | 2024-11-14 00:32:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2eb6b2e3-ff68-3ba3-b8fb-c45a40bff7fc | -1.6095 | -52.514099 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e79a5972-df08-370d-ab86-aec7cc645b95 | -3.778 | -52.081299 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f814123-5177-3ea3-b1db-e253dd77dbbf | -1.4046 | -52.3815 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8abe7b13-8ea5-3b35-b721-00a10e6d6292 | -0.8943 | -51.717602 | 2024-11-14 00:32:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b1c1ae86-1633-337e-9ba3-217333dd8dc7 | -0.9699 | -52.418598 | 2024-11-14 00:32:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f30cc788-7eac-3978-93a2-f6ecf0ebe522 | -3.2431 | -50.388901 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d37797dc-8a0e-3677-b8f1-7a8e480f6114 | -3.6285 | -50.5896 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84c5e876-16a1-3492-914a-ae6c79fcd7d4 | -4.432 | -46.566299 | 2024-11-14 00:32:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0dd7eca5-4337-35c5-a5a8-c7a43d2959d8 | -2.6589 | -46.827 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f20ced61-75fa-3070-8992-c109396447a5 | -2.1652 | -48.5434 | 2024-11-14 00:32:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32d11941-1776-39dc-acf7-ff9951cf92eb | -3.6368 | -50.580601 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e90f7ca2-723e-3c98-b853-6e6119dd6409 | -4.049 | -47.228901 | 2024-11-14 00:32:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 88fd88ad-bebc-3f99-8bdd-54b867edae35 | -2.8661 | -51.780399 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d4f612e-396c-3357-bc30-6055f0dfa3bb | -4.0521 | -50.0005 | 2024-11-14 00:32:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5a930aa-bcfb-34ca-94aa-210ee0d7c35f | -3.7748 | -52.067001 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1763c0f6-96be-34f5-999b-09fb0ffe9a6e | -3.1188 | -50.294498 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea5b88b8-9a84-327d-9183-0f9f4f736033 | -1.9588 | -52.0975 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f30944ca-1bb2-3a4d-b866-9d2773e27221 | -3.1641 | -50.449402 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec6f767b-14bc-3b1f-b742-06e324dacf97 | -4.3729 | -50.6464 | 2024-11-14 00:32:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7608c8df-6765-3453-bf24-767f65a70cec | -1.1345 | -51.686001 | 2024-11-14 00:32:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75af87e6-bb13-35b4-9974-298f4a4ddfb4 | -4.1264 | -43.8461 | 2024-11-14 00:32:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d62e5c6-ee10-336c-bef6-e681b0c5ce3e | -3.3639 | -43.923801 | 2024-11-14 00:32:00 | METOP-B | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6fdbcec-7120-3a50-be10-21a387d787ba | -4.7518 | -49.0849 | 2024-11-14 00:32:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab32a8a9-5b93-356e-bf6b-f93d1f89ce87 | -3.4192 | -43.8965 | 2024-11-14 00:32:00 | METOP-B | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f739d92-1a89-354b-854c-fa180793cb12 | -1.8372 | -46.071499 | 2024-11-14 00:32:00 | METOP-B | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b4827cf-c34e-3dc4-8e3f-a72187e47d5a | -0.166 | -51.549599 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a07b4664-9889-3899-a45a-852cec69676b | -2.6337 | -46.180099 | 2024-11-14 00:32:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 659aa284-8621-3a2e-9beb-8794d2edf7ca | -4.58 | -46.626499 | 2024-11-14 00:32:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 24a4b8ea-5376-39a7-8bbc-37be47747848 | -1.3543 | -52.341 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5386b56-23b8-331a-bd01-4b76bb9503e7 | -2.1072 | -50.698299 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0bd6197-d2dd-324f-b438-6811f9c865f8 | -4.4431 | -49.587399 | 2024-11-14 00:32:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c842deb-5902-3bc8-84f3-9bf51a56325c | -9.40866 | -40.32297 | 2024-11-14 00:39:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 95cf0621-2c52-35d3-9664-01d27f76975a | -10.05531 | -36.34975 | 2024-11-14 00:39:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 77.7 |
| 0d5f9d2b-c12b-3f68-b253-5be5326b25c5 | -10.05695 | -36.34264 | 2024-11-14 00:39:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 0f4a5e5c-c1f3-3bca-b935-4ee1a43f14c8 | -10.04256 | -36.34535 | 2024-11-14 00:39:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 34.3 |
| c50aa30d-5411-3b35-95b0-58554dbf1c8b | -4.0682 | -50.0029 | 2024-11-14 00:40:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |


[Clique aqui para ver as próximas entradas](README8.md)
