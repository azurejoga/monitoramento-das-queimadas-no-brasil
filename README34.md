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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03e28f54-069b-3681-80a5-2f1da98dac65 | -15.2897 | -57.4025 | 2026-07-01 13:40:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 1950aca5-ccf3-3d55-b586-530067f69703 | -17.712 | -46.7798 | 2026-07-01 13:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 199.1 |
| b8e2afa7-0a04-34b8-b79e-08022fc6e25c | -9.0175 | -45.7397 | 2026-07-01 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| c26ffb79-6d70-3020-bb94-d53f59db7011 | -8.9985 | -45.7418 | 2026-07-01 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 4cd46d9c-e334-3eaf-9cb8-b2b62b850192 | -11.4338 | -56.0509 | 2026-07-01 13:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 143d3af0-2cb9-36f1-9a74-d18dbef80899 | -10.6598 | -54.5169 | 2026-07-01 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 332.5 |
| 867b662b-8527-3a1f-af5d-4435771fd0af | -9.0178 | -45.7171 | 2026-07-01 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 954a7f3c-a125-366d-9660-f4651c7835a3 | -10.6784 | -54.5356 | 2026-07-01 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 228.4 |
| 0f0458f2-c4c1-3fb8-8844-f83aaa5958b3 | -8.9989 | -45.7191 | 2026-07-01 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 159.6 |
| fb028e4a-6d07-33ed-8a3d-44cf306b6fdf | -9.0175 | -45.7397 | 2026-07-01 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 9b7160c6-a46b-32c0-bbe4-711ad3cd198e | -12.5135 | -48.2802 | 2026-07-01 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 749ef640-bf08-3663-ae2d-a8f0351557dc | -8.9989 | -45.7191 | 2026-07-01 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 79fc87ef-8a4a-3834-beeb-8f1480edd36d | -12.5138 | -48.2581 | 2026-07-01 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f71af468-df05-3f83-9427-025919d97eca | -15.2897 | -57.4025 | 2026-07-01 13:50:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 102.5 |
| af4d0450-3761-3c5d-90ff-726def62cf1e | -8.7841 | -44.8315 | 2026-07-01 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| a03f772c-4279-3469-92e3-9a332b626fc0 | -10.6596 | -54.5372 | 2026-07-01 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 233.3 |
| ffba9ab2-6574-33ab-8c19-c1c3cab13e80 | -17.712 | -46.7798 | 2026-07-01 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 159.2 |
| dbb0847e-b32b-39c9-9e58-0aee64e6b7e3 | -15.29 | -57.3823 | 2026-07-01 13:50:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 6e10ebe4-ce5f-396b-b095-5f594b980cba | -10.6787 | -54.5153 | 2026-07-01 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 261.8 |
| 576da7b4-507a-30ae-a0a4-8f4a25b5d2d7 | -8.9985 | -45.7418 | 2026-07-01 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 17f4c8cd-8113-30b4-a427-60cff35b7f3c | -10.6598 | -54.5169 | 2026-07-01 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 290.2 |
| 07b881a9-6a8c-3607-9d7a-3d95c477f8c7 | -15.2897 | -57.4025 | 2026-07-01 14:00:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 5d9035fc-cd96-3b8f-9de5-cbdb3e06aa7f | -10.6784 | -54.5356 | 2026-07-01 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 207.0 |
| 4269266a-056b-3a36-8637-05221d757922 | -10.6596 | -54.5372 | 2026-07-01 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 225.3 |
| 0dcfb7be-b59c-31eb-b6b5-4c4b0fdaa3e5 | -10.6787 | -54.5153 | 2026-07-01 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 213.8 |
| 98086d4f-2aa6-3fc9-b9f5-18341412b7c5 | -8.7841 | -44.8315 | 2026-07-01 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| bbba6c06-7a9d-3306-bcb7-6b96475307be | -15.29 | -57.3823 | 2026-07-01 14:00:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 8683379a-fe67-3b42-913d-280309c3c5f1 | -10.6598 | -54.5169 | 2026-07-01 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 263.5 |
| aaebcdc8-9e55-320b-a1c6-8a41f5aac476 | -12.5138 | -48.2581 | 2026-07-01 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| be98a2f6-06c0-34e2-9c70-e8dfcef3975d | -11.4149 | -56.0525 | 2026-07-01 14:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 905a1f3f-00a5-3def-b78e-192e297f8ecf | -8.9989 | -45.7191 | 2026-07-01 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 1327b6c7-df5c-3fe9-81d5-911664db8d6e | -12.5327 | -48.2776 | 2026-07-01 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 74315ca7-9346-38c3-af5d-9c075b589031 | -11.4336 | -56.0711 | 2026-07-01 14:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| a12ae2fc-9901-3358-96ae-d80fb168321b | -11.4338 | -56.0509 | 2026-07-01 14:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| f9778c81-1368-3f08-98f3-769b256f4cf0 | -9.0175 | -45.7397 | 2026-07-01 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 2574a87e-7636-3423-b196-8e1c5a700b2c | -8.9985 | -45.7418 | 2026-07-01 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 22a1cc8d-9fa8-3889-a058-b0170c6dddd8 | -12.5135 | -48.2802 | 2026-07-01 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 2457753c-408a-3918-843e-ce79ee7e7cb2 | -10.6596 | -54.5372 | 2026-07-01 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 238.5 |
| 181a40a3-6b1a-3e8a-86c0-f3b2d2b093a9 | -15.2897 | -57.4025 | 2026-07-01 14:10:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 84234d92-e2d3-3d54-9fdb-ca43e3e4c495 | -12.5135 | -48.2802 | 2026-07-01 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 5000100f-02cd-3e73-b29b-02932e7eeff2 | -12.5138 | -48.2581 | 2026-07-01 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| d2561779-3d76-3111-8c22-abb1b2603e66 | -8.7841 | -44.8315 | 2026-07-01 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 69e10f3c-b528-3e4a-a404-55215085b6e4 | -15.29 | -57.3823 | 2026-07-01 14:10:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 2ff25a6b-6b38-3323-8ed1-6b288ec694c7 | -11.4338 | -56.0509 | 2026-07-01 14:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| c5c471e6-acad-3019-911b-3e4dcf6f1a7d | -9.0175 | -45.7397 | 2026-07-01 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 7c3b2f1c-8e25-31ef-a3a3-546c717f4330 | -17.712 | -46.7798 | 2026-07-01 14:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 87.1 |
| ece496c4-1365-3f7a-b60e-003a18fe7c8a | -11.4336 | -56.0711 | 2026-07-01 14:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| b5265037-01bb-36f7-8460-b3facfd332d2 | -10.6598 | -54.5169 | 2026-07-01 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 302.0 |
| 5a6cad0c-7bae-340c-a67b-e1e0b5d92430 | -12.5327 | -48.2776 | 2026-07-01 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| cb6eba49-5a88-3739-abef-f8d35c3e4f02 | -5.4925 | -43.2165 | 2026-07-01 14:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| d6b97c61-7d97-3a02-a233-390bde998875 | -8.9985 | -45.7418 | 2026-07-01 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| fadbf71b-6df0-32c4-a962-048a4ea11dc4 | -8.9989 | -45.7191 | 2026-07-01 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| c5739216-161e-3d86-9c27-d8b063a107bd | -10.6787 | -54.5153 | 2026-07-01 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 200.2 |
| cb854ab7-4896-32b7-8ba3-d1209a16b468 | -11.4149 | -56.0525 | 2026-07-01 14:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| df98e965-42dd-32b0-b400-c16ccdb7d321 | -10.6598 | -54.5169 | 2026-07-01 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 304.5 |
| afd12239-dec4-3e92-b075-a7ce81ed946a | -11.9113 | -43.3843 | 2026-07-01 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| e1479cc2-73f9-317a-92c4-c25939170490 | -11.4149 | -56.0525 | 2026-07-01 14:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 68d81075-d2d3-3b05-ac48-7189fae1ec62 | -10.8132 | -48.5605 | 2026-07-01 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| e9fb7aea-0953-3f4a-a5aa-3eaf83c6c486 | -15.29 | -57.3823 | 2026-07-01 14:20:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 36b73a52-80ea-33ae-b8df-8a831085d5db | -11.4338 | -56.0509 | 2026-07-01 14:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 92eaccd2-a85e-39b9-bbf4-234cb900dafb | -11.4336 | -56.0711 | 2026-07-01 14:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 7ddac3f4-3e41-3a63-965c-e727b5254769 | -17.7114 | -46.8031 | 2026-07-01 14:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 04e5e549-92ff-3071-bfc0-d4faae890ae7 | -8.7841 | -44.8315 | 2026-07-01 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| e64896ad-ed0d-31ce-9a34-7b4f683d275e | -10.6787 | -54.5153 | 2026-07-01 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 223.4 |
| cd7eea3a-ba02-372c-8ce9-e498c635e275 | -10.6596 | -54.5372 | 2026-07-01 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 181.9 |
| 51194874-1665-38f7-aec5-aa5c1c3fcc1d | -9.0175 | -45.7397 | 2026-07-01 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 42cdd7ed-10b9-35c9-b238-5b424c4d776a | -8.9989 | -45.7191 | 2026-07-01 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| f4099d77-862a-3b07-8509-7a95e5dab9c9 | -12.5138 | -48.2581 | 2026-07-01 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 68bb5548-bdab-3aa8-9edf-564fd5d8dc77 | -12.5135 | -48.2802 | 2026-07-01 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 160.9 |
| c2f12f1c-4ef8-3fe0-a1af-7943f8dafb29 | -8.9985 | -45.7418 | 2026-07-01 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 33e1e51a-4311-30e4-b7be-15c4192c15ef | -10.6596 | -54.5372 | 2026-07-01 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 186.3 |
| a6ff80b0-59b8-3d98-be7d-204bc8ce1d16 | -12.5138 | -48.2581 | 2026-07-01 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 6d4302b2-dcc0-3ded-8d31-3895576b08a4 | -10.6598 | -54.5169 | 2026-07-01 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 210.5 |
| fede8bb5-28e5-3a69-9b75-4a59a2565afb | -11.4336 | -56.0711 | 2026-07-01 14:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 73a2a4f5-ebee-3eab-9e12-57ab27226339 | -11.9113 | -43.3843 | 2026-07-01 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 133.3 |
| e0fc1c0f-cad6-31c1-88f1-4650201efef3 | -8.7841 | -44.8315 | 2026-07-01 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| afe68f73-9116-3f86-9289-6a645cb2d3cb | -10.1237 | -52.0905 | 2026-07-01 14:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 46749be5-d584-350a-8bef-3bc109422f3c | -10.7942 | -48.5627 | 2026-07-01 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 8698c5d4-e062-3602-a76c-9a2c73126ea8 | -11.4338 | -56.0509 | 2026-07-01 14:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| fc4c3f10-a71d-3f6a-966a-25a9089e4fff | -11.4147 | -56.0726 | 2026-07-01 14:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 7a7808a3-f1ba-3aa8-a63d-87ee6eac5c06 | -8.9989 | -45.7191 | 2026-07-01 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 5e450ca3-7f7b-32dc-963f-51fa882d3f77 | -12.5135 | -48.2802 | 2026-07-01 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 922e082e-d5fd-357f-b32e-a7c338cc4d20 | -11.4149 | -56.0525 | 2026-07-01 14:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 079e3d68-c094-3396-9e47-cfc5b252c54f | -10.6787 | -54.5153 | 2026-07-01 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 221.6 |
| 44ebe72d-bf90-34ea-b478-b81789e59386 | -15.2897 | -57.4025 | 2026-07-01 14:30:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 39b851d7-f244-353c-9e36-01284a3e2d45 | -17.9126 | -52.7212 | 2026-07-01 14:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 56.6 |
| ec100a76-bb6c-36d4-9932-81ad765ff00e | -11.4147 | -56.0726 | 2026-07-01 14:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 19ca9489-d1f1-3c48-97d2-cb0a95ea5b60 | -11.4149 | -56.0525 | 2026-07-01 14:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| e357ad6b-06bb-3b0f-94e6-df83b7e0e356 | -12.5138 | -48.2581 | 2026-07-01 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| edb562bc-f506-3cd3-8813-da49c48b8533 | -10.6598 | -54.5169 | 2026-07-01 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 163.6 |
| b0ce6549-cb21-3a7c-b0e9-14e42c3ea690 | -12.5135 | -48.2802 | 2026-07-01 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 9b18e494-4305-3dfb-9abb-6dd09822c7af | -10.7942 | -48.5627 | 2026-07-01 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| bf4b365c-532d-36c9-9d3a-d45ace61e8ca | -11.4336 | -56.0711 | 2026-07-01 14:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 385372a0-9292-3a0c-928d-387fa28ac898 | -10.6596 | -54.5372 | 2026-07-01 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 155.8 |
| 366a4d21-f74f-3e8f-bc1d-b1fdb78d00e5 | -10.1237 | -52.0905 | 2026-07-01 14:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 6f0dbce8-3116-33dc-933f-5d36d792ee57 | -10.6787 | -54.5153 | 2026-07-01 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 254.0 |
| 884d5475-58eb-3e4f-9db7-852e94eff165 | -11.4338 | -56.0509 | 2026-07-01 14:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 936d3c32-a0ce-358d-ab74-d275f3808a3f | -11.9113 | -43.3843 | 2026-07-01 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| daf85de6-1ef1-3ece-8331-e20a2df6e064 | -8.9989 | -45.7191 | 2026-07-01 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 6458c4ec-d9c0-31ce-8935-d958d3c47d7b | -8.7841 | -44.8315 | 2026-07-01 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |


[Clique aqui para ver as próximas entradas](README35.md)
