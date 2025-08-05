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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfcc91a8-1305-3b6d-be00-2f87bfd5c708 | -7.994 | -43.1534 | 2025-08-05 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| 560a37a5-5b84-328b-b24e-a320173e7ac1 | -8.9478 | -46.7354 | 2025-08-05 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 2385a8ca-f989-3755-8daa-728a66121329 | -8.012 | -43.2219 | 2025-08-05 12:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 109.7 |
| f7981625-9f5e-3dbe-809e-5123a3d736be | -13.0914 | -56.9114 | 2025-08-05 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.7 |
| e5c3e2e2-6b70-327b-a6bf-822b4b2a9cee | -8.012 | -43.2219 | 2025-08-05 12:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| bce1301b-4974-37bb-9cec-b438d9d69d40 | -6.2173 | -45.8621 | 2025-08-05 12:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 71cff5d5-d86a-3f07-928b-0d0624535dae | -8.9478 | -46.7354 | 2025-08-05 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 559a7766-96ab-36d5-959a-8448e50d1c9f | -7.7062 | -45.1254 | 2025-08-05 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 647fe01f-f707-33c5-b90d-5ec0e80c09a9 | -13.0914 | -56.9114 | 2025-08-05 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 6d9ce3b6-25b1-306d-b584-9dde055c0380 | -8.9478 | -46.7354 | 2025-08-05 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 289c43e5-1a5e-3090-be0c-db0854da370e | -8.012 | -43.2219 | 2025-08-05 12:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 180.9 |
| 3232f65c-50e5-352d-b761-ea654952d353 | -7.6873 | -45.1272 | 2025-08-05 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| d7c5216b-d029-39ef-a512-e8f4ec9b9edd | -8.9478 | -46.7354 | 2025-08-05 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 34acf9be-07b8-331f-a9e7-e7d6414b5b91 | -7.7613 | -45.2338 | 2025-08-05 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| af4d0f6d-8a69-3f09-8102-4344528719c4 | -8.012 | -43.2219 | 2025-08-05 13:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 183.8 |
| a54527c7-28b6-33ba-bb43-7af49e0954f6 | -7.7616 | -45.2111 | 2025-08-05 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 87c00c99-9863-349b-88c2-6c1f6fcbe93a | -7.9931 | -43.224 | 2025-08-05 13:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 40633346-c366-3253-aeb5-59d5f7ab9e0b | -8.0123 | -43.1984 | 2025-08-05 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| abf5882a-9661-3c04-aa85-cc3da31abcec | -13.0914 | -56.9114 | 2025-08-05 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 686e4835-a96d-3562-8583-a08a84921fcb | -8.9478 | -46.7354 | 2025-08-05 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| d67f17d0-caf3-3403-a5e0-f101173dd0b3 | -5.7887 | -43.6134 | 2025-08-05 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 193ad60d-cefa-3359-a92a-e77185f74027 | -6.2932 | -45.7441 | 2025-08-05 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 93ea8546-0f3e-3008-a5dd-fa537d3ad801 | -13.0914 | -56.9114 | 2025-08-05 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| ce727576-8882-3c21-a7b6-85a2ef1dcb86 | -8.012 | -43.2219 | 2025-08-05 13:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 161.0 |
| 60f72a2e-2288-3fdd-b4a7-656ad5780fa5 | -7.994 | -43.1534 | 2025-08-05 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.7 |
| 804936cf-2cd8-384f-b353-ddc9b2a37a2a | -7.9931 | -43.224 | 2025-08-05 13:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 139.7 |
| 1f313b76-3420-37c8-b68b-cff8e74dc84c | -6.9605 | -42.8816 | 2025-08-05 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 197f4380-2960-333e-96d0-d82a92f3f5bc | -13.0914 | -56.9114 | 2025-08-05 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| c1060e52-aa0b-3aea-b625-d0d983964296 | -8.9478 | -46.7354 | 2025-08-05 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 6deadd5b-3cff-3cba-a3d8-271dc50d1b09 | -8.012 | -43.2219 | 2025-08-05 13:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 231.9 |
| 8a9bfe20-03c8-3a34-ba4f-41d23b2f9a5d | -7.0946 | -44.3589 | 2025-08-05 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| bfe3fbd0-2988-32c6-8b28-ee0096d599bf | -7.5585 | -44.8887 | 2025-08-05 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 942a0306-aad4-3e0d-a0e2-288867f06b4d | -6.2173 | -45.8621 | 2025-08-05 13:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| cbc94469-ef81-33ef-9ab0-8b6ba569c1f4 | -7.7425 | -45.2356 | 2025-08-05 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 54abf118-f2b7-3fac-a837-f063fa11283f | -7.9931 | -43.224 | 2025-08-05 13:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 157.8 |
| fe4298d5-7003-38f5-b6a5-d6834ec5e03b | -5.7887 | -43.6134 | 2025-08-05 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 9951ae9f-c163-32d9-80ae-3b34bd9ad6d3 | -8.0123 | -43.1984 | 2025-08-05 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 30daed52-49ff-352c-a5de-0605f20dc3ff | -7.7613 | -45.2338 | 2025-08-05 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 28d41847-f65b-38fb-a2ec-ced290a3a94a | -8.0117 | -43.2455 | 2025-08-05 13:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| 85a34fc6-37fe-3d2e-b05c-2f94052c6188 | -7.9943 | -43.1298 | 2025-08-05 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 4a33c654-9e88-31fb-a256-37f3d3a5f5da | -7.994 | -43.1534 | 2025-08-05 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 6ab89950-c11f-35c9-af9f-710497d42860 | -6.236 | -45.8607 | 2025-08-05 13:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 1afeb2ca-8392-3406-b230-d60b178b3a19 | -7.0757 | -44.3606 | 2025-08-05 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 39d4ef2f-eb2b-3f18-a7b6-55e7b89656fe | -7.9934 | -43.2005 | 2025-08-05 13:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 3832c8b3-cba7-3aa4-acf2-05c30420203a | -8.9478 | -46.7354 | 2025-08-05 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| d7767d8a-bb7c-36af-836c-e5bb283984dc | -7.7613 | -45.2338 | 2025-08-05 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 7d6a8cd1-9e2d-3a14-9b92-e5735632000a | -7.9931 | -43.224 | 2025-08-05 13:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 164.0 |
| cfe13d5a-2c3f-3a62-a99b-0a11a5709233 | -8.0117 | -43.2455 | 2025-08-05 13:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 45987882-fd19-3977-92f7-fa66cdcd1b65 | -6.2173 | -45.8621 | 2025-08-05 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 5269c407-e6c4-3d4d-8725-93394fea2162 | -7.0946 | -44.3589 | 2025-08-05 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| e9f247b2-ca1b-37d2-bdc7-e27e066062df | -7.5585 | -44.8887 | 2025-08-05 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 4f1a7978-25a3-3707-b060-cddf00422030 | -8.0123 | -43.1984 | 2025-08-05 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| eb29df57-f73c-3591-a1ca-e1901e8a83ab | -6.7689 | -44.9823 | 2025-08-05 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| abe001f5-6d9c-32b7-b207-215aede0c88e | -8.012 | -43.2219 | 2025-08-05 13:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 237.4 |
| da1e154a-7eed-3b7c-a76e-0dd62c683546 | -6.236 | -45.8607 | 2025-08-05 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 2294a296-6d0a-32c1-ba61-fb412eba7870 | -13.0914 | -56.9114 | 2025-08-05 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 133.4 |
| e00d71a1-ed4f-382a-8644-9504e5fd61ce | -5.7887 | -43.6134 | 2025-08-05 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| db474069-ccfb-32b1-8ad5-2a1b9b66f42a | -7.7616 | -45.2111 | 2025-08-05 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| aa18daed-f342-3f41-bf13-fd65237b4019 | -8.0117 | -43.2455 | 2025-08-05 13:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| e2c1bf27-e39e-3fd9-993c-80b2478185aa | -7.5585 | -44.8887 | 2025-08-05 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 19b4908a-ab78-39bc-a515-811ef03de568 | -8.9228 | -60.5376 | 2025-08-05 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 153.0 |
| d7a98b9d-cc6e-3a80-9891-0d7c7a49d079 | -7.9943 | -43.1298 | 2025-08-05 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.2 |
| 518dc1f8-0013-3191-a7cd-5677d2ac009a | -6.433 | -44.8279 | 2025-08-05 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 04e79cd1-c0f1-3820-866e-3f04f6b99b77 | -7.994 | -43.1534 | 2025-08-05 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| 3c45bd87-9bb9-3c34-a2b1-13e549280dfb | -8.3661 | -46.571 | 2025-08-05 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 8faf7126-65c5-3d02-a7c2-54f47d6c820d | -8.012 | -43.2219 | 2025-08-05 13:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 283.1 |
| 256bd986-5d48-3e9f-8756-bd7939eb8299 | -7.7616 | -45.2111 | 2025-08-05 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 28cd96f0-1413-333b-9f7f-ea90cfe712be | -8.9227 | -60.5568 | 2025-08-05 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 358.2 |
| 82996984-75bd-308b-9aa8-4869243f44b1 | -6.9793 | -42.8798 | 2025-08-05 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| ca957186-75c9-3a8c-9027-51fdff210b3f | -7.9931 | -43.224 | 2025-08-05 13:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 124.2 |
| 50637765-88e0-32a2-923f-5a5deffbb424 | -7.0946 | -44.3589 | 2025-08-05 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 11cf57e7-92b8-3d3d-b853-b39ff71baf62 | -8.0123 | -43.1984 | 2025-08-05 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| 903c2b11-aa9a-3e9b-88c9-11a186216b48 | -6.236 | -45.8607 | 2025-08-05 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 6371e674-1d50-3a7a-8432-ca3aab4549ec | -6.2932 | -45.7441 | 2025-08-05 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 96cbd693-0eec-3ac3-bd5d-c819d3633baf | -7.7425 | -45.2356 | 2025-08-05 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 99b43173-68b3-35d9-ba5c-d02da8dc37fd | -13.0914 | -56.9114 | 2025-08-05 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 9a92a767-860c-3044-a78f-e35a9e457c53 | -6.2173 | -45.8621 | 2025-08-05 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| df44412e-90a5-3226-9660-7c94fcb6f1d1 | -7.7613 | -45.2338 | 2025-08-05 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 2507d5ca-1fe9-34b7-ae48-70c14ace17dc | -5.7887 | -43.6134 | 2025-08-05 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 3134976c-9e78-35d1-ae62-31c58eae66ea | -7.0757 | -44.3606 | 2025-08-05 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| dddd07d1-50ae-36b0-bf8e-25831b2dd851 | -8.0123 | -43.1984 | 2025-08-05 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 6365b3d0-aa55-3506-800f-2b4becf789b5 | -7.9931 | -43.224 | 2025-08-05 13:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 169.0 |
| 7628132c-6f71-3692-9237-eba1b4d4b278 | -7.5585 | -44.8887 | 2025-08-05 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 50aab63e-5cd0-3528-b242-e17d5efbe221 | -13.0914 | -56.9114 | 2025-08-05 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| d2134ab3-c1c5-3a90-ad7e-ebde8a3fd2c9 | -10.8064 | -46.4985 | 2025-08-05 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 26d67184-fe51-3eea-8630-2200f6d4bd74 | -10.7842 | -45.5037 | 2025-08-05 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| f4d71732-3e4f-38be-aaaa-ffb04df56899 | -7.8383 | -45.0899 | 2025-08-05 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 6ecd8d7f-e6ce-3dea-87ab-670f177e55b6 | -6.2789 | -45.2716 | 2025-08-05 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 0ac894b8-3727-35d0-bcbf-d3a2a72fa7fd | -6.2173 | -45.8621 | 2025-08-05 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| de7e13c8-63f3-306c-bc16-436926e8c7bf | -8.3661 | -46.571 | 2025-08-05 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 495bea53-df7c-308a-a3a4-7f3859c56237 | -8.3663 | -46.5487 | 2025-08-05 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 5d45fd5e-b931-3ba4-bd42-35068d514f5e | -7.7425 | -45.2356 | 2025-08-05 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 43afafc4-3060-33d3-a63a-53e77d1b7e63 | -7.7613 | -45.2338 | 2025-08-05 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 194.3 |
| a65e8dcc-4c0a-3d9e-9664-d104559fe63c | -8.9478 | -46.7354 | 2025-08-05 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 5c2b8cfb-f649-3016-ab62-b5c3e8616d9d | -13.0538 | -56.8746 | 2025-08-05 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| cff77769-2242-32cb-ab05-3aab9d7f0aa5 | -6.9607 | -42.858 | 2025-08-05 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| db406adc-c1e7-38e8-9e3c-6cd53f21ec4e | -7.0755 | -44.3836 | 2025-08-05 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| a64d1054-78da-3705-903a-b6fe79dc6764 | -6.9793 | -42.8798 | 2025-08-05 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| 63dad093-a14f-3fc5-9dcd-a1be8bc7a6f6 | -6.2932 | -45.7441 | 2025-08-05 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 3204bdf3-c81c-3f1d-b218-b8191d6c62a1 | -6.236 | -45.8607 | 2025-08-05 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |


[Clique aqui para ver as próximas entradas](README33.md)
