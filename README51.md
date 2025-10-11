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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91020f36-63a9-3609-becf-13be9788a370 | -11.892 | -45.4868 | 2025-10-11 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 2f7ae867-6e35-37d3-badc-0529d9c602ba | -11.7622 | -46.3487 | 2025-10-11 13:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| f34c34cc-2952-391f-8e0d-6b7e3908e4a6 | -9.1028 | -45.0248 | 2025-10-11 13:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| f3feb049-1ba5-3ff9-8482-ae052c71bd48 | -11.6469 | -47.5313 | 2025-10-11 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| edc0c453-4fe0-3cfd-a4c5-a2e5b0847184 | -10.9293 | -47.1553 | 2025-10-11 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 79bd94b0-3540-3a04-946e-c168c6127a99 | -13.8496 | -45.8223 | 2025-10-11 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| f575dae2-d5ad-3fdd-b4bd-50a0d772aac9 | -11.7809 | -46.3687 | 2025-10-11 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| e88437f1-4942-3860-be43-19a4006353b0 | -13.8491 | -45.8454 | 2025-10-11 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 26185c67-dddb-376f-abdf-a88bf1856b46 | -11.6282 | -47.5115 | 2025-10-11 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 067a66dc-ace5-38e9-b63e-0eed812eefb0 | -13.322 | -47.1144 | 2025-10-11 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 3ba33b5b-3e5f-3033-8678-3fefd3e9afbd | -13.7999 | -45.415 | 2025-10-11 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| e569e8de-fafd-371e-8264-ba38c990c4d1 | -13.3026 | -47.1174 | 2025-10-11 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 121.9 |
| de5ee9af-ca8a-3600-816e-cf31c47c54a4 | -10.5654 | -47.3556 | 2025-10-11 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 91f2a43e-91ba-3a7b-9c22-bbfb59236661 | -12.5093 | -47.4138 | 2025-10-11 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| fc828121-d962-3cfc-89d2-bdc11c7970da | -12.4705 | -47.4416 | 2025-10-11 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 0cdf18d0-f1b7-322c-9dd6-c14950dae448 | -10.2543 | -46.5892 | 2025-10-11 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 52aea1c4-d4d3-35cc-8aa9-410380cf1f24 | -10.9041 | -47.5588 | 2025-10-11 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| dd1e8ca0-db05-3db2-9ca7-b8f4096a2507 | -12.5097 | -47.3913 | 2025-10-11 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 4c324cd3-64f6-3d1a-ad56-a88b10bd3d3f | -11.6278 | -47.5338 | 2025-10-11 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 99d8cc9d-c1dd-3e26-9bad-7694d19c2d7b | -11.6469 | -47.5313 | 2025-10-11 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 18692f71-0ff3-32ce-b13a-f5a4e3266406 | -13.8496 | -45.8223 | 2025-10-11 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 8bd9903b-57e0-3cf5-a320-7ada3782cda2 | -10.5277 | -47.3379 | 2025-10-11 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8651c22a-1752-3cd3-8a9e-1ed7055114d8 | -9.4137 | -45.7861 | 2025-10-11 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 9c17cefe-d60d-317c-a4df-c13e2fe1177a | -11.7618 | -46.3714 | 2025-10-11 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 86be247b-b1db-3717-b5c6-7143c1d08a58 | -10.5654 | -47.3556 | 2025-10-11 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| ee94a849-0b85-36e3-a43b-9b4e65ba4105 | -10.6703 | -46.6954 | 2025-10-11 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| c42d2252-c0e6-3aa9-8fe6-630e56f5655d | -11.6282 | -47.5115 | 2025-10-11 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 6386c160-1b08-3880-8e47-317204f8f841 | -10.5464 | -47.3578 | 2025-10-11 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 1d67a318-3c5d-3db7-bffb-5ccf8f66c7a3 | -10.5274 | -47.3601 | 2025-10-11 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| bc965b3d-a111-3c3c-bf1b-0764bd2379c2 | -11.892 | -45.4868 | 2025-10-11 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 5536fb34-6d58-317b-9e42-d283badd05e5 | -13.3026 | -47.1174 | 2025-10-11 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| cedbe60e-4735-325d-afcb-1e166a52f209 | -11.7622 | -46.3487 | 2025-10-11 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 293d7d1e-5580-3a94-828f-d6e101a83d5c | -10.2085 | -44.6141 | 2025-10-11 13:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 8cdf4c6d-6f52-30af-b7d4-a8d5e6fb8ab2 | -13.322 | -47.1144 | 2025-10-11 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 43aeb7d1-1d4d-3d00-b737-fc4e386c12d0 | -15.0021 | -45.5725 | 2025-10-11 13:10:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 6460de76-fed3-39c3-bf88-1a3546c24952 | -9.1028 | -45.0248 | 2025-10-11 13:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 37c385cb-0c57-3907-8196-12bf10215dee | -10.9293 | -47.1553 | 2025-10-11 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 81f1f730-3b77-346d-9781-b5f290fafd63 | -11.7809 | -46.3687 | 2025-10-11 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| ea8ad505-dfed-3aa5-ac65-ff1d0727ecf8 | -13.8004 | -45.3917 | 2025-10-11 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| dc35dd11-68dc-3694-92a5-c070445c2cfb | -9.1024 | -45.0477 | 2025-10-11 13:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| a29bcaea-cc8f-3efa-9daa-a8a185363e37 | -12.4705 | -47.4416 | 2025-10-11 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 2c3dfe43-3061-38c3-9e41-995152fa3b80 | -12.5093 | -47.4138 | 2025-10-11 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 492445e6-b277-306d-a17b-15bd2e2f3117 | -10.8341 | -47.1671 | 2025-10-11 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 5073e5be-2597-3fb8-a8da-a86147b63ecc | -8.4838 | -46.1789 | 2025-10-11 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| d92f1d04-301d-3f88-a354-7a01c169274f | -12.5097 | -47.3913 | 2025-10-11 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| e4bdde0a-f6b9-388c-a27e-d811bf07c001 | -8.5021 | -46.222 | 2025-10-11 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| c0a75220-c5bf-3998-8e74-5ab4da49c678 | -11.7622 | -46.3487 | 2025-10-11 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 8136f814-8d44-3bfb-8036-795e17f70265 | -10.0934 | -45.9325 | 2025-10-11 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| b94a97d2-89e8-3fc1-ba30-e0cb79c088cd | -13.8496 | -45.8223 | 2025-10-11 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 6c8f999f-3065-3f2c-9f2f-9969afa6808a | -8.4841 | -46.1564 | 2025-10-11 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 90a2b727-e169-3ff6-97e5-2bc77460ebc5 | -13.3026 | -47.1174 | 2025-10-11 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 0831caa2-084c-31e3-9793-6485aad11622 | -10.2543 | -46.5892 | 2025-10-11 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 3bc888e4-0775-3991-abbd-7b969ac7ea2e | -11.6469 | -47.5313 | 2025-10-11 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| d882a910-622e-3e47-bb37-c4158b07eeb8 | -13.322 | -47.1144 | 2025-10-11 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 275229b5-9f57-3105-8c8d-4d2aaed31bd1 | -10.9041 | -47.5588 | 2025-10-11 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 8b70a79c-b62b-3e5f-ad31-05d830436c4a | -11.7809 | -46.3687 | 2025-10-11 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 4904eebd-475b-3f34-9a73-231c7a0ecde2 | -8.5018 | -46.2444 | 2025-10-11 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 80040ab7-be07-3962-8836-4b5aa257af87 | -11.6278 | -47.5338 | 2025-10-11 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| fca037f4-279c-3227-8e05-cdeee544f3b0 | -8.4835 | -46.2014 | 2025-10-11 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 99abf087-0c8c-3e37-bf47-66ee8250c92e | -9.3947 | -45.7882 | 2025-10-11 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| e64da061-9267-39ae-9d9d-7341f8e18563 | -11.6282 | -47.5115 | 2025-10-11 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 19974ee8-7350-33b6-9e45-1e70e5cf3469 | -8.4833 | -46.2239 | 2025-10-11 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 141.8 |
| cdac74b4-df26-328e-a107-5083eabc6b89 | -10.0937 | -45.9098 | 2025-10-11 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |
| cc4b89ee-8a35-302a-a661-f0f9be4d547b | -13.7999 | -45.415 | 2025-10-11 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 4f357434-0b9a-30e5-a8a0-c5d0fe09845e | -10.0747 | -45.9121 | 2025-10-11 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 240.1 |
| cead9703-915f-301e-ab16-2063a895729e | -15.5592 | -44.3367 | 2025-10-11 13:20:00 | GOES-19 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 129.2 |
| 48d30524-39b3-3679-8a59-810c50084dec | -9.4137 | -45.7861 | 2025-10-11 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| ce9cc0c7-74fc-38ca-82c8-298fa0c5622f | -10.9293 | -47.1553 | 2025-10-11 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 7a38c1d3-a1b0-37b9-94e9-c9e035c0c301 | -15.0021 | -45.5725 | 2025-10-11 13:20:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 4dab151e-1af1-32d6-980b-3f22e47a71b8 | -9.0022 | -45.4693 | 2025-10-11 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 43a38ff3-46d6-30a6-a59b-7d825df48948 | -9.697 | -45.8213 | 2025-10-11 13:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 64b0efd5-91d8-3d73-ba15-eff72358625b | -12.5097 | -47.3913 | 2025-10-11 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| af8fdbba-ab26-3a93-b92b-cfc75db1180b | -10.9231 | -47.5564 | 2025-10-11 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 9aece49d-d67f-3a7c-af01-2829497ad2f1 | -10.0934 | -45.9325 | 2025-10-11 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 9af84f15-b475-3a02-8503-9619bcab9204 | -9.4137 | -45.7861 | 2025-10-11 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 742c489d-d646-398b-b930-c8edaa5285f2 | -13.7927 | -45.7627 | 2025-10-11 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| e747f2ce-45df-369f-b460-59b463383cf6 | -10.6703 | -46.6954 | 2025-10-11 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 5ffea77f-8b47-3b6f-bcfa-d22f9c8a5776 | -13.7999 | -45.415 | 2025-10-11 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 8243ba4d-56c8-34af-97c5-079b48623002 | -8.5416 | -44.6054 | 2025-10-11 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 114.9 |
| e279523b-5875-3ab2-a6e4-84273d1ee973 | -9.3951 | -45.7655 | 2025-10-11 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| f77be236-a5b7-35c5-b2d6-ea91fdf21f7f | -11.7809 | -46.3687 | 2025-10-11 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 276b5c2a-da05-3957-810e-611b37171ef5 | -13.3026 | -47.1174 | 2025-10-11 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 155.4 |
| edf90547-630a-35a2-8ff8-f8e4f6281437 | -10.2088 | -44.591 | 2025-10-11 13:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 3417df5f-60df-3364-8fc5-c38258e233d9 | -10.9041 | -47.5588 | 2025-10-11 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 4e04d50c-fb81-312c-a87b-4608f97f80db | -9.3947 | -45.7882 | 2025-10-11 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 10ee04f7-54f7-31b5-9fdf-a67d72c58ada | -8.5029 | -46.1545 | 2025-10-11 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| fc92fa61-e8a6-3996-9651-610c65bd2a11 | -10.0747 | -45.9121 | 2025-10-11 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 228.2 |
| b239bc67-e3f1-3da6-b910-5f5bfc8b9847 | -14.983 | -45.5528 | 2025-10-11 13:30:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 180.7 |
| 9334cad9-ddfc-3997-adbe-360784d9594a | -8.5605 | -44.6034 | 2025-10-11 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 6ab9b341-4b70-35a8-b684-2e80a052b384 | -13.8501 | -45.7992 | 2025-10-11 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| f6142fe7-6ef9-3bcb-8640-78892a92f9c6 | -14.9825 | -45.5761 | 2025-10-11 13:30:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 153.8 |
| aac84ba8-6d84-32bc-8192-fc7046ebb3e1 | -13.8004 | -45.3917 | 2025-10-11 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 4e5b810e-426d-352d-871c-7a0f6c144d8e | -8.5227 | -44.6075 | 2025-10-11 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 106.9 |
| ba2db5a5-f621-35ea-a218-b792bbb784fa | -13.8496 | -45.8223 | 2025-10-11 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 2793de0e-ea59-3708-b79e-8b75b92d6df6 | -10.9293 | -47.1553 | 2025-10-11 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| c47c871e-7a81-3b52-8192-37ad3081eb66 | -9.6974 | -45.7986 | 2025-10-11 13:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 5bac4320-534c-3c48-aa65-c8945f1b084d | -10.0937 | -45.9098 | 2025-10-11 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 160.4 |
| c5728687-734d-3d0c-8d14-827e8e50dbc7 | -15.0021 | -45.5725 | 2025-10-11 13:30:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 250.6 |
| 9cf0876f-0c7c-39d1-92a6-224a9fac7941 | -12.7299 | -45.8422 | 2025-10-11 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| e571c938-8e79-3683-90ba-78c5f6b43534 | -13.322 | -47.1144 | 2025-10-11 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 113.6 |


[Clique aqui para ver as próximas entradas](README52.md)
