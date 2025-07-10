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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2eec1b5-57c7-3df3-8140-89b6bdeaebb7 | -11.78153 | -64.98387 | 2025-07-10 05:46:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0903bd9-c8ca-3183-bd92-41f7a3d405fb | -9.99806 | -65.30659 | 2025-07-10 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c72c5ed9-ec59-3ae6-ba59-08a0e11b4a8e | -12.0314 | -62.52765 | 2025-07-10 05:46:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2a6dd19-e86e-3a0d-b3cf-64c6fcb3fecc | -11.87746 | -58.71666 | 2025-07-10 05:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 240ee5d0-d916-3143-9239-db624612c3c5 | -18.65098 | -55.72416 | 2025-07-10 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f6ec71d2-9105-37ca-ae7a-0d5e1bd03722 | -12.10114 | -64.24854 | 2025-07-10 05:46:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9c24454f-19b5-3b19-9ca0-238ff88f2208 | -13.34781 | -52.89583 | 2025-07-10 05:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e09e590c-eca3-36ed-8287-c3fb4fa5bbae | -18.64614 | -55.71856 | 2025-07-10 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 69e662eb-0a10-3abb-9b41-4310520bec18 | -13.34631 | -52.91015 | 2025-07-10 05:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48048fe1-fde8-3181-a22b-e136977fd0df | -13.34066 | -52.89475 | 2025-07-10 05:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 288e9962-7089-3148-9d5e-8eb318b6b418 | -18.64454 | -55.72351 | 2025-07-10 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 741918df-0e31-3cc0-b82f-f796da95a4f0 | -18.64506 | -55.71803 | 2025-07-10 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a7b4577e-1d18-3fd5-ba13-846bc747127f | -12.10577 | -64.02268 | 2025-07-10 05:46:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7d7b970-a4cf-3ef3-8e13-a41f7f5c539a | -11.32751 | -55.21413 | 2025-07-10 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fe57df2-f92c-3906-ae5a-05d9395791b3 | -12.0276 | -62.52706 | 2025-07-10 05:46:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c467c9ce-d4d0-307c-9eac-9b7909692359 | -12.09474 | -64.24355 | 2025-07-10 05:46:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c4b9c38-6566-32de-aaf5-3f3283d709e1 | -12.10172 | -64.24464 | 2025-07-10 05:46:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 481f5f98-5ebc-339d-9a75-adee4360eac0 | -11.78097 | -64.98756 | 2025-07-10 05:46:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2ce975a-1746-3b5f-af67-aa161dd4ea2c | -12.09823 | -64.24409 | 2025-07-10 05:46:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa36c82a-01b9-3370-941b-f2694e9fd9db | -13.34141 | -52.88758 | 2025-07-10 05:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ed397c0-ee1b-37f5-a27f-d6d46ef935c5 | -21.43912 | -54.57163 | 2025-07-10 05:48:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4ff205b-c160-3e0e-8a7e-7f6e971cfdba | -21.44344 | -54.57657 | 2025-07-10 05:48:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66645809-6f31-34d1-80c8-57c7689f6abf | -21.43685 | -54.56894 | 2025-07-10 05:48:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 469ead95-9c39-3b27-8d43-2b0a0ac7124d | -8.5022 | -43.3085 | 2025-07-10 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 188.8 |
| 7bc46e3c-2a6a-3e63-b729-8c7f2316b489 | -8.5214 | -43.2828 | 2025-07-10 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 66e130ea-281d-3c7a-8a08-63c779929655 | -8.5018 | -43.332 | 2025-07-10 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| f5a56cd2-bd9b-356f-8509-5b37a4d4a6e0 | -8.5211 | -43.3063 | 2025-07-10 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 7bec98a2-b58a-3b55-8737-a4136a0bf6d1 | -10.5773 | -49.1533 | 2025-07-10 05:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 471beb00-ee6b-35b3-a140-2c54812d9669 | -10.5776 | -49.1316 | 2025-07-10 05:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| b9901c32-9a57-3076-9e29-f7d37aad7fea | -8.5025 | -43.285 | 2025-07-10 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 137.8 |
| a18bb24b-cd89-30f6-b8fb-a95f39498dc5 | -10.5773 | -49.1533 | 2025-07-10 06:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| da2b7376-892e-3200-9e9b-60237ce87006 | -10.5776 | -49.1316 | 2025-07-10 06:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| d7417c5b-aa78-38ae-aea1-6f8b94ef2b0f | -8.5211 | -43.3063 | 2025-07-10 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 0ca4beab-9854-33bf-aa3b-48ca016ea6b8 | -8.5214 | -43.2828 | 2025-07-10 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.6 |
| 80359dc9-7c7e-343c-a996-9a2b1718b853 | -8.5018 | -43.332 | 2025-07-10 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 6f036884-0ed5-3592-8456-7a077b9c7b54 | -8.5025 | -43.285 | 2025-07-10 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 141.9 |
| 798fe312-41de-3b8c-8d19-46096c9d5660 | -8.5022 | -43.3085 | 2025-07-10 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 170.2 |
| eb6b673a-c83d-3dcc-92cf-20001c6ec09b | -12.09963 | -64.24703 | 2025-07-10 06:08:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cedd106-8cfc-3531-add7-b4a911c99081 | -12.09923 | -64.25022 | 2025-07-10 06:08:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bafb0aea-aecf-39ca-975a-042db9dd443a | -12.10612 | -64.02366 | 2025-07-10 06:08:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e78dd0d8-5764-3594-897e-6816437435f1 | -12.10522 | -64.24457 | 2025-07-10 06:08:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfe3cd74-9424-3ebe-a7b2-365d27931544 | -9.08929 | -68.47944 | 2025-07-10 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b71ecb9-de14-3fc0-b9ba-950ae9a51f88 | -12.1114 | -64.02435 | 2025-07-10 06:08:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8caa347-eee3-3414-ba44-1fe9951580a6 | -12.10482 | -64.24776 | 2025-07-10 06:08:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bcb94a7-9bd3-31c3-a968-007c356c4f2a | -7.83931 | -72.90623 | 2025-07-10 06:08:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8fa68fc-bb79-3162-ae84-9695352b2176 | -11.78144 | -64.98782 | 2025-07-10 06:08:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4691bb0-ec36-3821-bb51-c303d02d592d | -12.02639 | -62.52833 | 2025-07-10 06:08:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 144a0dd4-9afe-3cef-9586-9d80de4ecc81 | -12.10003 | -64.24387 | 2025-07-10 06:08:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3cd6514b-7c80-32ad-b130-9bb6850fe5cb | -8.69727 | -64.12091 | 2025-07-10 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73d032a5-2d64-3eb3-b4d5-f7b64ed36ac9 | -7.91578 | -70.92674 | 2025-07-10 06:08:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 925798bf-34dc-3f30-bdb1-bc6fa48fc21a | -12.09443 | -64.24634 | 2025-07-10 06:08:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07902682-c078-3315-a7f1-f20612abef8e | -10.5583 | -49.1554 | 2025-07-10 06:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 7750ba04-f522-317b-987d-53b08f17d7cc | -10.5776 | -49.1316 | 2025-07-10 06:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 0ece86ec-22fb-3ad8-96f5-5732d716f9be | -8.5018 | -43.332 | 2025-07-10 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| 68360764-89a8-364d-a395-2aa0641404aa | -8.5211 | -43.3063 | 2025-07-10 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 795ff3a1-46c4-3482-8096-0e343f4c0403 | -8.5214 | -43.2828 | 2025-07-10 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 25c06fe7-7c45-3e52-8b19-0aea3228678c | -10.5773 | -49.1533 | 2025-07-10 06:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| e25e31cc-6902-34ce-aa7d-7ed860f379b0 | -8.5025 | -43.285 | 2025-07-10 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 138.9 |
| 0ecc43fe-1114-3109-8fa4-4ceea518463a | -8.5022 | -43.3085 | 2025-07-10 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 167.8 |
| 68294756-e9bb-38e2-9deb-5213262436d4 | -8.5211 | -43.3063 | 2025-07-10 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| abe83257-bd15-3832-941e-57bf78799578 | -8.5025 | -43.285 | 2025-07-10 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 122.2 |
| ac21181a-9c65-34a1-bcb3-c36b4ebb5fdd | -8.5018 | -43.332 | 2025-07-10 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 65e42923-7582-3731-b5f4-c73e72d7dfec | -8.5208 | -43.3298 | 2025-07-10 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.7 |
| f3d98a68-196d-3863-9843-0275bf7fbb3d | -10.5773 | -49.1533 | 2025-07-10 06:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 0245bccb-04ff-310d-9a01-e5b1d1c18eb3 | -8.5022 | -43.3085 | 2025-07-10 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 151.5 |
| 6ef1f87b-7b50-36a0-b858-a4bbee341cb9 | -10.5776 | -49.1316 | 2025-07-10 06:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| ea08b951-ed67-36b4-a93f-f30fb147fa0c | -8.5214 | -43.2828 | 2025-07-10 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.2 |
| 160a7d7f-0e75-3c20-8399-c30517967876 | -8.5025 | -43.285 | 2025-07-10 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 138.8 |
| 8f6d01eb-84d1-3568-bd92-757e18ea72d9 | -8.5022 | -43.3085 | 2025-07-10 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 195.2 |
| 229f3ba1-a8bb-3d49-9f73-cb0c51bda0a0 | -8.5018 | -43.332 | 2025-07-10 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 30d365d5-e37b-3589-8316-b32388ca5e96 | -10.5776 | -49.1316 | 2025-07-10 06:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| a1d9c97e-a403-3428-b877-f597541b6e5a | -10.5773 | -49.1533 | 2025-07-10 06:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 8d1aaf34-bf8c-3a90-91ed-ed5b3c722d78 | -8.5211 | -43.3063 | 2025-07-10 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 373b34a0-6b2b-3ca8-bc7d-aac61471bfda | -10.5776 | -49.1316 | 2025-07-10 06:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 58a64456-df7b-34bc-8c39-6ce32b5dc676 | -8.5018 | -43.332 | 2025-07-10 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.2 |
| 0eee1bc0-8bf3-395a-b612-663cd276aef6 | -8.5211 | -43.3063 | 2025-07-10 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 00900b71-a266-325a-9ad3-4110479a6847 | -8.5022 | -43.3085 | 2025-07-10 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.4 |
| ab76a2ff-a9c5-3dc6-af29-974e6fdf7522 | -8.5025 | -43.285 | 2025-07-10 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 125.1 |
| 7d9ca7bf-e31d-38e3-a7b7-112cf425d174 | -10.5773 | -49.1533 | 2025-07-10 06:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 0b306e95-3971-30e0-ab64-e3ddf588f13f | -10.5776 | -49.1316 | 2025-07-10 06:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 3ed30dcc-fdd1-34ea-b629-b7274e52e24d | -8.5211 | -43.3063 | 2025-07-10 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 9ec45ecd-e16f-3090-8291-e5b990bf8446 | -8.5025 | -43.285 | 2025-07-10 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.2 |
| 929f9b31-a218-312f-bf3d-afd897f21cc0 | -8.5214 | -43.2828 | 2025-07-10 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.9 |
| 89487be6-d165-37d1-a444-9396d20ea4f8 | -10.5773 | -49.1533 | 2025-07-10 06:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 0fa7db78-87bc-3e15-8beb-b9348266abd6 | -8.5018 | -43.332 | 2025-07-10 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.5 |
| a11e66fb-20db-3e3c-bef0-e8a61c334d65 | -8.5022 | -43.3085 | 2025-07-10 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 144.6 |
| 154f114a-5079-319a-b353-a0533d3e876e | -8.5022 | -43.3085 | 2025-07-10 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.6 |
| ccf35ce7-3465-38a7-8e35-6533c76669d5 | -10.5776 | -49.1316 | 2025-07-10 07:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| ee3db424-c043-3866-8beb-c17ab227c072 | -8.5211 | -43.3063 | 2025-07-10 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 9b9f456b-676c-3340-bf40-e63890e29138 | -8.5214 | -43.2828 | 2025-07-10 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.7 |
| 0d3dc8b9-ba61-3e0e-bd39-186eec974b44 | -8.5025 | -43.285 | 2025-07-10 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.7 |
| 141b950c-3404-3f91-9d71-c3ce57d1665b | -10.5773 | -49.1533 | 2025-07-10 07:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 243caf02-0d2d-3822-a22b-0e017381db23 | -10.5773 | -49.1533 | 2025-07-10 07:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| bdc2b067-b7c9-30b6-b044-4cd0a992c311 | -8.5025 | -43.285 | 2025-07-10 07:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.8 |
| bf5c4db8-d426-332a-8854-996d2d36b740 | -8.5211 | -43.3063 | 2025-07-10 07:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 262878ad-a7fd-3c92-9bc8-3f83e2bc4160 | -10.5776 | -49.1316 | 2025-07-10 07:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 23bdbb80-3ef0-3ada-927f-2ff4427e112e | -8.5022 | -43.3085 | 2025-07-10 07:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 115.6 |
| d68419cb-f2a7-3867-8ee0-0ba18ab1c0c7 | -8.5211 | -43.3063 | 2025-07-10 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| b0059580-b646-3af5-b262-a565b7911863 | -8.5022 | -43.3085 | 2025-07-10 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| d098de17-2db1-3660-a1ac-3b1dff97e9a9 | -10.5776 | -49.1316 | 2025-07-10 07:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |


[Clique aqui para ver as próximas entradas](README28.md)
