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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 535f24d8-1101-37c8-bed8-660acf143f81 | -20.45758 | -44.17926 | 2025-06-03 04:21:00 | NOAA-20 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b5902529-d874-3f90-be1c-b59a1bca8d3a | -23.59417 | -47.4391 | 2025-06-03 04:23:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7b3d7605-3883-36d0-a4b2-30c099f5b62c | -22.70136 | -53.95122 | 2025-06-03 04:23:00 | NOAA-20 | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9e87bced-3e2b-3884-b911-6d8169add1ba | -31.92333 | -52.31314 | 2025-06-03 04:25:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 397fa751-d721-3e55-9f74-cdc1657aa1a3 | -18.8675 | -53.6434 | 2025-06-03 04:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 172.5 |
| dd661fda-e928-3383-87fa-fb80f5f40012 | -18.8875 | -53.6402 | 2025-06-03 04:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 97.7 |
| fd6641eb-3c16-3c68-ad11-13002c19698b | -18.8679 | -53.6218 | 2025-06-03 04:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 6e9beaac-42bc-39d3-86a8-7ffd3d423c14 | -18.888 | -53.6186 | 2025-06-03 04:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 8486c37e-062c-3d0d-ab5e-a25435ce553b | -18.8679 | -53.6218 | 2025-06-03 04:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 88.0 |
| cf8d84a1-9228-3a60-ad67-415b4e48f749 | -18.8875 | -53.6402 | 2025-06-03 04:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 121.1 |
| dbbf737a-cc5b-3229-ace5-294dc6b1c4dc | -18.8675 | -53.6434 | 2025-06-03 04:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 1c0f848a-c3da-3ccf-b8fe-a64e88c40ca8 | -18.8679 | -53.6218 | 2025-06-03 04:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 22556724-d1b7-3d50-b165-7e8d7ea244aa | -18.8675 | -53.6434 | 2025-06-03 04:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 0bde6625-81fa-35dc-8ace-e29f8f961a95 | -18.8875 | -53.6402 | 2025-06-03 04:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 99224eec-a568-3d40-8029-219a9f8be699 | -18.888 | -53.6186 | 2025-06-03 04:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 66cca0c5-ce8e-36b0-b964-bd30994f12df | -11.9027 | -54.7931 | 2025-06-03 05:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 3f4415ca-d087-3005-89be-99b93f576a3a | -18.8875 | -53.6402 | 2025-06-03 05:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 2bb5cf3c-2854-3639-91c5-04868b6b9f2d | -18.8679 | -53.6218 | 2025-06-03 05:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 81.0 |
| f9e5f26f-211e-30ab-9954-0964bd88e269 | -18.8675 | -53.6434 | 2025-06-03 05:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 38c9918a-2b72-3709-b36e-23c0e0adbea4 | 0.68877 | -51.46001 | 2025-06-03 05:08:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1027c83b-04dc-3779-9e1e-06f4a8bfee6a | 0.69113 | -51.46222 | 2025-06-03 05:08:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1866f08-dc16-3a70-8fca-0a8edea03c77 | -18.888 | -53.6186 | 2025-06-03 05:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 78bf5f33-fc8c-3b67-bddf-11ced3db633e | -18.8675 | -53.6434 | 2025-06-03 05:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 73cb5ef9-26c9-3540-9637-487ef69f2569 | -18.8875 | -53.6402 | 2025-06-03 05:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 37db2553-f8e4-3729-b60d-5f40345c4ece | -11.9027 | -54.7931 | 2025-06-03 05:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| e50d397a-3bd4-3411-ac81-ac95d68f789a | -18.8679 | -53.6218 | 2025-06-03 05:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 768bcdf5-0e01-3058-9e85-6be9655124fc | -2.58814 | -51.92227 | 2025-06-03 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33c37bce-9b98-32db-b305-4fbcdc1befc0 | -9.06779 | -47.15602 | 2025-06-03 05:10:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| faf92d1b-63bb-33cf-b0e4-2ceb886fb005 | -7.08272 | -46.5614 | 2025-06-03 05:10:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed35eb40-af7f-3a48-bbf0-52b6a677d2e6 | -4.81179 | -45.26231 | 2025-06-03 05:10:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 184b4f75-cacf-3aa5-bea5-78519f484a97 | -9.19301 | -49.69704 | 2025-06-03 05:10:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e759712-c95e-3a84-8ce2-0febe3e0ec2d | -7.709 | -46.31626 | 2025-06-03 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0581f020-9030-3f41-9e08-0a777f1020c2 | -4.24738 | -47.58658 | 2025-06-03 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57796b93-e7ad-3a49-9adb-f656dc9ac156 | -7.71525 | -46.32172 | 2025-06-03 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc6ea259-6212-3cea-874b-9617f4ba4d20 | -8.06114 | -46.79716 | 2025-06-03 05:10:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad843086-3ba6-3e9e-bb3b-d5174404c9c2 | -3.98807 | -48.40825 | 2025-06-03 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55bd7872-991b-3355-aaaf-5d762d5bb30d | -7.7084 | -46.321 | 2025-06-03 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a9769db-7509-3540-9f7a-4033281ba0fd | -8.91101 | -50.04418 | 2025-06-03 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 49d8c27f-7b5c-34fa-9b53-4f08e5b7a437 | -6.63475 | -55.01035 | 2025-06-03 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04f33dde-adeb-3249-aab2-3d447bb29eef | -8.96777 | -47.97033 | 2025-06-03 05:10:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cec5c7a9-2332-3f8f-92aa-142e2a82d8a8 | -4.12998 | -54.89862 | 2025-06-03 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fc38fb5f-c22a-3384-a375-5882d062b33f | -9.07073 | -47.15574 | 2025-06-03 05:10:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 78f5acdf-360d-3588-84ee-fec22b17af83 | -9.40586 | -48.42092 | 2025-06-03 05:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58ae0318-f381-3f78-b1db-71c5d91d5ae1 | -3.98851 | -48.40523 | 2025-06-03 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b294295-1c73-3851-be09-3a69a17502ed | -8.84625 | -49.85166 | 2025-06-03 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c03aaa17-a9f7-38ef-85b8-311a5381bf6c | -8.91025 | -50.04969 | 2025-06-03 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 58fb11c4-036c-3099-bec4-7ab9939dbefd | -7.68543 | -44.57651 | 2025-06-03 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0057f21-860f-37ff-aa84-8be0d480c9bd | -8.9156 | -48.90179 | 2025-06-03 05:10:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a12a66b-e82a-3c8e-8f4c-e90cb828c6fd | -8.90755 | -50.05001 | 2025-06-03 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e9580569-47f1-33ee-b099-08a66aef39ef | -8.847 | -49.84594 | 2025-06-03 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2bcefce-f967-35cb-bb38-6718209fcaa9 | -7.70346 | -45.77671 | 2025-06-03 05:10:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ce670c5b-3fa6-38c5-8027-8d8a431a2b0e | -4.8174 | -45.26846 | 2025-06-03 05:10:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22da1765-fdd5-3076-b074-ae9db1478cb5 | -9.39437 | -48.42298 | 2025-06-03 05:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cd555b9-9eb1-36de-9cb3-d2acf8c6ccbb | -8.97056 | -47.96913 | 2025-06-03 05:10:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c125e5e9-7a22-3806-80bb-360d94b56b0f | -9.39802 | -48.43827 | 2025-06-03 05:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d01f59a7-2328-3a78-8a28-0fc266130b35 | -7.90427 | -50.36614 | 2025-06-03 05:10:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44063ea9-1710-3007-8935-be17ccee2aba | -9.38794 | -48.4294 | 2025-06-03 05:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15b9773f-8b51-3924-b20d-38348854250b | -8.60381 | -51.57127 | 2025-06-03 05:10:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b96c4e4e-4b2b-3691-9436-8181cb373a02 | -9.11447 | -49.63593 | 2025-06-03 05:10:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3f6d3d1-d59c-3278-9ecb-c1d80208f577 | -7.68623 | -44.57026 | 2025-06-03 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee88eb4e-c246-30a6-8e03-b439eb21511c | -8.9103 | -48.901 | 2025-06-03 05:10:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a75e1004-24e5-37f3-a846-4aa4549ef371 | -8.91516 | -48.90509 | 2025-06-03 05:10:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb733b50-a384-32c8-80e1-52c8080735ef | -9.19339 | -49.69412 | 2025-06-03 05:10:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a82c3a75-e837-3fcc-afe0-85752af984a8 | -8.72382 | -50.26477 | 2025-06-03 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86c46465-5c5f-3e46-a7eb-ee300526da53 | -8.56646 | -48.86935 | 2025-06-03 05:10:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d926a87-431f-3169-92b0-da1de616e5ce | -7.70912 | -46.32052 | 2025-06-03 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03bd0342-e673-3e16-a7ca-5c00ac685880 | -4.2479 | -47.58296 | 2025-06-03 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 358ed83b-7444-38d4-a0fa-f49e835c0adc | -9.39848 | -48.43465 | 2025-06-03 05:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6d27853-786b-3acd-acf2-8339654791cd | -9.19377 | -49.69118 | 2025-06-03 05:10:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 627844d6-d703-382a-9dff-e3a9ecc67df1 | -7.69308 | -44.57125 | 2025-06-03 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 326a1306-8e64-3448-b919-863cd62b19c9 | -8.19893 | -49.80122 | 2025-06-03 05:10:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aaea1cda-5dc9-3a80-95b8-b65c79487c97 | -9.3884 | -48.42579 | 2025-06-03 05:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 012c6947-e0f6-3858-9b35-1cf2dcb1d899 | -9.40351 | -48.43913 | 2025-06-03 05:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b52a954a-a5d6-3d51-93a5-67c530896832 | -3.98898 | -48.40213 | 2025-06-03 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b185214a-c45b-386b-a6d2-408de230e9fc | -9.07019 | -47.15993 | 2025-06-03 05:10:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab6762f0-71ad-3b79-8c0e-879d1edfd6ab | -8.90827 | -50.0445 | 2025-06-03 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6302d249-2205-3493-a36e-c3ea4b71c8b3 | -3.98686 | -48.40186 | 2025-06-03 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6821b4bc-3e06-3e03-896e-6059f8ec0420 | -7.71452 | -46.32224 | 2025-06-03 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96ec009b-f8e5-3c7b-971e-d38f01b2ce70 | -9.37832 | -48.41681 | 2025-06-03 05:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d05ca04-f2bc-3380-b28e-7036899715d0 | -8.90534 | -50.04904 | 2025-06-03 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 255b33c7-bed3-30b7-acd3-6a7ab7469692 | -9.40538 | -48.4246 | 2025-06-03 05:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fc90745-b528-32e9-9c42-c37b0cc018dc | -9.11075 | -47.72406 | 2025-06-03 05:10:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a58d78ba-aea2-3abd-8320-9beb529fee3d | -8.90609 | -50.04355 | 2025-06-03 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9f9e45fc-5a10-3d49-9d64-0057bdb0c148 | -9.07375 | -47.15686 | 2025-06-03 05:10:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7317a903-10e0-32ac-8b38-e62f99ced56a | -8.60319 | -51.57267 | 2025-06-03 05:10:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8707d5f1-9382-3d6a-8457-436d91776934 | -4.8181 | -45.26347 | 2025-06-03 05:10:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e78b0624-23e5-3c51-a518-2afcc428f3d7 | -7.0833 | -46.55696 | 2025-06-03 05:10:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4f68206-630d-3a3f-ac65-f6ad83370738 | -8.60322 | -51.57561 | 2025-06-03 05:10:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbb989c2-f2a4-3e34-9da8-98a1be1dc749 | -8.84525 | -49.85 | 2025-06-03 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce3cd9e3-7672-3dca-a0af-48d2247e2e1b | -3.98599 | -48.408 | 2025-06-03 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f228b6d8-3b42-301d-87f9-2bceb53a3f9f | -9.19843 | -49.69484 | 2025-06-03 05:10:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9be34d47-595b-3f64-b5c5-be0da2ed260a | -9.40398 | -48.43551 | 2025-06-03 05:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57a442c8-cae4-3a1b-8fb7-08b3833a843f | -9.19805 | -49.69777 | 2025-06-03 05:10:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2394e8be-ae5a-3baf-8369-ba9ff4302c9c | -9.43517 | -62.46183 | 2025-06-03 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 241ae22b-7e88-3226-9424-51368e7ff5d8 | -9.61112 | -49.0233 | 2025-06-03 05:12:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92f31262-72fc-3005-a2ca-46ef462fd053 | -8.73403 | -63.85112 | 2025-06-03 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67ec1980-88be-3f11-89c3-65567bdc2b72 | -12.23426 | -54.31589 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 23dfe91b-d16b-3bb0-89d3-461a164b50e6 | -11.58086 | -47.45346 | 2025-06-03 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f33170da-f156-39f2-8dfe-7829140efacf | -10.23821 | -52.22366 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 684cb979-7a3a-3bda-b548-93e487f288ba | -10.1438 | -52.14211 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README13.md)
