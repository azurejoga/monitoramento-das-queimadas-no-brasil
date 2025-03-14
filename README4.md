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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44ccad55-d387-3199-a2e1-8e4965bfd238 | -6.23823 | -42.7958 | 2025-03-14 04:36:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1ae18e7d-20ff-3938-8ec3-1cfc521d878e | -7.05997 | -44.39066 | 2025-03-14 04:36:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e7850e4-2fec-3037-9732-ffa12a10d4d5 | -6.2523 | -48.0377 | 2025-03-14 04:36:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d3e56bf-f895-389e-996e-011b9601d071 | -6.6373 | -47.85724 | 2025-03-14 04:36:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b17c5419-4f67-3947-a68e-275408b0cf78 | -6.10457 | -42.67238 | 2025-03-14 04:36:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 05d55e38-9c7b-3f3f-8dab-ce02054a2496 | -5.44601 | -45.42949 | 2025-03-14 04:36:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c3651ad-79c8-3220-a153-9b492bac6993 | -6.06854 | -46.13713 | 2025-03-14 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69116f6d-064d-35c9-a53c-0ee6a3b29f72 | -13.90427 | -46.10839 | 2025-03-14 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51874469-5f27-3abe-ace8-e4695787246b | -13.90778 | -46.1125 | 2025-03-14 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 80d07e84-cdf0-3897-b687-f7b5af2bc850 | -12.89554 | -44.87238 | 2025-03-14 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9905ddc-e503-3131-9086-0c972234875e | -11.88404 | -46.94322 | 2025-03-14 04:38:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 116373b1-1dcc-3488-83ef-d262617110e6 | -12.84212 | -43.83387 | 2025-03-14 04:38:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3fffe4de-89fc-39bd-80c8-f6828fd026db | -11.56662 | -47.62429 | 2025-03-14 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 261da282-7da7-3223-af69-981a291a1efd | -11.5714 | -47.61664 | 2025-03-14 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e83b703-9cc5-30c4-95d5-a9f1324cc0bb | -12.88535 | -44.88343 | 2025-03-14 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7b02af47-b5fb-3d0d-a442-f2e8daae19ae | -14.04137 | -47.55502 | 2025-03-14 04:38:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4e60595e-2284-3041-aab3-20c434400c06 | -10.72895 | -49.02618 | 2025-03-14 04:38:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 531f2eb3-faca-34e4-910e-c3c0a0257946 | -11.85582 | -52.2556 | 2025-03-14 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab32018f-7730-3aa1-9413-0482e625db96 | -11.57436 | -47.62127 | 2025-03-14 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44c703bf-276f-361c-a1d9-dafdc4880a00 | -12.5818 | -48.3339 | 2025-03-14 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f954f9e-00b0-386e-9af5-a1c7f10cf944 | -9.02636 | -40.58026 | 2025-03-14 04:38:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b1e2a55b-5dbe-3453-aa32-ec4ff4d7fc18 | -7.24371 | -44.77196 | 2025-03-14 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 062923e0-6ada-3e0e-99dd-2bc01a432858 | -12.88645 | -44.87526 | 2025-03-14 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8f0c5751-8e86-36b9-8cb6-db72dcc6370a | -12.87791 | -44.874 | 2025-03-14 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| edf0ea34-79b5-36ba-ac4c-32db3849d9fd | -13.9073 | -46.11605 | 2025-03-14 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 320bdf80-e8e8-36b6-b0d5-cba5cbd1895a | -11.56723 | -47.62019 | 2025-03-14 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5eba3c43-91d3-3576-97f5-7fa2314b7099 | -12.89127 | -44.87178 | 2025-03-14 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ee3e3d39-ddbf-3872-b292-fb3ec2839d8d | -13.9108 | -46.12018 | 2025-03-14 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a7c9a056-da71-3eb2-abb9-773dc35dfc2f | -11.88469 | -46.9388 | 2025-03-14 04:38:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26f5e41e-e790-35e9-b247-8090aa270ecf | -13.91129 | -46.11662 | 2025-03-14 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f2e63975-f33c-3dae-8f6c-d314b3734a9a | -9.83028 | -40.57097 | 2025-03-14 04:38:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bc971c0b-d665-3b3f-8ddc-cd2993af6d3b | -12.8467 | -43.8345 | 2025-03-14 04:38:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ffe4ae6-f085-34dc-bb87-c08c27889bcc | -12.84734 | -43.8297 | 2025-03-14 04:38:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b15eb937-a336-39f9-95c6-5e5c5d16d390 | -8.59105 | -45.05835 | 2025-03-14 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff8f51b0-720c-352e-bce9-61ecbc42470c | -11.56306 | -47.62373 | 2025-03-14 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 832192d2-6291-3048-b0b5-b04f41bdb0f1 | -7.24221 | -44.77402 | 2025-03-14 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe6dc3b8-5b66-304f-a691-8af39c7a224b | -8.10588 | -43.14642 | 2025-03-14 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| df582a65-275a-3783-8264-ee065d0cbec7 | -13.69761 | -44.32766 | 2025-03-14 04:38:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1846027-441d-3a46-859b-c535bc0701cf | -7.24215 | -44.78229 | 2025-03-14 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c142227-a5fc-3e57-ada3-28ebf855e3e4 | -7.24692 | -44.76945 | 2025-03-14 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f96e6b9b-5ec0-3bc3-b50d-86c61caf9a72 | -9.8248 | -40.57023 | 2025-03-14 04:38:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ba5438b8-96c0-3b5d-a198-1ab726ea7e9a | -14.05767 | -42.63679 | 2025-03-14 04:38:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cd357e4a-4ae8-3db1-b77b-f3e74945e8cd | -11.57374 | -47.6254 | 2025-03-14 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e0797d3-ab36-30ab-98b7-180e74eaa0d5 | -7.24146 | -44.7792 | 2025-03-14 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44d15ef6-2e90-38fc-8b09-76f2727a924f | -11.56367 | -47.61964 | 2025-03-14 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32b4c90f-84e4-3c59-b654-283a5d1fd448 | -10.31942 | -48.65014 | 2025-03-14 04:38:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a756ecab-fca0-3066-8b2e-5a396fe804d2 | -8.10653 | -43.14193 | 2025-03-14 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7b2ebdc0-9a9b-338e-9a4d-f83d5940fe2d | -9.0259 | -40.58381 | 2025-03-14 04:38:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9e1e768f-6d6a-3a4a-bdc1-5575487b3b40 | -8.58945 | -45.05899 | 2025-03-14 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66d54b1e-cf94-3003-8a99-6c08c1818862 | -13.91178 | -46.11305 | 2025-03-14 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cbcb7c14-d719-396c-b814-7090cc68fabf | -12.88108 | -44.8828 | 2025-03-14 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eaf39751-d197-3a50-87a5-eebeea197a26 | -7.24617 | -44.77464 | 2025-03-14 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 29741135-6236-3cab-b4ed-049208daa8da | -12.21262 | -50.92991 | 2025-03-14 04:38:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81c66d80-b97f-3546-a281-127c838f49a5 | -14.20628 | -47.01809 | 2025-03-14 04:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3e06502-437a-317d-abca-4375a5f488f4 | -12.89071 | -44.87588 | 2025-03-14 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 9de6dd05-58db-3176-8a1e-35acc7585de4 | -11.8884 | -46.93932 | 2025-03-14 04:38:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69134dbf-23ad-3138-908c-33f3cec2958a | -12.8859 | -44.87935 | 2025-03-14 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 362202b3-0497-3801-a4b4-ed50e683d626 | -12.84276 | -43.82908 | 2025-03-14 04:38:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db38ed52-a6f8-3319-8a0a-cae8e66ce456 | -12.88163 | -44.87872 | 2025-03-14 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56faeebe-265e-3524-a1d4-cf6bee8e9ffa | -7.24293 | -44.77713 | 2025-03-14 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea73a497-f5a3-3032-a7bf-07cf3f9a5874 | -12.89016 | -44.87997 | 2025-03-14 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1cbc71c2-125f-3fff-b4f6-e84fa389d4aa | -12.58529 | -48.33445 | 2025-03-14 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 561561b0-2fa4-3e5e-b31c-f10319eb4f1d | -11.96037 | -47.0073 | 2025-03-14 04:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac991f03-3e61-3fd7-9fd6-c5a426b58f1d | -8.10867 | -43.14524 | 2025-03-14 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| b1894b2a-b65c-334e-944e-a75b0e09b293 | -12.89182 | -44.86767 | 2025-03-14 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dee972f-075c-39c3-a437-751f822c9b42 | -12.87737 | -44.87809 | 2025-03-14 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f905202c-3ccc-3c80-ad61-f8053d36f956 | -17.78068 | -42.81004 | 2025-03-14 04:40:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 28dcb44a-5e58-3cce-885c-e305fd5cc657 | -17.74981 | -42.89578 | 2025-03-14 04:40:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee987be8-dc19-30f9-af33-4d4ea5a94d3f | -21.19519 | -44.93887 | 2025-03-14 04:40:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 821856d2-13eb-3d2e-bfb4-1a9b5c829927 | -16.67943 | -43.88517 | 2025-03-14 04:40:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d92f1b5-d7df-3b4c-b60d-2376ad40ab4e | -18.3347 | -40.01457 | 2025-03-14 04:40:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 34f59b42-3474-3f54-b8f7-383ceb0210bd | -18.46706 | -46.97306 | 2025-03-14 04:40:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c2bf16e-9c9c-3ae2-b01a-c5f3fb5681bb | -21.83134 | -47.04308 | 2025-03-14 04:40:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d2280bd-0f9d-3c46-a038-268ff141dbcf | -18.29985 | -54.57595 | 2025-03-14 04:40:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a530da36-f88d-3d35-97a5-d2b2e59935b0 | -21.61243 | -48.47338 | 2025-03-14 04:40:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62aad9d1-433c-3556-ba62-86e348aae5c6 | -20.14557 | -52.83578 | 2025-03-14 04:40:00 | NOAA-20 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e17bc22-87a3-3bb1-b4b1-c2219c63fcc4 | -18.29705 | -54.57133 | 2025-03-14 04:40:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c339fd3f-537f-3862-a7dc-a3b5f69ce9be | -19.34496 | -53.76736 | 2025-03-14 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3984c3ae-7d6a-396c-9f54-cf700917b1c0 | -18.46304 | -46.97242 | 2025-03-14 04:40:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 443104e0-c50e-31ae-9c43-823ba4ffd68e | -18.30399 | -54.57258 | 2025-03-14 04:40:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f220a8e8-9d3c-3ff2-a2e0-ec123bb6885e | -18.08342 | -54.02197 | 2025-03-14 04:40:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e57b7286-3da0-3aaa-884f-88e0e1e333cd | -17.78618 | -54.28757 | 2025-03-14 04:40:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4664d835-6a40-302b-b166-4207330137cb | -17.77544 | -42.80935 | 2025-03-14 04:40:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 748b62a6-1982-3c79-8ffb-28ab2627cca2 | -15.26188 | -51.47498 | 2025-03-14 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a3f95d4-7df7-359f-9bf8-d73b81399c6c | -19.34558 | -53.7636 | 2025-03-14 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbef72a8-741a-3e79-a1c7-642ea5b53766 | -21.83182 | -47.03903 | 2025-03-14 04:40:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6867ee0-4d8e-3d9d-bd71-099cdd43cb6e | -15.26519 | -51.47554 | 2025-03-14 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b4add5c-22be-3fb7-b53c-abd54d1de595 | -21.83231 | -47.03497 | 2025-03-14 04:40:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86e0541c-9fe0-3742-871b-5a4d54956192 | -15.07848 | -48.94304 | 2025-03-14 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9117958-dc3c-3ba8-aad3-9a9da0eecad5 | -18.34101 | -40.01519 | 2025-03-14 04:40:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 662a08dc-39fa-38ff-a116-62c0c5a80c34 | -21.61052 | -48.47538 | 2025-03-14 04:40:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41290f90-9a1e-315b-9bd7-6b2eed760a95 | -23.59493 | -47.43973 | 2025-03-14 04:42:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 24ab3219-bcce-3a15-9409-fae064b7b9a7 | -22.61913 | -47.45858 | 2025-03-14 04:42:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27ff9a12-2f9b-3416-bf1c-57a66717232b | -30.14086 | -52.60678 | 2025-03-14 04:44:00 | NOAA-20 | RIO PARDO | RIO GRANDE DO SUL | Brasil | 4315701 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 89e6d51e-bfd8-35a0-94db-b8ee2a949287 | -29.77641 | -51.17802 | 2025-03-14 04:44:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| e29eee08-5dfa-3b2c-88e1-df7de7824f89 | -29.77786 | -51.17637 | 2025-03-14 04:44:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 4242cab8-a744-3ecd-b38b-4ac72b7ae735 | 0.8326 | -59.95211 | 2025-03-14 05:27:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97c5311f-6d80-3f79-92e7-c6d14f3c0dc2 | 3.17207 | -61.01035 | 2025-03-14 05:27:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 382d13c7-ba96-379c-8259-551f2506e17d | 2.64104 | -61.11796 | 2025-03-14 05:27:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e91b17aa-4087-3a36-b10c-b48c52f1b8ca | 3.16875 | -61.01086 | 2025-03-14 05:27:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README5.md)
