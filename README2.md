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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 296282ff-735c-3645-9ed2-953c139d3093 | -2.6722 | -49.834202 | 2026-01-06 00:02:00 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eb763b6-153f-3043-bde0-5e344665e637 | -1.3597 | -49.401199 | 2026-01-06 00:02:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71ca0533-0394-3f3a-ae89-4d996c39b6d7 | -5.0442 | -43.590401 | 2026-01-06 00:02:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef334abb-37be-3364-9438-a4f95fd90a38 | -2.8466 | -48.642502 | 2026-01-06 00:02:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b73ba48c-cb44-3fac-ac44-bedd2c4bb5ec | -5.8938 | -39.214699 | 2026-01-06 00:02:00 | METOP-B | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3ef40147-4af2-34cd-bcca-d28ba5accb04 | -2.5162 | -47.818501 | 2026-01-06 00:02:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 863ba3a6-bead-302a-a763-7633dc875b6f | -2.5358 | -47.814098 | 2026-01-06 00:02:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65ad19e5-4c64-3644-a426-88be74118b09 | -5.3826 | -43.183399 | 2026-01-06 00:02:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1dd4bebf-9114-39ec-b4d0-9a68245bfa8d | -4.5777 | -43.801498 | 2026-01-06 00:02:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 365d0dd4-c05d-3939-92b5-1ccbe69c239a | -1.1432 | -48.080601 | 2026-01-06 00:02:00 | METOP-B | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4068256-460c-3d66-b43f-31d873ed68c5 | -3.2521 | -42.527302 | 2026-01-06 00:02:00 | METOP-B | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72a30769-086c-3f97-940f-d4c31923f473 | -5.3786 | -43.1661 | 2026-01-06 00:02:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ff17bfa-9208-31f8-8c9e-db06c5cae1a1 | -4.1493 | -47.4767 | 2026-01-06 00:02:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73915354-2081-348e-954a-965f103be8f4 | -5.3708 | -43.176998 | 2026-01-06 00:02:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65133fc4-6961-3204-8bc8-39d3acb3ea53 | -21.020901 | -48.484402 | 2026-01-06 00:02:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 95fd3080-5f8e-3556-a261-d76da8fafe12 | -4.1462 | -43.629299 | 2026-01-06 00:02:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c572b1a-a772-3f12-8d67-0ec0ffafcac7 | -4.7027 | -43.985802 | 2026-01-06 00:02:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d41c7c15-4250-3ab1-b6a8-89666706010f | -6.3358 | -39.5966 | 2026-01-06 00:02:00 | METOP-B | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9974f5bc-1a0f-3fcb-bf4c-cc2147808aea | -9.9767 | -36.078701 | 2026-01-06 00:02:00 | METOP-B | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ca09295a-8784-313d-b7d7-e54342c502c6 | -3.6991 | -43.433701 | 2026-01-06 00:02:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a77013f8-ed97-31a3-be79-ca4815e04383 | -21.023001 | -48.495899 | 2026-01-06 00:02:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cf9a499d-e8ff-3bf4-afa9-3c5f471e7428 | -6.5729 | -38.414501 | 2026-01-06 00:02:00 | METOP-B | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 99914a9c-e54d-33b8-a4a9-427973e617bd | -4.0112 | -48.052101 | 2026-01-06 00:02:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6612bd6c-eb7b-3f73-8069-cf4b3d786080 | -2.845 | -48.635399 | 2026-01-06 00:02:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0482f0c2-73ce-3bbe-b2b6-2bd3ae32d9e3 | -0.3677 | -48.432899 | 2026-01-06 00:02:00 | METOP-B | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf27e4e2-ffcb-3996-9b24-67511e882d0a | -2.3381 | -47.8508 | 2026-01-06 00:02:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e46aec6-0fa8-3421-a817-810facd0d27b | -2.5467 | -48.9109 | 2026-01-06 00:02:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0258724b-3bbc-3665-b4ff-02e6e8b34584 | -2.6475 | -45.629799 | 2026-01-06 00:02:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb1bb11f-e781-3538-a095-13ed2db56133 | -20.5279 | -58.0039 | 2026-01-06 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.5 |
| aa4dfdec-a69c-3bdb-8a41-7523bd3233d9 | -2.6431 | -45.6499 | 2026-01-06 00:10:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 04748c78-15ef-3eee-b1d5-7c757b45dc56 | -2.2662 | -53.7825 | 2026-01-06 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 4ce2403e-1ee7-3ed6-adb5-babda3294f6c | -2.2846 | -53.7822 | 2026-01-06 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 712c0573-dbb5-35e1-b940-30f29c412cfa | -21.0345 | -48.5034 | 2026-01-06 00:10:00 | GOES-19 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.2 |
| c35ba6ee-6886-3b62-a81e-4f7bd1a3b9f1 | -20.5077 | -58.0066 | 2026-01-06 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 02bbf86b-a763-3706-8a77-bc2f9f721772 | -22.4849 | -46.9429 | 2026-01-06 00:10:00 | GOES-19 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 03299feb-d03d-3701-b711-7cdcf0c99471 | -22.5059 | -46.9374 | 2026-01-06 00:10:00 | GOES-19 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 96.4 |
| b9a97163-056a-30aa-9588-e4a2b3da726d | -20.5279 | -58.0039 | 2026-01-06 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.4 |
| fac8d194-fdfb-3f42-8f91-d6b20c131453 | -20.5077 | -58.0066 | 2026-01-06 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.9 |
| f2beab4c-50f8-360c-9513-1e5d492dc620 | -22.4849 | -46.9429 | 2026-01-06 00:20:00 | GOES-19 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 0842012d-60c9-3423-b4d4-132c8f52dc46 | -22.5059 | -46.9374 | 2026-01-06 00:20:00 | GOES-19 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 110.2 |
| fe84a837-901c-3091-92d6-09721d5344da | -2.5238 | -47.8332 | 2026-01-06 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 65e6733c-cff1-3746-a55b-8c7ceb4546d1 | -5.3802 | -43.2013 | 2026-01-06 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 2491be7a-2aed-3a1e-9b14-73d1d02ec236 | -10.2193 | -36.2892 | 2026-01-06 00:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 79.4 |
| c8cee371-c226-3b89-924c-d6869bb299f0 | -2.6431 | -45.6499 | 2026-01-06 00:20:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 126.7 |
| af72007f-ef4f-3b2a-95bb-382bfdc23afc | -3.6962 | -43.4432 | 2026-01-06 00:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 50e26697-20e6-38cc-8e67-e27c7fd68e45 | -2.2662 | -53.7825 | 2026-01-06 00:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 437be4a4-0a8b-3430-b82a-396bf33426ed | -22.5059 | -46.9374 | 2026-01-06 00:30:00 | GOES-19 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 1c38134a-e283-308f-8a80-e89664493017 | -2.6431 | -45.6499 | 2026-01-06 00:30:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 5d9c045b-e4a2-35c8-ac09-d145d5732071 | -2.5238 | -47.8115 | 2026-01-06 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 808971c7-8802-3935-ab98-386c58f16b76 | -2.5238 | -47.8332 | 2026-01-06 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 153.3 |
| 9022e46d-83d0-34d4-95b7-48d61128ceae | -2.2662 | -53.7825 | 2026-01-06 00:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| e97db7c2-e9e3-3829-bea3-60e9350876e6 | -3.6962 | -43.4432 | 2026-01-06 00:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| c98b16be-55d3-32ea-afd2-fcac42b6602f | -2.5423 | -47.8327 | 2026-01-06 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 042b9872-52b6-3982-a4bc-0ffe822a1236 | -20.5077 | -58.0066 | 2026-01-06 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.7 |
| a635b1f0-46d2-3a99-b015-3098e9678f5d | -20.5283 | -57.983 | 2026-01-06 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 41ec2aca-e6ed-3423-9e56-64de71907e38 | -20.5279 | -58.0039 | 2026-01-06 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 230.6 |
| 18345e46-2073-3fe3-a561-d6700b84f4dd | -20.5077 | -58.0066 | 2026-01-06 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.9 |
| b2a38924-9ca2-336f-92e8-f3efae10455f | -22.4849 | -46.9429 | 2026-01-06 00:40:00 | GOES-19 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 65b046ba-7155-3faf-b443-1b00ead42535 | -2.5238 | -47.8332 | 2026-01-06 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 472411da-d3d8-35ad-9b1f-756758afbbdf | -2.5238 | -47.8115 | 2026-01-06 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| ab7acd86-efec-3003-8fbb-bbb01e0b4191 | -2.5423 | -47.811 | 2026-01-06 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 9819e10a-467f-38db-8822-9af493beed74 | -2.6431 | -45.6499 | 2026-01-06 00:40:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 1648e1ca-e1ad-3ad4-87da-dc69e2472c1f | 2.5442 | -60.3563 | 2026-01-06 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 43.1 |
| fd6ac1c1-709e-30cc-9782-f7a4a5bf07d8 | -3.6962 | -43.4432 | 2026-01-06 00:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 69038b4d-0dd2-3c68-92b9-d7a5ffa83eb5 | -22.5059 | -46.9374 | 2026-01-06 00:40:00 | GOES-19 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 69ad80f0-e1e2-396f-bf22-9d2bf31a6519 | -2.5423 | -47.8327 | 2026-01-06 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 00961790-ec3b-3586-8516-80b7756635e9 | -20.5279 | -58.0039 | 2026-01-06 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 162.5 |
| cf4ba085-cf02-3fd7-8081-301af44ce87e | -2.9829 | -48.580399 | 2026-01-06 00:41:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a6e0ac8-7e54-356a-878a-c8c308873c09 | -2.9297 | -48.214298 | 2026-01-06 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f75cdd0-f2a8-305a-b291-ce1e3d3dfe58 | -3.1825 | -51.079102 | 2026-01-06 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48da6bcb-f33e-31cd-9832-b6f17375f2f3 | -1.5972 | -53.978199 | 2026-01-06 00:41:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6ccb795-8683-3d82-8733-1699d53b458a | -2.9313 | -48.221199 | 2026-01-06 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d3555aa-7b89-3e5f-81b4-9639f36cba2b | -1.3566 | -49.4035 | 2026-01-06 00:41:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3914edd-6d4b-3ff9-9ebd-385ac435d499 | -0.3708 | -48.432999 | 2026-01-06 00:41:00 | METOP-C | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3a59f50-0b9f-34dc-a551-17745e23949a | -3.1841 | -51.086399 | 2026-01-06 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab88961b-27a4-3195-89aa-074a3bdfbdd3 | -2.9845 | -48.587299 | 2026-01-06 00:41:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27b44c90-a14e-302a-8869-2ae41c1b24e8 | -2.6544 | -45.643002 | 2026-01-06 00:41:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 19619f2f-c065-3fbc-a2c1-63a861745194 | -2.5415 | -47.8274 | 2026-01-06 00:41:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71df9f48-b64b-370e-84f3-6459c0282295 | -1.5994 | -53.9879 | 2026-01-06 00:41:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c90ffccc-c3b2-3d53-b50e-8cd83669670a | -2.6446 | -45.645199 | 2026-01-06 00:41:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 20344abe-9845-38a3-bde3-fcb8033e7b22 | -1.1506 | -48.101799 | 2026-01-06 00:41:00 | METOP-C | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b05c6fc-0844-3cfa-983e-5e314b88fc5e | -2.5186 | -47.817501 | 2026-01-06 00:41:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ef888c4-5822-3de0-9bc1-7e2801d48a14 | -1.1489 | -48.094601 | 2026-01-06 00:41:00 | METOP-C | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6efb58a-4196-3c84-b61a-5aa410cb6c84 | -1.3582 | -49.410301 | 2026-01-06 00:41:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d384c4b-5d81-3da7-9016-ff353de5d970 | -4.0179 | -48.057598 | 2026-01-06 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60ae9e90-9a35-3554-85c3-7fa7fc7f5a0a | -2.1786 | -48.132401 | 2026-01-06 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9308f78e-a61f-32f1-81f9-f5b4d81de804 | -2.6564 | -45.651699 | 2026-01-06 00:41:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 36196f2a-4fa0-38ed-a79f-a9f7354414ee | -1.1473 | -48.087502 | 2026-01-06 00:41:00 | METOP-C | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4095fd95-9e28-3e2a-b838-3a6738397b68 | -2.0958 | -53.502701 | 2026-01-06 00:41:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85d8fea2-44db-3560-8de3-990b9a4e2cb7 | -2.9329 | -48.228199 | 2026-01-06 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc04c3ac-9f7d-3d66-810b-e90bfeae0e52 | -2.3612 | -47.6717 | 2026-01-06 00:41:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d96e6a8a-401a-3c10-9852-88f62edfd595 | -2.5382 | -47.813099 | 2026-01-06 00:41:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2a53f9c-a750-327e-8bed-d8950cbd2179 | -2.5317 | -47.829601 | 2026-01-06 00:41:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7d3e3cc-a36c-3635-b75b-c868ac8e05f0 | -2.6466 | -45.6539 | 2026-01-06 00:41:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1312edea-417a-364b-9ef2-731e63bb2e39 | -2.5284 | -47.8153 | 2026-01-06 00:41:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 157a3170-ef0b-36d0-aa33-c464a37d6e75 | -2.5203 | -47.824699 | 2026-01-06 00:41:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 794e7e9b-6657-391b-9fdf-1d3ab40d1df4 | -2.6426 | -45.636398 | 2026-01-06 00:41:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3b671299-53fb-32d5-8fac-d02a94076276 | -2.1656 | -47.896801 | 2026-01-06 00:41:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7d6e3bd-bcd6-3e4b-9320-f6e870fa32af | -2.5399 | -47.820301 | 2026-01-06 00:41:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b909085-095f-308c-aff3-dae7931d190f | -0.0939 | -51.274101 | 2026-01-06 00:41:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
