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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 915fbe8b-9f64-379b-a7b2-4b358ceb5814 | -18.08602 | -54.31952 | 2024-10-08 04:59:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3def233f-8dc5-3dae-b0e3-6829fe0c8383 | -18.08252 | -54.31902 | 2024-10-08 04:59:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ab00730-dbc7-3987-80b6-d2b6a64985f4 | -18.08072 | -54.30656 | 2024-10-08 04:59:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2eb36834-fe49-305d-a5c5-15f86b4a9011 | -18.07958 | -54.31454 | 2024-10-08 04:59:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 085d8c14-5819-3683-bd27-70d436912284 | -18.07844 | -54.3225 | 2024-10-08 04:59:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5dd2fa51-8664-3e89-b32d-6bf03228578a | -17.34037 | -55.01783 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 23692886-ce42-350b-8a38-dc72820c9fb3 | -17.33753 | -55.01349 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9a0acded-c0fc-3bb4-9d64-5bd8a6e424ef | -17.33697 | -55.01728 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ace35d82-5c91-394d-8dc3-d8b494141c8b | -17.33641 | -55.02107 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3b72e9bd-733b-3b61-a4dd-945d25d125f5 | -17.33585 | -55.02486 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0b234ea3-a668-3004-a90a-2d101303f79f | -17.33413 | -55.01293 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d207701b-90e9-3516-9e06-ba3377d2c42b | -17.33357 | -55.01673 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a76ea580-1315-319a-8731-2f701c203ba7 | -17.33244 | -55.0243 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2595b200-f96b-3cf0-b99a-a9cc0d27a920 | -17.33129 | -55.00859 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c7b7e233-773c-35be-968e-593b53b5b30e | -17.3302 | -55.03944 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d7c139f2-e4a8-3177-aa41-0f77a961cc54 | -17.32845 | -55.00425 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0d73f2c6-a805-3197-90bc-09f6b68b1d76 | -17.32789 | -55.00804 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a6004ebf-49aa-3ad9-9d8b-3937d29ac9d4 | -17.32733 | -55.01183 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 809ef7c6-f5b1-353d-a51b-c7b6e319b9f9 | -17.3268 | -55.03889 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c7559766-2448-333a-b7f1-0222275179af | -17.32505 | -55.00369 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d994d7d6-3740-3a2f-9a88-86b232c0509a | -17.32449 | -55.00748 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 932b2a98-ed50-3e4a-9e2e-70f30bf57aef | -17.32393 | -55.01128 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2bdf3647-549f-3650-9f53-049b7e63cb14 | -17.15836 | -53.94943 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ada21660-153e-34f3-b053-bcb8ca3891cd | -17.02522 | -55.07679 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5790abe-1b5e-32b5-87d5-58849f635f2c | -17.02183 | -55.07624 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1438ec4a-f616-3de0-9b49-647a9dc205b9 | -17.01728 | -55.03701 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8d31071-42d0-381b-a7ee-3a78a4c4221a | -17.01389 | -55.03646 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9ba4b24-109e-3585-914e-730e7a757852 | -17.00144 | -55.02673 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d387860f-f540-3bf0-8d31-ac76539410fe | -16.9986 | -55.02242 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc27b41f-aee7-310f-a509-29f63d21005b | -16.98958 | -55.03637 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 749219cb-d9a6-363d-b418-d407ce84efab | -16.98618 | -55.03582 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ccc6a84-8c5d-3f4f-870c-f6f44ae339cd | -17.7945 | -53.80001 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e626f125-2ebe-365b-8df1-7a5b96297306 | -17.77189 | -53.80508 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 598393c5-c151-366c-a0cd-4ec6fef65064 | -17.77008 | -53.79224 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb8f9239-07d9-3852-ab9e-ba568f3ee79f | -17.7689 | -53.8005 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c1955795-905b-3552-bb86-5d7b398c3576 | -17.76832 | -53.80455 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b7d919ab-ebe2-38de-a28f-c1a3e623c1a6 | -17.7683 | -53.77914 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b946cff-44b1-30b2-961c-b566bd548cff | -17.76773 | -53.80868 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 53b4670f-1144-310c-a898-03cffcef0eb1 | -17.76714 | -53.81284 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 81fd2a23-1188-34b9-b1ef-1691e68199c8 | -17.76531 | -53.80009 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c99f434-3d8e-3775-9ada-854c2a8b8856 | -17.76416 | -53.80816 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d5e1ec0a-f415-3286-a34f-566a1bfab8b5 | -17.76357 | -53.8123 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 34466168-5d3d-3f8e-ad92-f829fe74dd5f | -17.76 | -53.81177 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0cef1fcb-4fcc-3a19-9474-1d9db82fd02c | -17.17593 | -53.92734 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1b7ebc9-2f1c-34ec-9173-c9ddfbef29b4 | -17.16189 | -53.94998 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1444f353-fe4f-3dc6-987e-bc41b19bbec3 | -17.15895 | -53.94536 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1d6175e-2b9d-3261-b949-2e62fa1e8598 | -17.156 | -53.94071 | 2024-10-08 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1b827ddc-a8dd-393f-bb67-15c9595db8d3 | -18.92522 | -54.55553 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d95ebad9-84c3-3beb-aaad-0d86f66120f6 | -18.92114 | -54.55906 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e56b13b9-ff4e-35ca-89f9-09ff8c4e8894 | -18.91765 | -54.55852 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41405a3b-46de-34a8-abc1-87fca13ae4aa | -18.91415 | -54.55797 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e109468c-4362-3d4d-91a5-32cfa3c6e025 | -18.91011 | -54.56126 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac1363a4-8b09-36e0-88e3-53c2c17974b3 | -18.90953 | -54.56529 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65c8261d-a189-366d-a141-b3e6d718a8a0 | -18.90894 | -54.56943 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32fd8518-755c-3ac7-b023-aa7549fa64c9 | -18.90664 | -54.56051 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4708356a-492d-329d-bef9-839b0e8dcd7b | -18.90606 | -54.56452 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78e8c4c5-f777-3893-bcdf-8392da6f7353 | -18.90547 | -54.5687 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8a35527-ede0-3d7e-8b35-c23d7415495b | -18.90259 | -54.56379 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38a3fed8-eabc-3889-8d36-62327f267aaf | -18.90185 | -54.4681 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33b4f9f4-844f-36d6-91a8-8506062ce727 | -18.90158 | -54.46968 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c544080c-b987-3473-8219-c93541d05947 | -18.90135 | -54.54747 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1cab61df-c33a-3cd2-a4d2-29279662e6f0 | -18.90127 | -54.4722 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2084c6be-3bf0-3e00-b487-9b988dd9d5bf | -18.90098 | -54.47378 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0168a841-b08a-324c-a08d-a4107215efdb | -18.90083 | -54.57618 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aa18eb18-c36d-3d43-9a46-336f22147396 | -18.90069 | -54.4763 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92052345-4469-386b-8faa-65882d6b7e85 | -18.90026 | -54.58018 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75cb6cc1-ad8a-31b1-9b42-55a1d1f3dcff | -18.90023 | -54.55526 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 486b7d58-71ee-37f1-a449-47d7963a64e2 | -18.89953 | -54.48454 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffebf6de-3f71-3431-a91b-910f07e67db3 | -18.89918 | -54.48611 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 166a333a-1595-348f-9485-23549ca3994f | -18.89868 | -54.46492 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fd850db-9aba-389e-a575-db40df1fa1f7 | -18.89809 | -54.46901 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 401b92fb-82f8-3cd0-9543-c890a1ad3476 | -18.89749 | -54.47311 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3d67328-4f21-315d-93b4-ec7b266e628a | -18.89678 | -54.57952 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ecb06fb-dc0c-3eea-ab89-c684fbb18575 | -18.89629 | -54.48133 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c31e50b-5e8c-30ee-ae97-ef71e9e5fe71 | -18.8958 | -54.46014 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7403a17-38d7-3990-b5bb-535522b1f634 | -18.89569 | -54.48548 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 161d306a-5082-33b6-91a0-ece5fc77d547 | -18.8952 | -54.46425 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8dc283e-361e-39d1-82a2-3a338aa153a4 | -18.894 | -54.47245 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54a44994-a171-3740-b870-de1c875e5e51 | -18.8934 | -54.47656 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 774e678c-9a17-3cbc-a6aa-d81732b3217b | -18.8928 | -54.4807 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77b3b15f-9544-3362-b678-b4a2500e76cd | -18.89219 | -54.48486 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e8b6b4a-23db-37a7-a8d4-87aa570208f7 | -18.8917 | -54.46362 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a60629ae-e287-3d28-a54c-3cd0efe91d92 | -18.89051 | -54.4718 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e75826b-a9a8-3d39-9d43-89bdec343368 | -18.88991 | -54.47593 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56224a7f-6d6f-364b-838d-80c328dc5b49 | -18.88574 | -54.5818 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53f7ae3b-1420-3331-aa08-55edd7e8d9aa | -18.88499 | -54.58323 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b6daf19-69cf-30bc-b077-c4f77263c849 | -18.88151 | -54.58263 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c223d7dc-0a6e-3c61-b4a8-82416148849f | -18.87862 | -54.57795 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c8cf45f-528a-36d9-97dd-42f962c8a076 | -18.87803 | -54.582 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46865e48-297f-383c-885f-514be109c327 | -18.87514 | -54.57732 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11326058-7079-372f-b62b-d5a1b73d5f17 | -18.86876 | -54.57207 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0bc363f-9ccc-3fcf-9ad2-542deb22ee84 | -18.86528 | -54.57145 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd63d01a-f368-38cf-bd93-f656d7676fe8 | -18.8618 | -54.57084 | 2024-10-08 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee620d33-8711-3f7f-8b83-f6296a44bc78 | -18.2145 | -54.45066 | 2024-10-08 04:59:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fba3417-7102-3202-9fb0-c5afbe058557 | -18.21391 | -54.45471 | 2024-10-08 04:59:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dbcedcd-da07-31fa-9f3e-062d964885d4 | -18.21042 | -54.45414 | 2024-10-08 04:59:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ce7a108a-bf80-3288-9b83-0aee844839f1 | -18.20752 | -54.44953 | 2024-10-08 04:59:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 871b0cd8-2e55-3b1c-a1ed-c422b5ade7ba | -18.20694 | -54.45356 | 2024-10-08 04:59:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 886df2f5-d839-39d0-a255-221aacdafba4 | -18.20636 | -54.45758 | 2024-10-08 04:59:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 57166ceb-1cb1-3c9c-970e-93866568657b | -18.20403 | -54.44897 | 2024-10-08 04:59:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README97.md)
