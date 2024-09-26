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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a98a56e2-bb79-3cee-960c-22a20f2095e3 | -11.31188 | -54.9424 | 2024-09-26 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c75cd8f5-9fe0-3813-b135-d0d871c53d37 | -11.30858 | -54.94188 | 2024-09-26 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 167d1b0c-9432-3270-9dc7-67f796e86842 | -11.22244 | -54.7954 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4604e095-09b4-3e1a-b2d3-30bb24ad1d90 | -11.22189 | -54.79891 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b585c17-c6f1-35fa-a157-51a32a4ec99f | -11.22135 | -54.80243 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 198532da-b2f2-371a-8453-cc14b2d71f60 | -11.22126 | -54.75929 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c20d3a9-f28b-3e18-a823-b5bf699f39e3 | -11.22072 | -54.7628 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 913de0a5-4454-35b1-ba85-f02f09f37dba | -11.21859 | -54.79839 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b59e970-3c53-3391-af30-dd436ed8c964 | -11.21804 | -54.8019 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 975a2aeb-36df-32b4-91a5-0e1b3247eea4 | -11.21796 | -54.75876 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d3ec157-f19e-3580-9817-e7cac38f0159 | -11.21749 | -54.80541 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae617461-9c02-3e7e-9f25-fffd5a01e634 | -11.21741 | -54.76228 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d568758a-b9bc-38bd-912b-5cd1e4429e85 | -11.21687 | -54.76578 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a65134a-d47d-3276-8e93-fdea1e242c27 | -11.32705 | -54.04891 | 2024-09-26 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5735c37-e12f-3d86-8bc9-8dc43003a859 | -11.32425 | -54.04479 | 2024-09-26 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ca5eeba-4ec6-3d7c-9030-03286a3a759c | -11.3237 | -54.04838 | 2024-09-26 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfb56ef0-2a62-310a-b161-856c97f48508 | -11.32316 | -54.05198 | 2024-09-26 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1fab863-5f9d-3c53-a2f7-94f22aba5e19 | -11.31701 | -54.04733 | 2024-09-26 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd0ce91b-eb22-3579-b141-5d0ca26fa649 | -11.27991 | -53.98274 | 2024-09-26 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0af783c8-e065-3a30-ba70-42d6d1bce542 | -11.21959 | -53.97328 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d80d0d8-0c7e-3f47-b857-e70fb40f3d59 | -11.21836 | -53.9361 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bcf1bd80-02b5-3288-b2c9-e2eb55dfd3d6 | -11.21556 | -53.93196 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 316a8283-e6b9-3f77-b195-ad760c6e51ca | -11.21501 | -53.93557 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a31c9e1-4307-3b6f-af28-90b5e41a78ca | -11.21378 | -53.89832 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cea9340a-4e25-3edd-b036-f545f33b1bac | -11.21343 | -53.96863 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ad7b788-9e5c-3c40-ae34-c179524f92df | -11.21288 | -53.97224 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a40d5196-51b4-3eb4-8e38-75ef888ad8a6 | -11.21227 | -53.95367 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| caf4a4dd-14e3-34ef-9f8a-b2759abe7358 | -11.2122 | -53.93144 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b37f373-2b78-3de6-b19e-a57794302e1f | -11.21172 | -53.95729 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e62ddee-c1e7-3679-8a74-f50c0388f33a | -11.21117 | -53.9609 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e1cd969-532d-324a-98f0-d35493e48f72 | -11.21063 | -53.96451 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6847f9af-1de2-3afb-b3aa-b7bc68e8aedc | -11.21042 | -53.89779 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9dd39cb-817d-368c-93bf-eb7a091f1e04 | -11.21008 | -53.96811 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 808719a2-a093-3a0e-9127-f807834380b2 | -11.20206 | -53.90764 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b835586-c2ed-36c5-8d76-7df6023912fb | -11.20151 | -53.91128 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62c16de7-3e1d-38a5-b13a-f7d77be9ad73 | -11.20097 | -53.91491 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99ecee72-9127-318a-bd63-39a56b949842 | -11.20035 | -53.89621 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2934b899-0634-36e3-9409-0acf831a7807 | -11.1998 | -53.89985 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6b55749-c9fb-3654-9241-04f79f0271b3 | -11.19925 | -53.90348 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1d60394-e55a-31bb-94ff-75dfea75d040 | -11.19871 | -53.90712 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a828de2-a422-3245-9de4-ee395dc46e7a | -11.19816 | -53.91075 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 21c1b27a-2ba9-3734-8aaf-3d2deff85d57 | -11.1934 | -53.98766 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e414c2eb-881d-39e9-a168-b524aa024a03 | -11.01108 | -53.93702 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34336865-aed5-35a9-96c3-147229c72063 | -11.00773 | -53.93649 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28c95a6e-260c-32cb-a032-d04e50ad814d | -11.19761 | -54.78069 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d585977e-e546-3a4b-8d89-d11cdc78ec68 | -11.19707 | -54.78419 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a0672374-709b-3f17-bf22-2eea041bfac4 | -11.19703 | -54.76262 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7ae4d757-f62c-379b-981e-63a8f82570e0 | -11.19653 | -54.7877 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4b9228bc-e6dd-3a42-8ac0-763b2f4a8455 | -11.19648 | -54.76613 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e5c4a7e2-5410-3464-b351-5bb7d33c85aa | -11.19594 | -54.76965 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3d303081-18dd-32d4-b01c-212a96b31dd5 | -11.19539 | -54.77315 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4b64583-d1b1-3341-9ac6-b0b23b66ec39 | -11.19485 | -54.77666 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cb5f3f23-a6ea-30ca-9e4f-8c2730c66591 | -11.19431 | -54.78016 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 03ba47d0-69d9-3505-97ba-2940a07bd5c9 | -11.19376 | -54.78367 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6646094b-7c82-3819-a211-811423776c86 | -11.19372 | -54.76209 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07b971b7-dbcf-32f5-b618-d7acd47d5772 | -11.19317 | -54.76561 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a48d8574-a428-3a7c-9119-2e1d31daec93 | -11.19263 | -54.76912 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b33116e5-086a-334f-8217-9403f9bc95cc | -11.19209 | -54.77262 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46ed8cc1-ed58-3aa6-8255-a3e1907f23a9 | -11.19154 | -54.77613 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78c205e1-1ed2-3703-b2cc-283f12de7fd3 | -11.191 | -54.77963 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 284b518a-49b1-376e-90a1-2e2b9b4eeca7 | -11.19046 | -54.78314 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 735f878b-b345-3855-9d6a-f7126ee6407e | -11.19041 | -54.76157 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b39cdda-3ab9-3bd6-bfc1-1e10f6167e73 | -11.18987 | -54.76508 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94adf644-2048-35e4-b9ad-0e985a0ae40c | -11.18932 | -54.76859 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ff3e369-45ab-30c5-aec3-ebd1ec122288 | -11.18878 | -54.7721 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8c2eda7-c998-3d3b-8d9b-7aeb611081de | -11.18824 | -54.77561 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95fae732-5f96-3351-a923-8d213c492b07 | -11.1871 | -54.76104 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ee154f7-7df2-3559-b540-3317c8ae4d96 | -11.18656 | -54.76455 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a7b482e-7282-310a-a8c1-4ac0c18dbea2 | -11.18602 | -54.76806 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 006436e4-1f62-3144-90a5-88b87c12afb3 | -11.18547 | -54.77157 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 159a0c43-ecee-357b-8507-3e118acc2f17 | -11.18379 | -54.76051 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 45367257-fe40-37d1-a57c-e02b5cec8c98 | -11.18325 | -54.76402 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 12f59862-05f2-3040-9a63-111787b8c4fc | -11.18217 | -54.77105 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ed28d86-c28a-3206-8899-b46df98cf6ba | -11.16007 | -54.3631 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 660ebeac-e7d9-381f-8a05-2d95703c94bb | -11.15952 | -54.36665 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 106bbde1-a41c-3e7c-963a-cc60e8a5bd15 | -11.15233 | -54.36914 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e8b1bac-f722-31c1-be95-52b542c3fb9e | -11.15179 | -54.37268 | 2024-09-26 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e5b0e51-73e7-39a1-b11b-e829b4880034 | -11.87555 | -55.44997 | 2024-09-26 04:59:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b075fd79-e08f-380b-80e4-02348657ae6c | -11.21473 | -54.80137 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e1946b9-9f1e-39ef-bdc9-37875d4ba15c | -11.21419 | -54.80488 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1694be28-ccb6-3f40-a33b-8f5870de7d22 | -11.2141 | -54.76175 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26b4c85c-5c52-3768-a2ab-e9cc53c06613 | -11.21356 | -54.76526 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4304bff-59a5-3bd4-96c1-bc980861afdc | -11.21302 | -54.76876 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0da4bcf0-5b1b-321e-877d-162045c3b4c4 | -11.21252 | -54.79382 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 509a6673-89ef-37fb-b575-43421de1340b | -11.21247 | -54.77227 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 317e3996-2d83-33bb-b331-1c48f25977d9 | -11.21197 | -54.79733 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de995cb7-b0b4-39fa-aac4-2efb31d08c84 | -11.21193 | -54.77578 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| a37d834b-b8b8-32d9-a3d4-91eb051a2552 | -11.21143 | -54.80085 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91c8463b-791b-3d4f-940c-19050f593ae0 | -11.21139 | -54.77928 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 67a9a387-a520-382a-8960-424a851c61a3 | -11.21088 | -54.80435 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4395991-bb68-3461-819c-47f5366eaf10 | -11.21084 | -54.78279 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| dc46437f-ee81-3d5f-befb-2d23609d5ea1 | -11.2108 | -54.76122 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb6e6f5f-f57e-3d33-bb6f-ac3e3f408e9c | -11.2103 | -54.78629 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 93c28ce6-7ece-3bf1-b942-6e6c0ce4e467 | -11.21025 | -54.76473 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 825f41ab-586e-380e-994d-26f35dd0856f | -11.20971 | -54.76824 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a24ba8f0-603e-3dbf-a405-7f105741690b | -11.20921 | -54.7933 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6163fc41-be50-3b9a-bffd-9fb3c61f2a2f | -11.20917 | -54.77174 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| aaf49bfa-0f6e-3763-9391-50863e618105 | -11.20866 | -54.79681 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee3b58c6-6fe4-3e68-b0b2-646c88da6f49 | -11.20862 | -54.77525 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 80fa25ba-79ff-3c6d-94d8-3e25bb7d1b91 | -11.20812 | -54.80031 | 2024-09-26 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README128.md)
