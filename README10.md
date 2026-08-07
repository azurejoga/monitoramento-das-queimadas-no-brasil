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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b98a9131-d765-3f5f-9207-cd8c726f3d60 | -11.1493 | -44.49218 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fe78b99-cef9-3d1e-bba7-b2c57c1dfcf1 | -13.93507 | -47.363 | 2026-08-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5400eb34-8ce6-33dd-b103-039e32357376 | -13.78258 | -49.72297 | 2026-08-07 04:10:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bf0a87f-7ae3-3f3e-88cc-0278d357446b | -11.14848 | -44.47312 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 088c1c03-d35e-3133-ac27-0f342608600d | -12.63057 | -46.8952 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb7c83dd-c652-3ccf-9344-d8bd061df6c6 | -14.26827 | -45.29519 | 2026-08-07 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00dd5d53-dbe5-3610-a12a-9f49b1045969 | -15.58577 | -54.29157 | 2026-08-07 04:10:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7439333e-9422-35b7-89cf-903e4f385e98 | -16.67142 | -49.14434 | 2026-08-07 04:10:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67edde8c-2b5c-3139-b43a-14f2866f45a6 | -11.14147 | -44.49497 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 464df86d-5c3d-381c-9cb6-35f165b9f1a7 | -14.34142 | -54.9309 | 2026-08-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 248bfebb-7a1a-3e30-bf27-5050c2eb1e7f | -13.83019 | -53.71466 | 2026-08-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1c9f3c57-0727-396d-aae7-cef52a7bfe3e | -10.68402 | -50.50146 | 2026-08-07 04:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 356c3de8-5391-31ae-a8e9-460e6ac2dec6 | -11.41196 | -41.79907 | 2026-08-07 04:10:00 | NOAA-21 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1ece7285-9c67-359e-a7ae-4ff1435f2d8d | -17.5296 | -45.35354 | 2026-08-07 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5326970-59fb-31e4-9ab1-3bd5432cbf19 | -15.10688 | -53.59475 | 2026-08-07 04:10:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1ef341cc-b897-3e97-a291-28818c726fd0 | -11.18553 | -54.86021 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b3ca425-ce5b-3817-a253-38d678870d21 | -11.13099 | -54.89164 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a132806f-45e7-37fd-b09e-bff3e4f3027a | -11.14788 | -44.47685 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d45a7583-3f1c-3d82-8b7e-ae5b181f2b35 | -15.10763 | -53.59106 | 2026-08-07 04:10:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ccea0c66-4e3f-3e45-89e9-f1c822912d37 | -11.17182 | -54.86273 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 283f0386-8aa6-3ef3-9a37-e61a219b0464 | -12.58538 | -46.90456 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f755a79a-75f0-36e6-9e6c-fbbf8663bc00 | -15.07877 | -53.59248 | 2026-08-07 04:10:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e14aafd7-fb09-396c-8439-a15095e9db93 | -12.55366 | -46.95523 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c123b23-958f-397f-92b9-8fc0432b65bc | -14.44319 | -53.34256 | 2026-08-07 04:10:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04a5dbc7-b2db-3676-ad66-d50c46e7f769 | -11.32118 | -45.20392 | 2026-08-07 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5e2ae8e-94ae-3f30-9501-eb7a150fbb40 | -11.13527 | -54.90356 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e81975a-ceab-3758-9165-41f84f5b0eda | -11.15052 | -44.48471 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65c728e4-1388-3f23-853f-363f1134b0ef | -15.58918 | -43.73454 | 2026-08-07 04:10:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ba188f2c-b253-3271-b25d-04230e0379f2 | -15.92693 | -43.9884 | 2026-08-07 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad356989-7c3c-307c-bc55-40f3087bbe0e | -12.55977 | -46.94201 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 46bf8db5-923b-3b0a-9e55-e57185b18329 | -11.14195 | -54.91251 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f2f8220-c2d9-384f-a0b0-681637d00baf | -11.43654 | -42.49974 | 2026-08-07 04:10:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 70648dfd-3b20-3c35-93dc-dc30d521da51 | -12.57415 | -46.90267 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca2d0caf-9f59-3af5-a58a-b5c0aa864b91 | -14.34043 | -54.93556 | 2026-08-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8f2878f-bf5e-35f5-be91-1bb59266a097 | -14.4341 | -45.67818 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e49bdf6-6016-3bd0-88f3-f0622c041bca | -11.18758 | -54.84994 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 593a2fc3-e318-3919-b4f7-6e85fd5432e3 | -17.13169 | -47.56432 | 2026-08-07 04:10:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7052dc4b-a57a-3bb4-9a28-457e50088288 | -13.93963 | -47.36134 | 2026-08-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d0a3e73-0ac3-3f53-b079-6dea2edb5fe0 | -15.8722 | -43.59833 | 2026-08-07 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b06f51c8-1661-3405-beb5-9b774f3d70a5 | -14.42975 | -45.66142 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7acfd43-aabf-3697-9b69-bf3db11e50a0 | -11.18126 | -54.84856 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44576e18-9a15-3007-8c9e-882483d5930c | -16.6836 | -51.37328 | 2026-08-07 04:10:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7429b5ee-bf7b-3fb1-81b7-41c9dc63630d | -13.62261 | -54.67655 | 2026-08-07 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7dc4c4fd-9e40-3c97-a0f4-6db83470147c | -13.83265 | -53.71986 | 2026-08-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9eb9b2bb-ce2f-396d-8abf-ea4b4b062bc7 | -11.13085 | -44.47402 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5329e75-eb1d-3c18-a75b-a57de000692f | -11.14949 | -44.48861 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b5aad3f-40d5-31d0-817c-40dbfd24de19 | -12.33228 | -53.16562 | 2026-08-07 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1f34db7-c90b-3191-8e5b-068b0f6b0392 | -16.69178 | -51.37336 | 2026-08-07 04:10:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba964cfc-f074-3618-8eb5-2220343d5d00 | -11.13451 | -54.91651 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 817b58f1-14fa-3d67-8353-2665528a3a15 | -11.15332 | -44.489 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 476b9516-fcc4-3908-9816-98e2deba5299 | -12.00824 | -49.28059 | 2026-08-07 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8409d062-d30f-3560-9d19-ee8eb45027e8 | -11.15271 | -44.49273 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f64628e-6e9d-3793-aaa9-7b873d3d55be | -14.33926 | -54.93509 | 2026-08-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc180185-635e-3282-969f-9f34c72ea4b0 | -12.57789 | -46.9033 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0939d81e-6489-3898-a410-cd1a80688f01 | -12.44307 | -50.36623 | 2026-08-07 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 319a9df9-fd07-334e-9db1-1c73b18f3eb4 | -15.0733 | -53.5913 | 2026-08-07 04:10:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09eae28e-bd78-3efa-87e9-80461745d376 | -14.42911 | -45.6653 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 25599168-920c-3cfd-a218-953b0e251a65 | -13.96513 | -47.37073 | 2026-08-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 583b3b1d-6495-36e8-b04c-a9bde7cddee2 | -14.1564 | -54.00057 | 2026-08-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4391006-9340-341d-883c-60a28442648f | -13.93669 | -47.35601 | 2026-08-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f5503c3-96dc-3da8-9605-302abc8854b3 | -9.93688 | -48.69914 | 2026-08-07 04:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae241428-f10a-319f-94b0-526df96043dc | -17.45993 | -47.15847 | 2026-08-07 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a372b485-17e9-3579-b5aa-f0d57ac87427 | -13.82373 | -53.71743 | 2026-08-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c362a180-eba3-3c36-bddb-a906d4f32ed3 | -11.16648 | -54.85644 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d85ac66-08bb-35b6-b510-2c422b566557 | -12.33372 | -53.1706 | 2026-08-07 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c182cf62-4ca2-370c-b4e8-fbf7590e0c2b | -12.35025 | -48.20859 | 2026-08-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e7c3f43-2671-347e-b684-436526e5c497 | -11.15129 | -44.4774 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 05061e07-5b8f-3e4b-9836-b0f550fde9fb | -11.14991 | -44.48844 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56772f0e-c6ef-3cc8-aa66-11d938b6e9db | -16.6892 | -51.36898 | 2026-08-07 04:10:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4cbb8c9-4ad8-3f05-b870-3038d2842651 | -11.14548 | -44.49179 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4155f7c8-dd1d-39f5-a73f-1cdab814b4d5 | -14.35002 | -54.91323 | 2026-08-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c7d68b05-e866-3ed7-ac64-9a4e11f59238 | -12.62679 | -46.89479 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09fb87c6-5fc9-371c-811e-f7481dd447c0 | -11.18655 | -54.85508 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d08280c-ba9a-3026-bc43-550de6702b0a | -12.57376 | -46.97341 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b2bf20e-2e71-3e17-a7ea-f8b1415a3936 | -15.10838 | -53.58736 | 2026-08-07 04:10:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11f0d151-41d0-3106-848e-06997a70f597 | -12.49531 | -50.37088 | 2026-08-07 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95b5c769-3a59-3928-9046-6d2f5f656185 | -15.86944 | -43.59421 | 2026-08-07 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c1560a7-b38f-308f-a79c-15b183742708 | -13.82292 | -53.72136 | 2026-08-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6bfaa951-02b3-31fe-998c-a3aa89aab652 | -11.15734 | -44.48582 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82597a61-1660-33a3-b2a4-f3b7c3bf3424 | -11.08258 | -47.79569 | 2026-08-07 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5099152a-1248-337e-bd56-b45bf0047abc | -11.4125 | -41.79552 | 2026-08-07 04:10:00 | NOAA-21 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ca240b5d-0659-30cf-8fa3-ad40b097ff5a | -11.13025 | -44.47776 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e81d0fe-257f-3df0-b653-bdd6bf5f1b4f | -14.22882 | -48.50712 | 2026-08-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e08955f-df69-3e2f-8b2b-dce2d656b0d6 | -14.42502 | -45.66859 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 495e4410-38e0-3821-98ca-b86c1aa364e3 | -12.58086 | -46.9085 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9383f4ff-40eb-3e1a-b1d7-ab42cfbee7a6 | -12.59363 | -46.90124 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 28d945d5-a8d8-3449-ac34-f9af82160367 | -11.15905 | -54.86054 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22419877-f623-3e24-a5dc-42b7960d259e | -17.59209 | -41.30284 | 2026-08-07 04:10:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8ee34d3a-f6bf-3ecc-af3e-01e8f8050fc1 | -12.00088 | -45.13067 | 2026-08-07 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9085747d-0bea-3217-a946-5e7983982302 | -12.6276 | -46.89012 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdc29f29-6a4c-343d-8c01-5c5087f7dce2 | -11.46002 | -44.56651 | 2026-08-07 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 094e0b32-b478-30a8-8e64-f9b612ed1ecc | -14.736 | -47.13567 | 2026-08-07 04:10:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d09b9b40-9739-3554-966a-dabd696a125f | -16.14111 | -43.55135 | 2026-08-07 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ac763ce-9186-3456-aa8c-b6fec33dac1f | -17.01363 | -46.01739 | 2026-08-07 04:10:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44878d36-5b5b-3fdf-a5fa-9cd06c1b39bd | -15.92418 | -43.98428 | 2026-08-07 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf1f1d76-cd50-38a1-b1f1-b9eca99f08c8 | -16.68251 | -51.37172 | 2026-08-07 04:10:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0e2b6d2-920a-3993-8496-85fa28b9ef4b | -11.14668 | -44.48432 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 85b84dc4-d3fc-3193-98bd-1b04bfda8932 | -11.45722 | -44.56221 | 2026-08-07 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 85bc3cf5-5b3c-3255-8424-8b041ce50407 | -11.13674 | -54.9055 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c003208-3667-3004-b33b-a911ccb1e41a | -10.12573 | -48.91228 | 2026-08-07 04:10:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README11.md)
