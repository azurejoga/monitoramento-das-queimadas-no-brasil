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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9f045b8-b174-3e0c-9c0a-2dbce3242f27 | -11.3081 | -51.0676 | 2024-10-08 02:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 147.5 |
| e54f7758-3c61-3b3f-83ab-c6c42ceb7b08 | -11.309 | -51.0038 | 2024-10-08 02:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.7 |
| fe0d62c6-8ef7-3499-a7f5-16c511ef80ed | -11.347 | -50.9997 | 2024-10-08 02:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 9c1ef347-8991-3eb3-b6dd-71c50d5cff08 | -11.3283 | -50.9805 | 2024-10-08 02:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 775dfc9f-eb89-3774-84a2-ec51f08749e7 | -11.3093 | -50.9826 | 2024-10-08 02:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| ab43d071-c34c-3dda-a61f-c93ae5f22081 | -11.328 | -51.0018 | 2024-10-08 02:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 762e5d42-1e7c-37d9-9d5d-ab5a9b83b575 | -11.5421 | -65.1362 | 2024-10-08 02:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| ada25993-47a7-38bc-9a63-c5063f7138b1 | -11.5233 | -65.137 | 2024-10-08 02:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 4e7c0ed1-d824-3777-bcc3-b635e21ba071 | -11.5232 | -65.1559 | 2024-10-08 02:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 1407b6a0-bafb-3375-a49e-5c3b00f8e625 | -11.6808 | -64.0121 | 2024-10-08 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 82a49ff9-b81d-31ed-9a45-d6b345983e15 | -11.6806 | -64.0312 | 2024-10-08 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| b26d35f3-a0e6-33f5-8feb-28795fa3b261 | -16.5897 | -46.4979 | 2024-10-08 02:06:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 9ebc5d7b-73fe-3e1d-990f-f6b0ec74ee1c | -16.5902 | -46.4746 | 2024-10-08 02:06:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 62.7 |
| c2862403-ef2d-324e-af24-4c0672682f13 | -16.5752 | -55.9055 | 2024-10-08 02:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 30.0 |
| 1ed90fe5-b55d-37ab-8971-d77f19c674be | -16.5462 | -57.7344 | 2024-10-08 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 15bd9757-f5ee-3558-8e07-4eea3d2b36ba | -16.673 | -57.1077 | 2024-10-08 02:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.8 |
| bb886b77-54bb-3306-ad1c-fb62b8165acb | -16.6531 | -57.1305 | 2024-10-08 02:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.6 |
| 99c8bf55-ed5f-30c4-b47e-1c82a45f496e | -16.9214 | -57.4676 | 2024-10-08 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.8 |
| 237678d8-c8e3-376d-9cbf-c681837e63ac | -16.9211 | -57.4881 | 2024-10-08 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.2 |
| ea01385d-4af1-3ec9-81c5-e198f3b9ccca | -17.0992 | -57.3651 | 2024-10-08 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.3 |
| 41f2554d-4c13-3f80-af60-7f8f558454dc | -17.0123 | -56.6773 | 2024-10-08 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.9 |
| f93f796a-298f-3619-9483-1d160207748d | -18.6192 | -57.2603 | 2024-10-08 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.3 |
| d3a97bba-554c-3384-a7a5-5ff5a35e1431 | -18.6195 | -57.2396 | 2024-10-08 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.9 |
| 656624be-34a7-3ae0-bef2-89482b713bf5 | -18.6394 | -57.237 | 2024-10-08 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.4 |
| b4eb478e-eb54-3ade-8a28-46d5e75801eb | -20.3732 | -43.9468 | 2024-10-08 02:06:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 107.8 |
| 3e4e3483-0a28-3b3f-80e3-b874e687da38 | -20.3938 | -43.9412 | 2024-10-08 02:06:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 199.2 |
| 1d8a17d8-27d1-3fa1-ac3b-c04f1057f368 | -20.3946 | -43.9163 | 2024-10-08 02:06:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 89.4 |
| 21dd73fb-8277-3505-b5bd-04729a604a7b | -20.4144 | -43.9356 | 2024-10-08 02:06:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.2 |
| b0d6a075-d5bd-332b-a4e9-74587a7bbc3f | -18.6139 | -57.2578 | 2024-10-08 02:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.2 |
| 8a017b7d-7b3c-3178-b956-61daed868374 | -16.03527 | -57.52088 | 2024-10-08 02:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a65190a4-ec33-3232-b021-59b4860bed4c | -9.95948 | -64.94507 | 2024-10-08 02:11:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3f89f4a4-8d9d-306c-83d2-512603f048a6 | -9.95224 | -66.77498 | 2024-10-08 02:11:00 | TERRA_M-M | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f440adc1-b31a-3970-9bf0-683b587b5050 | -9.95099 | -66.76606 | 2024-10-08 02:11:00 | TERRA_M-M | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ba729e2d-7242-3895-b99c-45ea8318a64c | -9.9434 | -66.77626 | 2024-10-08 02:11:00 | TERRA_M-M | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 05e048de-51fb-3180-8864-7fcdc15bb9ac | -9.75353 | -65.24063 | 2024-10-08 02:11:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8f69a3b9-5203-3555-80f2-8519da516dfc | -9.72196 | -66.57504 | 2024-10-08 02:11:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6c9f8fa1-3759-310b-ae1f-4875d84b710f | -9.71437 | -66.58525 | 2024-10-08 02:11:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f9ad0e29-179b-3001-aae5-a48a8511187b | -9.71312 | -66.57633 | 2024-10-08 02:11:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 86c89c67-9c89-39a3-9340-7ff7d86add8e | -9.5897 | -66.41782 | 2024-10-08 02:11:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| abc45f82-7e38-3f88-874d-1f835aa75528 | -9.55376 | -63.58424 | 2024-10-08 02:11:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 3b589226-a34c-3b1e-b11d-9c972ebe671e | -9.552 | -63.57259 | 2024-10-08 02:11:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 7b68133e-489c-3896-83e4-262b8d6be16b | -9.54376 | -63.5858 | 2024-10-08 02:11:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 18.1 |
| e6456365-c179-31cb-942c-93c126d15010 | -9.542 | -63.57419 | 2024-10-08 02:11:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 1c2cbde0-07e1-3272-ac6c-8243a04291c0 | -9.49285 | -67.1082 | 2024-10-08 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a0f4ed5-022f-3861-8de0-be1abe2a8d79 | -9.45971 | -66.74048 | 2024-10-08 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b671715f-22de-350e-9ca2-b829bd991e99 | -9.45846 | -66.73157 | 2024-10-08 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 85707774-832f-3b16-a22c-db0216d13e12 | -9.45087 | -66.74176 | 2024-10-08 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 56e5f2e8-af30-3e1f-a689-f797c5580949 | -9.44962 | -66.73285 | 2024-10-08 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.8 |
| e056377f-9a04-3535-91d7-ca3ca17da839 | -9.44838 | -66.72395 | 2024-10-08 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 75110cb6-cf30-3518-86b7-987fcb727429 | -9.44079 | -66.73414 | 2024-10-08 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9ee5573b-91bd-3f69-9ec3-5c2bf414ddd1 | -9.43954 | -66.72523 | 2024-10-08 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9004652e-c23f-3a1d-907b-ee4b8f2eac32 | -9.40463 | -66.55456 | 2024-10-08 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 27d517ab-8b62-33d5-8c1b-d3a5ff872247 | -9.40338 | -66.54562 | 2024-10-08 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 21b4abed-4d2c-3a88-bca6-9e64a330dd87 | -9.39453 | -66.54691 | 2024-10-08 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ec60da9f-6bf6-3a04-989b-0565549d6fa6 | -9.16164 | -66.06357 | 2024-10-08 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| c29a6b7a-210b-3ea1-a29a-1713a3160846 | -9.16034 | -66.05449 | 2024-10-08 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 448dd809-2f19-3ad8-a1bb-c447d8bf5b34 | -9.15118 | -66.06218 | 2024-10-08 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a30cfae3-6021-3b36-8f5b-89b21da50c45 | -9.04866 | -67.43633 | 2024-10-08 02:11:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c624ea79-84f6-3524-af39-de3cdfcbded6 | -9.01965 | -60.42982 | 2024-10-08 02:11:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4b30ea7d-ce6c-37cd-ab49-965b27247e45 | -8.71348 | -66.94904 | 2024-10-08 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae4a42f9-4fa2-3f87-b08d-c605f95afa11 | -8.70341 | -66.94144 | 2024-10-08 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 75f5028b-27e8-35fd-a4f1-948266752aa2 | -8.54669 | -67.13937 | 2024-10-08 02:11:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cff8bee0-7b98-3f31-9847-c1c4ea4fd143 | -8.54546 | -67.13049 | 2024-10-08 02:11:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 913a8491-dc40-3c83-b6d4-fbd34d3a045c | -8.54422 | -67.1216 | 2024-10-08 02:11:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 057aba4b-04b0-317a-a1ef-e0e9b4639f3a | -13.39029 | -61.93572 | 2024-10-08 02:11:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 2cf130ff-4998-393f-9076-62e73abd31da | -13.38823 | -61.92252 | 2024-10-08 02:11:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 33bc6879-abde-39f3-9736-b880d73aef2e | -12.95946 | -62.47007 | 2024-10-08 02:11:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1a0c095a-029d-34bb-be1f-ba94dede51bb | -12.87684 | -62.79259 | 2024-10-08 02:11:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| bbf5f9b1-e217-3132-8c41-3c874ce0bc4b | -12.8486 | -62.80926 | 2024-10-08 02:11:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8bf1765c-debe-3933-807e-3f2223b6ae63 | -12.82683 | -62.46623 | 2024-10-08 02:11:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 39.7 |
| bac8860f-70f3-3c10-b71f-b1ebc8fd57e0 | -12.82492 | -62.45385 | 2024-10-08 02:11:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 18.3 |
| ccc583d4-c924-3fb4-a71a-e2de850a04fb | -12.75412 | -62.2717 | 2024-10-08 02:11:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 07d49cb9-47fe-3027-98f7-0dc015c88076 | -12.74645 | -62.26558 | 2024-10-08 02:11:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 1b1f0a9f-301a-3619-8feb-1b0f3b609544 | -12.7082 | -62.96385 | 2024-10-08 02:11:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 93f24a0a-7a62-32ad-91e2-b0a64a4a0769 | -12.70643 | -62.95227 | 2024-10-08 02:11:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2ad5c890-aea6-3dd8-b459-c7fa79605ece | -12.69826 | -62.96546 | 2024-10-08 02:11:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 1ae5d8e8-545c-3167-a5c1-cce5dc7ebdff | -12.69649 | -62.95388 | 2024-10-08 02:11:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 67dc0bd0-35a7-38f2-a058-88d013b5f36c | -12.69471 | -62.94229 | 2024-10-08 02:11:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |
| a3afe7ff-cd1e-3c52-bc44-46b98afc98c0 | -12.64652 | -63.09744 | 2024-10-08 02:11:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ad7881ea-3c9b-34a5-bfec-0dde9b20dfc3 | -12.63666 | -63.09903 | 2024-10-08 02:11:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8d2c9893-562d-321b-ba43-b90845f1cbef | -12.4509 | -63.0237 | 2024-10-08 02:11:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d0251461-3d17-3e06-a1ce-580b315875e6 | -12.44915 | -63.01213 | 2024-10-08 02:11:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| f7a70831-9d20-3b46-8eef-5c30da44fe64 | -12.44739 | -63.00058 | 2024-10-08 02:11:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| c3a5ad40-7a19-318b-82a0-33eb35bd9248 | -12.18904 | -63.67035 | 2024-10-08 02:11:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 30.5 |
| d7789bfc-821c-304d-8c09-904ca147c206 | -12.18744 | -63.65962 | 2024-10-08 02:11:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0c0249fa-195b-34ad-8a6a-1c55ad953cfb | -11.89098 | -62.77439 | 2024-10-08 02:11:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 65bdd5f8-604c-3bf3-9f5d-78adc3953634 | -11.69741 | -64.97685 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 44ae8b78-301e-321b-996e-8c22089678b4 | -11.69604 | -64.9674 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0aa412c7-3123-38f2-b817-831aa0656374 | -11.68945 | -64.03378 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9f3b00ef-22d5-3801-81c1-551ab5135d86 | -11.68637 | -64.01286 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 71eb5e41-bb1c-3734-b862-30e17a2125b0 | -11.68617 | -65.02683 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fc15b89b-cacd-3dd0-bcf7-cee489e49c0e | -11.68002 | -64.03535 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| adf66cdd-7911-3db9-af44-267414469f97 | -11.67848 | -64.02499 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 68576999-5292-3d3c-8a01-131b91fbebaf | -11.67691 | -64.01431 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1aa36b90-429d-3886-9bd9-8103c43a9612 | -11.53326 | -65.05277 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8271a115-6b30-30c9-912c-6d7ef82ea5a1 | -11.5319 | -65.04333 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9b288ec1-d5b8-3ea8-bf2d-8feac7781256 | -11.52745 | -65.14015 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 16.0 |
| d4d61d42-3818-3566-86fa-d6742bc78767 | -11.51843 | -65.14153 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 24205e07-80f0-380e-8f71-5569a4519f10 | -11.51707 | -65.13216 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 72bf9bab-69c3-36fb-91ea-eb578523d457 | -11.51297 | -65.10399 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |


[Clique aqui para ver as próximas entradas](README26.md)
