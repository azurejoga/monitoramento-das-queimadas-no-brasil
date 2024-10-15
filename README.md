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
| 2aef2f9e-ef51-32a5-a2f0-cedd04e92911 | -14.11 | -46.17 | 2024-10-15 00:04:02 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 525bf085-f4a7-3070-8cec-561aaa5aba71 | -14.08 | -46.21 | 2024-10-15 00:04:02 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 016c3678-ef49-3519-9d8d-aff18d2529b2 | -14.08 | -46.16 | 2024-10-15 00:04:02 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b6d9592-ce76-30d5-94c1-52b9ae96886a | -14.11 | -46.22 | 2024-10-15 00:04:02 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eec46952-c96a-31f5-89fe-11736d160d03 | -14.05 | -46.15 | 2024-10-15 00:04:05 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 26f4b382-aada-396b-8a45-d9ff682a8f8a | -1.5493 | -54.3357 | 2024-10-15 00:05:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 78fe00d8-a886-3118-bab6-4c087bc43f5f | -1.8762 | -47.8272 | 2024-10-15 00:05:16 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 827d84f2-954f-3358-b114-ff39e7d22498 | -2.4418 | -50.2447 | 2024-10-15 00:05:20 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 9132cba6-ab41-3859-bf2a-9e311796fc85 | -2.4419 | -50.2237 | 2024-10-15 00:05:20 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| f8a79c05-4cec-3a09-9baa-ba126becf539 | -2.501 | -49.0802 | 2024-10-15 00:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 0114e4cb-f34b-38eb-80f7-4fbadd727d6d | -2.5028 | -48.5455 | 2024-10-15 00:05:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| c0a3ffca-aa69-3e68-985c-cbc2b0488d6a | -2.6496 | -54.6172 | 2024-10-15 00:05:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 249fe374-6f88-391d-8452-eb79a4927c54 | -3.0581 | -53.2598 | 2024-10-15 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 8fc8676c-aecb-314e-9df0-289b3d89b910 | -3.1099 | -54.2263 | 2024-10-15 00:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 02bc395f-77b3-3335-b179-bc64bc3002fc | -3.1282 | -54.2459 | 2024-10-15 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 9e9fc6b3-ec8b-3444-96b2-c2751caaff7f | -3.1283 | -54.2259 | 2024-10-15 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 734940e4-b38d-34bb-94d7-228c57362bd9 | -3.4883 | -51.5483 | 2024-10-15 00:05:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 387aa79d-6f23-3566-9254-183975b4f304 | -3.7217 | -49.0193 | 2024-10-15 00:05:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| cab847ae-bf93-3d75-8ea8-1b306a551aaa | -3.7218 | -48.9979 | 2024-10-15 00:05:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 210.1 |
| 80c1eed7-0a94-3455-adef-b33ffae4a426 | -3.7219 | -48.9766 | 2024-10-15 00:05:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| adddd60f-0c35-3746-8c1f-7fe5b0c74c9f | -3.7403 | -48.9972 | 2024-10-15 00:05:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 178.7 |
| 5760f230-bde8-38fb-a2c8-f417058e8ddb | -4.3774 | -47.7627 | 2024-10-15 00:05:31 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 86e62089-4b46-37fc-9a19-f5542f611297 | -4.3959 | -47.7618 | 2024-10-15 00:05:31 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 3d3ea623-18ef-3184-b1c8-c1c3b96df3c3 | -5.1983 | -44.8497 | 2024-10-15 00:05:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| b236595c-3a9a-339e-b093-cde6234b89de | -5.217 | -44.8485 | 2024-10-15 00:05:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 556d90d5-09f9-36ad-a765-929f19057cfc | -5.2306 | -47.9566 | 2024-10-15 00:05:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 6efa8986-25db-3dd1-b21a-a019f61b2227 | -5.2982 | -46.3936 | 2024-10-15 00:05:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 6fc7d506-d05f-366b-a77c-3faa64330065 | -5.5356 | -44.7359 | 2024-10-15 00:05:37 | GOES-16 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 51ebac35-4d25-3045-861c-39960d60f5f7 | -5.5358 | -44.7131 | 2024-10-15 00:05:37 | GOES-16 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 46be7106-687b-3813-8ab8-6e8f6b5fc5c9 | -6.4268 | -49.6028 | 2024-10-15 00:05:42 | GOES-16 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 6bb97564-13ed-3a10-a94e-ccd3855736f6 | -6.5505 | -48.2408 | 2024-10-15 00:05:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 109.7 |
| dd24011f-e10f-3b92-a533-d9be8147f1f8 | -6.5691 | -48.2395 | 2024-10-15 00:05:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 83.1 |
| fb61cb8b-93ea-3d0a-97c6-d6df71061b23 | -6.6325 | -60.0416 | 2024-10-15 00:05:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| a45aee7f-cc24-394b-9b79-32da8bffe7f7 | -6.6326 | -60.0224 | 2024-10-15 00:05:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 31fcf87a-51d5-3a66-9d6c-62c0914d29d0 | -6.6511 | -60.0026 | 2024-10-15 00:05:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 23d040ee-94f8-3092-8c13-abdf08c7c087 | -6.7285 | -59.3267 | 2024-10-15 00:05:44 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| dd9c0339-32f4-3139-b24d-cbcd712f55ce | -6.747 | -59.3259 | 2024-10-15 00:05:44 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 7b83ccb8-79c7-3619-a824-aebeecbf111c | -7.528 | -49.4817 | 2024-10-15 00:05:48 | GOES-16 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 8f66e6b6-bcc5-3fd7-8448-42ad9be25458 | -8.4639 | -47.822 | 2024-10-15 00:05:54 | GOES-16 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| f3506357-e877-3a4b-a359-17c0486d907f | -8.4642 | -47.8 | 2024-10-15 00:05:54 | GOES-16 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| f1cf5a67-fba4-38db-9ab6-5c5bd64b7e87 | -8.9141 | -47.9103 | 2024-10-15 00:05:56 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 7f18f8a9-4b3f-3694-9fdf-b6883b571d01 | -9.0852 | -47.7836 | 2024-10-15 00:05:57 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 592d6963-bd7f-3325-9f36-1ebc86be4e40 | -9.2549 | -60.8863 | 2024-10-15 00:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| dc090978-51aa-3efa-9c63-a17100e62217 | -9.3493 | -63.5846 | 2024-10-15 00:05:59 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 54d1b849-17ff-3f73-a02b-418f71fd74c3 | -9.3494 | -63.5658 | 2024-10-15 00:05:59 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 40978fa8-260f-3eb4-9901-3d2111bf053a | -10.0495 | -47.6589 | 2024-10-15 00:06:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 4bb399ea-bfc2-334f-be82-f1218ed0ef12 | -10.0415 | -54.3442 | 2024-10-15 00:06:03 | GOES-16 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| c387b61e-6f49-3807-aa53-def7b30c7cd9 | -10.3954 | -44.8206 | 2024-10-15 00:06:04 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 636b9810-55ca-3d42-a3e2-6388a3ea6f5a | -10.4918 | -42.433 | 2024-10-15 00:06:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 74.4 |
| c65cb858-1f62-34e9-8779-53ce3bdcac7b | -10.3524 | -61.1946 | 2024-10-15 00:06:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 78119f7c-3516-3d92-9efa-eb5e01e74ab0 | -10.3711 | -61.1935 | 2024-10-15 00:06:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 241.2 |
| a9b1f2d5-9a0d-39ad-b1d2-534f08bbef0b | -10.3713 | -61.1743 | 2024-10-15 00:06:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 84cd718e-5d23-3793-930a-fcd30b52c729 | -10.3898 | -61.1925 | 2024-10-15 00:06:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| b5f4f5a1-c44d-3a53-a5f0-a08d5129f49b | -10.822 | -49.256 | 2024-10-15 00:06:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| ef8674d3-0005-3cb0-ab3f-aa40d96db40c | -10.841 | -49.2539 | 2024-10-15 00:06:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| cae11323-f8ee-3077-a56d-beab8a05d60e | -10.8413 | -49.2322 | 2024-10-15 00:06:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| c1229d28-e35e-377a-93b6-90ae8f0f23f4 | -11.884 | -43.8142 | 2024-10-15 00:06:12 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| a3b49d20-48be-381c-b0d7-33c9ac46624c | -11.6915 | -65.2432 | 2024-10-15 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| a9884634-797d-3360-864d-b992982f90c3 | -11.6917 | -65.2243 | 2024-10-15 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 2de5582a-ccef-35ea-bee0-1c8198e6e16a | -12.0796 | -50.2966 | 2024-10-15 00:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 193b5740-f2d2-3ee1-a44d-9e9dd9290e3a | -12.0799 | -50.275 | 2024-10-15 00:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 3085423c-683a-3a62-bd6c-b2abfe6202eb | -12.0915 | -50.7665 | 2024-10-15 00:06:14 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| cd9f3f5b-e4b3-35ce-ad15-9dfe7dfa1bed | -12.0987 | -50.2943 | 2024-10-15 00:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 36eba443-d41b-3f6e-a73e-87a63fd5c4ac | -12.099 | -50.2728 | 2024-10-15 00:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 152.6 |
| aa69f157-07bf-30cc-b83e-9022112e7020 | -12.3793 | -63.7294 | 2024-10-15 00:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 979626b1-97d8-3803-b5b7-5f86bee76474 | -12.3795 | -63.7103 | 2024-10-15 00:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| d785a75c-d472-3fbb-bfa1-dfc0255d806d | -12.3982 | -63.7284 | 2024-10-15 00:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 97ee6456-b108-32d9-8b2f-8bee0469bf51 | -12.3983 | -63.7093 | 2024-10-15 00:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 87bc0f4f-f78f-35db-9616-89d4401cfc6c | -12.4603 | -63.0169 | 2024-10-15 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 922d560b-aad9-37e7-ad37-fea09aacf83c | -12.4961 | -63.2641 | 2024-10-15 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| e946d57d-1a1e-3e9e-b034-8db6988e2ffe | -12.5149 | -63.2822 | 2024-10-15 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 81.6 |
| fb6b34ed-9c1d-32c5-871c-0b465ca70e97 | -12.515 | -63.263 | 2024-10-15 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 124.1 |
| ebfa47f4-8825-3b85-87ba-93b2f3395bd0 | -12.9538 | -62.7962 | 2024-10-15 00:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 716d0bd2-125e-3cf1-bdd6-bc20a25d3cdb | -12.9728 | -62.7951 | 2024-10-15 00:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| be985b80-336b-344f-9d6c-7a1ee4916884 | -13.1285 | -62.3227 | 2024-10-15 00:06:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 78d4bee6-1db4-3ec2-8a82-9ce6968444a7 | -13.1287 | -62.3034 | 2024-10-15 00:06:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 545c293d-4d38-34ca-a70c-236e157a7a90 | -13.1473 | -62.3408 | 2024-10-15 00:06:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 1d5b2407-9a72-3ed9-a8bb-b956c0148972 | -13.1475 | -62.3215 | 2024-10-15 00:06:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 202.3 |
| fd192d1f-6a1e-3ea1-ac8a-6bda67a3fb8d | -13.3594 | -61.9789 | 2024-10-15 00:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 24c84f88-fbfc-33b0-bf4a-bc88cc2c2b97 | -13.3596 | -61.9595 | 2024-10-15 00:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 6e25c982-daf7-30a8-b05a-2421248ec445 | -13.3653 | -61.357 | 2024-10-15 00:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 3d4d7de3-8aff-3c97-a91a-b83e68a14374 | -13.3655 | -61.3376 | 2024-10-15 00:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| d1061ee4-1164-337b-996e-14f7bad82b22 | -13.3786 | -61.9582 | 2024-10-15 00:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 136.8 |
| e47c5fb4-423a-3e19-b9d6-21dc83ae3f56 | -18.8337 | -42.4119 | 2024-10-15 00:13:32 | METOP-C | SANTA EFIGÊNIA DE MINAS | MINAS GERAIS | Brasil | 3157500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aa32df6a-5d30-3dc9-835e-81c962742f2b | -18.835699 | -42.422199 | 2024-10-15 00:13:32 | METOP-C | SANTA EFIGÊNIA DE MINAS | MINAS GERAIS | Brasil | 3157500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 27bad4aa-f63e-3026-b46b-cf45ad756fbc | -19.6399 | -40.480999 | 2024-10-15 00:13:41 | METOP-C | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2b2495f8-4b24-3ed8-8915-a6d15a17ef82 | -19.6479 | -40.470299 | 2024-10-15 00:13:41 | METOP-C | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 37b82942-cc2a-3644-80ee-a6d0d903a850 | -19.6497 | -40.478802 | 2024-10-15 00:13:41 | METOP-C | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 14ff0842-d9eb-3df3-850f-37ddd4a5198e | -18.3503 | -42.697701 | 2024-10-15 00:13:41 | METOP-C | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d579e5e9-38fd-30eb-8652-d496530716e1 | -18.3405 | -42.699799 | 2024-10-15 00:13:41 | METOP-C | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f21b1527-1637-3158-8451-78360a0cc7e4 | -18.235701 | -42.581402 | 2024-10-15 00:13:42 | METOP-C | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 841a5e26-c868-3efb-9d32-9f10157ef4dc | -19.857901 | -44.942699 | 2024-10-15 00:13:52 | METOP-C | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 449c1942-cdaa-37b5-86db-6d0207c2f8f3 | -19.860701 | -44.958 | 2024-10-15 00:13:52 | METOP-C | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 89132587-333a-3cc2-b849-e2f11f8691d5 | -18.771 | -41.788799 | 2024-10-15 00:14:00 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 42e5eab9-98e0-3925-b547-3cef6a0e5402 | -18.7729 | -41.798302 | 2024-10-15 00:14:00 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 475dc6ff-2e0d-303c-9890-8c5eb9b2aacf | -16.768801 | -42.838799 | 2024-10-15 00:14:07 | METOP-C | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a860ef4d-5c60-3e3c-9d9e-7383adc02320 | -13.2689 | -41.941101 | 2024-10-15 00:15:01 | METOP-C | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7823c1de-d862-3a61-b87e-2dcabf546471 | -13.2707 | -41.9492 | 2024-10-15 00:15:01 | METOP-C | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c44c48eb-20b4-3fba-98ce-2b1c00febee4 | -13.2724 | -41.957401 | 2024-10-15 00:15:01 | METOP-C | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 63a975e3-2ec6-3476-8644-68861d77679d | -13.2591 | -41.943298 | 2024-10-15 00:15:01 | METOP-C | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
