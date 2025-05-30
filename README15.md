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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa30587c-3753-354a-843b-6a8bebfe97c9 | -6.2226 | -43.3459 | 2025-05-30 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 98fa28f9-730d-31d1-999c-989525b7c16e | -13.087 | -45.3023 | 2025-05-30 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 6a37023d-cb16-3042-8ed8-eb0501e27f61 | -13.1068 | -45.276 | 2025-05-30 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 366.0 |
| 5be4382d-9b57-3fdf-8430-303ba50dbe78 | -13.087 | -45.3023 | 2025-05-30 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| dbc02893-1c71-3311-8018-503ebc838f54 | -13.0874 | -45.2791 | 2025-05-30 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 74973b82-5a84-3c29-b5a2-1b1f6eb31361 | -10.7269 | -49.2883 | 2025-05-30 13:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 261b4d2a-9ce2-33ab-ae71-5e3312b6644b | -13.0874 | -45.2791 | 2025-05-30 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 6b16a251-79e2-3dd8-b786-0f01bbf08446 | -6.3536 | -43.3816 | 2025-05-30 13:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| b7974e17-8b37-3245-9b16-0e9c2e0f2bff | -6.9804 | -42.7854 | 2025-05-30 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 317.0 |
| 5cb48b60-22b5-38ff-aef2-41a27deb6e33 | -6.2038 | -43.3475 | 2025-05-30 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 90d35e40-1543-305c-a57e-3fa4c59eaf84 | -13.087 | -45.3023 | 2025-05-30 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| b2750199-ad01-3fd9-9747-678fd0c686e6 | -6.2228 | -43.3226 | 2025-05-30 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 6021eb13-78e6-3893-91d0-7fdd05a31808 | -6.2226 | -43.3459 | 2025-05-30 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 184.0 |
| 2e5666bd-ffee-300a-b4c9-5208363e9dda | -6.2414 | -43.3444 | 2025-05-30 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 37fbfd0e-c7e8-30b8-a55a-0b687849eddb | -7.5201 | -43.3436 | 2025-05-30 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| f02e91cc-cc0d-3b64-a316-690fb54e13a0 | -7.5013 | -43.3455 | 2025-05-30 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 9125dcaf-7ef4-36c8-ad38-1885c9288285 | -6.2226 | -43.3459 | 2025-05-30 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 231.3 |
| 0ee36698-a3cb-3be0-be43-349bec0f1c4a | -6.2228 | -43.3226 | 2025-05-30 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 6e6f42b5-5c80-3134-ac5e-d9ea2dad0134 | -13.087 | -45.3023 | 2025-05-30 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 8ad9a66e-6216-32ea-ae52-66f86a40a8e7 | -8.099 | -45.3144 | 2025-05-30 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| fa2485be-93db-3d77-9b22-f7881bcd67db | -6.9804 | -42.7854 | 2025-05-30 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 277.0 |
| 49842d12-e4b9-3193-ab2c-97e1ebd252e5 | -11.6878 | -46.2231 | 2025-05-30 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 0b5c6ed8-ae95-3c88-811b-cb09362f4359 | -10.7458 | -49.2862 | 2025-05-30 14:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 031c8fbf-c506-380b-844f-adcd9bbc1997 | -6.2228 | -43.3226 | 2025-05-30 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| ab9906eb-aca6-39a2-b406-5ef8ba2e1442 | -7.5013 | -43.3455 | 2025-05-30 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 55875e50-0ee3-3e17-8d08-c3189fd18af4 | -8.099 | -45.3144 | 2025-05-30 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| eeb47ec9-5b39-319e-8e35-2da275dde3e4 | -10.7269 | -49.2883 | 2025-05-30 14:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 52af8b9a-242c-3219-8fa2-bab3ac5db87f | -6.9804 | -42.7854 | 2025-05-30 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 310.2 |
| 19173208-972c-3548-a398-d55af4198f02 | -8.8101 | -47.1937 | 2025-05-30 14:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| a44a2902-fb7d-3438-bf9b-93c0d66b8008 | -7.5204 | -43.3201 | 2025-05-30 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 0293316a-786d-3f3e-9e24-d66b98332155 | -10.6247 | -44.767 | 2025-05-30 14:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 8c1c9de7-c589-3eb6-a24d-f929711f1cd9 | -11.6878 | -46.2231 | 2025-05-30 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 49c44226-2da2-312a-ba46-feb3aee8385c | -7.2384 | -43.2778 | 2025-05-30 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| a0ecbdf9-5cb5-3b37-8e23-79d5b790d57e | -13.706 | -45.2687 | 2025-05-30 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 65832b8c-f0ba-3ed5-8f95-c866c12d1176 | -10.7269 | -49.2883 | 2025-05-30 14:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 317ab980-be26-3774-bd91-0faa6e2d276b | -13.7065 | -45.2454 | 2025-05-30 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 1d697c0b-b7d0-39ea-a159-3c05cd826754 | -10.6247 | -44.767 | 2025-05-30 14:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| e60b9062-8a91-3d47-8b31-c773628178f9 | -8.8101 | -47.1937 | 2025-05-30 14:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 30dd1bf5-d60a-3552-b6df-fe6192f4471f | -6.2038 | -43.3475 | 2025-05-30 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 8b461c0d-c828-3347-8fcd-5ec0308fa933 | -6.2226 | -43.3459 | 2025-05-30 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 203.8 |
| 4e4741f4-6f16-3acc-936f-482feeb8cccf | -8.099 | -45.3144 | 2025-05-30 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| ca42c1b0-2f66-3f01-aef3-554731d5a720 | -6.2414 | -43.3444 | 2025-05-30 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 24f75ff6-939f-3edc-87f2-0ef3ef3f1123 | -6.2228 | -43.3226 | 2025-05-30 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| ade40452-6d38-3c8c-8b62-c3735fafddb0 | -7.585 | -45.8608 | 2025-05-30 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| ff9aaa17-a94c-3024-802c-0258b57c0c0d | -6.2038 | -43.3475 | 2025-05-30 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| d74a4b90-9530-3f9b-a66d-5fff307a71d1 | -8.099 | -45.3144 | 2025-05-30 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 89b6ce59-c786-3175-810b-2505baefa819 | -8.8101 | -47.1937 | 2025-05-30 14:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| e3a0bd18-8399-3b6f-9f86-839b10ab1edc | -6.2224 | -43.3693 | 2025-05-30 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 0a0a6868-7e94-3257-8126-4cc7eafee93d | -6.2226 | -43.3459 | 2025-05-30 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 342.2 |
| c15c0189-ef7d-3f95-99f3-3cb098e91579 | -10.7458 | -49.2862 | 2025-05-30 14:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| fe47c1a9-3e10-30f3-b6a0-0ee4e97b255f | -6.2228 | -43.3226 | 2025-05-30 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 888b015d-13f3-339a-a94e-c897f912574b | -10.7458 | -49.2862 | 2025-05-30 14:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| c5f19197-32a3-35bc-8a6a-d98eb4d9d179 | -6.9804 | -42.7854 | 2025-05-30 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 244.1 |
| f02bd28a-7111-39d6-9168-b0c65d70fc96 | -7.585 | -45.8608 | 2025-05-30 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 2781a40b-f044-360a-bac7-e98eb57d4f93 | -6.2038 | -43.3475 | 2025-05-30 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 9dd73034-2cdc-35f8-ba25-7051459fa2a3 | -6.2226 | -43.3459 | 2025-05-30 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 314.4 |
| c53deb3f-c204-3bc4-960b-2318f39ece1c | -8.099 | -45.3144 | 2025-05-30 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 254.4 |
| 5edac55f-35d2-3305-8d4a-7a181b41e30c | -6.2224 | -43.3693 | 2025-05-30 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 05c18ccb-8729-34d9-aa6a-75be2b9999e5 | -13.7065 | -45.2454 | 2025-05-30 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 0ea29045-5056-3f66-a59d-d018fce29977 | -6.2228 | -43.3226 | 2025-05-30 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| f28e4562-1b44-3cd4-85d6-e5c404475b5d | -13.706 | -45.2687 | 2025-05-30 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |


