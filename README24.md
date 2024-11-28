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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16570368-e04d-3c08-b496-2d02fd8055a7 | 1.2538 | -55.927 | 2024-11-28 02:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 8bebbebd-a0de-3ce9-b165-752758320760 | -1.5713 | -52.2713 | 2024-11-28 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 3c5032a2-78bd-31ee-80fd-7845c6fda13d | -3.0929 | -53.8247 | 2024-11-28 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| bc65dec7-25b3-3144-ab3d-6e0c3bd9bb7b | -4.0899 | -46.1493 | 2024-11-28 02:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| b5729124-e554-3c35-811c-0d8b1239340a | -5.9788 | -45.3621 | 2024-11-28 02:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 2d87dae1-be5a-391f-a054-d20225c3758b | -6.0862 | -48.0339 | 2024-11-28 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 1fa95f99-01b3-3a51-9b86-26598c32fa85 | -5.979 | -45.3395 | 2024-11-28 02:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 684d18d1-26c4-3e71-ac3f-e5796f5fba37 | -2.7234 | -48.9034 | 2024-11-28 02:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 835a9e99-82fb-333c-a0ed-315ac2ca776f | -3.3837 | -50.1125 | 2024-11-28 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 4b2786eb-3a90-3217-9cd7-ba1d33f8cd92 | -3.9674 | -48.0851 | 2024-11-28 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 685fe305-b61e-3591-8e5f-9c66c1a1523b | 1.2537 | -55.9467 | 2024-11-28 02:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 834ae06b-4402-3840-9e24-150eb3c0d3d0 | -2.8609 | -46.8626 | 2024-11-28 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| dc981808-901d-3d0c-9a40-a46bf814e30a | -1.3329 | -51.9463 | 2024-11-28 02:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 6a5b267f-9dc6-324b-8726-1ecf9df1b880 | 1.2537 | -55.9664 | 2024-11-28 02:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| ae105e94-c813-3f5e-8996-f30e8da50daf | -2.5963 | -53.9771 | 2024-11-28 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 47f87647-9829-3cff-8c8c-2fa0ba0224f3 | -2.861 | -46.8406 | 2024-11-28 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 9e166bb3-8291-3741-af71-63ed668ed8b2 | -1.6812 | -52.4742 | 2024-11-28 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 054dc02d-666d-390f-a21a-99bdedf3727a | -9.9126 | -36.2093 | 2024-11-28 02:40:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.9 |
| fa52cf6d-4969-3ac6-9623-e88effb8bbd5 | 1.2538 | -55.927 | 2024-11-28 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 805e81fa-d2cf-3c86-98f5-b50316d5c421 | -5.979 | -45.3395 | 2024-11-28 02:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 4cc6d127-2c7f-3d52-ad64-a66c3c197272 | -1.6629 | -52.4744 | 2024-11-28 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 3c6702b1-3494-391b-b70f-1c08d89f9b2a | 1.2537 | -55.9664 | 2024-11-28 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 95709089-06b3-3e23-8962-7cd484df7049 | -1.6445 | -52.4747 | 2024-11-28 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 74fdf49d-4701-3332-9519-ed54b5df4fcb | -5.9788 | -45.3621 | 2024-11-28 02:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 166.5 |
| e4004693-90ac-3950-9514-b8228aa1353d | -2.7234 | -48.9034 | 2024-11-28 02:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0bfde103-a37c-30b0-aebd-1697a26fa069 | -3.1113 | -53.8242 | 2024-11-28 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 618038b7-c0aa-3815-b184-4ac89ef58511 | -1.3329 | -51.9463 | 2024-11-28 02:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 5083114c-949d-33f6-abf8-b66312e287ae | -6.1041 | -43.9593 | 2024-11-28 02:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| d63e98ce-c4c6-3e31-ad79-26bd53b53ec4 | -2.7419 | -48.9029 | 2024-11-28 02:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 270fa7fd-ec7c-3f83-8d81-ea8339b86c56 | -3.3838 | -50.0915 | 2024-11-28 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 906c6ea4-ba7e-34ef-8bb7-ac26bd599f0a | -4.0899 | -46.1493 | 2024-11-28 02:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| d3cef239-483b-3c1d-91dc-7a4a1aab89a1 | -1.6812 | -52.4742 | 2024-11-28 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e3323f61-6466-395a-a452-fd3ab5215b57 | -3.3837 | -50.1125 | 2024-11-28 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 134.7 |
| e82f75cb-a20b-3115-938e-2ce00406728a | -2.8609 | -46.8626 | 2024-11-28 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d44b783f-2c79-3dc1-b013-a8f4b08da2fc | 1.2355 | -55.9272 | 2024-11-28 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| a1ed2b02-c209-3bef-86ae-824a51d7971e | -5.9975 | -45.3607 | 2024-11-28 02:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| d2d81fbc-920c-3dfc-8af4-9588f257612c | -3.0929 | -53.8247 | 2024-11-28 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 32bf94ed-301d-39b0-9342-70b13a8a0ffb | -2.5963 | -53.9771 | 2024-11-28 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e8750f00-b4a2-331b-a44f-54dc92dd1a38 | 1.2354 | -55.9469 | 2024-11-28 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 53cdd750-821f-31f1-9157-28b210c4ca67 | -2.861 | -46.8406 | 2024-11-28 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| fc025b38-66bc-3603-a671-bece4e45c634 | -1.3329 | -51.9257 | 2024-11-28 02:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 251d4f2c-61c2-3784-8d6d-0ca7b91a78e0 | -3.093 | -53.8045 | 2024-11-28 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| d2218bfb-1d2c-3918-aaaf-8c31223d44da | -1.6445 | -52.4543 | 2024-11-28 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 686ced98-3419-3f16-89d0-c81a18977f64 | -1.6812 | -52.4946 | 2024-11-28 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 3ad951a8-7bd2-321f-87d5-b67f31d9b3e9 | 1.2537 | -55.9467 | 2024-11-28 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 96a28e79-e0e7-3430-84ba-08c980e669a2 | -1.5713 | -52.2713 | 2024-11-28 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| db34d37d-9302-347a-9caf-9756047e2684 | -2.8794 | -46.862 | 2024-11-28 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| eca07b69-9aad-316b-bc41-2192abfa65e9 | -1.5897 | -52.271 | 2024-11-28 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| e9a86e0b-8409-3f94-ae0c-9e32ac5eb829 | -9.12282 | -35.65726 | 2024-11-28 02:45:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| ebce2e57-5f40-32aa-a038-2e81f30a9ea5 | -9.12491 | -35.65909 | 2024-11-28 02:45:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| abc9125f-3c0d-33f0-b9de-bed9fb2701ee | -9.12156 | -35.66356 | 2024-11-28 02:45:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 6ea13221-4453-3408-aa21-b5824a7680d2 | -6.66017 | -34.97773 | 2024-11-28 02:45:00 | NOAA-20 | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| b52b2d1e-90e7-3eb9-a6e9-dfaaf68c689f | -7.46149 | -35.24129 | 2024-11-28 02:45:00 | NOAA-20 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c22efcc9-b4df-3954-ba1a-e191494d8ffd | -3.3837 | -50.1125 | 2024-11-28 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 190.6 |
| 4fe3ed4f-6332-3fb7-8447-af849f03f6c5 | -1.3329 | -51.9257 | 2024-11-28 02:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 8990b1f7-50ec-37d1-b8e7-cc9109c900d3 | -2.861 | -46.8406 | 2024-11-28 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| fafb15ed-81ff-3852-815e-6e121bc4f00d | -4.0899 | -46.1493 | 2024-11-28 02:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 3450597f-2b21-3333-b3c7-759dd04e15df | -2.8794 | -46.862 | 2024-11-28 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 1788d134-5b68-31cc-90c3-dd4db317e0d0 | -5.979 | -45.3395 | 2024-11-28 02:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| bc32a44a-c66f-3b56-8d53-e5c49b53555b | -1.3329 | -51.9463 | 2024-11-28 02:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| cfba18bf-fa14-3166-ac27-64ddf65b16f8 | -1.6445 | -52.4543 | 2024-11-28 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 4d5d2495-ff31-317c-96c4-042f9873c9fd | -1.5897 | -52.271 | 2024-11-28 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| df879e7f-e377-31b9-a71f-a62273ae6aa1 | -6.5216 | -35.194 | 2024-11-28 02:50:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 86.9 |
| 491dd36a-4587-343f-a720-79afe0ed592f | -2.8609 | -46.8626 | 2024-11-28 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 9a92fd25-2834-3ae4-a9d6-aa240b8a14ac | -2.7234 | -48.8821 | 2024-11-28 02:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| b976b3dc-b056-32ed-bedb-3a2a11b1febe | -5.9975 | -45.3607 | 2024-11-28 02:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 148478e2-07a2-3539-829e-be684d263eee | 1.2538 | -55.927 | 2024-11-28 02:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 625af13c-bf45-39a5-92f8-f2d649960193 | 1.2355 | -55.9272 | 2024-11-28 02:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 54612823-c1cb-33b2-a2f0-c31abd52a719 | -1.6812 | -52.4946 | 2024-11-28 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| ef4f9f36-b6dc-3836-b1c7-101ae287aeee | -3.4022 | -50.1119 | 2024-11-28 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 99c53930-f8a2-3983-a386-849c3f1c3149 | -6.1041 | -43.9593 | 2024-11-28 02:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| adf84ba5-3f11-3364-b540-01a1b0ffa216 | -1.5713 | -52.2713 | 2024-11-28 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 1bc1ce97-da6c-316d-8601-8f1c275df86d | 1.2537 | -55.9467 | 2024-11-28 02:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| cf8bfb0b-f8d9-3376-b745-0b9cbf5b6bf6 | -3.3838 | -50.0915 | 2024-11-28 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 5615551b-3bcb-388e-a69d-72dfd442c6b9 | -3.1113 | -53.8242 | 2024-11-28 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 43a83866-795d-3437-a0df-7a15e8a91e3f | -5.9788 | -45.3621 | 2024-11-28 02:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 166.4 |
| e2ca4847-33ef-32ac-b30a-4925a86aefc1 | -6.5407 | -35.1917 | 2024-11-28 02:50:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 64.9 |
| 8cb3f88b-ed47-30ce-893d-f743d00472ff | -3.9674 | -48.0851 | 2024-11-28 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| fd5c50f1-02f5-36c0-bce0-b423180afea6 | -2.7234 | -48.9034 | 2024-11-28 02:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| e3532d22-a558-3bfc-b8bb-3c926f19738a | 1.2537 | -55.9664 | 2024-11-28 02:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ef22e07c-5ece-3acd-a4ce-b9483338a3c9 | -6.522 | -35.1666 | 2024-11-28 02:50:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 72.8 |
| 01acc1bb-40ad-3aac-b3d3-99686193b6a9 | -6.0862 | -48.0339 | 2024-11-28 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 15a8a636-8c67-3f54-82d0-ed36c60b7dd4 | -3.3836 | -50.1336 | 2024-11-28 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| b1419709-e0fd-335f-add4-bdc412b8cd72 | -2.8609 | -46.8626 | 2024-11-28 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 5caebb46-e508-3307-88de-65c9a0d0447c | -1.3329 | -51.9257 | 2024-11-28 03:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 7854a802-f03f-30c1-b231-beef3f7aacad | -2.7234 | -48.9034 | 2024-11-28 03:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 0ea0c27a-07b5-38be-a635-7d62f28159bc | -5.9975 | -45.3607 | 2024-11-28 03:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| a9c3f475-0499-30d1-bc2e-cf2e53f7e066 | -4.0899 | -46.1493 | 2024-11-28 03:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| f10183fa-a36e-36b9-858b-a8ee27e39da7 | -6.1041 | -43.9593 | 2024-11-28 03:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f3447e8b-1234-3ec8-8e10-963048b8748a | -3.3837 | -50.1125 | 2024-11-28 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 177.4 |
| 62c4b3da-a63b-3bd2-b90f-4cbf835fc713 | -6.0862 | -48.0339 | 2024-11-28 03:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| ccb00060-d71d-3a52-95ab-23224cc9439e | -3.3836 | -50.1336 | 2024-11-28 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| b70d3123-7dd8-3bcd-bf4c-c4a7035f639b | -3.3838 | -50.0915 | 2024-11-28 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 82efc528-5ba0-3800-b7c5-2f297efc9ccd | -4.09 | -46.1271 | 2024-11-28 03:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 46.8 |
| a37cb75b-3377-3ebe-85e9-f137b3e632bf | -1.6445 | -52.4543 | 2024-11-28 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| d4111cd7-2d3c-3f46-9de1-d2e4aa6e28a2 | -5.9601 | -45.3635 | 2024-11-28 03:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 38f387ea-a565-3699-88af-0a61f155fb68 | -3.9674 | -48.0851 | 2024-11-28 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| fcdfc216-73a6-3c61-aa31-e61ef3cbb384 | -1.3329 | -51.9463 | 2024-11-28 03:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| cc97e99a-9d1a-3d66-a75d-24d0698bb45a | -5.9788 | -45.3621 | 2024-11-28 03:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 4858b5ba-9c08-3655-8639-fdbe6ffab1a7 | -1.5897 | -52.271 | 2024-11-28 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |


[Clique aqui para ver as próximas entradas](README25.md)
