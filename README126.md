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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2124767-b401-3f8a-b042-acfa578ff427 | -12.1044 | -47.5816 | 2025-09-13 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 0594a568-34e9-3e41-9a0f-61439aac0059 | -10.8757 | -48.1804 | 2025-09-13 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 03e9bdcc-c81d-3dc7-a1ae-da4788dffea6 | -14.2097 | -46.2209 | 2025-09-13 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 1068302e-656b-36d0-a3f5-819458fd1695 | -15.1601 | -50.1379 | 2025-09-13 13:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 2915266f-b789-3723-b7f1-b490cdcdc7c5 | -12.8259 | -47.9486 | 2025-09-13 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 340e1750-cf51-3b9a-a974-8386a8cbc6c8 | -12.9591 | -48.0186 | 2025-09-13 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 2b17b67f-4906-3919-8bfa-7b3a6b5041c9 | -16.4906 | -55.1276 | 2025-09-13 13:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 92.2 |
| f29c9ac6-74ae-309f-81f1-15d93e995719 | -11.1896 | -51.419 | 2025-09-13 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| d66d3438-5040-3e93-b18d-55931bf24352 | -12.8456 | -47.9236 | 2025-09-13 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 8aa56b6c-799a-33f1-aeb5-4edbac9cad9c | -17.4137 | -49.2744 | 2025-09-13 13:00:00 | GOES-19 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| a0b09fdf-4d9d-35d8-9990-4bf9af818246 | -14.4204 | -47.3011 | 2025-09-13 13:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 5e8d4b6c-8c24-3e23-9cd0-4d3ac8b9f9e4 | -15.1601 | -50.1379 | 2025-09-13 13:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 85.1 |
| f7fc45af-3a70-38dc-8fa0-d1488dfe0d66 | -7.4322 | -44.4194 | 2025-09-13 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| ed2b4834-d468-3094-aa7a-901cd4c3e026 | -13.9185 | -48.2105 | 2025-09-13 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 806f12d8-a6c6-3eac-afd8-4ab621b99ec2 | -19.3417 | -45.1132 | 2025-09-13 13:10:00 | GOES-19 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 112.5 |
| d0c8af7f-7732-3825-afba-b8de0ea804c2 | -12.8263 | -47.9263 | 2025-09-13 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 001be1cd-c54d-318f-b497-603ae6d62858 | -14.2088 | -46.2669 | 2025-09-13 13:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 00761416-f26c-36aa-afcb-13d8906201a8 | -13.2414 | -51.7359 | 2025-09-13 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 3754c9c6-b81c-31d4-9c7e-33be5bf925ae | -16.0796 | -49.993 | 2025-09-13 13:10:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 2647204c-1442-381d-9cd5-345378340672 | -15.4713 | -47.3256 | 2025-09-13 13:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 256e00dd-6cd6-3c27-8581-41e11ca3a504 | -14.3357 | -41.4352 | 2025-09-13 13:10:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 107.5 |
| efb0f602-332b-309d-b13e-98d1d0da0fa2 | -12.9591 | -48.0186 | 2025-09-13 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| ac710c5e-0b55-301f-aa67-31abacf64b53 | -10.8785 | -45.5597 | 2025-09-13 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 254.8 |
| 55162805-b98d-3ceb-b74a-6d3c1241dea9 | -11.8698 | -46.7627 | 2025-09-13 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 731f1e6a-cbd6-32bb-84fa-9abf3b9025de | -12.5787 | -45.7051 | 2025-09-13 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 291.0 |
| de604e06-b482-37b3-8473-848a1f2ffb84 | -18.0071 | -46.9266 | 2025-09-13 13:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 88.8 |
| acc495af-dcf8-3e03-bc46-0191c015ca6b | -10.8976 | -45.5572 | 2025-09-13 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 472.0 |
| c46a1432-bd22-3125-97cd-42175f836f3c | -15.0436 | -50.1337 | 2025-09-13 13:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 605de77e-83fe-32e3-8e4e-a8b929eacaf8 | -14.4398 | -47.2979 | 2025-09-13 13:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 224.1 |
| bbe8bec8-621d-3ab6-80b5-46f30806cc1a | -12.9402 | -47.9991 | 2025-09-13 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 1b6f5517-f8e6-3185-a563-00d7a43e8d7d | -7.2131 | -43.8396 | 2025-09-13 13:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 0ae441ca-22b4-36b6-908d-5456a8a0eda3 | -11.1237 | -50.7049 | 2025-09-13 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 9e0298e3-0529-3f72-acbc-7c79e0539d2f | -12.9595 | -47.9963 | 2025-09-13 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| dcc68c46-0084-3dff-acf8-067993a3cbea | -14.4588 | -47.3174 | 2025-09-13 13:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| f99f6005-4dc2-3888-8d13-4f59a4a391a6 | -13.203 | -51.7406 | 2025-09-13 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 6ad5e7b4-a004-3415-9975-c25cdf86576c | -18.0065 | -46.9499 | 2025-09-13 13:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 5ae17d69-a5ef-38a9-a4ba-087e15db2ed0 | -13.8979 | -48.2804 | 2025-09-13 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 10a66c24-bc0b-36f4-960c-f7b6944083a1 | -12.9398 | -48.0213 | 2025-09-13 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 47e08972-21dc-34d1-bbd4-4874c3fb486e | -12.8456 | -47.9236 | 2025-09-13 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 187.2 |
| ae660aff-c908-3427-87dd-2ad23f790a89 | -17.4142 | -49.2519 | 2025-09-13 13:10:00 | GOES-19 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 96.4 |
| fca35e44-274e-36a7-a60c-f8740d64c3c8 | -10.6575 | -46.292 | 2025-09-13 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 218.1 |
| 9835df2c-d362-3da4-a003-2b010ffa42fe | -12.5791 | -45.6821 | 2025-09-13 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| ab28a831-5737-3b4f-841e-3f5aafdae1e4 | -14.4199 | -47.3238 | 2025-09-13 13:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 29b88e2b-65eb-355a-92f3-2b2222c2ce7f | -16.5099 | -55.1459 | 2025-09-13 13:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 95f6f9cc-b19b-3f26-9fdf-1c3c7ea74544 | -8.9176 | -46.1565 | 2025-09-13 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 886b3988-4aff-30f2-8687-6a9120c7081a | -13.9379 | -48.2076 | 2025-09-13 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| ba75e38b-8ca8-3662-8986-c85712a8e9a0 | -12.1236 | -47.579 | 2025-09-13 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 235.8 |
| 78a5eb7a-c855-3cae-bf22-e988d5d69d74 | -9.2656 | -59.4191 | 2025-09-13 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| b1a3100b-cd25-394b-bf36-6e857b8cc4f0 | -17.4346 | -49.2258 | 2025-09-13 13:10:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 79d478a3-81f9-331b-9e81-aef8abb9a1b5 | -11.8853 | -50.5554 | 2025-09-13 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 319e94b8-153d-3e29-8588-70240ed6a000 | -15.8648 | -47.2322 | 2025-09-13 13:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 409e67c4-6493-3cc4-9275-b8145999c21a | -8.497 | -45.1369 | 2025-09-13 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| ad7c10a2-e84f-361f-98cc-3d20096e7051 | -10.0937 | -47.2109 | 2025-09-13 13:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 427cecd1-193b-3b2d-a51f-f001a08b45ed | -14.1703 | -46.2505 | 2025-09-13 13:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| aeda97b1-7977-3742-aa5b-cdd1a6adb80d | -10.8781 | -45.5826 | 2025-09-13 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 2dd073c9-d8e3-37fd-acba-4566a60cc483 | -9.2658 | -59.3997 | 2025-09-13 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 158.0 |
| 11ff40ea-d0da-3a41-8525-f67cc962e4cf | -15.1597 | -50.1598 | 2025-09-13 13:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 3679291e-5bf2-368e-b23f-f49b51374712 | -12.8452 | -47.9459 | 2025-09-13 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| fab7695a-b800-3060-94ac-9dbfb99b3720 | -12.8259 | -47.9486 | 2025-09-13 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| a8548ced-73ef-37f9-b319-c503a599d1f4 | -16.4906 | -55.1276 | 2025-09-13 13:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 74.4 |
| feeb5df3-089c-3884-aca3-83c774bb383a | -8.5159 | -45.1349 | 2025-09-13 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| b9b2cdf4-b0e8-3294-a3a7-72aae692886a | -11.1259 | -51.9309 | 2025-09-13 13:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 49840989-c895-3d58-a825-84ddd5ffa3c3 | -12.5979 | -45.7021 | 2025-09-13 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 203.0 |
| 516c00c3-5fa7-3a67-a278-c5c59f3628bb | -9.5006 | -55.9588 | 2025-09-13 13:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 185.7 |
| 45173cb4-ad00-3cab-bee8-44c4c778d4f9 | -15.4517 | -47.3291 | 2025-09-13 13:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 67ad5347-e187-376d-8bd6-16af94d3bf68 | -13.8974 | -48.3027 | 2025-09-13 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 6013168c-5d9a-344a-9359-f7c9ff964def | -12.1044 | -47.5816 | 2025-09-13 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 308.6 |
| 162c68ab-574b-3f6b-b7ab-bec5cde3489e | -17.1549 | -48.4908 | 2025-09-13 13:10:00 | GOES-19 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 112.3 |
| ab4f7816-3f2f-3ad0-b2ed-77511f8b27cb | -13.2606 | -51.7335 | 2025-09-13 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 1f85da9b-77a9-3461-b014-f848049416a6 | -15.8845 | -47.2286 | 2025-09-13 13:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 199.5 |
| 7108a77c-e67e-30a8-bd75-bb6b28e0a52c | -13.2222 | -51.7382 | 2025-09-13 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 9b24f5ce-2efd-3383-b8c6-1bfb58ce5bd5 | -16.3422 | -51.5217 | 2025-09-13 13:10:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 100.5 |
| af867847-b5ac-3efe-be65-900b85f7a795 | -14.4394 | -47.3206 | 2025-09-13 13:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 9bb587b7-ff6a-3e95-b19d-8c3883b6d41d | -13.9172 | -48.2775 | 2025-09-13 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 103.0 |
| b415d9bf-17d2-36e4-acec-98658b9cc34b | -10.8972 | -45.58 | 2025-09-13 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 314.3 |
| eb27179c-8ec1-369d-a5c6-1132c8599fcf | -8.9179 | -46.134 | 2025-09-13 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| fec94316-dbdc-3212-a8ad-1ce0e8236931 | -11.7826 | -47.402 | 2025-09-13 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| d276730e-c0c8-3609-a59b-f93e30a5cb8f | -12.0657 | -47.6091 | 2025-09-13 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 87a9d457-2016-3ef9-b6b7-c41af7c4bc5c | -11.3926 | -50.4619 | 2025-09-13 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 207d891b-8193-3da5-8685-e13b30fa4290 | -10.6579 | -46.2694 | 2025-09-13 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| ab6fb738-b617-3a45-bc07-e2b59c96a21f | -12.104 | -47.6039 | 2025-09-13 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 264.6 |
| 64224e63-d785-34b5-b8b1-b01f5d5e5eed | -15.0432 | -50.1556 | 2025-09-13 13:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 6af58477-718b-3c71-8112-7770252635b4 | -10.3699 | -50.507 | 2025-09-13 13:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 7d93fb99-c461-38d3-8c2d-70e07d0ec813 | -15.1554 | -52.4865 | 2025-09-13 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 68cd1fab-4225-3a60-9115-823f33587c73 | -16.5102 | -55.125 | 2025-09-13 13:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 5f46baa4-9257-3e97-817c-71e0440165e9 | -11.1896 | -51.419 | 2025-09-13 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 177.6 |
| d7c90ba4-8a5d-369b-b6fc-ae2bd1836a4f | -15.0241 | -50.1367 | 2025-09-13 13:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| b840c149-6d98-3567-adc4-27f32fe7e619 | -12.8456 | -47.9236 | 2025-09-13 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 0564f1eb-d381-3e3f-b977-54912e398512 | -15.1363 | -52.4679 | 2025-09-13 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 24099a8c-b71e-3514-94fc-fdb893463f58 | -12.0657 | -47.6091 | 2025-09-13 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 34406af9-57fe-3950-a1dc-95cf9c4f4270 | -14.31 | -46.066 | 2025-09-13 13:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 2808b439-f8d5-3d1b-8c05-d9d0e8072972 | -13.9877 | -44.7767 | 2025-09-13 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 6c94e0cf-94cc-3e4c-a36c-835286a48e44 | -14.4204 | -47.3011 | 2025-09-13 13:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 17e786b3-acfb-3e38-9edf-2fb6cb1e50b4 | -13.9185 | -48.2105 | 2025-09-13 13:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 8ec08584-0419-32f2-a9e2-36acf96c17f2 | -17.1549 | -48.4908 | 2025-09-13 13:20:00 | GOES-19 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 5ffc18f5-7248-349b-a2ac-0ac2c1ae6fce | -15.1169 | -52.4705 | 2025-09-13 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 136.6 |
| ebe715a2-2761-3350-9404-c2b48b3e2b19 | -14.4398 | -47.2979 | 2025-09-13 13:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 108acaec-267e-3590-885e-315c0ebfcfb2 | -12.9398 | -48.0213 | 2025-09-13 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 08e1fc04-7708-3964-88e8-56093d7664de | -12.5787 | -45.7051 | 2025-09-13 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 83432458-a3b3-3e53-b754-803e65249e8f | -13.2222 | -51.7382 | 2025-09-13 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 282.8 |


[Clique aqui para ver as próximas entradas](README127.md)
