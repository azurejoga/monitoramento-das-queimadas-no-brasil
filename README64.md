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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28bfba74-9301-3a03-a5c9-062a1d951235 | -8.22741 | -46.92731 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3875c839-63e9-38e1-9062-61c567a56db7 | -8.02835 | -46.75127 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ab515710-dd6d-3910-b803-029f3ae33aeb | -10.83338 | -56.95654 | 2025-10-27 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5ee478ca-929a-3be7-9121-43aad5d4b9e6 | -9.63542 | -46.86449 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cc44af2-1247-3299-ae87-ef73d73c7ad2 | -7.83343 | -46.47214 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| af13cb69-a6eb-376f-9043-c8337be0b077 | -8.82407 | -49.9887 | 2025-10-27 05:01:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfa098e7-43b5-35e7-8069-1fc30af74a1a | -5.71775 | -49.31644 | 2025-10-27 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f2b1c41-6e2f-30ab-8283-34e74ce293f6 | -8.6509 | -44.77375 | 2025-10-27 05:01:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bf382b2-3a8a-32d8-9e79-cef98b13f917 | -11.70908 | -44.4414 | 2025-10-27 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c2b8fc2a-5ceb-3d91-bc29-3ab59acbeaea | -7.68332 | -46.33826 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25f07883-bfb3-370e-b334-94e7bc8ff35b | -8.36249 | -46.16057 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f7b2721b-9dbe-3fe3-9f6e-d50d0c1eaade | -10.20981 | -52.66145 | 2025-10-27 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6375ea78-0d9d-317c-b9a8-5c54abc113ae | -10.55125 | -48.01029 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e9581ebe-d12b-3c84-b15c-a256129a906c | -6.89245 | -45.1534 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fc4cc88-a6cb-3aa4-ba20-640ddf811e0c | -7.8365 | -46.45005 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7641fb74-faf4-342d-91e1-03fc47b579d2 | -8.12414 | -47.03114 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4e5d0394-3a56-3ce4-a6b0-dce03667bd43 | -5.77636 | -51.85738 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d882519-11f2-3ebd-a7e0-722a406408c5 | -8.09672 | -47.05808 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e614acd6-4c5e-339c-83b4-98fe56c06275 | -11.13582 | -54.37084 | 2025-10-27 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4248e711-c034-3fdc-84ea-d8cf92834093 | -8.53422 | -47.19686 | 2025-10-27 05:01:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 595c879f-3378-3eb7-a23a-e59af4c2b68b | -9.06113 | -45.10594 | 2025-10-27 05:01:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08ffd6c9-0098-3a9c-8f92-85fe3950a4fb | -6.57407 | -48.76832 | 2025-10-27 05:01:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 891318f5-2a8c-3a19-9fd6-25c8e35212ae | -10.36045 | -47.17729 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 640de11c-8135-3824-b68e-850819c08d6f | -10.60246 | -46.62164 | 2025-10-27 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24488b3b-75c7-3087-a4cc-7fde67032b5c | -8.052 | -46.95465 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c6cc4bb-bab0-3491-81d6-897260fe7054 | -11.03427 | -54.26339 | 2025-10-27 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a725ac8f-5f80-3240-94bd-8e1e25fad652 | -10.98209 | -47.8469 | 2025-10-27 05:01:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d659cdd3-b685-3440-b31e-c76bbb607fba | -9.57502 | -46.89571 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7e96d830-171e-398c-927b-e6f47e25f154 | -8.96331 | -47.19161 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e16adcee-d09e-3491-ad28-ba0f0bddafba | -11.046 | -49.89512 | 2025-10-27 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54d7f3d2-4904-30a4-8f4a-63e35c85b1a8 | -8.30965 | -46.19081 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 160a1547-0a4a-36eb-9799-2fe1f0597b9a | -8.31676 | -46.17709 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ab3df531-9660-37e4-bae1-4fd363384c5e | -10.31581 | -47.2102 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95e635af-4f60-3980-846f-3f0fec0a07c5 | -8.32329 | -46.82556 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82b068e5-90d0-300c-8846-3a3c409010da | -5.61423 | -51.79006 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd8dc638-48c6-3333-805e-bfdca6317a6d | -7.78734 | -45.37803 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e84d308a-7de5-3973-bfcc-511292750eb3 | -4.87363 | -50.85583 | 2025-10-27 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cea8d620-e674-33cc-89c2-5faade302444 | -7.38064 | -46.5453 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0314bcf1-de53-3ff6-97a1-590cf3e99a87 | -12.51029 | -44.33138 | 2025-10-27 05:01:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e265d5e2-09a5-3e9f-a5df-3109a682ec2c | -10.8275 | -47.62104 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 938cbac0-0d90-30b7-92f3-79e44bee8a3f | -5.77288 | -51.85685 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbde79d5-1f60-3b75-adc8-74a80a59dc0a | -13.08045 | -44.54469 | 2025-10-27 05:01:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2aff54f-a324-3794-8dee-e7abcdf79cfc | -8.69626 | -50.81409 | 2025-10-27 05:01:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 618efa11-9751-3d05-9276-9a5b34d1aa6f | -10.21392 | -52.65803 | 2025-10-27 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddbea445-72fa-3909-acf2-98ef05bdb0eb | -9.57357 | -46.90652 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b96edf6f-641c-3af5-a141-bf2194d0ff38 | -5.71132 | -49.30498 | 2025-10-27 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f999f381-0ade-3c72-ae32-d9b988979113 | -4.87724 | -50.85633 | 2025-10-27 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bc180b2-1fe3-39a5-8027-0578135498b1 | -6.63506 | -44.62841 | 2025-10-27 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cb01a5b-067d-3986-a939-0bfa83d645d3 | -11.42364 | -46.11507 | 2025-10-27 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ede9210-e79f-3c90-be58-56f1ea042b21 | -10.60773 | -46.6214 | 2025-10-27 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1fe8ed8-f245-3d08-85d8-910478865be7 | -11.04706 | -49.89814 | 2025-10-27 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6751e5c2-acfe-3440-959c-6e6829153548 | -10.21041 | -52.65748 | 2025-10-27 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a856f7f-15bd-3992-a382-289246757502 | -6.88818 | -43.56982 | 2025-10-27 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9acc7050-f4cb-3373-a8eb-f40b56fa9d34 | -7.22258 | -46.87352 | 2025-10-27 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c576637-ad2a-30e7-a778-62e84b5b958d | -9.56147 | -46.80626 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea8eb0f2-87c8-3c65-a255-96dca24ef080 | -11.41912 | -46.10763 | 2025-10-27 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d599ba08-2a0c-38ce-862e-a5685db20233 | -10.82797 | -47.6235 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9b47a919-b7b9-3493-aad1-2d313c384fe9 | -6.63455 | -44.6322 | 2025-10-27 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 482d9510-6c4d-3679-90c5-107f5af02328 | -8.96257 | -47.19686 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 31215ba8-ce51-3101-a3d4-bf88f6f5d1e4 | -7.83921 | -46.46719 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7f568eb2-d1f7-3fd3-a93d-b561d6718abb | -9.13207 | -51.298 | 2025-10-27 05:01:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c90b971a-fa74-303d-9692-ec8de83982c4 | -10.04506 | -48.16723 | 2025-10-27 05:01:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f50cc0ee-abae-37e6-ac0d-7632d525553c | -6.10241 | -41.77507 | 2025-10-27 05:01:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8d0a144f-2007-351e-9279-8cdae56ed0f1 | -7.93505 | -55.01788 | 2025-10-27 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 78105d01-85bf-324f-b8c7-b6a9024643f2 | -7.39645 | -45.12449 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccf922f0-b6b8-3fcb-8062-97ad31428f90 | -10.75672 | -44.20162 | 2025-10-27 05:01:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 439816d2-6f17-34a1-bc4b-14c73382eef2 | -6.89792 | -46.13772 | 2025-10-27 05:01:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd2425e2-aaef-3e08-9faa-7433cbb49fc5 | -10.2346 | -52.15879 | 2025-10-27 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 234c31af-fa53-31e5-a094-582d1678881d | -7.83265 | -46.47775 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ac86efc6-d9e2-310c-a276-d8183cbdbf1c | -7.83069 | -46.4552 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 83451719-5c6b-30ce-9c87-4f8f92fbab69 | -11.60998 | -50.98458 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3de9a388-ce5b-3965-9ce9-611694b90c67 | -8.8865 | -47.9957 | 2025-10-27 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2086e7e2-ac5b-35db-8ca0-56778aebe814 | -12.05189 | -46.60765 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52f238c0-eeab-3fdd-8f63-41ae791dda1c | -6.14264 | -41.826 | 2025-10-27 05:01:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 0963dc4e-165f-3e04-96b9-3b8921972029 | -11.90629 | -43.82661 | 2025-10-27 05:01:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c4a86117-e201-3427-89bd-3809b845982e | -7.67898 | -46.34128 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0efd1f6f-64e0-308f-93e3-b9234204591d | -6.90216 | -46.14414 | 2025-10-27 05:01:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c26046b9-6092-3f57-bb48-53606cd348bc | -5.71055 | -49.31012 | 2025-10-27 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38a8c6ac-07ff-3ba8-8c56-fe2bcc6d58a1 | -7.82966 | -46.42574 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40dd021f-4c9b-3b7b-9f70-a00f8ca1119e | -11.60538 | -50.98895 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0279981-12ca-3893-a4cb-0a225b6e71dd | -6.88122 | -45.15511 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89f51e9c-9108-3053-b971-cbd462d7e57e | -6.31211 | -44.74183 | 2025-10-27 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 57d87fca-f07e-3833-8f4c-792a225ed31b | -7.86815 | -45.71717 | 2025-10-27 05:01:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97c8bc76-c678-3475-830c-03b808377a40 | -10.92384 | -48.0298 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2037599c-e97f-3995-b72c-a69fb6f30ab5 | -7.86 | -45.38229 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3521ae74-af9e-33a6-81fd-d418dc4b944d | -7.2508 | -44.96038 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49c2d5de-8707-347f-b0e3-9d2528cf0532 | -10.56987 | -48.01333 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| be26718d-bd91-3416-a29b-46292eaf4620 | -7.67977 | -46.3357 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d07d551-5166-35ba-bb67-15915e436600 | -13.0413 | -45.86855 | 2025-10-27 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a7fd5dca-fed8-396a-a3d3-706a404895de | -5.71919 | -49.27973 | 2025-10-27 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 05b7dc61-60d6-3cda-8b88-16b0f2b5f5ec | -6.37124 | -44.2662 | 2025-10-27 05:01:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 34ca3ff7-b1af-3dcb-a34b-fbef30ff7fb5 | -10.20631 | -52.66088 | 2025-10-27 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ebbeb70-efad-362e-8cd5-ccbbef357cb0 | -10.96187 | -58.9758 | 2025-10-27 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5f4aeef-bae5-308e-bc57-f18c248e736c | -9.58275 | -44.94745 | 2025-10-27 05:01:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6d4f7452-8eb8-3445-b928-f842ea8428db | -10.87707 | -54.04327 | 2025-10-27 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f52057ba-d95f-314a-a04d-4aade891cac9 | -13.42848 | -47.39064 | 2025-10-27 05:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5114353d-04fc-3eb0-af7c-ce135a695202 | -17.41301 | -46.88816 | 2025-10-27 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e19ed7f4-e863-3402-b9da-6636043bbc97 | -14.37261 | -51.5332 | 2025-10-27 05:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87d70c3d-7342-3182-b0d8-cf3b39d0cc3c | -14.25449 | -48.13022 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab0253ab-b430-3c27-92b1-8961ecc8f2e1 | -13.23946 | -47.99929 | 2025-10-27 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |


[Clique aqui para ver as próximas entradas](README65.md)
