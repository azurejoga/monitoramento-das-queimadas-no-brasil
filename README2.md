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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9366b588-eba9-3935-9e76-3c5728136d05 | -12.6766 | -51.1665 | 2025-10-11 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e86acc20-228a-39b9-a156-b5f6c70912e6 | -9.1615 | -68.1828 | 2025-10-11 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 8d09bb67-adc6-3437-b769-73cd5af2973d | -13.2252 | -42.3414 | 2025-10-11 00:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 574.9 |
| 5726198c-c367-32a1-b454-f79635d3d776 | -17.4843 | -43.3358 | 2025-10-11 00:30:00 | GOES-19 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 91.6 |
| c66c39a7-d842-325f-8a71-20f18835d136 | -10.1918 | -36.7236 | 2025-10-11 00:30:00 | GOES-19 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 129.5 |
| 570ca893-0e93-3b24-89eb-f5fb8cc90ed7 | -11.7589 | -43.3136 | 2025-10-11 00:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| e648dab9-6c82-3b58-88e5-ce3ffefb5c41 | -7.8642 | -44.4922 | 2025-10-11 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.7 |
| b546313b-9638-3aa3-ac01-b22807e62513 | -13.2667 | -48.0186 | 2025-10-11 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 0e31203c-cdfc-3cef-aadf-042bef592e11 | -4.4241 | -43.4735 | 2025-10-11 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 7384a68d-66ce-3722-80f0-585d51fed2f6 | -7.8645 | -44.4692 | 2025-10-11 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 147.3 |
| a91b7bce-fc71-3d9d-bd57-3ee01861e566 | -7.4616 | -46.8542 | 2025-10-11 00:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 72637c1a-0522-304b-ab40-082c2adb5899 | -13.2062 | -42.3206 | 2025-10-11 00:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 107.8 |
| 542b47a0-d611-30eb-a4ac-b3cba9b2881c | -7.8454 | -44.4941 | 2025-10-11 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 45879e33-3874-31a0-8e1f-229d9e3ee4e7 | -13.2246 | -42.3657 | 2025-10-11 00:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 91.4 |
| c35072bd-3c8c-3971-8494-bd68ad822ead | -17.2722 | -46.8932 | 2025-10-11 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 16ed79d4-08ff-39cd-8f56-4f1e0dbf3b65 | -13.2062 | -42.3206 | 2025-10-11 00:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 112.2 |
| 4b32f868-3895-3850-9f43-5bdfb1033337 | -7.8642 | -44.4922 | 2025-10-11 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 610ce545-4cfc-3306-839a-ee8b6d5764e8 | -13.2246 | -42.3657 | 2025-10-11 00:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 107.2 |
| aa87026b-f90c-3547-99e2-46aea6cce3f2 | -12.6957 | -51.1641 | 2025-10-11 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 228.5 |
| af47e08d-914c-3d77-bef2-8301e249f4f5 | -12.6766 | -51.1665 | 2025-10-11 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 5aabaf12-3d1c-33a5-b0c6-87538455126e | -13.2057 | -42.345 | 2025-10-11 00:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 506.1 |
| 58edceda-f27c-37c8-be57-254dd508fccc | -11.7589 | -43.3136 | 2025-10-11 00:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 92587feb-e738-3361-a756-dc58e50e66d1 | -12.696 | -51.1428 | 2025-10-11 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 35707f6a-e0ee-349b-8c37-b8333246e120 | -13.2252 | -42.3414 | 2025-10-11 00:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 755.5 |
| 6f130d5e-fa32-3fdb-b820-cbf3a9fe573d | -4.434 | -47.6076 | 2025-10-11 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 86f65312-72c7-33d0-bc82-15393e7dd111 | -13.2052 | -42.3693 | 2025-10-11 00:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 110.3 |
| e5a47395-8274-31c6-aa96-687b06de6a6c | -13.2257 | -42.317 | 2025-10-11 00:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 175.8 |
| ef24f812-6ec6-3d23-8312-cda2e321a731 | -4.4054 | -43.4746 | 2025-10-11 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| c35745e3-e7b9-364e-933b-f9b34b8ca48d | -8.1996 | -43.3189 | 2025-10-11 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 7577b5c0-86ac-3e86-bb5e-a43b3abd478c | -12.6954 | -51.1855 | 2025-10-11 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| e17207a0-67be-32f4-a096-88a0d7c3ae1b | -9.18 | -68.1824 | 2025-10-11 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 2c5b3079-e521-3c75-8410-48ca305a1bfc | -17.4843 | -43.3358 | 2025-10-11 00:40:00 | GOES-19 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 4da23062-82de-3527-a6b0-5019c9410980 | -4.4241 | -43.4735 | 2025-10-11 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 182c895b-813f-34be-b502-fde9c1fbff7f | -7.8645 | -44.4692 | 2025-10-11 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| b4a847cf-27f5-387e-8f2d-5addcb352fb1 | -7.4616 | -46.8542 | 2025-10-11 00:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 4d105696-9158-3ece-8ecf-30f0999b6b36 | -7.4613 | -46.8764 | 2025-10-11 00:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 3cba1201-ef7a-3ecd-b12c-78a25e6b4f87 | -4.4342 | -47.5857 | 2025-10-11 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| ede0334f-b28a-39d3-886f-2ef740b79afb | -8.1996 | -43.3189 | 2025-10-11 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| b56690a0-737a-3070-9249-29e3d45ee9c5 | -12.6766 | -51.1665 | 2025-10-11 00:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| b6c6c128-991e-3c56-9dca-591c53a1f30a | -11.7589 | -43.3136 | 2025-10-11 00:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 63501bba-cbee-384a-9649-f649ab3b1805 | -8.5027 | -46.177 | 2025-10-11 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 63ed2ccd-fbe9-327f-ad19-4a8f6c564357 | -12.6957 | -51.1641 | 2025-10-11 00:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 99df072e-522e-359b-a519-59f66a1b8bac | -5.8522 | -42.8372 | 2025-10-11 00:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 33cdfcdb-a97c-3a8e-b9cb-77cde624464b | -8.4835 | -46.2014 | 2025-10-11 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| b0d24c81-d035-3627-ad16-d15c5e0a10aa | -13.2246 | -42.3657 | 2025-10-11 00:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 141.7 |
| 4d4f5f03-f67e-3813-92d7-e653f380930b | -4.4241 | -43.4735 | 2025-10-11 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| f9a167a2-2b34-3801-987c-94a2d0fb06fe | -8.5024 | -46.1995 | 2025-10-11 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 2fbd6052-aa2e-31b7-94d3-6b2e857e3615 | -5.8708 | -42.8593 | 2025-10-11 00:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| c0830e4d-6184-39ad-948d-88cd7a037454 | -4.4054 | -43.4746 | 2025-10-11 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 3bb79e29-aa69-3042-a3e3-9c1407c204c7 | -13.2252 | -42.3414 | 2025-10-11 00:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 676.1 |
| 594c2ebd-858c-35d4-97d6-a3b6b1122f6b | -17.2722 | -46.8932 | 2025-10-11 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 988994ec-207f-31eb-a2db-12e4c9a68579 | -8.1993 | -43.3424 | 2025-10-11 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 0487f445-3689-3b56-8f6f-5e4d2877b632 | -4.4342 | -47.5857 | 2025-10-11 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| f8f0ff7a-358c-3201-923c-e7def3485419 | -5.871 | -42.8357 | 2025-10-11 00:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 33.3 |
| aa07b226-4327-3fbc-a26b-8451d46f5705 | -13.2062 | -42.3206 | 2025-10-11 00:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 134.2 |
| 4a424520-8cf6-330b-b742-5b31d5e9d177 | -13.2052 | -42.3693 | 2025-10-11 00:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 86.0 |
| 1cd9a12e-c087-30af-8b1c-a6dee765f4c6 | -7.4616 | -46.8542 | 2025-10-11 00:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| b7a3b673-b045-3fc0-ad15-1259715f5e92 | -13.2257 | -42.317 | 2025-10-11 00:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 233.3 |
| a1506d06-44b1-311d-994b-1316ec9799b8 | -4.434 | -47.6076 | 2025-10-11 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 5d9628fe-10dc-3840-9bfc-1ab08b667005 | -13.2057 | -42.345 | 2025-10-11 00:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 448.9 |
| 3a206daf-7c3c-3078-ae4e-617f77a48c06 | -11.7589 | -43.3136 | 2025-10-11 01:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 21431d96-9829-3599-b888-f373d614bc61 | -5.871 | -42.8357 | 2025-10-11 01:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 35.5 |
| d2425835-bd0b-37ac-bc80-9030a199a755 | -13.2052 | -42.3693 | 2025-10-11 01:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 77.4 |
| 52c88a32-c168-3182-a7f8-ff39ec08cb88 | -13.2257 | -42.317 | 2025-10-11 01:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 156.2 |
| 145b7f69-ef12-389f-ad9b-bd4ba74b0cc7 | -7.8645 | -44.4692 | 2025-10-11 01:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| d4713c8a-58e2-3a74-bb78-5e1f097bf4f6 | -13.2062 | -42.3206 | 2025-10-11 01:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 143.8 |
| 653b76a7-c286-304e-89f1-30c154f2233c | -9.18 | -68.1824 | 2025-10-11 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 0d094867-e055-381d-9fee-6e1c8f96ba52 | -4.4241 | -43.4735 | 2025-10-11 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 4f4c22f0-ea12-30ed-a36f-9488ab9b31a7 | -12.6957 | -51.1641 | 2025-10-11 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| d4bb96fd-0f06-37f9-8483-852b5124384e | -5.8708 | -42.8593 | 2025-10-11 01:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 6521d35e-ebc8-335e-acef-a335a3dca0b9 | -13.2057 | -42.345 | 2025-10-11 01:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 473.8 |
| d36fea30-5176-3643-85b6-003236a4285d | -7.8642 | -44.4922 | 2025-10-11 01:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 11ecb04d-b146-352d-b7a8-207aef681100 | -13.2252 | -42.3414 | 2025-10-11 01:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 513.1 |
| 99d130e9-a159-30de-bc85-7a1660d503eb | -4.4054 | -43.4746 | 2025-10-11 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| cded9916-1750-3587-8343-52089566832d | -8.1996 | -43.3189 | 2025-10-11 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| e12e330d-015b-31bb-a682-19b231975b7a | -13.2246 | -42.3657 | 2025-10-11 01:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 27d1558e-b94e-3336-a5d1-47d17bf46c1c | -7.4616 | -46.8542 | 2025-10-11 01:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| cfdf143d-a2ca-3c78-ad35-888cab1a225a | -27.72466 | -51.22763 | 2025-10-11 01:07:00 | TERRA_M-M | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 989d6d80-2314-3cf4-b9c0-c53498b9e241 | -22.54658 | -52.05717 | 2025-10-11 01:09:00 | TERRA_M-M | JARDIM OLINDA | PARANÁ | Brasil | 4112603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| 1c18c55a-7132-389d-9365-843e33d8ed95 | -22.54449 | -52.04426 | 2025-10-11 01:09:00 | TERRA_M-M | JARDIM OLINDA | PARANÁ | Brasil | 4112603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| a171daad-9777-3ddd-8e51-d39afd76c31e | -18.03447 | -57.55157 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 6e164a96-c243-3975-aebe-8e76fd77a3b3 | -15.19238 | -56.78763 | 2025-10-11 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f292c4a3-f7f5-364f-8eb4-0e89c28d9ca4 | -17.3024 | -50.99255 | 2025-10-11 01:09:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 987e52f5-effe-3d1f-8d8d-89e72d06d010 | -17.84496 | -57.58924 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| ab9a1353-a9ba-3b92-abe0-8480602ef4f8 | -16.30253 | -47.14906 | 2025-10-11 01:09:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 71ef264c-ced8-38e2-ae54-27b89a4482c0 | -17.90132 | -57.66036 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ef07acb8-e8c5-3250-8a41-12d4f9f0a2ec | -17.82713 | -57.65854 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| a6802564-5647-37ec-98fb-43a3a5cbd415 | -17.83731 | -57.66671 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| fc91b54b-8612-33c6-ab69-a977b1d896b0 | -17.90651 | -57.4975 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 095084f2-1d2f-3484-99b3-bde9e75359d4 | -18.04332 | -57.54994 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 994a97c0-7af7-376e-94ce-4b2db85fd08e | -15.19108 | -56.77847 | 2025-10-11 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f479b7fa-6f5f-3a71-b852-3e9a6a5a26de | -15.67968 | -56.19893 | 2025-10-11 01:09:00 | TERRA_M-M | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ab2d5adf-885c-324b-ab67-b78921e35cca | -17.2942 | -50.98862 | 2025-10-11 01:09:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 5afd47ab-065d-30bd-87ed-38ca42caf682 | -18.82026 | -54.96423 | 2025-10-11 01:09:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2238592d-622d-3338-8302-6982e7f10e0c | -15.68186 | -56.15021 | 2025-10-11 01:09:00 | TERRA_M-M | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9296f05b-61b9-3b30-bbbe-ba34af3894d1 | -15.02753 | -49.45313 | 2025-10-11 01:09:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 006a9b65-a166-3010-bfa4-9007b4f0f93c | -17.81951 | -57.66931 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| b6b347aa-8257-3d6c-854f-31106f2df39b | -17.81821 | -57.65973 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.5 |
| a425961e-ed4a-3364-9ee5-4753c728929e | -15.27468 | -56.90992 | 2025-10-11 01:09:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d9c9d70a-58c7-3eea-83a6-58d3c080de68 | -17.83603 | -57.65727 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |


[Clique aqui para ver as próximas entradas](README3.md)
