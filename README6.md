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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ce43f0b-31ec-3eb0-80c5-fca8de013f1c | -20.34789 | -40.35883 | 2025-06-05 03:45:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 60bad8ba-63d9-344c-bfe1-ccb253e6a881 | -14.16069 | -45.48592 | 2025-06-05 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fac4268-5b1b-3020-ba9a-bd8f0cce0231 | -22.6757 | -42.85241 | 2025-06-05 03:47:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d4ce4a3c-2aaf-350f-8c0f-751fdd4ca47e | -21.80028 | -52.75918 | 2025-06-05 03:47:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 147574e3-af48-3abe-8a29-ac2383f6c55a | -22.53747 | -48.81194 | 2025-06-05 03:47:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fac7b4d-2e83-35ca-8e33-410859867e00 | -21.79858 | -52.76594 | 2025-06-05 03:47:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 510a858c-349f-33f8-86a3-adcf03c0a475 | -22.67485 | -42.85712 | 2025-06-05 03:47:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 228befb7-6ced-3b2b-a2eb-a8779d57e1e2 | -21.79633 | -52.76506 | 2025-06-05 03:47:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 889e4a46-572f-3ebe-8881-f079d5773c8c | -13.5152 | -56.569 | 2025-06-05 03:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 8a4a3697-6f16-3025-9969-c48969cfb3fc | -13.5344 | -56.5672 | 2025-06-05 03:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| d86cf6c9-42ea-311e-97a3-5b20d0bda4e0 | -13.515 | -56.5893 | 2025-06-05 03:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| f8e1e60a-ee03-331f-a0a6-7225cde7ee1b | -13.5155 | -56.5488 | 2025-06-05 03:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| bf43655b-81c1-38be-acc8-d1982d035c06 | -13.5346 | -56.5469 | 2025-06-05 03:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 42.4 |
| bc021824-4a72-3d7c-9405-d78c8f3f4698 | -13.5344 | -56.5672 | 2025-06-05 04:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 989672e3-876d-3e50-9e86-810058a0135c | -13.515 | -56.5893 | 2025-06-05 04:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| d6bbaca2-15d4-3f0d-8a13-8e20426506aa | -13.5152 | -56.569 | 2025-06-05 04:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 154a4a58-ef05-338b-8460-dc3a18625850 | -13.5155 | -56.5488 | 2025-06-05 04:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 0bbd55fd-1bf6-34f4-a048-9d5c63e6b6a4 | -13.5344 | -56.5672 | 2025-06-05 04:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| af0d8d7d-4c33-33cd-ad2f-2e3e9a4f3a65 | -13.5155 | -56.5488 | 2025-06-05 04:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| a0df1db5-84b9-3258-9946-2542fbe9ad45 | -13.5346 | -56.5469 | 2025-06-05 04:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 39.1 |
| b7faedae-94d1-32cc-9cc5-48e4fcfaa446 | -13.515 | -56.5893 | 2025-06-05 04:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 10ae380d-cb12-3e26-a807-cc190437462b | -13.5152 | -56.569 | 2025-06-05 04:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 32cccf6d-d744-3ae4-8e1b-06aa2b837b36 | -13.515 | -56.5893 | 2025-06-05 04:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 116233c5-c0de-3a03-87ae-736a25b71853 | -13.5152 | -56.569 | 2025-06-05 04:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 173.0 |
| e3d210fa-f581-3036-a3a1-2fba04b74962 | -13.5344 | -56.5672 | 2025-06-05 04:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 37d6ef4e-6f58-32ba-97dc-90afada3fb3b | -13.5155 | -56.5488 | 2025-06-05 04:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 769224e6-ba49-35b6-b86c-eda12d02d16c | -13.4961 | -56.5709 | 2025-06-05 04:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| e71f841c-946c-3e45-aad1-b1a0d9251d56 | -13.5346 | -56.5469 | 2025-06-05 04:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| bdb99019-6e09-3a4b-a422-03aba720ceaf | -18.8479 | -53.6251 | 2025-06-05 04:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 575a917e-b9cd-3c77-8061-89ae01bc36e5 | -6.63165 | -47.34065 | 2025-06-05 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cdd877f2-915e-345a-8500-cd83fcec3870 | -6.2038 | -48.55392 | 2025-06-05 04:32:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea81fc0a-9e6a-33d9-9c13-66ca38de7eaf | -6.2209 | -48.55301 | 2025-06-05 04:32:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e95336e-2a57-3f96-bb5e-958dcde3abcc | -6.9836 | -47.088 | 2025-06-05 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 919aad66-44fd-36bb-bba9-e156dde6012b | -4.82322 | -44.35694 | 2025-06-05 04:32:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2134881-4bc5-3905-870d-af1689ef2806 | -7.69773 | -45.78162 | 2025-06-05 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 60f6156d-b00b-3aa7-8250-8dc15c7e5bd0 | -4.81086 | -45.26274 | 2025-06-05 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6a8d1f5f-dc83-37ec-9402-cbd0c04eeedf | -7.21564 | -43.13188 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 66cf077e-7cb4-3c44-9664-ea5e13134245 | -7.20063 | -43.13737 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d4319b1a-3768-3f3b-8fac-551463d5fa9f | -7.19864 | -43.13638 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f9a6782d-957d-3baf-8c64-8acf1ab7e6f4 | -7.87719 | -45.98786 | 2025-06-05 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c95b7f57-fce0-3fd0-8694-e080bb125c35 | -7.01755 | -44.58252 | 2025-06-05 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 157e3590-d6bb-384e-a1a9-e4f4f5babe10 | -4.41277 | -42.13988 | 2025-06-05 04:32:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f9bcee70-b96a-3c1e-86e7-c080ff424f75 | -6.90984 | -47.76028 | 2025-06-05 04:32:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fcf3402-e4f1-3b8a-ab47-f9c1a6fedbd1 | -5.99409 | -47.89455 | 2025-06-05 04:32:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0aa64e14-ffce-3110-bcf4-4d2d92357052 | -7.54067 | -45.82965 | 2025-06-05 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f7c22ac7-e8d0-3f20-8a1d-abca71e1a310 | -7.015 | -44.59991 | 2025-06-05 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16871eb3-c7d4-35b7-b8c2-cc243dba9e63 | -5.19708 | -43.05943 | 2025-06-05 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6dada80d-4ed4-3042-87bc-056afd87899f | -6.81521 | -44.90557 | 2025-06-05 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b614453-a295-3891-96ef-e3f901864f0a | -6.20338 | -43.34113 | 2025-06-05 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2b01c388-c37b-36a8-99f2-b8de3ee47657 | -7.02169 | -44.60522 | 2025-06-05 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c32b637d-a445-3c2d-a56a-5e11bc90dc88 | -5.81865 | -46.48462 | 2025-06-05 04:32:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cc791b5-241a-3a0f-8d6d-b3c7fef79642 | -6.64073 | -43.19848 | 2025-06-05 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5da66bcc-1a44-3bcd-951b-efc22718f094 | -6.20727 | -43.34176 | 2025-06-05 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3e9511a5-b153-373a-b17c-93258881a3ae | -7.02105 | -44.60955 | 2025-06-05 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8f88f61-75fa-3c6c-b83d-9974870edba5 | -4.58687 | -47.86167 | 2025-06-05 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dee223f-c98c-366d-b2c9-e4ca3a501adc | -7.21114 | -43.13476 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a80902d2-c085-3ada-a979-a4192d88d0de | -4.5554 | -48.01906 | 2025-06-05 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8197fe7d-1c9c-33e1-b332-d6e78fa7cc41 | -6.47183 | -48.01947 | 2025-06-05 04:32:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b13eebe-4cb8-3edc-8322-f4457b334b3a | -6.63665 | -47.35209 | 2025-06-05 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ff84b28-ef79-3fd7-a0e0-e49024aaf2b9 | -5.19028 | -43.31784 | 2025-06-05 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 143e2040-bb47-3431-9972-56b7b082f982 | -7.67899 | -46.09523 | 2025-06-05 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85402027-a53a-35b4-a0bc-d99aa07e1279 | -5.92406 | -45.52684 | 2025-06-05 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8feac57c-9cb5-325c-851a-a1e821513055 | -7.55394 | -45.83567 | 2025-06-05 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 35c5491e-d8f8-38b1-9f84-35d31ebdecbc | -4.5561 | -50.3003 | 2025-06-05 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b2d6a08-21d6-39ac-985f-3aac8eee32a1 | -7.18255 | -43.149 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 391d910a-b1fc-3065-9f7a-ded5a2459384 | -6.96839 | -42.90806 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 38e8f1fa-0dd6-3666-8e73-950a15a96279 | -7.19815 | -43.13986 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 2c442461-30f1-39a1-85fd-92256f968388 | -7.62216 | -45.75044 | 2025-06-05 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 39057860-3cdb-3833-b836-9cd7696601e4 | -7.21515 | -43.13538 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e0267135-504d-3d41-a131-287fb3b681d7 | -7.59941 | -46.43729 | 2025-06-05 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ba5e7ac-a6b6-360e-83a3-e76e7501c642 | -6.8188 | -44.90611 | 2025-06-05 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 336006d2-330b-3054-a8d8-863db3563752 | -6.29508 | -47.00974 | 2025-06-05 04:32:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 104f9e09-46d1-3cfb-9226-ef2141bf3128 | -6.22035 | -48.55649 | 2025-06-05 04:32:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7538d042-1fc2-3c8c-a956-67e443558fd4 | -6.46691 | -48.0293 | 2025-06-05 04:32:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d61a867f-a170-3049-b26e-6ffd72805d51 | -7.54126 | -45.82577 | 2025-06-05 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cfcc9975-da17-334e-84a4-8a61678a828f | -7.20115 | -43.1339 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 63c62ae6-3485-3b65-a93a-d34b2c3e2339 | -2.53488 | -53.95857 | 2025-06-05 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 301826ff-07cc-39e4-8afe-e08de1b0d9d8 | -7.01563 | -44.59558 | 2025-06-05 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4be0f24b-2ec9-313d-98ae-9f63997474a3 | -3.94442 | -41.51358 | 2025-06-05 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0ca5ff32-103f-306b-9e21-a2847f480c2e | -7.6152 | -45.74934 | 2025-06-05 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b5bd49e-ab5f-3753-af62-57f008cd1cd3 | -6.95976 | -42.91045 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| ac39b2fa-77bb-31b0-8e57-a38887bcb137 | -5.4127 | -49.08072 | 2025-06-05 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc1c9119-dbd6-350f-b98d-87e8e289e4f0 | -4.4204 | -47.66324 | 2025-06-05 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a1d6c8b-8e45-3b7a-bd82-47cc62f2e9cb | -5.73817 | -46.07804 | 2025-06-05 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f8cd553-540d-3a93-a256-b3cb66f19688 | -7.66657 | -47.29086 | 2025-06-05 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 426c4d6a-54ba-345b-aea3-9dcaad6ea6f3 | -8.11395 | -45.36653 | 2025-06-05 04:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc16d729-0a40-346f-96a0-e9e2d0c2fbf7 | -7.87373 | -45.98732 | 2025-06-05 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01a35b81-3212-3fa2-83ac-35890a8b4117 | -7.20314 | -43.13351 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9ffb02cf-47dc-36d5-abab-8c7c8441d702 | -7.20012 | -43.14085 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 7b1f3e40-c36c-3b4b-965b-444278e9fb9d | -4.79667 | -47.21603 | 2025-06-05 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c0f452e-94e0-3232-aa7d-aa1fba6b2004 | -5.19413 | -43.31843 | 2025-06-05 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a02f3f17-2c58-39e5-9720-56266fc3c70d | -7.01627 | -44.59121 | 2025-06-05 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3ce686c8-5b01-301f-9e95-17ce1b9d3301 | -7.62158 | -45.7543 | 2025-06-05 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ba344df-01fb-30d8-9fce-9a0337afe686 | -6.20799 | -43.33684 | 2025-06-05 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 819c1d59-39ae-3f8d-8e86-28f1a5dbcb4e | -7.6181 | -45.75375 | 2025-06-05 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 978ebe7d-b00d-346d-907e-130679fbfce8 | -6.96891 | -42.90446 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b76adbdb-0842-3b58-a3f7-bba4ed22ab19 | -6.20766 | -48.55097 | 2025-06-05 04:32:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95d80b87-7959-3b70-8471-f4aa01df051a | -6.63719 | -47.34862 | 2025-06-05 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a511104b-cded-37ef-b117-7987d9e04e2e | -7.01008 | -44.60792 | 2025-06-05 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8ffbd1fb-36af-36d3-9eb3-02ac1115324b | -6.20932 | -48.56194 | 2025-06-05 04:32:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README7.md)
