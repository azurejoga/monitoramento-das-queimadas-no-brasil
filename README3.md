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
| 2db9adfe-e9f0-33db-af4d-c071307e43f2 | -5.6941 | -45.8771 | 2026-09-26 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 968deb91-7e57-398b-8e0b-71751916ca5c | -5.6756 | -45.856 | 2026-09-26 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| e19ac3a9-1f70-3c09-83ae-56e7a25b270b | -3.2728 | -50.1372 | 2026-09-26 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 40e6ce27-3637-3cda-92bb-b23045a39d3f | -3.2727 | -50.1583 | 2026-09-26 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| fca43c65-1547-39ef-9a25-db43756f7c39 | -3.2728 | -50.1372 | 2026-09-26 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 30c37d1d-3f71-39b7-83d4-c701da5f154b | -5.7357 | -43.2682 | 2026-09-26 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 05e884cd-0484-31bb-867c-3e1e0ead0f6d | -7.3656 | -42.0819 | 2026-09-26 00:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| f2c20aeb-8839-3333-9928-0755280ce465 | -7.3467 | -42.0839 | 2026-09-26 00:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| dbfde635-ad1e-3c5f-b546-deb1d8b1e356 | -5.7754 | -45.1053 | 2026-09-26 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 63992ba3-1008-3ab2-8748-97e3eb566511 | -11.9365 | -38.2942 | 2026-09-26 00:40:00 | GOES-19 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 73.4 |
| b66b36b7-6ab0-3242-b157-3c0f3a2bffad | -5.7384 | -45.0626 | 2026-09-26 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| cbff1275-c402-348e-9969-db97a7f75381 | -12.9065 | -49.956 | 2026-09-26 00:40:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 178.3 |
| add0f34d-bd78-3d9b-9f30-bae277198785 | -5.7756 | -45.0826 | 2026-09-26 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 5cdf5e6a-488c-30b5-8584-3e84e1151a43 | -7.4132 | -39.7823 | 2026-09-26 00:40:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 71.1 |
| d140682c-f345-3848-bcc3-2f681f5f3f53 | -12.9061 | -49.9777 | 2026-09-26 00:40:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| a37ca1a0-c47d-32b5-a081-474fb0ec2a23 | -16.5732 | -43.9798 | 2026-09-26 00:40:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 520fd9c6-278f-329f-ad80-f47f7c06524b | -12.8873 | -49.9585 | 2026-09-26 00:40:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| face486a-10db-35e4-8085-cc1e5612f405 | -5.6756 | -45.856 | 2026-09-26 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 45ab2178-ddb7-3531-8a2a-55bcb4988afe | -5.7756 | -45.0826 | 2026-09-26 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 01a4fe89-42d9-3c0a-bd40-0ec449df1b24 | -5.6754 | -45.8784 | 2026-09-26 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 918c19bd-aacf-3143-a2ea-99c1bfbf3bd8 | -11.9365 | -38.2942 | 2026-09-26 00:50:00 | GOES-19 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 78.8 |
| 01cb2953-9627-3ed8-9d71-23052ae4ca7c | -1.3459 | -55.4721 | 2026-09-26 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| f63c3a34-6843-36c1-ac4c-65be923e61f2 | -5.7357 | -43.2682 | 2026-09-26 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 4b2a461a-de1e-368a-ba85-53a9e13d28a7 | -5.7571 | -45.0613 | 2026-09-26 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 4bd8f3c5-8999-3170-83f1-2d21de36b490 | -5.7382 | -45.0853 | 2026-09-26 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 6726d0e1-23f3-30f6-8c33-ab46209cd136 | -5.7384 | -45.0626 | 2026-09-26 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| c048e23c-615a-3ba1-938b-5b2594d080b1 | -3.2728 | -50.1372 | 2026-09-26 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 308318f1-1766-3b7b-975f-40e9f750e17b | -5.7569 | -45.084 | 2026-09-26 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 38168559-1993-390c-bde4-8fa85fcb9175 | -7.3656 | -42.0819 | 2026-09-26 00:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 7ffbd459-dd01-3ad0-9e5c-da0f04172b95 | -14.7986 | -45.957 | 2026-09-26 00:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 85d63751-6e5a-3eaf-ac31-cbb8d3cf8f9a | -5.6943 | -45.8547 | 2026-09-26 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| e6e79938-b7ff-3ea7-9d53-c15f0e819bab | -5.6941 | -45.8771 | 2026-09-26 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 84021afc-922b-35eb-931e-eb059ecaf7ea | -3.2728 | -50.1372 | 2026-09-26 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| c152dcb6-4721-33da-8523-c3570e0489b9 | -5.6756 | -45.856 | 2026-09-26 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| d8bf3cac-a1f9-3796-b631-e2a36cc6732d | -5.7756 | -45.0826 | 2026-09-26 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| c88e605f-fa4c-3faf-bad7-82527c7dc0f1 | -5.7754 | -45.1053 | 2026-09-26 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 4cfa23a5-9189-3cf6-86ff-da7b87dd2b4b | -5.6754 | -45.8784 | 2026-09-26 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 01b5bf3e-fc9b-38f2-a35d-d5f94f52156e | -5.7384 | -45.0626 | 2026-09-26 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| a203cb83-5e40-3809-b7f5-bfe33ea965b5 | -5.7357 | -43.2682 | 2026-09-26 01:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 32bd1b28-be79-3825-b9a7-875b431cdde6 | -7.4132 | -39.7823 | 2026-09-26 01:00:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 468b5f11-be11-394e-937d-9dfec21565de | -11.8659 | -50.5791 | 2026-09-26 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| b06a71d4-df6c-36f7-a044-3ae8f3668e67 | -5.7382 | -45.0853 | 2026-09-26 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 27ec8f48-de14-3cd6-bf6d-fbd9e53c07d0 | -5.7941 | -45.104 | 2026-09-26 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| f7388869-079c-3f00-a5fc-f6f110c6a3c7 | -11.8662 | -50.5576 | 2026-09-26 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| cb167d5e-5cb5-3adf-9736-1ecc83cd7c41 | -16.5732 | -43.9798 | 2026-09-26 01:10:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 88.7 |
| b2e3531b-6ade-32c2-bb67-70ac60938708 | 3.6938 | -60.8681 | 2026-09-26 01:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 3f62014a-82b1-3fb3-ba77-3888469a9e05 | -5.6943 | -45.8547 | 2026-09-26 01:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 289a7344-5c84-301f-8eaa-7ed28718e7ca | -5.7756 | -45.0826 | 2026-09-26 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 70b5a2f5-0d47-36d1-a16e-e09bc2afcfb8 | -5.7382 | -45.0853 | 2026-09-26 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 2f744b85-d885-3ff0-b547-45a70ac1a0ea | -5.7754 | -45.1053 | 2026-09-26 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6d18ddb6-0922-31ca-a0c5-ece7069692dd | -5.6941 | -45.8771 | 2026-09-26 01:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 2fa900ab-9375-3885-8ac8-b1c7eb556312 | -12.2636 | -50.7248 | 2026-09-26 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| f90035e7-218f-3afd-945b-93f12f1f5354 | -5.6756 | -45.856 | 2026-09-26 01:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 34ec4a14-5cc6-3cbf-b1f2-e05da3487f4d | -5.7571 | -45.0613 | 2026-09-26 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 7389a593-c4b8-3bac-b1f8-d9112f20be1c | -5.7569 | -45.084 | 2026-09-26 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 12ba9402-08e2-3d3d-be42-9ecde2e5630d | -3.2727 | -50.1583 | 2026-09-26 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 3efb2dca-655e-3626-bee8-7164e73033bb | -6.0451 | -35.2493 | 2026-09-26 01:10:00 | GOES-19 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 68.1 |
| a6eb45a2-63a7-31e4-ac53-ec5205592709 | -5.6754 | -45.8784 | 2026-09-26 01:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| de0ac572-7d6d-3b65-a432-f6b2323f055c | -3.2728 | -50.1372 | 2026-09-26 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 7e0313fb-e0de-3604-bd24-95e79226777f | -5.7384 | -45.0626 | 2026-09-26 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 1915f0d1-6ee7-3541-a61c-d45669285556 | -9.7268 | -61.895599 | 2026-09-26 01:14:00 | METOP-B | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3952bdf5-b85f-321b-914e-0c1328d87420 | -29.1264 | -55.623001 | 2026-09-26 01:14:00 | METOP-B | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 300ea0a7-ff17-3dd6-a46d-11831a3160d8 | -11.868 | -65.020401 | 2026-09-26 01:14:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2673e38d-b65d-36c7-80fa-6df20a849ab8 | -7.3975 | -72.483902 | 2026-09-26 01:14:00 | METOP-B | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9deb838-f033-3735-84f2-a1438f3e95c6 | -11.8695 | -65.027397 | 2026-09-26 01:14:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 26f121c1-c715-3cf1-b755-16838c77011b | -12.898 | -61.721699 | 2026-09-26 01:14:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bc09c90e-bef8-357d-92b6-2af22b06382f | -12.8961 | -61.713402 | 2026-09-26 01:14:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 11352bc2-4f95-3717-927d-30659b2369e9 | -10.1273 | -69.011497 | 2026-09-26 01:14:00 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 2f50d648-d7fa-3500-9f2c-7c61f88f309e | 3.7043 | -60.870602 | 2026-09-26 01:14:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 170ee111-8d23-347f-88fc-321d30fc8fdb | 3.7078 | -60.8549 | 2026-09-26 01:14:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 05f46aa3-1cd2-3bc6-a311-b8cf583c7e24 | -12.2445 | -50.7271 | 2026-09-26 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| c757be7f-748b-3332-975c-7d123ac83380 | -12.2636 | -50.7248 | 2026-09-26 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 3737d49f-63a9-38e4-9107-e310f7bc4c82 | -3.2728 | -50.1372 | 2026-09-26 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 4815d64c-06fe-3a03-93b4-d5de56143f3a | -12.2827 | -50.7226 | 2026-09-26 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| bff85cb9-503d-36f1-9992-2b30e30b30b2 | -5.6754 | -45.8784 | 2026-09-26 01:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| f4237064-2274-363e-8f63-81b036cfeff1 | -5.6756 | -45.856 | 2026-09-26 01:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| d10bc18b-5bd4-3ddb-aa4f-909b8ef7f421 | -3.2727 | -50.1583 | 2026-09-26 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| ca13a3d7-3ac5-3401-8524-d6b0a4f55b3b | -5.7384 | -45.0626 | 2026-09-26 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 0f6d8708-e187-3992-a06d-28b374de9a3e | -12.2448 | -50.7057 | 2026-09-26 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| b8b79d58-2efc-3e62-9a7c-0d5377098ad8 | -12.2445 | -50.7271 | 2026-09-26 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 93ce0650-abe3-34d6-9eff-074629da2e35 | -11.8094 | -50.5428 | 2026-09-26 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| c6ad381a-db63-3316-8b0b-3b301104ecc7 | -12.2696 | -50.3381 | 2026-09-26 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| f3435364-6a15-3cd8-895b-844ac96a1516 | -12.2639 | -50.7034 | 2026-09-26 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 368df6f9-cc46-3d6d-a8d1-60f2cd0d94f7 | -12.2699 | -50.3166 | 2026-09-26 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| ee7f147c-a6bd-3294-82e7-1c3f28dfc2eb | -12.0362 | -50.6448 | 2026-09-26 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 6bba807b-bea1-3992-bc0f-865e96660ca2 | -11.8284 | -50.5406 | 2026-09-26 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 30b30b70-d8a0-3721-a4f3-fe56b05ce92a | -5.7754 | -45.1053 | 2026-09-26 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 802d60e5-c2de-31fd-9394-e0d5fa64eae8 | -12.2887 | -50.3358 | 2026-09-26 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 9ea150ee-4f41-356c-8759-3efd9dc1ca22 | -12.2636 | -50.7248 | 2026-09-26 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| db10cadc-d83a-3a66-b282-79e265f2a9b7 | -12.2508 | -50.3189 | 2026-09-26 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 3587818d-5a12-3270-b562-c02708806603 | -5.7571 | -45.0613 | 2026-09-26 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| c1169cd2-7fea-3fcc-b3c8-5872608a5b92 | -3.2728 | -50.1372 | 2026-09-26 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 1c4097fe-d35d-3a83-bd89-4a11dea1e4c0 | -5.7756 | -45.0826 | 2026-09-26 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 1433d472-f8ed-36d6-b58c-8c4d1cd6f0cb | -11.8702 | -65.034302 | 2026-09-26 01:36:00 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c5bd7713-6818-37e0-af0d-dd3e34fc7cc8 | -12.2429 | -50.332901 | 2026-09-26 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| efffe715-7716-3426-9420-988e0bf7cf95 | -12.2699 | -50.3559 | 2026-09-26 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a285214a-463c-3965-baf9-347927983750 | -12.9063 | -61.721298 | 2026-09-26 01:36:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fb466f53-eb38-384d-a8b8-1a7080c986ba | -12.2445 | -50.301498 | 2026-09-26 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ae22925-4d84-36da-a872-56fba6af264b | -12.8965 | -61.723598 | 2026-09-26 01:36:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bc62b684-03ba-3e81-8c0b-81fcd0a25009 | -11.8362 | -50.540298 | 2026-09-26 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
