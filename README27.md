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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2141db7-e8d8-396a-8670-bf2926ce6106 | -4.27133 | -48.65787 | 2026-08-30 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fcb1fb9-f140-38c1-8ef9-61f255bca2c8 | -2.93632 | -41.73579 | 2026-08-30 04:12:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| af1584c9-df21-34a8-9919-d0c9b0772da6 | -5.50709 | -44.62505 | 2026-08-30 04:12:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e1e454d-33a9-3de7-98a0-6194078e25d3 | -6.91373 | -41.63656 | 2026-08-30 04:12:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c7653866-2c3e-3dd3-bfcc-6259837e35ad | -5.88905 | -47.72736 | 2026-08-30 04:12:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b143a0b7-2e7d-3ac2-aa4d-99224b75e208 | -6.43718 | -43.07352 | 2026-08-30 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4f85a50-695c-378b-ac57-5f0ea5d23bdc | -4.36952 | -47.77781 | 2026-08-30 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 7ad4a87e-c79e-3636-ada5-90f14d008b90 | -5.45844 | -48.94018 | 2026-08-30 04:12:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4574ff8-f566-3da2-948f-ed370363f924 | -4.37184 | -47.77152 | 2026-08-30 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 433cccb2-eb3c-326d-bb6d-6cd5d9dd9a66 | -6.86621 | -41.67062 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1cebea76-d12f-380c-a856-cb03bef3eade | -6.86857 | -41.65593 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1e9cfffb-f48c-3f81-b6bb-23fdb3ac22b8 | -6.34662 | -44.10022 | 2026-08-30 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3589ceed-9631-3ff1-b7f3-480dfef19be5 | -11.34494 | -45.16409 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 39239e4d-0101-30a8-826e-a4181fb1acca | -11.2945 | -54.03764 | 2026-08-30 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 237b81c3-0042-36fa-b466-c2b04202941a | -10.40166 | -38.21928 | 2026-08-30 04:14:00 | NPP-375D | ANTAS | BAHIA | Brasil | 2901601 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ad4655c1-e2d4-3eeb-bbd6-1a2c2b96d88e | -10.81597 | -45.32104 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13d2a4f4-7a00-3861-a212-78f0a2bd7bde | -7.95361 | -44.27068 | 2026-08-30 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| def5e95d-8a57-3e6c-afd8-0a8a710e2e24 | -11.35248 | -45.16555 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 44d64a74-f6c4-3233-b336-431d13ebb0df | -10.95302 | -43.03479 | 2026-08-30 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 5f143464-d98f-334d-a9e3-5d4d0f4072b2 | -10.95583 | -43.03915 | 2026-08-30 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a177037c-23dc-3496-9b76-92bc94fc0fdf | -11.2407 | -54.01269 | 2026-08-30 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 559b973c-b261-3d17-92ee-1d9c6f43e7d4 | -9.76597 | -48.16291 | 2026-08-30 04:14:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c5d70f7-2a1d-33d4-8597-70bbc5186731 | -12.43785 | -42.88824 | 2026-08-30 04:14:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e9b17817-da98-33f5-aa60-8d500fcbeddd | -9.47166 | -51.58938 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2abd20cc-6a7d-34f7-973a-a813ef723e98 | -10.99648 | -50.52342 | 2026-08-30 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 075d9a68-643f-34ec-9127-4593f87e7879 | -6.40987 | -51.66818 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5552f18a-474a-3f78-b49d-b679f5b81377 | -11.20554 | -45.0755 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e521fe27-2e6c-3878-be9c-c85361005902 | -7.61059 | -45.848 | 2026-08-30 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78faa247-a4c7-3463-934e-0388f8156227 | -10.81515 | -45.32591 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 624119da-ef58-3df0-a5b4-2c111ac62747 | -12.90164 | -45.88183 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d287bd2-dd0b-31d9-8d34-d9550bce5ce4 | -9.21252 | -46.07343 | 2026-08-30 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cfde7d4e-9062-3a3a-a7f7-8346c526cc97 | -11.83961 | -46.76581 | 2026-08-30 04:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f710da14-387d-3e10-b4ab-06cd68a14524 | -11.27071 | -45.33263 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b01fc51c-affd-3a4c-8958-3744cb21c324 | -7.61331 | -44.84452 | 2026-08-30 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6ac6218-8ba1-3fba-a76e-61b3046595be | -11.34199 | -45.15865 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a028e7bd-c632-355b-a2ab-d8a564ca7f89 | -11.21309 | -45.07677 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6bd29fb1-79b9-3582-a78f-b6d607125eda | -10.34204 | -49.97229 | 2026-08-30 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1dfcd30f-24b0-3734-bdfa-315bc0139043 | -9.19573 | -51.55727 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44253c20-177c-39c0-b253-9c7e60849b27 | -7.09922 | -42.21675 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9aab1f7f-a93c-356b-8a19-87d7b64271c1 | -10.81213 | -45.32035 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05777966-c884-3b70-be88-76526e834e42 | -8.14219 | -45.47858 | 2026-08-30 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9091677f-a384-3e18-b255-eaa39905b504 | -7.7987 | -43.89942 | 2026-08-30 04:14:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec8302b9-e348-3e6e-83b1-76015f151032 | -14.94832 | -40.8331 | 2026-08-30 04:14:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3e95ed6d-cbfc-33d4-915b-bc17e41b9a46 | -11.16068 | -51.2985 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c1a71c9-abdd-39f9-951f-7fdd9173bbe2 | -10.39812 | -38.21875 | 2026-08-30 04:14:00 | NPP-375D | ANTAS | BAHIA | Brasil | 2901601 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 69fb445e-6af9-3108-a859-47a17ba52d44 | -7.09288 | -42.83423 | 2026-08-30 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e701bb8e-689b-3826-ba2b-8393b03343d8 | -10.13237 | -45.69795 | 2026-08-30 04:14:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9b26d9d-f55b-30d0-ab68-560ee0554081 | -12.19234 | -40.40768 | 2026-08-30 04:14:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0f16eb98-1e18-3336-aedb-8e6da6de8f44 | -8.09903 | -40.07397 | 2026-08-30 04:14:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 05b1ca08-b5b1-356d-a151-03ef4d8d698a | -11.6548 | -46.756 | 2026-08-30 04:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd7501eb-d1a3-39ea-8d08-b627da5f72ac | -9.09973 | -50.61053 | 2026-08-30 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1cefa02-e39a-3e14-a333-f95c5bf9cf24 | -9.78343 | -46.41991 | 2026-08-30 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7579d43-90f2-34de-a12f-2113b803d036 | -7.0773 | -42.22094 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| aae5c06c-1c2d-3be8-94c3-436e38dddabf | -11.33692 | -45.14296 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72efb54c-08d1-3e89-bc4f-4ac95ffe2a22 | -11.48346 | -45.05801 | 2026-08-30 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1a6f110c-6ea2-33ef-aefd-9ffab38a6e3b | -11.27213 | -45.33497 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ff25f055-d8f0-39b2-a628-f7894f378119 | -6.409 | -51.67295 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6807276d-3f5f-3ea9-9254-7699741eebac | -7.06078 | -42.14885 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d88509c1-9dbb-3d52-96b2-5c88b9de536b | -11.81421 | -51.04579 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 905ed082-ef33-33c5-a03f-0efc3e65edfb | -11.48423 | -45.0535 | 2026-08-30 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5487bf69-9ab3-392e-8349-e7928b21958b | -10.78961 | -45.33625 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 91dd944a-9e43-30d8-9d9b-9ba3bff02088 | -8.60653 | -54.78265 | 2026-08-30 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8d28513c-2a9c-338a-b7e0-4c75e4f5ac3b | -9.93178 | -47.60382 | 2026-08-30 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3a936e9-743c-3e25-b787-9bee346848c6 | -11.27079 | -45.3202 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 07a1efbe-9ba5-3b68-b3eb-ac94d47d3acc | -11.15921 | -51.30626 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f473a2a7-f8a5-3eba-a532-753828a8c1f6 | -11.01941 | -49.69088 | 2026-08-30 04:14:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 518519d7-4bdd-37f7-ab15-b328109758a8 | -11.24189 | -54.00683 | 2026-08-30 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ca47c61a-c8d1-3429-8688-4877171cf5bd | -11.26996 | -45.32492 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92515158-d170-3dfd-8366-7c0e1314679c | -8.20304 | -44.81521 | 2026-08-30 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5bff55b9-a123-357b-9294-88bb1dfd5c27 | -7.11892 | -42.83028 | 2026-08-30 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1762cf68-3f8d-30c8-8b53-e41ab2fcbcfb | -7.12698 | -42.7585 | 2026-08-30 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cbf6f437-6148-3f21-bc5b-105fbb0222c4 | -12.90248 | -45.87696 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11ed852d-0ef1-3413-b792-15f3afe1268a | -7.29888 | -49.542 | 2026-08-30 04:14:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b47e3184-5e68-318f-9ba8-77277bda84ff | -10.75777 | -50.88108 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35ceb0cd-7d10-3877-930a-618b34710f1f | -10.82201 | -45.33212 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf565291-3591-31d4-bb45-7234103a7275 | -8.75795 | -50.4684 | 2026-08-30 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9eb0c411-ee4d-31a0-abe8-696fafe80929 | -7.09738 | -42.22813 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f9dedc4-a238-32d8-925c-512f16b299ce | -13.19755 | -44.06977 | 2026-08-30 04:14:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80be0c71-5313-3d56-bda9-d64ea2a4fe1c | -6.81838 | -51.15373 | 2026-08-30 04:14:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 627d8a8a-4899-3cd4-95a7-24577fcf87fe | -11.29573 | -54.03164 | 2026-08-30 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7eff91ed-3cdc-315a-b9e8-1952aad1c58f | -10.73597 | -54.04087 | 2026-08-30 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2df56deb-ba5d-3d63-9629-a75a705ca1d2 | -11.26928 | -45.31783 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a7b64f81-8d7a-3a98-8905-834a65e7e4b4 | -10.80912 | -45.31484 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f64d4784-2040-38da-82fb-2b7723d2bc39 | -11.34657 | -45.15469 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c0239129-e81d-3cfe-a090-a258f46b5a2e | -10.79045 | -45.33139 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6d52a2fc-b572-3db5-b138-8a25ea4fb6bc | -5.76603 | -51.68557 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e99cd9a9-9984-3779-b09a-b373f92b09a6 | -7.61159 | -45.8475 | 2026-08-30 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6d86755-f273-32a6-af44-3a8cd045dfee | -11.5292 | -45.55853 | 2026-08-30 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9294f1e9-dc74-334d-9709-57b4b1e5dc25 | -11.19499 | -45.04688 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f8a367b-9150-3360-9d74-83eda08505e2 | -11.81899 | -51.05056 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| f05a2106-e4c9-3987-9889-cbac260ef0ca | -10.76722 | -50.65335 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 462ef1d8-5622-3753-8a8f-5c1ddd5d401f | -12.89479 | -45.87551 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c21a06a-93af-30fb-8c6f-68e48c6067dd | -7.04873 | -42.20081 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 51335b65-7c4a-3222-b978-a152e5689eca | -11.80114 | -51.05444 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 36.3 |
| e16657c3-ef84-357c-a986-18b2e898df48 | -11.53306 | -45.5592 | 2026-08-30 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad22ea83-cc23-3a8d-add9-f2704e9b88ec | -10.7542 | -50.69156 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1fd7ace-1803-3d02-a172-0dfe32b0fc61 | -9.41611 | -51.68764 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3cf36620-796c-338e-a82a-a6c2ec614635 | -11.48268 | -45.06253 | 2026-08-30 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af95dc89-4d92-3066-b84c-7cf270ce24ce | -8.6076 | -54.78048 | 2026-08-30 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ea4676a2-7022-33de-be91-d07a67825a47 | -7.04467 | -42.20399 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README28.md)
