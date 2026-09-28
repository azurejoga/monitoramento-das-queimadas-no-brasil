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

## Dados Diários - Página 167

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b37174c6-4fe7-3463-a32e-fe55aa34d2ce | -4.25286 | -51.0522 | 2026-09-28 17:11:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0242f034-86f3-33e4-aaf2-2874a6f00e36 | -3.52039 | -51.73026 | 2026-09-28 17:11:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| fb4a2d38-cab9-3765-a891-76a72e774f9a | -3.80415 | -56.80374 | 2026-09-28 17:11:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1001a188-f38c-3ecc-9f58-c7cf78835f2c | -1.43419 | -48.90156 | 2026-09-28 17:11:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 35d1c1be-435d-37eb-8424-1aa632c0c56c | -3.0104 | -54.21896 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 32b59f83-4194-3315-ba56-94b8c6c1bf2d | -1.68742 | -54.64929 | 2026-09-28 17:11:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3d544b4f-028d-3210-91e0-2633a04b2cdf | -2.0578 | -50.76425 | 2026-09-28 17:11:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c2dd4a22-a886-37a6-8a33-5a740640c55d | -2.25497 | -47.46091 | 2026-09-28 17:11:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4eb4662c-eb9c-38de-b86e-cb03d41754a3 | -2.67229 | -54.66656 | 2026-09-28 17:11:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5ecd1877-fdda-3b04-8a6f-c7b46867386f | -2.14295 | -54.64679 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7483c4bd-3b8e-3a89-8121-345b8120c021 | -3.2748 | -54.00181 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0054bed3-b7f6-321d-bf73-59e78e61d815 | -1.43251 | -48.89094 | 2026-09-28 17:11:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7d490f61-2843-3a13-96ab-9c97bd8d92cf | -1.9718 | -54.26205 | 2026-09-28 17:11:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0b83f3f1-17ee-31ca-9ee3-7dcb96926bcf | -1.47703 | -48.92195 | 2026-09-28 17:11:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 78c66e01-a335-3354-a936-dabfddf59c81 | -2.06157 | -49.53793 | 2026-09-28 17:11:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 8fd99741-d5fa-3068-964f-e278b7ecbc8e | -3.75533 | -51.33493 | 2026-09-28 17:11:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 4304ccdf-1eeb-3168-b843-4a372826c5c9 | -3.01094 | -54.19979 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1cedee04-3953-326f-b669-a5b381a5067a | -2.98157 | -54.14675 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 27f9b126-d532-3b3c-9e35-25e6bdc813ed | 0.89033 | -50.7793 | 2026-09-28 17:11:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e47ba59b-479d-38b4-bf47-80669a1921c4 | -3.71814 | -54.66252 | 2026-09-28 17:11:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4f54bf79-abcb-3291-850a-49817d23b92c | -4.31098 | -50.39717 | 2026-09-28 17:11:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| ec080d1c-ded1-3b95-8261-e9ea2e028bdb | -3.20732 | -51.04324 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 45c1cb26-4a05-376d-bd13-d1716572bb78 | -3.68389 | -66.15434 | 2026-09-28 17:11:00 | NOAA-21 | JURUÁ | AMAZONAS | Brasil | 1302207 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0c5501be-3951-3f1e-9f97-bdb1a3aeb14a | -1.97812 | -54.25715 | 2026-09-28 17:11:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 696a02ab-9e4d-3cae-b5e9-3c6833b41b0a | -3.83803 | -51.12288 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0a30cc6e-fd5c-3fc2-bcaf-727286a9fd1b | -2.97754 | -54.1435 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 84fb315a-8d43-3103-ae4d-b257eb41a032 | -2.8529 | -49.5438 | 2026-09-28 17:11:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 59ebe2cf-8c21-3bf4-9a68-ef9be75efc5c | -3.684 | -47.49358 | 2026-09-28 17:11:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0834a967-a85d-3b16-b9ea-e65130249f3b | -2.98099 | -54.143 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d9e1f920-3d1f-39df-bee5-5ef621eeedbc | -3.79285 | -55.56718 | 2026-09-28 17:11:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8d0654cb-956f-35c8-b964-f0a4f7f99740 | -1.56669 | -50.48173 | 2026-09-28 17:11:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 3d08d268-652e-33b7-9606-846d046bd233 | -3.83196 | -52.13351 | 2026-09-28 17:11:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fe3b9430-606d-32a1-a197-18c9d97b7b4c | -3.62798 | -45.16103 | 2026-09-28 17:11:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 57147dcf-b200-3a0e-82e9-24ed97c37f6e | -2.09277 | -49.557 | 2026-09-28 17:11:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 64baff56-4d34-3b94-b224-cae859d7ce07 | -2.44812 | -49.22036 | 2026-09-28 17:11:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e3f7ad91-ba56-34f2-94cc-233c39bd2327 | -3.60534 | -49.45343 | 2026-09-28 17:11:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 40e726eb-1b2c-32e1-b52f-99e0f41cec5d | -4.23391 | -53.73836 | 2026-09-28 17:11:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 152b3eb6-2ede-31eb-9edc-f47b22eebcb8 | -2.97896 | -54.76308 | 2026-09-28 17:11:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c6163c4e-d022-35d0-86b6-a16223b7ea38 | -1.23025 | -54.09984 | 2026-09-28 17:11:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b2738671-568d-3d74-bd7d-56ec348e1b49 | -2.97813 | -54.14725 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 640d1867-b79c-3112-9d7e-e69d8e571f7a | -4.73833 | -63.72939 | 2026-09-28 17:11:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 25d18647-a3eb-3fa4-a4cc-ac7b55bc1b33 | -1.2115 | -49.22815 | 2026-09-28 17:11:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 902a95cd-9a70-368c-9c16-816ae3c3066a | 0.28552 | -50.90407 | 2026-09-28 17:11:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 45d950ad-e081-3461-8e4c-dce83a7f1a5c | -2.57393 | -54.27838 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 37606f67-24fe-388f-ac84-53ccc33ad8ba | -1.77662 | -53.76745 | 2026-09-28 17:11:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 07d18062-da9d-3a53-bddd-71c0876560a0 | -3.68349 | -47.49054 | 2026-09-28 17:11:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f772d4b7-5484-30de-89f7-bea4a87005ff | -1.43335 | -48.89624 | 2026-09-28 17:11:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c795c2f1-8e86-3053-9140-957deef6901d | -1.71083 | -48.28159 | 2026-09-28 17:11:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c7f829a8-a384-3e42-8f92-f922a70a4d0d | -3.79697 | -51.79211 | 2026-09-28 17:11:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 1cc330d1-a077-329c-9733-374410bb7c61 | -2.90165 | -54.1053 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8364c06d-7cd6-332c-9794-a7db1ef67d5d | 0.63225 | -50.29019 | 2026-09-28 17:11:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| fad826f6-4304-3745-893b-697a3ac1ba29 | -3.15674 | -54.09726 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| edd551f1-b70b-3965-8c37-ef154aaf47ad | 0.34924 | -51.4492 | 2026-09-28 17:11:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 15.9 |
| edc9fe62-f27c-363d-bcc9-f6e79ad54e2a | -2.09882 | -49.5656 | 2026-09-28 17:11:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 26a96ae3-6cc8-37ca-947b-d2c025a515ca | -3.22317 | -54.32305 | 2026-09-28 17:11:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 188b448f-15a8-3fc0-b1bb-4eea554fb25c | -1.77077 | -53.7765 | 2026-09-28 17:11:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7a8daeff-a7a3-3d99-a121-76dae8c1b0b3 | -2.89777 | -54.1713 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7b8daf55-89ee-3898-9c4c-6dba42645b2f | -3.58896 | -64.48135 | 2026-09-28 17:11:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3d82f5f2-131f-38da-abb5-e8c86eb77ffa | -3.67837 | -47.49148 | 2026-09-28 17:11:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9bfe1d83-ab1e-360e-add1-f073ef8723db | -2.76794 | -49.48517 | 2026-09-28 17:11:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d3c7cc99-0e2f-3580-9fed-0e59fde0554f | -2.14029 | -48.95857 | 2026-09-28 17:11:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4a392687-fe8c-33f0-86ac-65bc3c62b170 | -3.07992 | -58.01227 | 2026-09-28 17:11:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 6e339c6b-4671-3be7-93af-a95354378f34 | -1.68401 | -54.64981 | 2026-09-28 17:11:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a6fe3ca5-6469-3a8e-8c0a-df036df81ac0 | -1.776 | -53.76347 | 2026-09-28 17:11:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0d39f60b-bdc0-3d11-bff6-e4a2025833c9 | -2.44347 | -49.22111 | 2026-09-28 17:11:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| cf1ceac8-ef9f-3fe0-9805-26ae87be1e86 | -2.58203 | -50.78631 | 2026-09-28 17:11:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b373c9f0-4bc5-3be3-8eb6-68718716eb86 | -1.79009 | -47.94909 | 2026-09-28 17:11:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ff55c533-b4a8-328d-a856-f8f6ef7953a6 | -1.94951 | -48.35948 | 2026-09-28 17:11:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 55d43547-85f4-3d60-8e06-32b8cfe9cd04 | -2.11941 | -48.03775 | 2026-09-28 17:11:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 78e06c96-6c8c-3c38-b4ec-d6697e0a6e58 | -1.43079 | -51.55327 | 2026-09-28 17:11:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f27a73b6-1973-31b8-ac6f-ce1f7cd03974 | -2.07317 | -48.13924 | 2026-09-28 17:11:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 370f541d-419d-33d3-bf2e-6b77a73c91de | -1.8861 | -48.69427 | 2026-09-28 17:11:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| c128c556-1399-3f4b-9afa-6b86370e6e3f | 0.63689 | -54.37943 | 2026-09-28 17:11:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 0f8b149f-54ad-35a6-903d-ef07be1ebba7 | -3.02571 | -55.88558 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 58f99df9-7808-3a6d-b754-4a255565c0fb | -1.43819 | -48.89551 | 2026-09-28 17:11:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b309f284-3d2f-3b74-9f40-6bf2070555e7 | -1.9787 | -54.26094 | 2026-09-28 17:11:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 94e96349-37dc-3557-af16-3e94890161b2 | -1.97525 | -54.26149 | 2026-09-28 17:11:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 719520ac-795f-32b7-92b0-b025e67af72b | -1.2964 | -49.05529 | 2026-09-28 17:11:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 73154838-30d6-31e8-bd8f-b45730b5a8d8 | -3.15442 | -54.08216 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 5af09633-8999-3882-8e2b-cff5e7236b26 | -3.14983 | -54.07519 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| e7016373-d7f6-34c4-95c7-3ebd4081e50d | -3.86211 | -52.00316 | 2026-09-28 17:11:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 94584aa4-e6df-37b1-ac68-63c830f77522 | 0.87643 | -50.78172 | 2026-09-28 17:11:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 7a6db38d-113b-352d-b484-bee611bc4b8a | 1.12702 | -50.00822 | 2026-09-28 17:11:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 28cdfae6-bc7d-3c3d-b3fa-4b81151fe23a | -3.19966 | -53.40919 | 2026-09-28 17:11:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 4abee6d9-1dc2-3064-8793-5f0d05b29489 | -3.62873 | -45.16548 | 2026-09-28 17:11:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f403d9e6-24a9-3f42-98a3-cda57f4f4da9 | -3.155 | -54.08593 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 3d6f123f-7b95-3ff1-b701-dcf192058ee2 | -3.27206 | -54.00241 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| eb19ed0a-802b-3e86-9843-a600372a3bf2 | -1.90865 | -52.0661 | 2026-09-28 17:11:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fbc0bca5-5a33-372f-a5e5-ac27f78f9db1 | -3.20676 | -51.03965 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d265e155-3f9f-3bec-a4ad-0d1cc63c9f6e | -1.46889 | -47.76404 | 2026-09-28 17:11:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 22b16a8f-1a5d-3c9c-a6db-04a1a80f61cf | -3.56527 | -54.22109 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8a54e25-20e3-3cb8-bb8a-ea83cd8a0afc | -2.06237 | -54.62154 | 2026-09-28 17:11:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8f2dffc8-d1f5-390f-b9c9-5835c954b947 | -4.32369 | -48.62949 | 2026-09-28 17:11:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 511f0bcf-c138-30d5-aded-fe462874073b | -3.56924 | -51.99098 | 2026-09-28 17:11:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 026e5216-8d2b-3b88-8346-13cdc39fec35 | -3.22942 | -54.31831 | 2026-09-28 17:11:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5be7b0b4-f526-3f0d-9889-ac73a6b26c63 | -1.21484 | -49.22537 | 2026-09-28 17:11:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 1eaae288-5e54-34c0-ae27-62f70fc8a9fc | -2.86992 | -45.72614 | 2026-09-28 17:11:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8978dbd6-def7-355f-994c-fdba44676d65 | 0.27932 | -50.91575 | 2026-09-28 17:11:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 866c5bf5-e053-3eec-82d5-9ffc7c6ea194 | 0.69806 | -51.43494 | 2026-09-28 17:11:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| df61fb0b-0664-3145-aab3-7b6de5fe390a | -0.44323 | -52.02333 | 2026-09-28 17:11:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README168.md)
