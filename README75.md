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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d218b1d0-8128-3f90-9f54-a623d5ac4deb | -1.73677 | -52.04515 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3720829-eb78-3f6d-ab4c-b983113cb851 | -2.87991 | -53.9571 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab0f0d05-3b12-3b3e-9431-d115e0f16176 | -2.90251 | -54.59945 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7911f16d-f985-38c4-ba0c-7ef5629582ce | -2.10422 | -46.26153 | 2024-11-24 05:14:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db4f90c4-9687-32a5-84c4-d5567a9bc846 | -3.10062 | -53.73566 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 987d7a5c-238c-35e2-aa28-62b3c0b6c923 | -3.23603 | -54.23085 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ecb7f385-7546-3bfb-a9ab-55994f1919e8 | -3.21974 | -53.92907 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9068036a-d7bd-32fe-9eea-8129a23a535e | -1.7925 | -53.66451 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1400e521-952a-3962-ae4f-28d3175d7f86 | -2.59555 | -54.05711 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40ddb5c7-ba13-38b7-bcee-e047e277e756 | -3.25991 | -53.2686 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dfa5c6b-c35e-3044-ace5-1286eb77e12d | -3.1123 | -54.00233 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b89b570-b39f-3ffa-976a-b6806514a2a4 | -0.93536 | -53.2126 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e926d490-242d-3a02-9862-55d469f17ee5 | -2.62265 | -54.9366 | 2024-11-24 05:14:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dab860c2-07de-33d9-ae0e-7a79a27bbcd9 | -4.51695 | -45.71997 | 2024-11-24 05:14:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e29c01f-79a6-3fc8-a368-c4a28491faa4 | -3.24599 | -50.11601 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73061d94-e223-3bef-a203-52b5f95a5071 | -3.22549 | -51.27898 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb5cdd51-2c67-3631-9b52-3f5287454835 | -2.14962 | -50.92274 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5600be24-2ffc-3869-a92d-68388f23427c | -1.07829 | -53.36996 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b926444-4d26-37a1-b601-6b0f8e8796d3 | -2.17554 | -53.63777 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0a5ac4b-dc14-3cba-b300-7f937fa73349 | -3.09242 | -51.32336 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b5530e9-1f61-3a15-863f-5b685defb109 | -0.96096 | -51.7186 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae839cd2-9f2e-3a56-b092-3d388322c347 | -1.22192 | -53.68518 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6ad1b096-859f-323f-a0f0-1860a5f1cebd | -0.81513 | -51.59826 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4174ec59-a4df-35c6-bbe3-c789fa71f308 | -0.88183 | -52.76439 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73327f69-2cd1-3eeb-94d5-124f56614f74 | -2.44002 | -49.09055 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1e7d2fd-07a5-3c8c-b10f-406e3274b336 | -1.6623 | -52.70972 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5a0c17d-f908-36b0-8b77-eb9c47500705 | -2.85696 | -51.27599 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f77e54aa-671f-321d-9698-d17ef347421f | -3.11967 | -53.10365 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8db33d9-724f-390f-937f-e46585756232 | -3.35512 | -50.13901 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d7eca88-8774-3878-9e9d-43afe3aa086d | -3.27025 | -50.55753 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93777445-e75f-3b96-b585-bbfa74d494a2 | -1.42375 | -53.38631 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 465ce4bc-7aa5-37bc-a8a3-4fb72908d331 | -1.76907 | -53.61277 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a1446f9-0550-3837-b9e5-20991f02960e | -0.98509 | -51.72095 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21d6ea89-9c67-37d9-9464-8114875a5a4e | -3.10012 | -45.78564 | 2024-11-24 05:14:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 044cfc0b-5192-38e5-9a9b-173ab915724c | -3.04375 | -49.4506 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 988cd423-53a1-342a-a44e-02b6d00ce520 | -3.08707 | -54.54234 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 897c14f9-706f-33f6-bee4-95a405ed474c | -3.18388 | -54.31961 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb1c81a5-cdbc-3839-bf76-9ad5b461dfea | -1.63606 | -53.3075 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 582335a0-47cb-35d8-ab24-2c2cdeabed11 | -1.839 | -55.60741 | 2024-11-24 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecf2d360-596f-30eb-bed1-1c5e1455c040 | -1.60725 | -46.8779 | 2024-11-24 05:14:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bee07524-0aa7-3e9f-9c7b-687700009c7c | -1.26386 | -51.76628 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c5230e2f-a490-3e42-be4c-708e6b05f692 | -1.19387 | -51.76373 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c0be883-149a-3f45-b40a-df9bc99d0c90 | -1.94284 | -49.52097 | 2024-11-24 05:14:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50ef1c74-77a9-3836-84a9-ed1464db5e6d | -1.66286 | -52.70616 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1d60346-62c8-3a53-8f21-9a41d3d523ac | -2.70878 | -46.28456 | 2024-11-24 05:14:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9a1f732-c74e-3470-9f6e-464a85342c52 | -3.67915 | -50.11595 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a444eefa-205e-3beb-b1cd-33f182e35121 | -3.17707 | -54.31386 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86a630da-84e7-3bfd-8d35-511c7fc024ff | -3.48558 | -49.91734 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50eabf0d-a29e-3e2d-9ee3-c18375d91638 | -1.10924 | -53.39927 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 77d98c5d-d3e2-3a61-847b-10d1b4f8e795 | -3.04448 | -54.02254 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f09983c1-e302-3afc-b3e3-a30148fdbaec | -2.91533 | -50.32011 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b3a3b54-feb0-306c-bdde-0af7a36a52b4 | -0.28261 | -51.50127 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba3a8413-9c6b-3cf9-90cd-b709153ec122 | -3.22778 | -54.23421 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6a58dda-4520-3f78-bcc1-ef4ed36fce28 | -3.22044 | -53.9244 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79563ff8-d718-33fa-b518-4151a9574653 | -3.31593 | -53.28749 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92a76854-6f77-3c68-8ce0-ca672962374e | -0.97773 | -51.7116 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a8ba7c3-1acc-3d3a-be5b-9ac43fa3d00e | -3.09613 | -54.55708 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1f75152-ca4f-3c04-acbb-413c155eaed3 | -0.93494 | -53.21064 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dda10668-38e8-3af7-81c7-51109ea800c7 | -3.18082 | -54.31447 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80e42b48-1c20-3b46-9f2d-07785c0f6b4b | -3.642 | -49.88745 | 2024-11-24 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b937c75-1c04-3c6c-99d6-cded9362322f | -3.2398 | -54.23143 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b129725-0b5b-39cc-b816-574de9eeb6fa | -1.42538 | -46.05771 | 2024-11-24 05:14:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11901360-db7b-3c98-aab5-75c21572bbcb | -2.56015 | -54.06098 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1672aa77-e2e9-3042-b43f-e85b6e9b2f40 | -2.69475 | -48.8272 | 2024-11-24 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c767700-7412-36fe-98e9-98fc04e90d9b | -3.48276 | -49.90187 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb6867dc-48c0-3534-bfc6-311c08ce500a | -3.04911 | -52.7548 | 2024-11-24 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bdd51e79-dd93-3db0-a830-274f96d909a6 | -1.19325 | -51.76777 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5558f520-eaea-3450-a99b-f208669b8652 | -0.83724 | -52.54742 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f9bea47-ca70-35cb-94c8-6dc2ae087560 | -2.27246 | -48.4311 | 2024-11-24 05:14:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1040d34c-2606-32d4-bfde-c6f2af819f72 | -3.11915 | -53.10714 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0ac3d4a-2335-3e35-9067-b8b9109eaadd | -2.22041 | -46.38633 | 2024-11-24 05:14:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0161d939-d50f-3278-aa74-d2bf22d2453d | -2.59625 | -54.05259 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2771fa5f-a26c-328b-be1f-c9afe16df875 | -2.20622 | -53.75669 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 465eaa60-274f-33da-a385-b345b7161dce | -1.77317 | -52.71899 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ad85207-8710-3ab8-b328-18396cdf9659 | -3.08437 | -54.55966 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ba46783-c33e-3949-92e1-9df38b9c4f34 | -3.492 | -49.90923 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd5a95ef-2953-301d-9888-9a2656e3686b | -3.20227 | -52.57615 | 2024-11-24 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1196a859-3281-30d2-afc0-30b9608b5ab9 | -2.87812 | -53.99493 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| abed5861-d5aa-320e-9f80-c39876407070 | 0.41392 | -50.85686 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b104d18a-6e7a-3036-b6e6-f01ff9366034 | -2.84123 | -54.01568 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8bc4816-7954-388f-bec6-0135c30e7198 | -0.2883 | -51.60529 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c6270b3-b77d-3764-a4ec-cc0d0635b1fc | -2.85677 | -53.9659 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b70ef4b5-ae4f-3fdf-a5e9-e9af1204f1bd | -1.25195 | -53.36159 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2a2ec64-4946-3cac-98d8-2534212649c8 | -3.3042 | -50.03232 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29965fdc-cec2-3848-a450-d470948d9966 | -3.09549 | -54.29041 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7ebda0c-0e44-39e1-9959-dec01c16d53e | -0.91459 | -51.64945 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 745d75c7-0a85-369e-b722-750f6d708666 | -3.26706 | -52.62908 | 2024-11-24 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbfb2bce-5e11-3aa5-91ad-6c9b9f899047 | -1.92406 | -54.42675 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c4ff1b2-d259-34ea-9ab7-668f111491d4 | -3.23146 | -54.16002 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ec9f28c-1a83-3c90-8f13-ffc2dd192a06 | -3.17877 | -54.32797 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c41a10e-89fe-37c7-ae1e-3a7baea64005 | -2.82152 | -54.59349 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a985e1a-84af-33ac-8198-8d1557a1763e | -1.7355 | -52.7205 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9929ba24-888b-3c37-8abf-3641cc44be50 | -3.00906 | -51.44304 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e09961f6-2cf8-3cf7-9b7d-eda0e0485946 | -1.25718 | -51.75282 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2bd19b55-1ef0-34a3-b30c-8c14803ac4eb | -3.2458 | -53.28051 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6a2adfa1-5703-3c93-8f9d-cbd6dc1e2d71 | -2.82389 | -54.10238 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d650b14-4b2e-35f7-8444-23827b377913 | -3.24632 | -53.2771 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e90d78f2-be2b-3889-b6d6-6b3f5e2b5259 | 0.08935 | -51.4893 | 2024-11-24 05:14:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 519475cd-0197-37af-a5a8-de50ff5e21ff | -2.16823 | -53.77462 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2f362251-213f-373d-a11d-5d5306925d62 | -2.57402 | -53.96977 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README76.md)
