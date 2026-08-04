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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbf6f689-a441-30e0-ba3b-5db88b33a963 | -11.2022 | -54.8771 | 2026-08-04 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 769c1a25-1042-33ff-a8c1-bf8020609388 | -6.5514 | -55.1569 | 2026-08-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| e019dbaf-5242-3cbc-8b6f-56d433c829e2 | -13.4448 | -43.8604 | 2026-08-04 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 50ee7234-f63d-3cbc-8ace-0fc46b9c73e7 | -3.6638 | -49.4898 | 2026-08-04 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 23d6bc7e-d9a7-3d93-bbbb-0910d918090f | -13.4448 | -43.8604 | 2026-08-04 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 66f02f20-0d79-3693-8bac-8912f5b1a455 | -11.2022 | -54.8771 | 2026-08-04 00:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 6e9c0c64-169f-3f94-93a1-283798058c2f | -17.595 | -46.6882 | 2026-08-04 00:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 81.0 |
| ed2a6a3e-83fd-3d31-ac74-cd035da0686b | -3.6639 | -49.4686 | 2026-08-04 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| df307e81-be56-3f7b-837b-7a1f184b1ac3 | -11.2213 | -54.855 | 2026-08-04 00:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| a55e87e7-2ca0-3a12-847a-eb08780fb5fb | -3.6824 | -49.4679 | 2026-08-04 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 94fb39e3-31cc-3a9e-8cc6-19a181b9d5ea | -8.774 | -63.6446 | 2026-08-04 00:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 9239a54e-201c-3808-be8a-42d7afc4431b | -6.5697 | -55.176 | 2026-08-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 5e2e11d8-493a-3ef9-9c8f-76a16779243e | -5.1319 | -46.2037 | 2026-08-04 00:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 8d866e63-1d28-3204-99ca-e46ffcf5ea17 | -11.2024 | -54.8567 | 2026-08-04 00:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 0eb46ab6-071f-30ed-8223-51c4f24cbbc1 | -11.2211 | -54.8754 | 2026-08-04 00:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 4d48cbf5-0150-31d2-9ace-d729ad41ac16 | -6.5514 | -55.1569 | 2026-08-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 4ecd1824-09e7-3705-8f7d-7b7d1ad9a297 | -17.5956 | -46.6648 | 2026-08-04 00:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 54.3 |
| f49a71ac-7e11-3f56-8128-0269f69c5798 | -6.5699 | -55.156 | 2026-08-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| ab45f7ba-024d-3c41-b7d3-328d0c7fe536 | -6.5329 | -55.1578 | 2026-08-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| b4a8168c-17e7-3e10-b16b-8ac1aaf4d3de | -5.1506 | -46.2026 | 2026-08-04 00:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 0e56dc55-0e97-3357-bc05-6676834cc488 | -8.3544 | -45.9897 | 2026-08-04 00:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 7bb5021f-b42b-3b53-b209-5eb8ebbd85f0 | -17.5756 | -46.669 | 2026-08-04 00:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 9a837df0-cbf4-326f-9b67-56175f096635 | -17.575 | -46.6923 | 2026-08-04 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 42f6527b-fe46-33e1-984f-856d9d9a2930 | -6.5512 | -55.1769 | 2026-08-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 3f8c95ca-8003-3f30-ba42-60e7566527a3 | -6.1299 | -47.2884 | 2026-08-04 00:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 108702f1-2108-3c54-8227-ede6a398695c | -5.1506 | -46.2026 | 2026-08-04 00:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 130.5 |
| a6a330be-f04f-3c3f-9e88-9ccd0b2deddd | -3.6824 | -49.4679 | 2026-08-04 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| e69b0933-504f-3da8-bed7-2c7f243d87d3 | -11.2024 | -54.8567 | 2026-08-04 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 713c1dc1-7383-3d77-88e3-0e1862036835 | -17.595 | -46.6882 | 2026-08-04 00:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 114.8 |
| a490c778-21b9-393a-be0f-e879fc3ba234 | -11.2022 | -54.8771 | 2026-08-04 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 9636c536-aa70-3fba-9f29-05c9de4c7448 | -5.1319 | -46.2037 | 2026-08-04 00:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 107.8 |
| beeb559c-8bb3-3874-8d0f-549e156a1843 | -3.6639 | -49.4686 | 2026-08-04 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 2c56cb13-627a-37fe-8252-c9390fc7c685 | -8.3544 | -45.9897 | 2026-08-04 00:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 04c89745-eb44-3be4-962e-7597f095972a | -11.2211 | -54.8754 | 2026-08-04 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| b1ca2c30-7e63-364a-9d21-930a022bb730 | -6.5329 | -55.1578 | 2026-08-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 6bf21502-a583-370a-8e93-42837866cc48 | -6.5514 | -55.1569 | 2026-08-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 45152941-444f-3572-88a5-25f009607cd3 | -17.575 | -46.6923 | 2026-08-04 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8c61c9b2-e098-353d-9d17-52c47e6fd3c7 | -17.5956 | -46.6648 | 2026-08-04 00:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 66.7 |
| b9f30b49-4e9e-3ad6-9e1a-b972eb487687 | -6.5699 | -55.156 | 2026-08-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| d67c69ad-9554-386c-a0d8-acf67cddb0ab | -6.5512 | -55.1769 | 2026-08-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| deebc864-ee47-3726-9215-f36ecc87f7bb | -11.2213 | -54.855 | 2026-08-04 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 2747c848-e553-3b04-9f5f-3af1a2057f38 | -6.5697 | -55.176 | 2026-08-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| bfdf66a7-579a-359e-8529-7eb02fecc8bb | -8.3546 | -45.9671 | 2026-08-04 00:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 6e6ec8a3-1e42-3433-ac0d-ed46000fea8f | -5.1506 | -46.2026 | 2026-08-04 00:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 167.1 |
| e83c2d03-2e35-3bfe-8542-d7d91fb10321 | -5.1504 | -46.2248 | 2026-08-04 00:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 45.4 |
| bbaaf42b-6ea2-3933-9cfe-c30d9291c0e7 | -6.5512 | -55.1769 | 2026-08-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| d7973873-63aa-3ffe-9ed5-fa9963146595 | -17.595 | -46.6882 | 2026-08-04 00:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 51.6 |
| a6bd412a-9c41-3a24-aba2-ff5aa85ad5f1 | -8.3544 | -45.9897 | 2026-08-04 00:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| b516cff4-11dc-3c47-8c9f-9aef55c62324 | -6.1299 | -47.2884 | 2026-08-04 00:50:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 10a05e21-2656-3f93-9d58-886a2ce0902c | -17.575 | -46.6923 | 2026-08-04 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 58.9 |
| cb918235-882d-33a8-b252-1fdf213b2c37 | -13.4448 | -43.8604 | 2026-08-04 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 08bd6eb2-d5c8-389a-bba3-57f5c1f7e8e0 | -3.6824 | -49.4679 | 2026-08-04 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 929f7871-6b37-3fa6-ab3d-559f8556858d | -3.6639 | -49.4686 | 2026-08-04 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 14a45c34-6786-36fb-8574-47369d3aa64d | -5.1319 | -46.2037 | 2026-08-04 00:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| cb9bcb87-37de-3876-842b-31fe59df8b5d | -13.4254 | -43.8639 | 2026-08-04 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 66f1ef6c-6251-3e1a-bfb1-1b6f31991e72 | -6.5514 | -55.1569 | 2026-08-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 29cef742-c9ef-3894-9316-607f0e7099ac | -13.4259 | -43.8401 | 2026-08-04 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 5a3c0f13-9f00-3c3f-914a-1866b5088025 | -6.5697 | -55.176 | 2026-08-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 22ba0f13-aaa4-395a-a68a-2b2db47fbade | -6.5699 | -55.156 | 2026-08-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 9e07ecf4-2ebb-3b40-90ed-e556bd11caf8 | -11.2024 | -54.8567 | 2026-08-04 01:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 6962efc7-31c2-38f3-9a98-ac62b3cac020 | -6.5329 | -55.1578 | 2026-08-04 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 57c5bc19-0b33-368a-b517-727d2f4a5e8b | -11.2213 | -54.855 | 2026-08-04 01:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 6787bd33-9c58-3ec1-8719-9e0cbfbc61c0 | -6.5697 | -55.176 | 2026-08-04 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 7e4fd774-7b87-37e3-a5c0-b79f42b571de | -5.1504 | -46.2248 | 2026-08-04 01:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| ec94809d-28d3-3ab0-bfe7-e3bfbceeff96 | -6.1299 | -47.2884 | 2026-08-04 01:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| d0c37089-a9c8-3591-8449-de8a23c35392 | -13.4448 | -43.8604 | 2026-08-04 01:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 149eb6b0-83ed-3f6c-9f62-31532e08d07d | -13.4254 | -43.8639 | 2026-08-04 01:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| e4175925-4340-3e49-9c90-14056d6f098d | -11.2022 | -54.8771 | 2026-08-04 01:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 31c1722d-3705-30f3-976c-af28116fa478 | -3.6639 | -49.4686 | 2026-08-04 01:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| df93b6fe-1ab5-3f23-8e84-5448816278be | -11.2211 | -54.8754 | 2026-08-04 01:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 9029436f-8ecd-3e8f-97c6-26bd0ad50289 | -5.1507 | -46.1803 | 2026-08-04 01:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 229e02a9-a657-3b1f-b831-3da61f28b5f1 | -6.5514 | -55.1569 | 2026-08-04 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| af8373c0-a43a-3b4c-a14a-53301799d940 | -5.1319 | -46.2037 | 2026-08-04 01:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| cc7249bb-ac7a-3542-a233-64505aa4e813 | -6.5699 | -55.156 | 2026-08-04 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 03d1694f-d1c1-32f7-8eef-b7cfa751d3be | -8.3546 | -45.9671 | 2026-08-04 01:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 34.6 |
| ea9d963b-94df-3de6-9e96-e55da85693c7 | -6.5512 | -55.1769 | 2026-08-04 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| ced21b44-4e30-3878-a0b2-0a6ef057c86c | -5.1506 | -46.2026 | 2026-08-04 01:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 166.4 |
| 3deaa1b5-6513-3f27-b801-618889ee8903 | -8.3544 | -45.9897 | 2026-08-04 01:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 6d6d2e95-4557-3ced-a820-fac83c012ba0 | -8.7738 | -63.6343 | 2026-08-04 01:09:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 03e6365f-8c68-3dd9-8f5d-a29d25456a72 | -7.238 | -59.452702 | 2026-08-04 01:09:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb4b848e-1fdb-3c67-8681-8735daa55e9f | -6.5271 | -55.164299 | 2026-08-04 01:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b54eeaba-189c-3b6d-9542-9cc4a708b475 | -11.2065 | -54.879601 | 2026-08-04 01:09:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e3318c4-9b72-34db-8ef1-9779ee0057f3 | -8.9532 | -63.242802 | 2026-08-04 01:09:00 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a2ab2bc6-324a-365a-8a3b-19328873abe2 | -10.8263 | -65.090401 | 2026-08-04 01:09:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 15b8a444-282b-31de-955c-ab235f96d591 | -6.5561 | -55.157101 | 2026-08-04 01:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7d88679-56c0-3947-adbb-3fc1c75803ea | -11.2117 | -54.8592 | 2026-08-04 01:09:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c362c5bd-ee12-375e-b010-5dfc388c612e | -6.5515 | -55.179901 | 2026-08-04 01:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37531e05-5965-32de-8dc5-c8acce020dd0 | -6.5464 | -55.1595 | 2026-08-04 01:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e30b64c8-b1fa-3c41-a8c2-d4a4dff3a340 | -11.1924 | -54.8643 | 2026-08-04 01:09:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a609f75-0f04-3811-a5c9-8e2d21a35fc1 | -11.2162 | -54.877102 | 2026-08-04 01:09:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f619892f-ac19-3a05-8378-67cb44a675ec | -6.5367 | -55.1619 | 2026-08-04 01:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31544cc2-4a26-357c-bc73-a1ef294030aa | -10.8248 | -65.083099 | 2026-08-04 01:09:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 14d44780-b701-31f2-ba2a-7a0e9e280ed7 | -11.207 | -54.841202 | 2026-08-04 01:09:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7ad6173-4e07-3b49-80c5-89245a34c846 | -6.5657 | -55.154701 | 2026-08-04 01:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59634a75-630a-3982-a182-e9ea50f2bb63 | -11.1969 | -54.882198 | 2026-08-04 01:09:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa0b0f2f-81d3-397e-a81f-9a489fca46bf | -8.9547 | -63.249802 | 2026-08-04 01:09:00 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9feb0002-e813-324c-bd15-5b4fc9bd5c5b | -11.1872 | -54.884701 | 2026-08-04 01:09:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f575af6-40f0-37d1-9c68-6507f734672f | -8.7754 | -63.641201 | 2026-08-04 01:09:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d6b6bd9a-fcde-3391-bf9e-365bae0971b3 | -6.5418 | -55.182301 | 2026-08-04 01:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 942ff654-9df6-38da-8327-c4f364c0500c | -11.202 | -54.861698 | 2026-08-04 01:09:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
