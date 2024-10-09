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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24ca4111-3a14-3454-b4e7-d2c14aae655b | -21.6745 | -47.7252 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 30.3 |
| e580fd12-768b-3fbf-82b0-18d6cce7878d | -21.67378 | -47.73072 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 4489befd-5edd-3b88-b374-91cd0d2c3459 | -21.6735 | -47.71022 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73d65ab3-e68f-3147-8a64-c7344fd63000 | -21.67282 | -47.71578 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbe37c50-90ae-3a52-9f4a-e3542b0a0900 | -21.67262 | -47.70815 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 76b34511-fac1-3be6-ac6e-c4645a661725 | -21.67213 | -47.72137 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b3d7973b-6df5-35b1-9fe8-e6112ecbde88 | -21.6719 | -47.71366 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| db78ceea-d470-3eda-965b-cd83f6f177f2 | -21.67146 | -47.72687 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b5ad201b-b552-3183-a83f-d20549993ad4 | -21.67118 | -47.71925 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d64d8ba2-9395-3728-9351-be9f73246182 | -21.67078 | -47.73241 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b17d37ae-7b4b-3671-a67a-1526ab964a2c | -21.67047 | -47.72475 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 857cc86d-2103-390a-8b51-cbaeefed32fa | -21.67014 | -47.70428 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6e9fe6c-75c7-3226-9df5-cdde8f256740 | -21.67009 | -47.73804 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ffc056a-1ddf-3151-934f-e5d4d7ff6986 | -21.66976 | -47.73023 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 5e6902b8-efdc-3575-a388-6ce485d0f22c | -21.66947 | -47.70977 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b645b6d1-5c5e-3486-a5cd-1ed63e335bdf | -21.66904 | -47.7358 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b2a1157-f232-3cba-b270-6191d3794047 | -21.66879 | -47.71532 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e82102e9-45fc-38e6-9bc9-a60d5d5a04ab | -21.66858 | -47.7077 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 83fd4b83-670d-31d6-b56c-f8b25536a9c7 | -21.66811 | -47.72091 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 330.3 |
| 9d6d6454-374c-32fa-818a-e0021a4164c2 | -21.66787 | -47.7132 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 45e7742a-b010-3fd6-b533-301d05dec7ac | -21.66744 | -47.72638 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 330.3 |
| d2a2630a-f186-363f-9706-7bb812d0e585 | -21.66715 | -47.71878 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 60.6 |
| c99cb310-1aad-3076-9ea3-8e479ccb4217 | -21.66676 | -47.73188 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01719871-1b0d-3bde-a0f7-81ed2265370f | -21.66644 | -47.72428 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 454.1 |
| 01dac2e9-714b-36d4-9d7a-a42d862eb11d | -21.66612 | -47.70378 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c15dfbb3-aa3a-383c-92f7-228972f0aee2 | -21.66607 | -47.73749 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bec42bb3-fd1f-3e61-900d-b99e4c21360e | -21.66574 | -47.72972 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 454.1 |
| 18d47e26-57de-3058-ad00-1ba8b3a8a8ec | -21.66544 | -47.70928 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c31b3f47-0a23-3eb6-a134-2211034331ca | -21.66527 | -47.70169 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67a071d3-1316-3f53-845e-b2fc6c89007e | -21.66502 | -47.73526 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4057c9c-0eaa-3de8-820d-77ae00258474 | -21.66477 | -47.71483 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a4850627-6db8-3162-8bf5-bf8e1ce80356 | -21.66456 | -47.7072 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8133c8a2-6420-3101-af5e-64e521ce6589 | -21.66408 | -47.72045 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 330.3 |
| 6b55a838-b20b-384c-a40a-431e8a72f5c4 | -21.66385 | -47.71271 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 6370076a-b92e-3048-9e75-f166da2d8709 | -21.66341 | -47.72588 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 330.3 |
| 7470d59e-f0de-3b89-bdb6-2fcbfe6d7ff1 | -21.66312 | -47.71831 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 5b8686e7-bcdb-3151-bf94-a6f6f3614b3a | -21.66274 | -47.73136 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e47fa992-e6e8-3213-ab9d-0fe40f80f5d8 | -21.66209 | -47.70326 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5fda04a2-3633-3574-8564-90f6cd310332 | -21.66206 | -47.73692 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76ac3602-f1a3-391e-a6ad-02de015fe5c7 | -21.66172 | -47.72921 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 454.1 |
| c5340150-a9a5-3e2e-b0f0-83d57bdc7ec9 | -21.66142 | -47.70878 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 47b00ac5-b398-345d-8d76-790146ea9ed8 | -21.66124 | -47.70117 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4eeb66d5-73dd-386f-9c86-9f1c88f287a4 | -21.66101 | -47.73474 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6abfb5b7-d4fc-39ad-ae6d-090f80fcc62e | -21.66074 | -47.71433 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 74a8b91a-6191-3517-aeec-0b6a5010ebd2 | -21.66053 | -47.70669 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0df9b7c1-c5c7-3e9c-a788-1d9609623432 | -21.65982 | -47.7122 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 193.6 |
| bae58bcd-40f7-3026-8d97-d820b6c1c650 | -21.65939 | -47.7254 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 442.0 |
| f41dff08-3276-3bbf-924a-fc9a74f1f7cd | -21.6591 | -47.7178 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 193.6 |
| 4ee378b3-7bf6-3607-b981-d70979a71333 | -21.65872 | -47.73087 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e1eb48c1-db20-3282-8a99-8fcf9f32d5b3 | -21.6584 | -47.72332 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 221.6 |
| a9376e21-9cc9-349b-be1c-9574c40f7f48 | -21.65807 | -47.70271 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f5583109-f1f1-3713-b7af-24e84f8d43d2 | -21.65805 | -47.73638 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 619425d4-9d38-3b32-bba0-70598f7c4f77 | -21.6577 | -47.72874 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 221.6 |
| a13c3420-d81e-3d45-ad34-a0d912b9c85f | -21.6574 | -47.70826 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 7d2f6793-f812-3f07-a920-972aa2171fb0 | -21.65699 | -47.73423 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae292c12-362c-354e-92f0-e9ab2c17a02f | -21.65672 | -47.71382 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9a21802a-ab60-313d-ad2e-8ea9563c8e38 | -21.65651 | -47.70617 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bad99d9b-437a-3ecf-b936-3776822da354 | -21.65604 | -47.71943 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 442.0 |
| 7927f0e8-fdb3-38fc-b215-8ab2b4ecbfd1 | -21.6558 | -47.7117 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 193.6 |
| 1b52849b-e595-37b1-939d-3a673ee94b35 | -21.65537 | -47.72493 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 442.0 |
| 69c53dff-8869-3e39-b5dc-ff560259b82c | -21.6547 | -47.73039 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| be1a55c8-9a3b-3138-8b3c-c3bfb574d7c9 | -21.65437 | -47.72282 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 221.6 |
| f4ba4b79-51d6-3808-b232-006acf0d5fa5 | -21.65403 | -47.73586 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d2cb014c-2610-3dd7-86e1-483e009bb464 | -21.65367 | -47.72829 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 221.6 |
| 6ec6ee35-e495-378a-9d9f-f40afc39e5a2 | -21.65297 | -47.73374 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddac0b86-9924-33e0-9aae-698f5d077b34 | -21.65249 | -47.70563 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 985134a8-7b42-3c4e-a920-9118a05f1113 | -21.65178 | -47.71116 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 22.0 |
| a533c7b1-8d7b-3e31-af04-2f6189cfa974 | -21.65107 | -47.71675 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 556a50a7-13e6-39ca-96ab-e55732970c94 | -21.65035 | -47.72233 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7dcaedb4-775e-3bca-b4cf-b47364c0194c | -21.64964 | -47.72782 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8cd97b45-3fa3-380b-8693-a5037e7ea214 | -21.64918 | -47.69954 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0673ee7c-d733-3f31-9714-a52018bd789d | -21.64895 | -47.73328 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eccc90f8-7334-36fb-81f5-04f349916d55 | -21.64847 | -47.70507 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 05467fdf-da88-32ce-93ea-aa8246115d5d | -21.64776 | -47.71061 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 22.0 |
| ace8bfc7-534e-3347-96e6-b0b0e1df062f | -21.64705 | -47.71621 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 235fc591-7235-3305-b7a4-c61ad019f625 | -21.64633 | -47.72183 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d37bfd33-cf58-3668-97f0-64acefabd071 | -21.64563 | -47.72732 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 379acb64-4dd8-3cab-a1db-47e8de16e35f | -21.64375 | -47.71004 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5e2ac2a-9692-3cd3-bfeb-fde675439b9a | -21.64304 | -47.71561 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d62d3409-3b29-3496-b00a-ff4044886e2c | -21.86034 | -48.40208 | 2024-10-09 04:42:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fef85469-c49f-352a-8203-686cd3c6bb54 | -20.77742 | -48.56117 | 2024-10-09 04:42:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6682674c-ac73-38e9-864c-8067a941f8dc | -20.74339 | -48.55622 | 2024-10-09 04:42:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3a67ba2-6d39-3a5c-a1c8-9c78f227f27d | -20.60903 | -49.35925 | 2024-10-09 04:42:00 | NPP-375D | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 916e7c49-6085-347d-94a9-69e29e8ae983 | -20.59495 | -49.35029 | 2024-10-09 04:42:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c34ee632-cfca-3705-a052-972b7dbc8546 | -20.57506 | -49.33376 | 2024-10-09 04:42:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d9173d7-8798-378d-add7-174ac8618bb0 | -20.56838 | -49.35511 | 2024-10-09 04:42:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83c88089-6016-39bf-8b5f-55f548f22488 | -20.56413 | -49.35901 | 2024-10-09 04:42:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c59fa559-c55f-39d4-8d6e-bd9de29ed3ad | -20.56113 | -49.35402 | 2024-10-09 04:42:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 979702bc-2f80-342d-a734-2e375d4988e4 | -20.55388 | -49.35292 | 2024-10-09 04:42:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 315bb6c3-43ee-3107-ab5b-2de7d51c8fe9 | -20.55026 | -49.35239 | 2024-10-09 04:42:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 405a8690-8fcb-33d9-b342-43670e3f430d | -20.40979 | -48.83662 | 2024-10-09 04:42:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a00711f-d9cf-3612-94e8-75a6cfdaf7dc | -20.40608 | -48.83602 | 2024-10-09 04:42:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 710d0fb9-a909-3ba9-b89d-af83f593e287 | -20.40545 | -48.84064 | 2024-10-09 04:42:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02b28167-05cf-354e-bd4e-96472aedff50 | -20.36407 | -48.72512 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7a04258-cb6a-3e8a-b3a7-602433be1fdb | -20.36345 | -48.7298 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71c0fb66-1298-3bc1-a13a-b9da3f992dfd | -20.35972 | -48.72925 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 13113a02-dc6b-38e8-86e5-118adef25874 | -20.35599 | -48.72871 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 62243458-e722-349b-93b7-7f8bf27734be | -20.3529 | -48.78073 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 363954ed-5268-3d57-b468-ab5fa4cc49b4 | -20.35242 | -48.72158 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6940746-59b7-3c5f-acf9-7a8d816e07ff | -20.35226 | -48.7282 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README156.md)
