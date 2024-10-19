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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90945dae-a91e-3993-927b-792abca862d7 | -3.68095 | -51.08179 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3a00564f-cc8d-3376-9741-fb385fa17d90 | -3.67682 | -51.08112 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74939de8-2472-3f93-ad60-82de1b56acff | -5.65151 | -51.29372 | 2024-10-19 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01aa7217-9c00-30e8-8d2f-16ca6bedb6ef | -5.51762 | -51.11725 | 2024-10-19 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ac205fa-f43b-3210-95c1-fa0e57aa989a | -5.5136 | -51.11658 | 2024-10-19 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0eaf6fe8-0a4c-3901-9722-ab8d9cffc37c | 1.11891 | -52.3282 | 2024-10-19 04:25:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7588ff48-b3b8-38ce-bd00-44cbaa859ba7 | 1.11812 | -52.33207 | 2024-10-19 04:25:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f627ed7f-924b-3ae5-966e-d938c1d2bdd4 | 1.00813 | -52.21997 | 2024-10-19 04:25:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4141ea3f-e48d-3003-b2c0-a0986c0f1abb | 1.00812 | -52.21676 | 2024-10-19 04:25:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9020bc04-ee87-333e-91c1-c4a73c6cc095 | -0.3607 | -51.71963 | 2024-10-19 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd46c980-9c94-32ee-a3c6-3cd4a3850509 | -2.20715 | -51.94812 | 2024-10-19 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4fd2783e-08d1-3a0f-afd7-270463413b66 | -2.08976 | -52.11738 | 2024-10-19 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5678fd2a-39ea-3450-896a-4ad9d491ce57 | -1.28005 | -52.927 | 2024-10-19 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 150f8663-e2ca-389f-98c2-e1b959f6337a | -3.54586 | -53.02446 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 652acb47-5db6-3975-903d-bdab4604bb26 | -3.54113 | -53.02367 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f70a915d-7089-3cc7-b695-745c18aa27b0 | -3.31422 | -52.85504 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d42667b6-7cb6-384c-b079-cef5824dc063 | -3.45387 | -53.01375 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e2f347ae-e789-320a-aae6-3b37f78a3297 | -3.36517 | -53.22095 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5869e512-5ccc-302d-8ffd-3c46f1dc00cd | -3.32435 | -52.99596 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 731591eb-e3df-3e9c-8580-0ab800756679 | -3.31631 | -52.85696 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 838072d7-306d-3268-8845-4212f7e764e4 | -3.31337 | -52.86006 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc31fd7e-7f70-3412-9d5a-a25d7860f7b8 | -3.3116 | -52.85632 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43f49247-51af-3fdc-a9ae-c03ed90d230d | -2.85567 | -53.32979 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 00c9dda1-2a0d-340a-8828-e1a16a2d29a4 | -2.85478 | -53.33519 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| d1ccd911-d4fc-387f-98e2-02cb3f881a45 | -2.85169 | -53.32356 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c28af8e8-14bf-342c-aa72-a4272c412f63 | -2.73522 | -52.57444 | 2024-10-19 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1200136-2a41-3962-bf5d-b63e7cd7023a | -2.73441 | -52.57932 | 2024-10-19 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f2d8778-ca9a-3b43-b627-0cf80883736e | -2.66488 | -52.57516 | 2024-10-19 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 798ef315-3d14-3a4d-b107-3b178851e0c4 | -2.66406 | -52.58018 | 2024-10-19 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc526757-6c69-3f7c-95ba-c8d86da4f877 | -2.65941 | -52.57944 | 2024-10-19 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a57f8fe9-cddd-3612-8236-3022e581c456 | -2.08723 | -53.40092 | 2024-10-19 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ea775af-2906-32de-b45f-5e8a78bc7e3b | -2.08131 | -53.40592 | 2024-10-19 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4143cb15-48b2-34a6-a68e-e8145fe30bf6 | -3.22364 | -52.61434 | 2024-10-19 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| facd2f34-729d-3d70-ab18-d98f9b5ae60d | -3.06179 | -53.24124 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eaa8f09b-8ef1-3c49-8d76-c9f338ddbdd7 | -3.05827 | -53.23908 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18c44713-912d-3936-ba5b-c24ad0c67078 | -3.05744 | -53.24424 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e96c914f-d3de-3ed2-8bcb-30786fdcdab0 | -3.05694 | -53.24053 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d9c681f4-a698-3977-83e8-7982e1e6c6a6 | -3.05342 | -53.23833 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 151e4122-9686-35d6-96c2-a8ba3d3eb907 | -3.01251 | -52.1831 | 2024-10-19 04:25:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae375bdb-008a-3936-b4e6-720d45291e21 | -2.98385 | -52.84715 | 2024-10-19 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 4d6e0c71-b143-360b-afb5-3dcce93933cb | -2.98303 | -52.8522 | 2024-10-19 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 7d63a665-fbe4-30ac-b698-289c038ba801 | -2.97831 | -52.85144 | 2024-10-19 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| bf0ac138-750b-35ef-9e20-eb659297bc63 | -2.97749 | -52.85653 | 2024-10-19 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 456c68b2-a80a-37cc-b0a5-448404f87780 | -2.97361 | -52.85057 | 2024-10-19 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a0df4228-91b3-3fe0-8e68-be8cc835e741 | -2.95913 | -52.90986 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 45c93cc5-39e0-3708-b19a-fc2bfc94f432 | -2.95831 | -52.9149 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| cd32cf2c-7043-36b6-9492-8b6cceddbeea | -2.95518 | -52.90426 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8288b702-7e96-38c0-bbdb-06a2a4ea4776 | -2.95438 | -52.90916 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 5a620aa3-6252-348b-a2b2-314c53fa9850 | -2.95357 | -52.91418 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 8b134660-60b5-34c0-b679-dad43ce12d16 | -2.94963 | -52.9085 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 52609593-5bea-3e8c-85d0-d986ad7ce01b | -2.94881 | -52.9135 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| abed7190-cbf3-3816-ae88-dd0d6f77b152 | -3.95381 | -53.41044 | 2024-10-19 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca390e09-6fa6-3337-ac1b-af8329473a5e | -3.88481 | -52.34761 | 2024-10-19 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e40f63d9-e906-3a2d-8122-c5010f409dd9 | -3.75394 | -53.40045 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f196a925-b123-3b18-9281-58416032fa57 | -3.71015 | -52.40142 | 2024-10-19 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d17a5cd-50eb-37bc-90f1-a03ed4bf91f0 | -2.08963 | -53.57526 | 2024-10-19 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a119588-8662-35da-b33a-ad5dbba92d20 | -3.53581 | -53.85071 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab586cc6-3330-365e-86b3-95d14b30c60f | -3.49435 | -54.45589 | 2024-10-19 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fdba0c6-e487-3aad-9bd1-b9179e81a5bb | -3.43613 | -54.14817 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38401161-a981-3d06-9ad1-1a6b459dfe4d | -3.43372 | -54.14715 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c9245d8-51c3-36cc-bdd4-737015778247 | -3.43319 | -54.15023 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5230095-bc95-3026-b635-35c999fdc2bd | -3.43104 | -54.14715 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b3b4769-3496-3220-a131-df29932329e1 | -3.4281 | -54.14925 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6dfc64ae-377a-3e25-98fd-ccba809916d4 | -3.42594 | -54.14619 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e01e062-0983-311e-ba2a-feb7729a7cf3 | -3.42543 | -54.14927 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68d629e3-f5fa-3803-a53e-acb08ac10a90 | -3.42083 | -54.14526 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92cf15bb-d02c-35e3-b1be-b35c62f1517e | -3.42033 | -54.14833 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22b957ab-d884-365c-939c-607ecbec3e2e | -3.39704 | -54.06716 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c4de9c0-95a6-32a1-86c7-6de8f5041e4c | -3.12079 | -53.74751 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76d45ea4-9895-386a-9bbe-17f37983067f | -3.11265 | -54.99049 | 2024-10-19 04:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c0a02d6-ca02-3849-8467-ae0f07a2ad39 | -3.59032 | -54.68417 | 2024-10-19 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5fae7ca-f6c1-3298-8b7a-a23caae04ab4 | -3.49489 | -54.45277 | 2024-10-19 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f205d8fb-c679-3bb9-9eb8-c62d4dd0b32e | -3.49373 | -54.45518 | 2024-10-19 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f07b65ed-bcd4-3206-a34b-776ef8b9a0fb | -3.44172 | -54.1461 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb5b37e3-8f76-36fe-ae93-d1afbc47f0ef | -3.44122 | -54.14917 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be2a0e37-2d58-3ce5-944d-c1e6457784c1 | -3.43933 | -54.14508 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ca3ac55-9afe-3b64-936c-7e559aca3754 | -3.43881 | -54.14814 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46299cd9-7a5f-3515-ae25-9fd83d8af9a7 | -3.43828 | -54.15122 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0dba0ba8-e6b0-3c6c-887c-06ed696f93a2 | -3.43562 | -54.15126 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc0f27a6-c47e-322f-8f3e-358b6c85e0df | -3.43053 | -54.15024 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a71813b6-a362-36d5-8a98-38c590aee886 | -3.42863 | -54.14616 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c6ec4627-d746-3b50-b013-6d2882388ce8 | -3.41498 | -54.67029 | 2024-10-19 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e870c26-fd95-3839-bf6f-4576132d6b56 | -3.41442 | -54.67368 | 2024-10-19 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02bb801d-4660-37b6-aea2-c76011c2b32e | -3.40211 | -54.06808 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8518aa1-3e6f-3d80-a8b2-a913e9c52e4d | -3.40162 | -54.07106 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea0ee7a7-aef2-3a78-831e-451f994cbec0 | -3.39654 | -54.07016 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb133f9b-b833-35d0-9d25-aa93d31eeabb | -3.32841 | -54.0822 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8174d4c-0061-3ba7-a062-ffc589b9dfff | -3.32332 | -54.08124 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b32f9760-5b3c-3f0f-878d-05fb99cafb60 | -2.91515 | -54.03424 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc2b5c71-c18f-36e4-bd8b-3555d1a77413 | -2.88626 | -53.986 | 2024-10-19 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e43b913c-8fd6-3645-a7d3-4de43b9c04e5 | -2.8752 | -54.18287 | 2024-10-19 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 830c0c2c-70ed-333d-9326-d3470d05f931 | -2.8747 | -54.18596 | 2024-10-19 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9234a254-63b1-3660-b1df-bb947acc2c1f | -2.83252 | -54.86653 | 2024-10-19 04:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89c0e00d-b5d3-312c-9a35-7391d182676f | -2.82714 | -54.8654 | 2024-10-19 04:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8397940-29b4-3e6f-b8de-6856591eb25d | -2.80471 | -53.98575 | 2024-10-19 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f4de9a5b-c401-3cc9-ad86-104fcde74b67 | -2.80422 | -53.98878 | 2024-10-19 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0f00bf28-805c-3131-8ce9-07533f8dfe45 | -2.7991 | -53.98796 | 2024-10-19 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0df6c909-8172-3076-91d2-c3a15daf05e7 | -2.79349 | -53.99018 | 2024-10-19 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b007a7b-f5ab-3d17-b5cf-af8d57a6debc | -2.71439 | -53.99169 | 2024-10-19 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c86d1c07-62ec-3be1-bf9d-a32e2039209e | -2.71178 | -53.99031 | 2024-10-19 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README24.md)
