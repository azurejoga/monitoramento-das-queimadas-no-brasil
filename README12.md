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
| 8e2df5eb-75f3-3c7f-a7fc-43eb5e4041c7 | -6.46664 | -45.35281 | 2025-07-15 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22f46744-c86b-3665-8597-5c857768916e | -10.57358 | -49.14009 | 2025-07-15 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c685e81f-646a-379a-8715-c3109342263a | -6.90943 | -52.85894 | 2025-07-15 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac635659-9d95-33c5-ba2a-ac337d14607c | -9.00042 | -47.93479 | 2025-07-15 04:10:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93746117-196a-30c4-99d9-58aeb4034f8d | -7.20298 | -43.10534 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 76c02cf5-d23b-3383-ac10-2438c1fa02ac | -10.87871 | -54.05982 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a703ccb-3d7c-30f5-82a9-f905e2ad853b | -6.91025 | -52.85443 | 2025-07-15 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c797e07b-e821-35b4-8c29-fc9c2a9ce6c3 | -7.29841 | -46.25946 | 2025-07-15 04:10:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e8b6c17-95b7-333c-998f-9a118b936545 | -7.19564 | -43.10786 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d9db9694-4d9f-31f0-af6c-5e797dc82d70 | -12.68109 | -47.87141 | 2025-07-15 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a960f3e0-047d-3f97-ab7d-f49c7ba744b5 | -7.19283 | -43.1037 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 28aa75bb-7cd6-3a4d-acff-24e9608d9962 | -7.17022 | -42.98543 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5834eb21-6334-39f6-a7bb-f611946411c6 | -10.49973 | -53.57516 | 2025-07-15 04:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 544cf876-2a21-31a7-9694-92040368e3a0 | -11.46317 | -45.09662 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| faa2832e-23d6-38d3-8fdc-8d47069f696b | -6.37909 | -44.74999 | 2025-07-15 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4510b990-eb56-36db-b8ed-4aa4240c0bf7 | -12.47477 | -44.50002 | 2025-07-15 04:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35f97692-d908-39fc-89c4-a3ce12af7cc4 | -6.37181 | -44.74878 | 2025-07-15 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8bdc4f4-c341-3a9e-914a-12a6426cb5d9 | -10.87722 | -54.06038 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc2322d1-f1a4-30a2-a6ca-16b34513a8da | -9.43784 | -48.4045 | 2025-07-15 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d72089a-7cbd-39fb-bcc2-daed10ceb710 | -13.03666 | -47.8256 | 2025-07-15 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ada83c4-7f20-3a1f-a513-1e56f87035ae | -9.28426 | -44.84077 | 2025-07-15 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 806aa57a-24c1-316e-8bbe-e99a602d48a0 | -6.72053 | -44.33311 | 2025-07-15 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60c98de9-796c-3939-b3c4-33e51457208b | -11.46099 | -45.08821 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| a266665a-4cad-32da-8316-5242ff1b71c6 | -11.94112 | -45.76326 | 2025-07-15 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfa672b3-bef3-3aeb-ac99-62ba519e3040 | -7.15309 | -43.15668 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9fab2686-ba7a-37c4-94c7-0996cd42e890 | -7.19621 | -43.10425 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a4156f8f-6da8-396b-803c-4c2f94f4698c | -10.78744 | -49.25633 | 2025-07-15 04:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3516518a-daa0-33e8-aa33-ab9e992046c2 | -8.59298 | -47.43502 | 2025-07-15 04:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b8e1d75-5d6b-3875-95b7-9476c51954e5 | -7.01037 | -44.39066 | 2025-07-15 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 315405f1-62bf-366e-bc38-4080e7f607be | -11.46731 | -48.5239 | 2025-07-15 04:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 689dd860-ce68-31f5-ad40-76120eeeff86 | -12.07816 | -43.47605 | 2025-07-15 04:10:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ed8c65bb-d35d-3962-bab3-d67c84a9e9e9 | -7.63777 | -44.42317 | 2025-07-15 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96fded5f-10c1-30c6-8a0a-724abcf06bea | -6.71054 | -44.32736 | 2025-07-15 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21266df0-aef3-33da-bfe1-153eb2a8e1b6 | -6.6349 | -44.57546 | 2025-07-15 04:10:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6cb6fd4d-8a58-3062-a72f-2265bbb190a8 | -11.46601 | -45.10117 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8787315-9ca8-32fb-bcc4-7094ea076ae6 | -11.85476 | -46.75415 | 2025-07-15 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbf15f87-3203-3f7e-8e50-cc0b357eb4ed | -8.29062 | -44.97758 | 2025-07-15 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04b4f9f1-c603-3eb2-881d-6769204d6744 | -11.45026 | -45.13081 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e4e56a5f-0dc3-326a-b847-9f5796cd8dab | -7.30743 | -45.36776 | 2025-07-15 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f6a7fe4-6cd7-331a-bb8b-b865c311f26c | -13.04739 | -47.81123 | 2025-07-15 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe6c7da4-f036-3c7a-9f0a-ab364afe414a | -12.06522 | -47.98546 | 2025-07-15 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2d1ccee0-25b3-3952-829a-88fccd21a650 | -12.70679 | -46.79822 | 2025-07-15 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50380dfa-6097-31b1-8f1f-88d268d1e1b1 | -12.82017 | -41.95681 | 2025-07-15 04:10:00 | NPP-375D | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8ac72151-10f5-3953-84d6-c7fea31a60f9 | -6.38033 | -43.71975 | 2025-07-15 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c76e9ba2-b8cd-3909-b64b-aa152f6560d5 | -13.13227 | -47.26648 | 2025-07-15 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2ef80ad-d9c4-3fcf-89b3-f51b6851715d | -8.22698 | -44.91607 | 2025-07-15 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fb8bd36-cd3d-3145-a993-8dff5a4e9e3b | -8.60886 | -47.4418 | 2025-07-15 04:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b2a0884-e209-3437-85dc-4b342400c853 | -6.88532 | -47.02774 | 2025-07-15 04:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70ea5b5f-b5e1-32c8-88cd-0cbaec6bbbc5 | -13.09857 | -47.28847 | 2025-07-15 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ddea3be-9df0-34bd-874c-313cf40d6cb9 | -11.47049 | -47.30807 | 2025-07-15 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67506ba7-4e93-3717-81b2-f947a8322af7 | -7.08396 | -43.6949 | 2025-07-15 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00125f17-bded-320c-8c8f-a0f79c9d364a | -11.45619 | -45.09539 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| b1208e23-96cd-3909-ab73-45623507dca5 | -6.91557 | -52.85984 | 2025-07-15 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0025dd4f-bb10-3b9d-bdae-8c55223fb727 | -7.1657 | -42.99208 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aa6c9f6d-0790-357d-99da-2e65b2424630 | -13.03357 | -47.82869 | 2025-07-15 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8d204ac-9af5-3b1a-9dc9-79a59d9f7ec6 | -10.37781 | -47.5596 | 2025-07-15 04:10:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9f2eb2b-9a0c-3fbc-b65f-40f62c241fd0 | -8.75383 | -43.95579 | 2025-07-15 04:10:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fe9b90ce-efcf-3ca6-b126-5d59ab2e7492 | -7.8891 | -44.4945 | 2025-07-15 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a1199a5-f811-36f2-92d6-8db256de2a20 | -14.04122 | -43.81189 | 2025-07-15 04:10:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e50ebad4-e43c-3f54-8d71-5a97a53b70bc | -13.04343 | -47.81056 | 2025-07-15 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ee64ef6-348a-3b3e-a6b1-8c6583d722e7 | -9.16976 | -43.13703 | 2025-07-15 04:10:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5168896f-2243-3617-a248-7e3bc1e0d475 | -6.47493 | -45.37279 | 2025-07-15 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7c6f710-0fcf-3c77-8945-a5e395a853d6 | -6.13181 | -45.85229 | 2025-07-15 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e705e58-67f6-3831-8438-189177656206 | -11.44742 | -45.12626 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 0afb6a55-30bb-3e50-be4c-8acdb527cba4 | -7.26263 | -45.30775 | 2025-07-15 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8697a8e0-0124-30db-bdfb-d47949f18ed8 | -10.55504 | -54.25498 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10cbd3d3-315f-3669-9ecf-3b2c671173ad | -7.20186 | -45.32951 | 2025-07-15 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5cd23ebc-7abc-36b2-b332-a756594cb61c | -8.23569 | -44.93013 | 2025-07-15 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eff0268c-219c-3b1b-8404-09291df77a2f | -6.3838 | -43.7203 | 2025-07-15 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c2fa606-c54e-3e64-b5a6-ed3291bc2621 | -9.51804 | -45.43927 | 2025-07-15 04:10:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6cf5c96b-2746-31bb-bdd4-f077d67880f0 | -10.86496 | -54.05785 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe085fa8-94e3-3610-86e2-1660da32ef4b | -11.52537 | -48.95902 | 2025-07-15 04:10:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a95d100-a46e-34d0-96d4-7f9806ac90aa | -9.9781 | -48.0799 | 2025-07-15 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7c6de000-2b93-3681-a496-3c8fd08613e8 | -6.44141 | -43.81121 | 2025-07-15 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3177a260-8438-3423-9b0e-400edd03609d | -6.52913 | -43.36183 | 2025-07-15 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba0ad694-904c-30e9-8216-40f85ec35a54 | -7.81241 | -46.56433 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e726ed3c-e48f-37eb-86cc-162751780c51 | -11.44392 | -45.12566 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 2fb600dc-0e85-3dab-bcad-e4e64a04bfab | -9.80732 | -47.74845 | 2025-07-15 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d32835fb-4daa-3873-b679-60a4927401eb | -7.19547 | -43.00056 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1eefc073-aa9c-3cfd-b2bd-fe34102cf15b | -7.30446 | -45.36269 | 2025-07-15 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f157e9d-71ec-3506-858c-b1360680cba1 | -7.08741 | -43.69546 | 2025-07-15 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f5c7bb28-6053-3552-92b4-a17d51269e6e | -7.09454 | -44.38818 | 2025-07-15 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c004f93-5340-3a9d-9532-8e199dfe71c6 | -10.87963 | -54.0551 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7001a8e6-bbe5-33fd-bc03-def23cd8a160 | -11.90457 | -46.7585 | 2025-07-15 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1d5bbbe-be0e-38a4-a2d6-bcca187c7db4 | -8.57008 | -45.54407 | 2025-07-15 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e8cf6b0-b54a-3296-b0f4-01aa1017172b | -6.73052 | -44.33885 | 2025-07-15 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf250d4e-40d9-3d7f-ad5a-200ef80488ef | -10.54779 | -54.25879 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 79bcfd27-4432-38c9-9b9b-b980911e8c93 | -6.88752 | -47.02868 | 2025-07-15 04:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e11eeac6-b602-3574-bafb-c94f675ec1c1 | -9.9774 | -48.08385 | 2025-07-15 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3a87edcb-8cf5-3e72-ab87-fe6a6da27916 | -7.28682 | -43.04072 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ec060674-208b-3489-9704-a605cacbf9c5 | -7.64194 | -44.41982 | 2025-07-15 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cace7301-0b67-3484-a8df-d6f20cf53add | -7.09164 | -44.38359 | 2025-07-15 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3263d293-98bf-3020-a493-0a3757b91d0b | -11.4461 | -45.13415 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 08dccdc3-76d7-3cf1-a666-251231f0b9ad | -12.09964 | -44.74232 | 2025-07-15 04:10:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68261593-c0b1-327a-93db-7b613646fdf3 | -10.56829 | -49.14378 | 2025-07-15 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| eb1bc9b1-e131-35f7-b744-99e52a98e350 | -7.19902 | -43.10841 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0ff8e6f0-8ca9-305f-bbe5-ec4596c839ab | -11.46252 | -45.10052 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 2e896a53-fb11-3001-9f16-ab34bc172eed | -7.16685 | -42.98489 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0919ba9f-3623-37d0-8de9-a6d99d12a31a | -7.09734 | -49.17441 | 2025-07-15 04:10:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bff72b56-238f-3833-a3e1-45b50300ec9f | -10.87817 | -54.05567 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README13.md)
