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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65e2d228-acbc-3f11-911e-70e13abd8326 | -16.3548 | -49.9477 | 2024-09-27 03:16:38 | GOES-16 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 981ea51d-10e9-3f96-af03-240fadf4af64 | -16.8933 | -58.0213 | 2024-09-27 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.7 |
| 59dc45fb-6a68-341e-8c31-0c3674e909d1 | -16.893 | -58.0417 | 2024-09-27 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| 8c71f61f-f359-3d1e-a124-3eff9ef030e9 | -17.1184 | -56.1894 | 2024-09-27 03:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 73.1 |
| f661b2e8-6ecd-37b3-b540-70f5e4797c85 | -19.2991 | -49.6765 | 2024-09-27 03:16:53 | GOES-16 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 63.3 |
| f1cb0606-90c1-3380-aa03-81ebfd4faf16 | -19.3977 | -42.5753 | 2024-09-27 03:16:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.6 |
| 10f6ffc2-6234-3a4f-9faa-354f94e4d693 | -19.3773 | -42.5809 | 2024-09-27 03:16:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.3 |
| 51aa031f-52a7-33ab-b656-c6a56b8da384 | -19.6342 | -42.8103 | 2024-09-27 03:16:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.2 |
| 904732ba-b3fb-3a47-8dd4-a09c08d1137e | -19.6136 | -42.8159 | 2024-09-27 03:16:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 140.6 |
| 20145b09-40ee-3678-a9d1-c8d633f21d30 | -19.6129 | -42.8411 | 2024-09-27 03:16:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.7 |
| 2d8ddf70-aa3a-3209-b2a5-897f0942fc51 | -22.7442 | -44.7785 | 2024-09-27 03:17:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.6 |
| 835b36cc-d5f9-3703-be65-22d3dca184bb | -22.7433 | -44.8035 | 2024-09-27 03:17:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.4 |
| 9b31af88-ad1b-3184-93bf-8b5a1b98217e | -2.3579 | -47.6206 | 2024-09-27 03:25:20 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| d5b68e52-6c48-3212-9645-ec08dda511ea | -2.358 | -47.5989 | 2024-09-27 03:25:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 6952db90-4d8d-37f4-8ab8-c11188be98c3 | -2.6783 | -57.5893 | 2024-09-27 03:25:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 4822715a-1a02-3e10-8ea2-827734b7eca2 | -2.8611 | -51.6699 | 2024-09-27 03:25:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| fc56b09a-a8a5-354d-ac55-003ca1c426d6 | -2.8795 | -51.6695 | 2024-09-27 03:25:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 28123e11-dff0-3001-9438-8d9e24024fb6 | -3.0107 | -51.0652 | 2024-09-27 03:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| af5cca0a-abba-3cad-bf3b-333a776d2bdd | -3.0108 | -51.0444 | 2024-09-27 03:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| dbc3ae36-b085-3f83-810a-aa904e6356f4 | -3.2136 | -46.7843 | 2024-09-27 03:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 6aa927e2-b88e-3f0f-b6c9-74dec445ea9d | -3.2321 | -46.7836 | 2024-09-27 03:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| f6daef15-8156-3098-96ad-f2e0718a0892 | -8.6101 | -63.1226 | 2024-09-27 03:25:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 2cb8c42b-b40d-34df-9e27-cdff79d3ad89 | -8.6286 | -63.1219 | 2024-09-27 03:25:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 69.6 |
| f4148128-2726-3797-b360-050756301af4 | -8.6658 | -63.1016 | 2024-09-27 03:25:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 39a307f9-3ded-3060-89c2-e29780b3b742 | -9.0656 | -61.3934 | 2024-09-27 03:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c6bdcb56-72e5-319c-b650-5af900e9f89c | -9.1029 | -61.3726 | 2024-09-27 03:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| aff18859-179a-366f-9f48-142482541afa | -9.103 | -61.3534 | 2024-09-27 03:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 5f4c5098-ac42-34b6-a2dd-15881b2ceac3 | -9.1215 | -61.3717 | 2024-09-27 03:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 031d2e13-95eb-3961-86b6-4fb4a07aa31b | -9.1216 | -61.3526 | 2024-09-27 03:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| ef275e5b-0f9b-3ee4-99c3-a2aef6b85da3 | -9.3028 | -65.3528 | 2024-09-27 03:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 41277a40-9189-324b-b2e3-4e73d0964084 | -9.3029 | -65.3341 | 2024-09-27 03:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 05133660-5647-39a1-8469-aa0bdd501926 | -9.3214 | -65.3522 | 2024-09-27 03:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 31de152e-4323-3816-87a0-6cfcb43d968d | -9.3215 | -65.3335 | 2024-09-27 03:26:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 02861313-2f97-3acf-bab7-20c09f77d8ab | -9.3672 | -63.6972 | 2024-09-27 03:26:00 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| c190f006-ea5a-3827-bc01-fe6cdaa9d1d4 | -9.5829 | -50.137 | 2024-09-27 03:26:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 30067c81-3171-3c93-abf5-c4949fa01e86 | -9.6018 | -50.1352 | 2024-09-27 03:26:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 7d9955a3-bda8-3cf8-8f1f-f694d69e397b | -9.602 | -50.1139 | 2024-09-27 03:26:01 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 3a323d32-3f22-3e1f-a271-68934edc252a | -10.1309 | -50.019 | 2024-09-27 03:26:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 7ddad5a0-b1b3-3e73-ba31-c6876579fc4c | -10.1312 | -49.9976 | 2024-09-27 03:26:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 8b5802bd-95fe-3e76-93a9-c435fe78d2aa | -10.3672 | -53.7858 | 2024-09-27 03:26:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| d0da2d99-1309-39e6-bb7b-e881f2acca50 | -10.4181 | -45.8016 | 2024-09-27 03:26:05 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 91d6f699-f275-37e0-a4c9-3839e045ac06 | -10.6639 | -45.8838 | 2024-09-27 03:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| bf21fe36-6cd9-3207-8f51-b966e703f970 | -10.7214 | -51.0657 | 2024-09-27 03:26:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| f02a69a9-c6b4-3b2d-9ef5-6d25d6af6e0c | -10.9264 | -54.2692 | 2024-09-27 03:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 00660f87-5dfb-303d-b1a5-7a366de3551b | -10.9267 | -54.2488 | 2024-09-27 03:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 6860e0af-d27a-3960-b681-dac4b0ec2298 | -10.9453 | -54.2676 | 2024-09-27 03:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| dd1aed38-c8a6-3ede-8df8-54d0b5d9a14e | -11.2534 | -47.1142 | 2024-09-27 03:26:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| bd7c33e9-42a8-3617-a6b4-ab56554a52a6 | -11.2034 | -54.7752 | 2024-09-27 03:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| e3dbc6fe-ea42-3fe4-9efc-9061aedaacf8 | -11.2223 | -54.7735 | 2024-09-27 03:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| a92f3b64-51fa-3925-af99-6728b4d3a9ce | -12.1859 | -50.8195 | 2024-09-27 03:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| eebc9925-e937-3d1a-86a6-c21ef904910a | -12.1863 | -50.7981 | 2024-09-27 03:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| efee0a09-8960-3dff-9ff5-0ed917358ede | -12.6633 | -54.6988 | 2024-09-27 03:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 679f686a-350b-3712-860a-6a59661e501f | -12.7014 | -54.6949 | 2024-09-27 03:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 9986bd72-6af1-39ed-8862-f6444d43891c | -12.6826 | -54.6763 | 2024-09-27 03:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 22b19015-c0b6-35e4-9871-5b03c44ee33d | -12.6636 | -54.6782 | 2024-09-27 03:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9c200f0d-b2fd-3b6d-b455-b4c95f370dcc | -12.6824 | -54.6968 | 2024-09-27 03:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 381a81ab-21f1-3c0e-ba73-3ec7de7ca414 | -14.9414 | -51.448 | 2024-09-27 03:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 1ea2dfc9-e948-3e58-bd9a-ecdbbce633be | -14.941 | -51.4695 | 2024-09-27 03:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 47a90f67-2a81-39bb-85b7-65f9494c2495 | -14.922 | -51.4507 | 2024-09-27 03:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| f9050dc8-c2bd-3731-bde3-e6e9e847cd85 | -16.1189 | -51.9436 | 2024-09-27 03:26:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 21ff4edd-3b06-3140-9ded-965e4a31c8c3 | -16.3548 | -49.9477 | 2024-09-27 03:26:38 | GOES-16 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 812d287a-3442-38cf-b72e-32347696d74c | -16.3552 | -49.9256 | 2024-09-27 03:26:38 | GOES-16 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 5e371e5c-f8f0-3422-95d5-b1651249208b | -16.7329 | -55.8237 | 2024-09-27 03:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| f659bd20-0a4c-3cb4-9fe8-75f333fec76b | -16.7325 | -55.8445 | 2024-09-27 03:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| d6b48198-ac65-3e0c-8ed5-07056a80acd1 | -16.8737 | -58.0235 | 2024-09-27 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 5e550df5-3644-39f2-82c8-77907d271815 | -16.8933 | -58.0213 | 2024-09-27 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 74246333-a5f5-3f49-af70-e2b479ebfe6f | -19.3773 | -42.5809 | 2024-09-27 03:26:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.1 |
| 1c43a7f5-d417-391b-8c38-94fffb711582 | -19.3977 | -42.5753 | 2024-09-27 03:26:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 129.7 |
| 692909f4-26d1-3752-9d45-5246b456627d | -19.3985 | -42.55 | 2024-09-27 03:26:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.3 |
| 4773ce38-e379-3d67-90b5-879935f1d4aa | -19.6136 | -42.8159 | 2024-09-27 03:26:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 123.0 |
| 12ed5c47-deed-3661-bf51-b606447627c8 | -19.6342 | -42.8103 | 2024-09-27 03:26:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.1 |
| c6e4a352-ec1c-3273-813a-f32fe045672b | -22.2257 | -48.6155 | 2024-09-27 03:27:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.9 |
| a6117852-78eb-3919-9f0d-16452318e06a | -22.7442 | -44.7785 | 2024-09-27 03:27:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.9 |
| 09f93b61-f274-375c-a536-929b26ca1207 | -22.7433 | -44.8035 | 2024-09-27 03:27:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 107.6 |
| df1571c0-4e12-3cea-afc4-59a9b9e5ecd0 | -2.3579 | -47.6206 | 2024-09-27 03:35:20 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 0d08f294-0fdb-37ba-b899-381ec7309736 | -2.358 | -47.5989 | 2024-09-27 03:35:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 170edd36-3561-3f37-b3b0-cc4611c9b84b | -2.8611 | -51.6699 | 2024-09-27 03:35:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| fcd4ccf1-19b5-3e00-b215-de1d3bcf8794 | -2.8795 | -51.6695 | 2024-09-27 03:35:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 989751a9-e7c4-3f3f-99a0-a932123c768e | -3.0107 | -51.0652 | 2024-09-27 03:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 07f6cc31-da65-329a-a0c7-8d79a33ec6e8 | -3.2136 | -46.7843 | 2024-09-27 03:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| fe797acd-e958-33ec-aa0d-10a20532d466 | -3.2321 | -46.7836 | 2024-09-27 03:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c3e9adef-e18c-3ad6-9197-47f952ed7b8e | -7.5289 | -61.3825 | 2024-09-27 03:35:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 4fd9507b-977e-379c-9095-95eef3484b11 | -7.77 | -61.2015 | 2024-09-27 03:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 38e4285b-e0d1-366b-a07d-97dd61eefb75 | -7.7701 | -61.1825 | 2024-09-27 03:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4d7a8653-fa40-3f6f-9cf9-f64e4e3c34f9 | -7.9174 | -61.2909 | 2024-09-27 03:35:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 0f403aa9-9222-30a6-96e4-eb7f09bbf38f | -7.9175 | -61.2718 | 2024-09-27 03:35:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 846cd5ff-6c30-3090-9a1e-65106acfbb61 | -8.1394 | -61.2817 | 2024-09-27 03:35:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0c3cbfae-d667-3e70-837e-a12d01ef46fb | -8.6286 | -63.1219 | 2024-09-27 03:35:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| d01983b5-0d61-3d28-b6bf-c13c58e9254c | -8.6101 | -63.1226 | 2024-09-27 03:35:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| a367cef6-3600-3ac3-8d4d-6b779841cec0 | -8.8775 | -61.7837 | 2024-09-27 03:35:57 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| cbb6eae1-7f8e-371f-a368-514b6938f9b8 | -8.8774 | -61.8028 | 2024-09-27 03:35:57 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 87e714c6-1bd8-309d-b35e-5f0ae9f161c1 | -9.0656 | -61.3934 | 2024-09-27 03:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 75dcd468-04ae-383e-ac39-8422bd3ad991 | -9.1029 | -61.3726 | 2024-09-27 03:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 02ab589e-9647-3ee7-8be9-5dd9fa4a169d | -9.103 | -61.3534 | 2024-09-27 03:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 60c7d41f-acdb-3c45-8112-c9e2ff79a34d | -9.1032 | -61.3343 | 2024-09-27 03:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 605283ba-0cd8-331f-beb6-1a5ba2362ab9 | -9.1215 | -61.3717 | 2024-09-27 03:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 56779303-ae9b-31ab-8871-9abe028b75cb | -9.1216 | -61.3526 | 2024-09-27 03:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 3f784df3-b012-3d98-8af9-0d80ccbfac0a | -9.1217 | -61.3334 | 2024-09-27 03:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| ae3a5084-2d16-363d-8ce8-1d148b5ee343 | -9.3858 | -63.6965 | 2024-09-27 03:36:00 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e653355e-452b-3c0f-a3c5-0e7da5ca2d88 | -9.3028 | -65.3528 | 2024-09-27 03:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |


[Clique aqui para ver as próximas entradas](README48.md)
