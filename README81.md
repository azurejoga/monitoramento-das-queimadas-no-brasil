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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94d06666-845b-3662-b770-4f8a3890b870 | -6.8411 | -58.9939 | 2026-09-16 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e4034af6-7adb-3d88-9314-9aa98508c1b6 | -6.1292 | -57.7223 | 2026-09-16 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| e238d6a2-95ab-38ca-a678-96c2a8c201bb | -8.5431 | -44.4902 | 2026-09-16 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 235.6 |
| 0970fa1c-ac76-3eb7-9511-83b865ef608a | -10.7015 | -54.1663 | 2026-09-16 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| c84a0e9b-0401-3d88-b059-556747d19d0a | -6.3013 | -59.9771 | 2026-09-16 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 4aa6c5b4-49f8-3b15-a0a5-ac360c899ee6 | -9.0866 | -61.0287 | 2026-09-16 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| d160fcf4-7931-3596-b2da-eb49ee76fad6 | -9.0962 | -65.9384 | 2026-09-16 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 903f861c-343a-3c33-8152-cf0f7c5caf49 | -8.6184 | -44.5049 | 2026-09-16 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 205.4 |
| b32b1204-9007-3eb1-869f-a9415d8b2a70 | -6.7684 | -58.8035 | 2026-09-16 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 6dd68150-4908-31db-a33e-da2977ecc7b4 | -10.7729 | -46.2096 | 2026-09-16 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 881b0d1c-3d6f-3a6a-afe5-172a33b3d87c | -7.0058 | -59.2382 | 2026-09-16 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| b4a5aedc-76b4-3348-a9e1-f19a4de5b299 | -3.1697 | -58.6437 | 2026-09-16 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 97b09add-4fb8-3efc-9f85-a79ae837d1f3 | -10.9595 | -50.2529 | 2026-09-16 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| f0919be8-ecbb-3cba-b87b-53c5b67a0aff | 4.1516 | -60.6878 | 2026-09-16 15:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 4a3a1070-483e-3375-8d48-37653181bc67 | -13.3758 | -57.026 | 2026-09-16 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d28f75cd-a03d-3b54-879b-276422634ee7 | -15.6557 | -52.7366 | 2026-09-16 15:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| c4b7d050-ddbf-36fb-bdfd-3c9bb1963781 | -10.3772 | -49.9508 | 2026-09-16 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 36e47222-3cbd-3e8e-b920-b379688c1984 | -6.9872 | -59.2582 | 2026-09-16 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 03233007-577c-352f-9ed0-f22daf95d8a9 | -6.6767 | -58.7105 | 2026-09-16 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 579f55bc-a979-3d73-924c-3412906b8454 | -12.1072 | -44.2021 | 2026-09-16 15:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 7c791620-c400-3742-9513-a2e1510a9256 | -3.4279 | -57.9816 | 2026-09-16 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 27b9afdc-3d27-3e45-aa11-e0d89ec5d5e3 | -3.1514 | -58.644 | 2026-09-16 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| dfe48281-85c7-39fc-802e-85b60834eb4c | -9.3569 | -50.1583 | 2026-09-16 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 3f1ddd59-81b8-3685-bef0-160cff8f4d09 | -15.4817 | -53.7947 | 2026-09-16 15:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| b6ec62c4-e215-3593-8086-b668cf77cc7e | -10.6829 | -54.1475 | 2026-09-16 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 26d861e2-5a94-32a0-9344-99a6fd7bf5e9 | -6.75 | -58.8043 | 2026-09-16 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 176.6 |
| cf54050d-4ea0-39f5-9f88-225d99944c65 | -5.144 | -55.9345 | 2026-09-16 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 9f6183b6-6272-306f-82a5-1f6a97c515d0 | -11.1738 | -42.8095 | 2026-09-16 15:10:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 175.5 |
| c4c703a3-2eba-3097-a952-f80cea84d0a4 | -3.2752 | -54.2622 | 2026-09-16 15:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 43607c5e-ab56-36d1-bf12-2753fe3fc4b1 | -9.0124 | -61.0131 | 2026-09-16 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 125b45da-d4f7-3ce2-9ed2-2a9f50ae3a3a | -12.12 | -57.1967 | 2026-09-16 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 9d4acf44-e1ad-3b98-94c7-95fa2be81a8e | -3.1174 | -57.6779 | 2026-09-16 15:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| cced4718-84b6-339a-9f54-bc2e1bcbcacc | -6.8032 | -59.1693 | 2026-09-16 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 411.9 |
| 7f949afd-7f9d-343f-96f1-aabc57ae1cf7 | -11.0247 | -49.6656 | 2026-09-16 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 89d2689c-07a8-351f-a215-cf096547d4e2 | -11.2488 | -54.1378 | 2026-09-16 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f6f4714f-38ba-3fae-a7a6-4b132770eebf | -12.2131 | -52.8637 | 2026-09-16 15:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| bf32fcfc-2ba2-38e7-b4af-481b51f125c5 | -9.031 | -61.0122 | 2026-09-16 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| e86ed535-6c9c-3896-970b-eeea51d86cec | -15.3408 | -52.9704 | 2026-09-16 15:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 45.0 |
| d359970f-16c4-39d9-8c36-ef95aee9cad7 | -1.6022 | -55.5682 | 2026-09-16 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 4dfca105-1fb0-317c-96f7-cc1b84e9b4fd | -9.8099 | -45.8759 | 2026-09-16 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 284.5 |
| 355d0643-8c20-3832-acab-036eedc4a3d6 | -2.6783 | -57.5893 | 2026-09-16 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 7877054b-d9d6-3355-8e2a-703751902705 | -11.2113 | -54.1208 | 2026-09-16 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| b6ad6e68-e432-397b-9c7b-76afb56fdcbc | -15.3804 | -52.9227 | 2026-09-16 15:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 3a1eb79f-48aa-3ede-b1c0-d8e9778f1f85 | -8.5428 | -44.5132 | 2026-09-16 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 348.0 |
| 266463fd-00ce-3dab-a1b0-ac41a2cf1744 | -10.5535 | -57.4567 | 2026-09-16 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 5bf3ddd3-798d-313b-af58-d9c3771aa079 | -13.5652 | -51.8656 | 2026-09-16 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| fe06f768-2784-3807-996c-18c5b333d409 | -2.7149 | -57.608 | 2026-09-16 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 9c5c1b73-67ab-372f-bd99-f192c00a313e | -6.1609 | -52.7496 | 2026-09-16 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 8731619d-1af6-3f4e-8954-00de0d9c8d8e | -6.7463 | -59.4416 | 2026-09-16 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 40e45d6b-229e-3386-9796-35266dba6902 | -15.2669 | -53.8851 | 2026-09-16 15:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 9533b8d1-e577-3e65-8cb0-c7bf58cfd89c | -6.2731 | -55.2904 | 2026-09-16 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 54824381-5e94-312b-9800-28decad1f840 | -12.1265 | -44.199 | 2026-09-16 15:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 490.3 |
| 43d4f610-0cd4-3f4d-a1fd-f12d932ae7b4 | -10.8571 | -50.8183 | 2026-09-16 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| ed3617c2-229b-35f5-b8c3-b1d9e25e6100 | -11.3276 | -47.2386 | 2026-09-16 15:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 7221cf48-7145-3cff-a1e3-fc42dc2ff77e | -9.7136 | -64.9074 | 2026-09-16 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 6c8d1887-56b6-3ca3-afa1-a3340dab5cd7 | -6.641 | -58.4987 | 2026-09-16 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 95eb1c31-80fb-3435-a718-7a1065b0497f | -9.1337 | -65.844 | 2026-09-16 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 9381505b-99bc-3dd5-ae2a-ec242c52496d | -11.4718 | -50.2388 | 2026-09-16 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 73fa5c51-eefd-3f49-a6c3-45fa96b069b8 | -11.2115 | -54.1003 | 2026-09-16 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 7edaa643-86cd-316a-80fb-570a22bed360 | -12.6818 | -54.7379 | 2026-09-16 15:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 9a96262f-1b06-3c01-a0d9-e9c70bfb09e9 | -9.0059 | -65.4186 | 2026-09-16 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| aba4bf2e-9461-3a24-816c-e542fe816c7d | -14.58 | -46.58 | 2026-09-16 15:15:00 | MSG-03 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0d07bcd8-835b-339a-8447-4014924e5192 | -6.81 | -59.17 | 2026-09-16 15:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47d9eaf3-dff9-35f2-a062-d634da0264b2 | -14.55 | -46.57 | 2026-09-16 15:15:00 | MSG-03 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b75a3649-5a42-3a4e-98ab-9c84bad351dd | -6.84 | -59.18 | 2026-09-16 15:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a96b2a8-09a6-3c57-afae-c335e1ec5d4a | -14.55 | -46.62 | 2026-09-16 15:15:00 | MSG-03 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2c445835-ac5f-3363-8672-4fcac3c590d9 | -14.58 | -46.63 | 2026-09-16 15:15:00 | MSG-03 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 42423f66-b239-3418-9e3d-2d5ca831fb8b | -13.3761 | -51.698 | 2026-09-16 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 14f1ef61-020a-30ed-9e35-f8141a396683 | -12.1265 | -44.199 | 2026-09-16 15:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 216.2 |
| 219a3feb-32ab-3c6b-ab45-2f14ee5e0a74 | -6.6952 | -58.7097 | 2026-09-16 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 72f8c38a-7149-3f35-a41a-592b88dd0415 | -15.3602 | -52.9678 | 2026-09-16 15:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 62af23b7-ace9-3cae-93e9-38a0d553fd71 | -8.5431 | -44.4902 | 2026-09-16 15:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 313.4 |
| 21487c82-c70c-3cf5-81e7-25491078f5c1 | -9.0309 | -61.0314 | 2026-09-16 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| f2f316b0-a3fa-34af-832d-ef8785577a99 | -11.2488 | -54.1378 | 2026-09-16 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ab9095aa-edb6-3412-9aef-a6ad2b33b3ef | -5.1624 | -55.9338 | 2026-09-16 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| dfa29d2e-28ec-3435-af6d-6c8414c1ff1d | -5.851 | -52.0465 | 2026-09-16 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| f140755a-5add-31f6-8c86-3f5bf0fcd1b1 | -8.2052 | -54.8416 | 2026-09-16 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d536edb7-05d1-32bb-98ed-abb3b70ea8f3 | -13.5841 | -51.8845 | 2026-09-16 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 37e3e609-3d57-3c02-a604-47dda770e83f | -3.4461 | -58.0005 | 2026-09-16 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 3ba3b3f7-5ea3-3620-bc3e-c00c4d0a7697 | -6.0993 | -59.9076 | 2026-09-16 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 7823f661-a349-3d0b-bd07-236b183e3022 | -13.3387 | -51.6389 | 2026-09-16 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 6296ff27-73b1-3e73-be1e-c4c3bcb36962 | -7.7992 | -66.9203 | 2026-09-16 15:20:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 44f65b94-2771-3314-90ed-30dc61659532 | -10.3955 | -58.2962 | 2026-09-16 15:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| bda9a35e-c3d0-3b83-8838-6fe3842b6c91 | -10.0293 | -52.12 | 2026-09-16 15:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 48d499f4-3f22-3b0e-8306-bb8bc57422a4 | -14.2796 | -51.7097 | 2026-09-16 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 79970e6d-288c-3400-8442-08ebec8ec00f | -12.12 | -57.1967 | 2026-09-16 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 743dd33a-f615-3ffd-b0c4-310389d6ce17 | -1.6206 | -55.5679 | 2026-09-16 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 05612068-f74c-3366-b925-224c04e62118 | -8.396 | -47.2121 | 2026-09-16 15:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 9f66156e-0181-3b47-89d0-579a9c5dd82d | -11.9543 | -49.7728 | 2026-09-16 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 38797a56-aa0d-3501-947f-ba2d2450e40a | -9.3707 | -60.3032 | 2026-09-16 15:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| fce29ca4-691d-3c45-9d55-3ce4a4950d01 | -13.3199 | -51.62 | 2026-09-16 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| c8cfae1e-5d39-3a11-8bb3-a19f05d41f1c | -13.5131 | -51.5319 | 2026-09-16 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 0ec81dfb-3e81-32b4-84f7-71112836f8c2 | -6.1178 | -59.8877 | 2026-09-16 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| f68110ad-b673-376e-8d7a-45a4f8983392 | -13.3949 | -57.0242 | 2026-09-16 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| f89a6e23-20c3-3c6e-9b47-3fcc9bc3a7ec | -9.7136 | -64.9074 | 2026-09-16 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 2dd81660-0552-3bee-b83b-3f254f9c98f1 | 4.1316 | -61.2378 | 2026-09-16 15:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 202f6b8b-f725-3753-ae2b-b8ef526c25f9 | -6.2731 | -55.2904 | 2026-09-16 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| c506e808-903c-3630-9640-e57d7adb0758 | -6.1292 | -57.7223 | 2026-09-16 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| ba8d2062-7a5e-326a-8e7b-ef9fcb918435 | -9.0962 | -65.9384 | 2026-09-16 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 58b28deb-a82b-3d72-bfaa-707fb90581a8 | -8.5428 | -44.5132 | 2026-09-16 15:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 656.7 |


[Clique aqui para ver as próximas entradas](README82.md)
