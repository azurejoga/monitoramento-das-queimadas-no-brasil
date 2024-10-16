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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f4cb1c3-061a-303b-9fa1-2f107985c809 | -2.14068 | -50.8367 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee79dfbf-25d1-37a8-b673-797ec4ccbad2 | -3.28444 | -50.93597 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d59ac20e-8b0b-3fcc-aabb-10f15471b91a | -3.28372 | -50.94042 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2483140d-cadc-3e72-917b-7a44901ee9c5 | -3.28071 | -50.93535 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c286fda6-811c-32b2-86ff-c9c3eb175f17 | -3.28 | -51.52147 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9509bfbf-6226-37ed-8b59-11759f7d0648 | -3.27923 | -51.52634 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6c31f631-021c-3d6b-9791-12c53c5fe8b7 | -3.27718 | -51.52367 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 50d0ae80-0639-3471-9a41-99617f7b6ee9 | -3.27625 | -50.93921 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 50fd4549-6913-3c98-8dfe-7aac61fc379d | -3.27544 | -50.93665 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e742f77d-fd01-3b83-9c4f-9b21d03be83e | -3.25506 | -51.2353 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3871cf8-08fb-3f90-ba1b-e6e53262449e | -3.19901 | -51.03072 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27316b60-1b5d-3286-a632-e43a83b237d9 | -3.13453 | -51.28538 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 640f2e87-66f2-36ae-ba5b-a072bde04f20 | -3.07615 | -51.1918 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de63872e-5fac-376b-8f35-ea6a14f24d3b | -3.07309 | -51.18659 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1429bc27-a637-3017-bd01-af194172be4f | -3.07235 | -51.19122 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c50efbab-5dd9-3853-b196-dae0966d0f15 | -3.07078 | -51.1767 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfca7db6-c187-39a2-8186-58ae4297d1aa | -2.90419 | -51.81678 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38dabb37-e20f-3126-9ae1-1b0b5dc54ca8 | -2.90339 | -51.82182 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be1c5b27-c859-3caf-b8fe-0a97d6a5e845 | -2.90276 | -51.81738 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c83f36b1-9646-3a1a-be5a-b4b4c2543af6 | -2.90024 | -51.81607 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d3dc9ec-0c25-3035-aa02-39638329d84b | -2.88569 | -51.67892 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1198c837-509f-3896-b14f-f2eb1ae400ba | -2.88489 | -51.6839 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6191f2ab-dc86-3057-a964-b6cafec9f07a | -2.88409 | -51.68889 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ff85d2cc-2f73-3279-a490-033732f7baeb | -2.88176 | -51.67828 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 740f21a6-4cc7-3b16-9fc5-ec857a51af7a | -2.88096 | -51.68327 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7096f69c-4123-3750-9fd8-77bf8f6d7868 | -2.87784 | -51.67764 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c5bd2ce-cc45-3a77-9111-cf86454a3155 | -2.87391 | -51.677 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84b54c61-7734-336b-9689-56b81b79c3ac | -2.81959 | -51.34016 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5defa88a-8a6e-3137-91dd-f48bbbbfdbbe | -2.58423 | -51.92421 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0899731a-8a78-3e8e-b414-b86c9740ed54 | -2.58022 | -51.92361 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c208a39-4c6e-386a-8043-8ffb3b88129f | -2.52374 | -50.71617 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ce09c75-d3a8-334c-aa43-c15dbe50e939 | -2.32009 | -50.92682 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ec7e9d1-ad82-3bdd-8543-4c0fbe07b01e | -3.61584 | -51.38173 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5512af6a-1c11-38b4-9481-fd779f07b44d | -3.61297 | -51.44917 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acc17583-838e-32e8-be69-8479d8490080 | -3.61203 | -51.38108 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 035cb615-6f0c-39ca-b73f-b9d637c4e2c0 | -3.60914 | -51.44855 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11bce813-fd3a-31c5-9402-aa86484ea7df | -3.58649 | -51.00366 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c9b70e0-c111-33b5-9464-eb8e20527f51 | -3.58538 | -51.4496 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da29de13-1308-31e9-a930-d63baed78974 | -3.5838 | -51.00542 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 65cdaf66-428b-3f02-87b5-31fdc3b5be89 | -3.54763 | -51.58602 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34cee6e3-7b7b-374a-a752-3ab9f16d201a | -3.54376 | -51.58538 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 132bfcd2-2f51-3de6-9c4f-bb25e9d858ff | -3.54023 | -51.389 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bb41362-fed9-3287-b2b1-a3b0408e0cda | -3.50628 | -51.31424 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| dbb85b50-3208-3250-aac1-dd7fade0203f | -3.49964 | -51.58814 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 086d840f-0c17-363b-b261-5209ed596e99 | -3.49885 | -51.59298 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93ade253-a076-39f5-a51a-d76091bb6e85 | -3.49781 | -51.59101 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1124599-0347-3b6f-b17a-48dfefcd4149 | -3.49767 | -51.67288 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2658506-d93f-3813-899e-e5d21ecd9ff8 | -3.49378 | -51.67227 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18cfe90c-ba84-3405-b3cf-66c0ca4c5da3 | -3.45218 | -51.50445 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e762746-7219-35f4-ba2a-163fe711a3b8 | -3.28104 | -51.5243 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7044e345-2ce6-32e6-b797-0c0edbab4a0e | -3.27998 | -50.93981 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3854c3ba-6f81-3d59-92a4-77db2abdd140 | -3.27698 | -50.93475 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0f00f890-15d1-31cf-801c-a40879817523 | -3.23158 | -50.85185 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dc3f3b5-5212-3bfe-9cb9-9616dc25e9b3 | -3.19827 | -51.03534 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f143b45-b10d-3242-a223-410a24d4c165 | -3.15896 | -51.30397 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 083c8ec1-8d06-3416-a7d6-7d5e9cc2e7c4 | -3.1582 | -51.30867 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b3d6e8c-835c-3720-9b5a-ba981f2ea3a6 | -3.1383 | -51.43245 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af699b16-b527-3e71-a3b0-dd0685bddee5 | -3.13298 | -51.31906 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d46161e7-e0ef-3732-95a2-dab48a95a169 | -3.07003 | -51.18134 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1d418b3-e47f-3783-9840-6282925fb49c | -3.06929 | -51.18599 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 119f0959-9ee4-3960-8097-16454259be6b | -3.06485 | -51.23798 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28078421-3e89-3619-9683-271b8d5dba4d | -3.0641 | -51.24268 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 064adc08-ff0c-3d60-904c-1de727cc4760 | -3.06028 | -51.24207 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fbaaea58-ad21-3e5e-a632-ee598496e1fa | -3.05572 | -51.24612 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 726fbaa6-882e-3359-bbaa-ad56e8c88132 | -3.05244 | -51.12165 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70c8fba7-00dd-37ed-9644-e95f74b164fb | -3.50801 | -52.16209 | 2024-10-16 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19d348a9-f502-3377-9ea2-d20b5ed218bf | -3.50745 | -52.16561 | 2024-10-16 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41f59754-5c86-3f9a-acaf-87e00eccbfbf | -3.50526 | -52.16153 | 2024-10-16 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8d2e82b6-4c9f-3081-bb69-beaeab3cf009 | -3.50468 | -52.16504 | 2024-10-16 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8046d18f-4bb6-30f0-8698-2def7b82d8f5 | -3.504 | -52.16142 | 2024-10-16 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9891c1c-5edd-3501-a330-0f4ec55bcf84 | -3.50344 | -52.16493 | 2024-10-16 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d62e13b-bed0-3de8-8d46-6961edc4b064 | -4.65247 | -50.93572 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55ad89c5-9521-34ac-b37f-5a255d1a264e | -4.64183 | -50.97851 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e36fbe24-8e30-3596-a42d-480bb7e2e776 | -4.64113 | -50.98285 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d756f783-4b46-3b14-8cb4-c3a6c91f205d | -4.36131 | -50.97211 | 2024-10-16 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 73f325ae-ea2e-3b33-9acc-526e096001dd | -4.3606 | -50.97644 | 2024-10-16 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8a892efc-4df1-3a07-a845-801d43ca616b | -4.35834 | -50.96717 | 2024-10-16 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c10ea12f-0d39-3382-9a7e-8b009ace8f84 | -4.35763 | -50.97151 | 2024-10-16 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e70ca4d7-aaec-3a46-8341-fb213da67b71 | -4.35691 | -50.97584 | 2024-10-16 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b976864e-f4c1-309a-81e3-48782215de0f | -4.3562 | -50.98018 | 2024-10-16 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 9db4b30b-342a-335d-99b9-1a74a7b13f80 | -4.35418 | -50.97729 | 2024-10-16 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1ece9b15-284d-3044-a48d-ba06c1db2005 | -4.35349 | -50.98165 | 2024-10-16 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 29c50c98-a71d-3ca2-945b-7a58fa80a698 | -4.35322 | -50.97525 | 2024-10-16 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 36103dc9-a871-30ee-a10c-d32f79434b57 | -4.35251 | -50.97959 | 2024-10-16 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 8f4d555a-3574-3c51-b186-f2e92eac4e8d | -4.35048 | -50.97671 | 2024-10-16 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a93f6ba9-02fc-3de2-814e-4de1584d0760 | -4.18337 | -51.24868 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 993d1deb-02e8-3faf-981f-afcaeca79e08 | -4.17961 | -51.24809 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5aea2341-31f2-38d6-8520-6efdb6bbabfb | -3.88418 | -51.96333 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4973c8d3-f52b-349c-8010-e0e88ea675a4 | -3.87773 | -51.9779 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 055e6e06-7dbe-3088-a7f1-7295af679b3e | -3.84642 | -51.75095 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 913e91c5-7004-3437-bab0-9db9f0012bc7 | -3.83032 | -51.87514 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bce06b8-b8e6-3d77-9188-9c319369eae8 | -3.82698 | -51.92069 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19686303-d125-3370-8726-a37f0b44bf9b | -3.82305 | -51.92004 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebcaa75d-39d7-325f-9a26-609f16bd4f21 | -3.82018 | -51.86324 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15c6dfb2-7b04-303f-80ec-d0cc10048e0b | -3.81627 | -51.86258 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb26beb5-35c0-36e0-a8bf-5f42fe31eda8 | -3.81354 | -51.92887 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af8b1061-c5b9-390f-9466-75f18aafdf67 | -3.80658 | -51.7747 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66d39479-8965-320d-9dde-1182235d201a | -3.78459 | -51.31837 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53f40a7a-e11a-35da-ab83-6ecebd063059 | -3.77929 | -51.35094 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a573c80-6091-3b63-ab2d-762e7d29652b | -3.77853 | -51.35556 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README48.md)
