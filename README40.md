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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 700e53ef-5b31-367c-80dd-652eee0f3137 | -7.8314 | -47.92319 | 2026-09-29 04:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3696882-3508-3f26-a789-881fb1b016e8 | -8.24185 | -45.43806 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b361618b-d1f6-3737-b5f3-d206738c9332 | -11.39052 | -54.03992 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8c479df-426d-3f6c-a464-9637af771657 | -12.31758 | -50.29173 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9f54a59-94b8-33cd-a183-697d5e996515 | -11.42217 | -43.44817 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7596e017-596b-3099-8a8c-0857a4cf7fe5 | -9.1457 | -49.96702 | 2026-09-29 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81eeecc0-73ed-393f-a1a3-56e33f397999 | -11.34691 | -54.11849 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 130db801-4bfe-3c4c-8130-53f442ccbdba | -11.6762 | -44.54441 | 2026-09-29 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00a3fb2f-f82c-3b58-8737-780d01a504a5 | -13.11345 | -47.40913 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4321b66c-3fa5-38e4-aaab-59e774cf89ba | -6.31323 | -52.62706 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 13deb100-af56-3d8b-92a7-b7a4b7441afa | -10.78736 | -48.807 | 2026-09-29 04:51:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e13b4b4-84fb-34a9-951b-b0f4a0f2e569 | -10.7891 | -48.75026 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66ecf75e-53a3-367a-916d-7ea5f189156a | -10.8124 | -48.73511 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 470e301e-50f8-348e-901f-2c49aaf40c8f | -12.02083 | -50.94411 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bebe04c9-0538-3b82-90f6-31bb6ce57b1a | -11.39383 | -45.40921 | 2026-09-29 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0f583565-a4cc-394d-949f-c0985d51cf52 | -10.12982 | -45.14333 | 2026-09-29 04:51:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 017c81e1-c0cc-3b29-a8c9-3a0d1474c384 | -9.09104 | -49.88601 | 2026-09-29 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a96e38a1-4cc3-3d58-a157-24a3586be594 | -11.95778 | -50.93747 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23d2d7aa-d590-39f2-a431-51eb3b9825ed | -12.87734 | -44.79826 | 2026-09-29 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f13d1ab6-b330-3be4-b98f-1abf84adca0b | -11.26155 | -43.532 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de9ca733-eb9a-347a-b441-3096bb283dde | -12.03082 | -50.94575 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b486345e-b718-38d1-97da-7494f1f89bad | -10.82155 | -48.72118 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f32e5f1a-e8b4-3f7c-a126-c22bd8223c70 | -9.95745 | -50.16156 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6ed41fd-b4f1-33c2-8c98-98d806ddefdc | -11.39409 | -47.45466 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f01427e-b968-3b92-aebd-f21ded090227 | -11.38774 | -43.45828 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd6f92f0-6ccb-3b97-9c97-a4b6c89459ef | -9.76435 | -36.98053 | 2026-09-29 04:51:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 96e9aced-bb99-30fe-b405-188a380f9d2f | -12.31424 | -50.29119 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0380b621-8640-34a4-8469-302217bbdbcd | -7.83048 | -47.92229 | 2026-09-29 04:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5780701-0e6c-3ea3-bdb3-8a61dbe3642f | -11.71652 | -44.50762 | 2026-09-29 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11f0a513-d511-3360-bc79-2cc52e9af4a6 | -11.38357 | -43.39631 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a2cc5f8-c3e2-3d86-b9ff-19df9396be2d | -6.9217 | -47.66843 | 2026-09-29 04:51:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 725c87cf-c4de-34d9-ac70-03cf0e104328 | -10.41093 | -53.82107 | 2026-09-29 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93baeca0-0adf-3622-b023-d1cc166fc9d2 | -11.70819 | -44.53626 | 2026-09-29 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 487f5bd4-2b39-36b4-98f7-1d37c03feb3a | -10.30874 | -47.5012 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ccd6aec-12aa-3ef5-bada-e246744f319f | -10.27987 | -44.62748 | 2026-09-29 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc26912c-fb07-3060-bcb2-6a9c76ed9d5b | -7.24623 | -45.26347 | 2026-09-29 04:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3e1d4d1a-933f-3b66-877b-74a6f2b32fbf | -7.47524 | -45.81213 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfdeae88-4f4f-3d51-aa94-5ccf6a051e76 | -9.77122 | -36.97431 | 2026-09-29 04:51:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e9c1f4e1-4e21-360b-ab21-7de02a07152e | -8.89973 | -48.58881 | 2026-09-29 04:51:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1710d3cb-382a-31ef-ad62-3970d7b79c82 | -12.59347 | -47.28201 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2247ec31-245f-3957-96bb-a2c4255e568f | -12.01695 | -50.94703 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dff1df46-220f-3db3-9355-5110d322532e | -7.49767 | -44.55355 | 2026-09-29 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa231a3d-dcd2-3f3f-9ab9-b3389bfef849 | -12.04643 | -46.50642 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0177c093-6b8c-324a-a46e-0d4a0d75a0a9 | -14.08879 | -46.31081 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4e192dbe-c83a-3614-8b43-83c0a175f28f | -11.36403 | -54.03977 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57232850-77ff-3163-930e-74f7319b346a | -8.65974 | -48.88307 | 2026-09-29 04:51:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dab27f49-8a42-3e4b-9cc8-1b03efcbf3e3 | -12.9041 | -52.06292 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9adf3f57-3740-3fb0-8651-f6099f57f6ad | -12.59515 | -51.96663 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d017f2f-930d-3c03-a57e-40f06950b822 | -6.67919 | -55.10926 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fd8038a-dffb-3629-ade6-0b8fd1e44bf8 | -9.96134 | -50.13701 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5dad193-61e5-3e86-93b9-2664dc864512 | -12.15602 | -50.41493 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8600b54d-7fa2-3301-bad5-c8ed09602f74 | -14.48357 | -43.25701 | 2026-09-29 04:51:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30981e70-3ca3-3d22-8824-9f6623f6d17e | -11.40487 | -43.43586 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8449712-462d-31f2-bfea-2afd6fe6485d | -7.27839 | -46.79262 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4d3d65c-75c7-31af-8548-b65d2942f1ef | -11.9053 | -50.60978 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d03d7fb-7a99-3ad6-a409-6712e5d3e628 | -11.17905 | -44.79816 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 267a7c65-74d1-302d-842a-91e8c076e397 | -11.08179 | -47.50566 | 2026-09-29 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b633fc7-be46-34d1-b353-07d718530d18 | -11.82792 | -55.21801 | 2026-09-29 04:51:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02d155fd-ecf6-3eaa-b120-0cd0f13438a5 | -8.3557 | -45.39746 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 975399ec-9942-3117-a8a3-2d1986a17df9 | -9.76641 | -44.82544 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 526e4e1d-260e-3a12-b8b4-db24fb05a697 | -11.08538 | -47.50626 | 2026-09-29 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b9e62ac-d646-3612-9997-f034b24fcc38 | -12.94338 | -46.66534 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6e69d22d-132b-316a-84c9-87ceb140e090 | -12.00237 | -50.99544 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9cc097ce-7496-3d7a-975a-8cdcc9fd9629 | -5.30979 | -55.8333 | 2026-09-29 04:51:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd899a30-3d6b-3fe0-891d-25c76db1af0c | -12.05026 | -46.507 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40aa2da3-c751-36b1-9459-9f93a59da68b | -10.78853 | -48.75397 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf783021-284b-30da-b556-f12890a2e86b | -11.38026 | -43.38584 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ccd997e-7262-379f-83f4-bd52185299d5 | -11.45074 | -43.48187 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4453ae66-f790-380b-bf00-5563dd75e7f1 | -11.39738 | -45.41341 | 2026-09-29 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8bf0e7e1-031a-37b3-9a8c-d163c50c5cb1 | -10.41019 | -53.82545 | 2026-09-29 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b077617b-8efb-31f2-87fb-6fb99519dfb0 | -12.0096 | -50.993 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53d0685d-e9b5-387d-bad1-6857ffba2744 | -7.51339 | -44.55984 | 2026-09-29 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8236403b-aee2-39d3-96ea-4dfa00809d58 | -5.72262 | -53.45481 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d61525f5-24d7-3b9a-af8b-50dde45a7b03 | -11.18774 | -50.05245 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b1d0875-ce59-3b4e-84fe-7fbc4455e7a9 | -12.73736 | -47.26543 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f54ac14f-25e1-3d8a-be3b-e7375154400c | -11.38093 | -43.38092 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2ad5b31-5d22-34b5-8aed-19e97362ac61 | -11.63393 | -54.99785 | 2026-09-29 04:51:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26c1201c-dfbf-3302-8533-a330a5c29f80 | -6.88746 | -52.47516 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9884ddc-e6d9-3e1c-8de1-65125f78e0ba | -12.87676 | -44.80252 | 2026-09-29 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3b28dc0-b7e2-369b-9189-5fe2dced4af9 | -12.04528 | -50.94088 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90c86408-fe34-3c1d-be4f-9abedad205cb | -12.03862 | -50.93978 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b81e3809-f109-3d8b-8db0-c8dd2bfd8770 | -7.51592 | -47.33757 | 2026-09-29 04:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 634fd3fc-9bc6-357a-99d7-c7a6246889a8 | -12.00832 | -50.94217 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a344185a-b2f4-33bc-a29c-cdcca835ede9 | -12.74218 | -47.28442 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 03d24e9e-f387-3ce4-9f06-800310080183 | -7.50582 | -44.55472 | 2026-09-29 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40a69ef7-616e-30aa-a335-5bdc0505ae54 | -7.6185 | -47.83445 | 2026-09-29 04:51:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ea2c486-6e87-34a4-b1cf-1824e225277a | -11.97337 | -50.92553 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d04b840a-ebe0-3dc3-b67f-f85fbb96f11d | -11.086 | -47.5021 | 2026-09-29 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82e35c64-e92f-3e4d-83f5-f3c4157d81c6 | -6.16435 | -52.91148 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c04865f-3d71-3ab3-b92d-7fd75a4ab63a | -9.28875 | -49.64523 | 2026-09-29 04:51:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08b2f0c0-200b-3d39-b4a5-b9761221d82f | -9.0755 | -49.87635 | 2026-09-29 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7749c59e-5024-3fc2-8726-553911ee0a25 | -11.33288 | -54.11145 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dfa5ace-d673-3bea-8b22-4c6408ddefbe | -12.75968 | -47.34555 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1c95d1a-ab33-3ea7-a2cc-1aab0b82c505 | -7.72248 | -44.57262 | 2026-09-29 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed236b1c-03c5-3677-b531-05d6fc3661ae | -7.38437 | -42.63383 | 2026-09-29 04:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7f1e1035-a6b3-3346-adf5-70b1f01a18d7 | -9.95746 | -50.13998 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3b21914-8671-3733-8b3f-558eeef7e195 | -6.91081 | -47.0074 | 2026-09-29 04:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5cedd93-c90b-3db4-9090-1ba111a9b1a4 | -11.05588 | -54.19548 | 2026-09-29 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4632667-a477-3d08-af28-fc257771baf9 | -12.24136 | -50.42839 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0df8dc6-639f-3c5f-bab0-04695716f8d1 | -9.10138 | -46.81802 | 2026-09-29 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README41.md)
