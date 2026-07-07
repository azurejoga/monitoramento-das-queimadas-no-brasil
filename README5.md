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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3774228-7b22-3801-b982-17e881cd2e03 | -10.9205 | -43.0622 | 2026-07-07 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| b9c17edb-2ea8-38b5-9238-409a454ed6d0 | -11.6592 | -44.5741 | 2026-07-07 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 07d517d6-c773-3b80-b152-577d1ce57730 | -10.9397 | -43.0593 | 2026-07-07 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 30ea36c3-a29d-3e9a-b2c2-c0aea5e5c020 | -6.9326 | -43.7032 | 2026-07-07 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 35a41b1b-a46d-3805-860c-7de3ce0a5f31 | -11.6789 | -44.5479 | 2026-07-07 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| cac7a726-5722-3ffc-99b3-55cbf36d047f | -6.895 | -43.7066 | 2026-07-07 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| cc86c718-233a-3043-a4d2-46fcdeb3bc08 | -11.6785 | -44.5712 | 2026-07-07 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 1398dc52-afb8-33cd-9534-99200179ff52 | -11.6597 | -44.5508 | 2026-07-07 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 10c39b23-3d80-3cc6-9d15-de49e3f606ff | -6.9138 | -43.7049 | 2026-07-07 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 214.5 |
| e78b4163-990f-315a-9e61-4eb15d905aa6 | -8.99075 | -71.27087 | 2026-07-07 01:39:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 3c307635-fb7b-3295-ace1-e48b35b93c03 | -6.9326 | -43.7032 | 2026-07-07 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 3219913b-a09a-3f3b-9330-939472830a22 | -11.6785 | -44.5712 | 2026-07-07 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| e6985140-d79b-3223-9d21-4b72534c4fed | -11.6592 | -44.5741 | 2026-07-07 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 390cd3be-d65d-3b14-b0d3-d5160e61ed9c | -11.6597 | -44.5508 | 2026-07-07 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 153.2 |
| c2e84fe1-d107-3eba-affd-3bd77f3cda97 | -11.6789 | -44.5479 | 2026-07-07 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 9b72855f-d223-316e-9f9c-352e60124ad3 | -6.9138 | -43.7049 | 2026-07-07 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 01cd0e2d-d6ca-3505-9aac-ccdedf16b7e3 | -10.9397 | -43.0593 | 2026-07-07 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 970b0361-cac3-354f-8f71-2107b4cbe6b3 | -11.6597 | -44.5508 | 2026-07-07 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 99277762-1fd9-3155-ab84-68fcbb8c4bcf | -13.2783 | -54.3469 | 2026-07-07 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| d40dee8b-44ba-3f0f-b487-f491fc07b86a | -11.6592 | -44.5741 | 2026-07-07 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 75a55d86-52b9-3d43-8e9a-9fb34a4a976d | -8.1154 | -47.1058 | 2026-07-07 01:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 425c03cc-6c34-3aa0-acd8-96f0f997bfc3 | -6.9138 | -43.7049 | 2026-07-07 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 0875dae9-a64f-3574-b286-4413e9c2425e | -11.6785 | -44.5712 | 2026-07-07 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| cf74f851-9ffc-3e5c-a73c-e45c536c8178 | -11.6789 | -44.5479 | 2026-07-07 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 48ce2c4c-1fcc-32c6-a3b7-c7868ce1ab68 | -10.9397 | -43.0593 | 2026-07-07 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 4a1e735f-3fdd-37e6-92b6-02d03eeff10a | -6.9326 | -43.7032 | 2026-07-07 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 118.6 |
| e6e9e1e0-e4c2-3c01-be79-b3599c8ed80a | -11.6592 | -44.5741 | 2026-07-07 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 681122d7-4ac6-3d70-88c5-0b8c9b261d67 | -6.895 | -43.7066 | 2026-07-07 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 41c53402-89f8-3e64-a2c1-9bf313a6d4ca | -13.2786 | -54.3262 | 2026-07-07 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 2d4ad83c-ee5e-335b-ad75-e8db6c98acd3 | -11.6789 | -44.5479 | 2026-07-07 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 211.4 |
| 694e580a-f190-3862-9d31-170eb18d5ab2 | -6.9135 | -43.7281 | 2026-07-07 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 53.1 |
| ec8ce0c3-4488-32bf-87b8-df0e84cf3b4e | -11.6785 | -44.5712 | 2026-07-07 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 46af71a1-0f20-383b-b474-9ae380bf1b91 | -6.9138 | -43.7049 | 2026-07-07 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 19934239-db2f-3bc9-802f-6fdb45f562a4 | -6.9326 | -43.7032 | 2026-07-07 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| dd536a2b-fc1d-3e2f-bc62-0bf6b973c28a | -8.1154 | -47.1058 | 2026-07-07 02:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| b82a4bc8-64aa-37b6-a459-acbe418d4d64 | -13.2783 | -54.3469 | 2026-07-07 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 671932f1-2ddc-3404-941d-3a025779581c | -10.9397 | -43.0593 | 2026-07-07 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 9a707491-1021-305c-88c0-4cf74e91002b | -11.6597 | -44.5508 | 2026-07-07 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 5e63f4eb-f742-311f-962e-74273cab931e | -13.2786 | -54.3262 | 2026-07-07 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 115f98a1-847d-36d8-ba26-6eb71ba88c83 | -13.278 | -54.3675 | 2026-07-07 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 78580930-ffe3-3bc6-af7e-78bee3bccf47 | -10.9397 | -43.0593 | 2026-07-07 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| a2240bfe-f0a1-3593-8c0f-a94b530dcc5f | -13.2592 | -54.3489 | 2026-07-07 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 167.8 |
| 57e703a3-9d1d-3c58-8191-17e0a6ad48fc | -8.1154 | -47.1058 | 2026-07-07 02:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| d4c95e11-11e9-3765-a5db-547731b2345f | -11.6592 | -44.5741 | 2026-07-07 02:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 80760afa-72e9-39ad-9f35-9068c02336ab | -12.7939 | -44.513 | 2026-07-07 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 0a97f945-6f1e-33b1-8191-1fedc6cd07da | -6.9138 | -43.7049 | 2026-07-07 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| edcceb67-d597-370c-909e-2f2bff04fc19 | -6.9326 | -43.7032 | 2026-07-07 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| ce75fc67-72ad-3731-8d62-00540e5838b1 | -13.2595 | -54.3283 | 2026-07-07 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| b332cb19-c6be-3359-8828-2747bb4c99da | -11.6789 | -44.5479 | 2026-07-07 02:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 35d3e9f3-eacc-3332-878c-5104c623b843 | -6.9135 | -43.7281 | 2026-07-07 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 46.0 |
| cde1ef1c-5dfe-3200-b352-e81d4f607e8a | -13.2783 | -54.3469 | 2026-07-07 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 291.9 |
| 9977d898-7c3d-3e3e-9451-26cbc6d1ab70 | -11.6785 | -44.5712 | 2026-07-07 02:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| bcc4d723-b434-3a65-85f0-51d4a3807603 | -11.6597 | -44.5508 | 2026-07-07 02:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 9bc3c47a-b6eb-3e55-ad14-994f445e2fe5 | -11.6597 | -44.5508 | 2026-07-07 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 909c0d8d-bdf0-3a4d-8629-5b5fa65ebb47 | -13.2592 | -54.3489 | 2026-07-07 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 73fa986b-06eb-3a4f-82d3-24b79636f174 | -6.9138 | -43.7049 | 2026-07-07 02:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| aa29441f-2808-3909-8896-04c4cfa3d71d | -10.9397 | -43.0593 | 2026-07-07 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d5bc3e57-be43-3721-b4d8-8070dc1883d7 | -11.6592 | -44.5741 | 2026-07-07 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 13c74deb-e76d-3d50-946e-041904072332 | -11.6785 | -44.5712 | 2026-07-07 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| cb3f5358-2422-3744-9325-578399962232 | -6.9326 | -43.7032 | 2026-07-07 02:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 56.7 |
| d8445554-7046-31f8-98e0-6fdbd96287fb | -12.7939 | -44.513 | 2026-07-07 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 008c1905-fc07-33eb-b389-e6d6ce2da77c | -13.2783 | -54.3469 | 2026-07-07 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 116.5 |
| afad022b-c907-3817-a7e8-b99f1f6b9dea | -11.6789 | -44.5479 | 2026-07-07 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 4b1aef51-dfe8-3861-8d32-14c2f32cbefc | -13.2592 | -54.3489 | 2026-07-07 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 74508f5a-e458-397a-94aa-dfbb1c12a91f | -6.9138 | -43.7049 | 2026-07-07 02:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 146.7 |
| c103528a-ac81-3aea-a38a-e864c37187d4 | -11.6789 | -44.5479 | 2026-07-07 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 3ee9c516-84fa-3362-9280-38b059e7ad05 | -13.2783 | -54.3469 | 2026-07-07 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 111.6 |
| ea5c57c9-3e73-39ac-a53f-0ff1b141690f | -11.6597 | -44.5508 | 2026-07-07 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 94626e02-4d08-327f-b5d9-a10cb81b3e84 | -6.9135 | -43.7281 | 2026-07-07 02:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 4d293592-6b34-35e4-8bed-a6279d9880fe | -11.6592 | -44.5741 | 2026-07-07 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 1738c347-8f61-31e1-935c-8e6207d52102 | -6.9326 | -43.7032 | 2026-07-07 02:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 8e39f0ae-3d65-3fdf-87ca-d38ea6827e75 | -10.9397 | -43.0593 | 2026-07-07 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 847cfeef-bbd2-3290-9a36-123712da858a | -11.6785 | -44.5712 | 2026-07-07 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| a7791e46-969e-3a82-8ab5-fc35a043e1bb | -13.3355 | -54.3614 | 2026-07-07 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 6d4463aa-15f1-3160-b04b-5461be6cacd1 | -13.2798 | -54.2435 | 2026-07-07 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| f60c6c90-7a2c-3022-92ad-466f2aa4cd66 | -13.316 | -54.3841 | 2026-07-07 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| b0197917-a244-328b-a691-1c31d3eab06d | -13.3352 | -54.382 | 2026-07-07 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 0908c270-264c-36e1-bf32-29fd4d255122 | -13.261 | -54.2249 | 2026-07-07 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 2b45a6fd-a520-3e6c-a3b8-b5a3a05798c5 | -6.9138 | -43.7049 | 2026-07-07 02:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 118.0 |
| dc5e5c89-7ad4-31f4-a2c1-c8373ef3f184 | -11.6597 | -44.5508 | 2026-07-07 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| bf368363-cc11-3692-bf92-fdd4400e17d6 | -13.2783 | -54.3469 | 2026-07-07 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 1bcc6559-127c-3266-9e26-4d4e0bff6c97 | -11.6592 | -44.5741 | 2026-07-07 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 8da2a78a-1cf5-36f2-84fe-e6f035d0bf43 | -10.9397 | -43.0593 | 2026-07-07 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 22b41ca1-9c05-3862-97b4-9b8d3c50a941 | -13.3163 | -54.3634 | 2026-07-07 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| d1af91ac-143c-3e36-af25-c8599e41a3b1 | -13.2607 | -54.2456 | 2026-07-07 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| eaaf2ae9-7d16-34da-901f-a05be8e04365 | -11.6785 | -44.5712 | 2026-07-07 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 593a82bc-4f96-337e-ba21-e561a8b27a48 | -11.6789 | -44.5479 | 2026-07-07 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 58acc8b8-69f0-3a5f-bbe6-9085f9875c6b | -6.9326 | -43.7032 | 2026-07-07 02:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| a9f1dd43-ef03-32b9-aa18-2ab96ad0dfd7 | -13.2801 | -54.2228 | 2026-07-07 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 504c0e51-ce77-366c-8ba2-154f63aa1c09 | -13.2783 | -54.3469 | 2026-07-07 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 4178f72b-2909-37b9-97d5-263d4b272b06 | -11.6597 | -44.5508 | 2026-07-07 02:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 3674b3dc-01d1-3607-940b-3d36d46f1383 | -11.6785 | -44.5712 | 2026-07-07 02:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 38d8a108-76d6-36a0-b7ff-4e13ff0a9406 | -6.9326 | -43.7032 | 2026-07-07 02:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 123.5 |
| e3133326-48d9-32ea-9cb1-0debaaeadcb3 | -6.9138 | -43.7049 | 2026-07-07 02:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 7c9856a5-0600-3871-82c2-58ca2d354679 | -11.6789 | -44.5479 | 2026-07-07 02:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 35052bb5-8ab1-3c98-b0e8-8874cd9299e3 | -11.6592 | -44.5741 | 2026-07-07 02:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| e7362dac-e633-3abc-a71b-c59ac5bb1959 | -9.4391 | -40.3171 | 2026-07-07 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 184e5c51-1983-337f-a79c-6d76ca713a03 | -13.261 | -54.2249 | 2026-07-07 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 6fda88c9-4062-3c76-a65d-4533b860d991 | -11.6789 | -44.5479 | 2026-07-07 03:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 2679134f-8f51-3622-a176-7cb9323e0706 | -13.2783 | -54.3469 | 2026-07-07 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |


[Clique aqui para ver as próximas entradas](README6.md)
