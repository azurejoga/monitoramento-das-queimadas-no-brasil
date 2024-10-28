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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0eb8631d-a417-3ef0-95b1-2330f29815f0 | -3.85601 | -51.70242 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f84fc09a-6add-3414-8305-0d25c463bef6 | -3.85204 | -51.6829 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af8c8b66-cf6d-3269-bd53-db2d15d3114b | -3.83962 | -51.89842 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ef4f4361-1561-361e-a4d1-92c9464b0545 | -2.67037 | -59.42816 | 2024-10-28 04:57:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e228c75c-73c5-3f7e-9803-60e5610c7766 | -2.20387 | -60.16698 | 2024-10-28 04:57:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cf54e896-6e2b-3336-8eaa-e9089d03df12 | -3.83905 | -51.90206 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3aa17a2-0c95-34d9-9881-86256cc2dbd0 | -3.83296 | -52.14102 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0e96969c-fac6-33a9-8046-83863d62efc3 | -3.82572 | -52.23129 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa29f339-4b73-3132-afe7-48f9bd83c8c5 | -3.80507 | -52.25354 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b651a5b8-d032-3f70-b8f8-d51731ed4662 | -3.80452 | -52.2571 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 654bbb7c-1e62-3ada-a6bd-f227e1e2c6f4 | -3.80372 | -51.6081 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f98f7dc-7064-3e42-81c6-b809c935bd97 | -3.80009 | -51.38198 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 410e3d57-291c-3cc8-891c-765d95a8eded | -3.79952 | -51.38568 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84962f3f-f19a-3018-9bff-5506ae3a2213 | -3.79663 | -51.38152 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0bb6afea-6c5d-3bf3-849a-f42591623868 | -3.79606 | -51.38521 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7f433b10-675f-3606-b2fc-70701e1a9566 | -3.79318 | -51.38099 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d1562c6f-1dcc-3edb-a33c-062c155f9c80 | -3.79032 | -51.3767 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35c0accc-abe3-3c72-a479-6a2aff4039be | -6.12871 | -52.162 | 2024-10-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 85bde82a-889b-3eb6-98ea-4f4722ae5642 | -5.39211 | -51.0892 | 2024-10-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17bd8638-1c6d-3537-bb54-a7192be6811b | -5.38857 | -51.08864 | 2024-10-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f566ea2a-b4bd-3911-bb28-ac0c80584adf | -5.38502 | -51.08809 | 2024-10-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b60d0ce-5077-3fee-a2cb-0f71ae3d51e3 | -6.90266 | -52.71711 | 2024-10-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0bd4781-5260-3208-a2ab-ee6f405af754 | -6.89985 | -52.71294 | 2024-10-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4e6c4c3-c8c0-36e9-9427-504dd3494c56 | -6.89929 | -52.71658 | 2024-10-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 751e21b3-cc95-3bba-9211-81079220a64b | -1.67446 | -53.32083 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4246e49-3013-3ebb-9f4d-c05241b497e7 | -1.61623 | -53.32586 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88df8e01-34a7-34bb-9a58-19e0116a82db | -1.61293 | -53.32535 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3805b13e-013b-3d48-aec9-c0b35c5fc7b3 | -1.60357 | -53.32038 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a60e2682-d4db-379d-a2a3-a3bc4638920c | -1.58913 | -53.34259 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d937c2ce-8600-3a23-9728-4ca66e9acca8 | -1.58583 | -53.34208 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9f3da7e-af48-36ed-8395-2491f029682a | -1.26485 | -53.13359 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47a4abca-dceb-337d-b88c-08fd8cbfd334 | -2.21667 | -51.99018 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57e40a1b-6619-3bed-a2d7-5a950dd65387 | -2.17594 | -51.96579 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c5bd1e3-f4f6-3e5a-8f79-ad59cd08bcd9 | -2.07207 | -52.02216 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56202e8e-5323-3412-a5ab-638f87660347 | -2.05959 | -52.16759 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abffdd47-f519-36e5-adc3-8bd267b4f8d5 | -2.05681 | -52.16357 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a13526c-accc-373e-ba60-2c431e767c87 | -2.05626 | -52.16707 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| f8f1b963-110a-3889-97e3-a9d999cbfd52 | -2.05571 | -52.17057 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 371a254c-4742-34c1-811b-6f286122f4a6 | -2.05368 | -52.00849 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ebeed7a-d2b5-343b-87c2-dd1e2afea6eb | -2.05348 | -52.16306 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b926a97-cc48-3160-b89e-8f9c7a5a6ec8 | -2.05293 | -52.16656 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 992c3e62-f2a1-31b3-bc4f-0383e400b748 | -2.05238 | -52.17006 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 7dd1ecf7-510a-342b-bf4c-81b7b092ca87 | -2.05034 | -52.00798 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8467e82b-dbd9-3fcc-8435-47fd4708fde0 | -2.0483 | -52.08689 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7c2bcae1-3d16-3173-b52c-5e7dc830fe76 | -2.04776 | -52.0904 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d5fcd6b5-5533-3eff-a278-f3a716bcf11c | -2.04661 | -52.07584 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 806d2ead-8585-311f-a20a-1aa790566c30 | -2.04606 | -52.07935 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f0802b36-2b96-35f3-b990-ebf9e3074784 | -2.04551 | -52.08286 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f198027e-ad12-39d7-a293-feac91cfef31 | -2.04497 | -52.08637 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f6728d96-6a33-3501-9c82-7e331654f086 | -2.04442 | -52.08989 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 57b43fe5-23f1-397b-98dd-f49c15c6e54e | -2.04327 | -52.07532 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 042eb606-09f1-3096-9269-563848a9ea67 | -2.04273 | -52.07884 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 968aad92-e0c5-3565-a791-1affca92d0f2 | -2.04218 | -52.08235 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3cd67730-1582-3a94-a2f8-7c9a763e59d0 | -2.04163 | -52.08586 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| caeced66-8e82-384f-8c62-9f128871c65b | -1.99756 | -52.08593 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f3e3ffd-8b48-356d-9bbf-df58202d596c | -1.98756 | -52.08438 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d39fd4b8-a54f-3b4d-83b7-84d09e78d78f | -1.98532 | -52.07685 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c2d6312-bb03-33aa-8487-08b869e88231 | -1.98477 | -52.08036 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30b6c709-94e9-387b-9b38-3708acaba5fe | -1.98422 | -52.08386 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb402889-b75a-3e72-bd8d-b60535f08710 | -1.98144 | -52.07984 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 32f76178-e236-3974-9392-334c3cab0b3b | -1.98089 | -52.08335 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| ed25786b-4316-3a12-9daf-a9ea075f4e5e | -1.98034 | -52.08686 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| fb722aa4-108a-3500-a723-e055bc0c6001 | -1.97811 | -52.07933 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| cdee3664-15ba-3ba0-bc4d-5cd2e98b8d8f | -1.97756 | -52.08283 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| d526d952-d8d1-3713-a993-7945816d4027 | -1.97701 | -52.08634 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 1f40d886-4c2c-327b-aa94-8f7b132c3e16 | -1.95394 | -51.94947 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96c742e5-eaa9-3a76-a1da-1277dbb77d3a | -1.94973 | -53.06254 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb6ee3a3-70be-3f13-ba8e-cf3eb96d55a0 | -1.92657 | -52.12518 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72f2cfa3-a02a-36de-8113-a0dfd8f6c793 | -1.92603 | -52.12868 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d20f25ee-70fa-3f3e-b53f-73f38eefbe64 | -1.92548 | -52.13218 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9e502f3-bfea-3bf4-8e83-f537f6f9f4b4 | -1.92494 | -52.13567 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5668324-968f-3eb1-aede-210ded582303 | -1.92324 | -52.12466 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b3526ab-0249-3b66-bdb5-84489558783d | -1.9227 | -52.12816 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dfa2bd8a-af35-3714-95c4-3de6a0811b1a | -1.92215 | -52.13166 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa07c6b0-0c2e-366d-bd62-4330694729e7 | -1.92161 | -52.13516 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcb47645-a8ec-37c0-a7d5-6627445a7da6 | -1.92082 | -52.05248 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1c845e6-a109-3760-b077-8941854b6611 | -1.92027 | -52.05599 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 21b659b1-5947-3a32-b883-99aab0ed089f | -1.91991 | -52.12415 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cac205e-0289-3572-99d1-253edd73f4d6 | -1.91937 | -52.12765 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6383ce02-8fa0-3d04-b149-1c3861bbebbe | -1.91882 | -52.13115 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a87fdc78-7253-3e59-bd1b-9625dc54ba7d | -1.91803 | -52.04845 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9df37b81-a3eb-38b9-8f31-85fd2fd26873 | -1.91748 | -52.05197 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48160874-be8c-3c80-bc11-7b59f9d574a4 | -1.91694 | -52.05548 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a5f71f4-ef23-381e-b913-1e29d105c803 | -1.90499 | -52.32889 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ee6990f0-b950-346e-88d4-fffd3d7eff1e | -1.90167 | -52.32837 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fac69612-eddf-3518-98ab-1bc355570f35 | -1.90113 | -52.33184 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fbb7e11d-b1b0-3f12-81fb-b4cdcf27b28f | -1.89781 | -52.33133 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5981c29-a983-3603-b2e5-c2eeaf45ba1f | -1.82226 | -52.42245 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c77cb4a0-3f88-39c3-92c7-4b8339465447 | -1.8185 | -52.25134 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b17e1b3-4be1-3104-bab8-5814071ee96e | -1.81059 | -52.19304 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d19f4346-f728-3f11-871d-f2124461862e | -1.76993 | -52.04005 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f8fc493-ab2f-3f5a-87a0-b4aa15d8fd4f | -1.76604 | -52.04304 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f0497a5-9616-3a1a-ac9f-af0c5b83961b | -1.75678 | -52.32006 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7a06ef2-7cad-350f-9464-7c8787d92ebe | -1.75624 | -52.32353 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 103842e5-b9c2-3e2d-8a89-aba11d2fafd4 | -1.75491 | -52.02696 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01b87d74-d78e-3b3e-aa29-747e0b3b7d39 | -1.75325 | -52.31956 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0d0012f-58b3-3d86-9888-1827cc1a7dd0 | -1.75048 | -52.31558 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45677292-3b57-381d-961a-aa73baf05a1c | -1.74716 | -52.31507 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 307eed60-e732-3f03-b51c-b76ba6b4fe47 | -1.74334 | -52.33933 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 510a2d98-8bfa-3e0b-8ac8-3c11a3ecf893 | -1.74003 | -52.33881 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README63.md)
