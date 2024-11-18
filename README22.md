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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f66711a0-266b-3429-a9fe-336865a91e2b | -2.96395 | -49.20132 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 63afd161-6a9b-3d71-9d63-6079242adad4 | -2.1561 | -50.70906 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 586ae903-0762-3240-979b-0c8e64617243 | -2.59029 | -51.72863 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b61c700c-878e-3e04-8f3a-4badb7c4261a | -3.14783 | -45.99109 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6b38ab9-2e2d-30e3-a4f5-1c3ff7d20cf3 | -3.29942 | -45.67446 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 8fcc5b29-6428-32ed-b260-64e23c4fc4af | -1.62782 | -53.29998 | 2024-11-18 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1efb3c2-c709-32af-a1cb-b27afc11f0f1 | -3.07661 | -48.0672 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49799388-8fcc-30b0-9b11-cfadab4bc58c | -1.61848 | -52.62457 | 2024-11-18 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17d8e315-913e-3a68-82eb-c2e448e9ca02 | -3.20793 | -46.46737 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e193e728-c468-3c31-b79f-aa5ded6479fa | -3.77906 | -46.67424 | 2024-11-18 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbd20ebb-05c8-31ae-b97e-9857c561f905 | -2.33909 | -49.14005 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b07fa2a3-0e55-3b02-8597-3678a51e2bbc | -2.58542 | -51.72414 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e46452c4-6169-33be-87af-3fce2de7a20a | -2.60092 | -51.79995 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b8d8bf1c-bbe1-3f30-a238-b1a8fffa0979 | -3.18331 | -45.44337 | 2024-11-18 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 74d6c773-acbe-3bd4-bc1e-04fde1d721cd | -3.15153 | -45.9917 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd86761a-1891-3b1a-8601-7562768800c2 | -1.7623 | -50.74494 | 2024-11-18 04:10:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0c0d09e-2036-3eba-b554-45f9b9896c19 | 0.80076 | -50.22637 | 2024-11-18 04:10:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70c55c12-8aeb-3336-816f-4668acc6f389 | -2.59603 | -51.79542 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8cb4b4f-19d1-3809-bd6c-b6cbbb44956d | -2.64899 | -46.22771 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e7071df-1c46-34ae-9cee-436c8a648ace | -2.57951 | -51.72181 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6b1db5a1-9cd4-3d5e-8a4d-6c1c7cd546b1 | -2.43102 | -48.64183 | 2024-11-18 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 965be01f-458b-3707-9354-9ccc78b40485 | -1.43769 | -53.39024 | 2024-11-18 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4b23a2ef-b933-3ddd-8c51-a2f79c4696cc | -2.36765 | -53.68851 | 2024-11-18 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0eb4c6f-7311-3082-be6b-10f94e0b95f3 | -3.27912 | -48.80615 | 2024-11-18 04:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43cefc67-ba00-374e-aa5c-75339a9b3728 | -2.83184 | -46.66302 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8047190b-40b6-33ec-a963-2db50360ca09 | -3.29874 | -45.67867 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 1f7a24ed-d02f-31de-9c25-f863202cdae9 | -2.98417 | -49.1045 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 27e1eb39-d705-3da5-8ecf-47123fcc2e2c | -2.67892 | -46.1856 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b85152e-168a-3e57-9645-e9488218834f | -1.8939 | -46.44814 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b197c64-761f-3147-b06a-7957c4bf0042 | -3.07598 | -48.07107 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 207292b8-2327-30bf-b66f-e9fff6f3b05c | -2.93767 | -48.33221 | 2024-11-18 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fdf7eb8-85d4-31bc-9934-b7577f7bf2a9 | -2.55491 | -47.28218 | 2024-11-18 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 466142ed-49e4-38e8-98ec-0e423ff992f0 | -2.25545 | -49.04882 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9923725-9bd7-3a09-8bfc-10db7405e4f9 | -0.95039 | -51.72613 | 2024-11-18 04:10:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dfb850be-ac3e-3994-9739-a380d7704e46 | -2.6535 | -46.22372 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca7b3440-3ce8-39db-be3a-b9b5bc3f575a | -1.7732 | -50.75131 | 2024-11-18 04:10:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa570d49-0ba3-3f52-800c-6cbcf88b3a15 | -2.63407 | -46.56728 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4293131-072c-320e-982c-e46aa9381ff0 | -2.58602 | -51.72059 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b7059ca8-2efd-3029-9db1-5b263a3fb368 | -2.59088 | -51.72509 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c4097c5-322c-32b0-bf88-8ebc40f34745 | -1.8509 | -50.80305 | 2024-11-18 04:10:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47112635-f010-3993-abff-ceb8d32b4b2d | -7.18326 | -39.11995 | 2024-11-18 04:12:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 97ee0313-2c82-3b9e-8363-50e267cabe9b | -5.17573 | -44.36951 | 2024-11-18 04:12:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9547e54b-4115-36b9-bd39-3afb6fb3a2b1 | -4.42933 | -50.09513 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f224a58a-d7a4-3c1c-b144-724cf3ff365a | -4.72733 | -44.43376 | 2024-11-18 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11fc674d-e0b3-34ab-942b-ca5f558981c0 | -4.90949 | -44.02562 | 2024-11-18 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 4cec9728-cb70-37fc-920d-f76b9e61bef7 | -3.66356 | -50.44225 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5f2579d7-2d81-3c81-991b-b40e4468aff0 | -3.39597 | -53.27342 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92ab8a24-d964-3b97-95a7-c9e913794c55 | -3.33057 | -53.3543 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1cf3cfa9-d66f-3e13-9c30-a44b438eced4 | -3.06654 | -53.28359 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e04a2015-7272-3768-9fb1-2bd20914ee83 | -4.99372 | -44.3297 | 2024-11-18 04:12:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fb9cff0-18f1-3e22-8e14-be99e231bae7 | -3.34662 | -49.50846 | 2024-11-18 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 704dd3ba-d4d7-3832-8346-66e1c827f58b | -3.09975 | -53.105 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c2e41dd-d8d4-37a9-a7f7-74157a850da3 | -6.98619 | -39.65857 | 2024-11-18 04:12:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ca5812ce-2dbf-3f66-aa32-5955ffe0fc21 | -6.46854 | -42.37338 | 2024-11-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2c0f9d30-7043-3064-b67a-aa25253f1587 | -3.40262 | -53.3063 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbda736b-7c5d-3852-9a83-5f2e915e88f4 | -3.08244 | -54.66302 | 2024-11-18 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 62dab0e8-a3af-3f7a-8564-14319daddbb5 | -3.96635 | -46.71338 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a3bb869-5279-3c61-adb7-bfe85c0c7ce9 | -3.57702 | -53.27248 | 2024-11-18 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 180a5ed5-c8f5-38b7-841d-413aeaeed94c | -3.33652 | -50.49179 | 2024-11-18 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e408cc17-c204-3dd5-9935-fd3f9988e6c2 | -3.88889 | -46.64161 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9baa7ed-1379-3106-ba2d-c688b5476503 | -3.33059 | -50.49669 | 2024-11-18 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 66b1a837-fba6-3b03-a0d4-737b411ecc7b | -4.99473 | -46.80473 | 2024-11-18 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4215c522-aca0-306c-987f-b1e32730e853 | -5.27064 | -47.18932 | 2024-11-18 04:12:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2acd8a9f-a1fd-302e-95c1-59ed63bcc4de | -4.95383 | -44.84081 | 2024-11-18 04:12:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74111ae2-254b-3e6d-b891-6164df182527 | -6.1643 | -44.42502 | 2024-11-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cddc61d5-a57f-3d1e-a9e4-82db08bd45ea | -6.39705 | -44.7403 | 2024-11-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d25efcc9-3185-3a63-add5-7079b2f43ac0 | -9.30152 | -46.21793 | 2024-11-18 04:12:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d8f3868-68f8-34e1-9bae-8deb3350f86e | -4.26634 | -50.67915 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f542236b-c8ef-37d2-b687-81bff8ab038d | -6.47604 | -42.36741 | 2024-11-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 97f589c5-ffbf-34e7-aae6-c4cb63d67940 | -3.18472 | -53.24009 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c99fa89e-a7d1-38e7-9c83-87b896f1a2b2 | -4.27258 | -50.88467 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9025883b-7b8e-395a-85c4-cb22744d1c74 | -3.18926 | -53.24987 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9bb3f3a9-39c6-312c-8a00-c8be1a4d51da | -9.62959 | -45.21606 | 2024-11-18 04:12:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f8ac45a-265c-396f-ac07-1da470270503 | -5.07659 | -41.9996 | 2024-11-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9638dfb0-e5d5-3e65-b676-a6a681485836 | -4.10314 | -51.06433 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f712396-865b-32d1-bf66-21ef1f0cddc2 | -3.39313 | -50.73492 | 2024-11-18 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dadd44d7-722f-3ade-9713-9e7e2fe5604c | -4.9955 | -46.80009 | 2024-11-18 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 729f0cb1-ba7d-3095-9c03-6f30af58f60d | -3.32657 | -50.49022 | 2024-11-18 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 503ed44d-973a-35a0-9979-f4f13c2ec004 | -3.08147 | -54.66872 | 2024-11-18 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a9f049a0-2871-3fe0-8ecf-4d074ad66b5f | -3.37256 | -53.32453 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| acb3b125-237a-33d6-abe8-e66a7d91dfba | -4.35402 | -45.87201 | 2024-11-18 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c65054c-a068-37cc-86ab-1dd983989ea2 | -3.10332 | -53.10492 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e03cb88f-1d60-33ab-8439-3534465f9b00 | -4.2713 | -50.67996 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bda44ebe-ea6e-312b-a91e-5e0528158424 | -4.81803 | -44.48203 | 2024-11-18 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4b3c9a8-4393-38cc-923a-4a3b9b2f9b35 | -4.07204 | -46.08739 | 2024-11-18 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76eb49a3-08b8-367c-9103-16e59b99c0e9 | -3.33959 | -50.50397 | 2024-11-18 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 47631954-a505-384b-980e-693961b94fb1 | -3.89966 | -50.09234 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f54325a-f9fe-3389-82e0-fd1834f71229 | -9.63018 | -45.21243 | 2024-11-18 04:12:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 032bd073-c14e-3030-847b-753e97c058fd | -4.80876 | -42.2136 | 2024-11-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eaf7e640-869f-33a9-97c4-ac319fac849b | -7.74369 | -37.78912 | 2024-11-18 04:12:00 | NOAA-20 | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| acc1c1ea-1e0b-3048-a2d9-bc197dae1429 | -3.17942 | -53.24986 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8cbf3788-4f91-308d-b6a5-907c84a314db | -7.148 | -46.17915 | 2024-11-18 04:12:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 340805c5-cddc-337a-bd11-9d61adf2e691 | -7.39961 | -42.76149 | 2024-11-18 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fcb5b01e-257f-3af4-9d36-22439a1f1712 | -3.75985 | -52.14563 | 2024-11-18 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3491345-8f1f-377d-858f-238ece00b97a | -3.96097 | -46.72226 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc4a744f-54c5-387a-9ce8-7c4e69e991ad | -4.10579 | -51.04876 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f2cd203-e45a-3b8d-8363-ea727762d263 | -3.37103 | -53.33376 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa94e0f8-e3b4-3225-b2bb-16b3c52d3c4b | -3.04585 | -54.40718 | 2024-11-18 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ece88b97-efa4-33e9-94eb-75403d372d0e | -9.9021 | -44.47228 | 2024-11-18 04:12:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a769c070-3c26-39d9-84ef-f45356956ad9 | -4.8902 | -49.78012 | 2024-11-18 04:12:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README23.md)
