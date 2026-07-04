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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 856e19c7-3b1e-3a27-a29e-df9be6e0ff0e | -18.13323 | -46.4611 | 2026-07-04 04:49:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f6ac1e8-5ec0-35b7-b7fe-a45d921adeb3 | -13.23319 | -54.38806 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b4c83d9-8586-3b86-804f-56bae83dc77d | -18.71967 | -47.53988 | 2026-07-04 04:49:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f0c97d6-1fdb-382c-8cad-6bd603857e5c | -12.67645 | -48.22231 | 2026-07-04 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb3f512d-fe04-3ccc-9ff5-45d8ee3a4476 | -11.63207 | -59.01542 | 2026-07-04 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6f85434-4851-3b28-86f0-51948280ef95 | -13.44331 | -43.85649 | 2026-07-04 04:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7125935b-d526-3887-bfee-21501597f559 | -13.23504 | -54.37676 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51032fcd-9b42-3f52-83de-564563c04e0f | -13.23996 | -54.34671 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 8b52a5ab-43e7-3e1c-bbe7-e2b63c3cba01 | -13.23778 | -54.33867 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 44afbb2d-0051-344c-a049-3ce7d52ed2fa | -13.25696 | -54.34954 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7b0623e7-e602-3e82-8e69-418471c4704a | -13.24798 | -54.34035 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 2c64333f-1108-38c9-bab1-2059f33fa21f | -11.62756 | -59.01458 | 2026-07-04 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96808b0d-f5be-39ff-b015-b4d366ec735d | -13.25478 | -54.34148 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fb36c42c-c61f-3cca-87ba-a132a64d229e | -13.23287 | -54.36866 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4702173f-9366-3325-ab07-ddb75f7b7cd2 | -13.25417 | -54.34523 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 33d0b1c9-2dc5-3090-a009-ed5997e3c198 | -13.23195 | -54.39562 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afed658a-7e07-3158-b5a2-d9636f1173b9 | -11.40742 | -57.81376 | 2026-07-04 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df147eaa-620a-33fb-b5f0-e653f2d5a407 | -13.22917 | -54.39126 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 143131af-b546-384d-9f70-f7fe19aedfb9 | -13.22976 | -54.34498 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d61e8155-1ca2-3ddf-bbf1-ac8d53d5d56c | -13.25016 | -54.34841 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 90b6f063-0c4a-376a-8d1d-10eb7e4fffb6 | -13.22855 | -54.39505 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f523d8f5-c4dd-30c8-891e-9d19e9d45a57 | -13.22636 | -54.3444 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0eb4a21f-ce77-33f8-8831-c7af5300dab1 | -13.25635 | -54.35328 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ed6ad039-ac17-3cde-a8d1-d8e09234ec8b | -13.24737 | -54.3441 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c83b93d3-4499-3a82-aa4a-5d70a756bf36 | -13.22947 | -54.36808 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8963138f-7cdf-39d2-8e94-39a7c0b2ec5e | -13.24118 | -54.33923 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0c6288fa-b3b2-3e5a-adb6-42575daa9957 | -13.23225 | -54.37243 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e41d42bd-aa01-3caa-a5a4-721b98b98e46 | -13.23595 | -54.34987 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| b1944faf-4808-3ea4-9822-08a721f758ac | -13.24615 | -54.35159 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 23b6235a-9a8c-37ed-a3cd-29c1bab3b320 | -13.24458 | -54.33979 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7d6a6d61-6cb6-37b1-adcc-ba925efaf0e6 | -13.24648 | -54.37095 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 239c7738-149c-304b-8beb-26bb348d1d22 | -13.25757 | -54.3458 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ed7103f5-d90d-3b15-b82b-3e4eb8cfc8c4 | -13.22453 | -54.39824 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ea04714-559f-3c61-9f4a-970598011c62 | -11.40628 | -57.81412 | 2026-07-04 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f9ae1c64-116e-34b4-a081-ed979d976d01 | -13.23566 | -54.373 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c7a9ad1-694a-32b7-a507-1d4fbeca70f1 | -10.9401 | -43.0355 | 2026-07-04 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 227.3 |
| 8b5fb256-53cd-3bde-8cfa-2df700f82c70 | -11.4337 | -46.5743 | 2026-07-04 04:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| e62c6ab7-6e7d-366a-bcb1-d16819d5ab7e | -10.9205 | -43.0622 | 2026-07-04 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 3c68df1e-f200-3a81-963b-72f95377cd73 | -12.7553 | -44.5194 | 2026-07-04 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| ef9a0cd0-8edc-3631-8bc1-baec8325f40c | -13.2209 | -54.353 | 2026-07-04 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 868c447d-99b9-342a-a4fa-b923b011e07d | -13.2212 | -54.3324 | 2026-07-04 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| b70e56dd-8943-3d12-bb52-4a9f05737ae6 | -13.2592 | -54.3489 | 2026-07-04 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| d7484315-79b9-3d06-b088-06a702eea795 | -10.9209 | -43.0384 | 2026-07-04 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 238.9 |
| b90325f7-857f-3a56-9e8f-cc92143c619f | -10.9397 | -43.0593 | 2026-07-04 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 177.8 |
| edc93753-6a5b-3b40-ba11-6d8813905939 | -12.7544 | -44.5662 | 2026-07-04 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| ddaf82c5-a367-3b2f-881e-410c8a0de6dd | -13.2401 | -54.351 | 2026-07-04 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 304.3 |
| 46a74208-0277-359b-9c0d-9a1832875fc8 | -12.7741 | -44.5396 | 2026-07-04 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 6cf083cf-aa87-36c5-b692-6a5d1f903625 | -12.7548 | -44.5428 | 2026-07-04 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 292.2 |
| 37343c76-caed-30b4-9893-50ffffce0e36 | -13.2404 | -54.3303 | 2026-07-04 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 162.2 |
| db269446-9774-32ed-9e1f-15267c81c7a6 | -21.90191 | -48.48953 | 2026-07-04 04:51:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62e82362-e3b7-39fd-bfc5-e12827d7cbf3 | -20.3937 | -46.56575 | 2026-07-04 04:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45742d23-331d-3ee1-b097-17db75d44a94 | -21.88091 | -55.81333 | 2026-07-04 04:51:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54adb1ec-b397-3427-95a7-1bf6ef3d79eb | -20.39423 | -46.56098 | 2026-07-04 04:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea2ab0a7-6f50-37b3-91d8-3120b295e9f0 | -20.71113 | -50.5303 | 2026-07-04 04:51:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9bc271dd-7032-3317-bcfd-f49784995290 | -21.20598 | -48.59784 | 2026-07-04 04:51:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f605ce8c-0ac9-3085-877b-bca6fb09c8ed | -20.70744 | -50.52977 | 2026-07-04 04:51:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 85cf7d7d-6c37-3692-8c6f-251592ea6191 | -20.4447 | -43.52962 | 2026-07-04 04:51:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 946cf55a-01bf-31dd-874a-502c47edb424 | -20.32731 | -45.38991 | 2026-07-04 04:51:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6760303c-54e0-3059-ac0a-425d6e600864 | -20.76667 | -48.56988 | 2026-07-04 04:51:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b56672a2-a60b-39c8-bcca-5deed1e29bc3 | -21.11147 | -49.00126 | 2026-07-04 04:51:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ba56fcdd-243a-31db-897b-357a2b62724f | -22.09746 | -50.23314 | 2026-07-04 04:51:00 | NOAA-21 | POMPÉIA | SÃO PAULO | Brasil | 3540002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 626d079b-f8cd-39d0-b557-64f89be4fb7c | -21.43201 | -48.64687 | 2026-07-04 04:51:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df0a3fd9-c35e-3a58-932f-3c36b0a2a79b | -21.72474 | -46.38948 | 2026-07-04 04:51:00 | NOAA-21 | BANDEIRA DO SUL | MINAS GERAIS | Brasil | 3105301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1bc56b28-e999-3cfc-879a-f04030d05b12 | -20.44839 | -43.5291 | 2026-07-04 04:51:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6f353711-68ee-3c5d-bda9-942b81e3edbd | -21.2055 | -48.60188 | 2026-07-04 04:51:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 83229d66-f7b3-3093-ba36-e74ce28fce14 | -20.44112 | -44.85984 | 2026-07-04 04:51:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e020bff5-f5a8-3774-9d88-c6c368063037 | -19.00018 | -49.76813 | 2026-07-04 04:51:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afe40e7c-823b-36c8-8542-fc8cf6864a32 | -19.51685 | -52.74226 | 2026-07-04 04:51:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfa9264a-417f-3aed-9a9e-9e953ecc192d | -20.71176 | -50.52565 | 2026-07-04 04:51:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fcb14eb0-28b2-3568-b340-72d044386e00 | -20.71422 | -50.52875 | 2026-07-04 04:51:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b135475e-6d0e-320a-8199-93a6a16181e4 | -19.5135 | -52.74172 | 2026-07-04 04:51:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8844f73f-93a0-364f-aa28-4e43854ed701 | -10.9205 | -43.0622 | 2026-07-04 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 8af7db98-e707-31b1-9709-20fe75ba517f | -9.4391 | -40.3171 | 2026-07-04 05:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 63.7 |
| a3444a42-07ea-31cf-ae11-ad05c41a1bd2 | -12.7544 | -44.5662 | 2026-07-04 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| f27167aa-091b-3b97-9995-65ab189966d2 | -10.9397 | -43.0593 | 2026-07-04 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| ceed9f0a-0cf1-3c06-a778-5dab7938d1c8 | -13.2404 | -54.3303 | 2026-07-04 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 144fd8cd-ae44-3797-9366-e7b8d1db0762 | -10.9401 | -43.0355 | 2026-07-04 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 233.7 |
| 6cb26801-8749-3556-9809-494859974873 | -12.7553 | -44.5194 | 2026-07-04 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 15fea345-4354-31a8-9de5-74c9f94014f6 | -10.9209 | -43.0384 | 2026-07-04 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 752e852a-6b36-39ac-8407-56b8d2032f9f | -12.7741 | -44.5396 | 2026-07-04 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| a78b8e9d-1e7f-3da9-b8e9-91aed27dbcd2 | -13.2592 | -54.3489 | 2026-07-04 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| de7fc990-bd27-3bd5-9298-c8bbec6cc088 | -12.7548 | -44.5428 | 2026-07-04 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 308.0 |
| a761aeb0-2104-3ce8-954c-d318da7c652d | -13.2401 | -54.351 | 2026-07-04 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 87bdd9ec-d5eb-3a81-af00-1a24bdb50a15 | -13.2595 | -54.3283 | 2026-07-04 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 80c89785-2c96-3939-9168-49af1607ac3d | -10.9205 | -43.0622 | 2026-07-04 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 06622116-d593-3a30-a3e2-b51e6178a3a2 | -12.7553 | -44.5194 | 2026-07-04 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 2b176663-60a8-3a08-8143-4c3324c199d9 | -13.2592 | -54.3489 | 2026-07-04 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 7f867a3f-8f81-383d-b2ef-605a4cc74e93 | -10.9209 | -43.0384 | 2026-07-04 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 84462d41-cdd9-321f-9eab-f5c500bd53c4 | -13.2595 | -54.3283 | 2026-07-04 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| ead24515-3183-3e69-92aa-cbbc9eb1b261 | -9.4391 | -40.3171 | 2026-07-04 05:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.7 |
| 1e85a14a-4029-3342-93ec-c2ede5e8d848 | -10.9401 | -43.0355 | 2026-07-04 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 238.3 |
| 16cf8d5d-01ca-35cf-9e6c-92674bacc26b | -12.7548 | -44.5428 | 2026-07-04 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 246.5 |
| 4ec0f694-2111-32a2-9bc7-b30e01487294 | -12.7741 | -44.5396 | 2026-07-04 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| fa9ec449-61ed-33e4-a3f4-a55a5bdd38ef | -13.2401 | -54.351 | 2026-07-04 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 945e8282-1f27-3a60-aa83-53ffb49f82f8 | -13.2404 | -54.3303 | 2026-07-04 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 7e965f89-a1ea-3fdf-b46b-3f4b3820b960 | -10.9397 | -43.0593 | 2026-07-04 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 05f558e3-fac8-303b-8467-3d0d9c75888b | -10.9397 | -43.0593 | 2026-07-04 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.4 |
| ccf99039-bb5b-3d24-aca1-e020939b2920 | -13.2401 | -54.351 | 2026-07-04 05:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 284943de-2c9c-3379-bf2e-1cc0349015fa | -13.2592 | -54.3489 | 2026-07-04 05:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 76ba3843-a43e-3e4f-902f-13c17beb9418 | -13.2404 | -54.3303 | 2026-07-04 05:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |


[Clique aqui para ver as próximas entradas](README17.md)
