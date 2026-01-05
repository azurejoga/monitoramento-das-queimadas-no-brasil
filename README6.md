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
| 51659d09-d790-399c-9e8c-d2cc7f2b6541 | -1.57683 | -53.03276 | 2026-01-05 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a216855-8637-3deb-834a-6fcee7e214be | -1.11579 | -53.11023 | 2026-01-05 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 124c843b-39dd-3305-aa00-a937c74a918f | -1.97098 | -53.35863 | 2026-01-05 05:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35b0f13f-ade5-3c54-afc8-a58f8f7f2ff4 | -1.59358 | -46.02208 | 2026-01-05 05:10:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6609557-0261-35be-8c58-9c3eeb6f50b1 | -3.53372 | -54.17038 | 2026-01-05 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e92b3a40-b87f-3b5e-8fd4-2b85254a9672 | -2.96095 | -54.08403 | 2026-01-05 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b140902d-306b-3fa6-8907-7d107100df1d | 2.54537 | -60.35971 | 2026-01-05 05:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 81f64d75-82df-3c75-94e4-eefbd4ed48fe | -1.33355 | -49.40732 | 2026-01-05 05:10:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cdda24c-2bab-3f3c-b26f-04f487b7882c | 3.26738 | -60.93723 | 2026-01-05 05:10:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19784b0b-ca31-3d31-ac3e-ad9b29673ed3 | -1.25289 | -53.48172 | 2026-01-05 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47387290-d0e0-30ea-8625-f45fed5b456c | -2.91897 | -54.12186 | 2026-01-05 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a513f94a-0c33-35bc-ad7f-31373f5d8972 | -3.42986 | -52.84543 | 2026-01-05 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2aef3118-b192-3c37-9bff-f3af740829eb | -2.91545 | -54.12133 | 2026-01-05 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3632fdaf-9939-3dfa-bc11-eb840db429a4 | -4.31205 | -48.6285 | 2026-01-05 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 498c688c-4f2d-3bb2-9ad7-34adeee44aa6 | 2.54937 | -60.35915 | 2026-01-05 05:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fa9899b3-9ac9-365d-8536-eac762bdbfa7 | -1.74858 | -55.63447 | 2026-01-05 05:10:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96d85063-578c-3ed4-9c4b-2587339fd764 | 0.46705 | -60.44102 | 2026-01-05 05:10:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ee4b12a-e117-3aa0-9108-49efa649e963 | 0.55286 | -59.80256 | 2026-01-05 05:10:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85e81d10-1b90-3cfd-8e84-12a67a798921 | -2.80505 | -53.00256 | 2026-01-05 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 61a869a7-3c0d-35b5-a4d1-e7c43548e7ef | -3.40224 | -51.87483 | 2026-01-05 05:10:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fd120d1-d9ab-3b95-8b6d-0759ae5562a3 | -2.44651 | -47.79116 | 2026-01-05 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ea5141f-aab8-30d2-9c54-afd9f722a6e7 | -2.73488 | -49.46298 | 2026-01-05 05:10:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba209ceb-3b87-3e1b-90fb-891aa5b5a82e | 2.55336 | -60.35857 | 2026-01-05 05:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63fce33e-0ac5-3154-990c-fa14125e38d4 | 2.78856 | -60.30779 | 2026-01-05 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b43e752f-6b02-3897-a9b9-64a3b4dd3426 | -2.4532 | -48.63668 | 2026-01-05 05:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cccb291-dd84-3d63-9451-aafab3e768fb | -2.97329 | -54.33216 | 2026-01-05 05:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36480602-6f31-3866-b982-5f0cdb2ea116 | -0.08918 | -51.27882 | 2026-01-05 05:10:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 24ec5d40-be59-3418-80cc-da77e6555601 | -2.80434 | -53.0071 | 2026-01-05 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 35951db8-d5c0-34a3-a915-442b523890ff | -2.82924 | -48.65848 | 2026-01-05 05:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38aa77e5-fa16-3caf-a25c-fb9fbf4c4704 | -2.51069 | -49.06422 | 2026-01-05 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d0a7ff4-043c-3591-bb27-b6259269dd32 | -2.80061 | -53.00657 | 2026-01-05 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4856cd34-8a01-3ae4-bed2-5e158b1415b1 | 0.91302 | -59.35242 | 2026-01-05 05:10:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74cd4a3c-48b2-3bbc-8f0c-5566459c11a9 | -2.5629 | -53.87661 | 2026-01-05 05:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05695acd-15f5-3e78-9fc5-36876cc69c4c | -1.32819 | -49.41134 | 2026-01-05 05:10:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2933a0dd-f0b4-3480-ba51-fe23e3470b90 | -4.31713 | -48.62932 | 2026-01-05 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30afdc35-2075-344e-afdb-e861f6e4f01d | -4.88009 | -47.92681 | 2026-01-05 05:10:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 440df437-e4c8-36f6-b539-21ffbdcff32e | -3.53804 | -53.02297 | 2026-01-05 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79c8ac58-3a35-3757-9b8b-174729b66d5a | -2.85622 | -53.0039 | 2026-01-05 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8453aa16-0372-3238-b201-af30a033472b | 3.06876 | -60.2438 | 2026-01-05 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f9bbef1-9249-3d8c-9863-a8664f008d08 | 0.68217 | -59.49814 | 2026-01-05 05:10:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8dfa6fd0-7aa4-357c-85d2-c092da9a0d06 | -3.14357 | -54.65736 | 2026-01-05 05:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd22b2b8-9606-39cf-8e71-3a87ac26bd53 | 2.54591 | -60.36315 | 2026-01-05 05:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f76b895d-885f-3348-8d2d-ff8018244609 | 2.5539 | -60.36201 | 2026-01-05 05:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d03a466-32ac-3e8d-8608-0de52c6fb28d | -1.32743 | -49.41609 | 2026-01-05 05:10:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5fab432-2912-350e-80f5-97a956be04d4 | -1.25521 | -53.49025 | 2026-01-05 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bf74836-d6d7-3aff-901f-8fdc05e77ef2 | 2.5499 | -60.36257 | 2026-01-05 05:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bff08386-12fe-354d-8676-9f154a832d9e | 2.94619 | -60.28288 | 2026-01-05 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c263158-095e-3399-9b30-95f252f8845b | -0.74273 | -52.42653 | 2026-01-05 05:10:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 492dc8b7-06aa-3f6b-a1e6-c7a4b51f4da9 | -3.87939 | -50.96778 | 2026-01-05 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 698a477e-f616-338c-853d-6d72c39c9cfe | -3.17072 | -52.87083 | 2026-01-05 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3cae387-e83c-3ec0-8f60-66cbcd8d592c | -4.31249 | -48.62558 | 2026-01-05 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e030db0f-5fb5-3eaf-b586-809a4717cf23 | -2.44744 | -47.78493 | 2026-01-05 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 47b6b7e6-2c06-3822-8702-b27a8de06740 | -1.97375 | -50.16188 | 2026-01-05 05:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 633df705-2dff-3bbe-9774-4a036337d068 | 2.94672 | -60.28631 | 2026-01-05 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bad52d6-2d97-3eaa-a87f-66218d69f471 | 1.65679 | -60.74689 | 2026-01-05 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 887d7a48-54fd-37d5-a50d-46b472fb0a34 | -3.69861 | -53.48409 | 2026-01-05 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a6f2ee4-a802-3c67-a500-dde29af839ec | 3.06823 | -60.24036 | 2026-01-05 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 647f6180-0b84-322f-9de7-7c1de7b680ef | -3.68247 | -52.53114 | 2026-01-05 05:10:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c2702f2-a374-3c27-a348-69922408e210 | -2.83421 | -48.65923 | 2026-01-05 05:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c00202c-1407-39e6-b313-5f660b752ed5 | -3.29848 | -50.08123 | 2026-01-05 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23b3f1f3-1bfd-31f7-be2e-288d27edbc2d | -4.50594 | -48.52053 | 2026-01-05 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3a4fbb1-e9ac-36a0-ae94-59312f4a9d5d | -3.17003 | -52.87542 | 2026-01-05 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1482c599-afc6-35d9-8df2-9a94bbeb1a36 | 2.69638 | -60.19881 | 2026-01-05 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 006a56ff-1ad9-3043-a4c7-e7f0b628d6d6 | -1.11513 | -53.11442 | 2026-01-05 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cdec703-7da0-3615-b706-472f7182049d | -2.44698 | -47.78801 | 2026-01-05 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d5dcef08-1b17-32e1-91f1-8b779ca32ccb | 0.55661 | -59.80197 | 2026-01-05 05:10:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e35e6a35-9a92-3ee6-b0cb-6be84aa82a32 | -3.17007 | -52.87292 | 2026-01-05 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0195c655-a3a0-3a8b-b586-168f900308d9 | -2.75967 | -54.21719 | 2026-01-05 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2756d9e-2525-3619-be23-eeff7d012d2f | -2.4479 | -47.78186 | 2026-01-05 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dbe5401-faa8-38c7-8256-435dcc749ba8 | -1.32739 | -49.41224 | 2026-01-05 05:10:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34877b0a-208f-3ac2-aa86-487401f2d245 | -2.80132 | -53.00203 | 2026-01-05 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 24fb12be-e72d-3605-ab3e-98bb3b58c36d | -2.75617 | -54.21667 | 2026-01-05 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbb4ca98-8c02-3250-997c-5b999646fab4 | -4.31757 | -48.62639 | 2026-01-05 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 171b7514-191b-33bb-9cf2-71842492bb09 | -1.25646 | -53.48222 | 2026-01-05 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f7dc9a1-ca63-3406-9fb4-bd65f989d317 | -2.44825 | -48.63599 | 2026-01-05 05:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d185f240-246c-36b0-9029-df30cbb108dd | 3.06477 | -60.24442 | 2026-01-05 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61a1f669-6ea0-391a-b99d-5d894967eb49 | -18.55285 | -52.80102 | 2026-01-05 05:14:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d43b68dc-3be1-3643-ab93-a65b5d43d23f | -17.64978 | -56.44526 | 2026-01-05 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e5d5ab12-5369-3043-bf69-a1b668b43b5e | -16.60106 | -58.21027 | 2026-01-05 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| e9a9cb19-e1b2-36bb-b6e3-9675b31ab3d1 | -16.44347 | -58.16334 | 2026-01-05 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 400b7785-f3eb-3854-a34b-b9d4dead1169 | -17.65042 | -56.4407 | 2026-01-05 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b1913ec7-9e45-3c9a-9081-7ddb8e9cf3be | -16.16372 | -59.3224 | 2026-01-05 05:14:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5771e546-3c58-37d0-b9a0-6efaaebd7340 | -16.5971 | -58.21352 | 2026-01-05 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 44c6c429-df20-3c0e-bdc4-5e14612a5a0e | -16.15984 | -59.32545 | 2026-01-05 05:14:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90064263-5a9b-3cb0-a258-5cd498777dd2 | -17.64672 | -56.44015 | 2026-01-05 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 99ad30eb-acfa-3353-ab04-900bb903bf19 | -16.1604 | -59.32185 | 2026-01-05 05:14:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ee9e176-40ff-3556-b353-ca27905dcc7c | -16.5937 | -58.21297 | 2026-01-05 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 53550294-8b32-3afc-b4d9-4abe3692bd1b | -16.5903 | -58.21243 | 2026-01-05 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8aa4375c-2ca0-3a75-8725-c2d7c3d166f1 | -22.02955 | -56.30311 | 2026-01-05 05:16:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cc48bf3-18b1-391f-a242-35025b1051a4 | -22.03514 | -55.51734 | 2026-01-05 05:16:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81dabaaf-26b8-306a-a7c8-209b450e30ab | -22.03927 | -55.51793 | 2026-01-05 05:16:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2ad226c-5589-326e-a5b1-ee553a3e997d | 0.46457 | -60.44064 | 2026-01-05 05:59:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ad4a2e4-f870-3f4c-ad4e-170f19ccdabf | 0.55196 | -59.80208 | 2026-01-05 05:59:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78399dc2-1de9-3f9b-b43c-b369b350bcd0 | 1.65704 | -60.7477 | 2026-01-05 06:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ba731c3-9c2c-317f-a340-f49ff1ecb5a1 | 2.69303 | -60.19899 | 2026-01-05 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 800810fa-a93e-3f0b-a262-9e535e1c20fb | 2.54827 | -60.36024 | 2026-01-05 06:01:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0e624204-620f-37f1-b818-b9cddba9587b | 1.06426 | -59.70432 | 2026-01-05 06:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 890b5c72-e0fb-341b-bcd2-fe2b117e26d2 | 2.55311 | -60.35932 | 2026-01-05 06:01:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 910a32fc-be69-3e85-a47c-213c70b4b038 | 2.78876 | -60.30544 | 2026-01-05 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b325308f-6e3d-3fcc-8d6d-7ca259c147e2 | 2.94325 | -60.28431 | 2026-01-05 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README7.md)
