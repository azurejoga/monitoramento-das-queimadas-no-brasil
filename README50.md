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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e933cd6-3f31-3c2b-93d1-bbd013c3ce7c | -2.98843 | -49.59163 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6875f424-6b44-38e7-816c-d78898ee853a | -1.05808 | -52.42308 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a130d96f-cdb3-3344-bba2-497c7c634faf | -1.79694 | -52.74396 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 44986c05-08a8-3219-9014-c1a8efb2a79b | -4.16849 | -46.71892 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46865ff5-1fba-3836-8ca2-7f95c731a4b7 | -4.69531 | -44.96961 | 2024-11-27 04:42:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09a9bd49-4ed4-3a7d-bb95-1c40a9056a61 | -3.08951 | -53.26599 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 014e90e4-d226-38d8-b9e0-3d11d3e93c7f | -1.69248 | -52.53301 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06124494-7925-3142-9474-83c753d61cc2 | -2.82323 | -52.96132 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9ecd2dc-98f0-3041-b590-0833312ba992 | -5.65077 | -46.64475 | 2024-11-27 04:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2440bef3-dea7-3970-b1ea-9302704109a5 | -3.15329 | -50.61869 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe721745-31f2-3ee1-8a87-e63b3dae28d3 | -4.30009 | -48.18042 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95408d20-4b21-3bab-827d-13113d0e6f59 | -4.64532 | -50.6805 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a97c4f22-9c01-3c4a-8d73-e57a4815d08c | -2.25615 | -53.46597 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2330ec8f-69e2-36c1-b4b1-03f053cdac8f | -2.32215 | -46.11899 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc87f4a6-a08b-38a9-ba75-44c5aa74454c | -3.80657 | -46.61108 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9545b7b4-35a0-3282-b3c6-0f0704544eb9 | -3.57087 | -41.96413 | 2024-11-27 04:42:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f0a83012-20ac-3acc-af25-2c6b904386c8 | -0.27843 | -49.8439 | 2024-11-27 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2f91370-4eab-3f37-9598-4fdda5b53673 | -1.15182 | -54.19709 | 2024-11-27 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee947d56-265b-3e64-8f89-ba17ce1a6c50 | -3.27827 | -50.01828 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3f5a41f-3c6c-36d4-8b91-52529798a5ae | -2.81905 | -51.79195 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25bb21a8-c3a5-33b7-996f-be242952654d | -3.66696 | -54.04984 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6a78e26-9e09-31f7-af94-b56961175d7e | -2.25249 | -53.46538 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df2a3780-a3a6-3fdc-a390-55fed3985ff8 | -3.29259 | -51.15575 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ff4e3a4-8b2d-3fdd-b7ed-b1623ec1f6c1 | -2.98199 | -53.8901 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26968d1a-f9b3-3417-b31a-adcdd2817c1e | -3.17767 | -48.4414 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3e1321a-cb05-3c8e-8002-b4deb0220288 | -4.21504 | -47.21725 | 2024-11-27 04:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ca00bd1-179f-3bf3-a588-869be49841e6 | -2.81728 | -54.76284 | 2024-11-27 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1bfc1b9-aa09-36ee-a3aa-18423d49ef6c | -3.04731 | -48.51514 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 4920bdb3-9387-3899-bce8-1ecf4bd613e7 | -4.14001 | -43.80641 | 2024-11-27 04:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 3190f03f-48a9-34c0-95c9-2400cf49f67d | -3.07426 | -50.96777 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 390a9d22-e7e9-3a73-a2dd-97c2a98d3bed | -3.10773 | -53.10633 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf454b72-a4cc-3703-8bae-8ad75affacd5 | -1.09871 | -53.61621 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b82d36fb-54b7-3067-9c95-0c9752c1a652 | -3.4424 | -50.01257 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc0db517-ae13-30e6-b834-c1f6fb9f8d8d | -3.08366 | -53.25661 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9786a7ed-946b-3401-a271-9de249289c7c | -1.62778 | -53.87387 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edbd235a-3dc2-31c4-9c91-000c1b88944b | -3.90326 | -50.60265 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 581e71db-b952-359b-8c3a-1acc2df4418e | -2.72669 | -48.63681 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f04c7ee5-40ff-3863-9bea-f06576de261c | -3.52622 | -53.78954 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8eed6cae-f3fe-3c75-b14b-1fb952553881 | -2.59704 | -54.25953 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2fe1d132-a561-36cc-bd04-38f09c867d15 | -2.93586 | -49.12309 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb36cf91-c7bf-3206-878c-161259d539bf | -3.2607 | -50.51915 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f2c13879-a00f-3794-a1e6-63f7792e6c9e | -4.1781 | -48.45151 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a164fe91-dc2d-30a1-a3c8-da4c9bed12a7 | -2.70038 | -51.99058 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22d3dbd8-9b91-371c-bd34-e85f8fe2ab9a | -2.69102 | -51.7161 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59112493-b63b-3ad5-937c-c19386062910 | -2.34827 | -47.64736 | 2024-11-27 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70488b89-babe-3cc2-9431-cf1645f51d05 | -1.44813 | -52.58984 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1149616-17b1-36b6-87a7-d097f529948f | -2.99364 | -51.00468 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a1c696d-6472-304a-8a04-f95afa7111e0 | -2.81548 | -46.83042 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 86f49fdb-acd8-334b-bd4e-67dc774d7e7f | -2.68446 | -48.59713 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ae5fb70-9760-3fe0-a095-56529837a1b8 | -3.25414 | -51.14229 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbceff0c-d147-39a2-9441-2245de5d8b6c | -2.17721 | -52.74243 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98de84bd-093d-3341-bcce-0f88d11675b6 | -3.2101 | -53.37659 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8d48b30-0a28-36be-aa0d-cc8123dca005 | -1.48928 | -52.53553 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66f88c29-9c42-338c-b265-27aeb7550358 | -3.25081 | -51.14178 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb01e8a5-f6b1-376c-9ee3-6fb8f7833005 | -3.15927 | -50.5808 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3061fd2f-157a-340e-9b33-4b8cbe5a5f89 | -1.44687 | -52.59782 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3f7290a1-d3a8-3cd3-96e3-9973490bf00c | -1.80049 | -52.74452 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7520ccc3-718a-3ead-a589-dab956764186 | -4.23449 | -48.698 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c17fbad-ab8d-3bdf-a247-7d0b675c65d3 | -3.54342 | -50.19042 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eca9d0a0-0235-37cd-960e-85c9137d3011 | -2.80542 | -52.91356 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5cd98bd4-2f1e-3b01-be48-a558f37e29f7 | -4.62419 | -48.02635 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 099ddf0a-89e9-3eab-9edb-5e791850adc0 | -1.67516 | -52.43811 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b9735bd-e0da-3ba3-882d-dbe1ff986e30 | -1.49322 | -48.02965 | 2024-11-27 04:42:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a28474b5-dfd0-3572-82ad-2c7993e2d370 | -1.06268 | -53.01297 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac65966f-381a-3ace-8055-5017a9da1964 | -1.19663 | -53.88242 | 2024-11-27 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffc1eb1e-e817-3443-975d-ddff287e2a4b | -1.21447 | -54.53736 | 2024-11-27 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cebc9a1a-ab28-33cc-9512-ac39a208416a | -2.41182 | -53.84608 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 846cbd99-297b-329e-8d1a-fc1d6486c3a1 | -2.64573 | -51.76092 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a475484-a0db-36d7-a8f9-560fce0b20d5 | -3.59354 | -50.38836 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c776f82b-c6e6-3aa1-8560-a65a7c6944ca | -1.48223 | -52.53438 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1428936-d05c-3f0b-be5e-360405693c92 | -3.0575 | -53.28195 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1d4b275-b9c7-3b48-9021-e41b706e017c | -3.49465 | -50.45744 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4902bd34-9043-38eb-8244-2e1adb3df4b2 | -2.60178 | -51.79153 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56819852-0edd-3f0d-a785-f4ead4d1d25b | -4.33951 | -48.65395 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cab78c2a-a810-366c-abf8-65b5f50adb5c | -3.4985 | -50.45451 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cc664dc-342f-3bda-9775-4ab77a86416f | -4.25208 | -48.67442 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4f635d2-0ab4-3486-a75b-df1935fbc57e | -3.75255 | -52.65072 | 2024-11-27 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cb6a84c-481b-3400-bcd0-2b0ac0f36582 | -3.11529 | -53.26582 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 200dd9db-0e14-338e-9a34-b93c6888189a | -3.44724 | -49.50293 | 2024-11-27 04:42:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d22da99-164c-3a47-82d3-23bc9983d753 | -3.94325 | -46.88906 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad152187-aba7-3201-a899-b8a9aad19190 | -3.27429 | -48.76453 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8497ee3-bfaa-337a-b0a9-fd2de2614b2b | -2.02398 | -51.18765 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07e6ac91-0ed0-366a-af87-ee50f7946be3 | -1.24111 | -51.61911 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d0f334a-ce75-3646-9d5a-37cf2a0c0c45 | -2.42745 | -53.84411 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a2897b0-11b3-307f-8da0-8c34d433bedd | 0.32694 | -49.7173 | 2024-11-27 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74e0f793-2542-3b72-8a22-2a5ce684e53f | -1.56197 | -52.78775 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6b60ef9-48a3-335f-865f-04cac9809711 | -2.9457 | -48.55891 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 288b1e91-71fb-3346-bf60-94c2a0aca2a5 | -3.10164 | -50.36353 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17da7c21-2f0a-399b-a068-a6fd4c18f05d | -3.8508 | -51.3867 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 157bade3-d64e-3d00-828d-a3f4f3ed26a8 | -1.91862 | -48.6992 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4694bafe-d062-387a-88e3-f4584d63f5b0 | -3.53923 | -50.45383 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5350e513-2f45-3bb5-b247-9c3e25d99b04 | -4.23448 | -48.67546 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9a76f00-02ec-3c80-98b9-90e892d318ad | -2.84827 | -46.83864 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f2a2a4b-b942-3464-864d-960210a80e08 | -0.9956 | -51.72927 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 872e9d0c-fa23-3a94-bffc-2179df0720f2 | -1.76741 | -53.62483 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9302c003-8f51-36be-bdd6-e7f5dd605518 | -1.65599 | -55.23556 | 2024-11-27 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47a26f2c-c701-3a3f-8663-5d91195440d1 | -3.84059 | -49.89781 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be5fb02a-7755-3de5-b94d-a73c35de6839 | -4.20671 | -50.89748 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ac31019d-f06c-3430-a190-1b461545ef1c | -2.78784 | -49.20409 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cc82e44-1db1-306d-b588-16cafef87180 | -4.17899 | -48.62597 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README51.md)
