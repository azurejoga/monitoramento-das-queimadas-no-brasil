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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a932b761-cd5b-3a93-ad6b-cb54929bf0df | -17.15991 | -57.41629 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 348bedf0-a532-3eef-905e-c1fbf1a16b5f | -17.1599 | -56.75008 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8fe9309e-d849-3672-bde8-4226527bbca5 | -17.15583 | -56.75777 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| af813f14-347d-3ced-8401-93c58e2a0762 | -17.14752 | -56.80078 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cb69230a-dd89-36e7-8177-ad6b09d27370 | -17.14599 | -56.8009 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0979136a-efff-3eca-96ef-ea9afdf58355 | -17.14584 | -56.80944 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| a3c2f3e6-5f7f-347d-81c8-f7e7ef565d70 | -17.145 | -56.81377 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| bd23ec20-a739-337a-9f07-94be3eeeda63 | -17.14417 | -56.81808 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 17bba4bc-0ef7-3419-b3fc-323e6739dace | -17.14365 | -57.42767 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2d3877fd-77af-3363-a338-144167a333a8 | -17.14322 | -56.96338 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| b1852a62-37f7-3964-9eb7-07055739a56d | -17.14248 | -56.79569 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0874e97b-97e4-3b23-8c17-05226f694541 | -17.14218 | -56.77322 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 61b4f397-387a-3aaf-aaed-9fb11d43e7bb | -17.14195 | -56.8226 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 075e785d-0ef5-3bc9-bdbc-acb771918933 | -17.13971 | -56.79472 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2d514318-d40b-3684-a54d-a46af9bb6064 | -17.13915 | -57.42675 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4bc56e95-0af2-303a-9395-24ba82da06f7 | -17.13844 | -56.81738 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 2828a93f-12c1-3493-8ad1-0bf46a2ca1a3 | -17.13787 | -56.77234 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 20977fcf-6a64-3382-a2e8-4dc916d9d1fc | -17.13706 | -56.77665 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| af3bbb51-2de5-3875-87ec-b66b6f4891f2 | -17.13682 | -56.82605 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 5cc9e2de-6e25-32c4-91db-abe229956da7 | -17.13649 | -56.83452 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| b75bf939-55bb-328a-ada0-a4846dd90ede | -17.1352 | -56.83474 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| fd7ba865-4067-3a0a-b1eb-2fb5c5759447 | -17.13462 | -57.34473 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| db8eb66c-c172-3df5-b8ba-10d7db6e9711 | -17.133 | -56.82932 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| f7bf4587-e818-3886-8d3a-1995cf19d645 | -17.12963 | -56.84665 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7f111267-7f2c-3ca3-8805-77a1aeaa831e | -17.12924 | -56.84254 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 4bd5dd9f-fe6d-38f2-9aa5-0333e63264eb | -17.12843 | -56.8469 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 746288d3-c00c-3b90-9a9a-51a9b679a36b | -17.1241 | -56.84602 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 83b044aa-7f2b-30a5-ab78-7c66be492468 | -17.12328 | -56.85038 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 1194c8ed-16b0-34c9-a7a4-6b55047f925d | -17.12058 | -56.84078 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| aa8256e8-c8de-3cd3-be59-c0804f10f50f | -17.11976 | -56.84513 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 8b0fa5de-e9c2-32b7-a3b8-f5c1c480f129 | -17.11543 | -56.84425 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8b2cf1c6-2aee-3332-9d08-a45c921bfa3c | -17.11489 | -57.42389 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a6acb960-15c1-3442-9e60-7b59fc16744c | -17.11398 | -57.42864 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f75a2f66-2979-350f-839d-5fa00efd22d9 | -17.11109 | -56.84337 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f117191c-14cd-3d21-aabc-a27eb0c3ce09 | -17.10948 | -57.42771 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 335fc66f-beac-3aae-832a-e100a7ef3158 | -17.10242 | -56.84159 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b06ecca8-973f-332c-8f11-3125233d646c | -17.10159 | -56.84596 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| df2a9a7e-8450-35d5-a6ad-0c37b7bcda89 | -17.10056 | -57.37671 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 5c843a8b-1d15-30da-9b79-cd509e0dd44c | -17.09878 | -57.36168 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d888c4d1-7322-336f-a390-58072f1d6d57 | -17.09375 | -56.83983 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 707fcf99-87fe-37a7-b90b-82d6c1781d4f | -17.08424 | -56.84243 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| bbdb1ae8-4d1c-3fde-91a0-11d1f53bbc8e | -17.08074 | -56.83719 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6a0ea5b3-506c-353f-97c7-55ec4e220e7e | -17.07206 | -56.83543 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3a2f5721-2863-380a-af75-38204b9f3123 | -17.06773 | -56.83455 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 250a9b57-d3af-3adf-9734-5b9f20f6b175 | -17.05906 | -56.83278 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6163c604-0679-3a35-87c4-5ff06058fa0b | -17.03051 | -56.84054 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ebc9d7a6-59d3-3cc4-998c-06323a493488 | -17.02946 | -56.84182 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 050578fb-cb29-33d6-9b62-0b0ba28925a7 | -17.02617 | -56.83966 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 311b7e31-5b1d-377a-86ca-7d0267d35a20 | -17.01643 | -56.83918 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 35c87ed1-324b-3ac2-abea-92a9a3fd6e83 | -17.00274 | -56.6972 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6f552f9a-9a45-3630-b73d-22f1f3c98cb6 | -16.98924 | -56.72122 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 98a3bdc1-0dff-3c80-b499-e39e9580af0b | -16.9882 | -56.70318 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7b3ea36f-45c7-3ef1-9e94-3e6bce0f4d5f | -16.98738 | -56.70747 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8be118c9-130a-318a-a9c4-36229b623675 | -16.98389 | -56.70233 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5d89f288-195b-32e3-9a4f-0f5d8bf1afb5 | -16.9833 | -56.72895 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cc66cc9f-7146-393f-a585-561c203d0cdb | -16.98248 | -56.73325 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0ddd826c-9165-376a-a6a6-f2f9fb3b45ef | -16.96973 | -56.75306 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8085b467-1c11-39dd-9874-10a88a992a70 | -16.96931 | -56.80244 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9f228caf-860c-39ed-a9e1-e7adb613d375 | -16.96848 | -56.80678 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e78e9e5c-9caf-36b0-bbf2-20fa261fdead | -16.96765 | -56.81112 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6eb7157c-4bca-3627-b8a5-12afeacab422 | -16.96624 | -56.74787 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| dfa72757-d188-3b71-95f5-fce8acb69e6b | -16.96541 | -56.75218 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b21f5cbd-f17f-3be4-a98d-e520f873be13 | -16.96414 | -56.80591 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 14739447-dbd3-3777-831c-09b23de8897b | -16.95944 | -56.75996 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| be8beb78-5234-3418-b909-6fcb180ba082 | -16.93346 | -57.48196 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 94b52f57-4fba-3930-acc5-dc041f582668 | -16.92987 | -57.47623 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 2bcfb1d7-54c5-3bdb-a0e9-6d8e030adaeb | -16.92893 | -57.48103 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.2 |
| 5d795684-133d-3386-8c80-00e2f79fd372 | -16.92799 | -57.48584 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.2 |
| 8189119f-a5fc-36c9-b0a3-eedd11aa550b | -16.9255 | -57.69369 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ec586de4-a3eb-31e4-95aa-c38f63ffdf0f | -16.92534 | -57.47529 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 6e6aae03-77d1-3291-a4b4-e62fd3f0fa44 | -16.92346 | -57.48489 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.2 |
| 72d49deb-c156-391c-9ba1-af9e83251b14 | -11.97831 | -57.59875 | 2024-10-08 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30bd9ff2-f7a8-3bdb-9530-b3acffa8cc5f | -11.97791 | -57.5999 | 2024-10-08 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19751572-a23c-3259-9668-ac31c93c4bf0 | -11.97776 | -57.60168 | 2024-10-08 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c063667-a4a7-341c-8835-8a455b03f675 | -11.97735 | -57.60283 | 2024-10-08 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 779469a0-58a6-3a5e-9fa5-35e672f256fc | -11.97383 | -57.59495 | 2024-10-08 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15a0ce04-b78f-3f45-adb3-6dd041b85ec4 | -11.97274 | -57.60084 | 2024-10-08 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2754f31c-54f3-33f5-9e30-ea028149be8a | -11.97219 | -57.60379 | 2024-10-08 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df54c574-4072-31ec-9fd6-6f3bca3b6c23 | -11.96826 | -57.59703 | 2024-10-08 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85a77f9e-dc23-302f-a16d-b1d00048278d | -11.96771 | -57.59999 | 2024-10-08 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a1fe662-de6c-3ae5-b80e-a50937f46a07 | -11.96324 | -57.59616 | 2024-10-08 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3d629e8-ce65-3b18-8a24-e53be69deaca | -12.47807 | -57.66339 | 2024-10-08 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b3f1773-db13-3d8f-8415-b5b5857ab04d | -12.47197 | -57.66835 | 2024-10-08 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df09fcbf-6e1b-3ed1-9b9c-48810b6d4cfd | -12.47252 | -57.66543 | 2024-10-08 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90cb94b1-87be-3647-b265-7b591de776e8 | -15.70614 | -59.423 | 2024-10-08 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 716f16b4-779a-3cb4-967a-a0adf07a338d | -15.70547 | -59.42632 | 2024-10-08 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 550341ff-e249-3c48-9383-7e0a98420a07 | -15.70345 | -59.43633 | 2024-10-08 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae45d681-bcb3-3ca5-84d6-58804fd5e36b | -15.70272 | -59.43991 | 2024-10-08 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44584431-4ad1-3aa6-9bcb-ccc23ede98ca | -15.69952 | -59.42866 | 2024-10-08 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b10418b-38aa-312a-849c-4db8b2df098e | -15.69747 | -59.43877 | 2024-10-08 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b69edb67-0933-388a-b365-7418349a59e7 | -15.6967 | -59.44255 | 2024-10-08 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7abb6c35-24f5-325c-aef5-21bdd79c279e | -15.68175 | -59.40824 | 2024-10-08 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 049e62ee-6b72-3ac0-a78e-2fc98cf23aba | -15.66722 | -59.42568 | 2024-10-08 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6b33fe4-0e85-3c4e-8df3-2e91338c8b9f | -15.66655 | -59.42893 | 2024-10-08 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f22281f-aebf-3b24-8b06-c12deeac9dae | -15.66586 | -59.43232 | 2024-10-08 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c03a51cd-3cf7-3153-bfcd-fb972c17a353 | -15.33977 | -58.13257 | 2024-10-08 04:36:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f2b47f4e-444e-31fe-8429-16d1a83d0980 | -15.12844 | -59.02266 | 2024-10-08 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 130b915f-833b-3fd7-b937-f97b41f4ee76 | -15.12775 | -59.02609 | 2024-10-08 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c144bb8-18d0-3a53-9753-c61ee63057f8 | -13.4079 | -61.9229 | 2024-10-08 04:36:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b1b90d2-8c2d-379f-874a-3c915ba759ef | -13.40675 | -61.9283 | 2024-10-08 04:36:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README71.md)
