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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90e5328a-1596-3348-94bc-620e1e702d81 | -12.09734 | -64.24003 | 2025-10-11 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46eddfe6-fdf2-3a9e-8eeb-c2dd9b082905 | 1.20796 | -50.85991 | 2025-10-11 06:44:00 | AQUA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 27a9e28e-b05e-333a-a735-442a6f0558a8 | 1.19826 | -50.88114 | 2025-10-11 06:44:00 | AQUA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 72f079bf-e4a3-31c2-b069-61a9e793234b | 1.19531 | -50.86183 | 2025-10-11 06:44:00 | AQUA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 3fd8aa50-10b9-3329-860f-a3efd23dfbcc | -10.58254 | -69.06643 | 2025-10-11 06:44:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b407567a-38f7-3d51-89fc-ce145e3131d5 | -8.4277 | -70.10748 | 2025-10-11 06:44:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7d2d840-1d0c-305b-8f85-fd956c2d2f86 | -10.57829 | -69.07003 | 2025-10-11 06:44:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86935686-3aae-3884-aed1-c17d434a5e30 | -8.41812 | -70.11559 | 2025-10-11 06:44:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 603098f8-8767-3856-9d85-d8e5d62c0079 | -10.57572 | -69.07063 | 2025-10-11 06:44:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0103abd-364b-398a-aed6-7ecf6732f3e6 | -8.431 | -70.1057 | 2025-10-11 06:44:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59b556af-a45f-36ec-8df5-6822bc95b6ea | -10.6953 | -68.55251 | 2025-10-11 06:44:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c75108ed-c90b-38e8-bf78-529b7bca24a0 | -10.57629 | -69.0658 | 2025-10-11 06:44:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa8f7cc5-7f0c-38d0-9f6c-e931ec53aa33 | -8.4176 | -70.11942 | 2025-10-11 06:44:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6236383e-4121-3b05-9b0c-a7910b39f38b | -9.16964 | -68.17768 | 2025-10-11 06:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94a787d5-3957-33c0-91c6-b212e5439cb8 | -8.42326 | -70.12022 | 2025-10-11 06:44:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 006f2731-ad26-36c6-a2d1-19f8b6460ef9 | -8.44076 | -70.11874 | 2025-10-11 06:44:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 389e8213-378e-3850-8d91-71c678788b8c | -8.44129 | -70.11494 | 2025-10-11 06:44:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26a3a522-6474-30f3-aa11-d2e4eb0140f8 | -9.1761 | -68.17859 | 2025-10-11 06:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4f22ed2-6b4c-32f7-943d-812e86ac6a98 | -8.42819 | -70.10366 | 2025-10-11 06:44:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed9cb56e-0178-3f98-8cdc-61e2febe8bb6 | -9.17542 | -68.184 | 2025-10-11 06:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 917b4c0d-30ff-3457-ab79-ceaab84ffb6b | -8.41864 | -70.11178 | 2025-10-11 06:44:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f0ffa3d-d3b3-37ba-a9cc-f96010f16ed7 | -10.5789 | -69.0652 | 2025-10-11 06:44:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65828bb0-02b0-366d-af1b-e0223cc903cf | -10.70173 | -68.5534 | 2025-10-11 06:44:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1e186b4-8cdc-3b8d-bc5b-844f65ca4ec4 | -13.59285 | -56.92878 | 2025-10-11 06:48:00 | AQUA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fedb38bf-1395-3c03-978b-ea9ac1164ce4 | -15.16374 | -56.71566 | 2025-10-11 06:48:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 919edc6d-0681-3f8a-811a-e7c42392ce55 | -17.83409 | -57.65345 | 2025-10-11 06:50:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 477c17fb-4aca-39c6-93c5-5dea7e5e3f31 | -15.96181 | -59.52965 | 2025-10-11 06:50:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| af29d678-eda8-395c-975f-192a681416e0 | -17.82526 | -57.65822 | 2025-10-11 06:50:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 1924b009-99e6-3d32-baaa-e81c067a3244 | -17.81498 | -57.65745 | 2025-10-11 06:50:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 4d9c9275-9e83-3224-b215-56333d01f32c | -22.53384 | -52.05902 | 2025-10-11 06:52:00 | AQUA_M-M | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 45.2 |
| b6036c21-8c1e-3bf6-8948-0e419a91f69a | -22.5435 | -52.0429 | 2025-10-11 07:30:00 | GOES-19 | JARDIM OLINDA | PARANÁ | Brasil | 4112603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 91.1 |
| 2c9a7984-c61c-3d1f-b645-62b391aaaf6d | -17.2722 | -46.8932 | 2025-10-11 07:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 65.9 |
| e8770442-0994-3e4f-b950-f1bbfd90842f | -22.5435 | -52.0429 | 2025-10-11 07:50:00 | GOES-19 | JARDIM OLINDA | PARANÁ | Brasil | 4112603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 84.2 |
| 6ca9b5c0-b233-3fe6-9943-4197c3ec47f1 | -13.8501 | -45.7992 | 2025-10-11 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| dd9d4739-213f-3ef7-aa10-146b2530194c | -11.7622 | -46.3487 | 2025-10-11 11:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| ce3f0f37-7e54-37f7-a0ee-d35a847fb3af | -10.5084 | -47.3624 | 2025-10-11 11:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 52967345-0ced-3e54-9a16-a06785adc89c | -13.8496 | -45.8223 | 2025-10-11 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 60441e80-6cd7-34e1-bd13-af8658a734eb | -11.7622 | -46.3487 | 2025-10-11 11:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| f8e9ec65-5711-37f3-9403-ef83a2f88211 | -11.7622 | -46.3487 | 2025-10-11 11:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 68ba0469-5a87-3820-a20d-35d0a299f218 | -10.5084 | -47.3624 | 2025-10-11 11:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| b4aee784-dd72-31f9-bf1f-4d4c1a1bdcd3 | -10.5277 | -47.3379 | 2025-10-11 11:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 5e4d573b-5c70-3de0-a091-a0277be6b387 | -10.5087 | -47.3401 | 2025-10-11 11:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| b3a4c165-d4b2-3e51-92fe-02826e8eb564 | -10.5274 | -47.3601 | 2025-10-11 11:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 1dbd9f1a-93ed-3c88-85c4-aead87c6de26 | -13.8496 | -45.8223 | 2025-10-11 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 314.8 |
| 2a80bfe2-8a45-3afb-a242-8ac7e97c71e3 | -11.7622 | -46.3487 | 2025-10-11 11:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 9ba5cb10-eec9-3874-a91f-d87742792362 | -13.8501 | -45.7992 | 2025-10-11 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 265.7 |
| 932f385d-66bb-3056-95a9-33e180b9849b | -13.8491 | -45.8454 | 2025-10-11 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 35c1a9b9-0eeb-31f7-b008-ae2a0a57948f | -10.5087 | -47.3401 | 2025-10-11 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 0eb61da9-7e5e-3f77-996d-200904b8eb13 | -10.5084 | -47.3624 | 2025-10-11 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| fdbc6668-5b7d-34fc-b7bb-1c617b244382 | -15.0021 | -45.5725 | 2025-10-11 11:40:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 85d1dde0-5c94-387e-a56a-766c3da1a79c | -11.7622 | -46.3487 | 2025-10-11 11:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| dffab9be-c12d-3d40-b8e4-20a518df30ac | -13.8501 | -45.7992 | 2025-10-11 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 1068335b-839c-3224-989f-f3a55141dd44 | -10.9293 | -47.1553 | 2025-10-11 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| ba8410d8-9872-30fc-8c31-8e40e37ede7b | -10.5084 | -47.3624 | 2025-10-11 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 6d27a5d6-b7f7-3f35-80bf-727cdc52bd28 | -13.8496 | -45.8223 | 2025-10-11 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| e2454799-5c90-3b17-87ae-62973a407bff | -15.0021 | -45.5725 | 2025-10-11 11:50:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 126.8 |
| a453bc23-5557-3e63-9588-7aa39014b7b5 | -5.5947 | -41.10109 | 2025-10-11 11:57:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 54c1f67a-7125-3cc7-a45c-d663cf1cf746 | -5.34136 | -41.58242 | 2025-10-11 11:57:00 | TERRA_M-M | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 81c0459f-9f97-353c-bf8e-88042b45c7de | -6.42485 | -37.56338 | 2025-10-11 11:57:00 | TERRA_M-M | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 15.4 |
| ba3ab226-54c1-3abf-b9d6-5e1b6957faae | -6.17753 | -41.74281 | 2025-10-11 11:57:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| acdefdcf-4641-36f2-b0e1-e420da0cf357 | -6.8365 | -42.79515 | 2025-10-11 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| a7273aab-f405-39f0-94e2-91d4462a6845 | -6.18856 | -42.56049 | 2025-10-11 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 121.3 |
| cc211a8b-9fc0-3fc5-a98f-abc6c19235e4 | -3.47342 | -44.30355 | 2025-10-11 11:57:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c09d074e-f3db-3cc6-99f9-c5a04f4d604a | -6.22105 | -42.66177 | 2025-10-11 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 38.2 |
| 317b008f-cfe9-3c76-baa8-df1c53921b7f | -6.19611 | -42.57058 | 2025-10-11 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 318.1 |
| 6260751a-9cc7-38cb-8424-a7e41c983079 | -5.97177 | -42.26874 | 2025-10-11 11:57:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 35c1e68d-0169-3659-beca-2530123548aa | -4.48884 | -44.2945 | 2025-10-11 11:57:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a12a57ad-1483-3294-854a-9fcf2476dde6 | -5.97304 | -42.25993 | 2025-10-11 11:57:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| bf510a58-565b-3621-9466-dcb279816f4c | -4.20249 | -43.27671 | 2025-10-11 11:57:00 | TERRA_M-M | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 595850e0-d851-3118-9db1-55debf5d94a4 | -5.48362 | -43.41333 | 2025-10-11 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2309835e-638d-3e57-86bf-7e36a5e2c440 | -6.18983 | -42.55166 | 2025-10-11 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 183fbd8f-2e07-3b72-95bc-0eacfc631b70 | -6.21976 | -42.67065 | 2025-10-11 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 40.4 |
| 98b77320-c1b1-37b1-a3aa-9c9824444c12 | -6.71856 | -42.20753 | 2025-10-11 11:57:00 | TERRA_M-M | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f298f2ec-5d20-3dcb-a06a-a6ad3bf837e5 | -6.72342 | -44.14885 | 2025-10-11 11:57:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| d14ded90-7c1d-3267-a9b1-9df8e9659e54 | -6.17532 | -44.67717 | 2025-10-11 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d1026cb9-7e73-387c-ae86-a963ae700b56 | -6.26545 | -42.99136 | 2025-10-11 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 1723e48b-2c61-3d0d-81f7-aae8b5f0fb4d | -6.50018 | -42.4433 | 2025-10-11 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 4b517395-d91c-3545-a83e-6e41c960ca6b | -6.19866 | -42.5529 | 2025-10-11 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 34.6 |
| 88928cd6-22c6-3bc5-a992-d542166fc5f1 | -7.21887 | -39.90598 | 2025-10-11 11:57:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 7432c477-0dd4-3acc-818a-c5c721be2a0c | -3.35572 | -41.85691 | 2025-10-11 11:57:00 | TERRA_M-M | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 7ecb6657-9479-3506-a5aa-ed483b331bf1 | -5.86231 | -42.83958 | 2025-10-11 11:57:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 28.0 |
| de891d8c-d73d-37e1-ae88-3619b9d132d3 | -3.25048 | -42.27385 | 2025-10-11 11:57:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 19a515b0-15ff-3bf8-b8cb-5466eef914f1 | -4.49218 | -39.36979 | 2025-10-11 11:57:00 | TERRA_M-M | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| ef38f176-ce59-3a37-bbb8-5450426748a3 | -6.75648 | -37.57145 | 2025-10-11 11:57:00 | TERRA_M-M | VISTA SERRANA | PARAÍBA | Brasil | 2505501 | 25 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 4600bbaa-bcff-3225-a861-010aa7efca08 | -6.11689 | -42.22968 | 2025-10-11 11:57:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 7e332186-f5f6-30ff-b344-66c45d4e9d90 | -6.15323 | -42.55553 | 2025-10-11 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 7638fba4-4974-385f-910d-a73194a19760 | -6.25315 | -43.00188 | 2025-10-11 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d75a0cef-fc4e-3c39-90a9-fd4df30cec94 | -7.01136 | -42.09573 | 2025-10-11 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 01c75a0a-b3ab-3381-be08-e7ad26a6be0a | -3.59841 | -42.41993 | 2025-10-11 11:57:00 | TERRA_M-M | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 249.0 |
| 365fb1dd-d96f-3a07-b24a-f0c040b8500b | -4.20114 | -43.28596 | 2025-10-11 11:57:00 | TERRA_M-M | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 6ef6f60e-b277-33d0-92ae-15027c1769c1 | -6.26676 | -42.98242 | 2025-10-11 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 5aaf4ab9-2d8e-3d9a-8d1b-66cd95d12c09 | -6.25573 | -42.98396 | 2025-10-11 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 05649259-3a71-3ea0-888d-e1fd38f8a199 | -6.74196 | -42.81147 | 2025-10-11 11:57:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 351a77c6-9ec4-3efc-8b49-f2373207ee5a | -3.60118 | -44.35566 | 2025-10-11 11:57:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| bf9fb231-bad8-3c31-83f5-0a650655d320 | -5.74753 | -43.37596 | 2025-10-11 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 2eaacc89-b45d-38bd-8397-da9de297df32 | -3.74534 | -44.40381 | 2025-10-11 11:57:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6241a6d1-8c6f-37ab-8572-acbb383b5db2 | -3.5997 | -42.41104 | 2025-10-11 11:57:00 | TERRA_M-M | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 9ca74eed-05bf-3c39-a6fc-4a7bbcfd4eb3 | -5.8484 | -41.52707 | 2025-10-11 11:57:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 56ff0b34-78c1-3f7a-b295-02cf82b8edde | -6.04359 | -42.47364 | 2025-10-11 11:57:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 3292378b-8404-3a18-883c-04be25458fe3 | -6.74405 | -42.87263 | 2025-10-11 11:57:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |


[Clique aqui para ver as próximas entradas](README47.md)
