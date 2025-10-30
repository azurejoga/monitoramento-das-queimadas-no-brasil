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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e98c448-e10c-3e72-8eff-bccfdda35f8b | -3.2169 | -54.74993 | 2025-10-30 12:57:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a18f027e-b423-36eb-8ac9-eb0a555c850d | -1.94244 | -56.88152 | 2025-10-30 12:57:00 | TERRA_M-T | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fe8281b9-92bf-3be0-a7ab-4c54eaac578a | -3.7364 | -53.33031 | 2025-10-30 12:57:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c9493715-bb5e-34fe-a7bd-da07887b955d | -4.5316 | -54.96284 | 2025-10-30 12:57:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b3ca6e45-1c34-377b-9d08-310e542f4fe2 | -11.12698 | -51.04584 | 2025-10-30 12:59:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 4f43416e-9d23-3b34-8ede-67ac73535973 | -11.12112 | -51.09419 | 2025-10-30 12:59:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 146.6 |
| a2b398ee-0937-3608-be97-8503b7e380ca | -11.31113 | -51.44321 | 2025-10-30 12:59:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 40.4 |
| c6c33a5c-4e23-3700-99ea-95aa65551879 | -11.11593 | -51.01984 | 2025-10-30 12:59:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 49bbbbfe-d398-32e1-b355-e8d1fb0eac93 | -11.11565 | -51.07462 | 2025-10-30 12:59:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 419.7 |
| 8a33fe79-b3d4-3f64-8fa4-42f015d91a15 | -13.37537 | -54.30444 | 2025-10-30 12:59:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| a66bff04-32a5-33e7-a651-bee1d93e7b69 | -11.11292 | -51.09877 | 2025-10-30 12:59:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 1caa83b8-d3f0-3e28-ad8b-5cf2fbd556b9 | -11.11838 | -51.05037 | 2025-10-30 12:59:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 146.7 |
| e41b7d57-903a-3b94-abdb-8bbf9d6574e8 | -11.12683 | -51.10043 | 2025-10-30 12:59:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 40.4 |
| df4c110e-d6b6-398e-b9a7-e719d2992fcc | -11.11302 | -51.04419 | 2025-10-30 12:59:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 780c6a44-1be7-3ce2-9749-6d1d8c9b6dc7 | -14.48826 | -51.51372 | 2025-10-30 12:59:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 35241f92-65b7-3a98-9ff6-ed999dfa7d1e | -14.04603 | -52.77747 | 2025-10-30 12:59:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| baa5e9f3-923b-3033-8cb6-5b9a8dda2f21 | -11.19791 | -48.59653 | 2025-10-30 12:59:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 7e5782a8-20fd-3f17-b0c0-d82e5a6cbe90 | -11.11675 | -54.03918 | 2025-10-30 12:59:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c85fab3d-7afd-3898-af32-76826b2aef99 | -13.36242 | -54.31763 | 2025-10-30 12:59:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 96b4bc56-d1a5-36d0-a033-b55b672ae4a8 | -11.12113 | -51.026 | 2025-10-30 12:59:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 8cce7b1c-2707-3edd-b069-24d6d9a279f9 | -11.12958 | -51.07628 | 2025-10-30 12:59:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| e997cd19-ea61-3b0e-b11b-c53a1132b543 | -14.04641 | -52.78332 | 2025-10-30 12:59:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 40a895a3-8aca-39e2-957a-0c8db08748de | -11.12405 | -51.07006 | 2025-10-30 12:59:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 35ba5cc8-0beb-374b-a7e3-b8419b743e50 | -11.11011 | -51.06843 | 2025-10-30 12:59:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 341.2 |
| aa825e86-97c6-3ade-b8d0-99b0e18b8d5a | -11.10722 | -51.09256 | 2025-10-30 12:59:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.6 |
| fc6b7124-801a-3229-a0a5-6f16ad58aaed | -3.7867 | -43.9011 | 2025-10-30 13:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| e1e3e2ad-bad2-34c7-b366-bc7f3875b0c2 | -4.2544 | -43.7149 | 2025-10-30 13:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 472a4f40-2659-34ad-acab-283fd7ef48a7 | -15.1607 | -47.2438 | 2025-10-30 13:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 07d3b153-9ad2-3e3d-a907-7229f0cf0134 | -13.2271 | -47.0387 | 2025-10-30 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| a915e714-1baa-3d99-9e00-07d0d7e34178 | -13.0446 | -47.5379 | 2025-10-30 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| aec41ffa-a541-3876-82a5-56e45d09e6ca | -4.2731 | -43.7139 | 2025-10-30 13:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 148.0 |
| c0bb5c2d-8e1b-34b0-b56c-dde16014bf33 | -12.6639 | -47.3469 | 2025-10-30 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 40958e9a-b661-3b9d-957c-b790dd92817c | -13.5876 | -47.3438 | 2025-10-30 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 2da20622-90d5-3624-a886-83c09f36a65f | -3.8605 | -44.0355 | 2025-10-30 13:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 36b3688e-9738-314b-8637-05f1465a72be | -15.1607 | -47.2438 | 2025-10-30 13:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 145.2 |
| e4f9d857-1829-3b0a-bb79-6ab5ee2c66d2 | -13.5876 | -47.3438 | 2025-10-30 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 94.5 |
| ef01227b-6faf-3ccd-936c-292618947494 | -13.0446 | -47.5379 | 2025-10-30 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 853eab11-459c-3af6-a350-cf1926996600 | -6.1462 | -41.5996 | 2025-10-30 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 658be2ac-7895-376f-8f1d-28c474b52493 | -4.2731 | -43.7139 | 2025-10-30 13:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| c9aac2b4-b588-3743-84ce-f4b7235fbae9 | -5.2496 | -40.9731 | 2025-10-30 13:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 121.3 |
| ed14bc66-61d2-345e-a413-0a026f243734 | -3.8054 | -43.9002 | 2025-10-30 13:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| f706bc8e-8497-34c3-9fdb-7836a51afcb2 | -4.2544 | -43.7149 | 2025-10-30 13:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 8de1340f-4563-38f3-99b7-d4835fc4b256 | -12.6639 | -47.3469 | 2025-10-30 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 4eb03836-c33e-3d0f-bd4d-2b1ee449d83e | -3.7867 | -43.9011 | 2025-10-30 13:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 23052c8e-4f7c-3210-ab2b-24800cf93f8f | -13.5686 | -47.3242 | 2025-10-30 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 205f049c-ae2a-31d8-ad26-972815c13005 | -13.5686 | -47.3242 | 2025-10-30 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 2332d3de-1992-3cc3-bf3a-06fe5920e114 | -15.1607 | -47.2438 | 2025-10-30 13:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 69e7f201-ba7c-38ab-9fb7-2d23e8a616ab | -12.6639 | -47.3469 | 2025-10-30 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 2a420b34-f38a-3b7c-abc1-0bcc664ebf60 | -13.3656 | -44.8847 | 2025-10-30 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| fbda9aa1-202d-3115-8a5d-41693a2815d3 | -3.4581 | -42.637 | 2025-10-30 13:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 58a73850-2b8f-3de2-8898-b5d526e7a277 | -13.0446 | -47.5379 | 2025-10-30 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 380c2417-f824-3986-a630-9519289ce3b6 | -13.5876 | -47.3438 | 2025-10-30 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 139.5 |
| b0dbef12-6878-315b-ba87-4279903e3052 | -4.2544 | -43.7149 | 2025-10-30 13:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 81c1f627-98f9-3c96-a1d2-fd1279b0bfe8 | -4.2731 | -43.7139 | 2025-10-30 13:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 33a1d9b4-ac63-3961-beea-fa09c4d106c5 | -13.725 | -43.4529 | 2025-10-30 13:20:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 6fec9b9a-a8de-3e43-bfc1-bd9254d6f8f2 | -5.2496 | -40.9731 | 2025-10-30 13:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 139.0 |
| 8217e7a3-81e7-3836-9a24-2b6cbeac272e | -6.1462 | -41.5996 | 2025-10-30 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 134.6 |
| 860bcac4-82fa-32d2-a722-6ca963e4f15e | -3.7767 | -42.4798 | 2025-10-30 13:20:00 | GOES-19 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 121.7 |
| d0d7aa0b-1380-35fb-a78c-7cd9ee0c9d48 | -5.6992 | -43.1541 | 2025-10-30 13:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 94.2 |
| 7dcc0781-4403-3f43-a6ac-7b9f6288d875 | -3.7867 | -43.9011 | 2025-10-30 13:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 5d283b7a-47c6-344a-9ce2-a5d1edb5dd98 | 1.6204 | -55.6865 | 2025-10-30 13:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 82d26322-8607-373d-bdd2-666dead3207e | -13.0446 | -47.5379 | 2025-10-30 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| f79ed0ed-2d98-3ca4-869f-3fa6993b194a | -13.5686 | -47.3242 | 2025-10-30 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 100.0 |
| e875b350-fc4b-3316-ac77-cff5bec8588f | -13.3656 | -44.8847 | 2025-10-30 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| bb9ca51c-6464-3736-9b5a-b95318d86bb6 | -12.9323 | -47.3752 | 2025-10-30 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 8e759113-1ed7-3381-8b01-26ae2c8f6b1d | -6.1462 | -41.5996 | 2025-10-30 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 170.7 |
| e8eafb60-5c91-36bf-9bb8-bad61e6c909f | -6.1464 | -41.5755 | 2025-10-30 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 112.2 |
| ccb95ccc-5e7e-3d33-8cb0-034379fef07e | -5.2496 | -40.9731 | 2025-10-30 13:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 154.4 |
| 0da06d8e-83d5-3c22-ba02-33cac074f81a | -5.6992 | -43.1541 | 2025-10-30 13:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 7806b67b-86b1-3ba1-b990-c660338eff28 | -5.7963 | -40.8312 | 2025-10-30 13:30:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 85.6 |
| aceefc05-e0c4-3be1-bef8-a7e5928fb79b | -4.2544 | -43.7149 | 2025-10-30 13:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| d30576ec-2e0d-3bb7-843f-ce9d55fd5b43 | -15.1607 | -47.2438 | 2025-10-30 13:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 3a9efaac-4b87-38fc-8afa-5855f40beb2c | -4.2731 | -43.7139 | 2025-10-30 13:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 3369c647-804e-3c79-9450-3fc28a97bc0d | -5.6065 | -45.1852 | 2025-10-30 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 4fe11517-ae72-3d97-b1da-d3fdf6f98ea0 | -3.7867 | -43.9011 | 2025-10-30 13:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 1b5cb59b-6e9c-3144-8da3-09cd1fb6d144 | -5.8152 | -40.8296 | 2025-10-30 13:30:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 131.1 |
| 9ae06f0c-a6f7-351e-ae32-22a763e4c187 | -3.7767 | -42.4798 | 2025-10-30 13:30:00 | GOES-19 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 7eebd5c8-769a-30aa-b752-41a8ae5717b2 | -13.5876 | -47.3438 | 2025-10-30 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 73e83866-d33b-347d-8412-955f37cfcbc5 | -6.93 | -42.2449 | 2025-10-30 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| cab7b542-12a3-31f3-a743-dbb2a3ac500f | -6.1276 | -41.5772 | 2025-10-30 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 132.1 |
| 4417f1fb-600d-3eca-ad12-e50f5d62bd61 | -13.725 | -43.4529 | 2025-10-30 13:30:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 8685dac0-f266-379f-a062-61bb862452ad | -6.0108 | -41.9708 | 2025-10-30 13:30:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 42457876-561b-390e-98be-23c0020d1895 | -6.2758 | -41.8042 | 2025-10-30 13:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| b037ebbd-d757-35d4-a374-d6a946ff578b | -4.4763 | -44.0252 | 2025-10-30 13:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 5aa4e904-b8ab-3583-8729-7c70ae785f78 | -6.0461 | -44.1484 | 2025-10-30 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 153732f9-3c5f-37e0-9502-c3646dda789e | -4.495 | -44.0241 | 2025-10-30 13:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 75170814-883f-3b7a-8be7-5d33bbea1882 | -5.6992 | -43.1541 | 2025-10-30 13:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 8ca32eb6-e51c-3f23-af2d-24a358479f23 | -6.0106 | -41.9947 | 2025-10-30 13:40:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| 11fb07ac-8cb9-3665-ad3e-d2d7743b5dcc | -3.8605 | -44.0355 | 2025-10-30 13:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| b2ae2738-eb6c-36a8-85db-7bca234d3e3a | -4.2731 | -43.7139 | 2025-10-30 13:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 08c22f25-752b-3fbd-900b-cf9f8257524e | -6.2785 | -45.3169 | 2025-10-30 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 0b726b16-af52-3d9a-805e-950917e40d32 | -5.2496 | -40.9731 | 2025-10-30 13:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| ed2f733b-cb45-3bfd-a516-0c8bb6356011 | -13.0446 | -47.5379 | 2025-10-30 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 356df8a3-56bf-3cf5-affb-b1a1afebab02 | -13.3656 | -44.8847 | 2025-10-30 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 9ef21c5c-a704-396a-9fd7-68a1722a76bb | -3.7767 | -42.4798 | 2025-10-30 13:40:00 | GOES-19 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 9933b7df-7a50-3be9-9bd2-fb9c601c49f8 | -3.995 | -43.4047 | 2025-10-30 13:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| a262e640-29dc-34f4-a0c0-fd54dcf4e446 | -13.0404 | -46.7282 | 2025-10-30 13:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 104.1 |
| d230c0f7-2b16-3137-ac90-5324b1ecc8e2 | -3.9949 | -43.4279 | 2025-10-30 13:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 00a1f07b-ddfd-3cc2-b536-c9ee703f2f21 | -13.725 | -43.4529 | 2025-10-30 13:40:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 16f4e6a0-afbd-37dd-8a69-acf2c0e202c9 | -12.2897 | -50.2712 | 2025-10-30 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |


[Clique aqui para ver as próximas entradas](README69.md)
