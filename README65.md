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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 032e87c2-ea9f-3005-b26a-b5c90eeb8c3a | -17.7848 | -57.4885 | 2024-10-23 09:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 312.5 |
| 219ca6bd-171f-3fb4-9491-ce579b9db12a | -17.7844 | -57.5091 | 2024-10-23 09:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.2 |
| cd19d5d6-a067-3264-b9d4-b6baf6fd8a91 | -19.5469 | -56.6773 | 2024-10-23 09:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 201.2 |
| 5da364ad-49fd-311e-bfd1-2d57dda51cf2 | -19.5465 | -56.6983 | 2024-10-23 09:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 113.8 |
| 5fd26127-a4a8-3d8a-9149-8addcb4ddcc3 | -19.5473 | -56.6563 | 2024-10-23 09:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 131.2 |
| a69e5d9c-9fc0-38a3-8276-ef220dcfc2de | -17.7848 | -57.4885 | 2024-10-23 09:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 171.7 |
| 75610b55-cb5f-3efa-b701-bee5ee618be4 | -19.5469 | -56.6773 | 2024-10-23 09:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 163.0 |
| 965a4628-1a94-3b61-9b9d-842a12f3d6e2 | -19.5465 | -56.6983 | 2024-10-23 09:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 120.4 |
| da25d39b-d6c9-3160-ab40-6d2e8f2d8da4 | -17.8045 | -57.4861 | 2024-10-23 09:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.5 |
| 104db509-6daf-3e3f-ac2c-157f124eaadb | -17.6868 | -57.4593 | 2024-10-23 09:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 154.3 |
| 0ea61a99-da56-39a3-ae5f-21dd2e496ad9 | -17.7848 | -57.4885 | 2024-10-23 09:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 174.8 |
| 989029f4-b4b3-3186-b4a4-d56dec14cb5b | -19.5465 | -56.6983 | 2024-10-23 09:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 132.2 |
| 5adf21ac-c2f0-3d84-9a98-3feb665d5aa4 | -19.5469 | -56.6773 | 2024-10-23 09:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 195.1 |
| 701b2c2f-3371-3df4-8f32-7605ce18b6fc | -19.5473 | -56.6563 | 2024-10-23 09:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 112.2 |
| 26f1cbb8-d221-3970-8043-f2f3a4a599e7 | -17.6868 | -57.4593 | 2024-10-23 09:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 142.3 |
| 32a71a96-94e6-3395-bff4-4f71735fe040 | -17.7848 | -57.4885 | 2024-10-23 09:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.4 |
| e5858871-9884-3170-879d-067ccc35446d | -19.5465 | -56.6983 | 2024-10-23 09:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 123.4 |
| d47455bb-7276-35ec-a914-f74d43a12798 | -19.5469 | -56.6773 | 2024-10-23 09:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 176.1 |
| a383f0e2-8c92-363f-9927-43d50422b35b | -17.6868 | -57.4593 | 2024-10-23 10:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.8 |
| 5051e149-ccf5-30a7-86fb-91dbd293a168 | -19.5465 | -56.6983 | 2024-10-23 10:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 107.7 |
| c7b80c3b-dd25-3fa7-9ef5-2cf6649ffcb0 | -19.5473 | -56.6563 | 2024-10-23 10:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 121.3 |
| 80985075-246f-3155-bc6e-e07c46eb8ebd | -19.5469 | -56.6773 | 2024-10-23 10:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 177.2 |
| 67f363b4-659e-3cfd-a0fa-dbf8a3b77704 | -19.5465 | -56.6983 | 2024-10-23 10:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 135.8 |
| 32be38d4-8777-3be2-90b8-fa69e6a4c5c0 | -19.5469 | -56.6773 | 2024-10-23 10:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 211.0 |
| 96ef5265-e8db-3221-90f1-b39fd1663e9a | -19.5473 | -56.6563 | 2024-10-23 10:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 130.7 |
| 6e1fa01d-a6c1-3d13-9b13-0f8ffb3121d5 | -17.6868 | -57.4593 | 2024-10-23 10:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.7 |
| 1c76d239-912f-3d28-92aa-8a4ed1153ce5 | -17.744 | -57.5756 | 2024-10-23 10:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.6 |
| 98674fa4-711d-3735-95bc-b15aa92f9e96 | -17.7637 | -57.5732 | 2024-10-23 10:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.2 |
| c5794c3f-aa0d-3e64-b5fa-a7b5d28e9bb8 | -19.6249 | -56.7919 | 2024-10-23 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 112.2 |
| bbb1b106-1c53-33c7-adc3-9a424d055fbb | -19.6245 | -56.8129 | 2024-10-23 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 252.3 |
| ccaf65a7-731e-3568-be4e-c16e7852a830 | -19.6241 | -56.8339 | 2024-10-23 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 120.4 |
| cd15cacf-c062-30a2-848d-ea75dad836e2 | -19.6044 | -56.8157 | 2024-10-23 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 178.6 |
| 30648590-1e46-3720-a94f-439d3e00674e | -19.604 | -56.8367 | 2024-10-23 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.2 |
| 07cc391b-d54b-3aaa-9075-355f69c976c0 | -19.5473 | -56.6563 | 2024-10-23 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 134.3 |
| 99e2ea1c-2bf3-311a-a1c5-324b68b8f4af | -19.5469 | -56.6773 | 2024-10-23 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 211.1 |
| c2da6fd1-39d0-33bc-afd9-4e66c69a84ed | -19.5465 | -56.6983 | 2024-10-23 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 128.8 |
| 3b32c63f-9467-3aca-b2f8-1128b89b66c1 | -17.7637 | -57.5732 | 2024-10-23 11:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.0 |
| 5c60a485-0f5c-39d8-b03b-1c2bffb504b0 | -17.6868 | -57.4593 | 2024-10-23 11:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.1 |
| c2dfef58-31ab-3be7-bcd4-e63486ead1ef | -19.5473 | -56.6563 | 2024-10-23 11:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 144.1 |
| df65797d-01df-3159-9ac1-78b62e031859 | -19.6245 | -56.8129 | 2024-10-23 11:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 302.2 |
| 5760223b-38b1-3bb9-974c-e000c32c18b9 | -19.6249 | -56.7919 | 2024-10-23 11:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 115.4 |
| 4a2185fa-9302-3ca4-b2d7-4790e4d5d443 | -17.7637 | -57.5732 | 2024-10-23 11:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.5 |
| a49cabc3-9c34-399c-8328-ec2266223428 | -17.6868 | -57.4593 | 2024-10-23 11:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.0 |
| a1b471ed-1cd6-354b-b2d7-692c65cf0965 | -19.5268 | -56.6801 | 2024-10-23 11:16:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.7 |
| 43b2bd97-cf7a-3c61-98cc-0b8a0c25bb38 | -19.5272 | -56.6591 | 2024-10-23 11:16:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 632e9f43-54c3-311e-851f-7a8c839f556f | -19.6245 | -56.8129 | 2024-10-23 11:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 303.3 |
| 5799da7e-4173-3000-93d7-fa5c23043b4d | -19.6249 | -56.7919 | 2024-10-23 11:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 114.4 |
| 9fcebf02-d41c-32df-bee1-c0ade9750726 | -19.5473 | -56.6563 | 2024-10-23 11:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 147.7 |
| 355559d6-822f-36ca-980f-4e86cfa3064d | -17.6868 | -57.4593 | 2024-10-23 11:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.2 |
| 2d9b599b-5fd4-3cbe-bbac-759c535eac9f | -17.7637 | -57.5732 | 2024-10-23 11:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.6 |
| 6e57739f-db45-3836-b22a-9e1407ec486d | -19.5268 | -56.6801 | 2024-10-23 11:26:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.6 |
| 982a10e0-3a16-3076-9436-76b124ff7b7b | -19.5272 | -56.6591 | 2024-10-23 11:26:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.5 |
| a6d98db1-1c2c-38c0-8442-6249cb370b19 | -19.6245 | -56.8129 | 2024-10-23 11:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 280.3 |
| dfadf024-accb-3a4c-bfa7-50e7c02b950e | -19.6249 | -56.7919 | 2024-10-23 11:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 109.5 |
| e88065c3-0163-32fa-abff-194402400bcc | -19.5469 | -56.6773 | 2024-10-23 11:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 211.8 |
| b56dd209-38cf-32b6-83c4-f631bd82f20a | -19.5473 | -56.6563 | 2024-10-23 11:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 157.4 |
| 11d78e5b-1135-3ba0-b7a6-3fe17ceb8f41 | -17.6868 | -57.4593 | 2024-10-23 11:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.0 |
| 299888f3-b987-3fb1-a8c6-25b22a5af809 | -17.7637 | -57.5732 | 2024-10-23 11:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.0 |
| 28032445-9b80-3609-8848-9375949e4f72 | -19.5272 | -56.6591 | 2024-10-23 11:36:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.3 |
| 84702fb0-d6d9-318a-911b-bbc12b210b65 | -19.5268 | -56.6801 | 2024-10-23 11:36:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 6c94398c-a4f7-3424-926e-418b9a8358b1 | -19.5473 | -56.6563 | 2024-10-23 11:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 184.1 |
| d577d5b8-a6cd-36a7-8ee8-56338bbf3afc | -19.6245 | -56.8129 | 2024-10-23 11:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 399.4 |
| f659a9f1-59b7-3546-98e8-c30d9fc280bc | -19.6249 | -56.7919 | 2024-10-23 11:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 125.3 |
| b323b06e-de05-3859-92d4-60883dc2a145 | -19.5465 | -56.6983 | 2024-10-23 11:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 168.7 |
| 85c1272f-fea1-30ad-aa8c-730f972e5f16 | -19.5469 | -56.6773 | 2024-10-23 11:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 249.7 |
| 69bf31b6-b995-305e-9798-ec9f293a3bbd | -17.7065 | -57.4569 | 2024-10-23 11:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.2 |
| 5e3e7917-5f90-38c8-bdd9-1f53d9faa24d | -17.7848 | -57.4885 | 2024-10-23 11:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.2 |
| c1ddd536-f67b-3444-bd79-3805b5164410 | -17.7637 | -57.5732 | 2024-10-23 11:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.8 |
| 6d1d3066-3488-3a5a-bb95-af2b5f0f8e4d | -17.6868 | -57.4593 | 2024-10-23 11:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.3 |
| 844dd671-3e7e-3737-8e25-e0fffe5523fb | -17.744 | -57.5756 | 2024-10-23 11:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.6 |
| 1fb7fba5-90cc-3aef-90eb-6231ae385bf3 | -19.6253 | -56.7709 | 2024-10-23 11:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 6eb1626a-7e87-3dbb-8dd6-190d44897313 | -19.5465 | -56.6983 | 2024-10-23 11:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 169.4 |
| 8c6acba8-f52e-3a51-a86f-b74df113aa85 | -19.5469 | -56.6773 | 2024-10-23 11:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 275.1 |
| a9305ce8-4f0f-3b25-afae-6f5d1ab29ce3 | -19.5477 | -56.6353 | 2024-10-23 11:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 2ddc09b5-c76e-3877-abd4-5debfe2ef0de | -19.5268 | -56.6801 | 2024-10-23 11:46:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.8 |
| d6f22d14-86fb-3c58-aff6-aae7b0f52f5d | -19.5272 | -56.6591 | 2024-10-23 11:46:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.6 |
| 2b4dbf4d-20d0-39c6-a613-7ef5a4a1bcae | -19.6245 | -56.8129 | 2024-10-23 11:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 390.6 |
| 980c8065-2139-35ec-bc8b-b7d42d4da87e | -19.6249 | -56.7919 | 2024-10-23 11:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 132.6 |
| 064f3bdc-f534-3da4-a114-0c8bf980d3a2 | -19.5276 | -56.6381 | 2024-10-23 11:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 92.0 |
| 9c13a7cc-f10b-3e86-ba37-174d054d8314 | -17.0184 | -57.5178 | 2024-10-23 11:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.9 |
| f58dffd7-f44d-37db-b823-2a8f1602e5a3 | -17.6868 | -57.4593 | 2024-10-23 11:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 147.1 |
| 87f745e2-fb46-31e7-98e1-179dcb0e875e | -17.7637 | -57.5732 | 2024-10-23 11:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.1 |
| 0bb58aa2-2834-3204-b7f0-3b46cca1f955 | -17.744 | -57.5756 | 2024-10-23 11:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 146.8 |
| 8d35cd3e-f162-3338-902b-283364f1f439 | -17.7848 | -57.4885 | 2024-10-23 11:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.3 |
| c4ba277e-f57e-3c67-81a8-b848baf284ac | -17.7065 | -57.4569 | 2024-10-23 11:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 8515743c-1d72-3a2d-8c13-5b7ca8e3da21 | -12.9166 | -42.2767 | 2024-10-23 12:06:18 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 189.1 |
| 7850c949-e571-39b6-8038-518a3e5c5ecf | -12.9161 | -42.301 | 2024-10-23 12:06:18 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 166.4 |
| 19c9c210-070f-3fc4-97ad-e4b3eb54f64e | -17.6871 | -57.4387 | 2024-10-23 12:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 78c01947-f8c7-347b-b0e9-6457b15607fd | -17.6868 | -57.4593 | 2024-10-23 12:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 140.9 |
| 61cbf3c5-7778-3734-812e-f6502bfab9ef | -17.7637 | -57.5732 | 2024-10-23 12:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.9 |
| a06579f0-b0e9-3088-8037-f2a982725065 | -17.744 | -57.5756 | 2024-10-23 12:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 147.0 |
| 9f3927e6-9edc-3c6d-b1a1-8846dec0b61f | -17.7065 | -57.4569 | 2024-10-23 12:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.8 |
| 24c131b8-d896-38b4-83d1-709f14e8721e | -17.7848 | -57.4885 | 2024-10-23 12:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.9 |
| f6be4991-cf0d-39b4-a3a8-d37828c07ae9 | -19.5272 | -56.6591 | 2024-10-23 12:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 163.9 |
| 330c2578-d87d-38ed-bdf0-9c2501446c9d | -19.548 | -56.6143 | 2024-10-23 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 3139ee28-ed77-36bc-928b-2cec5398cc29 | -19.5477 | -56.6353 | 2024-10-23 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.9 |
| 65280fec-a339-305b-9f27-61d9afc10519 | -19.6245 | -56.8129 | 2024-10-23 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 571.2 |
| 16f21631-9a04-35e5-9cd9-817c6cd55579 | -19.6249 | -56.7919 | 2024-10-23 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 157.5 |
| c951f668-b40b-3975-836e-44098d74e9c4 | -19.6253 | -56.7709 | 2024-10-23 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 98.8 |
| e25d5626-0056-3807-bb66-1c72af41ac14 | -19.5268 | -56.6801 | 2024-10-23 12:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.0 |


[Clique aqui para ver as próximas entradas](README66.md)
