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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 796a6621-ddef-30c1-8779-78f485910cd3 | -3.3891 | -41.6201 | 2024-11-01 14:05:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 96c7d97e-ca9a-3bf4-ac68-95f9378cd29e | -3.2535 | -50.3479 | 2024-11-01 14:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 0a93d16c-fa51-3102-a940-4f458e794daa | -3.2232 | -53.3769 | 2024-11-01 14:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 64076e15-a67b-3029-81a8-bc2bebf7aa6f | -3.272 | -50.3263 | 2024-11-01 14:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 95b037c0-a554-3947-8a29-0cec355d7d27 | -3.2416 | -53.3764 | 2024-11-01 14:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| af77f0cf-add3-3699-9c7f-e62e4379c408 | -3.2231 | -53.3972 | 2024-11-01 14:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 184.3 |
| c6e4300c-a585-37da-979b-1621f5f9da6f | -3.2535 | -50.3269 | 2024-11-01 14:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 2a910400-ab72-31c9-a36b-44143e483258 | -3.7703 | -43.5323 | 2024-11-01 14:05:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| c8846042-5712-347d-9a0c-db58753323ea | -3.8225 | -44.1522 | 2024-11-01 14:05:28 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 39b64635-84be-33e6-8c0f-81c7def1d87e | -4.2033 | -45.8538 | 2024-11-01 14:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 168.3 |
| e4574b8a-a83b-3f39-869c-6ec6be5b6715 | -4.4387 | -46.8624 | 2024-11-01 14:05:31 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| de281880-8017-3416-84fc-57125a601455 | -4.3869 | -43.4525 | 2024-11-01 14:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 1d77b9c3-02a5-3c84-8e47-a52c3fed0d2e | -4.4056 | -43.4514 | 2024-11-01 14:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 9699758a-e8fb-3d8d-9727-dd66c36ed16a | -4.4282 | -42.89 | 2024-11-01 14:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 3a5a10b5-119a-3955-80ce-21dc6dc5d5ff | -4.7373 | -44.0786 | 2024-11-01 14:05:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| f6935a25-c332-3f22-90d2-3ddb41a5987c | -6.9974 | -41.3016 | 2024-11-01 14:05:45 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| f293d0c2-3c42-3516-9be1-06ef0f8d52ce | -6.9971 | -41.3258 | 2024-11-01 14:05:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| fa0b4340-ab93-35b9-967b-fcedd98f7b7d | 3.4157 | -51.2606 | 2024-11-01 14:14:46 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 98f85d18-72a3-3bba-83ca-ebb3de3aa04a | 3.4342 | -51.2601 | 2024-11-01 14:14:46 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 0054f612-f747-34f6-86e2-300e89d8f630 | 2.58 | -60.6973 | 2024-11-01 14:14:51 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.3 |
| bcc7c2f0-b644-34f0-8937-4fce0af90943 | 1.796 | -50.4467 | 2024-11-01 14:14:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 67.3 |
| cf2a2235-17d4-3c6e-9304-9cd13299840b | -0.6896 | -51.6847 | 2024-11-01 14:15:10 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 09ece0df-41f4-35a2-bbe7-f5e0fae0c841 | -1.4244 | -52.1913 | 2024-11-01 14:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| f0a3666d-0220-3f53-9461-802e2e5cfbe2 | -1.406 | -52.2121 | 2024-11-01 14:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 2516fdc0-4a73-3101-b6b1-555a4d9ad3dd | -1.4244 | -52.2118 | 2024-11-01 14:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 117.3 |
| fd7166d4-ea95-35d8-9e55-107ead158607 | -1.4426 | -52.273 | 2024-11-01 14:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| e4e6a17a-200b-3da0-9372-b864b9a5730b | -1.5535 | -51.9845 | 2024-11-01 14:15:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 01f52a3c-53d2-3d0c-8adb-816615c46289 | -1.5532 | -52.1076 | 2024-11-01 14:15:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 40ca2407-29bb-3d91-a034-f42aac3f287b | -1.6079 | -52.3935 | 2024-11-01 14:15:15 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 218ed5da-3eb9-3cf9-8b8f-5ce36090e6af | -1.6079 | -52.3731 | 2024-11-01 14:15:15 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| bed07cee-15ba-37d0-9b6d-ebb79fba31ae | -1.7366 | -52.3507 | 2024-11-01 14:15:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 23480017-f77a-30bf-a987-f3f35c67251c | -2.305 | -46.8352 | 2024-11-01 14:15:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| d52c6719-3962-3428-8f97-072b1bf6ea03 | -2.3545 | -48.678 | 2024-11-01 14:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 2de885f8-d185-3e61-b311-d1639eac5309 | -2.3444 | -46.127 | 2024-11-01 14:15:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 8a583a6a-af33-320a-bc68-b1a53ff6f9ed | -2.2499 | -46.6606 | 2024-11-01 14:15:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| d8a1e131-23fd-3784-ab35-f8a94263c506 | -2.2864 | -46.8357 | 2024-11-01 14:15:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| fbc5aaa4-dbc0-3c80-b5a5-a217dd44a52f | -2.2685 | -46.6601 | 2024-11-01 14:15:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| a01a9023-91d0-3301-9e9f-68f4c5e29653 | -2.4344 | -46.8976 | 2024-11-01 14:15:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| e0919101-4cfb-3edc-9696-642d8ee817c4 | -2.5377 | -49.1431 | 2024-11-01 14:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 1aa58203-b287-3082-9998-a01f2d3fe766 | -2.676 | -46.7365 | 2024-11-01 14:15:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 76dfd860-800b-3846-aac6-a49baa490969 | -2.836 | -48.4501 | 2024-11-01 14:15:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 0be312a0-6326-32be-924a-2a966f84e94c | -2.8361 | -48.4286 | 2024-11-01 14:15:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 0906b627-471d-373a-8fa1-93bc84de92e4 | -2.7961 | -49.2211 | 2024-11-01 14:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| ba0d7467-1c7a-3bdf-8a98-08579f5a85b9 | -2.9354 | -46.7722 | 2024-11-01 14:15:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| cd3f1526-ebea-3bf4-b35e-5943d8b5650b | -3.0539 | -49.4683 | 2024-11-01 14:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| b5df5e86-c41b-35d8-8349-624d00a2a1a1 | -3.0538 | -49.4895 | 2024-11-01 14:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 901eccf6-ad3f-348a-bcaa-b228836468f4 | -3.2535 | -50.3269 | 2024-11-01 14:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 7bbefcd8-aa75-314d-9c7c-090a88cbdad9 | -3.2231 | -53.3972 | 2024-11-01 14:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 256.4 |
| f85425ae-3899-324f-99f1-12dda5790643 | -3.272 | -50.3263 | 2024-11-01 14:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 286ac735-1e11-327c-bad8-8058f059b052 | -3.2611 | -53.0717 | 2024-11-01 14:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| f6e649a8-f87f-35e1-8b4e-9fbf67b08f03 | -3.4304 | -44.308 | 2024-11-01 14:15:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 4553b7d2-7293-332c-8eb2-1bbd214d47a2 | -3.2232 | -53.3769 | 2024-11-01 14:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 4e2fe423-ea2e-3977-be73-d649583bdd66 | -3.2535 | -50.3479 | 2024-11-01 14:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 2e87e0cb-af7b-3942-b266-569d9085fc04 | -3.5762 | -44.8935 | 2024-11-01 14:15:26 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 098f5880-6282-3c57-9fcb-8b20b5bfff0a | -3.7703 | -43.5323 | 2024-11-01 14:15:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 13f8db73-c984-3e09-94f6-0a295f592b87 | -4.3869 | -43.4525 | 2024-11-01 14:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| e1ab7c8f-2567-37db-85de-89b7fd7c12e4 | -4.4056 | -43.4514 | 2024-11-01 14:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| d09e43ba-e2f2-3bda-b5f0-23b69c396b2c | -6.9971 | -41.3258 | 2024-11-01 14:15:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 89aadb8c-f2d3-355e-ad21-4c890dabe4fd | -6.9782 | -41.3277 | 2024-11-01 14:15:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 21a347ec-7c8f-3856-a4b9-2efaac3bbba1 | -7.0157 | -41.3481 | 2024-11-01 14:15:46 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 1682df83-029c-3c41-b767-3e19cc015b17 | 2.58 | -60.6973 | 2024-11-01 14:24:51 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.1 |
| e007fbc8-13c6-3069-9f8b-4db0c7417fc6 | 1.796 | -50.4467 | 2024-11-01 14:24:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 73.4 |
| b54ac0ab-9912-37d4-84c2-631e00d73e16 | 1.0767 | -50.9572 | 2024-11-01 14:25:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 72e97d04-43d8-3af7-b527-94f0c2da9040 | 0.3221 | -50.8167 | 2024-11-01 14:25:04 | GOES-16 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 74.6 |
| f42de1be-fcca-3ae4-9ec5-a57f5f24811b | -0.6896 | -51.6847 | 2024-11-01 14:25:10 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 8b3f0fe1-ab19-300c-8180-78a042f0e757 | -1.4244 | -52.2118 | 2024-11-01 14:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 1cf68cea-7810-34a8-8966-b2ab552b7e66 | -1.4426 | -52.273 | 2024-11-01 14:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| ce3eec6b-f7b3-3ff1-9dfb-2ee57f12719d | -1.406 | -52.2121 | 2024-11-01 14:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| c9c350be-be29-3b6a-8612-414de889d939 | -1.4244 | -52.1913 | 2024-11-01 14:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| f0d454e1-6cd2-3ec8-b5d5-9abef2553d55 | -1.5532 | -52.1281 | 2024-11-01 14:25:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| ce29be0d-5a0a-3576-824c-e45b29991a33 | -1.5535 | -51.9845 | 2024-11-01 14:25:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| eebf3eff-072b-32de-803f-faf942e10701 | -1.6079 | -52.3731 | 2024-11-01 14:25:15 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a80b30ea-5d7b-3bf5-a17a-a290dc85e0dd | -1.6079 | -52.3935 | 2024-11-01 14:25:15 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 34e07ee6-6511-3aa7-b0bb-a59e6befc0c9 | -1.5532 | -52.1076 | 2024-11-01 14:25:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| f9f4c794-3b76-37bb-96a9-c3ddd9caf89d | -1.7366 | -52.3507 | 2024-11-01 14:25:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b6ef3e04-8abf-38f6-855b-40c4460b4899 | -2.1563 | -53.6838 | 2024-11-01 14:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 7b7ceb05-8c06-3e89-a202-902f5a168223 | -2.1563 | -53.6636 | 2024-11-01 14:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 9955afb1-34e4-34ed-b14d-5bcc061c7230 | -2.1695 | -48.7252 | 2024-11-01 14:25:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 969e7733-fbdb-395a-b547-c664f64d7cb4 | -2.2499 | -46.6606 | 2024-11-01 14:25:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| b070e42d-179d-3154-aff3-b64794a418e3 | -2.3444 | -46.127 | 2024-11-01 14:25:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 96.8 |
| e9bdc629-a07d-3086-ab57-cff38b126974 | -2.3537 | -48.9133 | 2024-11-01 14:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| a74ece66-617b-3b93-bd2d-e69af0c6f2d3 | -2.3545 | -48.678 | 2024-11-01 14:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 26c67f8f-8fba-3c3f-9474-8e8f2f8538bf | -2.2134 | -46.5071 | 2024-11-01 14:25:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 991e8e96-0723-3c50-86dc-27dc2a30839d | -2.5192 | -49.1649 | 2024-11-01 14:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| de37e808-878d-32bb-b8d0-e3a9e4926e41 | -2.5377 | -49.1644 | 2024-11-01 14:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| ae0c33e7-cc02-39f1-bbdb-c7c19efde168 | -2.5377 | -49.1431 | 2024-11-01 14:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 169.8 |
| 9fffefdb-9352-3959-8f0f-60cfbd601cc5 | -2.676 | -46.7365 | 2024-11-01 14:25:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 0148af0a-34b3-34c7-b00e-8d65035cbd4a | -2.7961 | -49.2211 | 2024-11-01 14:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 85af1eb0-2d35-39f6-8b5b-37ad434f4cab | -2.8722 | -48.6636 | 2024-11-01 14:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 2d15634b-386e-3267-9b89-84b6648fd932 | -2.836 | -48.4501 | 2024-11-01 14:25:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 43022323-b9d8-38ab-9631-aaf21e25aa94 | -2.8754 | -52.8989 | 2024-11-01 14:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 8008ac8d-4192-361a-a213-166a422d219e | -2.9094 | -48.6196 | 2024-11-01 14:25:23 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| f976f24d-ab72-3c07-aa51-8ebdbebb5668 | -3.2047 | -53.3977 | 2024-11-01 14:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 0a50c2ad-fa13-3d2d-bc4c-ad38c434e701 | -3.2535 | -50.3269 | 2024-11-01 14:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 09a19bd7-2770-32fb-9e8a-e19daa6961cc | -3.2231 | -53.3972 | 2024-11-01 14:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 277.3 |
| 5e53edf2-7ae4-3170-aa32-61c4a83d72c6 | -3.3891 | -41.6201 | 2024-11-01 14:25:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 101.1 |
| 3edc1d7f-d6d4-3158-b853-6b1f152515e8 | -3.2535 | -50.3479 | 2024-11-01 14:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 338551ec-114c-381e-a924-26610289f874 | -3.2232 | -53.3769 | 2024-11-01 14:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 7aec3191-0d8d-3c92-98e1-b4a7b6787ea5 | -3.4078 | -41.6192 | 2024-11-01 14:25:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 5aa9e2c0-dc1a-3d28-be32-c479f536c4fe | -3.272 | -50.3263 | 2024-11-01 14:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |


[Clique aqui para ver as próximas entradas](README62.md)
