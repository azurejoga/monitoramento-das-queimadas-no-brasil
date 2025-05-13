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
| a7d60bfe-cd25-3947-b142-67829d3afbf1 | -13.55331 | -52.87326 | 2025-05-13 03:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b7145f3b-a160-3a1e-ac46-7759cc5b1855 | -11.7937 | -47.40946 | 2025-05-13 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f496d87d-ec7e-39c6-b4f1-99e5582d6d07 | -13.56046 | -52.8749 | 2025-05-13 03:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7cc0baf9-7a61-37b9-b2ff-f66504ca8ed2 | -14.63401 | -45.09798 | 2025-05-13 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 411ba520-97fb-3111-b9f2-faa51f43dd41 | -14.17759 | -45.47021 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e43f8b1-fe0f-31e3-99d9-b5766897ac56 | -12.18143 | -46.71137 | 2025-05-13 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4d4a90a0-8b28-32c0-8c2a-30c9be00ebec | -14.18816 | -45.46998 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08a88f43-3d31-3043-bf1a-3546f0e6e5cc | -12.83564 | -47.41209 | 2025-05-13 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98ecb20e-c7e8-3430-b5f9-d114fd8efdb3 | -12.14783 | -48.00828 | 2025-05-13 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 66a3b2f7-8df1-34b1-ab26-7e916114336e | -11.78699 | -47.35856 | 2025-05-13 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d146efdd-5983-3238-97b6-56ad4d5919c9 | -17.11204 | -49.14402 | 2025-05-13 03:51:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 603080d8-8b59-3389-a687-ee6696b7030c | -14.18489 | -45.48129 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c2e9895-87ce-39af-83c3-2a6427a0c9ee | -11.78859 | -44.27811 | 2025-05-13 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb3546e1-ba2f-3d21-bdc8-c6fdfe810365 | -11.79903 | -47.41059 | 2025-05-13 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e89b10b-b7bd-3805-9dc7-3b9ebdbe9783 | -11.78903 | -47.4049 | 2025-05-13 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4e66798-f358-3de1-b39c-3c0471e83c35 | -12.14637 | -48.01577 | 2025-05-13 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2cfeff74-9fba-39f1-bd79-8558c6e7f306 | -13.55485 | -52.86618 | 2025-05-13 03:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3fd680f9-8c93-318f-b880-d9952cf2885e | -15.4077 | -41.42627 | 2025-05-13 03:51:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c7599588-a031-374d-9774-f68fb580c056 | -12.15188 | -48.01694 | 2025-05-13 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 966a493c-4daf-3994-af1e-a1bfcb9702a0 | -14.19178 | -45.47549 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a606252-55f8-3e77-8364-c5b177c202b6 | -15.78141 | -43.34627 | 2025-05-13 03:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bfdbdc6a-8012-3ac8-8a54-2454cde5be8e | -11.77569 | -48.20123 | 2025-05-13 03:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e609f01f-d274-311c-a45a-5818e1af9d4d | -15.40839 | -41.42219 | 2025-05-13 03:51:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 28fa44c9-c416-37b9-a56e-f9b2a79879b1 | -11.79837 | -47.414 | 2025-05-13 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| adb5246e-8bcd-35cc-8f18-08f3e50df677 | -14.18744 | -45.46745 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73b20fb3-513a-35b5-9917-69509c5e6233 | -11.79303 | -47.41286 | 2025-05-13 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20caaf2c-40ab-3c77-9eb2-1dc8793f9967 | -13.57115 | -52.86936 | 2025-05-13 03:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 304c9def-1dfe-3403-9b04-8dde2e40f9da | -13.39053 | -47.63448 | 2025-05-13 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e80924b8-6c71-36c8-a511-6bd467087ea7 | -11.78969 | -47.40152 | 2025-05-13 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b3fe3ab-6244-32fa-8ee1-432889e502d4 | -14.1954 | -45.48101 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a669c0e1-e415-359a-892a-0fa6b2887adf | -13.39583 | -47.63543 | 2025-05-13 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| debbd386-c403-3b84-9afa-8e74ab94c06f | -13.07184 | -47.80558 | 2025-05-13 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bd7e41a-de8c-37f6-aca0-6ac7add221ac | -14.17844 | -45.4656 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3e4f7a0-99e9-38cd-9aa6-e4bea42263a1 | -11.79729 | -44.27969 | 2025-05-13 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6eee867f-b902-3064-a6a9-bb33dfba1c9c | -14.66056 | -45.12568 | 2025-05-13 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca97e8ee-fa4b-3ae3-94d9-2e1d07079482 | -11.78482 | -47.35732 | 2025-05-13 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26a7a164-f6b5-3691-a7ff-149ca22730e5 | -11.79013 | -47.35847 | 2025-05-13 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11379428-6212-3b77-bc13-f921206958d6 | -12.15261 | -48.01323 | 2025-05-13 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 42808093-bfdb-3a93-a1ef-25e2114afd76 | -13.57831 | -52.87097 | 2025-05-13 03:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25128c11-7e7b-3434-80d4-672d534f7ef2 | -11.78424 | -44.27731 | 2025-05-13 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 429f46a4-68e4-3f10-bab9-66f37693ff3e | -14.19001 | -45.48471 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78052548-3eb1-31eb-9907-92261cad5eb5 | -17.90434 | -44.40331 | 2025-05-13 03:51:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f527f86-cbe5-3653-b5a4-fe709badad5a | -14.19475 | -45.47851 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5f933d8-6a91-3e9d-9a1a-80558d351695 | -14.1909 | -45.4801 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 206701e8-a979-3056-a2d9-8d666ba1b2a5 | -14.18639 | -45.47919 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a26fec9-8b23-3254-9fc8-e9c30bf5262f | -14.80116 | -46.75902 | 2025-05-13 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc2857df-0af3-3ebe-acd7-5e36fcade34f | -15.41121 | -41.42688 | 2025-05-13 03:51:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e4885348-b51f-3a2f-ae51-85496869b734 | -12.83501 | -47.41536 | 2025-05-13 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ee64524-e821-3299-9a25-4bf5ce88658d | -12.18086 | -46.71437 | 2025-05-13 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 72b33b8f-9fc1-3820-b06a-9628e91fd528 | -12.19607 | -46.71749 | 2025-05-13 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9d86692-9dff-361f-afbe-ecdbd546c758 | -13.5553 | -52.87304 | 2025-05-13 03:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 86427763-f6b9-3d90-851b-7ec92a92849e | -11.6231 | -48.11903 | 2025-05-13 03:51:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a27b769-937b-3088-ab42-f4eb7159759a | -14.80603 | -46.75993 | 2025-05-13 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cda5c040-8b5f-305c-b1bb-fc5ca82e0be4 | -13.56798 | -52.88359 | 2025-05-13 03:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 108207e4-587e-3e16-8375-9bc5c28e2ffd | -11.61748 | -48.11793 | 2025-05-13 03:51:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 292e58a1-82c7-36a5-901d-559f8c5a3592 | -15.41259 | -41.41874 | 2025-05-13 03:51:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f3e0c4e0-1957-30f5-946c-da2ea4ef9541 | -15.78469 | -43.3451 | 2025-05-13 03:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c98da2b-2792-3971-99da-16ead0ce9a45 | -12.1865 | -46.71238 | 2025-05-13 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e73f19bb-0818-3954-a4eb-bd0d984dd973 | -14.65976 | -45.13 | 2025-05-13 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7506cd56-b523-3009-b053-f385915902af | -13.39654 | -47.63178 | 2025-05-13 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78eb33d7-79a7-3029-92ca-64e22e8861d3 | -13.55689 | -52.86597 | 2025-05-13 03:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e28b7535-101a-38d4-81e0-520cb1d47aa3 | -17.66326 | -46.68299 | 2025-05-13 03:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3eb8649d-2942-3582-ae53-313aa9d97568 | -21.52048 | -49.68358 | 2025-05-13 03:53:00 | NPP-375D | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9fede7b7-a2a4-3503-a95b-0a60df7c98e1 | -20.99537 | -51.79405 | 2025-05-13 03:53:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a806fad7-6b55-38e6-b373-e29b639a811e | -20.21278 | -46.75011 | 2025-05-13 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88238a4a-31dd-3b02-b5d1-2a67e8833926 | -20.22063 | -46.73327 | 2025-05-13 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d386018-6126-36bd-86a3-1673e0e15c6f | -20.21638 | -46.75506 | 2025-05-13 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcf21c5c-b0c1-38f6-83bd-9b79e7cae470 | -21.79137 | -52.74221 | 2025-05-13 03:53:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1678f0fd-f7a2-3b91-88c3-4101265a90c1 | -19.15817 | -47.81495 | 2025-05-13 03:53:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ddeb273-7cdf-358b-9beb-b636883ca359 | -20.21365 | -46.74566 | 2025-05-13 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a497d36b-cf07-3d0f-aa56-718c85aa58b7 | -19.15702 | -47.82073 | 2025-05-13 03:53:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9f30a249-4406-3c5b-b142-02611559e77d | -21.78364 | -52.74207 | 2025-05-13 03:53:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aaf32809-2bc8-35b7-aff2-4ccd6870b3b1 | -19.15695 | -47.81612 | 2025-05-13 03:53:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5086f7db-9abc-3637-b4f5-5664cb71ea89 | -20.21977 | -46.73769 | 2025-05-13 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57389d7d-c9f3-3586-a45a-448b54cfa28a | -20.22414 | -46.73868 | 2025-05-13 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 963db78d-8a59-3da3-8793-7019abe219a1 | -21.78971 | -52.74377 | 2025-05-13 03:53:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8fda1f5-9f23-3e58-91be-a078693de791 | -19.16165 | -47.81755 | 2025-05-13 03:53:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9f09ed1a-363b-3448-953a-53e28ff72a77 | -21.78239 | -52.74728 | 2025-05-13 03:53:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1516b6f1-a0b3-3bff-abeb-85fc845dcb7b | -19.97977 | -44.10162 | 2025-05-13 03:53:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f7b07ec6-5163-35c8-b71f-ef80bc50c153 | -20.21191 | -46.75456 | 2025-05-13 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 010aeb9d-731b-325d-b8aa-503bd9577aa9 | -20.21722 | -46.75077 | 2025-05-13 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82984f86-ab45-39ba-8c7a-76bbb5482aae | -20.22329 | -46.74305 | 2025-05-13 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e4d97e5-9386-3b7b-8fdc-29fb8b997bf3 | -21.7853 | -52.74048 | 2025-05-13 03:53:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a01da3a-d480-3717-bb25-ab99827e9f67 | -21.78409 | -52.7457 | 2025-05-13 03:53:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a43e7c7e-5a9a-31ee-8bcb-9fe9f9feb615 | -19.9705 | -44.21549 | 2025-05-13 03:53:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 317cd37b-0842-309d-8ddc-ceb4b6537548 | -20.21626 | -46.73227 | 2025-05-13 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 454aa270-fded-3680-b390-568cc1a3897b | -29.32256 | -51.91492 | 2025-05-13 03:55:00 | NPP-375D | ARROIO DO MEIO | RIO GRANDE DO SUL | Brasil | 4301008 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a04b6af6-81c7-33cb-9bda-02aac96f1008 | -29.32754 | -51.91626 | 2025-05-13 03:55:00 | NPP-375D | ARROIO DO MEIO | RIO GRANDE DO SUL | Brasil | 4301008 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 15837016-d5d1-38f1-a066-95ad8d9e2d43 | -8.07 | -43.1216 | 2025-05-13 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.1 |
| 7ffd27f8-f448-39ff-93a7-4b3c4ee9a4fe | -8.0889 | -43.1196 | 2025-05-13 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.5 |
| d2af0799-2058-3e78-a795-d2a2a5ff8723 | -13.971 | -56.8077 | 2025-05-13 04:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 9e074584-0d68-3d22-9de1-833a3213c20f | -13.5683 | -52.8783 | 2025-05-13 04:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 9474916b-7cef-3810-8c69-ccc7982e57f9 | -13.9905 | -56.7855 | 2025-05-13 04:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| cab4f3d7-3a60-3d24-a54c-4a589d9856fb | -13.9902 | -56.8058 | 2025-05-13 04:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| e2df2ea3-497b-33f9-ae5c-6c055e53220d | -13.971 | -56.8077 | 2025-05-13 04:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| b2d69ed2-744b-3c79-aea1-abb8e4fa81dc | -8.07 | -43.1216 | 2025-05-13 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 0672308e-5e21-3328-96f7-c1b526f9a130 | -8.0889 | -43.1196 | 2025-05-13 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 0ada11d8-b761-356a-878e-7484a31b2801 | -8.0696 | -43.1452 | 2025-05-13 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.9 |
| 7155d131-b5b4-3001-ba49-828de0fa118d | -13.9902 | -56.8058 | 2025-05-13 04:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| a89b0263-59f7-3a82-9109-553335ef7dc1 | -13.5683 | -52.8783 | 2025-05-13 04:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |


[Clique aqui para ver as próximas entradas](README6.md)
