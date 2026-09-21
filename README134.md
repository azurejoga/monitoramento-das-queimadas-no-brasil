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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d74c9278-9b56-3c8a-8e3e-b971654c43f7 | -10.4099 | -50.3324 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| f245b927-6838-3d99-851f-94e24bd6338c | -6.5257 | -44.9342 | 2026-09-21 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 96ae4083-dde8-305d-868c-418bcdadf6b0 | -11.801 | -49.8345 | 2026-09-21 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| fb325c30-7989-3878-bf50-1f8ecb668433 | -5.9334 | -59.9707 | 2026-09-21 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 5190effe-b0a1-3d70-b106-c7bed20da6c4 | -10.2152 | -53.9216 | 2026-09-21 14:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 14604dcd-06aa-3dc2-bafd-3c0c5301bb40 | -4.0142 | -53.4946 | 2026-09-21 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| cf518355-c909-3fd9-a702-16a5d02e1692 | -10.336 | -50.2119 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 943e8e06-7144-3dcb-889f-76b1c17b0446 | -9.8307 | -48.451 | 2026-09-21 14:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 447380d7-06f7-3aec-844b-07e8f043524b | -3.1698 | -58.5859 | 2026-09-21 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 5a644ce2-c3d6-314a-add0-ce950492f76d | -5.6221 | -43.3934 | 2026-09-21 14:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 276.3 |
| f161dda1-6e85-3e17-8476-837f0e592479 | -4.2238 | -48.6342 | 2026-09-21 14:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 5a13c456-d4c4-332e-aee7-cfc58cf11526 | -13.2404 | -51.7997 | 2026-09-21 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 4a0017c5-ea44-3ded-ad7c-25599ab3f30c | -10.4728 | -51.302 | 2026-09-21 14:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 7b6be595-b0dd-3a67-a7c5-437e6095aa3a | -9.1523 | -49.9853 | 2026-09-21 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 3f1fce62-6dfd-371c-8e87-6f56d677ac8d | -9.5593 | -66.0545 | 2026-09-21 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 0f800b25-07a0-34d4-9701-d7052f8d237f | -1.4302 | -48.9955 | 2026-09-21 14:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 417838c9-aff2-3375-85d6-5543e18d7ec1 | -3.4369 | -50.6142 | 2026-09-21 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 55b96b90-37ed-327c-bb05-567aca27338f | -6.3195 | -60.0147 | 2026-09-21 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| a23ec56f-5119-3e3f-bf99-ae515f32b5fd | -6.8264 | -55.5222 | 2026-09-21 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| bfec6d26-04e6-30cc-ae58-d8c5ceae7405 | -10.3546 | -50.2313 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 8e6b29f1-003a-3868-a0e4-3e051ab1665b | -8.7914 | -48.7285 | 2026-09-21 14:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 15933f48-cd13-39bc-8c99-4a4b53e344bd | -7.4286 | -44.7409 | 2026-09-21 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 67313b96-f00b-3323-9d00-cf9a4161a566 | -5.7692 | -43.7077 | 2026-09-21 14:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 139.1 |
| e16fdb7a-d626-3caf-9da8-becdb4054b18 | -10.3916 | -50.2916 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| f836b950-816b-3935-a56e-f42ce73b433b | -10.9355 | -50.6186 | 2026-09-21 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 4b8f0786-168b-30be-a8dc-2d5feeff58e9 | -6.338 | -60.0141 | 2026-09-21 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| a263170f-e471-3f88-b5a0-c3d85b6c5b8a | -10.4672 | -50.2838 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 37e13fa1-73f7-3f13-9b0c-50270b9a3fe8 | -10.2979 | -50.2372 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 59024947-45e0-36a3-b7ff-85da7cad83e4 | -8.7703 | -45.8793 | 2026-09-21 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 843e54a6-7a00-397f-aefe-1e56bfcd1c3b | -10.955 | -50.5738 | 2026-09-21 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 442aff83-280d-3c00-a938-06df632ea317 | -6.5634 | -44.9084 | 2026-09-21 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| a3a05333-0868-3395-9c07-3d29078aa54a | -11.8014 | -49.8129 | 2026-09-21 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 83be5255-54f1-34d8-a99d-e9b994e5432b | -10.4917 | -51.3001 | 2026-09-21 14:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 002d9b04-2b30-363c-a8a9-2f6569057ecb | -2.9157 | -57.7983 | 2026-09-21 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| cb2d42aa-2b5e-3b24-b7b6-a6bcdcb9a133 | -6.4979 | -45.863 | 2026-09-21 14:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| ee19d6fd-8519-3930-94f2-e6cac1f52e86 | -11.8168 | -50.0482 | 2026-09-21 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| a3cf8f88-2389-333b-89f7-fe328bd71a28 | -7.3259 | -55.6153 | 2026-09-21 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| da3323eb-dafe-3340-a82f-f231374ba321 | -6.0194 | -51.81 | 2026-09-21 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| dc8fa53c-9d44-364f-a3bf-060145d55e63 | -10.2635 | -49.984 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 531dbf39-4d2c-36c6-85cf-e61bacf9f550 | -11.662 | -47.7737 | 2026-09-21 14:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| d9f70c84-9598-395e-b301-1b17e98139a3 | -12.8899 | -50.9695 | 2026-09-21 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| a063dc57-b404-3eb3-ad86-9b4737ae85b9 | -6.6761 | -50.9381 | 2026-09-21 14:50:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 630c14b6-767d-3953-8cba-20442e8f65ee | -10.8909 | -54.0882 | 2026-09-21 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 89439e6c-9b99-3e42-84f1-98103adf517a | -10.911 | -53.984 | 2026-09-21 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b5a999a7-c47c-31c4-b6fc-57b6309babc4 | -10.3917 | -48.8915 | 2026-09-21 15:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 83876e43-6481-3266-9676-29b52c410e4b | -7.5477 | -61.3247 | 2026-09-21 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b580f949-11b7-36c5-84b2-35584ad29474 | -10.6758 | -50.2406 | 2026-09-21 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| da7f845b-7a54-393d-b289-86391dd4cc53 | -9.3986 | -48.3213 | 2026-09-21 15:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 9ac69e50-0532-3234-aabf-d3e189e12bb6 | -10.3914 | -48.9133 | 2026-09-21 15:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 62d7f2d6-e25f-3b45-b0e7-925174b8c6e6 | -9.7693 | -46.0615 | 2026-09-21 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| c2ec5658-0dbe-3461-849b-8b6d14ff6b36 | -12.3102 | -50.1826 | 2026-09-21 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 6911e509-fb05-33fe-b2d8-9cea539fa46b | -8.7267 | -44.8836 | 2026-09-21 15:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| a7aaf2b6-3e5c-3a69-a9cb-2825758a98b2 | -3.6449 | -58.8647 | 2026-09-21 15:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 34b593d6-3989-35ea-8047-c3579d712cb5 | -5.6223 | -43.3701 | 2026-09-21 15:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| fb4d2c17-d2b8-30e4-b4a9-6a17fafc95bd | -9.5593 | -66.0545 | 2026-09-21 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.2 |
| fe2a6e39-9533-3dbf-8438-9a3cfbd5918f | -6.8058 | -55.8217 | 2026-09-21 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 3600f50a-2559-36f4-b823-1cffffac48c8 | -2.9997 | -60.8047 | 2026-09-21 15:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 569d2211-94f3-3e9c-8a31-24a2d83f1455 | -12.5412 | -50.0676 | 2026-09-21 15:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 7dfbd386-2088-34bd-988d-cb68772c57be | -6.5571 | -45.5434 | 2026-09-21 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 7adc84d7-5324-3c45-8f61-928191fefe82 | -6.5444 | -44.9327 | 2026-09-21 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d7f937c7-4731-3f18-8dc9-1be8b4973600 | -6.8985 | -41.6976 | 2026-09-21 15:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 124.3 |
| 7bd594d2-ca5c-3e79-beba-159a0a801463 | -9.8325 | -48.3198 | 2026-09-21 15:00:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 955c93c5-c274-33b6-aa5d-387a2c0c70a9 | -10.2152 | -53.9216 | 2026-09-21 15:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| dbb6702a-0d8f-373a-851e-56416a6215e3 | -12.5761 | -49.1071 | 2026-09-21 15:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| f15ab25a-bc71-369b-b39f-d214fbb8a928 | -13.241 | -51.7571 | 2026-09-21 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 75ea0ae6-b01e-3a58-af87-1f666a22135f | -3.3 | -57.8681 | 2026-09-21 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| bf82ca7a-1c7b-359a-a73c-1d29a6e88b51 | -3.4599 | -59.54 | 2026-09-21 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 528c3ca8-9470-3cb0-9dd5-6f9e0ae68a09 | -3.6947 | -60.5645 | 2026-09-21 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 186b64f9-55b1-3a33-8c65-8014d06a7ef6 | -12.5415 | -50.046 | 2026-09-21 15:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 2ff133a8-738d-3298-840d-1fc7c43d3c4e | -9.2759 | -46.1852 | 2026-09-21 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 8c10ec5c-60d5-362b-8015-4459691f3735 | -9.8307 | -48.451 | 2026-09-21 15:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 98577bac-909a-3f3a-9a98-75cbaa132df4 | -9.7504 | -46.0637 | 2026-09-21 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 163.6 |
| ebbb7239-7228-3790-a582-2724ec53fc2c | -11.8545 | -48.8502 | 2026-09-21 15:00:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 6cc713b1-0bb7-3bfa-8052-afbd37b4f787 | -6.583 | -58.9658 | 2026-09-21 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 7abcee71-dd63-3110-be09-5169ff8301b2 | -6.7123 | -58.9412 | 2026-09-21 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 73a8e9e2-d348-35c8-83d0-5482643648db | -3.4003 | -61.2898 | 2026-09-21 15:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 2a7d9f91-d02b-3688-a877-3685480a23f6 | -2.9158 | -57.7789 | 2026-09-21 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 3b5b3493-2f55-3d7e-98bb-9671efce61c8 | -8.1874 | -54.742 | 2026-09-21 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 3183c40d-e1bb-336f-ab0f-72294d9d4340 | -8.5984 | -54.6139 | 2026-09-21 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| eb5f61ed-c920-3b7c-96a1-3208d39b99a9 | -8.1876 | -54.7219 | 2026-09-21 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 5d01053c-6e80-3fbd-b48b-37f7ed36ea72 | -3.4186 | -61.2895 | 2026-09-21 15:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| fe02e7d9-464b-3bde-94f5-81a5aa62b15f | -3.3867 | -59.5223 | 2026-09-21 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| b5ed4399-b07a-3d4f-8c35-94f276086bd8 | -13.3443 | -51.2973 | 2026-09-21 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 269.9 |
| 5bf99a0e-6db5-38cf-a4b1-cd055af2b043 | -6.1653 | -47.5052 | 2026-09-21 15:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 189666ba-0618-382d-bcb2-2c0f51c395be | -14.08 | -52.1188 | 2026-09-21 15:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 0d24e93d-0726-3939-bf3b-62c699a28bfd | -3.0507 | -50.2702 | 2026-09-21 15:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 7c233761-4c1a-3f18-8df3-f22f96149ac9 | -9.1523 | -49.9853 | 2026-09-21 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 8a098011-c1b3-3b18-a6bd-900d313204cf | -3.6632 | -58.8643 | 2026-09-21 15:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 116.6 |
| a7452fce-5329-373e-9df2-18dbd4154696 | -11.1017 | -48.3072 | 2026-09-21 15:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| acb29fa8-ecb4-30f3-9f6c-b56d61da5a72 | -7.3376 | -44.4744 | 2026-09-21 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 139.0 |
| ebbd227d-f057-3edf-80b8-d0691fdee42c | -10.6875 | -50.7722 | 2026-09-21 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 1e4c79ff-79ee-3bbd-97f1-17d05b5a311f | -3.4555 | -50.5927 | 2026-09-21 15:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| cf1f4174-49cc-322d-b85e-8b678b4fe938 | -8.7706 | -45.8567 | 2026-09-21 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 89218747-855e-3abe-b8f2-0b44b317ac21 | -6.8264 | -55.5222 | 2026-09-21 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 037817c6-7bb2-3687-b480-320c34e74fe2 | -5.7504 | -43.7091 | 2026-09-21 15:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 283.5 |
| 2a4f3f3d-5c35-3852-b762-6540347a00ed | -11.8014 | -49.8129 | 2026-09-21 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| b34ca089-53f0-3cd8-bb0d-8e30d2bf4bec | -7.3291 | -55.1955 | 2026-09-21 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 7cd819f7-dd92-3888-9462-6783087c4f0e | -3.4975 | -59.1752 | 2026-09-21 15:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 8beeb6a3-f0f2-3a4d-b6dd-f2deae6e4ade | -9.1708 | -50.0049 | 2026-09-21 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 508.3 |
| eea3c330-96d7-352f-9070-35800ff5217b | -6.7369 | -55.0874 | 2026-09-21 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |


[Clique aqui para ver as próximas entradas](README135.md)
