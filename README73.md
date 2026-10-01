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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e10296ad-dac3-3c2f-b29f-8465a4953009 | -4.30123 | -54.79547 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8cdb7dbb-d9b4-38a0-998d-61aa39736c93 | -4.37962 | -49.73693 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6185e745-9b93-366b-ab64-40abae5bb061 | -2.78779 | -51.66344 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed954607-148a-3fde-89e7-615eeafdc73f | -3.56975 | -51.48167 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7004e615-5288-3fc7-96c6-3ed6bd180bdd | -4.89492 | -48.37692 | 2026-10-01 05:16:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a8231b1-2bc1-3940-94f8-71a0c60e6ca4 | -4.28891 | -50.76733 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 297.8 |
| 1a62090a-a87b-3a7d-98f0-8a40e201a12d | -3.18373 | -51.2413 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9317d049-0678-388a-8c8a-d44d5a18fa25 | -3.17098 | -54.09589 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 9c736631-6e63-3c00-930f-4ec2bca2aebf | -1.39512 | -55.34031 | 2026-10-01 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a345545-aac5-3577-9c56-71c84e507cf4 | -3.25337 | -50.81666 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ced0d8ef-4540-3a04-9cc5-b0697a981401 | 1.80412 | -55.62535 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a5d6535-8fdf-39ca-bfa5-832d69dde207 | -3.29283 | -53.85199 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 7986f17e-1c14-31c3-a917-743fa105b0d5 | -4.45394 | -47.92651 | 2026-10-01 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 364281c1-1b47-3700-99b6-8c8420e1dfb2 | -4.88977 | -48.37218 | 2026-10-01 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 2a9369e2-1e41-3676-bfb0-7fec0503e8a9 | 1.87481 | -55.62541 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c03e990e-e979-38bf-acb3-387b3ec19327 | -3.17335 | -54.10605 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 17500731-104f-3d8a-871c-6a67ec523bbe | 1.70843 | -55.90859 | 2026-10-01 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c3b661c-47b0-36bf-af11-c157767071a4 | -1.32796 | -55.41973 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7805e86-1587-394e-8e81-d90e6a04ba10 | -3.63175 | -54.5029 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d47febe2-0fa3-3dad-8fac-4df5d3de3eee | -2.99621 | -51.03391 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e423ca10-f07e-3163-a721-85f04f33f7ca | -4.39364 | -54.82566 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcea4e93-e159-3a62-a00b-68587fcd9442 | -4.27417 | -50.76528 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| bafd1e70-614c-3a90-93f2-67ee5c29afae | -4.57832 | -55.84629 | 2026-10-01 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc9e16c4-4894-30fd-bc39-d3aa03488e0b | -3.18038 | -54.09917 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 0c1f6dc1-8caf-3fd1-966b-bc6aa6d8c07b | -3.6307 | -54.61074 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f60d6c9-601f-3b50-9e35-a139f8213cc4 | -3.01568 | -53.88108 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37cf9e8c-8bb6-3a82-928a-8e96afebc971 | -4.38923 | -54.82959 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0309bf01-80d1-34b0-b576-5c0a42708d42 | -3.0079 | -53.87987 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b60c601-4ae8-3ce2-bdc9-95b014bc0a3a | -3.48235 | -54.69641 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 839a95e6-6b22-3b90-bd9b-54bc68b76574 | -3.01069 | -54.22867 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e2a1b3e-b70f-3829-ba5d-089f16250b8b | -3.40208 | -59.59079 | 2026-10-01 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ea6f23d-4f03-315e-afa1-3f55d246dacf | -2.99018 | -51.03168 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8fc82c86-0c0d-32ca-b2d2-47537eb16957 | -1.37894 | -55.20916 | 2026-10-01 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26a40344-2431-3d06-ab9e-45d79139702d | -2.89992 | -54.08903 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3568edd1-49d9-3196-ab5d-124b00def7ab | -3.47862 | -54.69586 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc153b78-df1c-3b58-b16f-62d15b744d9f | -4.45516 | -47.91781 | 2026-10-01 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f35be80e-0a34-32f0-a2d0-4a424bfd11cd | -1.96713 | -55.55259 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb57a7d7-cf03-32f0-aec4-fcedefc85161 | -2.96187 | -51.02731 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5e659736-8414-3eaa-af1e-e5df569e930a | -3.60938 | -48.91495 | 2026-10-01 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60637464-8c8b-3cf5-9b87-e081bca7739d | -4.30055 | -54.80006 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f8510b0-992d-3d44-927a-dad50d889cf3 | -4.05954 | -51.09667 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c384e25-56a2-31ee-9bf3-5bee8bc08e86 | -3.29207 | -53.85697 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 5b54ed9d-2100-3ba6-bc2f-4c70ba56ad5e | 1.87427 | -55.64398 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6e09db2c-076e-3b16-84e5-2ea94d077a8c | -3.14004 | -53.74782 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e7f45ff9-5d76-3ff7-bf98-d71b13b4a735 | -2.91446 | -51.31128 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 454fd3c4-36fe-33d4-a87b-e8b660ab4d11 | -4.06362 | -51.10229 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 982e1655-6cf8-3679-9bde-f799ea3180a4 | -2.78609 | -51.66047 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1548df1b-8d81-3ce3-8692-e43b0dd42a67 | -3.68794 | -60.54401 | 2026-10-01 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a280817-beee-315b-a4d5-65c722d72b6a | -3.95704 | -49.04835 | 2026-10-01 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c09d02ca-4398-36a9-a634-09adaf296408 | -1.74694 | -57.18189 | 2026-10-01 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40b3cd2c-8a96-3110-871e-7b67a0bd646f | -4.89496 | -48.37733 | 2026-10-01 05:16:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da1cf147-a519-3bd2-9989-ce20ca7d7c40 | -3.10072 | -50.27016 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 274aa3e9-8e30-36c2-bab7-7b9b4b2611d4 | -1.44706 | -54.4622 | 2026-10-01 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af1c8122-2a3c-3a54-956f-de25f6fe2c5a | -4.49884 | -53.95173 | 2026-10-01 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf7a2610-6458-3187-9913-ddc825236dd1 | -4.29815 | -54.79034 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b02291b0-4fe1-3e6f-b321-97ee28248c40 | -2.89153 | -54.09262 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2dc7e209-859b-37dd-b733-489a3157a576 | -3.29523 | -53.86254 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6f2250c4-c658-336c-b980-b714954daef4 | -3.51583 | -61.13453 | 2026-10-01 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a16b90f-fbf5-3d6a-8d1f-d186d062acfa | -3.07081 | -58.40549 | 2026-10-01 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccba5987-a4d0-3ecc-abb6-912ae4a90bcb | -3.85837 | -51.94563 | 2026-10-01 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c412a61-c7d6-3d3c-a7f6-9c978ee2be55 | -2.936 | -54.18638 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cba1a311-4aaf-3ecb-988d-7c7fdbb7ec1b | -2.49489 | -56.63229 | 2026-10-01 05:16:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3c1ba20-6763-3ce7-8141-8011da8ec97e | -3.48102 | -49.92337 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e20ddf56-a364-3d03-9bd3-903314d33b5d | 1.80694 | -55.62119 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d447c3c-5a22-32b8-af9e-e4935c7b42d1 | -3.17967 | -54.10398 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| e056b262-31ed-317d-be1d-e4bd63f1e1e3 | -4.26598 | -50.75257 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| f7b1b4ca-19de-377a-b353-012acdfa0b9f | -2.14931 | -58.11702 | 2026-10-01 05:16:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4324dc9e-12ab-37e0-8d6d-97b7e7c09ea3 | -4.04083 | -54.23971 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fb4fcbd9-7c4d-3e1c-a0d5-4572d032c0f9 | -1.37103 | -54.63823 | 2026-10-01 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 883ace07-19b4-36dc-b789-7d7f65b5e2ce | -4.05877 | -51.10052 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 757ce2e3-4d72-3986-8dc9-893d564ea042 | -4.30932 | -54.68906 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d804c396-b060-3a98-a4b6-9f82049b00ed | -2.15207 | -58.12095 | 2026-10-01 05:16:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e81a9be-a92d-34ed-a54b-b710ff97f38f | -3.09573 | -50.26942 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c9c35386-ce6c-37d9-936e-85a6f082f071 | -4.27669 | -50.78237 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 193.3 |
| e2414ae6-6b85-3635-917f-73e244384139 | -4.27827 | -50.77156 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 229.4 |
| 951bcf36-aed7-331d-bc50-e5efe172ecca | -3.16549 | -54.08023 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b5832d6a-2a5b-3e05-a91f-0e49ab4c71f5 | -3.25254 | -50.81884 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 215632fa-1d6a-380b-aacc-e3564b3f00fa | -4.63846 | -50.61884 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8983ae32-0bdc-3e0b-9248-ab830b2f93e1 | -3.96873 | -53.4633 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8fb4fdd2-78f9-3a9a-b948-bdf1fe0c48fb | -4.5404 | -50.7742 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02e50bfc-a009-3498-93da-05662566e4a3 | -3.72906 | -55.95189 | 2026-10-01 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7512d0b7-62e7-3448-8498-651b8b5417ce | -3.29132 | -53.86193 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b3aef154-4dec-39d2-94a1-7d614355f0d7 | -3.95951 | -49.45239 | 2026-10-01 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6451ee6f-4a09-3565-9312-5469ba803b3b | -3.96153 | -49.0562 | 2026-10-01 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c4bc73b-41af-3670-9f35-fe5233d4644d | -4.62974 | -50.60875 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a8b2bda9-392a-3e8a-92a1-1bdeeaf6d3bd | -4.25538 | -50.75652 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| fa36b076-f801-3a94-ace7-78b4bae9c2fd | -2.92815 | -54.16119 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9f746eb-5d00-3cf5-8815-7e6416c18e07 | -3.10317 | -57.91061 | 2026-10-01 05:16:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78a96ae4-377f-35ab-9d2b-fb851bdea3be | -4.26106 | -50.75188 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 01727913-6fac-32ea-89b6-d1afab17042c | -3.68451 | -60.54346 | 2026-10-01 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6909e0f-dd1f-3c85-a49a-d0dc7d84c070 | -3.80088 | -50.60912 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bb4166a8-5ab6-3af5-85a4-9535d5cde835 | -4.15834 | -48.89875 | 2026-10-01 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 456d9a29-9d62-39b5-9a89-ef4afd76effc | -4.27248 | -50.74233 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 92027dbc-ce22-30d8-affe-a046ca34a477 | -3.1686 | -54.08567 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e6bb13af-4905-32c6-96ce-e2b295c42ebb | -2.90448 | -54.08485 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11ae21ca-aa85-3260-b022-e728a1c666f3 | -4.26122 | -50.78553 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 28359d3f-860b-3ccc-a4f2-2534d5a0d8f3 | -3.2577 | -48.77431 | 2026-10-01 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48f4792f-285e-326d-bcc3-a6aeb78e8c5a | -2.46412 | -56.07684 | 2026-10-01 05:16:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fb9d947-8db6-3b7b-ad94-fabf5a57ad71 | -2.97846 | -51.04528 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 536aa70b-0f1a-3f2d-90dc-2d3538af95b7 | -4.26927 | -50.7645 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |


[Clique aqui para ver as próximas entradas](README74.md)
