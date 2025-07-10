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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cb1776e-3592-30eb-9919-0a4f0793fae3 | -10.5773 | -49.1533 | 2025-07-10 12:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| ed47b942-5874-349a-b167-3835ee91ea2a | -8.5022 | -43.3085 | 2025-07-10 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 132.7 |
| 33e039ed-4546-3bc2-b205-3c1d8356e276 | -6.1425 | -45.8676 | 2025-07-10 12:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 20064bd5-7e85-3fbe-9784-83579b4070f7 | -8.3613 | -43.9548 | 2025-07-10 12:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 169.7 |
| f97c5075-655d-34e9-922e-a8a254357a71 | -8.5025 | -43.285 | 2025-07-10 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| d1cac1cf-a3b3-3c89-ad5a-e15eaed83403 | -7.0102 | -43.4865 | 2025-07-10 13:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 6ce1e7c0-27b9-3f14-8050-64ca12eaeef5 | -8.5211 | -43.3063 | 2025-07-10 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 713d242d-034e-35f5-a910-82513e9f3c2d | -13.338 | -52.9054 | 2025-07-10 13:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| a0ed4e8f-5c47-320f-a068-88510f7d1818 | -6.1425 | -45.8676 | 2025-07-10 13:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 09d41da2-d51b-3c52-b956-b7fdb17319a1 | -8.5022 | -43.3085 | 2025-07-10 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.7 |
| 27f8bae8-c1c4-3795-bb96-2444fd3d4676 | -8.3802 | -43.9527 | 2025-07-10 13:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 122.0 |
| ab81c860-3d03-3b1a-a231-7f5f5b5aac1a | -13.338 | -52.9054 | 2025-07-10 13:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 118.2 |
| debcf2ca-8c3c-380d-ba4e-80be4278250e | -10.5776 | -49.1316 | 2025-07-10 13:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 55d59dc3-0dc1-3013-adcc-46132d01bc5c | -7.0102 | -43.4865 | 2025-07-10 13:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 1b7f6404-94a1-3dee-82b6-8210feb153f2 | -6.1425 | -45.8676 | 2025-07-10 13:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 3a5b9db0-f944-369a-b4a9-15b7764975cf | -8.3802 | -43.9527 | 2025-07-10 13:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| b774e476-1bbe-33b1-8df9-2b791f57d298 | -10.5773 | -49.1533 | 2025-07-10 13:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| d176d8fb-1dbd-3ddd-ac43-eeada6208cbb | -8.5022 | -43.3085 | 2025-07-10 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 142.6 |
| 5caae50b-266f-3b42-9e94-aa21d707847f | -8.3802 | -43.9527 | 2025-07-10 13:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| ff83b2d9-b948-3bce-bc9f-fff2cbc84cf2 | -15.2502 | -51.533 | 2025-07-10 13:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 5fbd8f82-2c4b-3ce3-b975-da472ffb9fac | -13.338 | -52.9054 | 2025-07-10 13:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 19a9c00f-0e8a-3878-9bb5-1d75be962b47 | -10.5776 | -49.1316 | 2025-07-10 13:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 9b44bb7e-0687-3bcf-85ad-dd58cfeef696 | -6.1425 | -45.8676 | 2025-07-10 13:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 7bb00b4b-d8d2-3e79-83eb-c19ac88e22e5 | -15.2308 | -51.5358 | 2025-07-10 13:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 141744e2-6167-3769-967b-2a451a53f2c6 | -7.0102 | -43.4865 | 2025-07-10 13:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 162.8 |
| e79ecb77-132b-37f0-a01c-8373713af1e3 | -8.5022 | -43.3085 | 2025-07-10 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 140.1 |
| 4bff1443-5223-3577-9d05-04ad706c5a9d | -10.5773 | -49.1533 | 2025-07-10 13:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 38e04911-2990-3130-98dd-13cff685f34e | -6.8485 | -42.7979 | 2025-07-10 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 93d6dc39-b778-30fa-b619-ab28ad34504f | -7.029 | -43.4847 | 2025-07-10 13:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 015d4f50-64b2-346e-832b-33a2f9201ddb | -6.8485 | -42.7979 | 2025-07-10 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.1 |
| a416629e-4489-32d3-a621-11d55dbb526e | -7.0102 | -43.4865 | 2025-07-10 13:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 98bae4a0-d5b6-34f8-9815-0ff54ed98d0a | -8.5022 | -43.3085 | 2025-07-10 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.9 |
| 0abfb558-3d7e-3ffb-aa03-33d414897ccc | -7.029 | -43.4847 | 2025-07-10 13:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 0242ceb5-dd0b-31b3-a543-53869b1e01e9 | -13.338 | -52.9054 | 2025-07-10 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| aba2ea76-c529-34cd-8ab3-ba350d16373e | -10.5776 | -49.1316 | 2025-07-10 13:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 3263db55-3ef5-3127-81b7-9092228c280f | -6.1425 | -45.8676 | 2025-07-10 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 146.5 |
| aed5d5fe-cb47-321c-adce-a86572c7fe6f | -10.5773 | -49.1533 | 2025-07-10 13:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 6629784e-a88b-3607-95c9-82a6520c7eb6 | -8.3802 | -43.9527 | 2025-07-10 13:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 99f3af1f-faad-3133-b68c-06f0a2e7144c | -10.5773 | -49.1533 | 2025-07-10 13:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| ca2b1f63-d2e1-302b-a576-b53057b5d667 | -7.0102 | -43.4865 | 2025-07-10 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 123.5 |
| a63c90c0-dc2b-3aac-9047-7053a87faad2 | -13.338 | -52.9054 | 2025-07-10 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 6a929707-fc87-38b9-bd54-fae5819b6928 | -7.029 | -43.4847 | 2025-07-10 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 6dd6a48e-d929-3610-b091-2aded72131e3 | -8.3802 | -43.9527 | 2025-07-10 13:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 129.6 |
| c5aa3620-82d4-3f17-b8b6-5881a52ab267 | -10.5776 | -49.1316 | 2025-07-10 13:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| ec609f30-3131-305f-a5f1-6f59afb7aa0a | -6.8485 | -42.7979 | 2025-07-10 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 3f8db93d-9bad-3dc3-a58a-1a2cdadbc7c9 | -6.1425 | -45.8676 | 2025-07-10 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 10b22ac2-ebab-348a-a867-f9101403f6a8 | -8.5022 | -43.3085 | 2025-07-10 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 125.1 |
| de67c123-0b13-3095-89ef-f47f3318596b | -7.0099 | -43.5098 | 2025-07-10 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| a9177840-3a75-30ce-993d-07c275ee6f9e | -6.2049 | -45.1868 | 2025-07-10 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 5af1f96c-8a34-38b0-b391-8286825d4542 | -6.9914 | -43.4882 | 2025-07-10 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 116.3 |
| e7143a64-92cd-329d-a0ef-32a38036d7b6 | -6.9911 | -43.5116 | 2025-07-10 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 57b3884e-021b-34fe-8e35-cf5c4bd12ac7 | -6.8485 | -42.7979 | 2025-07-10 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 2fbe1ed4-50c3-3476-9ece-8df48f87dcde | -8.5211 | -43.3063 | 2025-07-10 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 12c62664-726c-3f8f-90b2-372283f01aca | -8.5022 | -43.3085 | 2025-07-10 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 29a7f8d8-fadd-345f-89c4-5a80d9e57ce6 | -13.8686 | -45.8421 | 2025-07-10 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 473831d9-3256-369f-ba46-972fdc022813 | -8.3802 | -43.9527 | 2025-07-10 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 5fdb8f08-392c-3a83-80aa-1d39a8898d22 | -6.1425 | -45.8676 | 2025-07-10 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 6185def9-aecb-3e14-8e91-45dce081ba1c | -10.5773 | -49.1533 | 2025-07-10 13:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 294a0266-f234-3a77-8813-5e8b679ec9b3 | -7.0102 | -43.4865 | 2025-07-10 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 337.4 |
| 30bdc08e-7def-3c50-8436-60210c6bc9d3 | -6.1862 | -45.1882 | 2025-07-10 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| f21ff07f-e4a4-3e3f-acb3-ec1285904c5c | -7.029 | -43.4847 | 2025-07-10 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 145.6 |
| b523dee3-3f8f-335d-b453-97e4c0ace97a | -10.5773 | -49.1533 | 2025-07-10 14:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a35176ec-8a91-38bd-9c78-12440a62fb80 | -6.8485 | -42.7979 | 2025-07-10 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| f2a5dbd0-3153-37c1-95d5-4d27b6758579 | -10.5776 | -49.1316 | 2025-07-10 14:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 84197b4b-2b1f-3961-836e-2c050698ea23 | -13.8686 | -45.8421 | 2025-07-10 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 83c8f70d-4fd5-3e7b-baa8-70e8c7bad35f | -7.0102 | -43.4865 | 2025-07-10 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 8e03dbd6-e854-3c52-9da1-0e07a6c32f71 | -8.5022 | -43.3085 | 2025-07-10 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 133.8 |
| 37af69f9-4171-3362-9da3-8c0994154410 | -7.029 | -43.4847 | 2025-07-10 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 21d972c9-c1cd-30b0-959b-f50f9b81fd2a | -6.2049 | -45.1868 | 2025-07-10 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| c0fe0a56-762a-3e9d-9cd8-1d8a2b4b874b | -7.0099 | -43.5098 | 2025-07-10 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| ce380f0b-28a6-34ca-9b6b-ddcfa9925ab8 | -8.3802 | -43.9527 | 2025-07-10 14:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 1a63f52c-f730-3bad-8ebd-9125681800cd | -6.1425 | -45.8676 | 2025-07-10 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 993e60d4-d408-3c04-9cd9-a5ab0580b5d2 | -6.9914 | -43.4882 | 2025-07-10 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 2ff8e5f2-547f-3bd1-944c-f9d2d6ccfdf4 | -5.7887 | -43.6134 | 2025-07-10 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 25590b18-be62-361c-b443-d5dae004b0bd | -19.3778 | -51.4008 | 2025-07-10 14:00:00 | GOES-19 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 9c70fd42-3e6c-3d65-8a89-cd7e94569fcd | -6.1425 | -45.8676 | 2025-07-10 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 56d8cb3b-9d1e-3d3e-9a18-5ec71062aa43 | -10.5773 | -49.1533 | 2025-07-10 14:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 16473f90-2c3b-3e80-a703-9a0bd3d66769 | -10.5776 | -49.1316 | 2025-07-10 14:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 5b4fd996-1d73-3cac-8f45-c82410446c50 | -15.2502 | -51.533 | 2025-07-10 14:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 15baad2f-15bc-3099-9f78-5f9db402e55e | -7.0102 | -43.4865 | 2025-07-10 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 7d6b6d27-1bbd-3922-830d-4cca2741f2d0 | -6.8485 | -42.7979 | 2025-07-10 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| c586d05f-2aca-3320-b430-12ab669a17ed | -6.8673 | -42.7961 | 2025-07-10 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| f231b3d4-b5cb-3b05-b450-f994ac6fba47 | -13.8686 | -45.8421 | 2025-07-10 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 338.8 |
| fb3cd948-cf2a-30f0-9a5f-f09dd47af544 | -7.029 | -43.4847 | 2025-07-10 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 53aa2ff6-1cfb-3bfc-99dd-d1f119206819 | -19.3778 | -51.4008 | 2025-07-10 14:10:00 | GOES-19 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 107.5 |
| ef11bd3f-00bb-3dfe-ad4b-c57df1aa3044 | -11.4397 | -45.0923 | 2025-07-10 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 374e13c9-e964-34f6-9c3a-98033f3a7306 | -13.8686 | -45.8421 | 2025-07-10 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 70fb0033-6628-3a61-af1e-35449b55d51f | -10.5773 | -49.1533 | 2025-07-10 14:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 21b3bfe0-89ca-3dae-9ec8-0aeea7a04cbf | -8.5211 | -43.3063 | 2025-07-10 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 8b0558a1-b2db-362d-a82e-c797fbd53e6e | -19.3778 | -51.4008 | 2025-07-10 14:20:00 | GOES-19 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 404a027b-99cf-31e4-8908-ceb7a512dee2 | -6.8485 | -42.7979 | 2025-07-10 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.6 |
| 42f3a1d4-fad5-311d-a32a-ebb236cb43e1 | -7.7432 | -43.6013 | 2025-07-10 14:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| df5d3c33-1d41-328a-b136-4f923f485f2d | -10.5776 | -49.1316 | 2025-07-10 14:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| c68e4fcd-135d-3e0a-871b-d99e3fba181e | -5.77 | -43.6148 | 2025-07-10 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 3b7c2f03-8be0-31de-bd0d-9b63c6b942bb | -15.2502 | -51.533 | 2025-07-10 14:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 62d93502-ef0b-374b-86c4-46c965791d89 | -11.4397 | -45.0923 | 2025-07-10 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 3097c287-4938-3ceb-98aa-041763dc0bce | -7.0102 | -43.4865 | 2025-07-10 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 0e41976d-95e2-3fa4-ac3c-35fdda0cf700 | -6.1425 | -45.8676 | 2025-07-10 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 178.0 |
| 01b9e9ca-9fce-3f18-bdc3-44c837a9142d | -7.029 | -43.4847 | 2025-07-10 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| ef871372-4c8c-38e5-8c10-3bb80eb0adc3 | -7.029 | -43.4847 | 2025-07-10 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |


[Clique aqui para ver as próximas entradas](README30.md)
