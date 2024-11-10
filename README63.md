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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54c5c5d0-8d76-3571-bc77-218c23ec0c47 | -2.10686 | -49.50403 | 2024-11-10 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 499047d5-cf93-35ec-9983-3cbe0e3d33aa | -2.07074 | -50.34883 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 110fdf79-f6c6-3981-8174-800ecb7078f9 | -2.09316 | -46.34049 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b307c95e-ce01-351e-b656-28b1f7c8ba1f | -2.16406 | -50.1963 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1bfde8e-7041-33b5-aa13-9f2382949537 | -2.39912 | -46.59574 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8370888-4bac-3cb7-b306-b43579ca30ce | -2.4591 | -47.93603 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 815c7f6e-ae70-37d5-b267-f85cb17929e1 | -1.849 | -51.1132 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dec7e32c-2dcd-30f5-8bc0-e07ffb417845 | -2.16587 | -48.53297 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48987dfe-407b-315e-a1a9-4c6912f71d88 | -2.6302 | -46.76938 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4561bc90-ad44-37b0-80d3-b09f32b5cb1b | -2.11768 | -48.1092 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dc7f205-801c-3501-8af7-72bc71c74c93 | -2.35179 | -46.67494 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb63a682-972c-3150-a019-d182091e2645 | -2.57167 | -46.53785 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df30f8bc-d6f9-320f-b566-d57cbe57ea1c | -1.56806 | -52.25198 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9ec4b7c-9b58-35b4-acb3-7dea30f12d92 | -2.22879 | -46.6149 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64cffa46-611c-3bd7-b8e2-2de5c1d2721b | -2.21242 | -48.38851 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72846975-f610-3d0d-b93d-c7c894cf0cee | -2.67939 | -46.78819 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 255f3c89-f19f-3cbf-b46a-9bb82d9be796 | -2.10319 | -46.47918 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5adec1d1-d39a-343a-aeef-0f03690f3298 | -2.37561 | -46.81304 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07424171-2c2a-33f1-873e-17c50d484d57 | -1.98119 | -49.01796 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8dbc6e3b-6294-377d-aab7-d84847ecc4bc | -2.11978 | -48.2472 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09b2aabc-4baf-3d0d-92ba-9bd4c4ed8492 | -2.07352 | -48.47636 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b01cdae8-32c3-35ec-bc58-41f8fe9f24b6 | -1.22712 | -51.75487 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d786c343-427c-39a3-b445-ccd69b719074 | -1.52903 | -52.21066 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3bb14b08-551d-3c6f-b1e8-9979d0c0cfc3 | -1.60835 | -52.00261 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee0fe784-605f-384c-b91f-7952d30ff3f0 | -1.40956 | -48.13584 | 2024-11-10 04:36:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86f4c90f-7877-30db-b1c1-b07d471eeb77 | -1.48568 | -51.58471 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 892c989d-7699-3833-bd69-7231decf412f | -2.53733 | -46.31089 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b767a33-96f7-30f9-bd56-6386db943b51 | -1.96595 | -51.54231 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d47ab31-48d7-30c4-b0dc-55ac67e5c0dd | -1.42601 | -52.27702 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12cf097c-bf3d-3af8-8d44-7b37c2d7d599 | -2.20355 | -48.38007 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f35870f-5bb8-37de-b1a7-bbdb4f141020 | -2.22764 | -48.48612 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3c0a263-d0de-3178-aaf8-331afc299934 | -2.35862 | -46.67599 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09b6ad51-b122-384b-91d1-ea3ec7813647 | -1.71603 | -52.46928 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c2772694-d26b-3805-80ad-e2ac6d767b47 | -1.21759 | -51.76685 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edcc4ea5-7d7d-3c88-b1ea-978e6d3f469e | -2.43664 | -45.98685 | 2024-11-10 04:36:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9769dff-c6f8-3c1a-9517-42dcf7133914 | -2.1587 | -48.53538 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 078e21f0-9f70-3117-a53a-ca2cc1ecd36e | -1.72563 | -51.1608 | 2024-11-10 04:36:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 882f8b0c-f487-39c6-ab25-35fae5b8858f | -2.19662 | -46.79654 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbc6f021-f9b8-3b4c-9f90-91fecda2ddbb | -1.6355 | -48.20663 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 282a6393-334e-3d8b-88de-b00578bf2fd5 | -2.3308 | -48.85964 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83061e0e-6e69-3c4f-b41d-110496fafc92 | -2.37268 | -48.57274 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6065eab-25dc-3d0a-b8d0-eb1aed8805a8 | -2.34702 | -48.92953 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffe6f66c-5e46-30bb-bd14-c0ed7bc7cfa0 | -2.68677 | -46.80803 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85faa378-2071-3669-ba19-5b93fb7d124a | -2.24875 | -46.50483 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84ddc99c-aa3b-3734-bfaa-1698c0c28772 | -2.36539 | -46.85604 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ff5b19c-65df-39be-8e91-b23ecdf481f8 | -2.09054 | -48.82187 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 56293a3d-67a2-3577-af45-63b622dc5b64 | -1.87535 | -48.55425 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54e84a67-7868-3530-928b-dd36e7b967ad | -2.22703 | -46.42542 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cba52eab-339b-386c-8b8b-1c4603868511 | -1.69938 | -48.16707 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18f48735-ec0c-3a67-97e7-a8f3d631a9ff | -2.10803 | -48.55937 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4817888-a7f7-35f9-bd31-a4841a68f7da | -2.20954 | -47.74078 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 12f49295-56a2-30da-890d-a831c91e5c07 | -1.52523 | -52.21006 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ab0aad07-939f-3f72-9bd3-c586612011a3 | -2.67882 | -46.79184 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bcdc1aa-b35b-3c42-af09-3c47996baf62 | -2.21851 | -48.39298 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be8fcb76-4e9f-3443-bdc1-dfafd89ed77a | -1.76662 | -45.60894 | 2024-11-10 04:36:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72966528-24b1-3a97-907e-3c07db2ff070 | -2.62148 | -46.16744 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c9d4fc0-52d9-3d74-ae01-fb2ca840a04e | 3.36884 | -51.26511 | 2024-11-10 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8174a09b-d723-3eed-b2fb-49b5271f49c1 | -1.83854 | -52.15491 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b89076c2-5f90-3361-b99e-27c171e2264c | -1.52668 | -52.20087 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fcaed78c-0124-3ffd-9c4f-5b697a9e7fde | -1.48379 | -54.40276 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9c43ba87-27ac-370a-97a8-d63c4a290967 | -2.46696 | -46.87487 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a4747e3-8135-30d2-af5d-fb3d3d2ed4ec | -2.39492 | -46.7788 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f3bdb93b-b6bc-3efd-8cbe-152e85fd5c53 | 3.73618 | -51.63562 | 2024-11-10 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1473e90-a8d5-395c-b480-47789fb45def | -1.99331 | -46.3563 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1646e385-74bc-35d0-8602-85ef919b8026 | -2.23792 | -46.55235 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd604680-030f-3a8a-a402-ce96f5caebe8 | 1.56463 | -56.02932 | 2024-11-10 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7decd4aa-aa40-32d8-a286-008cb1c34e85 | -2.62727 | -46.14551 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29f364f7-c5c1-35b4-afa3-612e91b4ab0b | -2.6811 | -46.77722 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 911a0e24-589d-38a0-8c4f-4cbdbc2de631 | -2.37974 | -47.92687 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fae27d50-d351-3fb6-81a3-4ae2c7d3e331 | -2.4012 | -48.88834 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bf643c0-276a-3335-b74e-4c19390f9531 | -2.55058 | -47.32737 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2922104a-c77f-3b53-8695-e0fdd76ff1cb | -2.23465 | -46.84348 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a40a2fd-a98d-3cdb-9858-2775f457fec2 | -2.03254 | -51.16612 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 748495b7-f889-39e3-9a4c-6066a9c05f32 | -2.04718 | -48.98909 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f709f9d8-88d5-3858-8e4d-4ffc640caa3d | -2.50791 | -46.29477 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 884d19fb-5b26-30e9-b383-21521a5cf708 | -1.15528 | -53.78693 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1cc8a52c-7282-3b2e-9fe8-8bea61b57bd0 | -2.42985 | -48.46871 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f8bc2a1-373e-376b-870d-0098cd7bbba7 | 3.73695 | -51.6406 | 2024-11-10 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f21f2c70-c12f-3fd1-a646-7f054cea1b67 | -1.98508 | -51.51529 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f697c56e-e2ab-3791-84be-32f12f6db8c1 | -2.20494 | -48.86442 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77a77ae1-5bf8-3031-b29c-42501f7e0200 | -1.80971 | -52.26264 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30f65c18-7ba5-3f4d-b4fc-463543113171 | -2.36761 | -48.54019 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02631b88-6fb0-3bfe-8aea-f4328d33e365 | -2.53387 | -46.31034 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d9d519c-c8ed-3ad1-947e-413b58934aa5 | -2.61318 | -46.16693 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 108b9d75-73dc-3c74-8b50-b7ab82715f3c | -2.99665 | -45.02969 | 2024-11-10 04:36:00 | NPP-375D | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5c7a459-0341-3dfd-8a2d-16ded1e118fe | -2.5004 | -46.29746 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c52032b3-66a9-3915-bd35-a7ef048b146e | -1.55002 | -52.27548 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 384a3884-753a-36f8-850a-aaa0eefbe79e | 2.85491 | -60.07843 | 2024-11-10 04:36:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51d0352f-42aa-33ac-bd31-6e3d492c2042 | -1.62941 | -52.23338 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2449f7e8-01f9-3db1-9980-dbff8a6f1fb5 | -2.18677 | -48.31395 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ed764ac-7537-321d-b9a7-2d20275e116a | -2.66972 | -46.7154 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19cdc140-82a1-3309-8593-737f000de21e | -2.46575 | -47.93706 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcfcee38-2015-31d2-a77b-6c93d6259bb1 | -2.13998 | -46.69109 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da53ee02-f928-36b2-92f4-d147fb552173 | -2.23787 | -49.86102 | 2024-11-10 04:36:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b69eb61f-f8a6-3019-bd77-0ccef58e9287 | -2.63256 | -46.04379 | 2024-11-10 04:36:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 599dcc6a-2260-359c-a966-763739ee16e8 | -2.14216 | -49.00729 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43ac9cdc-aebf-32a3-a72d-033ea493a1cd | -1.62137 | -52.53481 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2393a10e-dd41-3875-a21a-9fa340f6c0fc | -1.83396 | -47.93368 | 2024-11-10 04:36:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9ab8224-d09f-3b00-bd08-d7a91f84fb78 | -1.61838 | -52.53662 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b7d1ffe1-2ba9-30e0-81e9-1c46cef7243b | -2.14523 | -49.13966 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README64.md)
