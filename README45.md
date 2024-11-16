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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92c9bad7-c8f6-31fa-b6ba-03b08ce6b0e1 | -2.9768 | -47.98986 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a544fe23-5281-3f3f-9d04-ce0e308bf803 | -2.1931 | -46.61694 | 2024-11-16 04:48:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b09c4eff-bc62-3d50-bf54-5e39e48e98bd | -3.56286 | -47.37343 | 2024-11-16 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed0ef668-f38e-3b6e-bcae-9eacc5d4239e | -1.8567 | -46.28333 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 218e96ea-52ff-3fd8-a2d4-e269f35584dc | -1.64551 | -50.46966 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79e3ddf9-1f50-3dd9-bc40-0b79b696946d | -1.5816 | -50.44607 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1a942b3-518c-3ffc-8692-f4c59dfbb689 | -2.35362 | -49.11297 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e14a3da0-25d5-34b4-8ac8-c6a539d33170 | -2.3933 | -47.92678 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 695495aa-5213-31b5-bf43-bcde3a45f263 | -3.52151 | -44.71523 | 2024-11-16 04:48:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c7bf5b21-8dcc-371d-a215-0dc38f165585 | -2.64716 | -48.48204 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9b6bb751-bf27-31cf-bad7-06072874d35f | -2.03415 | -46.37381 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0e21631-3756-339e-947a-dd158e49ccd9 | -2.66212 | -46.83904 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac9676c3-3b0e-3f86-b3b0-e3d0aa1c367a | -2.28189 | -50.63631 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 125bcfd5-fd8d-37cb-b614-8fa9c8d314ff | -2.09801 | -46.58556 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b87152ea-27e6-3110-89ef-f2856f7c7d2b | -0.26387 | -48.51245 | 2024-11-16 04:48:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f7fb08e-8eaa-3947-a5f1-291553b2845f | -2.15727 | -50.51996 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0abf70cf-49b6-3483-9a8d-1d76e432cc3e | -2.13523 | -50.81391 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a3b27de-769a-31c7-aaa6-6662dddd999f | -2.54977 | -46.89258 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03010404-0160-30d0-822a-7bcc29b09e3e | -1.23392 | -53.7061 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f0ad720-042f-3094-8f40-85827855840e | -2.46638 | -44.84103 | 2024-11-16 04:48:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1447231-29a3-3c83-a7ed-2493ee478ef7 | -3.94639 | -46.71287 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17a3cfe3-9ddd-36bd-b430-b671658a9773 | -1.55733 | -46.09216 | 2024-11-16 04:48:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 847c6b82-eb87-3555-a562-8789b05f65e2 | -2.56163 | -53.99679 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33e1afd1-a5a4-322e-8bc1-828d66d43ff1 | -2.3842 | -48.53894 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f696dac8-719a-3868-8f20-9783671a9445 | -2.18976 | -46.60674 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0e5e4b33-1459-39c8-9139-86d33a37d7fa | -2.14188 | -46.40517 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fee98dd1-149f-3f00-9846-031ecd16ba6b | -3.88253 | -45.02478 | 2024-11-16 04:48:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d7f47c55-e1f6-3328-99da-52f2bfa1e00e | -1.24823 | -47.46922 | 2024-11-16 04:48:00 | NOAA-20 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24a9e3dd-4c02-3042-9736-9b875d7b25c6 | -2.63843 | -46.53479 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0ca71c7-7ee6-3e70-9eaf-3d9f61bf899b | -2.20373 | -53.71472 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 51e86ede-604e-37fd-87c0-a3c9a1817167 | -2.22656 | -53.61547 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de991a5f-13e3-36e1-ab1e-ade7a4c8469c | -2.74298 | -48.56411 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 071d13d4-e2b8-3f8c-80b6-075c46c2a58f | -3.98176 | -43.72457 | 2024-11-16 04:48:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 295b42b7-d566-3ebc-baa2-750e129f74bc | -3.06551 | -45.34924 | 2024-11-16 04:48:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5dfd86b-7165-3e33-bffe-e0289f4c33d4 | -2.2395 | -49.00532 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f836666-9d1f-38a2-af9b-8ae9c5fa9af8 | -1.64213 | -50.44757 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b588a2fd-9b73-377c-aad4-0698a25287f9 | -2.65657 | -46.17245 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3df2c558-59cc-32dc-9208-8e62a5b4fe81 | -2.55343 | -54.03521 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea8b0634-2115-33e0-ac6d-943e4acffbe6 | -2.55487 | -54.0387 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6a25cdef-36fa-3404-b813-1d5985c9843d | -3.90731 | -47.16479 | 2024-11-16 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b968a1f2-ac08-3be5-aa7f-44d9b8f559d9 | 0.66085 | -51.76289 | 2024-11-16 04:48:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aebd5cc2-6c85-3e64-a989-6b66160c1bb0 | -1.22701 | -53.70493 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33b74479-60b5-3f98-9433-706ab9856663 | -2.77549 | -48.5762 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b94523e1-2ed6-3752-b7ee-8094b2c00221 | -3.50538 | -47.2207 | 2024-11-16 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4ad44e7-374e-3168-9d00-1e0c944eb608 | -1.21467 | -53.56429 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 965d8bff-162a-3b80-91aa-d86441ae41f6 | -2.1485 | -53.71122 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e0af1150-0415-31df-8670-911a0f2c9733 | -2.1558 | -46.39615 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5ebb852-ce9d-357b-90fc-694527ea5c2a | -2.62978 | -54.38257 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1eba9161-8e4a-3b50-98ee-1aa5fc0670a2 | 0.15835 | -51.13689 | 2024-11-16 04:48:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d320bf2-a5c0-31d1-9b91-cb4e735df708 | -1.21064 | -53.56751 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd12250c-abdf-35f8-990b-ff43af2f7174 | -2.57223 | -54.42357 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48d3292b-232b-3d20-a1d3-d365da6203ff | -3.73788 | -45.66529 | 2024-11-16 04:48:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 63f524d0-3284-34f0-b85a-9a19b755e93c | -3.0742 | -48.01091 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f603f4f-1f85-3402-b90d-d97952317591 | -2.0768 | -46.47649 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfd359e8-3b11-3222-8fae-491302255fdd | -1.63843 | -53.27721 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fc894b6-bb84-3edc-9aa5-dc6a8d7e71e3 | -2.37299 | -48.91541 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81c460d9-e573-386e-9955-9ea5ad687ead | -2.55666 | -46.90068 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a96215ea-c791-3e27-82f2-1bc6e68e2ed0 | -2.15252 | -53.70802 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cfd7e942-b301-349b-bb49-041a0ebf7ae4 | -3.0402 | -47.97649 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e70e5b3-6a97-3e5c-a8a2-5662b79adae6 | -1.58216 | -50.44256 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 352acde5-aa49-3be0-9ba4-89695964a91b | -2.56227 | -54.00143 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed0d3416-d4f9-3e9e-bf42-7e7b44b46d9d | -1.57548 | -50.44153 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64938766-2d33-3d08-a716-e366501faf88 | -4.39787 | -43.81649 | 2024-11-16 04:48:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cac8499-86a3-3d99-aed3-151c3ff0049f | -2.63449 | -46.55993 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44cc500e-31ba-3550-872b-bccae0509ada | -3.74246 | -45.66468 | 2024-11-16 04:48:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6c37661c-c93d-3c75-bddf-08f37ded25fe | -2.57098 | -54.43148 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1d354ce-205b-35f5-a8f0-c97de89706b6 | -2.94072 | -48.32686 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c019735e-c55b-37fe-82b8-b06c5104023f | -2.07304 | -48.54148 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cce9f74a-6c74-3e21-b2bb-141d5dac68e2 | -2.3868 | -47.94399 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6c858e2-49ff-30b8-960d-ec7375d8ea90 | -3.06978 | -48.01483 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32784cd3-716b-32ee-a8ca-051eda94276f | -2.46152 | -53.92786 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a8622c6-b004-3cd7-aada-5831245dbcda | -2.24138 | -46.83765 | 2024-11-16 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc6741ea-b675-3238-933d-b6e3d8ee4dbb | -1.86387 | -54.27752 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b3696bb-633f-3cc2-9f59-a621b9a66138 | -2.64419 | -48.47728 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d3065290-aa00-32be-9b3f-7eef4235cda9 | -2.45726 | -53.97773 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25000257-1985-31cb-82b2-e034f57da3bd | -1.40238 | -51.08975 | 2024-11-16 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 668caf64-b895-35ff-8024-87090df75a88 | -2.97612 | -47.99433 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 605c6174-08cd-3758-b575-a1884bcdca41 | -2.64206 | -46.535 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab0c3111-85f0-3a43-943f-034fd62e94b9 | -2.09694 | -46.59267 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f604c075-dbe0-3465-a7f5-ba92c8f4ca69 | -3.78979 | -43.91329 | 2024-11-16 04:48:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| bbfa9d2b-5122-3920-9f68-7b603dcd32a3 | -1.57677 | -53.80126 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f2bf8d1-ea1c-3f01-add4-b351a604f1fb | -3.73545 | -45.65173 | 2024-11-16 04:48:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e6485ee0-fb29-3cd4-a978-f0dd8dce9e2e | -1.13182 | -54.16676 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a405cd6e-aabd-3df0-8f3c-8fc600e53b83 | -2.22675 | -48.25069 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8408a44c-7690-3166-8a16-3457ac1c7ec9 | -2.67413 | -46.84084 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c1de698-fbe2-3aa3-8591-365545c97620 | -2.3759 | -48.91993 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29804f04-0a98-36bd-a797-746315e0aad8 | -2.18068 | -47.94774 | 2024-11-16 04:48:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9e922c6-dc29-35d6-b547-5cf2b16187e9 | -2.14414 | -48.80447 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68836dfa-0b8c-38ef-bada-ab0193c885b9 | -1.74891 | -50.4823 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62645ebf-205e-3a12-b0d3-14fe1f9bff2d | -2.15955 | -46.42636 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ec19f51-a24c-3d1d-ae48-170d7c347d5d | -2.63856 | -46.56059 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5db03ff-ebc7-345e-970c-61dc2518fbed | -3.92618 | -45.85352 | 2024-11-16 04:48:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98d0651c-f074-3826-b24c-31ec38d500f5 | 0.12588 | -49.85026 | 2024-11-16 04:48:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74d2e1fe-f497-3929-9de0-9510efc50e7a | -3.50259 | -47.2179 | 2024-11-16 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e79ba03a-b63f-3660-8b7b-cbb152f43126 | -1.0897 | -53.17823 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08c10648-51e2-3c62-af3f-61d1dba7da54 | -1.71395 | -46.16112 | 2024-11-16 04:48:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87126619-bd98-33ea-8067-d2e3d63f5f39 | -3.89519 | -46.47553 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0420bb1-ec50-3cbb-a80e-3779a0610960 | -2.96117 | -48.04259 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45126f8e-4268-37e3-b39a-f85a0d526a3d | -3.07352 | -48.0154 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d591e42f-daac-33ed-ba39-74c367dd08b7 | -3.36984 | -47.32412 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README46.md)
