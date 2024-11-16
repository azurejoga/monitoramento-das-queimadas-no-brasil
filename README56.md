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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 208aedf7-7408-311b-bd66-e3883726e00b | -15.9025 | -59.2741 | 2024-11-16 05:00:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 097ac20a-3123-3632-8117-b9d90a8736c5 | -3.2008 | -45.5629 | 2024-11-16 05:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 57d2f46e-a15c-37a5-87b7-31f862ee0a6a | -2.2299 | -53.6219 | 2024-11-16 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| fd174771-b8c3-355e-b8a6-5cf874c8e3b7 | -2.78 | -48.5806 | 2024-11-16 05:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 685f558b-a5d7-3f6a-bbf3-49c69896a05a | -2.2299 | -53.6018 | 2024-11-16 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 9868d764-44a1-3f1f-9008-27b37de85853 | -15.9025 | -59.2741 | 2024-11-16 05:10:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 6fc3d2ac-7a94-3de6-9b16-79a15e7f688e | -6.1363 | -42.578 | 2024-11-16 05:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 43b57a73-4bfb-347a-aeb9-b724a7f12649 | -3.2009 | -45.5405 | 2024-11-16 05:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 0ab3894b-da64-390c-9cea-4609e6e05bc1 | -15.9028 | -59.254 | 2024-11-16 05:10:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 53c331fb-b6c6-3bd3-8cd4-a7f592bbd9d0 | -5.1615 | -44.08406 | 2024-11-16 05:16:00 | AQUA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8d3d3a30-1e30-3979-9622-2aa7b80443e9 | -4.47037 | -44.5624 | 2024-11-16 05:16:00 | AQUA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 56fd3e82-7f75-367a-a913-5b0e52c95279 | -2.65999 | -46.17241 | 2024-11-16 05:16:00 | AQUA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ee9b5d1d-a75e-3fda-9536-ce328146b6fc | -3.73308 | -45.66051 | 2024-11-16 05:16:00 | AQUA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 2d8dcadf-96d9-3791-b8d0-547a7da3f12d | -6.13074 | -42.57919 | 2024-11-16 05:16:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 40.8 |
| 90e036ff-bdaf-3beb-99a3-86fc72ffa037 | -6.14017 | -42.58055 | 2024-11-16 05:16:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| c6aa187e-e15c-38db-85b5-4b43b221a615 | -3.74351 | -45.65265 | 2024-11-16 05:16:00 | AQUA_M-M | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 50aea1a6-be81-3657-aff3-fe7f25543780 | -5.66545 | -35.62822 | 2024-11-16 05:16:00 | AQUA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 40.9 |
| 35675e66-8e8f-3285-b65f-51aaabc69abb | -2.7739 | -48.57934 | 2024-11-16 05:16:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 10d83b6b-4f2e-3ac8-a625-a460cf400572 | -2.7693 | -48.58722 | 2024-11-16 05:16:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2c31ed03-4a63-305d-a1e7-5e2d66cb1a88 | -3.94468 | -46.70184 | 2024-11-16 05:16:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| db1f07f2-c79d-3a50-a430-27b125c0c0e3 | -2.34221 | -47.46645 | 2024-11-16 05:16:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 276f06ed-139f-3de3-80e1-3f55476092fc | -4.80938 | -42.91303 | 2024-11-16 05:16:00 | AQUA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7a868548-3027-32e2-a2ad-f2046c21607e | -2.14117 | -46.55217 | 2024-11-16 05:16:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c0e2ce26-ed15-3693-85e7-94805870fada | -3.49775 | -47.21421 | 2024-11-16 05:16:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d9434938-b961-378f-bd3c-6630129d8211 | -4.9889 | -44.31546 | 2024-11-16 05:16:00 | AQUA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 36c91a04-66ad-36c2-a3e5-5b41b197f32f | -2.081 | -48.95233 | 2024-11-16 05:16:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bde96b90-60d8-34b2-b15e-c6cfee4ca0fb | -4.99774 | -44.31676 | 2024-11-16 05:16:00 | AQUA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6be8c606-561b-3d80-85b9-af4279db73be | -2.81426 | -46.65902 | 2024-11-16 05:16:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2560d7c2-c89a-3f5b-bd34-ffba92c98ed2 | -3.27838 | -45.4961 | 2024-11-16 05:16:00 | AQUA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 31.1 |
| ac0297e1-dcac-3b80-a0ed-45057680dba9 | -3.74212 | -45.66187 | 2024-11-16 05:16:00 | AQUA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 173bec0f-4691-383a-b60e-874ecb5bc42e | -2.78915 | -48.55334 | 2024-11-16 05:16:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| a004c55b-fc8d-35a4-b3d7-fece82507a93 | -3.9874 | -43.72408 | 2024-11-16 05:16:00 | AQUA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 669a18eb-db44-3881-bdfb-67d0aea95117 | -3.99526 | -46.49454 | 2024-11-16 05:16:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ba86d58a-5908-3645-9112-25cb88ba824f | -2.97977 | -47.98415 | 2024-11-16 05:16:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1410591f-31ec-3fc6-97de-ce52472e75fb | -3.27699 | -45.50528 | 2024-11-16 05:16:00 | AQUA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 85aa630d-ffaa-316f-9423-31d6b49cfeff | -5.67328 | -35.62218 | 2024-11-16 05:16:00 | AQUA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 42.0 |
| cecd6d35-7c0c-31eb-af3d-4f93454455be | -3.33944 | -45.15234 | 2024-11-16 05:16:00 | AQUA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9d3d60c7-9254-36d4-b460-223b12ca5368 | -2.77139 | -48.57322 | 2024-11-16 05:16:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 31f577be-98a8-34d6-bc03-c5f5436588ab | -2.34399 | -47.45472 | 2024-11-16 05:16:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| fdd01f48-5442-39a0-bcc2-f992e0119d86 | -2.35779 | -49.10631 | 2024-11-16 05:16:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 64d476bd-c176-3531-8de3-2d3550c5fa9e | -3.73447 | -45.65129 | 2024-11-16 05:16:00 | AQUA_M-M | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 28.0 |
| ba4af135-3646-36dc-82f1-7e421030aa4d | -3.51556 | -44.71184 | 2024-11-16 05:16:00 | AQUA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a7b5a3e4-9996-3998-b522-5ba279ab8b3d | -4.27971 | -48.20286 | 2024-11-16 05:16:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c91cc054-632c-347c-b8e8-185bed7f1f05 | -6.13222 | -42.56904 | 2024-11-16 05:16:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 6805f4c9-5a12-35d3-9353-51c4b28e5634 | -5.15262 | -44.08278 | 2024-11-16 05:16:00 | AQUA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 78045f47-0738-3f46-87eb-a8942a1d64f9 | -3.78426 | -43.90875 | 2024-11-16 05:16:00 | AQUA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| aa1a8118-6737-3f6b-aa84-00dd7d9991fc | -3.26797 | -45.50396 | 2024-11-16 05:16:00 | AQUA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8d135b36-beb8-3a49-8e79-355491b58710 | -4.36977 | -48.08434 | 2024-11-16 05:16:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 11335744-e586-3045-b962-63ecdff68b98 | -2.66785 | -46.18364 | 2024-11-16 05:16:00 | AQUA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 9c5955a0-8fb5-3e02-9a3c-879f0272d74b | -2.787 | -48.56712 | 2024-11-16 05:16:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 589b0be6-3d7a-3349-ad08-1bcff3197546 | -2.13139 | -48.77612 | 2024-11-16 05:16:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| f22fd3a3-9b94-34c1-b0e3-80a61bf00b47 | -4.91016 | -43.22751 | 2024-11-16 05:16:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ff70e391-e15c-3701-a640-555b89089c48 | -5.16017 | -44.09296 | 2024-11-16 05:16:00 | AQUA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 52b25733-17cb-3f07-b067-e46b1bc0f0fb | -3.97983 | -43.71387 | 2024-11-16 05:16:00 | AQUA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aa5b9b32-ce73-39dc-9f03-c0eb9a7be25d | -3.49941 | -47.20325 | 2024-11-16 05:16:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a03a9d45-cc14-3a70-815f-eb9573f13ac6 | -3.19524 | -45.55324 | 2024-11-16 05:16:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| d159063d-f90c-33bb-b6e8-1c09b6d75a4d | -6.14165 | -42.57045 | 2024-11-16 05:16:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 83d7ae71-a0cd-3b6e-8983-3257f1f26932 | -5.71754 | -44.80521 | 2024-11-16 05:16:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 84ba3e7e-b922-389e-87bc-2abf503c14ed | -2.63902 | -48.4759 | 2024-11-16 05:16:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 225c9aa7-4fea-3cbe-9eac-924938d6037e | -2.77607 | -48.56547 | 2024-11-16 05:16:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 84dd1cf9-d50e-39e2-b1ba-e385c6763863 | -2.35541 | -49.12179 | 2024-11-16 05:16:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3bfe9b03-e136-3deb-8b05-ae94042f157b | -3.58108 | -50.52636 | 2024-11-16 05:16:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 8056e098-0602-395f-9bd2-4251bd29dec2 | -5.6688 | -35.65461 | 2024-11-16 05:16:00 | AQUA_M-M | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 38.0 |
| 8540c52f-2e13-3a51-9c84-7d3edb80f161 | -4.21581 | -47.21561 | 2024-11-16 05:16:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e9df963b-eabd-3e27-b12e-93e33aee644e | -2.55209 | -46.89308 | 2024-11-16 05:16:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a379e1ce-5a73-3736-810c-05e598525333 | -2.62903 | -46.18795 | 2024-11-16 05:16:00 | AQUA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 498642ec-5c72-3462-8557-c5001d27c6e4 | -5.1513 | -44.09167 | 2024-11-16 05:16:00 | AQUA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7b975597-7e0a-30a8-bbf0-0a957ec55a15 | -4.46905 | -44.5712 | 2024-11-16 05:16:00 | AQUA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dec95b61-93fb-3ede-bb68-4c8dc1083369 | -3.98872 | -43.71518 | 2024-11-16 05:16:00 | AQUA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| c7ec0b32-fd43-3de4-8958-337f84fdc6b4 | -3.19663 | -45.54401 | 2024-11-16 05:16:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 109.6 |
| e9f45700-86b9-346f-940b-8fde69ac71aa | -5.24061 | -44.91081 | 2024-11-16 05:16:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 17f7a10c-5fc8-3350-85d4-e5276b352c10 | -3.79312 | -43.91005 | 2024-11-16 05:16:00 | AQUA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0efcc2f5-bd21-35ab-b819-61b53ea8456c | -3.68894 | -50.09919 | 2024-11-16 05:16:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c46d7069-4eba-3eab-9697-2289754b876b | -5.9532 | -44.46421 | 2024-11-16 05:16:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1910f35d-0b0c-36b5-b7a2-eb8db1a9a936 | -2.64991 | -48.47752 | 2024-11-16 05:16:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 0be2de0a-634c-39a6-8801-18c724e20462 | -4.29659 | -48.0923 | 2024-11-16 05:16:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 01ed9eeb-77b4-3617-82ab-7f626c50cf6c | -4.30028 | -48.0681 | 2024-11-16 05:16:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ffe49e1f-85c2-3087-b314-0d322aa892a3 | -3.26936 | -45.49477 | 2024-11-16 05:16:00 | AQUA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b2ef6ec5-1503-3bb1-99f1-b2fed1e3d1ba | -5.48557 | -43.20475 | 2024-11-16 05:16:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 22c547b6-caad-3227-a247-55a93b609d14 | -7.3971 | -40.39772 | 2024-11-16 05:18:00 | AQUA_M-M | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 9b242287-0c54-3cff-97ff-feb854fb5e60 | -8.27582 | -45.97005 | 2024-11-16 05:18:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2aa0b4d1-f063-3b3b-9abb-58a8310d54bd | -7.39798 | -40.39087 | 2024-11-16 05:18:00 | AQUA_M-M | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 9d6eb62d-92c7-3133-bbbc-f113e7cc8b35 | -7.24718 | -46.77934 | 2024-11-16 05:18:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c1565a7f-b369-3e1d-a921-d2df49b20999 | -8.28471 | -45.97138 | 2024-11-16 05:18:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 37c40e81-b230-353f-a6f4-06134e559650 | -10.66385 | -44.49587 | 2024-11-16 05:18:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 16c4a318-e410-372c-8c8c-d9e3ed6c362f | -6.01724 | -48.03914 | 2024-11-16 05:18:00 | AQUA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ecf750b1-b47a-373f-aba7-f525ef905255 | -3.2753 | -45.5151 | 2024-11-16 05:20:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 3408ae4c-c06c-3aab-8396-dfa92e86b082 | -2.78 | -48.5806 | 2024-11-16 05:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 54b4286e-fa41-3d26-ba42-b22442591502 | -3.2009 | -45.5405 | 2024-11-16 05:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| f54364c0-4e68-35aa-9663-c6f2340ff2da | -2.2299 | -53.6018 | 2024-11-16 05:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| bef7c255-39c5-33c7-9f66-121b3a4d2d7d | -6.1363 | -42.578 | 2024-11-16 05:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 111.3 |
| a21b2733-e3d6-3d58-88d4-e8b9c67c8b68 | -2.0271 | -53.9477 | 2024-11-16 05:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 148ea4db-9321-3109-b3aa-f77aefe89099 | -3.2754 | -45.4927 | 2024-11-16 05:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 46.1 |
| d97c920a-6594-303f-bc8e-1bfd3be66c21 | -2.2299 | -53.6219 | 2024-11-16 05:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 9d970e73-d398-3452-ab90-81ccda29afd5 | -3.2008 | -45.5629 | 2024-11-16 05:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 56317abe-e7bc-354d-918e-8201308d3727 | -17.62564 | -57.56271 | 2024-11-16 05:22:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.5 |
| f50268fd-15eb-3f12-94f8-c43e63c63cb4 | -17.65625 | -57.53596 | 2024-11-16 05:22:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| 34c5dc1b-c814-3011-a96a-4fcfe7dda349 | -17.82969 | -54.54019 | 2024-11-16 05:22:00 | AQUA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 86b79488-4bba-38ed-ab80-a50890187699 | -17.58334 | -57.55805 | 2024-11-16 05:22:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 6b7d2e5b-f357-37e7-b2b0-d2fae242672d | -17.24486 | -57.45229 | 2024-11-16 05:22:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.2 |


[Clique aqui para ver as próximas entradas](README57.md)
