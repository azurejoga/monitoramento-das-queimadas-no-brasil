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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0996fe3a-cc0c-336e-aeac-0f4b3f32bd97 | -3.21898 | -42.96337 | 2026-10-09 05:01:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4433e181-2b5f-3983-bf5f-15f64477b524 | -3.07331 | -50.96049 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09f38cb4-579d-3cb4-8cc0-1236f476cbdf | -0.99853 | -47.65464 | 2026-10-09 05:01:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d7a798ec-b80b-3640-abe9-99d3878635ee | -2.35827 | -48.88401 | 2026-10-09 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d45959b-5f76-33aa-8a9c-f484cef30060 | -2.74374 | -54.09906 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 845f3475-3ba6-3dc6-b76e-e14a8b4874ab | -2.74951 | -54.04061 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 912b43be-91ad-3abc-9ac5-94dd62e9a0cc | -3.35086 | -50.41174 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c42d4b69-bac4-3864-a57b-72532814ec9c | -3.39252 | -50.2143 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa544014-775a-3a88-9049-78d0830320e0 | -2.78431 | -54.06986 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ce3166b-5ea9-3f48-bce5-54a81e46621a | -3.20488 | -50.56167 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2a7957e-e748-3ace-ad4a-7f43638af877 | -2.73424 | -54.11344 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 867acdb6-8813-39fe-8b67-544f54df2bfa | -2.83143 | -54.13586 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22f87f5a-80bc-3048-a7ab-3e964d1ef7e7 | -1.10859 | -54.15225 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7083e063-ace4-39ef-b0f3-14ff905660eb | -3.16501 | -50.59556 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 904a4f38-fe4e-3f64-a031-a0f67da2a928 | -2.57317 | -54.01432 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 601087d7-c91d-3da1-b6ba-bf443a5acb13 | -1.20048 | -55.68623 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8947087a-43cb-31ce-b25d-826224da19df | -1.4767 | -53.61167 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9067522-1f45-36c3-b221-43b840ff6efe | -1.7271 | -56.06611 | 2026-10-09 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5040f170-fba4-3085-94ce-5eca2ba6d1df | -4.35879 | -44.35181 | 2026-10-09 05:01:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e60b1ade-0b72-388f-8681-579a8f482ba4 | -1.8703 | -53.96708 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9d78d37-fe11-37a8-8d92-566594a06e24 | -1.45291 | -54.77626 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9f7e0aa-1b2b-357f-96a2-5af5811bae79 | -2.79689 | -54.08275 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10c89f00-0c03-3c47-aa8a-3601b8307ac7 | -3.20601 | -50.55455 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| caf95a06-39a9-34a4-a57b-b23ca58185b9 | 2.41614 | -50.82545 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 1c52617f-c51e-337f-9290-4de0ae0a9cfe | -3.26248 | -50.39464 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a68a80fc-5375-31bf-b822-56caaf8b2112 | -3.38513 | -50.21688 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7d564fd-42af-32d2-af35-21fe7c9544b8 | -3.1768 | -50.58647 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16d8f5dc-e754-3f5c-aa41-9515c991cadd | -1.42135 | -54.62239 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b52397ed-6fd7-35a9-8564-ed6951a1e6cc | -2.50528 | -56.12868 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 084ff7c7-e6d9-346a-a3b0-26853c365ce7 | -3.36434 | -50.48332 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ab831ba-3b98-32cc-a09c-c3ea09cac440 | -3.25117 | -50.40026 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3cdbcf7-740f-3354-916c-bc4a930075bb | -1.48701 | -55.86887 | 2026-10-09 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4721f3bb-e39b-3aff-917f-392dfffd516e | -1.19191 | -55.66505 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6c8b67e-c0f7-33fe-b557-71c15bd48a55 | 1.0584 | -50.03223 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3740a123-a794-321a-8462-00157ec1b253 | 0.5063 | -50.77588 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a4dc0ff-e55e-38d1-9c18-17eeff4d92a4 | -1.70605 | -55.43649 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43868562-f22a-39cf-a84f-b16f50e7ad21 | -1.52701 | -54.52038 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94c249e1-51b3-3e17-890b-2fd2940e3074 | -1.26659 | -54.68261 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30850508-3200-3897-9d40-834c0c6a114d | -1.64326 | -55.27868 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab613202-5d64-35d6-8c2d-7ecc1e99e0ff | -2.74414 | -54.119 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d7e40ae-9bf5-3373-8968-73d82573fe53 | 0.94191 | -50.19697 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a82f45ae-61b5-3045-9e86-b946b0f3dbde | -2.3388 | -48.86872 | 2026-10-09 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 51286816-711f-3996-9a00-f7bfeb1a9f4e | 0.53543 | -50.89499 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70b2f9c4-930b-3c96-87f6-46a63a97c967 | -3.14873 | -51.62347 | 2026-10-09 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aed0b23a-73f5-344b-832a-e3ac9c0de7df | 0.97478 | -50.12403 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e105682a-2c1d-37a2-bb33-a8820c530bb5 | -1.48309 | -55.86829 | 2026-10-09 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 351131b2-e894-30f4-a4d7-d81846bdc2a3 | -2.82615 | -51.28528 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d55468e-f90a-3acd-9ad5-d990517bef60 | 2.26165 | -55.98336 | 2026-10-09 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0e65521-8ffc-3e7d-97ed-dcb3c63543f9 | -1.13045 | -57.28833 | 2026-10-09 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 601ddac2-9dea-379f-86ee-65f1b3de9083 | -2.41001 | -56.53645 | 2026-10-09 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b241b0d0-8902-3e3d-9f84-091a1acf67f7 | -2.746 | -54.10737 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 07c8a429-213a-3544-bfb0-24f11f56a5dc | 1.15873 | -51.17558 | 2026-10-09 05:01:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55aa86d1-424c-31bb-8159-02c749534d7d | -2.74889 | -54.11181 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c4a1c0bc-7f7f-3e26-8983-da834f2a9243 | -3.1622 | -50.59148 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad35a036-30cc-31b8-a590-943946b3c5d6 | -2.94875 | -51.41154 | 2026-10-09 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed36e3e5-a7ef-3e46-b7e8-04c0c6a10dc4 | -2.75855 | -49.5337 | 2026-10-09 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67ea4c92-0e8a-3093-8941-b900baa8457a | -1.5269 | -56.11791 | 2026-10-09 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d3d215ed-c1a7-33eb-85e5-b9732302c9bf | -3.17568 | -50.59359 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7256299e-9caf-3392-baae-2cf5af053f6f | 3.73388 | -51.62333 | 2026-10-09 05:01:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90355561-978c-3a61-bf09-8fcffc07b682 | 2.41559 | -50.82199 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 87afe5a1-866d-3819-be05-7dc047d66abd | -2.50755 | -56.16431 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44b49455-fa04-366a-81f5-67650ce0b9df | -2.36244 | -48.88058 | 2026-10-09 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1909a88-d235-38f7-9320-e2ea66ff9037 | -2.75611 | -54.08913 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a31e3bb7-2f4d-3d63-8818-86b6e9bb5399 | -3.19589 | -50.55297 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5f1bbfd-c337-3578-a869-af91c01f39a2 | 1.1554 | -51.1761 | 2026-10-09 05:01:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c005f5c1-64d7-3c3e-8836-cc61a9c4795a | -3.00863 | -51.01152 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 42db4f4a-a982-3a21-88dc-1ad1394f9c14 | -3.32097 | -50.18077 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec98bdf1-1950-3716-baab-97043592e3ca | -3.02959 | -42.10868 | 2026-10-09 05:01:00 | NPP-375D | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c6c6d2a-b58b-3d49-ad00-13c48777beea | -2.08557 | -46.57369 | 2026-10-09 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a131141-836f-388e-bb58-efadbdf30889 | -1.31986 | -55.44048 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 877a07fd-1733-386c-8489-7a671eb7d75e | 3.85942 | -51.77815 | 2026-10-09 05:01:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35c4ec9f-69b8-389b-b5d5-ba6e0b164e4f | -2.75178 | -54.11625 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ef5495bc-16e3-37c3-9846-a30f985d2133 | -3.20151 | -50.56115 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5481dfcc-98df-30a5-9841-c379de670279 | -1.49052 | -54.53976 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2bd2559-d3ae-341f-aa53-6204e07e5232 | -2.50295 | -56.11829 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6c86aaa-20fe-3b94-b4f4-922810459728 | -1.15691 | -54.22906 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 11c617e3-7fbe-3993-8fee-bb979a92f20e | -1.61805 | -55.12066 | 2026-10-09 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a00ac676-f7d7-3845-a50a-3feb5baef889 | -2.78081 | -54.0693 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38ecf315-1d0e-3fa4-af81-5591328f26ad | -2.75075 | -54.10018 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 928b272b-6c3c-3c09-9120-84bf06935095 | -2.78309 | -54.07758 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83cf6389-707d-32ae-ac15-62fe00a90ae0 | -2.26727 | -48.05585 | 2026-10-09 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| babcc021-5a13-33fa-ae79-27456852958c | -2.46945 | -56.0808 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68b7a332-d8ba-3d1f-90ac-423a0235d967 | -3.19421 | -50.56366 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 086bb5ec-ff7c-37f2-94a9-460b29376688 | -2.83681 | -54.12479 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50ee311d-570a-37a8-a945-64a606dd7f19 | 0.92472 | -50.25285 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27fb9943-675a-3aec-8606-d9cf8f0f2521 | -3.00753 | -51.0185 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c823f9c-8625-395c-b603-29993b2cbcc1 | -1.38907 | -55.46407 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d83385e-242c-3879-b33b-efa607a48330 | -3.279 | -50.02465 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc929f61-a36e-3ba1-bcab-ab7ec93bf6ce | -1.18686 | -54.17979 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42ea300e-e22e-3360-9111-76d1a88b0005 | -2.76064 | -54.10575 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e339036-6048-3b6f-9023-475137379713 | -2.08099 | -46.57653 | 2026-10-09 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adec381e-9071-3c02-aada-1db8e925ce1c | -2.46869 | -56.08563 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 92088955-055c-3fdc-b168-55f2dde1fc9f | -3.16769 | -50.44604 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbabd7da-5104-3184-88c6-b558ac78d193 | 0.44678 | -60.53781 | 2026-10-09 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26299b41-ceeb-3453-9885-f9bf3b590f7a | 1.67985 | -55.63511 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb7281a1-3baf-308c-b38c-c37e5a735273 | -1.52709 | -54.56723 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a72db8f3-4cca-3e47-8841-42184b931206 | -1.72222 | -57.14961 | 2026-10-09 05:01:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a0c5552e-68ba-3935-9b2d-bacb1e9b4a15 | -3.47889 | -50.08467 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a310803f-439c-35cb-8cc8-d7b8e06c16cf | -1.8092 | -57.11889 | 2026-10-09 05:01:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9dde59b2-6171-3bd7-9041-7397f139f69a | -3.18635 | -50.59161 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README122.md)
