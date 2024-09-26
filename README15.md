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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73f3f364-9bd9-3629-b52c-fbd2bffdfbe1 | -2.6602 | -57.5313 | 2024-09-26 00:45:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| dd19e53e-3754-3343-bb8e-58ba80eedf05 | -2.6785 | -57.531 | 2024-09-26 00:45:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| f8cc761e-09ec-3e27-9293-fd381cf71903 | -2.6968 | -57.5307 | 2024-09-26 00:45:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 7e69fef5-ef63-357b-bdb7-18195c04af1a | -3.3157 | -53.2325 | 2024-09-26 00:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 07544994-4a6a-3d64-ba84-7fe7fb033f24 | -3.3158 | -53.2122 | 2024-09-26 00:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 1c9ce4bf-5623-346d-85d9-d5c20c812395 | -3.3342 | -53.2117 | 2024-09-26 00:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| ff901a7e-919d-3797-9a06-39fbe2e3229c | -3.3505 | -53.7775 | 2024-09-26 00:45:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f998f99d-f6a6-3517-9d28-0626483301e8 | -3.5673 | -50.3794 | 2024-09-26 00:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| fff81a42-6c50-36b4-8456-439edf8d2385 | -3.9208 | -46.4459 | 2024-09-26 00:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 55768077-c0f3-31d3-a282-dd50a387a6a8 | -5.212 | -47.9577 | 2024-09-26 00:45:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| ecb8448c-1005-3edb-924c-0bc7c3dc9275 | -5.2306 | -47.9566 | 2024-09-26 00:45:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 8d385913-1bf1-3e36-b2a4-6c2a99ac9718 | -5.8808 | -48.0908 | 2024-09-26 00:45:40 | GOES-16 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| c62c5316-a865-3412-a1ce-6228f3cea051 | -5.943 | -52.1241 | 2024-09-26 00:45:40 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| a9f3873c-6f10-3225-af46-74872905dfd7 | -6.5772 | -60.0437 | 2024-09-26 00:45:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 157679a1-11a6-3ebe-bfdc-883475dc5913 | -6.6001 | -62.9649 | 2024-09-26 00:45:44 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 4cad7527-d91b-33ec-bba1-56a5a2b7fa0a | -6.7839 | -59.3245 | 2024-09-26 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 2180a785-daf7-39d5-9aa6-72c4898f2f22 | -6.784 | -59.3052 | 2024-09-26 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |
| d9ef74e5-6370-34f8-bd92-634baa9faee2 | -6.8023 | -59.3237 | 2024-09-26 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 26d7881c-1c1d-3e41-8314-ecddb0beff5d | -6.8024 | -59.3044 | 2024-09-26 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 151.4 |
| 4ecfe688-86e1-387a-8223-c58ba09f79d2 | -6.8384 | -63.1457 | 2024-09-26 00:45:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| b1f9634e-bb48-3315-b0da-865074d28d93 | -6.8385 | -63.1269 | 2024-09-26 00:45:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| af3c6c67-ade8-3b38-9777-5fe7e6a270d1 | -6.9305 | -63.1241 | 2024-09-26 00:45:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| ff34fe2c-9b70-3988-9863-0123f8eafe19 | -6.9306 | -63.1053 | 2024-09-26 00:45:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 5998f637-6c62-3c60-9b49-5fe60f9d6bb1 | -6.9681 | -62.9349 | 2024-09-26 00:45:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 2d995fb5-7ab3-325e-8256-72df421a70ae | -6.9682 | -62.916 | 2024-09-26 00:45:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 5fc3fb85-cbc2-385d-b54c-47a44118a06e | -7.0912 | -46.4412 | 2024-09-26 00:45:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b2b85bfb-f20e-304c-adb1-a2196df8edfa | -7.2905 | -61.106 | 2024-09-26 00:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 0ed986d2-a2a9-38b0-89f7-bbf7908c2435 | -7.2906 | -61.0869 | 2024-09-26 00:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| b70210a4-33b5-3383-af16-20e0f417e57d | -7.3637 | -55.5134 | 2024-09-26 00:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 5c4799d4-b300-3a7f-9298-ddc51d449cba | -7.3639 | -55.4935 | 2024-09-26 00:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a65568e3-ee0a-3b5b-af27-8837f9e6c56c | -7.3824 | -55.4924 | 2024-09-26 00:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 53ef719d-0f6b-3e39-918f-4fd152649d44 | -7.5705 | -55.1617 | 2024-09-26 00:45:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 03d5e89c-7af6-3074-9800-2620e90e1bdf | -7.7147 | -55.7131 | 2024-09-26 00:45:50 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 304b249e-7c3e-3ce7-8cba-10886f7ff71b | -7.7333 | -55.712 | 2024-09-26 00:45:50 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 52c3c93c-b7da-375f-9ff5-1616f5538bdc | -7.797 | -54.7263 | 2024-09-26 00:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| c98450fc-73e3-330a-be86-5851a3240ff1 | -7.8154 | -54.7453 | 2024-09-26 00:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 26f608c1-f61a-3e18-bfec-3f43ee3d7769 | -7.8156 | -54.7252 | 2024-09-26 00:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.0 |
| cf8fbf16-1422-3980-bb6b-153e411d57c5 | -8.1757 | -61.3946 | 2024-09-26 00:45:53 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 233d14ae-172c-37e7-8939-ea23f1a8188d | -8.3153 | -55.0157 | 2024-09-26 00:45:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 9f6aad03-0cbc-3953-8cd3-cf6cd652780f | -8.3155 | -54.9956 | 2024-09-26 00:45:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 517b5626-1000-36c3-9cd8-619f1bac28a9 | -8.5542 | -63.1814 | 2024-09-26 00:45:55 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 42.8 |
| e3810e76-fd72-364c-a59b-3acc93405ccf | -8.7087 | -54.7881 | 2024-09-26 00:45:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 408aa01a-0b61-32e7-abf4-7683980e00a9 | -8.8098 | -58.2172 | 2024-09-26 00:45:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 44a8b7c8-9767-3f85-9dea-334f5e32bc72 | -8.9301 | -57.1488 | 2024-09-26 00:45:57 | GOES-16 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 56e135f9-6a51-3e22-974e-9e76c3acf86c | -8.9244 | -67.1889 | 2024-09-26 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 46818ce4-acf7-3dd1-b602-5d8284f8f4d8 | -8.9429 | -67.1884 | 2024-09-26 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 6d0c6b67-8748-3cd2-90b0-2253920d0068 | -9.0468 | -61.4325 | 2024-09-26 00:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 56b8ab62-09d9-340f-99df-4985a9974f94 | -9.086 | -61.1245 | 2024-09-26 00:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 035079c1-b899-35a4-94ec-6b822ae8e21e | -9.1046 | -61.1237 | 2024-09-26 00:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| fe3c686e-a36e-3fbc-af99-58f213913f49 | -9.1349 | -65.564 | 2024-09-26 00:45:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a09fca69-b7e2-3faf-ab16-fd9a6d354e2d | -9.4353 | -51.4829 | 2024-09-26 00:46:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 0907da4e-1499-3404-ad9c-ca61bf97bafc | -9.5827 | -50.1584 | 2024-09-26 00:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| bf01e267-b1b7-35f7-af7d-c87ea536d774 | -9.5829 | -50.137 | 2024-09-26 00:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 716ed58d-abb6-39a3-ab36-1169cb702462 | -9.6015 | -50.1566 | 2024-09-26 00:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 7c1d163b-d366-37e4-a3c8-5b203302a576 | -9.6018 | -50.1352 | 2024-09-26 00:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| ffa3f561-f979-3b93-9df4-410c88ec2f5a | -9.806 | -53.5664 | 2024-09-26 00:46:02 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 4ec0a9a7-924b-3b44-8980-ae957904375f | -9.8083 | -68.8152 | 2024-09-26 00:46:03 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 94f2cb3c-92fc-3ea5-aa2a-95ba7c2019c9 | -10.0692 | -68.5871 | 2024-09-26 00:46:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 5e10c267-541a-37bb-91fe-dc62da80bb3c | -10.3713 | -58.9056 | 2024-09-26 00:46:05 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 5933f469-bff1-38e1-8c1a-867a336d3bf4 | -10.3882 | -67.8737 | 2024-09-26 00:46:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 64.4 |
| a589d321-eef9-3c76-b41f-50fbacf86414 | -10.9928 | -44.415 | 2024-09-26 00:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 6bf27aff-806b-3ad5-a896-ee1c414708bd | -10.9105 | -57.4308 | 2024-09-26 00:46:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 985391c7-4ef5-3e89-be06-2369ce3b6c0b | -10.9107 | -57.411 | 2024-09-26 00:46:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| b07b9585-0456-37d7-b5e5-0ee740924648 | -11.1845 | -54.7769 | 2024-09-26 00:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 3229e51b-06fa-3d07-b047-36ae1000e79e | -11.2034 | -54.7752 | 2024-09-26 00:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |
| cd5acb89-ce2c-3fd8-a8c6-f9fb91a3cc35 | -11.2036 | -54.7548 | 2024-09-26 00:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c59c152f-ac8d-3541-a8aa-48571dc97efe | -11.2413 | -65.2809 | 2024-09-26 00:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 00176c53-3594-3fac-a6f4-2a65845a6a3f | -11.2599 | -65.299 | 2024-09-26 00:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.0 |
| cf46364b-8e95-374a-96dc-e305bdfc25fd | -11.26 | -65.2801 | 2024-09-26 00:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 7ff92c51-5043-3b6c-be2b-5fb2552d0292 | -11.2788 | -65.2793 | 2024-09-26 00:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| b6255247-51ec-340f-9b50-bb01a8543cce | -11.8422 | -49.635 | 2024-09-26 00:46:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| edc3561c-1d54-3d86-a69d-9bc4ee4ad65e | -12.2175 | -45.5074 | 2024-09-26 00:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 9bc24644-09ec-34d7-8b97-26ff5a81e9ac | -12.2367 | -45.5045 | 2024-09-26 00:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 5264b6dc-8b27-38ff-b146-5fb56d4fd801 | -12.2371 | -45.4815 | 2024-09-26 00:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 110d9966-fa2e-3389-8de7-4bbd780f11d4 | -12.7696 | -51.3256 | 2024-09-26 00:46:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 50559ca8-71a7-37c8-92e7-8339bc4dbe77 | -12.7881 | -51.366 | 2024-09-26 00:46:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 5fc19906-3373-39a2-816e-307242fa1bfe | -12.7884 | -51.3446 | 2024-09-26 00:46:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 23d2bc70-41f4-32bd-82cc-0e1925e25680 | -12.7891 | -51.302 | 2024-09-26 00:46:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 944c5f10-3e92-3e74-b631-e8ad60b79fdc | -12.7898 | -51.2593 | 2024-09-26 00:46:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 62d3933e-c682-3c18-b0c7-8d500ac846e2 | -12.7901 | -51.238 | 2024-09-26 00:46:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| a6957a8c-fcea-353a-bd10-52b543b1a0d2 | -12.8072 | -51.3637 | 2024-09-26 00:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 116.6 |
| a6bec1ca-f0d3-3111-a0dc-86bb532b042e | -12.8076 | -51.3423 | 2024-09-26 00:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 9e652ec9-c345-3718-a05d-1131e8ac3364 | -12.8089 | -51.257 | 2024-09-26 00:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 135.5 |
| bf263247-c74d-3e51-97c9-acba2724b6d7 | -12.8092 | -51.2356 | 2024-09-26 00:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 0fc2b6b0-5bab-3a72-974f-29736bdec98c | -12.822 | -62.7078 | 2024-09-26 00:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| d1040f1d-5109-3317-8270-16834ade8ea9 | -12.841 | -62.7067 | 2024-09-26 00:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| efda2394-4a16-32e9-87e2-70fb059dc610 | -12.8411 | -62.6874 | 2024-09-26 00:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 75f8270a-fc13-3858-94db-b314bc444547 | -13.1958 | -45.6539 | 2024-09-26 00:46:20 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 6b771b8e-182f-3cc2-92bf-176b51fba041 | -13.1963 | -45.6308 | 2024-09-26 00:46:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 17bee603-938f-3fa8-8b47-66a9a2d8b296 | -13.4993 | -61.2698 | 2024-09-26 00:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 00608506-aa43-357d-90dd-20f2d9b122df | -14.4439 | -45.2555 | 2024-09-26 00:46:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| bdd4e038-621d-32ef-a1b6-c35073a83e09 | -14.4444 | -45.2321 | 2024-09-26 00:46:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 286.1 |
| 3d19524e-0f31-3e66-a76f-cda8c71456c9 | -14.4449 | -45.2088 | 2024-09-26 00:46:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 36adc84b-7db7-37e4-9753-ce91affce3fe | -14.4634 | -45.252 | 2024-09-26 00:46:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 164.5 |
| ab1c8860-0cdc-3618-81d3-312efbc821e5 | -14.4639 | -45.2286 | 2024-09-26 00:46:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 610.7 |
| bb72a3bf-7cd8-314e-ae72-5cd1aed01235 | -14.4644 | -45.2052 | 2024-09-26 00:46:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 568f18da-0249-3520-95a4-60375247ed0e | -14.6728 | -45.4701 | 2024-09-26 00:46:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 2e023359-4aca-335e-a497-8c4202dac28c | -14.5705 | -45.6973 | 2024-09-26 00:46:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| bee3db02-25b3-3172-9efc-e44d11ba301a | -14.896 | -57.9873 | 2024-09-26 00:46:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 151.5 |
| e5d2678a-d853-3f03-b2f6-6563964a2a2a | -14.8963 | -57.9671 | 2024-09-26 00:46:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |


[Clique aqui para ver as próximas entradas](README16.md)
