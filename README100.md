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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66194d33-6ef5-38a3-938f-7548629db2fd | -14.111 | -46.3063 | 2026-09-29 18:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 48646731-1eb2-3f29-ac4d-eae664f187f7 | -11.1625 | -50.6367 | 2026-09-29 18:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| e9f8def6-86bb-3361-a2e0-cc4fd0f41153 | -11.6212 | -43.5011 | 2026-09-29 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.6 |
| aca0b3b4-ad44-3f68-b30c-da1f7a945eeb | -14.4639 | -45.2286 | 2026-09-29 18:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 220cc74b-6256-3374-9fbc-dc0a61c8a2f4 | -11.0241 | -49.7088 | 2026-09-29 18:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| fc9c1031-b98b-3bdb-ba76-165f4ee82381 | -11.1958 | -44.8269 | 2026-09-29 18:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 215592e9-376c-3421-95b9-9826f9157441 | -14.1115 | -46.2834 | 2026-09-29 18:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 127.9 |
| a06493f8-8443-3c80-95b1-5de652af67c0 | -11.3922 | -43.4417 | 2026-09-29 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.4 |
| c7fecc6e-6275-39b1-be64-5c944d035658 | -8.0166 | -42.8681 | 2026-09-29 18:20:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| f7e14772-90b4-3c0d-9a7a-7a1923f5c9e1 | -11.6797 | -44.5012 | 2026-09-29 18:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 748bc05e-372b-3d95-918e-080e0cacf71f | -11.699 | -43.4416 | 2026-09-29 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 211.3 |
| 1c9e70fa-fd6c-30d6-b7ad-293d7248ad35 | -10.7255 | -44.4291 | 2026-09-29 18:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| da7ce0bf-f874-3def-9ba1-a3239c634fb8 | -11.4302 | -43.4596 | 2026-09-29 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 294.9 |
| 79c34f12-ea27-3c70-ada0-489fa9f364e6 | 2.569 | -50.848 | 2026-09-29 18:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 75.5 |
| c800e171-fe12-3ae2-9d68-1f37ec3c5b88 | -8.3617 | -45.4013 | 2026-09-29 18:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| d2157e08-71eb-356a-97e3-974efe70e109 | -8.6451 | -45.3489 | 2026-09-29 18:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.8 |
| c420fdb3-b8e5-3f71-b171-62a1c5ca899c | -10.9343 | -50.7039 | 2026-09-29 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 9235d263-de51-3a66-87e0-8be2be8bbc1b | -9.0783 | -49.8853 | 2026-09-29 18:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| d2ab8560-4daf-3b32-8cf5-e11612127a19 | -0.5073 | -49.1326 | 2026-09-29 18:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| baeea263-64a9-3480-ba2a-bb49c9432737 | -11.1907 | -45.1274 | 2026-09-29 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 96c6b3be-2e34-3a66-852e-46780317efcd | -10.6505 | -50.7123 | 2026-09-29 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 3f827ba5-23af-3cb4-9b63-bee7dd26f4a5 | -12.4346 | -44.1733 | 2026-09-29 18:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| c9feb367-810a-320f-a564-e4157efb51f7 | -9.9956 | -50.2675 | 2026-09-29 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 40ab1b4f-c50e-3aee-907a-60094e8d7e19 | -6.9795 | -71.7732 | 2026-09-29 18:20:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 227.0 |
| dd06b071-2454-3ee1-a5ad-db7871ba896f | -13.3641 | -44.0166 | 2026-09-29 18:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 7cc93de0-cd3f-39e3-938d-b3e626efcea5 | -15.7547 | -46.0347 | 2026-09-29 18:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 60aeb5ff-8641-317f-a93b-0c40ea3105b0 | -11.4119 | -43.415 | 2026-09-29 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| b5353b8b-d31f-338c-a7a1-40ff4f8038c4 | -6.9795 | -71.7732 | 2026-09-29 18:30:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 213.4 |
| 5f62fb0c-60e3-35fb-974a-f3e457b813bb | -9.0783 | -49.8853 | 2026-09-29 18:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 2531014a-6d99-3fc6-abd3-6d3582215af3 | -11.3922 | -43.4417 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 259.9 |
| a2deda9e-2397-309e-8bb1-6e87e52795be | 2.569 | -50.848 | 2026-09-29 18:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 38dc05a6-6d5b-3b88-8182-fc8bedbfb573 | -11.2753 | -43.5539 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 0bd744ba-6087-367d-a893-f149741ff4c7 | -8.9633 | -44.1655 | 2026-09-29 18:30:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 44fbcfc4-1328-3199-89c5-33103d12a984 | -10.9533 | -50.7018 | 2026-09-29 18:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 9818b495-f0ea-3655-97f4-f0f92b0b7410 | -15.1847 | -46.141 | 2026-09-29 18:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 115.4 |
| eb275a99-f4c7-3772-ba37-4aa8383c37ee | -10.2843 | -44.6274 | 2026-09-29 18:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 8f21f35e-b900-33ca-8258-fde0d570249b | -9.434 | -41.8356 | 2026-09-29 18:30:00 | GOES-19 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 9b1d13df-b428-3069-a5b1-9d1609b2f9f6 | -4.2338 | -46.9387 | 2026-09-29 18:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 0d77c472-4d62-3af3-acdc-3bb821c9f65c | -8.9823 | -44.1633 | 2026-09-29 18:30:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 3594b14b-7011-3180-a593-469a7aae6005 | -10.6505 | -50.7123 | 2026-09-29 18:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 131.4 |
| fe3f0958-c032-3d4b-88b9-826679dd5e56 | -7.7874 | -71.9851 | 2026-09-29 18:30:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 114.4 |
| fbf419e1-941b-3c7f-8b1a-3bdd850bcf9d | -15.2043 | -46.1374 | 2026-09-29 18:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 198.5 |
| a445cea1-4099-310b-8562-c32cb629db98 | -11.1273 | -43.2687 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 104.2 |
| b3e9beb5-7b89-355e-afc4-091197b172e0 | -10.1241 | -43.928 | 2026-09-29 18:30:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| bf4fd6f3-437e-3ced-824e-dfbdbfa0d6cc | -13.1803 | -48.5409 | 2026-09-29 18:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 9f260e21-cc55-306a-b463-b5782acb4aee | -11.4311 | -43.4121 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 39129ed0-e7a5-361e-9db7-f6f295f068d1 | -11.0241 | -49.7088 | 2026-09-29 18:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| f313907b-e841-33b6-abe5-f403f0c3fb3e | -11.6207 | -43.5248 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 9cc98e87-1e78-35ac-9d0a-b5f9965aca3b | -8.2102 | -45.4621 | 2026-09-29 18:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 282cdf59-168a-34c9-aee0-5e2fa67eaeee | -11.3927 | -43.418 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 29f9d11a-ae49-377a-8f8e-2ef02f0ecb8a | -8.9294 | -49.7706 | 2026-09-29 18:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| f7750fea-4109-30d7-b189-7e2c06de7964 | -11.2758 | -43.5303 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.5 |
| bbaea67b-775d-39a3-9b79-0ed42052f650 | -10.6869 | -44.4576 | 2026-09-29 18:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| c7d83417-e5c3-38df-8991-d9bc15c6a9af | -11.4119 | -43.415 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.0 |
| ab090057-e881-343d-9441-d52035ffab95 | -11.449 | -43.4803 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 2c45e8de-09af-3677-9d9f-f2348ce850d5 | -13.3641 | -44.0166 | 2026-09-29 18:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 729547d7-8802-3ed6-8ca7-707d9abcf9bc | -10.6967 | -48.7486 | 2026-09-29 18:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 844362f8-7eed-3c9f-a6e2-cbf49c2427c9 | -11.2566 | -43.5331 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 294.8 |
| 8f747c7c-0fcd-3e40-a74d-28b3010cbcf4 | -11.7178 | -43.4623 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 208.7 |
| bbe3554f-c590-3eb7-b116-bcdba8f64c70 | -10.2067 | -49.9898 | 2026-09-29 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 456f3c9f-2e70-3127-97cf-a37448956342 | -11.7834 | -51.0152 | 2026-09-29 18:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 123.6 |
| cd1b8e93-531c-34df-831c-17417e451246 | -11.1815 | -50.6347 | 2026-09-29 18:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 81db0e46-1474-3945-8f75-472f0e6ca8e2 | -11.7831 | -51.0365 | 2026-09-29 18:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 3d4a99b0-a0e7-3527-b1d1-c35b4ebbfaa1 | -11.6596 | -43.4951 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 1a7d93e0-d404-3ef9-8bc2-f2e38a4b9de5 | -10.9066 | -43.8669 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 249.8 |
| ec04b28f-1924-3743-9ba8-5d4793747419 | -14.0915 | -46.3096 | 2026-09-29 18:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 136.6 |
| b5bd8b39-6521-325e-bf89-80d13ccdb3bc | -10.7056 | -50.8341 | 2026-09-29 18:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 213.0 |
| 5a153ae3-06db-3c4d-9749-a9291d37a79b | -11.6212 | -43.5011 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 9fc4155c-40f8-369c-b78b-6e8560c88f23 | -8.3614 | -45.424 | 2026-09-29 18:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 8df51d05-0844-37d4-a32e-5d1d8c02533a | -10.8851 | -50.1539 | 2026-09-29 18:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 66544c2a-714e-3d8f-91be-4513ce4f5a67 | -9.0783 | -51.5346 | 2026-09-29 18:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 3c1c6b98-07e6-31b1-a53b-17a8398a8da1 | -9.1337 | -49.9656 | 2026-09-29 18:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 02b8fe8e-0da8-3226-8c8f-26470c860240 | -8.8548 | -49.7345 | 2026-09-29 18:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 5ab9afb0-266a-3b6c-931a-664ef42817fc | -15.9476 | -39.9576 | 2026-09-29 18:30:00 | GOES-19 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 107.5 |
| 5556a43e-a899-3225-9ba5-7866526f293b | -11.6797 | -44.5012 | 2026-09-29 18:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 6fc51db6-3b1f-3cac-86b3-eb9c63541154 | -11.5628 | -50.5069 | 2026-09-29 18:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 493a95b4-3b70-3d7e-99cf-135844ab2455 | -15.1986 | -41.4228 | 2026-09-29 18:30:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 110.2 |
| c8b19661-8446-3cf6-8de1-6a3c0757cb7c | -10.1051 | -43.9306 | 2026-09-29 18:30:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 58450195-24d2-3025-9757-fa116a21961e | -10.9545 | -45.5724 | 2026-09-29 18:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 40719af1-5746-333f-a654-9aa08ea5815c | -11.699 | -43.4416 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.5 |
| 42bf87ae-e12f-34f2-92c5-7e60d9a584f0 | -11.2561 | -43.5568 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 199.8 |
| c4a1bbd1-08ed-34b5-8ef2-4d142a331a52 | -9.0969 | -49.9049 | 2026-09-29 18:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| fad81207-74ca-3efb-b9bb-f65ea50083d4 | -11.3931 | -43.3942 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| c30b15c1-0c14-37c5-b675-2d88883b1b74 | -11.4791 | -49.743 | 2026-09-29 18:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 1fe49533-7fa4-3ced-9e6a-411d9f6ffeae | -16.9411 | -42.0873 | 2026-09-29 18:30:00 | GOES-19 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 147.5 |
| 8703d5ed-57a5-36a4-be74-279f316f5bc9 | -11.4115 | -43.4388 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 250.5 |
| b2bef445-5fc3-3ad1-9780-deccdde38f25 | -10.1878 | -49.9918 | 2026-09-29 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 1a48d781-233c-3bd6-a002-c37e61caa4b9 | -9.9595 | -50.1431 | 2026-09-29 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| d8850f84-be04-3716-9168-d747b3794919 | -11.6404 | -43.4981 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 1bed87d8-81db-357f-828f-e94af155e20b | -0.5073 | -49.1326 | 2026-09-29 18:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| aff0a55f-46d0-32f6-8c42-4048ef77cede | -15.7547 | -46.0347 | 2026-09-29 18:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 2ea335a2-a18a-35b7-babc-77345efc3abc | -11.8132 | -49.0519 | 2026-09-29 18:30:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| e6f90f25-674c-3b67-bae3-612fd5b9e973 | -8.5051 | -72.4721 | 2026-09-29 18:30:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 005cdfe6-8f9f-3e48-8e74-6f512e27db12 | -11.4495 | -43.4566 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 5ef1452e-fa6d-3b21-a306-ea168858bc23 | -8.2283 | -72.821 | 2026-09-29 18:30:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 122.7 |
| ac4d3275-aad1-3162-810c-c4952074e2f3 | -10.934 | -50.7252 | 2026-09-29 18:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 1d87b903-8bb4-3f28-a349-a57b6b05968c | -10.207 | -49.9684 | 2026-09-29 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 19dec00b-e729-39d9-bddc-6056b7bbc17a | -9.1157 | -49.9032 | 2026-09-29 18:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 161.5 |
| 20229f02-bcdc-327e-815f-deb7bf493695 | -11.6986 | -43.4654 | 2026-09-29 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.2 |
| cf62f5c8-6228-3679-9da5-774ad0b3de2d | -14.1115 | -46.2834 | 2026-09-29 18:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 167.1 |


[Clique aqui para ver as próximas entradas](README101.md)
