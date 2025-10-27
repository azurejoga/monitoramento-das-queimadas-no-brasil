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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9bade64-a082-397d-8e7c-a51a7088b1bc | -8.32043 | -46.17509 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f40c8e09-bc7e-3a1b-b022-c54f5ae6652d | -8.5695 | -47.39195 | 2025-10-27 04:32:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f7cb8d4-6001-3023-8bd6-16dd1e9a8220 | -7.83747 | -46.46862 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| fe857baf-775e-31b7-b7af-8378de96dad6 | -8.06958 | -46.94931 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| faf61a20-4f99-3e59-b13a-3d046a936971 | -5.00351 | -44.923 | 2025-10-27 04:32:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb301ea7-f9c4-3647-ab4f-96c5b57394c9 | -8.87881 | -44.84097 | 2025-10-27 04:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47953f2e-f0e3-3d39-97b9-18424d99f215 | -5.60451 | -47.09821 | 2025-10-27 04:32:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d5858213-464d-3f10-a100-31130db0cd33 | -4.48426 | -43.41983 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 99afbacd-5db3-3e25-9bfd-4d50b71e08d6 | -3.75545 | -47.5851 | 2025-10-27 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48b96f82-5a17-3655-b970-e5399d5d42be | -6.55395 | -41.60059 | 2025-10-27 04:32:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6ab24cf4-23bf-31f6-a8f9-27dbd7f9befb | -5.89281 | -41.32229 | 2025-10-27 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2ebd83a5-a3de-39d6-8ba2-e1850fbc9b0d | -7.06052 | -47.38422 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6641f559-c475-3308-b115-3540cf0c8761 | -6.10789 | -41.74398 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f7be52e6-6c55-3aac-b22e-49e1248d0c0f | -7.68172 | -46.33664 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcc256bb-3684-3ac6-a627-e6f6a3d83e21 | -8.52639 | -47.20864 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e43302b5-a00c-34ca-b049-ec2bb8c90ac3 | -4.44611 | -43.41859 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9850c762-0094-35cc-a327-41d88361938f | -7.89582 | -47.23999 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27875bb8-841e-3e3f-8659-896b7e985f2f | -3.47249 | -49.96967 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a5d73c9f-8cbe-3738-851d-6645629c053f | -6.23473 | -42.54632 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 99bca2db-73d0-3401-93c0-4c99ce03dcf2 | -6.25406 | -41.84196 | 2025-10-27 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d9cca8b1-7bb8-3239-a2da-0a561828ed1e | -9.46648 | -47.727 | 2025-10-27 04:32:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d42bbd29-fde8-31f1-bda3-b886125d6221 | -3.12196 | -51.20767 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9050f248-9218-3e9c-b497-0786ceb43f82 | -8.96073 | -47.19239 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 18ade632-ca0b-3427-a796-dc28fa25b73f | -7.04217 | -45.72368 | 2025-10-27 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 357132c7-6ffd-3ce3-a810-0a6c4f470129 | -2.22569 | -51.87395 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 166dd68b-4846-3dbd-a740-367c25804b52 | -7.84129 | -46.42085 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d7d89c1-1c2b-38fb-9af5-a1b13234c9b2 | -6.34985 | -44.63747 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f1a18bb-c13c-362d-8745-fea9e334c7f8 | -8.53169 | -45.56421 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e51b67df-11f3-389e-8cdb-408249129aa7 | -7.83298 | -46.47534 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 75b1454a-b77c-307c-b7a4-e0eaa8723e20 | -9.9889 | -47.17824 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc8f77dd-cd03-39bf-a0b5-dd4def72e3ff | -3.22821 | -50.20527 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79eb14a4-8fed-3a8c-85ce-3d6a6735ed34 | -8.6978 | -50.81124 | 2025-10-27 04:32:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 59d87664-5ec1-36b0-b677-3db5b2465d9d | -3.21582 | -44.43247 | 2025-10-27 04:32:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0aec3df0-5722-3160-a780-ee5dddf38157 | -4.48275 | -48.67311 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| faceb491-41de-32fc-8c6f-aa17be118d38 | -2.23161 | -51.99572 | 2025-10-27 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ea95631-d47c-3f3d-bf14-c2263fd897c9 | -4.26499 | -50.50375 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d092a03-f661-3b0f-8fcc-c006ac2779ef | -3.13151 | -50.15288 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22eb9e19-d5bb-36d4-923e-989d0a5f0e2d | -5.64427 | -47.62638 | 2025-10-27 04:32:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d3316f4-ad53-3dc7-9a61-175e1ad9ae92 | -3.42519 | -52.6274 | 2025-10-27 04:32:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b77ae45-a430-3c2d-9d48-8859d7f8a6cc | -9.25447 | -45.57274 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15ff4bae-b544-347a-ae19-6ed38140f530 | -4.45294 | -43.42422 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bb200e9-a4ce-355c-967a-db289b96241b | -7.83643 | -46.49807 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9d55fd69-74bf-3307-a1c1-0ae580f3832e | -6.45003 | -42.34963 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 80bbf17e-2520-3fd4-a32c-2b0bfaa0f337 | -3.57041 | -44.52836 | 2025-10-27 04:32:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e324d7db-3025-38ff-9dd2-5e11b915db6b | -3.11793 | -51.21359 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73549898-645c-38ec-8dda-73683dc15111 | -3.4269 | -52.62726 | 2025-10-27 04:32:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a92bdf9-bd2c-3d1e-8961-67e72b6f84bc | -7.85085 | -46.40359 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 289ba8f7-1af9-3400-8df3-c94a53759e0b | -9.5838 | -45.18421 | 2025-10-27 04:32:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a99e5995-2da3-33bb-bf88-d0262fcc1a5a | -4.43482 | -45.97839 | 2025-10-27 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad49725d-1953-3db3-9496-2c53db2b4947 | -7.84074 | -46.42448 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca368312-f9c6-3a44-abce-da3ac129baff | -6.16105 | -41.55569 | 2025-10-27 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| beec415c-736a-3268-8ea4-2db40b24f0f3 | -5.33511 | -44.71722 | 2025-10-27 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abddbb2a-245a-3752-9a72-f3f6790a18b9 | -5.2467 | -48.80874 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 095849e4-627f-3df7-9386-5a3c8814a12b | -2.68219 | -51.88916 | 2025-10-27 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e326085b-78c7-38f5-8248-5d814f50ec2f | -7.82905 | -46.47848 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb742671-a4ed-35f2-baf7-ffe189420fd8 | -9.62589 | -45.48347 | 2025-10-27 04:32:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fd211837-df88-36af-9c63-cf6d98853a52 | -3.88274 | -52.24654 | 2025-10-27 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c93abb3-0b75-3f69-817f-58edf3544914 | -8.6535 | -44.77102 | 2025-10-27 04:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f995598a-92ec-3f33-9f1d-0ee0ac4b6806 | -4.95191 | -44.87629 | 2025-10-27 04:32:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1feff198-12aa-3b8f-b0d0-514ff26972d7 | -4.17954 | -48.19873 | 2025-10-27 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1386b2c1-6320-3d7d-8ec3-59ccf3bdd73f | -6.69612 | -43.99449 | 2025-10-27 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9c9e724-d419-3509-b97a-db402ef0aa71 | -4.81417 | -38.64509 | 2025-10-27 04:32:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c00a8540-5521-33cd-b9d7-45ddf249b48d | -9.11567 | -45.84931 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4ed92cd-352f-3ad3-9ee4-e90833fbddcb | -8.07238 | -46.9534 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8741d6b3-0b7d-32e0-8617-9394e4a2d009 | -3.71544 | -47.64592 | 2025-10-27 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a4daabd-1d71-3df4-bf47-aadcfca26501 | -8.21767 | -46.93914 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03257eb6-d0b7-36f0-897c-5d991ffc50a3 | -3.72858 | -49.68508 | 2025-10-27 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2e1e8b52-0c3a-3fdc-8245-df2f2d944cb1 | -5.0347 | -41.18793 | 2025-10-27 04:32:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e90142a3-308f-327b-952a-93a3c97c1f2c | -4.48223 | -43.4334 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aab73d83-b839-369d-bbfb-e97da7acec4e | -8.11653 | -47.02196 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3122ab8-20fc-3b8b-9192-8be2b0e6a6bb | -3.39296 | -50.39634 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 001d3523-0baa-3fd6-90a4-a3ceceaca977 | -6.08612 | -47.00026 | 2025-10-27 04:32:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53bfa24b-a904-3eec-aafb-f3adff62cab1 | -4.28321 | -49.66648 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 543a2cf4-2e76-3858-a9de-69bd3125bdce | -7.16202 | -44.85238 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49891491-f41a-3797-98a2-05e98dd6eb6f | -3.07622 | -49.47822 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9c780c4-4fd8-36e8-8438-feb37ab576c5 | -4.87005 | -48.524 | 2025-10-27 04:32:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 953a1805-7015-3817-8002-5370ba764c8b | -7.05117 | -47.22622 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 841f7fac-b426-364c-b197-617904baa71b | -7.43359 | -41.87416 | 2025-10-27 04:32:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| e26dc619-5ed2-36a3-819e-6f10b22642f3 | -4.85133 | -46.73607 | 2025-10-27 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24ab8de0-1e29-388f-851d-f7b8da2b2d70 | -8.27068 | -46.8776 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8b3224b-70c8-3b16-ab45-02c26e879780 | -4.3946 | -43.32034 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 9cd62758-46b3-3730-a154-563168057913 | -3.05016 | -53.01222 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b659c1fa-2331-3eff-a5c6-8fd3df6c3931 | -6.88265 | -45.16373 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8658500a-03d6-38be-b282-d0ec4e63c680 | -8.323 | -46.82704 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6606e0f-0408-37c7-9f69-9ad96a345bbf | -4.48494 | -43.41531 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8912a5b0-912c-356f-b0df-7bb0c48360ae | -4.56168 | -46.34496 | 2025-10-27 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aebf9b4f-a277-3566-b867-4e3d538a14ce | -3.51636 | -49.23379 | 2025-10-27 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42cdc616-e3bc-34aa-8179-e9b4900269a1 | -5.63377 | -50.31849 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6159200-6a1a-3666-a684-51401f631b57 | -9.12357 | -48.24715 | 2025-10-27 04:32:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a8fc805-5b79-36b5-b461-2c66eb5541bb | -5.77547 | -42.97312 | 2025-10-27 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 45909b3f-fdcc-359d-985b-2e995eec326a | -8.53228 | -45.56025 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1c5b7b9c-39a3-344e-bf9b-47c239b287d0 | -3.95775 | -43.31326 | 2025-10-27 04:32:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3a2ca937-3ba8-35ab-bc4f-c3d4d68bbc78 | -5.26568 | -50.97745 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccb71115-a442-3e66-bf23-77105c8e41d0 | -6.10617 | -41.75614 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ed20e6c7-7fc5-3559-b0e3-9ac9c88eb0a1 | -7.87333 | -45.72516 | 2025-10-27 04:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64e09bee-dbee-3c25-8d34-485b1dba8f3d | -3.61565 | -42.7812 | 2025-10-27 04:32:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61a97ec9-5968-33f9-8251-b85c7f213db3 | -7.33683 | -47.13809 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c906cc9-718f-3457-a708-24fb93c66028 | -5.59542 | -41.32366 | 2025-10-27 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ee6c1ec9-7beb-37e7-aa55-ec7a8eced721 | -7.85668 | -46.50117 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b7637d1e-dded-3df3-914c-12c8ee84dbca | -3.86499 | -49.8057 | 2025-10-27 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README29.md)
