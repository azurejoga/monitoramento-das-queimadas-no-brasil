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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74c81bc7-41a8-3708-afc7-77fff005b1b3 | -6.81704 | -59.66741 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66e45590-0bb3-387e-a9bf-a88184618d16 | -6.81935 | -59.67362 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e282d44a-374a-3b76-a523-29d8489b9c8c | -6.3782 | -54.95157 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d755b447-2f78-3452-9868-e585a839fb91 | -6.55511 | -55.09604 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6e628f64-c146-361b-8c1a-74555fafb549 | -5.78668 | -46.10857 | 2026-08-23 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e96915be-c516-3b61-9c4b-e0227ad06fb3 | -6.85514 | -59.41571 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b939d7db-b7cf-3691-afb9-58b630989f72 | -5.61073 | -51.7864 | 2026-08-23 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9377f74-c60a-313b-8fe4-7f07d8e99477 | -6.90166 | -55.7 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b76901ba-43f1-3c01-a4d7-4e103f23eb41 | -5.1663 | -45.05782 | 2026-08-23 04:44:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbc71f83-9c14-3f2b-837e-1dd695f1d4ae | -6.69826 | -58.73356 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 88ee4c30-5c9d-3e6d-8228-df105d82671b | -6.19422 | -55.43227 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c10f42e3-7a2c-36ad-b9eb-200156f5dd60 | -6.68487 | -58.74012 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 6e1ba09b-5e3b-312e-acaf-5f5186df3e95 | -7.4879 | -55.33255 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c38fb595-528f-3495-8432-ae90c278c1b6 | -2.56334 | -47.24588 | 2026-08-23 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 228ed65d-96d7-3e13-81c7-c981a7ea2071 | -6.79661 | -59.60305 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ff2f4c3e-1e12-31ff-b799-1c287399eef5 | -7.03585 | -55.49883 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5dabdea-8e0c-3930-b903-0455f5ef368c | -6.97218 | -59.05677 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0894dc57-f6a4-352f-aa55-c22b991c9a13 | -6.79792 | -58.6519 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f49d80b8-319c-3091-85d2-c7209238dea4 | -6.70056 | -58.72103 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c597e236-b0a3-3b26-8c6f-cedc38d866fb | -2.91413 | -48.87316 | 2026-08-23 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e4622bb7-d72d-3948-836f-e702c0abc511 | -6.79648 | -42.66831 | 2026-08-23 04:44:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c10084ea-4f9e-32be-8fb9-54987d68ce65 | -4.17096 | -42.44115 | 2026-08-23 04:44:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2ae3196a-11ae-33e5-b8ca-85eda5b26990 | -8.47979 | -46.99275 | 2026-08-23 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b03da55-ae5e-3124-b8e1-49a08800aaca | -6.70495 | -58.73027 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| edc846f8-ffef-3e9c-bd20-d4061b17019f | -6.79245 | -59.41771 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70b02c5b-c24c-3fe2-aba6-c10e19078095 | -8.17423 | -44.44394 | 2026-08-23 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4a66a8f-935c-39b9-b2ab-4cb115498b01 | -2.56666 | -47.2464 | 2026-08-23 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9426988-d00b-303f-a317-da660ee6dd62 | -6.13834 | -59.9171 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a31905d-69af-3856-986f-1ad514bc25f8 | -6.67668 | -58.75146 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 010e77a5-64c3-3978-b71f-f224e4ee8fb8 | -6.76058 | -58.65786 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93c73418-166c-39f3-9e26-d8f031ba3177 | -6.79716 | -58.6562 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2180c0fd-5ad5-3756-aefc-c735bf57dc75 | -6.54769 | -58.51665 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29c906db-a5f4-32da-bc57-adaa6d19bc46 | -5.95968 | -53.62257 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f44b288b-96d9-3c03-8ddb-f567bd733969 | -6.55121 | -58.53049 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 759c9341-f0d9-317e-aa50-394a0e87687c | -5.60995 | -51.79101 | 2026-08-23 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a3d32b6-acb5-3463-b8f4-b24f6a670ece | -7.0697 | -59.978 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cfbd140-eb30-34fe-aab9-abd50a255a26 | -8.1599 | -46.7126 | 2026-08-23 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ee69b12b-2395-3a51-874b-ae2691cb022c | -6.77526 | -59.44646 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe5c90c0-4b1d-3a7e-b838-8c75ed75c1e5 | -2.9873 | -48.96316 | 2026-08-23 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afb8ed2f-9c57-3579-b423-faaf1c22b368 | -6.94597 | -41.75026 | 2026-08-23 04:44:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0c583e72-1eea-31db-a8f6-d51f9a6fa77f | -6.18769 | -53.52934 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb585723-87c9-3121-8365-582629e6493b | -6.95691 | -59.07239 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2b83a052-5302-3358-8952-780fae17ec53 | -6.94977 | -59.06963 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00833914-a27c-3ed2-9f13-a96836e4feff | -6.79841 | -59.59322 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 962e48f5-e66c-3e44-8335-e282f2ed63ec | -7.58289 | -57.69598 | 2026-08-23 04:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8320b8db-8f51-3a41-8a0b-130f66fb0b93 | -7.68755 | -50.75197 | 2026-08-23 04:44:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b011228-e661-3ecf-9b7f-5416e25ce4eb | -6.51395 | -51.44233 | 2026-08-23 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cec0d423-254f-31dc-9761-69bb475cfc8f | -7.15382 | -42.79119 | 2026-08-23 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a485cb67-8dbf-3e8e-8993-56e658ecfdf4 | -7.4853 | -55.32985 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 013f5028-d88b-3006-ba0f-0518a382ece7 | -5.65157 | -47.08623 | 2026-08-23 04:44:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78248464-666e-3503-974e-201b408b9e78 | -6.94327 | -59.0791 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c868229-cdd0-3b7f-bf22-243a34162e48 | -6.81616 | -59.67227 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a59ab629-ba81-3b9d-b027-124b8afa74b7 | -6.93726 | -59.07805 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37bd98d2-edba-3df6-b611-465328a22f1b | -6.18041 | -53.52113 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20630e4d-7bc4-3050-9965-19f910c74b41 | -6.76115 | -58.68831 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b490c29-cea1-3f5e-80ab-7b61cd78ca65 | -6.19035 | -53.51396 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1bf0af5-4a05-3573-8879-83962b16bc18 | -6.94736 | -59.08319 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d1b7eadb-80c9-3c52-8e75-ed776c8543f6 | -6.65801 | -58.80086 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2dc9d4f9-b9ab-3ac3-9d23-038929ccf54d | -8.01892 | -50.00544 | 2026-08-23 04:44:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ef5121b6-81bd-3e70-a773-29fcb5995975 | -6.78063 | -59.65514 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73315323-0977-39ec-960b-dd7236adbfb1 | -6.66723 | -58.7367 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 5cc2688d-c0f8-3b6e-9482-7dd66def313e | -1.6114 | -54.39968 | 2026-08-23 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 290acc87-ecb0-3f81-a7ef-c7fc6f123fb1 | -3.42807 | -48.93821 | 2026-08-23 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dd5b5b1-747e-3229-953b-4d617c9aeb51 | -1.41643 | -55.72451 | 2026-08-23 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 703a02b5-fffe-35ac-a103-390b93fb38b5 | -6.85603 | -59.41101 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d0dfd29-a657-3e62-b7ee-b1617322778b | -6.19375 | -55.43592 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63b4eb91-ec9e-385d-afa4-041848123cf3 | -6.82735 | -59.66534 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c2eba336-3082-3e7c-81a4-13323fdd82ce | -6.1847 | -55.43051 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c7378872-5f04-3fe8-bbf1-2a6ac01b2920 | -7.48455 | -46.09623 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 667dd9f5-7ce2-3d82-8f1f-3babf1246e36 | -6.37361 | -54.95073 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d70a4c18-f1de-39da-840e-8b8a7fd45db6 | -6.1846 | -53.52184 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d8685a4-f8ea-3391-9573-f7aa687595a6 | -6.95524 | -59.08141 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| edd2ae3d-7940-3f43-8000-6296b8815b2a | -6.66878 | -58.72833 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6bd12e52-3326-387b-9764-288258a2a9a9 | -6.82239 | -59.67345 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d3f922a1-d449-39c7-aa50-edbc7e919cc5 | -5.53376 | -46.60993 | 2026-08-23 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99d5554d-fa29-3df7-a00b-8c27084307bf | -6.75094 | -58.67775 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc521082-dec7-3807-a9e1-7d8898b7e105 | -7.26631 | -49.90381 | 2026-08-23 04:44:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 42ca5811-36d5-347b-967d-2e7efe5610d4 | -6.37441 | -54.94594 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 351e283d-3df1-3851-99d9-85aa24ebe1be | -3.0574 | -50.34154 | 2026-08-23 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49f9e24e-1287-3681-94c6-b6e35bc73d3f | -7.54938 | -55.5632 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90b0ab43-6edc-37b3-a12c-d14cc9c9307a | -4.31461 | -46.4172 | 2026-08-23 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfc06f16-68eb-37f6-82f6-571cdd5a25ca | -6.70418 | -58.73446 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 09b77e27-0591-3ed4-95f4-f75f5f71889d | -6.18984 | -44.85942 | 2026-08-23 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f7e124b-e8bd-304e-b5ca-1faf9b38320f | -6.85972 | -56.8662 | 2026-08-23 04:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31bfbe79-39a7-3e99-8cef-82c0b9302d96 | -8.08214 | -47.26303 | 2026-08-23 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f46f2c95-3d02-3715-aa6e-323b916d4fdf | -6.80583 | -58.66385 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 64274b21-c9bc-37a4-86d0-66fc9a1c764b | -3.85633 | -42.94272 | 2026-08-23 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3497838e-7244-3f32-a7a4-88d684f41009 | -6.79306 | -59.6576 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb64067a-8166-3bec-8c0e-6b127ede1df5 | -6.79946 | -58.64323 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac61e078-2d75-3daf-8956-9127749f80bb | -8.0855 | -47.26355 | 2026-08-23 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 23874ec9-a7a1-3b6b-a741-b82965931732 | -7.99034 | -45.23755 | 2026-08-23 04:44:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8c52b75-afa4-3b6d-b588-b6f9611b9f02 | -3.156 | -48.73639 | 2026-08-23 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe98da4d-d7ef-33ff-bb8a-08c0890a686c | -7.5503 | -55.55811 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5add3e9-3cbb-3680-b5b4-576fb2f0c8a2 | -6.18751 | -53.53033 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e06c1c82-e020-39e2-a4a4-133bc28f91eb | -6.64942 | -58.79964 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78d86076-814c-3342-928a-e72880929439 | -6.67311 | -58.73785 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 7ca31e6d-3ea8-33dc-b01d-fb7313eedbc1 | -6.67757 | -58.72519 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff68fb5c-aea9-3fa0-9d50-555cd8535ff6 | -6.70645 | -58.7221 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bd6dd253-1a4e-3843-a81e-a1c58a19d215 | -7.18877 | -42.75442 | 2026-08-23 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cc6761b9-7191-3af7-9ade-d4b20eb81226 | -5.1688 | -45.06097 | 2026-08-23 04:44:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README28.md)
