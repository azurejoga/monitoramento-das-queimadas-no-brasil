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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7ca9a52-ddc4-357b-8218-37624b581a0d | 2.35903 | -61.00532 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4754da4a-b3ee-3af3-bbe2-6ba53814de28 | 1.66901 | -60.49852 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d8db3f5-64a5-38a7-9ef5-407ed4ab6d32 | -20.28731 | -50.98064 | 2025-03-05 05:27:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 4f05c52c-af7e-30b2-a0bb-b974f864025b | -20.28638 | -50.98036 | 2025-03-05 05:27:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 47a06bd7-ab56-3c6a-9808-6546e3974911 | -20.28782 | -50.97497 | 2025-03-05 05:27:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9f507629-17ef-3fbb-96dd-f7dbc965db11 | -20.28076 | -50.97994 | 2025-03-05 05:27:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f5b799bb-47a3-3365-a81c-c86f739f2af3 | -20.91833 | -55.5513 | 2025-03-05 05:27:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5419703f-73df-3ea1-81e6-397d8fa4f267 | -20.28685 | -50.97467 | 2025-03-05 05:27:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 8a829469-80b3-3fd8-a1df-63beac85e19f | 1.12336 | -60.51333 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf5f261c-82b7-3bd7-a0cd-da635c7949fc | 2.3565 | -61.01022 | 2025-03-05 05:44:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6a42c44e-834f-3776-8bcb-e66f61012266 | 1.13202 | -60.51712 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6cc635f-22c0-3060-8724-1c758abcf6a4 | 1.13123 | -60.51212 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e9c73e7-f3fa-3220-836b-7a18fcd48f40 | 3.23473 | -61.20673 | 2025-03-05 05:44:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b46b3c78-95e3-3b03-b5b5-8985c64dc1a1 | 2.35572 | -61.00538 | 2025-03-05 05:44:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e7dfb8ed-b6e6-3bc6-9b56-6a98c0baaf2f | 1.65145 | -60.29649 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94a0ff69-26d3-3cbb-8050-114ddf5df280 | 1.16844 | -59.15382 | 2025-03-05 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b11fac7-fa10-3d27-a673-0cb040e0811c | 2.43066 | -60.64937 | 2025-03-05 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49ff13eb-8540-3395-bc3f-1edad63ba2ba | 2.2679 | -60.25977 | 2025-03-05 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9165c11-b1ee-3ee9-b912-3ad20b5931a1 | 0.9766 | -60.37331 | 2025-03-05 05:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc724739-dac0-3ff5-b3a1-cdbb0a7d259b | 1.16415 | -59.15454 | 2025-03-05 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5ffc4ff9-2488-3327-b4f7-f56362ffbdf6 | 3.34276 | -61.2479 | 2025-03-05 05:44:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8551bf10-7234-389f-a408-119813e1faa5 | 1.94442 | -60.37234 | 2025-03-05 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc15bae2-ab70-3d95-ae4d-2435c7e9429a | 2.43582 | -60.27956 | 2025-03-05 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f065487b-c03e-316a-be97-94fb0a861b90 | 3.53127 | -60.09361 | 2025-03-05 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 241fe41d-b944-3959-86d5-507dc4d04e4d | 2.35496 | -61.04832 | 2025-03-05 05:44:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17c560f4-5a05-3840-9d9c-a2660bca6249 | 2.62584 | -60.41311 | 2025-03-05 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9e48f169-5e03-352e-9d2a-c611a05413c1 | 1.18135 | -59.15183 | 2025-03-05 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 400c4339-0cbc-32cb-98f3-8f66afde8d2f | 0.87925 | -60.57045 | 2025-03-05 05:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c0c3708-0a05-386b-ad42-3edd1d553556 | 2.3587 | -61.04775 | 2025-03-05 05:44:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad125aa8-d54c-3c79-9460-558e5a2f4ce3 | 1.08437 | -60.67181 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e82f061-6c70-3efc-8cc9-dcbfc9f3def6 | 1.08516 | -60.67671 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b31a7500-782e-38b0-9bef-2cf12e9bd7f3 | 2.35943 | -61.05227 | 2025-03-05 05:44:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df7b6274-dc71-33e0-b1b3-0cde6e4a550e | 1.94522 | -60.37733 | 2025-03-05 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6ac62521-a9cd-3b0a-8e8d-1b0da5b75c8c | 2.10618 | -61.267 | 2025-03-05 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f161257-b130-3b9f-ba3c-97f6f1504854 | 1.13832 | -60.50587 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84114069-dec2-3a5c-83b6-2bd0102974e4 | 1.58376 | -60.20307 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47b8c996-42ce-3960-8894-a4e7feff3ff9 | 3.51728 | -60.10595 | 2025-03-05 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 821af44f-43d6-317b-8b23-6bf32d656516 | 1.182 | -59.15588 | 2025-03-05 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4142053c-505c-3735-8e9c-2f2284d19c42 | 3.2377 | -61.20185 | 2025-03-05 05:44:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6843d53b-da39-3d00-a4ec-3673b8e983c6 | 2.37267 | -60.23585 | 2025-03-05 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68f41d0f-bc77-35c3-86b2-93675abc853e | 1.13517 | -60.5115 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21c71b93-4e28-3643-a05f-cc1659d4f97a | 3.23403 | -61.20243 | 2025-03-05 05:44:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbec6350-486c-35c8-bf82-fd340bf61b4e | 1.76488 | -60.23346 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42b43702-e832-3803-bc59-ab95cde2183b | 1.58322 | -60.19965 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 487f213b-1960-38e5-ad29-86127416d15c | 1.76718 | -60.22262 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8fc8f4b-17d5-3bda-aecb-070d94d81eb6 | 1.17639 | -59.14845 | 2025-03-05 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 52220310-3929-3133-b77d-b696f467ccdb | 2.25755 | -60.77818 | 2025-03-05 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07c4d12a-9bfe-395f-8ed7-070c6b48ac0a | 2.77493 | -60.88692 | 2025-03-05 05:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a5d5e61c-bf85-39c6-98f6-a279f2d1567c | 1.77114 | -60.22196 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50e10c05-c16a-3cd4-bad7-a0e8a7fe2402 | 3.08239 | -60.07706 | 2025-03-05 05:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db0361ad-d143-323a-9ee7-ff19f265528a | 1.3074 | -60.40774 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83c34a48-2953-3854-bd73-7786ce570400 | 1.17705 | -59.1525 | 2025-03-05 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c2555503-f256-3ff5-ad91-df65fec3a303 | 1.17209 | -59.14914 | 2025-03-05 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ca06063-c271-3dbc-b9b5-c69d9657722d | 1.95306 | -60.37611 | 2025-03-05 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bebc540e-696e-3420-a5cc-5b176081aa80 | 1.12808 | -60.51773 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 870d6145-7004-30cd-b948-d5780b7db52d | 1.7717 | -60.22536 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1822d22-94aa-3392-b11b-e34ca33e6f87 | 2.35123 | -61.00135 | 2025-03-05 05:44:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7f382d35-86a5-3cbf-8c30-269b440c9b0a | 1.1383 | -60.50895 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbf9c3e1-b816-373d-8e06-92f7ba291aa6 | 2.35197 | -61.00599 | 2025-03-05 05:44:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f9c2edc4-41c4-398c-b988-9cb88ba7fa1e | 1.13438 | -60.50649 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 352c9bd3-445f-3bfb-acb4-25e7340c409d | 0.97606 | -60.36989 | 2025-03-05 05:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edc675a4-7d09-3bb7-ac40-22732977d2c6 | 2.86132 | -60.74839 | 2025-03-05 05:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a61d4073-6170-3dc6-b360-9b822ccae7e0 | 1.28472 | -60.08159 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 624daf17-2d53-3284-b1c5-febbef673632 | 3.31441 | -61.21172 | 2025-03-05 05:44:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7e55d99-f4e9-30f9-abab-1eb3259fe31d | 1.1273 | -60.51272 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 575a5cc6-ac7f-3c93-9a2c-ebc6fe288003 | 3.35076 | -61.25102 | 2025-03-05 05:44:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7dd48e14-cfc2-3caf-bb85-d9500392e881 | 3.54528 | -60.08124 | 2025-03-05 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9345cc69-1da5-3d56-9cbd-9d673d98794a | 1.97188 | -60.31703 | 2025-03-05 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19f2a09f-9565-3bad-aaff-c6ac5f47aa74 | 1.94835 | -60.37172 | 2025-03-05 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5aa436c6-8cda-3a4c-8057-2b598219a4bc | 1.94914 | -60.37672 | 2025-03-05 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e79da9d4-edfc-3b58-a1cb-ab9f79b5a90b | 1.28068 | -60.08222 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9901809-12c5-35d7-b0e3-c49be29126e0 | 3.31075 | -61.21228 | 2025-03-05 05:44:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f48b84ad-d832-3845-9e61-38415aedc521 | 2.10327 | -60.23646 | 2025-03-05 05:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2e4dc47-2c5c-3d35-b4bc-604354c24822 | 2.10408 | -60.24142 | 2025-03-05 05:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 012ad139-84cd-36e4-a0f3-7ae375676274 | 0.41849 | -60.5029 | 2025-03-05 05:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bfe843dc-3bf0-3a5f-95a5-f050bd8d7abd | 2.43503 | -60.27471 | 2025-03-05 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4aad05ed-8f27-3305-a8b7-7e239d5c9aae | 3.35007 | -61.24676 | 2025-03-05 05:44:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75a5deae-5a8e-3a2f-9999-48d962acf79a | 0.73065 | -59.36118 | 2025-03-05 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fe6a0c3-54ac-38a9-bddc-dca13db54792 | 1.1391 | -60.51087 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f945635e-870c-3bbf-bd49-057e3651b59c | 1.93984 | -60.39389 | 2025-03-05 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0be43d22-e389-30d3-89e3-673ed07afc21 | 1.93667 | -60.3992 | 2025-03-05 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d6cbd5f-a154-36dc-a131-967df094e680 | 1.16781 | -59.1499 | 2025-03-05 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b78a525-dd4c-3117-9e8e-8139b69afef0 | 1.16352 | -59.1507 | 2025-03-05 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 59fdc9a8-d4dc-3dbb-ba0e-ff4287a15ec0 | 3.34642 | -61.24734 | 2025-03-05 05:44:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5388f51-6b6d-3b80-82e3-df4cb1db5c50 | 2.35274 | -61.01075 | 2025-03-05 05:44:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 170cccc5-7851-353e-929b-c11984b31136 | 2.77566 | -60.89144 | 2025-03-05 05:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 16d4020c-8028-30f9-9abb-00bf0a39c9b2 | 3.56959 | -60.2326 | 2025-03-05 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47203bdf-7e49-3e56-b4d4-bd6d559007c4 | 1.13045 | -60.5071 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17bfade7-c92d-3c5e-a815-74776ee8bc7b | 1.65013 | -60.29428 | 2025-03-05 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a33c98c9-9b5a-3abe-9078-219f47a4d0ab | 2.84076 | -60.83628 | 2025-03-05 05:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ff28acd-b4ca-3b2b-b6ef-090fd5c7e68c | -20.91376 | -55.55341 | 2025-03-05 05:50:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ab70f57e-6ead-3768-8427-48ccb04c5a95 | 1.94824 | -60.37761 | 2025-03-05 06:39:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9f252f87-9795-3f3f-85c2-5ace3d8a09ce | 1.16304 | -59.14894 | 2025-03-05 06:39:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 14.5 |
| ab6c8bbe-e8f1-3171-88c8-8ed90cb3ed6b | 1.94688 | -60.36863 | 2025-03-05 06:39:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |


