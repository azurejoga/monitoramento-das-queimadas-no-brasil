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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e244035-5c68-3e1d-8ad4-337d824bfc00 | -9.33537 | -46.57882 | 2025-11-17 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cadb9af9-fa5c-36e5-8850-2a8d5f33aed1 | -10.66249 | -49.375 | 2025-11-17 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 368ea539-e023-3644-ad0f-ba4c317821ff | -3.52191 | -51.23639 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99584558-744f-3fc9-a8f1-c1697a7966c4 | -3.0895 | -51.54359 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de360540-eae6-3c9f-8ebc-492410a09482 | -9.8055 | -48.56029 | 2025-11-17 05:08:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71b5bd78-7faf-31ad-acf7-6b942316f8a8 | -4.64972 | -46.89825 | 2025-11-17 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfb89b90-54b5-3aff-a6fa-aba90250b560 | -3.45846 | -50.11683 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7e3f1ba-6874-3733-abd6-04a6260edaf5 | -3.74522 | -51.38937 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aee1c610-134e-35de-ae3d-aedaf38063fc | -4.6611 | -46.74091 | 2025-11-17 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 55807ba1-2bca-3d36-8a6f-348915b17d18 | -3.24059 | -50.49923 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 536f7e85-de60-329c-ae2f-ba537e070544 | -2.89442 | -53.28757 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c3289ab-11af-38d5-a54b-be2b7defb9d6 | -7.03632 | -47.61965 | 2025-11-17 05:08:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2473eb0e-9bf1-35ea-9ee8-6364719197db | -9.71472 | -43.95845 | 2025-11-17 05:08:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 81c6455e-97c3-366d-b6f0-3f26651b4384 | -10.65182 | -48.16749 | 2025-11-17 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e210a6e8-6936-3559-b5ea-ca6bdd3bfffc | -2.80216 | -52.96386 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c2f7b1d-5066-380b-8f8f-e2d4ae1fb31c | -3.95427 | -50.90016 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbea652b-3278-38b1-886b-c9a7022bda41 | -9.33024 | -46.57438 | 2025-11-17 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 23d10b6f-f8fc-3ac3-af35-75618f08197f | -9.35282 | -46.59867 | 2025-11-17 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c2ac90d-b613-3657-97b7-a95477e90f7f | -3.51272 | -53.03563 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3cff0c51-797d-3932-b58b-a6ec8746e5ce | -3.58251 | -50.71591 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43e5d271-d971-3a81-b8be-97b3f964e77e | -4.65645 | -46.74025 | 2025-11-17 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dfdcd6b8-73e6-3e01-9876-33ae754e61fd | -3.23272 | -50.4981 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 5230c9f4-ffbb-3c7d-af4f-15131f2d8290 | -6.35998 | -46.14781 | 2025-11-17 05:08:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f51e6f18-63b8-3a5f-ab25-94faeb319953 | -4.40233 | -45.8389 | 2025-11-17 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 895856c7-f6e3-31f8-a8cb-37fdc35214cc | -11.13531 | -44.93867 | 2025-11-17 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb492063-a2a6-39c4-8452-8a750cafebca | -4.99651 | -44.3536 | 2025-11-17 05:08:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 164d5aa3-bb64-3397-af17-1dff2e658b73 | -2.99217 | -54.91629 | 2025-11-17 05:08:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4464d80e-7483-3962-abf6-21e6b7aa4e0e | -4.73433 | -46.38211 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13ab6692-b7a7-357e-b222-225ba28df826 | -3.23694 | -50.4902 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a739b6bb-6696-37e1-b7cf-f12a937c0f95 | -3.51246 | -49.92772 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8605832-b09d-38fc-9549-05e28603b222 | -5.40471 | -44.06597 | 2025-11-17 05:08:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb52cb62-870d-33b4-a632-7dc83fbfda3e | -3.83595 | -51.19864 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47a1f9c7-9285-3eab-adb3-01267b3b5c71 | -6.44225 | -43.81672 | 2025-11-17 05:08:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4045d2b0-a951-3e38-9579-d07e39390815 | -4.91722 | -47.41376 | 2025-11-17 05:08:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 98c7d6d1-21a4-3080-ac3c-d4aa9cf8e28e | -3.24373 | -50.50485 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 144add33-ae86-376a-87da-be7d66d86edf | -6.00072 | -51.51525 | 2025-11-17 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 189fb7c0-e65a-3853-a222-2796ea3e53a7 | -6.71151 | -42.93565 | 2025-11-17 05:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 65d01a1b-8583-3681-9cb0-28a7b00d4302 | -5.12681 | -55.97202 | 2025-11-17 05:08:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7920afba-2630-3643-bab1-50bb89a34ac9 | -4.14021 | -52.10209 | 2025-11-17 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b962dd67-956a-37e0-8226-fec7ddb14b41 | -3.23 | -50.50971 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d4f41caa-8594-33be-a12d-6a7600c89c88 | -9.58503 | -49.11388 | 2025-11-17 05:08:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a897636b-fc70-3743-8620-381253296d0b | -3.46654 | -50.11805 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fbb7aa5-d71f-303d-b48e-0c87846d2718 | -4.09941 | -47.11525 | 2025-11-17 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 35bb11dc-cd00-30ac-8aac-fd8cd69d4355 | -3.74922 | -51.81064 | 2025-11-17 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a5ec190-5368-3a5c-afb2-8789984982c0 | -3.17307 | -50.64988 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06cb444b-78c8-346c-a23e-bef77f1d396d | -3.23075 | -50.50472 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fed93d7a-81a4-3005-a2a0-ea68b4a9a483 | -11.16104 | -44.03628 | 2025-11-17 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 48c23243-7725-3833-b458-24ec2a4572f3 | -3.78976 | -51.19586 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 20846276-e770-3c59-8323-70643083fd94 | -4.69793 | -46.31265 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 763d64d4-6b26-32ce-b7e4-5e8e249e993b | -4.46063 | -49.7875 | 2025-11-17 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a52ec28b-0036-393d-a129-1c34aff7eda7 | -2.78834 | -54.02464 | 2025-11-17 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b23f1da2-9906-3b81-86b1-993bcf64d0c4 | -7.43289 | -48.93731 | 2025-11-17 05:08:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b7b88cfd-4fb5-394d-85f7-e7e48790c8e5 | -3.10846 | -53.12442 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0ba76ea-8a14-3eea-bbee-c70ad93e5413 | -4.02 | -48.81065 | 2025-11-17 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3fd54854-d45e-3005-8f1d-37f4b0d6df44 | -4.55229 | -48.47797 | 2025-11-17 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 690b90fa-aae9-31ff-b018-8d2dd5f02514 | -3.321 | -50.20224 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f324d392-3940-3a5c-a461-747e08851045 | -7.70455 | -49.38585 | 2025-11-17 05:08:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a5d7da2-a8b1-3557-ba6d-e39c1b234540 | -3.77335 | -47.64732 | 2025-11-17 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63768f09-c3e2-3bc2-bf08-c1f2826921f9 | -3.74457 | -51.39175 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c045006-9d17-3335-b5e7-fb1351d05ae4 | -4.68814 | -46.30494 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cd56416-1653-3c22-9cea-ec162890d34c | -5.00192 | -44.35929 | 2025-11-17 05:08:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d61956ce-0ffd-3d0c-af9d-9906dba75527 | -3.52121 | -51.24093 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebaaab5d-fc7e-39fd-a419-0d47a2a068ef | -5.36231 | -44.86206 | 2025-11-17 05:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1174f34f-e8c9-3355-8605-3caf855cc09e | -3.34611 | -50.19913 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 428d6f3a-0573-3b11-ae6c-f2638069529a | -3.13418 | -50.25417 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 210208dc-3cd7-3875-af93-d6f090d4749e | -3.87897 | -46.46442 | 2025-11-17 05:08:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 027c8122-9a1e-33cc-96f7-c0c01274f3ba | -10.13353 | -49.15126 | 2025-11-17 05:08:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9677b4e9-c413-3e23-b48f-bda775e509a4 | -3.44789 | -51.4182 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 003dc091-f333-37e8-b0ce-7f70f9fd8449 | -3.35683 | -50.18286 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6711d134-59f6-35f7-a7a4-6fdfbf952057 | -11.20533 | -46.61331 | 2025-11-17 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42f52337-17cc-3d8f-a331-a6014fca55c7 | -5.13013 | -55.97255 | 2025-11-17 05:08:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30fa8234-1183-3d1f-a7a9-edfd24dcce02 | -3.90858 | -45.80222 | 2025-11-17 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8221d0eb-d259-3b12-9f8f-2347704eaaee | -4.68766 | -46.30819 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a373fa9-392c-3553-acf0-df53b2d25888 | -3.30773 | -50.07158 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20625709-9862-330f-807b-073fda5aa1ea | -3.23586 | -50.5037 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f50525bb-c0f5-3660-9cd9-df56d5878f79 | -8.87036 | -50.19243 | 2025-11-17 05:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1659bb30-9c09-306e-8f78-cc43da40a44a | -3.60568 | -51.99319 | 2025-11-17 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 094a6a5f-3f41-306a-95b8-d4f9a82b51d5 | -3.79873 | -51.09579 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50363f3d-cadb-354b-be5f-7fdc36621934 | -3.4523 | -50.80807 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84ef4f5a-deac-384c-8157-52eba7ca0b2a | -6.68705 | -42.04938 | 2025-11-17 05:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 480959a1-7742-3da7-9727-d2e0cef0fd82 | -9.74739 | -43.96764 | 2025-11-17 05:08:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad378310-4cc5-31e1-8678-2b3f1bb5ba7c | -11.16037 | -44.04222 | 2025-11-17 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bf127316-51d5-3959-9784-bb54c592df5f | -8.50631 | -49.41796 | 2025-11-17 05:08:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03f0467c-8137-3524-8a46-f3f24713ca08 | -3.30889 | -53.85271 | 2025-11-17 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89a801d3-17f0-38ac-aee8-118cca7534c0 | -4.06348 | -47.49641 | 2025-11-17 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19fab98b-0531-3357-8839-e3e05bf6f990 | -4.06269 | -47.50173 | 2025-11-17 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6af2d2bf-66e3-3a8f-82c3-ddb5a98cb9b0 | -7.26505 | -48.02053 | 2025-11-17 05:08:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e54ad861-e077-38b6-947b-63368afe9534 | -8.86662 | -50.18758 | 2025-11-17 05:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6d68c38-5e8c-3e55-ab0c-23cefc5ddbea | -4.40683 | -49.33978 | 2025-11-17 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| afba2e11-a91e-3253-a234-35da71cca525 | -8.54293 | -46.06227 | 2025-11-17 05:08:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 987fce24-6330-335b-8ba0-f3b8b746c8d2 | -3.22957 | -50.49249 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e4aa08a-5ff2-399d-b279-41a4a329f99e | -3.39404 | -50.18158 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b190ef23-223d-35c2-9483-d529f491ca83 | -4.74016 | -46.37937 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4d86727-2540-3977-93da-f056939a0d8c | -7.12684 | -47.1231 | 2025-11-17 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3556ba54-7ed2-3672-83c8-106a7b43b652 | -11.1543 | -44.03541 | 2025-11-17 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d682faca-d56d-375a-aea9-fcb0572b7123 | -3.22831 | -50.49411 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e9a49755-8aab-3cfa-b6d3-1ec2efe81cc8 | -9.68586 | -56.09798 | 2025-11-17 05:08:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10f389e8-72b3-3a8d-9bd5-b59c655388bd | -3.39459 | -50.17811 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8efc31eb-4900-38df-87d6-b602e3cd7d31 | -3.33283 | -49.90359 | 2025-11-17 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6c13846-8f08-3963-83d6-17a3fa273886 | -2.8876 | -53.28651 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README42.md)
