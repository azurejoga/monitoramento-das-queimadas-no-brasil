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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 108f12ff-908a-3314-b72f-403ab61da56a | 0.9761 | -59.3811 | 2026-03-23 00:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 2af0011c-b2a8-365b-80c3-09dc83676d5c | 2.6518 | -61.3015 | 2026-03-23 00:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d4dd8927-6110-3477-b371-18922156ae5e | 2.64122 | -61.30042 | 2026-03-23 01:24:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 233d649f-ea90-33c8-9097-afb6040215ab | 2.65352 | -61.30206 | 2026-03-23 01:24:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 5ba2152d-4ad1-3b37-9fe4-001e79eee060 | 4.02949 | -60.89216 | 2026-03-23 01:24:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0927d912-e112-387d-bb53-227b934a6fb1 | 3.24288 | -61.19537 | 2026-03-23 01:24:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0ad2337e-d247-3a62-865e-51c27c1c906c | 0.99171 | -59.38456 | 2026-03-23 01:24:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 216ba90b-68df-3e81-9a05-b63c50a87781 | 3.22786 | -61.21231 | 2026-03-23 01:24:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 93301ebc-f050-3550-82cc-fe7a0f4b2ede | 3.23036 | -61.19368 | 2026-03-23 01:24:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 22.2 |
| faaeecd4-f076-330b-8d29-b48d09601dfb | -20.1939 | -46.5023 | 2026-03-23 03:10:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e72b84bf-472b-371a-a82f-2d80d6b12615 | -9.81351 | -37.72711 | 2026-03-23 03:38:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 59d9695b-8f7a-3477-92d5-9c155b0a0b1e | -10.66284 | -37.12265 | 2026-03-23 03:38:00 | NOAA-21 | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7d0d5af3-8fa4-3083-855c-d01cb802f8a5 | -9.9419 | -36.10276 | 2026-03-23 03:38:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 31576075-1da5-37c7-bcf9-dabf79654ea4 | -10.65934 | -37.12207 | 2026-03-23 03:38:00 | NOAA-21 | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| a26f409d-5ba9-320c-a256-dd79491b7c80 | -11.16573 | -37.21702 | 2026-03-23 03:38:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2841c65c-27ac-3469-8fb1-cb591eedc3b0 | -11.16508 | -37.22097 | 2026-03-23 03:38:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2915ccb7-9f4b-31ba-ac84-7f432dd1b02e | -20.19251 | -46.51298 | 2026-03-23 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 77450207-68ae-3cb2-a2b1-f3e9f31eeea7 | -20.18645 | -46.51557 | 2026-03-23 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3ee75d3c-05d0-36c1-847b-f63ce920b142 | -20.1811 | -46.51488 | 2026-03-23 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ef461814-7bd6-3c8b-b4af-b52309f03890 | -20.18036 | -46.51833 | 2026-03-23 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1a3d1439-aa17-360c-9347-80d45834ebeb | -20.1918 | -46.51634 | 2026-03-23 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 50d46b4f-a332-368b-b00f-ef9d55e7e938 | -20.19855 | -46.51047 | 2026-03-23 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23fb1145-7d37-3c2f-a5bf-d22233955f99 | -20.19783 | -46.51387 | 2026-03-23 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1a65082-e3d4-395a-ba0d-2394303feee3 | -20.18184 | -46.51139 | 2026-03-23 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e09b75b5-47ef-342b-ba09-2dce5cf33d8a | -20.18573 | -46.51892 | 2026-03-23 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 87012ece-ee90-30b1-812e-08bff33c5ab3 | -20.1939 | -46.5023 | 2026-03-23 03:50:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 72.7 |
| b3abd821-6d63-35df-ad5e-5ff9e99e6819 | -20.1939 | -46.5023 | 2026-03-23 04:00:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 8644b296-2f54-35d4-847c-efba18ab057d | -4.22689 | -38.06717 | 2026-03-23 04:06:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0c27b747-5d86-305b-99c5-98a926ddfcbd | -9.81196 | -37.72954 | 2026-03-23 04:08:00 | NPP-375D | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6c1560dd-b9a3-371a-8f2b-5694847cea4a | -10.65863 | -37.1239 | 2026-03-23 04:08:00 | NPP-375D | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 91743066-6067-336d-970f-63f81b9a85e9 | -5.44686 | -46.1387 | 2026-03-23 04:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac50d5bc-c4eb-3f2a-a918-eaf5bee31381 | -10.65929 | -37.11942 | 2026-03-23 04:08:00 | NPP-375D | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9304160a-dd92-3626-a4db-597ae460ad5a | -10.66235 | -37.1245 | 2026-03-23 04:08:00 | NPP-375D | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 890c2aca-3061-3dab-aaa0-09f63f9f1b56 | -5.44827 | -46.1398 | 2026-03-23 04:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6d8a5f2-4544-3d4d-8e3b-e37d2d3d5f57 | -20.1939 | -46.5023 | 2026-03-23 04:10:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 63.3 |
| e4d267ca-8420-3bf0-ac60-aca487d304ae | -12.63446 | -52.14689 | 2026-03-23 04:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb8b9330-7afb-377d-a780-fee0b106d995 | -12.63529 | -52.14272 | 2026-03-23 04:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c46802b5-82e6-328b-ac58-9efafc4fda8b | -20.18405 | -46.50842 | 2026-03-23 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b061a4b-79d0-3574-88df-65d01e940104 | -23.93947 | -47.05436 | 2026-03-23 04:12:00 | NPP-375D | JUQUITIBA | SÃO PAULO | Brasil | 3526209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 935072cf-b771-3144-a492-255c69f9eeeb | -20.1817 | -46.52169 | 2026-03-23 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 7127bcec-e2a2-330b-9fb6-a9585d5ce6cb | -20.17964 | -46.51222 | 2026-03-23 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3132557f-ac3a-3e7f-bb72-eedb3b495a1d | -20.18612 | -46.51785 | 2026-03-23 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c594c7ed-7ea1-348b-9ac5-fbf42859f792 | -20.19053 | -46.51409 | 2026-03-23 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6b63825c-d186-3307-892b-fe3d1e4faafa | -20.19856 | -46.51097 | 2026-03-23 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a784032e-1d5f-39be-b6c2-9131861c26eb | -23.59302 | -46.43123 | 2026-03-23 04:12:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a19d6ff8-9670-36c3-bf02-924c5055fc85 | -20.18976 | -46.51847 | 2026-03-23 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 75cde1c6-6f98-3ee2-9141-b7c1e0fc62f4 | -22.99343 | -49.85142 | 2026-03-23 04:12:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 8a8e850f-c0ce-3f26-a5da-580a219ec1b3 | -20.18249 | -46.51727 | 2026-03-23 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3613c5cb-b83b-34df-9143-67fd50d7eadf | -20.18327 | -46.51286 | 2026-03-23 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d7d26b5a-2b70-3d83-b606-41c0db97cd75 | -20.20219 | -46.51163 | 2026-03-23 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b86f96b8-66b9-3496-a002-f03fc6280c96 | -20.17885 | -46.51667 | 2026-03-23 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd183342-06a8-377d-b8eb-a5722bfeedf9 | -20.18534 | -46.52227 | 2026-03-23 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 32.5 |
| f26b34a6-12c2-3b6a-a804-cd86ba2a7abc | -20.19778 | -46.51539 | 2026-03-23 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28ae0d11-c84f-393d-9868-5ac560121133 | -20.19416 | -46.51471 | 2026-03-23 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1f75f20c-c482-3cd4-ab84-df4d42fd9044 | -22.99426 | -49.84728 | 2026-03-23 04:12:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 808c0ae9-4294-3a81-96cb-8a0b0221a704 | -5.44775 | -46.13911 | 2026-03-23 04:27:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4040ba1a-5eaf-3bac-8066-9c52c0e2b2f4 | -1.55755 | -54.01111 | 2026-03-23 04:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66c498e0-a06c-3060-a20f-35cf3546b002 | -12.63713 | -52.14013 | 2026-03-23 04:29:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 429138e7-25f3-3824-aba5-7d2aa2d2e161 | -20.18912 | -46.51848 | 2026-03-23 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4db0dff4-9b5e-384e-bbe6-a8c4affdea45 | -20.18496 | -46.52213 | 2026-03-23 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd115798-fc9f-3979-808c-edf66865269d | -20.17845 | -46.51645 | 2026-03-23 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 974f22f5-72dd-3c25-8827-bdc931353044 | -20.18141 | -46.52144 | 2026-03-23 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 26.2 |
| e2880b07-5555-33f9-a487-993715d1daed | -20.18973 | -46.51411 | 2026-03-23 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8b668ca-21fa-39ee-8464-a7e1d9952c36 | -20.18557 | -46.51781 | 2026-03-23 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26eaff13-9db6-3e1a-bfe7-4edfe8f962e6 | -20.19214 | -46.49682 | 2026-03-23 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8add9bb3-6060-3ce4-9b94-b6f5081167cf | -20.20103 | -46.51168 | 2026-03-23 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d75b2670-5c78-356a-b237-4396fb56dcea | -20.74648 | -51.66232 | 2026-03-23 04:32:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9d49d90b-4986-3163-9096-01451b06c440 | -19.78047 | -49.77208 | 2026-03-23 04:32:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f3c4068-d0c7-35b9-92ee-f08c447644d1 | -20.18321 | -46.5085 | 2026-03-23 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad5e4b09-121c-353e-82a1-c40e27b29d8c | -20.19746 | -46.51106 | 2026-03-23 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2dd83480-29ca-3d59-bc7c-323c888933ef | -20.19329 | -46.51477 | 2026-03-23 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aecfde5f-9c1e-31f9-a2c8-181524ec05d7 | -20.18201 | -46.51712 | 2026-03-23 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fc56d49d-3fd4-3b55-875a-42f3a6d0560c | -20.19686 | -46.51539 | 2026-03-23 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 732e69a8-b037-304d-b890-410c3bd19f76 | -20.17786 | -46.52073 | 2026-03-23 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 26.2 |
| ec8965ff-c8ab-3b6c-9f5e-388052dc61a7 | -20.18261 | -46.51279 | 2026-03-23 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bdf1952a-e160-3e4d-aba1-2aef5454c3f0 | -22.99542 | -49.84565 | 2026-03-23 04:34:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 7f7bedd2-3d68-3a21-b3de-f00a44d4ff30 | -22.99484 | -49.8494 | 2026-03-23 04:34:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| e2c76f4d-15a0-314d-930b-a4e58d7c06a3 | -25.65392 | -49.32532 | 2026-03-23 04:34:00 | NOAA-20 | FAZENDA RIO GRANDE | PARANÁ | Brasil | 4107652 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 881d23e0-e620-3b17-b754-50c857121cee | 0.54743 | -60.25727 | 2026-03-23 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ca53bf2-b1b6-3906-b88b-fc8a083f0990 | 0.5445 | -60.26182 | 2026-03-23 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8978587f-442a-368d-b8c5-3012ea964af5 | 1.72833 | -60.54705 | 2026-03-23 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2a327aa9-a587-3ec8-a123-e10abc589857 | 4.37707 | -60.7651 | 2026-03-23 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 41f02207-8991-399b-8c18-cf4ad3a9a4c1 | 2.94771 | -60.74698 | 2026-03-23 05:16:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9e8f0f1-8813-3cc4-a520-6fcd7b947ac8 | 2.64125 | -61.30239 | 2026-03-23 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 58751279-f0de-38e0-a3bb-94565596acf6 | 1.08677 | -59.24052 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d2a9086-95d2-3ead-9f00-a3120c35fe52 | 3.54352 | -61.81529 | 2026-03-23 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80a0066a-dd6c-3750-b9b1-8997df3e35ba | 0.73676 | -59.60765 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22908436-aaa9-38de-999b-058f2400e6c5 | 1.97183 | -60.57053 | 2026-03-23 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10c68b1d-6188-3ec1-8985-057e4539e746 | 4.37789 | -60.76346 | 2026-03-23 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 575f8c2f-35db-3c9f-a76e-de4255c5d3eb | 0.98942 | -59.38051 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da34285d-7264-37b8-a417-1e175e662520 | 2.64439 | -61.297 | 2026-03-23 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 242e547e-0198-351e-b8b8-29fd78d93195 | 0.57674 | -59.90961 | 2026-03-23 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32f0c399-0617-395a-baef-c3f3c883cf11 | 1.91576 | -60.81501 | 2026-03-23 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fe91063-7ccf-3ce3-840b-bed5efce5cf5 | 4.94139 | -60.34258 | 2026-03-23 05:16:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fdcc64c-3f76-3ee2-a430-be50a919c89f | 3.53488 | -61.8129 | 2026-03-23 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d618ace6-ce2c-3b53-84b9-8ba142b90963 | 0.78059 | -59.8678 | 2026-03-23 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 984c729e-50ca-3be1-a76e-b0d86180dad6 | 1.70305 | -60.4339 | 2026-03-23 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cd88bc09-3971-3ead-b52a-94dec7a705a7 | 1.97795 | -60.51252 | 2026-03-23 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43e03be6-ca19-36ce-8ee7-fc9432f52be6 | 2.64752 | -61.29163 | 2026-03-23 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 040fc6d9-d1ff-3500-b4e2-f09db293598e | 1.11449 | -59.4384 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README2.md)
