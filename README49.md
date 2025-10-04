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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b168cd93-76f2-3c41-aaba-6da0d91134f1 | -21.93249 | -46.59799 | 2025-10-04 03:55:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 82d45ef5-e8ed-398c-a2ac-d761fd101ddb | -18.17045 | -53.34764 | 2025-10-04 03:55:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 912fcb5d-2cea-390a-81ca-f8d2445a8b73 | -20.47162 | -44.8223 | 2025-10-04 03:55:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 4cc61802-61c5-3418-8cd4-f3130ba11ba9 | -17.70467 | -47.09336 | 2025-10-04 03:55:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 3c4d0147-8af2-3022-a268-6d121d263177 | -18.18104 | -53.35999 | 2025-10-04 03:55:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 05f432f2-0943-3abf-8567-015e260eaaf9 | -18.16259 | -46.10474 | 2025-10-04 03:55:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 481d1828-1dc1-3838-a973-89d1e1d6d97d | -21.84938 | -41.36795 | 2025-10-04 03:55:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1850132b-778c-354e-b3e9-39843bdca778 | -20.10082 | -46.28144 | 2025-10-04 03:55:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 680eb1f8-e630-35e6-a33e-b25687e8f0f1 | -20.42335 | -42.34458 | 2025-10-04 03:55:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3d18a4fe-1077-3c20-89c3-4efee4ecdf97 | -20.46773 | -44.82154 | 2025-10-04 03:55:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 84baf704-575c-3a07-a8cc-88954505548d | -21.126 | -42.88075 | 2025-10-04 03:55:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a25170ca-0acd-3c7b-b579-f7da08670768 | -19.59381 | -44.62929 | 2025-10-04 03:55:00 | NPP-375D | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26807cdd-eb0e-38ca-9a10-4ac1c600ebea | -21.3142 | -45.18071 | 2025-10-04 03:55:00 | NPP-375D | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 530b5bdc-6f2c-3f4a-9f38-db411c65b911 | -18.462 | -49.4435 | 2025-10-04 03:55:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| acd9aac6-4484-3d8c-87d5-07a715abe7b1 | -19.70536 | -44.13171 | 2025-10-04 03:55:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bb14df78-195a-34dc-b732-6d7280937230 | -20.06854 | -43.75564 | 2025-10-04 03:55:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e8081040-783d-3522-9fff-aa3106cff715 | -22.57205 | -42.38033 | 2025-10-04 03:55:00 | NPP-375D | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b55a0f28-710e-3191-b831-f5a45150bcd0 | -21.06358 | -43.44864 | 2025-10-04 03:55:00 | NPP-375D | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ca12ae76-58cf-3427-a437-61394002a409 | -22.76104 | -45.30355 | 2025-10-04 03:55:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1961cd2c-a20f-3fc8-8953-c8aed526496d | -20.10806 | -44.63395 | 2025-10-04 03:55:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c204db78-7f07-3504-8158-f8a90aa6d385 | -21.55847 | -45.27396 | 2025-10-04 03:55:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| af13f961-480c-3c96-8247-79a90da1fd17 | -18.17678 | -53.35107 | 2025-10-04 03:55:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8a8b8c71-258c-31f0-9205-eece4ed29ba6 | -20.14296 | -46.41902 | 2025-10-04 03:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae2c2b57-4e15-3eb2-b141-3c7049b094a7 | -18.72726 | -41.62063 | 2025-10-04 03:55:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 49134d76-752f-3ac8-a32f-66b593744143 | -17.1697 | -53.04517 | 2025-10-04 03:55:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e14f6d7-26fb-3038-b1bb-ef31d4bdea4f | -19.57963 | -48.02135 | 2025-10-04 03:55:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0d952ef1-0c1e-39da-b42e-ed92c946bf21 | -17.70571 | -47.08813 | 2025-10-04 03:55:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 6ff0bba2-4aa6-37f8-84ad-adc6bbf56be0 | -20.1421 | -46.42344 | 2025-10-04 03:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f2c632b-4ba4-37fc-b457-1bf39939f7b4 | -22.28434 | -46.75929 | 2025-10-04 03:55:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4a898043-a21f-35a2-a3d3-a869ede167cc | -20.4755 | -44.82315 | 2025-10-04 03:55:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ef2376f0-7fd1-3d81-82e3-e7c7fc19fe1e | -17.16491 | -53.03799 | 2025-10-04 03:55:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 185ae62d-cb96-3795-97d4-1afd35ce68fe | -20.40232 | -41.33078 | 2025-10-04 03:55:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 88a164cc-0379-3d6c-9fcf-96ada4b9911a | -18.22847 | -53.3746 | 2025-10-04 03:55:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9fea51c4-a55d-38a2-a6b9-6af8cded5576 | -20.4109 | -44.13485 | 2025-10-04 03:55:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 688a9b67-192e-3826-b24d-d61225495cd7 | -22.2768 | -46.75284 | 2025-10-04 03:55:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9ce37443-f371-3750-976f-da062065b9ea | -21.34122 | -44.99311 | 2025-10-04 03:55:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| fd6dd799-1a53-3236-a9ae-435b929461d0 | -22.27596 | -46.75711 | 2025-10-04 03:55:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 57470061-3fd1-3bca-ac3a-f137f3f1d865 | -22.2835 | -46.76363 | 2025-10-04 03:55:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 60ac70e2-05a8-3793-a05a-64dd740474f5 | -15.2205 | -56.8414 | 2025-10-04 04:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 9da23493-8295-345e-9c30-c0b39ae23e7f | -5.4847 | -44.1212 | 2025-10-04 04:00:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 67d060ce-c261-3d1b-8ee2-bbab667bf8b1 | -5.4849 | -44.0982 | 2025-10-04 04:00:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 0636f206-82b5-3541-95ff-8ab8c1bc2cdb | -6.8774 | -47.2334 | 2025-10-04 04:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| afcb38d1-767c-396f-96d9-3eba0650b8d3 | -14.6526 | -48.2964 | 2025-10-04 04:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 111.1 |
| f2c36003-35eb-371e-87ad-cf0f10310c39 | -14.2316 | -46.1024 | 2025-10-04 04:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 93.5 |
| d9c47ba5-5a52-390b-9519-b52da5c74d68 | -6.0806 | -42.5118 | 2025-10-04 04:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 188.5 |
| 44079cfb-4ae8-34c7-b787-6d487fe4328e | -11.9339 | -46.3699 | 2025-10-04 04:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 25e68a98-1165-3a76-b273-ad7e32326b59 | -10.3343 | -50.3402 | 2025-10-04 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 2af38227-77d5-3a0f-94a2-aaf59574cf55 | -14.672 | -48.2933 | 2025-10-04 04:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 121.2 |
| b1debc64-3500-3574-8ee8-5c18e41550b5 | -4.954 | -45.0694 | 2025-10-04 04:00:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 1588d10a-da4f-3e2c-b975-c8d032d6d867 | -12.0314 | -45.1901 | 2025-10-04 04:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| e0714df9-d0db-3e2b-87f5-a759998b9a9f | -11.9139 | -46.418 | 2025-10-04 04:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 21bb25a2-7a30-3158-ba1b-cbbc642607fd | -11.9331 | -46.4153 | 2025-10-04 04:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 423e3b9b-ef7e-38b2-9d60-c42005a1e421 | -4.4443 | -43.263 | 2025-10-04 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 7809bfee-2553-398c-8fe7-fd6448719ead | -7.7489 | -46.3168 | 2025-10-04 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 41c7bfd3-fc33-3f0f-a778-11247deff82c | -6.0804 | -42.5354 | 2025-10-04 04:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| c080270c-8e1b-3176-8de4-be2ec9147a71 | -2.9013 | -50.7351 | 2025-10-04 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| c7a4e1a2-3f34-32e9-b253-7c8041756f71 | -5.2152 | -45.0756 | 2025-10-04 04:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| c564df15-91b7-3419-8e74-6f8ec0e48b85 | -9.3464 | -54.5201 | 2025-10-04 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ec8954a6-8fe0-3f71-958d-de7e33be9d7f | -5.1967 | -45.0541 | 2025-10-04 04:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| b3f5f2cf-4abc-35e6-b680-db34420aab15 | -14.6521 | -48.3188 | 2025-10-04 04:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 774ab1eb-2011-3e13-8fa4-acdd7818549e | -11.9147 | -46.3726 | 2025-10-04 04:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 7ad70c21-7745-38bb-a88f-912587995ef0 | -4.6133 | -43.1594 | 2025-10-04 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8c904af5-69e7-32ac-ab6f-f32cff5607fe | -14.2321 | -46.0794 | 2025-10-04 04:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 033c33dc-ddc4-33ca-aaba-4d373e0319d8 | -6.0618 | -42.5133 | 2025-10-04 04:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| eebe9c0b-0c8a-3f12-aa6b-4db231cf0634 | -4.6135 | -43.1361 | 2025-10-04 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 1d6d126b-3a85-3ab0-b24d-8147ac130622 | -4.4258 | -43.2408 | 2025-10-04 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| ba8cd1f3-1081-3163-ba50-ff7a4ac4e3c3 | -12.031 | -45.2132 | 2025-10-04 04:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 32e9d091-e662-3bbd-812b-f65beac9284b | -14.6716 | -48.3157 | 2025-10-04 04:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 33aa909a-6cc2-382e-83fb-5822155cf7e4 | -5.1965 | -45.0768 | 2025-10-04 04:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 0b9ff91f-b73c-3ad4-a049-db0a8a5c7a34 | -7.7491 | -46.2944 | 2025-10-04 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 27238801-d42a-31ce-8306-aa9fa5c56697 | -14.251 | -46.0991 | 2025-10-04 04:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| fed060f1-3b7d-3744-8c21-f2aa5cc36285 | -4.4445 | -43.2397 | 2025-10-04 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 36e36378-35c4-393f-b697-45b03512cbeb | -11.9143 | -46.3953 | 2025-10-04 04:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 323.7 |
| 3c372e79-0e44-3d92-8601-c895e1a2827e | -11.9335 | -46.3926 | 2025-10-04 04:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 329.4 |
| 11c9677d-3ebf-3ac7-a96a-79867883c841 | -14.251 | -46.0991 | 2025-10-04 04:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 57.7 |
| f6240549-5463-3286-8f6d-e46b272f0d50 | -21.6882 | -50.0788 | 2025-10-04 04:10:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.6 |
| 03c742c8-c4a9-3002-bfcd-6828f70096f1 | -11.9143 | -46.3953 | 2025-10-04 04:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 226.1 |
| 4deb96a2-4ce0-33fd-a0da-42170f39a821 | -12.031 | -45.2132 | 2025-10-04 04:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| b5036652-cae4-317a-9d9a-816b43a24d30 | -15.6019 | -52.4888 | 2025-10-04 04:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 8c9b44d1-63dc-3cc0-94b9-b3c3bba0ad68 | -6.0806 | -42.5118 | 2025-10-04 04:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 124.9 |
| 94be3df6-c81c-341d-bae6-9761cbbbef4d | -5.1967 | -45.0541 | 2025-10-04 04:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 04e396eb-5500-345b-9154-d2b66911b560 | -6.8774 | -47.2334 | 2025-10-04 04:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 8f6280f2-22e9-3798-97d0-bbca6dd34824 | -21.6888 | -50.0559 | 2025-10-04 04:10:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.9 |
| bf98e41a-cfb8-3362-9fe9-322a50f1ed0c | -11.9335 | -46.3926 | 2025-10-04 04:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 75eceebd-38d6-3804-9c07-971bbf527c23 | -11.9139 | -46.418 | 2025-10-04 04:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 0b56e58b-8fc1-3b82-837b-abe0bab3feb2 | -5.4849 | -44.0982 | 2025-10-04 04:10:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| c3d34bd3-e623-32af-99d4-608f3b3f7a21 | -14.6526 | -48.2964 | 2025-10-04 04:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 23f59222-baa4-3405-b6a6-e2cd44b5e196 | -5.1965 | -45.0768 | 2025-10-04 04:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 15881698-a519-339e-a356-929eb3892e57 | -4.4445 | -43.2397 | 2025-10-04 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 65f8f2d6-a341-30b0-bee9-4d6a7b4b7aed | -6.0618 | -42.5133 | 2025-10-04 04:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| ae026e9d-9d97-3daa-9abe-c46b4e9fba91 | -11.9147 | -46.3726 | 2025-10-04 04:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 113.4 |
| bd6b3f91-997f-3c36-9328-d3a39a5cf534 | -12.0507 | -45.1872 | 2025-10-04 04:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| cc381e98-2b6c-38d9-8cec-20e87f5f3117 | -4.954 | -45.0694 | 2025-10-04 04:10:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| cc1a6a3d-8eea-3c76-bdd7-e810f45f75ea | -12.0314 | -45.1901 | 2025-10-04 04:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 825973bf-b7fa-3e3b-a5bb-3fbc375aabc9 | -11.9339 | -46.3699 | 2025-10-04 04:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 4b09c391-dd4a-3be3-87a9-e9c10ec0817b | 0.51223 | -50.77558 | 2025-10-04 04:10:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51cc82f6-06f9-38cf-b656-3ca4bf2ad6ac | 0.51067 | -50.77552 | 2025-10-04 04:10:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0895937d-5116-3c5f-ae3a-c6a5f2c66aa1 | 0.50636 | -50.78336 | 2025-10-04 04:10:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 771a5ca9-6010-3ec4-b130-7e44d96134ac | 0.50734 | -50.77997 | 2025-10-04 04:10:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e083f7a2-6e4b-3aea-858d-83d46344dde4 | 0.50681 | -50.77649 | 2025-10-04 04:10:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README50.md)
