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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b880f29c-1428-3440-b765-4e3ef87a1f47 | -12.27248 | -44.60334 | 2025-06-19 03:32:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2bd87bae-dba1-3375-8e7e-d1869173963e | -12.40003 | -46.36509 | 2025-06-19 03:32:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aabb8c29-190f-3194-a1d6-4f5485e4ee02 | -14.21092 | -45.52114 | 2025-06-19 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 518a8d4c-5157-314f-a208-aa3defde9ded | -22.67607 | -42.85614 | 2025-06-19 03:34:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 89cc15b2-5bd8-3f5b-bde0-794eecce46df | -20.94155 | -47.42962 | 2025-06-19 03:34:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f8f368f5-213e-3601-8b5c-1a777d43890d | -20.94267 | -47.42487 | 2025-06-19 03:34:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42e3af27-2ddd-3ca1-a34e-8043c445d663 | -21.09133 | -48.68608 | 2025-06-19 03:34:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1ee9ce1b-0624-3255-8ec9-2b7aca2ea71f | -19.86701 | -44.95486 | 2025-06-19 03:34:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f6ea8fa-2c84-38f7-9a34-a4aa3297650c | -22.55466 | -42.20525 | 2025-06-19 03:34:00 | NOAA-21 | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| e417770d-aec6-31a6-ac88-ebd2e2adb991 | -20.94581 | -47.42983 | 2025-06-19 03:34:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ff1ac45-2cc8-3b2e-a2dd-afbfd9ed742b | -19.86761 | -44.95663 | 2025-06-19 03:34:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21fcc059-34be-3f04-988c-4ef64906803c | -20.93976 | -47.42878 | 2025-06-19 03:34:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 467fd7a2-771a-3b02-9ee2-9f3d50c6d09d | -17.70316 | -46.30401 | 2025-06-19 03:34:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0c22008-0f1f-3c10-a7e5-522c22cd3d54 | -21.6685 | -41.94792 | 2025-06-19 03:34:00 | NOAA-21 | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4316416e-e276-3301-986f-8c1dd861f9c3 | -18.06178 | -44.49247 | 2025-06-19 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b0d018e-57e4-3fdf-af01-e2f749b5b430 | -19.86627 | -44.95828 | 2025-06-19 03:34:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f342a3b-8ba7-31e2-a8e5-f79fa2872ae4 | -22.54056 | -48.81499 | 2025-06-19 03:34:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ffd58c19-dd7d-3943-98e7-26099d21b1d6 | -17.70726 | -46.30193 | 2025-06-19 03:34:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a90dd723-224e-3209-b557-5ef36d37dbda | -21.09094 | -48.68416 | 2025-06-19 03:34:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 0a480b53-c25b-3991-a915-48ce7c51da60 | -18.06105 | -44.49599 | 2025-06-19 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4d547f3-62cd-368e-8cdf-d7efcb349e94 | -7.2405 | -43.0899 | 2025-06-19 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 55cbe6a2-7a34-3410-a8f7-bc5d3d797853 | -11.9707 | -58.756 | 2025-06-19 03:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 5075009c-ed27-32b7-ba99-b5c55d2e2293 | -11.952 | -58.7376 | 2025-06-19 03:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 2a9784ad-cfec-354b-80af-e6a1ec152427 | -7.2408 | -43.0664 | 2025-06-19 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 57.1 |
| 7fad25da-79cb-3303-a2eb-486483a80c13 | -11.9709 | -58.7362 | 2025-06-19 03:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| fb5a2f35-5b44-3d0f-ab97-688f97bf1f82 | -11.9518 | -58.7574 | 2025-06-19 03:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 38786faf-1070-3cb0-b95f-60f5e11db17c | -8.0703 | -43.0981 | 2025-06-19 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| ca87859c-4629-341e-8788-a467140f669d | -8.07 | -43.1216 | 2025-06-19 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |
| c9b046e6-4384-3500-b321-3d6b856c4af5 | -8.07 | -43.1216 | 2025-06-19 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 0a24b5ae-d9d2-379f-a06a-741991766118 | -11.9518 | -58.7574 | 2025-06-19 03:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 122.9 |
| c9bf8531-3b8b-3ecc-8232-92480b392aab | -11.9707 | -58.756 | 2025-06-19 03:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| c2d9363b-4236-3bf7-a264-cac952667aa7 | -8.0703 | -43.0981 | 2025-06-19 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 84c1f170-69aa-389f-bc41-78e3c3f8886d | -11.952 | -58.7376 | 2025-06-19 03:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 0abf10ea-5477-354c-85c1-3e21b0b46101 | -11.9709 | -58.7362 | 2025-06-19 03:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 3ebacde6-7e6d-32fc-9b23-b57f4f6a3950 | -7.2405 | -43.0899 | 2025-06-19 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 8f1b9ae5-fa39-3515-97b0-1628fb2c1639 | -7.28927 | -47.10165 | 2025-06-19 03:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d01f8060-ebfa-33e9-b224-9c6d63556be1 | -6.66801 | -42.4731 | 2025-06-19 03:55:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a0a5f62e-12e4-3289-83e4-6d58d7b98982 | -4.28086 | -48.18702 | 2025-06-19 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7ecc3f7-fbe8-30e6-9459-2335fc20010e | -7.24273 | -43.09373 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1a220c6d-045d-3dea-b3a0-a6817607fa13 | -5.91251 | -43.45415 | 2025-06-19 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68343e58-33da-3d5b-9d5c-647e31b73b62 | -7.22962 | -43.07628 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c22232d6-cb6b-3da4-a4f0-4b80a6fbe649 | -7.23491 | -43.09241 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 00ebc1d8-573a-3dc5-b8c0-e76743a72be6 | -7.27968 | -47.09618 | 2025-06-19 03:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f0e5511-7fc9-3bc2-913e-e4ebd8d8dc69 | -4.84733 | -43.18617 | 2025-06-19 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f16f6fca-df1c-32f9-b419-1fb027da2bee | -2.73903 | -47.33716 | 2025-06-19 03:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2e0fceb-4a6e-395c-9f92-235630b882ab | -5.45111 | -43.57873 | 2025-06-19 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69ac02f5-b405-3e07-a2b1-950fd26dfbc4 | -4.83568 | -43.18063 | 2025-06-19 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 093ca64a-58f5-3fb8-a26a-33ab6405d48a | -7.23575 | -43.08749 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 52c4ab23-9659-352a-b40d-d704d4cd1648 | -7.24357 | -43.08878 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 12f727d9-dcee-30c7-b17c-900a88c99c66 | -7.28126 | -49.99272 | 2025-06-19 03:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10cea20a-6c66-3f0a-b981-4b9935424ad0 | -5.29066 | -44.72187 | 2025-06-19 03:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3377024e-555e-3130-be5c-50bce60ac760 | -6.68977 | -43.21196 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9c8c7e60-a487-3faf-8229-33794b88f892 | -6.68843 | -43.19571 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3a40a4a0-77a1-3901-b403-24b5b6f5f35a | -8.0692 | -43.11194 | 2025-06-19 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| e51f79b4-2568-3176-a89a-76543812bd3e | -7.24441 | -43.08382 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| d72f1547-fdef-3e88-8356-c76af7b17a85 | -6.8422 | -42.80323 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 028b69d5-7683-3cf8-9864-5154cf702dff | -6.37023 | -43.65607 | 2025-06-19 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a63d48c-47e8-32b4-b3ab-4deff238205c | -8.07387 | -43.10778 | 2025-06-19 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.2 |
| b67274ab-fa1d-34ab-9e03-6445269175c8 | -7.17214 | -43.20746 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8e4a754f-4ba8-33d4-b5a6-96e934a40c82 | -4.55458 | -48.00848 | 2025-06-19 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac05512c-e26b-3ddb-8d74-d2a633eeecd5 | -6.66649 | -42.4824 | 2025-06-19 03:55:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 47ae871c-25df-36b9-b6eb-63858ece4f2b | -8.12888 | -43.13894 | 2025-06-19 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0b2a620d-2ab6-35cc-ac0d-dbb40fcc1824 | -8.07773 | -43.10847 | 2025-06-19 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 3fff0f88-fcd7-36ee-baab-eaa51b3aba54 | -6.68756 | -43.2009 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d37af495-fd4b-36a5-bf1c-4b73bbd2a616 | -2.91142 | -48.23698 | 2025-06-19 03:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 48748d89-9836-386c-85e8-665afe068ac2 | -5.77393 | -43.46137 | 2025-06-19 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d2e8ed2-cc2b-3db0-bf65-9210cfae4a90 | -6.68183 | -43.21059 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 88a4505e-7d98-36bc-b36c-83d0bdc918a1 | -7.16735 | -43.21187 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 941e049b-12ff-34cd-b258-541245800374 | -8.19553 | -47.15915 | 2025-06-19 03:55:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 517aa8a9-f8f5-36cf-a392-2996c2fbf5b6 | -8.07307 | -43.11261 | 2025-06-19 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 436d6568-01a7-3280-9a3c-f0e14bcd8826 | -4.84673 | -43.18975 | 2025-06-19 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 335f9295-55b9-301a-a6af-09f1f0197b98 | -8.12623 | -46.08908 | 2025-06-19 03:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e46eadd4-fee2-397d-aad9-8e4282168f2d | -6.6858 | -43.21127 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4291d9fa-6f82-3a48-8417-0caa1344453b | -5.9119 | -43.4578 | 2025-06-19 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c66e222-d83c-31fd-a320-5fefa9ace810 | -7.23268 | -43.08187 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| c40269cd-2ca0-3514-984c-bb579ae3ee6d | -7.28141 | -47.10063 | 2025-06-19 03:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcb20a5b-3189-36d0-a4b8-863e30174b11 | -8.1271 | -46.08425 | 2025-06-19 03:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46122139-0776-31db-b618-6fb5c567de0e | -8.07885 | -43.10557 | 2025-06-19 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| aeb26a86-4f52-3930-beeb-848311848c54 | -5.90782 | -43.45708 | 2025-06-19 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4a4645b-346c-3514-b29f-effd8f6e42c9 | -6.66942 | -42.47989 | 2025-06-19 03:55:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3e61582e-f3f4-3c48-b729-3ebc9dd6096a | -8.12153 | -46.08827 | 2025-06-19 03:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 184beae1-b551-3c90-b7fa-ff7da0714255 | -8.12583 | -43.13346 | 2025-06-19 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 7ea180b1-e9a2-3333-b562-36b331cd0f2d | -8.06614 | -43.10644 | 2025-06-19 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| a3055286-33c9-3b6b-8fcf-78c538d43872 | -4.55523 | -48.0046 | 2025-06-19 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10e411b7-1580-3a45-bb5e-897eb8bdfb5a | -7.54085 | -43.80741 | 2025-06-19 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92566087-b0ef-3722-9221-cf97807e39f8 | -6.66268 | -42.48183 | 2025-06-19 03:55:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cbce9489-ea7e-3d8c-b5be-47b0c789d379 | -7.2405 | -43.08318 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| ace20588-b00c-30f2-82b2-92f1bbb32b0d | -7.28208 | -49.99678 | 2025-06-19 03:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92a4175a-5d19-3744-b7ee-29f527f9188b | -5.8446 | -43.49209 | 2025-06-19 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bd7a0af-7bf1-3cfb-8be1-c322b9f32bf7 | -4.84325 | -43.18551 | 2025-06-19 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7259fa24-1140-3ad7-8552-8ddd905a7c5f | -8.19047 | -47.15829 | 2025-06-19 03:55:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 158aa794-bac0-38aa-8aa9-49a68952f109 | -6.33849 | -43.74582 | 2025-06-19 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86dd48fd-76a5-34e1-880c-5af87da0a4dc | -7.1634 | -43.21121 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ebf82599-0674-37da-84d7-331b1014958c | -4.55077 | -48.0086 | 2025-06-19 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f544e3d5-4b34-3bd7-afa4-157324ddff63 | -6.68668 | -43.2061 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b94251dc-4306-36ee-a3e4-3a5aae781c31 | -5.13508 | -37.84566 | 2025-06-19 03:55:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c8279751-1101-3cb1-9b8a-f427ef962f11 | -6.32357 | -43.75883 | 2025-06-19 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44c13a83-94fc-3932-80f3-9ddd34f35852 | -6.68095 | -43.21573 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f1174053-d9b1-31c5-9a30-ea4227cc804c | -6.91388 | -43.58501 | 2025-06-19 03:55:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dffd125d-24bd-3dc6-9522-d5f96b63b48d | -2.87545 | -40.38363 | 2025-06-19 03:55:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README9.md)
