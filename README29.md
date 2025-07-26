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
| 6f8f4aa0-b763-3879-a287-97838409b2ac | -7.29561 | -60.17455 | 2025-07-26 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56a1840f-b1ad-306a-a322-a7e72898753e | -10.22641 | -59.40479 | 2025-07-26 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3398f13-b516-347f-b0ff-9841480c57d9 | -6.54232 | -56.2505 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b23a3db-9147-3205-a290-e0897b153d16 | -7.81657 | -61.33215 | 2025-07-26 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b45f466-91eb-3357-b10c-93e1aa70300c | -6.6335 | -58.83274 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 14b05f32-e267-32c3-b2e6-338f3d4ad38c | -6.54518 | -56.24651 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8fe0bfd-074a-3b64-8b7c-379c80935307 | -6.64308 | -58.82949 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| fb8f07d0-773c-3275-ac48-02f9c17ee640 | -6.62207 | -58.849 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 27.2 |
| c56c5ac1-9e38-3108-8fcf-790b7156eb14 | -8.50012 | -64.04088 | 2025-07-26 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e24eb736-2d3f-33cc-9c33-d113c29d516c | -6.63925 | -58.82441 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 372bea62-0047-3df3-b184-3cd4d5211b0b | -8.07035 | -63.86298 | 2025-07-26 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e52d9f45-5f08-3f79-a402-a3421e8d548d | -6.68639 | -58.84491 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8436ff94-24b3-305b-a93d-49aa83ccb921 | -6.537 | -56.24971 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b668fb1-c378-3d7c-891b-5c5eb86782e5 | -6.54856 | -56.2446 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a720c6b2-b10d-3d46-b612-5ef934c3bb60 | -7.29097 | -60.17756 | 2025-07-26 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e6f821d-7410-3453-8a56-82342f1fb0bc | -6.64499 | -58.84782 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 0fac2f0d-1868-30cc-8154-e95d02cd5530 | -7.2915 | -60.1739 | 2025-07-26 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97f8624f-a16b-3271-9585-f05da7f35b7f | -6.66345 | -58.84608 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 8dd257ff-e0b9-383c-846c-84c792cffb26 | -6.67429 | -58.83423 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 644d70e5-e9c8-331a-9e58-a609dc64016f | -6.67109 | -58.85612 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 9a89a74a-0742-3bf1-bbdf-bd2c9e604c54 | -8.53213 | -63.87898 | 2025-07-26 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c729c957-0af5-3599-986a-5fef068eac36 | -7.66585 | -69.93163 | 2025-07-26 05:44:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21e1fa4f-1f3c-3b2f-b205-8a93de063942 | -7.4949 | -63.81777 | 2025-07-26 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 493624f3-794f-3258-89fa-979f4723a802 | -7.57017 | -61.40685 | 2025-07-26 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ea9f8dfa-14f7-3d25-bb22-d47cb337ef9a | -6.53214 | -56.26165 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eed81fb4-1dd8-377d-968c-1798e5052c74 | -6.65263 | -58.82644 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 7e7b62a5-37fc-37ee-a0c5-a8b605aa685f | -9.46103 | -57.8509 | 2025-07-26 05:44:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c5b9c6c5-39e2-30b1-befd-07ad6d08d063 | -8.07092 | -63.85928 | 2025-07-26 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91ffafb3-51bf-30ae-b25e-94dc60af9c99 | -6.64818 | -58.82575 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 155c97a0-8860-33e2-ba96-35db9d01856c | -6.64116 | -58.84285 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 7e857b94-eec4-3d4b-a722-b967378d299d | -6.67237 | -58.84735 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 172.0 |
| cebaaa4f-c495-314d-9efb-51c0624a5275 | -6.63223 | -58.84164 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 995db01d-1d77-3257-9e8c-4e64e23ffd6d | -6.64244 | -58.83395 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ca477142-371a-3eec-a1d6-318bb115b354 | -6.66919 | -58.83793 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| da4dab3f-c75d-3458-bbd4-9ca3ca552412 | -6.54422 | -56.25317 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9c835ab-9b8c-306a-923d-9c501ca87cbd | -6.6915 | -58.8412 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8c0c279c-373e-3146-b507-eca8ed3da81f | -6.65963 | -58.84101 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e335a3e9-5ce9-35a1-a99d-fe9539d5eab0 | -6.67045 | -58.8605 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| a9c0a697-67be-33ab-907e-588be447b887 | -6.64754 | -58.83015 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 8b8961a6-095d-3ecf-b6ca-f409f5c8fd84 | -7.9019 | -63.52848 | 2025-07-26 05:44:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 041eea62-8cec-3817-a955-428a73856a84 | -6.63862 | -58.82884 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 25cd8efc-2c55-3da9-9c77-40ff418f31e8 | -6.67747 | -58.84361 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 54bb6cc5-873b-3a2b-879f-f0cc33a7b5c6 | -6.66091 | -58.8322 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 2222cbe7-2be2-30b3-8624-e86edeee2fd1 | -6.64436 | -58.85217 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| cb4d25f9-dcb0-3bed-9bb1-942a96436e2e | -6.68005 | -58.82602 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c9478113-1065-3636-83ea-6d743123eadf | -7.18559 | -59.44392 | 2025-07-26 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30575885-4eb1-3e2e-b6a3-19952442a52b | -6.53517 | -56.26316 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e29f964b-9ac9-3acb-b364-7e4884dec231 | -8.50353 | -64.0414 | 2025-07-26 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2abd3139-abb2-3050-a19a-7c0925adcf18 | -6.65836 | -58.84978 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 2515d87c-3eff-3675-9d25-de8612c0f4e3 | -6.54764 | -56.25129 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51a79347-cff0-3114-ad50-d7637443372a | -6.6284 | -58.83659 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 36d1dcbf-275f-3a9a-8450-0cc70cef62f0 | -9.55133 | -65.32384 | 2025-07-26 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41721001-6950-3e2d-b63a-303ba61d1409 | -8.61056 | -64.07256 | 2025-07-26 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a459ac7-6b5a-3ff1-b4db-36753133fd29 | -6.55342 | -56.24871 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3564c0c-1b9a-3e77-822c-39cd5671830d | -6.65582 | -58.83593 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 70aa9de9-7ecb-34a4-a195-9edf970dad71 | -6.65327 | -58.85348 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 3ada5bab-be5f-386a-b638-6cdccfeb0910 | -6.64052 | -58.84726 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 1da85a10-5412-3b09-826b-84c3eee51207 | -6.66218 | -58.85478 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 2b21cbad-4d4a-38dd-912b-1e56275f0685 | -6.63036 | -58.85465 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 69efdaf8-c189-3c12-a326-3a596c89538f | -6.69021 | -58.84989 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aabc670f-8671-3961-a31f-7ad26db6a027 | -8.50296 | -64.04508 | 2025-07-26 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a6b9977-5ba2-363c-bbaf-c2bc71839aee | -6.63669 | -58.84228 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 8ca0efd3-fa8c-35e8-96c7-bd8dd402b1c5 | -8.52121 | -70.02316 | 2025-07-26 05:44:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 784125e2-ec99-3f98-8ad3-7b0d70026348 | -6.6469 | -58.83457 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 77212913-18e0-399c-a902-8393af1a1a2c | -6.68511 | -58.85364 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dd97a9da-ad61-305e-a32f-672b7c4cbffd | -6.652 | -58.83084 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 01708899-4682-35d3-89a7-9ffe0d530a0c | -6.55481 | -56.23865 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2843ba4a-535f-3a61-b91b-237abcfe23be | -6.55875 | -56.24949 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5c0960c-1467-3e7d-af36-aa37d59962f3 | -6.66601 | -58.82848 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 886267b4-d2fd-3c2c-9527-45b016f9dfa2 | -7.57087 | -61.40215 | 2025-07-26 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d565ba9b-b18b-3461-a196-73be85070870 | -6.6399 | -58.85157 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 71b979a1-632f-3eeb-a6bd-a2a537455c9e | -6.67047 | -58.82915 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3498fc1c-cadc-3c14-961a-58bda6ee63f6 | -6.55967 | -56.24279 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34173a11-348b-390c-b2cd-3dd734bfb185 | -10.04607 | -64.99065 | 2025-07-26 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fe10ad3-266e-3995-b83c-6b2ed59fc4f0 | -10.6453 | -68.73659 | 2025-07-26 05:46:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9595f845-44d7-32f0-a986-8ca75ec058f4 | -9.97088 | -64.9566 | 2025-07-26 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5ac2de90-e433-392c-a429-13c65f08be01 | -8.93346 | -71.25211 | 2025-07-26 05:46:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37d2459e-5c0d-3c8a-b036-ff6bdec90f59 | -11.95008 | -58.75961 | 2025-07-26 05:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58834034-ec4e-33dd-918a-5cdff5082a8c | -9.76253 | -65.09216 | 2025-07-26 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a468092-a3d9-3ab0-9352-2f7462bed718 | -10.1307 | -68.76836 | 2025-07-26 05:46:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b4670b2e-202b-3534-8b91-5573a6e80a61 | -9.97143 | -64.95302 | 2025-07-26 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c9195c0-0bf1-340a-8e17-4755e6e73952 | -9.52577 | -68.2959 | 2025-07-26 05:46:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39cb9c00-0ab3-3f31-b9ec-44de772c5836 | -11.0093 | -68.49951 | 2025-07-26 05:46:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c46ca68-5a9e-30e2-bf80-3d680ad74378 | -9.76088 | -65.09221 | 2025-07-26 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12daeffb-1d9c-34a5-9cbd-dd78be86f911 | -21.99571 | -57.60892 | 2025-07-26 05:48:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8cd1610f-e050-33cf-b364-7b065cd66433 | -21.99525 | -57.61414 | 2025-07-26 05:48:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6dfbf32f-a2fb-34b2-bb85-060a73200557 | -20.62599 | -54.83803 | 2025-07-26 05:48:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 803ecfa7-94ad-32b6-a19d-c7c9a794f232 | -20.61909 | -54.83748 | 2025-07-26 05:48:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08e53a40-8d0c-392b-9fd8-f37bb344eb51 | -22.00207 | -55.53072 | 2025-07-26 05:48:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b53e98a5-3599-3a33-96c7-d802340b006d | -18.2442 | -44.7767 | 2025-07-26 05:50:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 22a8f743-5d35-3411-ad7f-2b344791abb2 | -18.2435 | -44.8008 | 2025-07-26 05:50:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 134db27b-eff0-384a-8567-c0ed9ed8ec02 | -18.2442 | -44.7767 | 2025-07-26 06:00:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 6fc0aaeb-9aa5-3a59-b457-630d68b91928 | -18.2435 | -44.8008 | 2025-07-26 06:00:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 89dbe818-a661-3e3a-9423-94e43e6c2a69 | -6.67618 | -58.85954 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 1952657a-661f-3501-a8af-58109a174971 | -6.62409 | -58.83414 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| b632af23-9d78-360f-b178-fde7fa1a14d1 | -6.68001 | -58.84324 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 197a90c4-4d48-3c9f-801e-4cadee4bfa56 | -7.2865 | -60.1792 | 2025-07-26 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fe33938-4ab9-3651-b679-194e43b3ec89 | -6.62926 | -58.84747 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| a5c86990-d8ef-3812-848c-5fd9b0716eef | -6.68466 | -58.84818 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b72f2da8-0523-3fec-aa08-fe14c5b4a260 | -6.68715 | -58.82985 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README30.md)
