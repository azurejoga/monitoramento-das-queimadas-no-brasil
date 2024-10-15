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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 869caced-9733-34c5-9290-c221c703cce2 | -8.4639 | -47.822 | 2024-10-15 00:25:54 | GOES-16 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| dd5bb4f8-9ca6-3647-828e-5043dd0c0878 | -8.4642 | -47.8 | 2024-10-15 00:25:54 | GOES-16 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 9950761c-fa3b-307e-abbd-9a85ae0841f4 | -8.9141 | -47.9103 | 2024-10-15 00:25:56 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 8e8dc08c-906d-3447-840e-0fa63ca2ff7c | -9.0852 | -47.7836 | 2024-10-15 00:25:57 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| fd66fbe7-16bd-3b09-8b16-539c8ea9374a | -9.2549 | -60.8863 | 2024-10-15 00:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| caa94d92-1843-304a-b5d2-2815c1d8eb42 | -9.255 | -60.8671 | 2024-10-15 00:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 2555914c-7b6f-3987-b220-d8cbf7710353 | -9.6874 | -46.4984 | 2024-10-15 00:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 53951f3d-c083-3d45-9708-33f4c84c1936 | -9.6878 | -46.476 | 2024-10-15 00:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 90ce12ce-2eb8-3f32-aa3c-0fa54f9cc433 | -9.7067 | -46.4738 | 2024-10-15 00:26:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| f8493d38-166b-37ae-939b-40283a78eae3 | -10.0495 | -47.6589 | 2024-10-15 00:26:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 9f1d8e26-ff9a-3349-92e4-f09e8919946f | -10.0498 | -47.6368 | 2024-10-15 00:26:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| e72922a0-672a-3803-b7b6-96c2fb128ce6 | -10.0678 | -47.701 | 2024-10-15 00:26:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| daafa5e4-e844-3c65-9451-14cfeb566dc4 | -10.0415 | -54.3442 | 2024-10-15 00:26:03 | GOES-16 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 0051d725-e752-3f91-b003-cb7b7570aaef | -10.0417 | -54.3238 | 2024-10-15 00:26:03 | GOES-16 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6ee9bfd8-984a-3cc5-9c4c-0b66061ad986 | -10.1447 | -46.3102 | 2024-10-15 00:26:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| a16a2f4a-f337-367a-bb46-f1aa1532ff6e | -10.1637 | -46.3079 | 2024-10-15 00:26:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| c2b300ec-c863-311b-83cd-03495e728d6a | -10.164 | -46.2853 | 2024-10-15 00:26:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| db97aff8-0b1d-310c-bbfe-ffa7129c4f4d | -10.3524 | -61.1946 | 2024-10-15 00:26:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| fd755101-9cee-3bc0-a6cd-488bcc9b0a58 | -10.3711 | -61.1935 | 2024-10-15 00:26:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 224.3 |
| 8c63938d-bd67-315d-a66f-56e33bf5a360 | -10.3713 | -61.1743 | 2024-10-15 00:26:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 0756ef4d-ff8c-3b4f-9d2e-9c312e1566c9 | -10.822 | -49.256 | 2024-10-15 00:26:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| c67da053-d185-3466-ad4b-e3b4498132ee | -10.8224 | -49.2343 | 2024-10-15 00:26:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 34bb5e0b-a34f-30b1-9991-e920d285ea4e | -11.6915 | -65.2432 | 2024-10-15 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 7c950b7c-5b1f-3f96-8a36-e907ecbb39fb | -11.6917 | -65.2243 | 2024-10-15 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| bbdab924-4886-31b2-bd86-59e101d43eb5 | -12.0796 | -50.2966 | 2024-10-15 00:26:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| a7a350f2-445b-362c-8a3e-53c57d2e31f6 | -12.0799 | -50.275 | 2024-10-15 00:26:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 5023a272-5ec9-38cf-8921-32a5f19ea00a | -12.087 | -51.0656 | 2024-10-15 00:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| fbfe7346-a63d-331f-81e6-ceec5bfad874 | -12.0987 | -50.2943 | 2024-10-15 00:26:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 1c9c2f36-ca99-30d7-8bd2-45b8ae3e3387 | -12.099 | -50.2728 | 2024-10-15 00:26:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 53b747ea-14e0-3c13-b181-4280f03abfd2 | -12.3793 | -63.7294 | 2024-10-15 00:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 47cc3939-43b8-3451-831a-c7fc888e85c5 | -12.3795 | -63.7103 | 2024-10-15 00:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| a97f5b83-2c3d-32bb-bb6f-c34c38a245a8 | -12.3982 | -63.7284 | 2024-10-15 00:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 70.9 |
| c8dea0bd-cb09-3776-820c-17ab6f2c9e94 | -12.4961 | -63.2641 | 2024-10-15 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 0c86afa8-e8c9-3be5-9b3d-99e775991405 | -12.5149 | -63.2822 | 2024-10-15 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.3 |
| c7552eed-3745-3025-938a-04bd6d1978af | -12.515 | -63.263 | 2024-10-15 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 3a9d8091-7752-3855-a2a1-7a0d2f4c4ba9 | -12.9538 | -62.7962 | 2024-10-15 00:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 89.7 |
| c52bfea0-d947-3342-a244-c9530df05531 | -12.9728 | -62.7951 | 2024-10-15 00:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| d01067e4-4174-3fdf-a0a8-f691a3ab3bbb | -13.1285 | -62.3227 | 2024-10-15 00:26:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 109.5 |
| fac3da9d-298b-3e46-9988-315659101b9f | -13.1287 | -62.3034 | 2024-10-15 00:26:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 89493c21-36fd-36b8-a032-ea5e834e8dad | -13.1473 | -62.3408 | 2024-10-15 00:26:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 106.5 |
| a1517540-62d6-30c4-a8ef-3d53255946ce | -13.1475 | -62.3215 | 2024-10-15 00:26:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 197.0 |
| 362ac171-aebb-3f22-82ff-5923c6ebfff1 | -13.3596 | -61.9595 | 2024-10-15 00:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 67525f82-ef63-3066-aa53-14041147c44e | -13.3653 | -61.357 | 2024-10-15 00:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 3344962a-66b6-35c7-8ccc-6cbff29a089b | -13.3655 | -61.3376 | 2024-10-15 00:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| cc068452-9a02-3d3b-9c30-bdd3e1f79d45 | -13.3786 | -61.9582 | 2024-10-15 00:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 1b73fd94-06c1-3cd3-9a10-62b4ae02de3d | -14.0749 | -46.1749 | 2024-10-15 00:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 5108cf1a-6c6d-3ff8-8e9d-52cab7094b08 | -14.0944 | -46.1717 | 2024-10-15 00:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 2c50e74d-64ed-3a88-bd07-71014ce51dbf | -14.0948 | -46.1486 | 2024-10-15 00:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 3f508170-b55b-3181-b7c8-3ba4809bf818 | -14.1138 | -46.1684 | 2024-10-15 00:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 8b3185a1-4081-3149-bee6-b3c778832c9e | -1.531 | -54.3359 | 2024-10-15 00:35:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 2ab3424d-9c09-3971-9dd7-1c249410dd20 | -1.8577 | -47.8493 | 2024-10-15 00:35:16 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| dcfbea96-e913-397c-8cc7-fdb224ec7901 | -1.8578 | -47.8276 | 2024-10-15 00:35:16 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 24464f23-1995-3c24-a117-e09ed200ba35 | -2.4418 | -50.2447 | 2024-10-15 00:35:20 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 48e397e6-68a0-3c48-8fd0-98f129f55d41 | -2.4419 | -50.2237 | 2024-10-15 00:35:20 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 9ed0a492-6988-3d0d-b58c-4dacc89e6ab3 | -3.0397 | -53.2603 | 2024-10-15 00:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 8acaf4f7-f8b6-3715-a0e2-e14d46b314ef | -3.1099 | -54.2263 | 2024-10-15 00:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 86608c4f-5f25-3109-850d-e2b6159e09b6 | -3.1282 | -54.2459 | 2024-10-15 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 2f96eae6-81fa-34b2-baa4-20f71d9f787f | -3.1283 | -54.2259 | 2024-10-15 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 9c63337f-5d75-3afb-94fb-f32ae8ba7f06 | -3.5861 | -54.6741 | 2024-10-15 00:35:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 60bfe38f-d368-3165-9d6c-6b458c219021 | -4.3774 | -47.7627 | 2024-10-15 00:35:31 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| cb2cba89-8154-389f-a937-f5682701a63b | -4.3959 | -47.7618 | 2024-10-15 00:35:31 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| e1c329d3-55da-32f6-a298-6463ac8c53f9 | -5.1983 | -44.8497 | 2024-10-15 00:35:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |
| e2a6915f-d32d-3c5d-a1c6-6420783e04cb | -5.217 | -44.8485 | 2024-10-15 00:35:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 267.4 |
| 8db1025c-03e3-3444-a5dc-91e254551001 | -5.2172 | -44.8258 | 2024-10-15 00:35:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| a3bdd844-0b66-31bd-a2ad-969cd5e3975c | -5.2797 | -46.3725 | 2024-10-15 00:35:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 15b32af8-c7e3-3cde-a7e8-f88b18a39286 | -5.2982 | -46.3936 | 2024-10-15 00:35:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| dca7f07c-70c0-3abd-8c50-690e9c9526c2 | -5.5732 | -49.3995 | 2024-10-15 00:35:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| af21d71a-8e66-3803-9be3-e6047a239198 | -6.5505 | -48.2408 | 2024-10-15 00:35:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 3cd00160-e2bc-39ea-aa0b-245a28075e70 | -7.5093 | -49.4831 | 2024-10-15 00:35:48 | GOES-16 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 8dd472c8-bcaf-3012-93b1-08fa11ac59f9 | -8.4639 | -47.822 | 2024-10-15 00:35:54 | GOES-16 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 70f2d100-5d10-3303-b076-b0cd901522f3 | -8.4642 | -47.8 | 2024-10-15 00:35:54 | GOES-16 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 8313baac-9842-3066-8687-cb9d2bc6b520 | -9.0852 | -47.7836 | 2024-10-15 00:35:57 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 307680c9-0aca-35c2-bf19-4342881e5ec2 | -9.3493 | -63.5846 | 2024-10-15 00:35:59 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| c6bbe8a6-20fe-3bb3-9f78-79e8bd10d19f | -9.3494 | -63.5658 | 2024-10-15 00:35:59 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 575df20f-76cb-3efa-bbe3-1f30ac26a872 | -9.9222 | -47.297 | 2024-10-15 00:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| d4a99847-cc89-3733-90fd-15a82210aa85 | -10.0415 | -54.3442 | 2024-10-15 00:36:03 | GOES-16 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 9e2dd1e3-ada6-306e-a585-01bf9e93c48f | -10.0417 | -54.3238 | 2024-10-15 00:36:03 | GOES-16 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 0c70d82a-62db-31ac-b473-ac7be1bf0d9d | -10.3954 | -44.8206 | 2024-10-15 00:36:04 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 879516aa-5ab6-302a-a779-a4f0064b4565 | -10.3524 | -61.1946 | 2024-10-15 00:36:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| aba896ae-456e-355b-acf7-729aed8450ba | -10.3711 | -61.1935 | 2024-10-15 00:36:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 193.7 |
| a521feef-81b4-308f-a37f-7b1b25b35a4f | -10.3713 | -61.1743 | 2024-10-15 00:36:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| cb7e28e8-ff36-34ec-bf14-2931babb4d4b | -10.3898 | -61.1925 | 2024-10-15 00:36:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 4fe0392b-85f3-38c4-b5bf-071a9c5ae12d | -10.822 | -49.256 | 2024-10-15 00:36:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 5b68b6b6-6e2d-3d00-a182-d151700049b5 | -10.8224 | -49.2343 | 2024-10-15 00:36:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 83305f03-53a7-3f6c-b1ac-dd54f816e101 | -10.9473 | -54.1037 | 2024-10-15 00:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| a7e5560c-6fa1-3d56-abeb-991ef535957c | -11.6915 | -65.2432 | 2024-10-15 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| f5f9fcde-4028-37a5-9c74-a90b37f351d2 | -11.6917 | -65.2243 | 2024-10-15 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 38b26a59-1517-30e4-a807-9978f8318b9f | -12.0796 | -50.2966 | 2024-10-15 00:36:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| d5b1d00b-6cfb-390b-8f2d-e37dffc987d9 | -12.0799 | -50.275 | 2024-10-15 00:36:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 3a65a3a8-ea5c-3018-b48f-f74f5087c634 | -12.0987 | -50.2943 | 2024-10-15 00:36:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| aca64e05-742f-3e2e-862b-d03061eeae82 | -12.099 | -50.2728 | 2024-10-15 00:36:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 9a4a7958-cd0f-3ba0-ae0e-fd54c69cb038 | -12.3793 | -63.7294 | 2024-10-15 00:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| cf02f74f-3eb0-37f3-b9d3-8125e2e8c5a2 | -12.3982 | -63.7284 | 2024-10-15 00:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 84.1 |
| d367443e-e01e-3188-8a07-b2874695487a | -12.3983 | -63.7093 | 2024-10-15 00:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 45b44f02-fefb-3ca3-877c-2aefa707ddc9 | -12.4961 | -63.2641 | 2024-10-15 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 2ea9c191-96f5-34be-9dcc-e2b6db047b90 | -12.515 | -63.263 | 2024-10-15 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 40afd261-51bb-3c13-b638-912edc4136fb | -12.9538 | -62.7962 | 2024-10-15 00:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 5d81401d-a886-3036-b174-8f6b38b068b7 | -12.9728 | -62.7951 | 2024-10-15 00:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 92.7 |
| c66d448f-a157-3fc1-9403-b71306c945ae | -13.1285 | -62.3227 | 2024-10-15 00:36:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 105.7 |
| bc56031c-d684-3093-a165-288e5ea75c07 | -13.1287 | -62.3034 | 2024-10-15 00:36:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 94.8 |


[Clique aqui para ver as próximas entradas](README11.md)
