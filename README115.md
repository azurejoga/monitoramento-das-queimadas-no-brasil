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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9230bf71-9842-3bf2-88d5-a39b90d8b091 | -9.6232 | -47.0416 | 2025-09-03 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 6caf27dc-f4e1-36c7-bcdc-c7dbc8e0817c | -11.8533 | -51.4318 | 2025-09-03 13:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 63adebb0-6cad-3304-a4ba-7fced6e33a43 | -11.6836 | -57.3518 | 2025-09-03 13:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 4368a8c7-f43e-3479-a21f-95746c89d8f5 | -12.824 | -48.06 | 2025-09-03 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| e09f88d3-c55c-3fe8-9935-f471d86d7957 | -8.2006 | -49.5559 | 2025-09-03 13:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 25590adb-17dd-3a3f-87a6-a9ebcd1002a4 | -9.7427 | -49.414 | 2025-09-03 13:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 00933dc6-362e-3d8e-8358-83707592206f | -5.7343 | -45.5375 | 2025-09-03 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| cd8c0768-7482-353d-877d-14b527c98c8b | -6.797 | -44.0859 | 2025-09-03 13:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| c00a5336-1257-3b37-b3b0-14908f43682f | -15.0254 | -50.071 | 2025-09-03 13:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 8edc2762-1129-38b7-86c6-b59751b504dd | -7.5302 | -47.4443 | 2025-09-03 13:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 182.9 |
| 8a8b6caf-4cd0-31d6-9c0e-1a5848b36d3b | -5.9079 | -57.7506 | 2025-09-03 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 158.8 |
| 10645401-452b-3ef1-a430-77342102e9f3 | -5.8896 | -57.7318 | 2025-09-03 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| d31058c0-ebc0-3b02-9027-b46539b91a6b | -7.53 | -47.4662 | 2025-09-03 13:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 9fabb5d7-2fe1-3c19-9386-fb838fe159d5 | -6.0597 | -44.6976 | 2025-09-03 13:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| cc32dd11-b726-39f3-bd95-30e3bbdb4a8b | -8.0197 | -44.1072 | 2025-09-03 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 1259e055-3a1e-3c70-88ce-f6d76e9caff3 | -5.8111 | -43.2156 | 2025-09-03 13:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| f42acab7-1f58-39d1-ab2b-bed2bc9a7e31 | -7.5157 | -45.3478 | 2025-09-03 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 200.8 |
| aa3f075b-aba2-30ee-b4ff-0f41e96611af | -9.7613 | -49.4337 | 2025-09-03 13:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 236.1 |
| e402c5cf-2ffe-30b3-be3a-680828bb402d | -8.0203 | -44.0608 | 2025-09-03 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 8c37f24c-693c-3417-ac18-ada6642d0050 | -8.3646 | -48.2899 | 2025-09-03 13:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| ddbf53e5-e242-37f0-9fcb-1ce6cf27f7eb | -12.793 | -47.6415 | 2025-09-03 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| f18330c5-4392-3fe7-95e4-3137ae2b1b69 | -6.7407 | -45.911 | 2025-09-03 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 5171e4cf-b58f-35ee-8f67-99b418ed677a | -6.5546 | -43.9221 | 2025-09-03 13:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 50226cce-67eb-3b0c-8277-3e60e8fdcdca | -9.6226 | -47.0861 | 2025-09-03 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| d65c95fa-71e3-31f3-82d7-4530665be1e9 | -11.6647 | -57.3533 | 2025-09-03 13:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 878a05f8-265f-333a-a063-b431c4d912a2 | -11.0181 | -51.5001 | 2025-09-03 13:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 152.1 |
| ae625bb3-580d-38c0-86a1-1279c9dccbaf | -5.7343 | -45.5375 | 2025-09-03 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| caaa0fbb-ac84-3a25-a46c-801f4033e920 | -10.7524 | -48.8294 | 2025-09-03 13:20:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| ed2142a4-a468-39a1-8fcf-95dad7b11c16 | -10.0932 | -54.7667 | 2025-09-03 13:20:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 128.8 |
| e7471978-0b81-373c-abd0-ea44ba6816b4 | -6.7967 | -44.1091 | 2025-09-03 13:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| dc355c39-a19c-3e81-8656-ea60b9c2d5a0 | -10.9323 | -50.8529 | 2025-09-03 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 56b5c04e-79f3-34a0-917d-6e57db0a268a | -8.2006 | -49.5559 | 2025-09-03 13:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| d4a609ba-10af-3509-b492-57f79c5eba8a | -5.8455 | -45.6421 | 2025-09-03 13:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| ddc971c6-ade6-3b81-9956-328300bb1c13 | -6.3692 | -45.6258 | 2025-09-03 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| e7080d89-d2f2-3173-8ceb-622373d3dcb1 | -5.7183 | -45.2226 | 2025-09-03 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 322f73ea-34f0-3701-9c40-8c0c9c843371 | -10.9136 | -50.8336 | 2025-09-03 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 9aeba321-750d-3488-9b47-6fd7fb50bedd | -6.0699 | -45.6259 | 2025-09-03 13:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 174.2 |
| ebc8f1b7-8b0e-323f-bcd6-12ba23b84ca2 | -12.824 | -48.06 | 2025-09-03 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 72ede342-5a0b-3bbb-be83-c31fd7146a26 | -16.8532 | -49.6196 | 2025-09-03 13:20:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 4e95ccd7-1bbd-34d0-9869-dab5f9353d45 | -7.4969 | -45.3495 | 2025-09-03 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| e3392ed7-3a46-32c7-8959-5876df0d81eb | -7.0131 | -43.2291 | 2025-09-03 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 95a7abbe-8481-338c-8421-7be2b7d97b9e | -10.9524 | -50.7658 | 2025-09-03 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 4d72b406-1838-3cd5-95d5-59334976ecf4 | -11.3901 | -43.5602 | 2025-09-03 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 20cd29c5-2f8b-33a2-a60d-7602713aed27 | -6.7597 | -45.8871 | 2025-09-03 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| f03f0c66-54b9-30fe-ae1d-5cc455e61463 | -8.3644 | -48.3116 | 2025-09-03 13:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| c5c34bad-a12d-327f-bb49-201de9ce79cf | -6.1234 | -45.9139 | 2025-09-03 13:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f241502a-3789-3e2e-92d2-831be72e35ad | -11.8533 | -51.4318 | 2025-09-03 13:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| d6ad859c-b684-31d7-ae47-8e4f9363c632 | -15.1771 | -52.356 | 2025-09-03 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 163.4 |
| dbdde8f3-4984-3311-a639-00fad11bc10c | -15.0254 | -50.071 | 2025-09-03 13:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| dd29e792-cedb-3c76-afc7-e5a51f3de95b | -12.8244 | -48.0377 | 2025-09-03 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 842c63d2-9967-35c0-9186-590785ecf65f | -6.6982 | -48.4035 | 2025-09-03 13:20:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 79.4 |
| ffdd7d48-6410-36f3-9a93-6933afda7dd4 | -7.0128 | -43.2525 | 2025-09-03 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.9 |
| f6d2e1c7-8d0b-3195-b75d-a5f14f50c8e1 | -9.6229 | -47.0638 | 2025-09-03 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| cdb0e8fa-1d44-3d0c-9b3a-fd7090824710 | -6.3502 | -45.6498 | 2025-09-03 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 355.3 |
| 61f29c93-4462-3dc3-ae50-48db09b45d5c | -5.7181 | -45.2453 | 2025-09-03 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 224.6 |
| da9a6fcd-a6f8-3ea3-a022-0884836ec3c2 | -13.5162 | -47.0393 | 2025-09-03 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 94f4b855-cc31-387e-836f-1693b0c1d68b | -6.3689 | -45.6483 | 2025-09-03 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 306.3 |
| f85e6306-150c-3436-a936-95f614f3d888 | -9.7429 | -49.3925 | 2025-09-03 13:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| ffbe713e-6a41-39cb-8bec-a2aae5045b5d | -6.7595 | -45.9095 | 2025-09-03 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| c19cad86-7ccf-3895-ab7e-cc437560f76d | -15.1576 | -52.3586 | 2025-09-03 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| c8234c1b-8976-3875-8c76-b001d01155f5 | -12.8432 | -48.0573 | 2025-09-03 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 7a8ff72d-89e3-32f1-beaf-07902ae9ba2e | -6.3504 | -45.6273 | 2025-09-03 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| f6b1ce20-366a-3254-acbd-eb3b2c685540 | -9.7615 | -49.4121 | 2025-09-03 13:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 23d0b535-5a14-3b45-b4a0-74e2d4d66593 | -8.0197 | -44.1072 | 2025-09-03 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 6fcffece-85b6-3790-808d-702a3308c0ed | -8.8842 | -45.822 | 2025-09-03 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 1a9e45c6-5b47-3b08-ac93-f1b79ee56e71 | -9.7427 | -49.414 | 2025-09-03 13:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 2b9616be-423a-3bf8-9e67-5b62c1326bde | -8.0794 | -45.3844 | 2025-09-03 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 239.7 |
| cf4c663e-90c3-35cd-8383-18e600458d4f | -11.6836 | -57.3518 | 2025-09-03 13:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| e6ed64f6-0df0-3312-9b8f-58a7c5949ee4 | -8.0796 | -45.3617 | 2025-09-03 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 583.2 |
| a3d70559-0656-314f-adcf-d81e5399a6f4 | -10.9326 | -50.8316 | 2025-09-03 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 27d6e414-b68d-34be-9a5a-eb6089534e2f | -7.9828 | -44.0415 | 2025-09-03 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 14f98270-461b-3100-9d62-cd0e530d2b0c | -7.5157 | -45.3478 | 2025-09-03 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 5ae2df3e-2c20-3459-a37e-4293baf5caf1 | -9.4023 | -48.0365 | 2025-09-03 13:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| e1e8b621-7ad5-3f00-b81c-74fcb10c8506 | -6.797 | -44.0859 | 2025-09-03 13:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 36be1755-cd02-3cda-8aa4-618c3bad8c09 | -8.0206 | -44.0376 | 2025-09-03 13:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 21ee2df1-feb0-3e76-8e17-be6b9a6451e1 | -11.8537 | -51.4106 | 2025-09-03 13:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 097912af-698a-35bf-abe9-eb4317013b30 | -6.6538 | -45.2417 | 2025-09-03 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 4f9d9f92-c9b0-32c0-be2e-e10509e62080 | -7.5302 | -47.4443 | 2025-09-03 13:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| a8347283-214e-33e5-8b99-fb16506182b2 | -9.1373 | -49.6659 | 2025-09-03 13:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 9bfdf57f-ba44-361d-8fbc-60eb2874cb16 | -6.35 | -45.6723 | 2025-09-03 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 270.8 |
| 5d68f52d-5a63-3472-ac78-267a0185ca18 | -6.3687 | -45.6709 | 2025-09-03 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 226.5 |
| 5dca76c5-3b17-3bd4-8944-6eeea8afadd7 | -7.4842 | -44.8043 | 2025-09-03 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 60708ca5-2653-3f52-92c5-0c8df1e0aa18 | -10.7714 | -48.8273 | 2025-09-03 13:20:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| ef91a7b8-c0d5-3dcb-9e1d-2bf5d4bd07e9 | -8.8839 | -45.8446 | 2025-09-03 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 1314f3f8-f25a-3de8-ac8c-162afd45a295 | -12.7926 | -47.6638 | 2025-09-03 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 85091c3a-b3c5-3ac0-a4c9-b9ce68dd53be | -7.53 | -47.4662 | 2025-09-03 13:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 74c00ab7-6754-3900-b41c-ab1f00cd5bf3 | -9.6232 | -47.0416 | 2025-09-03 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 08ba3b5b-40dd-38f4-a65a-2acb13350088 | -7.4966 | -45.3722 | 2025-09-03 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 0418150b-1f9d-3570-a779-dd25b370d7af | -6.994 | -43.2543 | 2025-09-03 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| efdc582d-754c-3a53-a2de-6d15f59d3d85 | -11.3897 | -43.5839 | 2025-09-03 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 382f47be-bb01-3722-bcff-95f3e1515fef | -10.5004 | -53.651 | 2025-09-03 13:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 43bfbeaa-ff93-3360-b356-811cfc2f5d73 | -9.402 | -48.0585 | 2025-09-03 13:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| dc798f01-8b95-356b-8302-ae73cf2d3bde | -5.8297 | -45.3051 | 2025-09-03 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 90206143-491f-3b5f-9b43-390f716e6698 | -11.3709 | -43.5631 | 2025-09-03 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 1d5a89be-2e5c-3a36-88bf-a3d07bbf4b8d | -12.4071 | -47.7849 | 2025-09-03 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 81d10605-e4b2-36a6-aa87-8e006246ca09 | -13.5162 | -47.0393 | 2025-09-03 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 80.6 |
| c4399b6b-b406-32a3-8d7d-a773fa05223c | -8.0608 | -45.3636 | 2025-09-03 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 219.1 |
| 42ffbe5b-b895-306a-8722-480bd3c69547 | -9.6421 | -47.0395 | 2025-09-03 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 82f7aea8-5da2-36af-94de-3ae076ae4691 | -5.8642 | -45.6408 | 2025-09-03 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 0923b1e2-9394-34f7-aea1-cc9339289aed | -13.5167 | -47.0167 | 2025-09-03 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |


[Clique aqui para ver as próximas entradas](README116.md)
