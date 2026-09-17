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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e44c4cdb-2182-3fbb-b15d-aa02d12ba687 | -7.08127 | -41.78109 | 2026-09-17 04:40:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ff06ae46-d3a5-3895-a2fc-7b466c89a256 | -8.14248 | -44.86279 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 91c73672-2b6a-3021-8db0-0c0cb1669e09 | -7.94266 | -44.83429 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 390eddae-08db-392e-9d56-9923dbe97a15 | -8.53349 | -44.53144 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 323c8532-df7a-3a2b-ac76-a36c168bde8f | -6.65946 | -50.92098 | 2026-09-17 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06ad5487-728c-3e59-a43d-1addec3c86cd | -7.07952 | -41.77925 | 2026-09-17 04:40:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6e8d5df6-8c69-34c5-8851-0ddd2ae277be | -8.9488 | -44.39868 | 2026-09-17 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 343be1b7-6388-3738-b406-dc4aaefd5fe0 | -9.10761 | -45.72314 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 6851e0ea-742f-3969-a270-ae2d2abf833d | -9.11483 | -45.73596 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 39aaafee-acc7-31a4-8583-da87856a9baa | -8.61022 | -44.50059 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6cf8af9a-81c1-3e50-abc3-51f526cd4e42 | -7.08367 | -42.09153 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ab24978a-708f-34fd-b2e5-0777a8957a1b | -7.1362 | -42.16975 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f7818f14-46c9-33a4-9bb9-35e9af161651 | -7.13588 | -42.17395 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c58afde3-9e2d-3781-b85d-a62827e6e377 | -8.86551 | -46.9878 | 2026-09-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6d2d9299-e02e-3d22-9df3-9c4eed4fcf3e | -9.83786 | -48.36811 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d676bd5b-cca6-3bb2-a8bb-699c39353ee6 | -11.58657 | -46.87696 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48b9f3d7-75ca-3d4f-8ac5-276ab1b3ab0c | -7.14366 | -42.15387 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d2451f59-21aa-3cab-bc2d-fe1810dc298b | -9.57587 | -46.57458 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fa5db79b-7393-3ffd-ad0f-562f5146e896 | -9.61768 | -45.34447 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d8ed4690-570c-3fa7-b433-9989f039163e | -7.02903 | -42.06457 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| f34f69c8-3b03-342d-9258-7d9491009dfd | -9.57215 | -46.57397 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70720c97-69b0-3566-aa68-6654ff9b55a8 | -8.53393 | -44.49736 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ee2a8ed0-46f2-3339-8d1f-1de2599a62d9 | -10.01474 | -45.49449 | 2026-09-17 04:40:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb4200f6-a8ad-3fd4-a779-2b724059aba0 | -7.94672 | -44.8348 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 0e80bf66-7123-39f0-93c3-dea04375f416 | -5.98322 | -53.58518 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c92eabfa-6f2a-3227-b515-54b59224fd82 | -8.85833 | -45.86579 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d2bdaf2-d48e-3dea-9173-9806e48c574c | -5.97945 | -53.58448 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80a9b815-bffc-3080-9ff4-e357715f1edc | -7.61832 | -46.69286 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2a59eea-c184-3e16-9e87-5f71c3d0d826 | -7.01965 | -43.3833 | 2026-09-17 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 33ada750-0274-31b8-9064-6c30e0166e3a | -4.61146 | -50.92315 | 2026-09-17 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb668968-5018-30c7-9266-bc31477e712c | -5.64865 | -44.80436 | 2026-09-17 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1927f6c7-a8e3-37c5-be2e-1f11de5fef65 | -9.62376 | -45.35962 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9f6dd246-892d-3d0c-af67-c14266f43627 | -8.47158 | -44.56723 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fea5aa2-2256-393a-b37a-c44b53a08868 | -8.14302 | -44.85909 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5e5b750a-46a5-3455-a9eb-f617ea34af99 | -9.11303 | -45.72038 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 15f0dc49-e995-36d5-9cc1-318792cd815a | -6.67593 | -43.64681 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ec8f13b9-314a-3aba-8a07-72880a812568 | -10.78509 | -46.1957 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1c4dc216-2fdd-3715-af5f-fe35b01b0189 | -8.88016 | -46.91299 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 007d49dd-d447-3b84-be90-1e4e3cf46d42 | -9.62327 | -45.36316 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 24414e43-9616-3e0a-9cab-a47cb03c9daa | -7.08716 | -41.84881 | 2026-09-17 04:40:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 5af11e1f-627f-39f0-9d70-89c6848cbbe1 | -6.10659 | -57.62843 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b119800-57f1-3fe4-8b8e-8638db7c48e3 | -6.3092 | -55.15178 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b5e0cc21-69dc-3a9a-9f53-0ea5febf653f | -11.57283 | -46.86574 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e35e7b65-33c9-3618-ba44-136a7768f22d | -8.3298 | -51.30823 | 2026-09-17 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b76c3ae-a8ea-3a46-9e9c-f75acc993cb7 | -7.52888 | -49.49915 | 2026-09-17 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6024c281-ff16-32d8-b797-88ace5de359f | -5.75294 | -57.59062 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55991262-20c3-3e8c-b1b6-4098526aa1d2 | -8.43103 | -47.74861 | 2026-09-17 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 518a72a5-3149-3f73-96c0-218022d4e4e6 | -6.75916 | -55.84454 | 2026-09-17 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d84189a2-b7ec-31d7-b07a-d94eccc4683f | -6.90183 | -59.02795 | 2026-09-17 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 772887ab-9ae5-3353-b5de-88cc31ae2c7d | -7.72222 | -42.49985 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 68b08523-7539-39c7-aac8-b11415337167 | -8.4858 | -57.6465 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f3cfff03-579c-3cce-8938-e9a8fb47e656 | -11.89089 | -43.81778 | 2026-09-17 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f03da9f3-5c7c-3478-ba48-bba47dacb5ab | -11.89548 | -43.81845 | 2026-09-17 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54b2ef2a-dafc-3863-a25c-60353e696dda | -7.17514 | -42.10006 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f0ac3f91-40ba-3267-a0ed-1c533474c901 | -5.86626 | -52.05564 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e89ccea-f9ff-32b5-8b3e-0fd934ab9463 | -9.77255 | -46.09379 | 2026-09-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c13e4229-58d7-3d99-acc6-9af2f0c096e3 | -7.03356 | -42.062 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a5fa8e99-f90b-3770-9727-8bd304cf6cf5 | -8.8595 | -46.97845 | 2026-09-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0fa058c8-36d4-3f0e-9240-2b303d6f5a23 | -8.56227 | -44.47739 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7032f84-3e14-32a2-aa65-bfa2ec16859d | -10.90099 | -48.36112 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd1593ea-25b9-36e1-813c-60e698451a33 | -11.32658 | -46.7713 | 2026-09-17 04:40:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3db139f2-f2a1-3a91-bbcb-5d7b0beb6599 | -11.56652 | -46.88348 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 12f58141-5acb-3ce3-ae8b-99e1da096487 | -10.57725 | -57.69236 | 2026-09-17 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 458af2a7-6956-375a-b5b3-453bf4061a0f | -8.85891 | -46.98251 | 2026-09-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78394c28-8c16-309f-9c1b-87a3f436304c | -8.69433 | -44.87069 | 2026-09-17 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f6b7fb8-8f23-342b-9ebb-f833e3af13e1 | -9.56716 | -46.58228 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d969869-3fa7-39a4-912a-776e1c547473 | -5.11615 | -47.62138 | 2026-09-17 04:40:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56b49a95-0cce-301a-b49b-1b0e1b632a38 | -5.97537 | -55.35971 | 2026-09-17 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e89df68-10ac-3c4e-aacd-896b149466de | -7.58794 | -46.13805 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4eb18a02-fee4-3d04-bde6-7bce41306dbf | -12.5228 | -45.96265 | 2026-09-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09a24c4d-699a-3c0f-823e-9f8840dd16bc | -8.47214 | -44.56325 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 11bd5a85-e3a3-3f1f-b8b3-56e3e2d8db1a | -4.37955 | -55.03351 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5085c6a3-4326-39f4-a142-8372e7e442ff | -8.57091 | -47.29383 | 2026-09-17 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fbba4ae-9ae7-31c8-8cf7-e1a53f2af430 | -9.84428 | -50.50795 | 2026-09-17 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8b35012-1854-353c-b8a9-c8f0a91c2952 | -8.61299 | -44.48118 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 080646f4-1584-3fbf-887d-f638ffba39ca | -7.03722 | -42.0347 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 75af7683-d8e8-3ed6-bfb3-fe2f5a4ba118 | -9.12315 | -45.72549 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fb146c7a-54a8-3fb9-b7e0-2cf12821a899 | -10.86601 | -54.04378 | 2026-09-17 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c86aee9d-ce22-303a-b1da-0614cab659ad | -5.97737 | -46.63269 | 2026-09-17 04:40:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b99bb668-1a16-392c-98ce-408977cf5a5e | -9.99326 | -45.44489 | 2026-09-17 04:40:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 58a0ee48-d822-3ff7-b9d8-5c7c65963b11 | -8.46849 | -44.55905 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90b6b970-5e2d-3946-8aa9-3d76265bc636 | -7.1152 | -55.12424 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4b50ed99-b36d-3b0f-b731-cd72faec4e8c | -9.09495 | -60.97607 | 2026-09-17 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4483713e-448b-3e4c-8ecc-b2e31a49b435 | -11.48572 | -45.73879 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdb43bac-9ba5-3a82-96de-92a84c7165a8 | -5.82166 | -52.08067 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 579bdcbe-1545-3890-a3e3-6709a69e2620 | -5.98699 | -53.58588 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b22630e-df75-3c83-ba0b-df06d9e7b18a | -7.38443 | -44.49468 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| efa2634d-d135-3dc8-b889-9fd0b84bdc6b | -5.88619 | -44.96284 | 2026-09-17 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb2e469a-acc8-3b9d-90b5-938c5982c9b2 | -9.45992 | -45.45012 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b91b37b3-cdf0-33c3-af8c-f3defc869faa | -5.76172 | -45.10195 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 957ea172-17e7-329d-8859-01c55caf88ff | -9.5678 | -46.57784 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0fa1387-0a20-3f4a-bcd4-01934dad1819 | -3.48991 | -54.71356 | 2026-09-17 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7378eaaf-aa65-3474-8efb-182dbf59dd45 | -7.03363 | -42.03213 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 1d5bda71-2c31-3fa0-870e-42a496df2cb9 | -11.5387 | -46.88207 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 93cf2bf9-6f60-34f5-9ebe-b64fdab61d8a | -8.25868 | -42.17971 | 2026-09-17 04:40:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5b1912a4-5799-34b3-96aa-507fc6f1cfb6 | -10.46408 | -50.95833 | 2026-09-17 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 201398ea-97f2-3b53-8278-134135880b81 | -12.32521 | -47.95543 | 2026-09-17 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88e56732-12a2-31f4-8bb5-1065864929ef | -10.39879 | -46.63048 | 2026-09-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e20cf71-7300-3de0-85e0-e3dd70968d60 | -8.58839 | -44.56446 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dbc8bd7b-839c-378f-ad50-abdb73b59401 | -7.94553 | -44.8187 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README38.md)
