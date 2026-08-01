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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c294af1c-de74-34f6-b256-e720793b7464 | -14.0929 | -46.2407 | 2026-08-01 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 5c8858b2-0409-3256-9432-bd7872a0de63 | -5.5608 | -43.9775 | 2026-08-01 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| d0a027bb-bd4c-3329-8b3b-33394aa9df5e | -11.2593 | -54.8313 | 2026-08-01 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 4e895fbd-63ae-32b9-ae8e-54469c2ca4cb | -6.5699 | -55.156 | 2026-08-01 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| d07db1a6-d45b-312c-bc73-f8a91a9c010a | -14.073 | -46.2669 | 2026-08-01 00:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 66c753ae-4b70-3363-bd26-84e00b6cc3cb | -18.0424 | -51.2877 | 2026-08-01 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 112191a8-1320-35af-bf83-a32cf4f28b1e | -3.0612 | -39.9346 | 2026-08-01 00:00:00 | GOES-19 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 77.5 |
| b7e4cfbe-c3d8-3652-8ac9-17cc64dff6c1 | -6.7555 | -41.0103 | 2026-08-01 00:00:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 107.5 |
| 9397d27a-9b37-3537-a27f-bb654e94ffb6 | -18.0419 | -51.3097 | 2026-08-01 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 271.7 |
| f455776b-8545-3eae-9d1e-e64946a0f8de | -14.0735 | -46.2439 | 2026-08-01 00:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 233c46a4-14dc-35af-b3f2-4b5f77a521e1 | -11.2402 | -54.8534 | 2026-08-01 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 809.7 |
| 0b9491b5-ce40-3247-8e57-c86444c6e0f2 | -18.0619 | -51.3063 | 2026-08-01 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 1f3acc5b-b5e7-3c8f-9abb-6303bcd8374d | -2.8932 | -48.0171 | 2026-08-01 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 25711c96-3bd9-34a2-b892-c23ddaee80ab | -11.2399 | -54.8737 | 2026-08-01 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 610.0 |
| 6dd9eab1-6df4-3056-a266-5f65c2c9cfb7 | -7.6505 | -45.0624 | 2026-08-01 00:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 4107e0d9-4582-35ac-b76b-39a4891552ae | -18.0414 | -51.3317 | 2026-08-01 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 67d0de32-c3e7-3d70-bd60-513a316a746f | -17.0593 | -45.891 | 2026-08-01 00:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 59.1 |
| cbb9b489-72dd-3083-84c3-85cbabb0655c | -11.2404 | -54.833 | 2026-08-01 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 69a8e7b4-172e-37f1-a4b0-05d63dd46772 | -11.2588 | -54.8721 | 2026-08-01 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 252.3 |
| f15ee585-9a51-395d-81e5-02c77f3ea273 | -9.8837 | -48.7287 | 2026-08-01 00:00:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 87b78760-ed89-354a-90bd-df0a538111a2 | -11.2591 | -54.8517 | 2026-08-01 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 321.5 |
| df514fda-9f0d-3183-b3bb-1a353cc0f728 | -7.6505 | -45.0624 | 2026-08-01 00:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 85c1155c-953f-3586-9509-31a134b83a74 | -6.5514 | -55.1569 | 2026-08-01 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b795eb93-c772-3e7b-ba1f-4b5d4349f5c4 | -18.0619 | -51.3063 | 2026-08-01 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 25b05a66-c510-3d2a-9886-cca18c83960d | -3.0612 | -39.9346 | 2026-08-01 00:10:00 | GOES-19 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 91.6 |
| 4a937acb-fda4-3a50-99d5-86b2e76f5eed | -14.0735 | -46.2439 | 2026-08-01 00:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 3d562207-9634-3f43-ad88-5ffd99d1c73c | -11.2402 | -54.8534 | 2026-08-01 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 753.9 |
| c1854613-55c2-339a-a212-564c854a6a15 | -6.5699 | -55.156 | 2026-08-01 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 7cb227cd-6fca-3fe5-8ad9-0e2e051cfb63 | -17.0593 | -45.891 | 2026-08-01 00:10:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 67.1 |
| c30fde12-c025-3ab5-9658-721b2ea91f12 | -14.0925 | -46.2637 | 2026-08-01 00:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 7f9be05f-9247-3906-8193-f9012954da08 | -6.7744 | -41.0084 | 2026-08-01 00:10:00 | GOES-19 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 8cdd71ca-571e-3b88-805f-29b74eec6bd9 | -14.073 | -46.2669 | 2026-08-01 00:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 9999801f-3664-3ad5-897a-6e20ac1de925 | -11.2588 | -54.8721 | 2026-08-01 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 254.5 |
| 0ab6818b-588d-31d9-bcc1-8c1f1f03c01f | -18.0419 | -51.3097 | 2026-08-01 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 0a8c2459-9bae-32b8-94fb-4488d0eed6b2 | -11.2399 | -54.8737 | 2026-08-01 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 516.8 |
| f349e91e-d7ba-303e-90f0-c97077059845 | -11.2213 | -54.855 | 2026-08-01 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 67bfd6a9-ea88-3eda-9d90-2452598290c2 | -14.0929 | -46.2407 | 2026-08-01 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| c025a255-227d-3d24-a353-d196bd46b285 | -6.7555 | -41.0103 | 2026-08-01 00:10:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 14fccf8a-7b52-3688-b1ab-66af2b44240d | -11.2404 | -54.833 | 2026-08-01 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| e3479886-fe4e-3108-8053-1504270a5397 | -11.2591 | -54.8517 | 2026-08-01 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 332.5 |
| c17aba1f-4ad3-30bf-b17f-18b86343efbc | -5.5608 | -43.9775 | 2026-08-01 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| ddc2890b-271d-3c4d-a3f0-0109a4387c39 | -2.8932 | -48.0171 | 2026-08-01 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 1e49ca11-4290-3cf5-b8a5-c3a1584f7bbd | -11.25 | -54.91 | 2026-08-01 00:15:00 | MSG-03 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4e96fbc3-19bb-32e4-9ecd-3b6c980bf3e4 | -11.25 | -54.85 | 2026-08-01 00:15:00 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd4fbf17-6335-36a8-81b5-0f0f178ac3b1 | -18.04 | -51.34 | 2026-08-01 00:15:00 | MSG-03 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| afd76cf9-ad32-334a-89cc-792f618e902e | -2.8932 | -48.0171 | 2026-08-01 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 64bbba64-67d0-3785-90ad-059b8052b91f | -11.2402 | -54.8534 | 2026-08-01 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 425.6 |
| d2985f37-be19-374f-bb68-76260021b5a0 | -6.7555 | -41.0103 | 2026-08-01 00:20:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 6872e72f-ecf4-30bc-8547-b005173ff3aa | -11.2399 | -54.8737 | 2026-08-01 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 272.2 |
| c5ea2aea-55e9-3914-93ab-a9611f1b8eb5 | -14.073 | -46.2669 | 2026-08-01 00:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 54c99481-ae74-37f1-9d53-4a01f48e3e5a | -18.0419 | -51.3097 | 2026-08-01 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c5de7e71-ed36-3c47-9747-727bbd3a2f84 | -11.4284 | -50.6075 | 2026-08-01 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| e0207233-e5be-3c43-9cd9-6d83cda86279 | -5.5608 | -43.9775 | 2026-08-01 00:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| b39d072b-02c6-34a4-8e25-698f5c4fac91 | -3.0612 | -39.9346 | 2026-08-01 00:20:00 | GOES-19 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 84.3 |
| a1d31de0-fcdb-35f1-ab64-885fb8611a08 | -11.2213 | -54.855 | 2026-08-01 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 62e29adc-dbcf-3b7e-8b29-fabb5676e24b | -14.0735 | -46.2439 | 2026-08-01 00:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 206.9 |
| f54f0c1a-724b-324d-b401-8c58433df8f3 | -6.5514 | -55.1569 | 2026-08-01 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3c74ddaa-4e81-31e2-ab52-52f001f5530d | -11.2588 | -54.8721 | 2026-08-01 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 303.2 |
| bf39776f-741b-3ae1-bf37-95bf7d3cbbc8 | -14.0929 | -46.2407 | 2026-08-01 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 0317e2a5-179e-3b22-8ebe-dc06b0c0ac11 | -6.7744 | -41.0084 | 2026-08-01 00:20:00 | GOES-19 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 70.6 |
| 9dce87c0-386b-3645-8bc6-32e5eaabed44 | -11.2591 | -54.8517 | 2026-08-01 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 431.7 |
| 7bfbeba3-0945-3ebe-b652-d2a72c3a71b2 | -11.2404 | -54.833 | 2026-08-01 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| dfa31298-3c34-3e7b-814b-878eb649933c | -14.0735 | -46.2439 | 2026-08-01 00:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 49121f7d-891d-328d-806e-b39d5054e7fc | -5.5608 | -43.9775 | 2026-08-01 00:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 7097eee1-8855-347f-8f16-6d0f0fe9c900 | -1.6591 | -54.4543 | 2026-08-01 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 1e6cb122-b1c2-351b-92e0-44e08f9b32f5 | -14.0929 | -46.2407 | 2026-08-01 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 60de2f70-5fd9-3333-bc51-c5818c253ad6 | -11.2402 | -54.8534 | 2026-08-01 00:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 642.5 |
| 716a24c7-b291-3a49-9a23-aaebb1d52ac9 | -11.2399 | -54.8737 | 2026-08-01 00:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 579.0 |
| c6edd25c-d61e-32b3-b9a7-665d9c1dbf24 | -11.2404 | -54.833 | 2026-08-01 00:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 7aec09a3-d37d-39f8-a483-1e263151be80 | -11.2591 | -54.8517 | 2026-08-01 00:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 215.1 |
| 093764b5-1cf2-39d9-86e3-0fb6dd44aa40 | -6.5699 | -55.156 | 2026-08-01 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 84717ad4-196a-3478-9363-676a5742451c | -6.7555 | -41.0103 | 2026-08-01 00:30:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 738fb3f6-4677-3570-8a28-13c7f55ca14c | -11.2588 | -54.8721 | 2026-08-01 00:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 199.5 |
| 39ae116e-de08-3c8c-905d-470b88ea77e7 | -4.6019 | -49.0499 | 2026-08-01 00:31:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88e5b461-b937-332d-87a3-9d949f737818 | -9.8808 | -48.724098 | 2026-08-01 00:31:00 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d6a6fe0-ab74-30a0-9ff9-ff05f666bc5d | -8.166 | -55.440899 | 2026-08-01 00:31:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ed118b0-f40d-3a45-8387-dd96f23cb77a | -8.1676 | -55.447899 | 2026-08-01 00:31:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40de0315-c875-3f75-9671-9e299be79961 | -18.520599 | -47.3848 | 2026-08-01 00:31:00 | METOP-B | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3b7c2314-583e-38b3-a36c-ddd7bfc2766a | -8.1954 | -55.434399 | 2026-08-01 00:31:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfb0c4da-1dd2-379b-9c95-de1f5ce43dda | -14.3394 | -48.025101 | 2026-08-01 00:31:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d560a3cd-cfaa-3a6d-81f3-f6d55e946ebd | -6.567 | -55.148499 | 2026-08-01 00:31:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79fc048e-7483-33cb-94db-51442283c43f | -18.5278 | -47.372002 | 2026-08-01 00:31:00 | METOP-B | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 285cb6c0-3437-3606-b710-6b8b7aa89404 | -5.5552 | -43.9814 | 2026-08-01 00:31:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db6af34c-2b00-3324-a668-b82999b94507 | 1.0963 | -60.507 | 2026-08-01 00:31:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a3a41beb-fa52-3bf7-9b7b-56ed54c8dd9a | -21.664499 | -56.300098 | 2026-08-01 00:31:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f6200dc6-af56-3a7f-afdb-1222d933af81 | -11.251 | -54.833599 | 2026-08-01 00:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8766a0d7-5755-3cfd-bd98-d81fb7b72601 | -5.5389 | -43.956699 | 2026-08-01 00:31:00 | METOP-B | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8acc2cd-8e8a-315f-aa89-351b33d9de25 | -11.2298 | -54.830898 | 2026-08-01 00:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8e2b8071-be2c-30f1-9d16-bf942701ffbf | -14.0752 | -46.257301 | 2026-08-01 00:31:00 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ef85d377-3763-3512-827d-c92f125a84e9 | -14.078 | -46.2272 | 2026-08-01 00:31:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca1e2e1b-04d5-3372-890f-6a06ad9b6107 | -4.3664 | -47.754902 | 2026-08-01 00:31:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acabd0b3-8e25-38de-8625-1411c9d26c1f | -18.4797 | -51.683899 | 2026-08-01 00:31:00 | METOP-B | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c0599242-9bdd-3cdd-92b8-31c134fffc04 | -13.9476 | -49.1399 | 2026-08-01 00:31:00 | METOP-B | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d00198e8-c16c-3bc9-8f5f-96f56fb1a287 | -11.2459 | -54.857201 | 2026-08-01 00:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a12ad023-5778-3fc9-916b-0730a5808729 | -17.0548 | -45.877701 | 2026-08-01 00:31:00 | METOP-B | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 57db9082-4322-3bbd-aa6d-8aaa5a62bda6 | -11.2427 | -54.842999 | 2026-08-01 00:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a95d74f-1867-3c26-8ffe-b34a71f3bd41 | -2.8774 | -48.0061 | 2026-08-01 00:31:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62a4b904-2c27-3480-9ce8-861bb730e8e0 | -6.5556 | -55.143799 | 2026-08-01 00:31:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1f12a11-eb7c-3a27-86fb-4dea3247391b | -11.2412 | -54.8358 | 2026-08-01 00:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f07f1e25-6408-3dc8-877f-21e6060daff7 | -18.518101 | -47.374599 | 2026-08-01 00:31:00 | METOP-B | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
