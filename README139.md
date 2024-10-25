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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c85615d-5b95-39c1-99b7-68d9728319fe | -9.17271 | -40.94252 | 2024-10-25 16:50:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0b4d766e-cd77-3850-b6a0-5f94d0658b16 | -9.16752 | -40.94351 | 2024-10-25 16:50:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1ad983f2-5359-3068-bd9f-a5414c820ac0 | -8.91657 | -40.43332 | 2024-10-25 16:50:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 1e01bf87-6485-3aea-a6d3-12a4d6dfd603 | -8.9133 | -40.76416 | 2024-10-25 16:50:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 52.7 |
| 357df664-5cec-35dc-9b19-5d42da2f3081 | -8.91269 | -40.76081 | 2024-10-25 16:50:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 52.7 |
| c09bfa4d-1c48-3372-907b-6eeb20b49236 | -8.87074 | -40.74057 | 2024-10-25 16:50:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b05b59ec-9b77-3ccd-a176-6fd3a2ed054b | -8.76101 | -40.61274 | 2024-10-25 16:50:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 405dd617-6efc-343f-9a07-90a7f30d3000 | -8.71573 | -40.80774 | 2024-10-25 16:50:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| b436e585-05e8-3ef3-a304-fb74786c1290 | -8.71513 | -40.80434 | 2024-10-25 16:50:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 278bc777-815c-3ee9-83bc-3a4e4fbb580a | -8.65771 | -40.45503 | 2024-10-25 16:50:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 41fa96b4-64dc-35fe-9bd0-327279be5617 | -8.62534 | -40.70304 | 2024-10-25 16:50:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| bb8012b5-c05e-3fd8-a18f-af64b30366a2 | -8.62243 | -40.70654 | 2024-10-25 16:50:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 5eba9ba2-d0f8-3fed-ad23-f08f25d58699 | -8.62182 | -40.70308 | 2024-10-25 16:50:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 98183ef6-ac23-36f5-821a-d3cfafdbef71 | -8.62 | -40.70398 | 2024-10-25 16:50:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a5e24d78-5ec0-3748-b3b4-86a579f9b556 | -8.61706 | -40.92091 | 2024-10-25 16:50:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| be2e9c2f-4fd3-308c-901a-87c6c93220e5 | -8.57962 | -40.49732 | 2024-10-25 16:50:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b794d49e-2867-35e5-b608-ca43d335ca3c | -8.4411 | -40.90334 | 2024-10-25 16:50:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 84436f6d-d354-311f-ab85-28f619429fbe | -8.4265 | -40.82826 | 2024-10-25 16:50:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f8225ed8-0419-3aad-8f3d-5427bbcb36e1 | -8.91506 | -40.43599 | 2024-10-25 16:50:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 031f6cf9-ec4c-3537-ae68-0c7f4bae2e05 | -8.58104 | -40.49432 | 2024-10-25 16:50:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 14d88149-d4ce-3416-af14-d88b8665cfc4 | -8.34555 | -40.45937 | 2024-10-25 16:50:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 1baee5a4-7451-3240-a6e9-da041e38f4cb | -10.51658 | -40.15802 | 2024-10-25 16:50:00 | NOAA-21 | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 6d205f41-506b-371c-8a77-b193dad66e3c | -10.43054 | -40.42292 | 2024-10-25 16:50:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c319b266-26e4-3811-be21-11cf269f27e1 | -10.36483 | -40.53421 | 2024-10-25 16:50:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 480e5307-0e7a-34e9-b563-a91a7606bb9d | -10.34017 | -40.28433 | 2024-10-25 16:50:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 3e797d0d-1feb-3c02-a6ea-762b3906781d | -10.33697 | -40.26709 | 2024-10-25 16:50:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b7757d72-9480-3e1c-ae66-96186dcd7dea | -10.27458 | -39.96226 | 2024-10-25 16:50:00 | NOAA-21 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| f772e12a-b524-35db-a8ba-091ea5d7bfd0 | -10.27393 | -39.95877 | 2024-10-25 16:50:00 | NOAA-21 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 388cc9ae-f53e-3aa9-b893-605867e0774b | -10.19368 | -40.07897 | 2024-10-25 16:50:00 | NOAA-21 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 44.0 |
| 0ace016c-def4-3d80-88d0-a3dbb16fd7ae | -10.19302 | -40.07542 | 2024-10-25 16:50:00 | NOAA-21 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 44.0 |
| b34c5623-f0ae-3ab0-9e37-fa3a0454015a | -12.24216 | -40.96479 | 2024-10-25 16:50:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 179980d0-f823-3879-99a3-06cd12b174e0 | -12.23875 | -40.96454 | 2024-10-25 16:50:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 71cfb1b8-b8df-3cb1-bfe2-0a598e058e51 | -12.03077 | -40.85268 | 2024-10-25 16:50:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| e9b5ee1d-2d09-3338-941f-9ee8e1ea49cd | -12.03022 | -40.84976 | 2024-10-25 16:50:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| cbdcccf4-0400-3e91-8511-443d76524189 | -11.45138 | -41.49978 | 2024-10-25 16:50:00 | NOAA-21 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 20.0 |
| a45a5ec1-5b0c-3835-8bbd-c2731c3f1fe4 | -11.16552 | -41.47013 | 2024-10-25 16:50:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 45a9955a-42a0-36c5-9316-58a250e333e1 | -11.16452 | -41.47356 | 2024-10-25 16:50:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 159199f4-6783-3a29-baf4-1d1f46b71e81 | -11.74028 | -40.24072 | 2024-10-25 16:50:00 | NOAA-21 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 20.1 |
| c42c00bf-4280-30d0-b5e3-88c484d65efa | -13.24407 | -40.48503 | 2024-10-25 16:50:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1eedaa19-0bb1-3d2d-b9d9-1c1f4603546c | -12.95428 | -40.6469 | 2024-10-25 16:50:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 9e1065f4-0cfb-3f89-971b-1aa90806bda3 | -12.95391 | -40.64926 | 2024-10-25 16:50:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 55e75fb1-4fe8-32ac-8031-303951c71b39 | -12.95286 | -40.64356 | 2024-10-25 16:50:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 7f3d035b-ddb1-3b6c-aaff-91e43e9a1171 | -12.94944 | -40.64843 | 2024-10-25 16:50:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 1dea7a14-6f3a-3a1b-89f9-7e83c2a2789b | -12.94345 | -40.64401 | 2024-10-25 16:50:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 44.9 |
| 45b68f5c-1db7-37d8-95d0-9252f93fbdf0 | -12.94311 | -40.64642 | 2024-10-25 16:50:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| aed260dc-de4a-33f0-accb-067ddd1780df | -12.94195 | -40.64013 | 2024-10-25 16:50:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 41.8 |
| 17b98d30-e0ae-3f40-97b4-4fc84dd393d1 | -12.93728 | -40.63869 | 2024-10-25 16:50:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 44.9 |
| a3e6080a-c95f-3e91-9aed-4f9ff103e9c2 | -12.93699 | -40.64109 | 2024-10-25 16:50:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 37.8 |
| cbb2d72c-9198-30f7-99d4-6727235d8962 | -12.79991 | -40.48748 | 2024-10-25 16:50:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 53f16caf-2ffa-3dec-8243-7ddd1d72d9b2 | -12.7994 | -40.48473 | 2024-10-25 16:50:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 06850026-142d-3182-b435-936db073b599 | -13.37477 | -40.54508 | 2024-10-25 16:50:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 96ac5eb8-45f0-3933-bab9-7c09bee7702e | -13.37427 | -40.54728 | 2024-10-25 16:50:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 3b75b936-dc13-3b3f-9ecd-322d4cf74bde | -13.70702 | -40.88118 | 2024-10-25 16:50:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| b50be812-69a3-332a-a572-4e884f07d830 | -13.63637 | -41.56628 | 2024-10-25 16:50:00 | NOAA-21 | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7b671de8-b793-3b8d-a85f-f85fff580557 | -13.35958 | -41.34918 | 2024-10-25 16:50:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 00a4a1ff-4390-34a4-9ba6-39b0eae59a39 | -13.35795 | -41.67443 | 2024-10-25 16:50:00 | NOAA-21 | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 40d146a1-bc6b-3c80-a20b-c1df09524569 | -13.35792 | -41.67133 | 2024-10-25 16:50:00 | NOAA-21 | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 7a36a013-a939-3575-8fc5-f759b06c138e | -13.35397 | -41.34521 | 2024-10-25 16:50:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6768ed97-0c3b-3b57-b65e-5766a149351f | -13.11153 | -41.66927 | 2024-10-25 16:50:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 8bf90722-7ffe-3cfa-8204-cb03dea9d477 | -13.11066 | -41.66453 | 2024-10-25 16:50:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e719548a-c0f3-30c9-a25e-10cf1182f368 | -13.05 | -41.74893 | 2024-10-25 16:50:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 33a818f6-15ac-306f-99bb-b2ca53e55fbe | -12.87372 | -41.7665 | 2024-10-25 16:50:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 51d641bb-d492-3f00-986f-5b34e3998722 | -12.61165 | -41.68177 | 2024-10-25 16:50:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f72e0b9f-e633-39df-b1cd-4b812baf01cf | -12.5885 | -41.02338 | 2024-10-25 16:50:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 161a3210-588c-3e40-b6fb-e42d0665cd11 | -12.58621 | -41.02256 | 2024-10-25 16:50:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 612ee334-707a-39bb-beb3-22c0461d937b | -12.37434 | -41.63842 | 2024-10-25 16:50:00 | NOAA-21 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| ede30105-2a86-3882-a0b1-f5c57f0cc188 | -12.37127 | -41.63739 | 2024-10-25 16:50:00 | NOAA-21 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 3ce06a77-5c59-3c4f-862d-abafd1f28e11 | -15.24502 | -41.08685 | 2024-10-25 16:50:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 25a5862b-30b8-34d2-bac6-0eb3303d262c | -14.63242 | -41.90771 | 2024-10-25 16:50:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 93a1b57c-83b0-3dfe-9623-b7a61a675a57 | -14.59587 | -41.97732 | 2024-10-25 16:50:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 70d4d5f2-52ef-3639-a035-f031b8ac89a4 | -14.59146 | -41.97812 | 2024-10-25 16:50:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| c6d27f0e-14f4-3bf1-96be-81a53af6b4fc | -14.57434 | -42.00919 | 2024-10-25 16:50:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f0be6275-1876-3c80-a4e9-68319c3a740a | -14.53183 | -42.12267 | 2024-10-25 16:50:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8242f80b-bcf4-3905-ac71-4e492d63a220 | -14.53106 | -42.1208 | 2024-10-25 16:50:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9df8fd9e-dcee-3242-a6e5-9d0cf630ed80 | -14.47552 | -42.0396 | 2024-10-25 16:50:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| d1616526-9431-31a8-9053-e2c417ec2908 | -14.45216 | -42.20763 | 2024-10-25 16:50:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 7190e686-1a53-3dca-862c-61ca00ab9c47 | -14.45135 | -42.20326 | 2024-10-25 16:50:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 8fc54bdc-eede-3597-9887-b89ac10e3fad | -14.42174 | -42.14142 | 2024-10-25 16:50:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| ef3ca2f1-7a1d-3f9a-a2a1-39f696e5ca00 | -14.42134 | -42.14055 | 2024-10-25 16:50:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 1f8d3089-b947-37ea-8e49-c0ff5b9b1ebd | -14.41697 | -42.14145 | 2024-10-25 16:50:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 38aa34fe-dfb8-3e8f-8948-05696e82f015 | -14.29937 | -41.97227 | 2024-10-25 16:50:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d4734e57-254b-3635-83db-61a3df4fbedc | -14.18704 | -41.85554 | 2024-10-25 16:50:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 62abb6e8-6ded-3c8a-83ca-1e714857f795 | -14.18619 | -41.85096 | 2024-10-25 16:50:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 3b815de3-cc63-3390-947c-414ceb7c3b61 | -14.1826 | -41.85658 | 2024-10-25 16:50:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 413f14cf-43a7-3272-ac59-410b063d846d | -14.18173 | -41.8519 | 2024-10-25 16:50:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 1c6a67e7-e32b-30ab-933d-689ef72f300e | -13.89091 | -41.86961 | 2024-10-25 16:50:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| d5256adf-7d2b-372f-9e6f-53d8ed283c9a | -14.45784 | -40.69453 | 2024-10-25 16:50:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 1edad265-339b-36f2-bf38-5946cdf0e73f | -14.45685 | -40.68925 | 2024-10-25 16:50:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 9ea321e4-c82d-3137-a1b2-f5d80bdacfde | -14.45203 | -40.69015 | 2024-10-25 16:50:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 43052fb5-bdfb-3156-8b86-5a76f63168b2 | -14.40454 | -40.70273 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 461e9dc7-8b9c-306e-bd6f-28928f4d99ef | -14.12988 | -40.6307 | 2024-10-25 16:50:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 91294c17-2ec3-302d-8f71-7400c42fa9a3 | -14.12501 | -40.63159 | 2024-10-25 16:50:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 1ecc913a-15ef-3042-95ab-c9abf000efb5 | -14.12405 | -40.62646 | 2024-10-25 16:50:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 31.7 |
| 96f27f3b-515a-3382-811c-1d3c4b006825 | -14.98273 | -41.71209 | 2024-10-25 16:50:00 | NOAA-21 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 776c9241-df92-36e6-be6f-76772f3d55a9 | -14.97827 | -41.71292 | 2024-10-25 16:50:00 | NOAA-21 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 1ba537b4-7a46-3945-8bfa-2bc2fdc8d950 | -14.87529 | -41.63251 | 2024-10-25 16:50:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| ba7bc772-2394-3832-b76c-c29a15a384cf | -14.87301 | -41.63139 | 2024-10-25 16:50:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 39.4 |
| ee4960cc-a3dd-3e52-8be5-3804b6fd6221 | -14.87078 | -41.63325 | 2024-10-25 16:50:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| ffc76572-f31d-392b-a386-e01bf9dfbd8c | -14.8654 | -41.69119 | 2024-10-25 16:50:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d2703058-7fd3-3dda-8b24-eb3994acd20f | -14.82452 | -41.36634 | 2024-10-25 16:50:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |


[Clique aqui para ver as próximas entradas](README140.md)
