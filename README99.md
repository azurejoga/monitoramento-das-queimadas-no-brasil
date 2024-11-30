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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3133e8ed-52ce-338e-b184-93c31c311704 | -2.80767 | -54.07066 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1319b880-e577-3bf8-a1c4-fc6cf7aa26a5 | -1.36098 | -52.54087 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d787aeef-87ac-3c5f-8aa1-90d76243de61 | -1.40535 | -53.39293 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1fddd77-ab15-3fd9-8230-7374d84b2e47 | -1.99073 | -53.28866 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae3380b8-b152-3a99-87b9-13c1a088907e | -1.27429 | -51.62458 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 074b1f99-77e3-30e5-a861-8c77febaa54c | -2.79559 | -54.12603 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a133d287-76b3-31c5-8172-5ef4d256d1de | -1.12774 | -53.73867 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1973ee02-5cf9-3836-9857-059f44a085a8 | -4.05481 | -54.44652 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e108222-687f-3fa1-9c62-e4a0a11a8109 | -3.05625 | -53.28373 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1bf54b9-a9d1-3944-a35c-b886996b093c | -2.61121 | -51.80538 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8dfe9a1e-5fcb-3b98-bd68-004dadc45dad | -2.27291 | -53.47056 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e648b93-b94e-3fe5-9dd5-ae94ca263a40 | -2.76724 | -52.873 | 2024-11-30 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb79a255-ce7a-378d-87f4-4708d81d6c6e | -2.84607 | -54.06587 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d51b041-b8a9-330c-8c60-fb8e85a38e0b | -2.58333 | -51.93917 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edb89d77-57d6-307a-a879-0b8e3d3c9b2f | -3.14486 | -53.83807 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b180243f-f91a-399c-b6f9-acf7df877b9e | -1.59465 | -51.26844 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50596c22-0f2a-390e-8676-762ca281623a | -3.21966 | -53.62358 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b6dd93d-570e-3e73-a675-6672df9188a9 | -3.49251 | -53.82204 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6c4301b-4be1-32af-b29a-a0121b550baf | -3.41766 | -53.22589 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8827a0f5-5202-3e8e-a7b1-fb060617484d | -1.36336 | -54.6535 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 931ce11d-1dc3-301a-8641-de6dea228869 | -2.25715 | -53.46079 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4158b4d5-eba8-3a60-a4cf-8ca3cb3735ec | -4.06166 | -49.05575 | 2024-11-30 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f58d9aaa-f679-33f1-a192-df06902b1b51 | -0.81613 | -51.60006 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c75b66f1-2f7f-3b15-8181-49e80ce0ff49 | -3.83991 | -46.52058 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9af7da5c-9c50-3f1d-ab43-44a322d07a35 | -3.07759 | -54.12296 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4ad3723-710e-3d1f-9bd4-4ed8b457568c | -2.91206 | -54.11899 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b9db309-868c-358c-8dbb-e424dcfee22e | -1.49125 | -52.66333 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e50c444f-aa77-36c0-9c55-9e38b53aeea0 | -1.29557 | -51.37028 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d043abbf-a639-3963-9b82-8f20bb8af06b | -2.33439 | -50.6729 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3d9eb9f3-2af9-34ae-8acd-075d70d53b28 | -2.59661 | -51.82841 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3405a505-fbee-3015-bcdd-33d184a7d10d | -2.75357 | -54.11965 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46e77d93-8e09-35c3-9451-b047aff58d51 | -2.26842 | -53.47715 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae8e3d2d-78a3-3824-a88e-93ba51c751da | -2.04037 | -51.20237 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24270903-cc0b-3a7a-a50c-6fc6602eb12c | -1.59917 | -52.28938 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fcc7f02-ded6-313a-ad05-beecda3b3865 | 1.67657 | -50.66238 | 2024-11-30 05:01:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5efaeaa-a772-339f-a544-c4d29c648b74 | -1.1443 | -53.69851 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78fdb729-58a4-3458-a513-d8a335a3ac55 | -1.75166 | -50.54731 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ea8c1dd-3a48-3ee4-b314-c7a4a041a5f7 | -2.57955 | -51.86778 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa3e15f9-ed63-3667-a8b2-e31738969994 | -1.58235 | -51.27526 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b01960ff-8c9b-3fbe-99f1-35415d7a9327 | -3.49587 | -53.82258 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47da46a6-185c-32d4-b151-aae17da9154f | -2.8322 | -54.08879 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a7759e5-eaf5-32f0-9485-a92730cb44dd | -0.82644 | -51.85849 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 99c1382d-feff-347c-b8b8-8cd3505d437e | -1.08581 | -51.88384 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc583365-39a4-3224-8349-8c02ab3349e8 | -2.84325 | -52.54264 | 2024-11-30 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b81e4a5-254e-3d91-b25c-2884512cdd33 | -2.83948 | -54.10781 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 498f911b-7a46-39af-95f0-25466240a3ae | -2.72578 | -54.12249 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 966f8988-f2af-3a9f-ae1d-b6649f80dc6b | -2.66296 | -48.79591 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a84ce91-947e-32e1-9f86-e548f0b89b0e | -2.61695 | -54.21199 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35a88ae7-b97a-3dbc-9cd0-09736f4e5c27 | -3.31236 | -54.10921 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f54dd554-a623-3262-997f-97a727195ebe | -2.20242 | -48.34703 | 2024-11-30 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28114b69-85f0-3678-b25e-dc7e4342e430 | 1.27864 | -55.91102 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a23ebae3-8d39-3af9-b54f-af0baf2c4d7d | -2.75494 | -55.31312 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0321a514-efed-379c-b985-7af15ded407b | -3.05786 | -54.69996 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5bc8e983-c9c6-3b78-a660-e1327b0544ef | -1.06583 | -53.22412 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 743bf653-e4ef-3e44-a0f8-588efd19e08e | -3.17713 | -54.32445 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70ed032b-77ea-3944-bdd3-1e33c0c503e9 | -3.28402 | -54.16588 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81c7828b-cfef-3266-8f6d-0bc6b278444c | -3.02023 | -51.37155 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ee48730-823f-312a-a600-cce0b65f1445 | -3.44089 | -50.02549 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| efdd614f-7bb8-315e-a82b-cb5f67e1fb47 | -2.96292 | -53.94732 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c37c7fa3-6240-33ee-989f-516c94fa37ff | -1.12878 | -53.21906 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0aa95ab9-c879-353b-b133-6426dae925f3 | -3.84836 | -51.00035 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60f2ca87-9c84-30b6-b61e-bb0659cf800f | -1.07323 | -53.63745 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d86d8914-a849-31e8-8471-7e3c426561c0 | -3.30399 | -50.27391 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c28248d0-46e4-3bbe-a56f-0eb8ba048772 | -1.75853 | -53.63896 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edaca11d-4115-3d56-860c-dade456a6fbd | -3.30774 | -51.10522 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5237cf2-86d5-30d0-9695-9279f74c11a6 | -3.79089 | -46.69595 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d78a573-07d2-3677-be16-0662c6832b37 | -1.08325 | -53.63903 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c062ebf8-27ec-369e-a3ca-e486c63b42c7 | -3.12363 | -53.27486 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62d310f4-8b78-383f-af08-e3f22ce6bed1 | -3.88092 | -51.97859 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| afce53dd-175f-3e92-814b-9ab3bd03b067 | -3.08934 | -54.12884 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ce9acb1-ab11-36bb-89c2-7a01390ec979 | -2.44792 | -53.62531 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6224e4a-9c7c-39fb-8bbb-5a86ec577a05 | -1.5336 | -51.61866 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf44af27-83f5-3148-a6d7-4d89a9620793 | -1.18797 | -51.76545 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d414391-e6e8-38f9-bdb9-a535ccf8355d | -1.43894 | -55.24539 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 59d3e2c2-03ee-387c-9d8a-90f70948b990 | -3.254 | -53.62528 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 62fbb67c-6ae9-3d94-a579-d5ed006a2579 | -3.33343 | -53.36284 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05fc3bcb-57b4-3652-b00e-d9c2ad46d7d8 | -3.22126 | -50.44705 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22a39e3e-69c9-37ab-ba6f-44a264fd1e1b | -1.12103 | -54.14957 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ebe4610c-c661-30b8-a6e9-c17e16cb4e07 | -2.90258 | -53.0616 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d09ce927-e774-3c14-ad4e-e82019a7f7f1 | -3.1185 | -53.26285 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45bfbe9f-8333-30e1-8ce7-0d749b7031e9 | -2.52775 | -54.25868 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5d48178-e540-3140-99de-3eb0a1975529 | -3.57728 | -52.29644 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c9a7c7e-39bb-3995-83db-b3aa4d6f9709 | -3.26513 | -51.62291 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 02d87d27-ca8a-3833-82f0-325d015ecd18 | -2.94722 | -49.44279 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7cde443-34fb-3161-b30f-c6f3f6f14b24 | -0.05304 | -50.82714 | 2024-11-30 05:01:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2905290-6fc0-38c2-bae2-ee7179629c89 | -3.01527 | -45.09943 | 2024-11-30 05:01:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| af516168-6dfa-3772-aada-44c5be9d4ab7 | -2.81104 | -55.297 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 516313cc-5871-36ef-b108-43432992d758 | -1.08236 | -53.38298 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69f5c7f1-8588-3aa8-acdb-6b41d40820cb | -2.76146 | -49.22419 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c2e92d1-3768-35cc-a0d9-27ca5a455d49 | -1.58927 | -51.25448 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8b7a5e4-d872-38b2-9575-4ee0083db8ec | -1.26052 | -51.7589 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0725f8d-c4c0-3640-b937-8b163540f50c | -1.59098 | -51.26787 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f585ffbb-d8af-3aed-9411-fd2eb6993f24 | -3.33304 | -53.54479 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc0b21b5-3445-33d5-b4ec-11e36a127bcd | -1.60495 | -52.29813 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ee78fcd-7d01-368e-9004-2525123a825e | -2.53547 | -53.99955 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e952bc8-f4e3-3144-852b-63b1965cc7b2 | -2.61083 | -54.20747 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8da8257e-88f0-3721-8e51-ced20927e671 | -2.85051 | -54.05939 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9e14dfd-54a2-3262-9883-4cd738027f23 | -4.49388 | -49.64067 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0eea62ba-91e3-3009-b01c-4e28c4342bb7 | -1.03995 | -51.73899 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ed3547d8-e5a4-3c6f-9620-91d24dcbe8a2 | -3.05923 | -48.5186 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README100.md)
