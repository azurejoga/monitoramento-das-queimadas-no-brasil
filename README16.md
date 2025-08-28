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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 612fba88-f7b9-3927-bb6b-c5174451cf88 | -9.1278 | -65.768501 | 2025-08-28 02:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64911de6-df04-3207-8334-f266308eb4af | -9.1123 | -65.748299 | 2025-08-28 02:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a96bf8b-3e26-30a8-8798-d65a77c6859f | -9.1375 | -65.765999 | 2025-08-28 02:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c8a9b171-1ad5-3980-a43a-a86897832fb2 | -9.1145 | -65.796204 | 2025-08-28 02:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba78ee59-738d-35b5-afed-5b90c363fdd4 | -9.1363 | -65.2835 | 2025-08-28 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 847e82d0-e4b7-32e6-9f85-1c2a5d222795 | -10.4738 | -57.9366 | 2025-08-28 02:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 51fd18fb-2264-3d78-842e-52db40de575c | -9.1155 | -65.7699 | 2025-08-28 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 357.8 |
| 52019a3c-48bf-3f6f-b309-a5ac15710b08 | -13.1837 | -45.2865 | 2025-08-28 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 55a3b86c-d29e-3120-8e89-5454a372b471 | -10.4736 | -57.9563 | 2025-08-28 02:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 889d0b96-a4e9-3b54-bb29-103bc50bc065 | -6.8774 | -43.5919 | 2025-08-28 02:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 9138363b-72e9-39e4-8db6-30f87d7e33b3 | -11.3334 | -43.5216 | 2025-08-28 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 56c7e71d-b10c-307b-a69e-ad80f95e1c5c | -7.3955 | -39.6845 | 2025-08-28 02:40:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 134.0 |
| 284185df-a695-3d7e-8c8a-e1975937244a | -11.3329 | -43.5452 | 2025-08-28 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 5cb606ad-44ac-3b17-9318-25703960a709 | -12.9662 | -44.5781 | 2025-08-28 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 977ad4f1-1ab6-315c-b84d-f867721d1292 | -9.1153 | -65.8073 | 2025-08-28 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 8e8e90c0-eeb7-3ef1-8465-4519c5902fb7 | -7.3357 | -59.6484 | 2025-08-28 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| ed40ceb8-a846-356d-a399-123dee797653 | -7.3765 | -39.6867 | 2025-08-28 02:40:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 51.4 |
| baaf6433-8dba-353a-ae52-c4f002e87237 | -8.9479 | -65.9616 | 2025-08-28 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 5a4a4e98-0f14-36a9-b7f7-fc7424261a54 | -6.896 | -43.6135 | 2025-08-28 02:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| ce7baebf-e2fa-30bd-a811-9b1f9102ee4b | -9.1154 | -65.7886 | 2025-08-28 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 620.3 |
| 0745c5a8-0b5e-370f-8f38-41a4b4c7f65c | -9.134 | -65.7694 | 2025-08-28 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 2f27e1b1-673d-345a-8ea5-4403c32e76e2 | -11.3521 | -43.5423 | 2025-08-28 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| be066bb0-6a6c-3d70-a125-21c741fff9ed | -4.7893 | -47.2614 | 2025-08-28 02:40:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| bb85bd7e-a8a4-3db9-b962-850930b27b98 | -6.8772 | -43.6152 | 2025-08-28 02:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 204.9 |
| b9436650-0cef-3685-aebc-f0b8812ed2b0 | -9.1339 | -65.788 | 2025-08-28 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 235.0 |
| 8e24d968-1ae6-3feb-bf5d-f8d9c0a6b122 | -10.5375 | -46.6894 | 2025-08-28 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 4c4dc152-e01d-3b68-9558-dc18c9dd6f3b | -8.9664 | -65.961 | 2025-08-28 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 815587fe-1638-3094-815f-a2e1d535e9a7 | -6.8772 | -43.6152 | 2025-08-28 02:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 1f73e758-cb07-3d63-b827-30ebd3b6ab50 | -7.3958 | -39.6595 | 2025-08-28 02:50:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 52.8 |
| d44240fd-995c-3ee6-92ea-55c33e153f1b | -11.3521 | -43.5423 | 2025-08-28 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 4c8655b6-cc3d-37e4-8257-6bf5eb28d4e1 | -7.4144 | -39.6823 | 2025-08-28 02:50:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 53.2 |
| 0c1d6f8e-6c34-3902-a740-0246cf8947e5 | -6.896 | -43.6135 | 2025-08-28 02:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| c1dbffe0-89bb-3cfc-bd20-362e70faa23c | -11.3334 | -43.5216 | 2025-08-28 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 02222012-dd72-3517-a6c6-85432ebf4176 | -10.4549 | -57.9576 | 2025-08-28 02:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 0cf5fc0b-247d-37ec-a72a-4662f2b93712 | -10.8236 | -60.7633 | 2025-08-28 02:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 4c9ac096-7578-304b-854f-8fcb54162daf | -6.8774 | -43.5919 | 2025-08-28 02:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| b1fe340e-c469-3a6f-9248-ce822be7c7f4 | -11.3329 | -43.5452 | 2025-08-28 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 646d9d45-93bd-3755-9369-5f8a9a8879b6 | -7.3951 | -39.7095 | 2025-08-28 02:50:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 63.3 |
| a4ef3d57-16f6-3bf3-b3a8-e3febed81856 | -8.9479 | -65.9616 | 2025-08-28 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| acb122c8-85b0-389a-875c-a992066d4f0e | -10.8047 | -60.7837 | 2025-08-28 02:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 823f6e39-0071-3983-876e-b7dabf215ee3 | -8.9664 | -65.961 | 2025-08-28 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 0d3cae24-0d10-3b9c-9109-34f120d5480e | -13.1837 | -45.2865 | 2025-08-28 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 89f199db-b69c-375a-b8d2-8a523b10e053 | -12.9963 | -56.9 | 2025-08-28 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 45f6953a-3314-3f5a-84b8-24f9a39abb7f | -20.3098 | -46.0226 | 2025-08-28 02:50:00 | GOES-19 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 3c36fa23-c88a-3201-affd-82be72f40683 | -7.3955 | -39.6845 | 2025-08-28 02:50:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 183.9 |
| a526b242-8409-3531-8e56-62fba62bbc35 | -12.9662 | -44.5781 | 2025-08-28 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| c0b47797-55f0-3284-ad23-4e1979748030 | -10.4738 | -57.9366 | 2025-08-28 02:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| c571b93a-00a4-3c46-954c-9e705248778b | -10.8235 | -60.7826 | 2025-08-28 02:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 0ea902c1-d18d-3dd9-b49f-ca2c3b903cb5 | -9.406 | -60.5711 | 2025-08-28 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| fc13b48b-9a43-30c9-a125-c8e0abb3750b | -6.9129 | -62.9366 | 2025-08-28 02:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| fb77b987-b5dc-34d5-9b7d-f44937dab112 | -10.4736 | -57.9563 | 2025-08-28 02:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 8477f292-1b7f-3815-a192-87ebba8f00d9 | -4.7893 | -47.2614 | 2025-08-28 02:50:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| d2c3ab11-8f44-35aa-9ae1-46c8a83d81cb | -10.8049 | -60.7644 | 2025-08-28 02:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 1677012d-3048-3d6b-ba26-9edfcc358345 | -11.3526 | -43.5187 | 2025-08-28 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 695c6b1b-41e1-3438-8680-133bd5c32acf | -11.3521 | -43.5423 | 2025-08-28 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 189784f4-b08d-3c60-a9f9-9bcaa2078be3 | -13.1837 | -45.2865 | 2025-08-28 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 8b5d8ecc-9fa8-315e-a221-ad51a72b74eb | -9.1153 | -65.8073 | 2025-08-28 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 8ec1bc58-c876-3802-8274-98c7a07b769f | -9.1155 | -65.7699 | 2025-08-28 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 242.6 |
| aaf21c53-4814-3e8e-91a2-d2bbd6fa611c | -11.3526 | -43.5187 | 2025-08-28 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 312d7212-ac2f-3af7-87e0-cb6f07ab2061 | -9.1154 | -65.7886 | 2025-08-28 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 319.1 |
| 212ff6be-6586-3c6f-b0fa-8a79e0838058 | -12.9963 | -56.9 | 2025-08-28 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 04826dba-f13c-3ef8-b722-81771f3b0e2c | -7.3951 | -39.7095 | 2025-08-28 03:00:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 74b7619a-f141-34ae-92c6-1617a9822d18 | -7.3958 | -39.6595 | 2025-08-28 03:00:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 58.4 |
| a1b0d4b9-194d-3c4a-bc94-ec7296f9d052 | -9.0969 | -65.7892 | 2025-08-28 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 9c8ecf8c-f748-30ad-91de-42f63845c0d0 | -10.8047 | -60.7837 | 2025-08-28 03:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| a5913d1c-0b3a-3300-a1e1-ce13fc2a6c50 | -10.4738 | -57.9366 | 2025-08-28 03:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 3e2826b4-03a5-3e78-9f8d-8545f3a1123e | -6.8774 | -43.5919 | 2025-08-28 03:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 4a57d16f-e71a-3d1e-91d8-104e7f526e38 | -6.896 | -43.6135 | 2025-08-28 03:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 72252bb4-44b2-3d90-843c-3cf148631273 | -9.406 | -60.5711 | 2025-08-28 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 8d8dccfc-2b3e-379e-bd84-53fb8318364f | -11.3329 | -43.5452 | 2025-08-28 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 58391f35-ce9a-311b-8a6a-fbff3b839632 | -10.4736 | -57.9563 | 2025-08-28 03:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a8b0295c-3b2c-3a78-af2a-370989e501db | -12.9662 | -44.5781 | 2025-08-28 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 91add7a8-6f39-32eb-93f8-9019da1fab08 | -20.3098 | -46.0226 | 2025-08-28 03:00:00 | GOES-19 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 487c0842-7e86-3ba2-9684-85eae49b2eb1 | -7.3542 | -59.6476 | 2025-08-28 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 3a9c3086-b96c-3f81-b31f-4156026c8301 | -7.3955 | -39.6845 | 2025-08-28 03:00:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 239.3 |
| 3997c8da-e98d-3a68-8f22-118da25fe315 | -10.8049 | -60.7644 | 2025-08-28 03:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 00e16e4b-6c15-3636-bf02-5d0f9361103a | -10.4549 | -57.9576 | 2025-08-28 03:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 153f2601-0478-3e72-915f-882d18935210 | -8.9479 | -65.9616 | 2025-08-28 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 3b4331d4-c3a8-3bc4-b726-ac6759245586 | -6.8772 | -43.6152 | 2025-08-28 03:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 6af8990a-b072-3e90-ba88-2540d2f886c9 | -9.1339 | -65.788 | 2025-08-28 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 277.8 |
| bf35cf51-d511-3da7-99a2-d39884c2c28e | -11.3334 | -43.5216 | 2025-08-28 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 776f94b7-998f-3dda-b9c5-69eeff4ca060 | -9.134 | -65.7694 | 2025-08-28 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 216.7 |
| 618c6b50-6740-3ac4-bdc0-bf85e2098575 | -10.4738 | -57.9366 | 2025-08-28 03:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| d445093a-9f7c-3041-90e4-2c01a2eb1f18 | -9.1154 | -65.7886 | 2025-08-28 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 317.0 |
| 27e2a206-d467-37e7-ac11-e4aba2f8c695 | -6.8774 | -43.5919 | 2025-08-28 03:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 9bbb697e-7db3-30bb-876d-fa00a944d34c | -9.1339 | -65.788 | 2025-08-28 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 225.5 |
| cbb93735-c3f1-30e4-ad62-744d02c01c52 | -9.134 | -65.7694 | 2025-08-28 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 4049c99f-d5a8-3870-b7aa-b4f601785b37 | -7.3951 | -39.7095 | 2025-08-28 03:10:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 61.8 |
| 42e138f0-e817-3749-9784-cf3f7aba4afd | -10.8236 | -60.7633 | 2025-08-28 03:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| a90d74e1-aaa9-3178-8a85-695f62fe8ba2 | -10.4736 | -57.9563 | 2025-08-28 03:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f81b27a8-58f8-377d-8371-16ffc6cc8047 | -8.9479 | -65.9616 | 2025-08-28 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c393056c-829d-3cf2-8a0c-c905c1c10f07 | -6.8772 | -43.6152 | 2025-08-28 03:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 192.7 |
| eef5e6f8-354e-33f0-9b0c-62297e713ac2 | -13.1837 | -45.2865 | 2025-08-28 03:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| da16a300-fa63-381d-8f03-7d558c3f1dd8 | -10.8049 | -60.7644 | 2025-08-28 03:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 3b1ea5ff-b1a0-3530-9562-54f67ba17aed | -7.3955 | -39.6845 | 2025-08-28 03:10:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 245.1 |
| b4a614ad-6a9e-30e6-967a-bbf74ca420c2 | -6.896 | -43.6135 | 2025-08-28 03:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 604821d4-e73d-3e70-a42e-56413d7fb266 | -9.1153 | -65.8073 | 2025-08-28 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 8e704569-c86e-36fe-bb8a-31bd472e1c36 | -12.9662 | -44.5781 | 2025-08-28 03:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 7f5ed19e-670e-3da8-b606-39606f8ae7f9 | -10.8047 | -60.7837 | 2025-08-28 03:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 2a559478-417b-3e67-a4ed-cfe9ab9190e6 | -9.1155 | -65.7699 | 2025-08-28 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 206.7 |


[Clique aqui para ver as próximas entradas](README17.md)
