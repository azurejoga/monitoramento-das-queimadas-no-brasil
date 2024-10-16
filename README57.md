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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aaa7529e-0e64-3ad1-9832-35d68f3893bf | -3.61412 | -51.37912 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fb526e9-ce9e-313e-b250-f872d146635c | -3.61366 | -51.3821 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 547780f2-2005-35b1-ac27-235436cd1cca | -3.61244 | -51.44636 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af568bee-442e-356b-a445-1a5168e56414 | -3.61201 | -51.44939 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4114f1ed-57c1-31b3-91c8-8fc37aefc78c | -3.61174 | -51.37877 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b936ec2-7e18-36cd-9b71-8b33a16b6757 | -3.58797 | -51.44859 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab3a1567-79d7-3ce7-a619-f156fb89403c | -3.5087 | -51.31242 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4dca0d1d-d41a-308f-bf19-5b24048adea4 | -3.50857 | -52.16348 | 2024-10-16 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fed61113-887f-3fa4-852b-4ff3140a9e16 | -3.50576 | -51.31417 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d72f3232-5103-3405-b49d-74d2251a06a8 | -3.50373 | -52.16277 | 2024-10-16 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc5137cc-051a-3fbb-81b5-96c41a2826b2 | -3.28355 | -50.93404 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 756d972a-2a89-3b0d-90a6-5465837227e3 | -3.28307 | -50.93727 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 105a0443-d488-3165-b483-add71ed005c5 | -3.27735 | -50.93975 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0af205f1-910a-3f7f-903a-cc2636b0791b | -3.1988 | -51.034 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2eef82f8-1df9-3272-b3b2-8869daaf10cc | -3.19834 | -51.03707 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81b53ab8-8092-3396-a5d9-d2660dacc6f6 | -3.07386 | -51.18436 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87ad8ee4-0e37-3b56-829c-fe0045171022 | -3.0734 | -51.18741 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf48a08f-0078-3309-be3b-72bf67ad8fab | -3.07293 | -51.19051 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e51e8ea-4dfc-3eba-8569-5caffb9869ba | -2.90354 | -51.81316 | 2024-10-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebef1137-f06e-3b35-8cfa-acf48d9baf7f | -2.90272 | -51.81877 | 2024-10-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf22cb8a-7892-3039-acbc-9e8f27886754 | -2.8856 | -51.68499 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3b21dc4a-5e04-3047-ada1-c45aadda7d4f | -2.8815 | -51.67857 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 003dd66e-9f13-3e76-afb9-0661b0c78c07 | -2.58443 | -51.9218 | 2024-10-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cd43906-1b24-3467-a5e1-df0b19cd13f8 | -2.52593 | -50.71679 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c399ebaa-f0af-3bd2-92d1-212ba757a708 | -3.28833 | -50.93805 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b621baa0-a072-328e-b80d-ee46f4cbc2fc | -3.2826 | -50.94054 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 977de643-5d0a-3fc8-9eed-a1da5b538ebd | -3.2783 | -50.93325 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ed251eb8-d051-34f5-a3e1-fd4c4d40ef38 | -3.27782 | -50.9365 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e8972e6e-ffed-311e-aed2-44cf89f57fda | -3.19925 | -51.03096 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7138bce-3744-3e4d-b693-8cd43c023d37 | -3.07806 | -51.19138 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6f439c9-4d31-39e2-92ac-8b01e32ab1ac | -3.07478 | -51.17825 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d27e932a-7e08-314a-aa1b-dff68c70ee9e | -3.07432 | -51.1813 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcd2d499-d660-3576-ab87-f7a37adb8694 | -3.06872 | -51.18354 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01a96e94-e8a8-3414-8595-219cd0cea26c | -3.06561 | -51.23911 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9470c40c-b9f2-3565-af91-8b024d49ae0f | -3.06516 | -51.24212 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 316e51f0-6c8c-39e9-872a-c4e9dd9859ad | -3.0647 | -51.24513 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b239fb56-e23d-3c29-abb8-03096dfc12dd | -2.90561 | -51.81839 | 2024-10-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e1dca3e-10d8-3726-8161-90964b5634ef | -2.90069 | -51.81776 | 2024-10-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f011e42-4b83-3f1b-beab-1615621b5ad4 | -2.88645 | -51.67933 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e300d000-fa05-31fe-a862-84abb5a81e9d | -2.88065 | -51.6842 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5332701f-dad0-30e6-bcdb-a0f8baccfd78 | -2.87654 | -51.67781 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b4511548-124d-3768-9e87-ea94c13136bb | -3.54689 | -51.58443 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27d2c633-253d-346e-9597-7e049620d878 | -3.5321 | -50.8886 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c388be7-5319-3778-8010-98147d6f07db | -3.51138 | -51.31172 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a09bafc-42e1-30c0-bbe9-3b8c9bd06f67 | -3.50622 | -51.31114 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28d2b7ae-494f-3b91-8856-ea4840de837e | -3.50503 | -52.16204 | 2024-10-16 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 07b9969f-b840-36e0-81d5-65458c0e563d | -3.49984 | -51.58921 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59eb867f-3572-3d56-babf-cdf877c45b32 | -3.49802 | -51.67178 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72fe92f3-65c9-3a3e-a341-d1cdb7a435c5 | -4.64118 | -50.98239 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f211dfd-5709-3a72-9da8-ad54874a237f | -4.36274 | -50.97081 | 2024-10-16 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d7e53f6-bd6b-3113-b134-471823995418 | -4.36225 | -50.97419 | 2024-10-16 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01841d2b-549d-39c0-8bf3-239ee369e658 | -4.35693 | -50.97338 | 2024-10-16 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b677f51b-32e6-3b0c-9478-27fbf6d410c8 | -4.35644 | -50.97678 | 2024-10-16 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efb49d6e-5228-3435-88c4-ab3ed4d54db0 | -4.18341 | -51.2485 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d760999-80b0-3e5d-9d80-806221bcf505 | -3.84495 | -51.75114 | 2024-10-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4787bf1-adf3-3caa-a9e7-a55433deafed | -3.78101 | -51.35131 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 583cc8f5-1bdf-3fe4-9560-31dd038d7a9b | -3.77589 | -51.35035 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c69b9dd-9970-3442-bec1-2e530e7e2a9e | -3.77076 | -51.34954 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70070628-6a18-38b8-8676-93fcd8435975 | -3.75197 | -51.93532 | 2024-10-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8fcb9b86-eda6-37ec-9c79-57852baeb12b | -3.74977 | -51.93874 | 2024-10-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 11f61af4-be47-3108-b914-079b90f2b19d | -3.62518 | -52.0153 | 2024-10-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee174514-ec70-3332-8636-8ffc0a5d32d4 | -4.64168 | -50.97905 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7dcebd6-fc5f-36a0-85e8-43a589155bcc | -4.36176 | -50.97758 | 2024-10-16 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6518cb6-de14-358b-81b4-084317d9fd85 | -4.35742 | -50.96997 | 2024-10-16 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53aea960-425a-3f63-bf4b-a810c0d986c7 | -4.35596 | -50.98018 | 2024-10-16 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 961577b0-e84b-3ae0-bfc6-bb85e0ddbdf4 | -4.11412 | -51.09435 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72323bc9-ac6a-3d31-89c4-006ed6e56968 | -4.11367 | -51.0975 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1f8eb01-d2d7-3b3f-98cc-ce1a6bd7fde1 | -3.92369 | -52.14781 | 2024-10-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba399ead-b20a-3adf-a5e4-254480205484 | -3.87875 | -51.97774 | 2024-10-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16742694-65b8-33d7-a5b7-c251607aa11d | -3.84997 | -51.75179 | 2024-10-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e542601-9f96-3330-bdcb-b719219e18ba | -3.80788 | -51.27636 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e1168b2-8951-33a9-9925-768180cd0392 | -3.78765 | -52.23576 | 2024-10-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6789dbe-99eb-308f-afa3-fbcd3aac673c | -3.78055 | -51.35442 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cbaad265-ee89-3255-97d2-7211303eb718 | -3.77635 | -51.34725 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 30ed0c55-6af4-38c5-b864-c06e459b9cd8 | -3.77544 | -51.35344 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4b9b0483-f09a-3318-bdd5-6a91a3b5db07 | -3.77498 | -51.35657 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b69ceab6-9db0-3556-966f-c30f244e7f9d | -3.77031 | -51.35258 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e19b316-673e-354e-be8b-79062a7fdb36 | -3.71576 | -51.40367 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91f6ec2e-cd7b-3326-848b-d2e120413806 | 1.01158 | -52.21906 | 2024-10-16 05:23:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0c1f38e6-40f0-3c9b-bd06-aa6eff219eab | 1.00711 | -52.21993 | 2024-10-16 05:23:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 13.1 |
| f97de276-3a18-39b9-b9e7-7fe35471af65 | 1.0064 | -52.2154 | 2024-10-16 05:23:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6ac399e3-0334-3da2-b357-a583cf6b544a | 1.01086 | -52.21455 | 2024-10-16 05:23:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 09810de0-f7c2-31c7-aa86-f7d09606d52f | -0.61278 | -52.38959 | 2024-10-16 05:23:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 861ac4d3-51b1-30bb-a61f-423f00c995ed | -0.6135 | -52.38502 | 2024-10-16 05:23:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 271e0f84-3604-3b7b-9cee-f5a0221aa397 | -1.32831 | -52.41352 | 2024-10-16 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5f2b2785-5168-3507-8969-f5be4ea4f3b0 | -3.05215 | -53.25625 | 2024-10-16 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7559fe60-1277-358b-bc31-5b9922e91229 | -3.04837 | -53.25109 | 2024-10-16 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c8a851a-b4bc-3da7-9922-3735765398be | -3.04771 | -53.25551 | 2024-10-16 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8213f705-2d89-3d45-88e4-bb15c88f6a4c | -3.04326 | -53.25477 | 2024-10-16 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34272bf3-e760-3b32-a8cb-4e8645dddd1d | -3.05151 | -53.26054 | 2024-10-16 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f22373f7-387f-3ed1-8ccd-e270673328bf | -3.04904 | -53.24658 | 2024-10-16 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f53a5f7-53de-39d8-985e-800ffefc9aa6 | -3.04707 | -53.25978 | 2024-10-16 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f10ffbe4-2738-3124-92fc-3f08af24ab73 | -3.04459 | -53.24586 | 2024-10-16 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06c57d30-0369-3c19-891a-c448b5921835 | -3.04392 | -53.25034 | 2024-10-16 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c3960cb-4582-3a02-9ae3-a60d0b5ec032 | -3.04014 | -53.24511 | 2024-10-16 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52138c22-8a51-3ff8-ab41-886142922021 | -2.0956 | -53.40988 | 2024-10-16 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 778c3dec-7683-3b83-862d-efb7c9d0694e | -2.09126 | -53.40919 | 2024-10-16 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 883a2cb4-ad81-3dc4-90f8-8d671ec26432 | -2.09062 | -53.41334 | 2024-10-16 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f5ba8cd-be7b-3af3-addf-66fc89815a60 | -3.20917 | -52.46281 | 2024-10-16 05:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e0f512f-5bf4-3a83-b231-1ebb8a887534 | -2.86423 | -52.91291 | 2024-10-16 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README58.md)
