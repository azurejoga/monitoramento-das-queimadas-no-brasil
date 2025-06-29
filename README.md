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
| e62cc0d0-5383-3311-8871-1505e6da8646 | -10.9815 | -45.0874 | 2025-06-29 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 1f530724-51b3-397e-975e-60127f490fe1 | -11.0354 | -56.2844 | 2025-06-29 00:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 457.1 |
| a3e5b10e-22a8-3587-8b60-b262076002f5 | -11.0168 | -56.2659 | 2025-06-29 00:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 282.7 |
| 7da16b0c-300d-342d-9277-4570402f10eb | -11.0358 | -56.2443 | 2025-06-29 00:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 65e469fd-0c74-3bbd-98fd-c97e847546c1 | -10.5767 | -52.0271 | 2025-06-29 00:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 88603b5f-45e4-30c6-859a-eb6145788805 | -11.0003 | -45.1078 | 2025-06-29 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 28665530-2ffd-32e5-990e-0b99517f04b1 | -6.634 | -47.274 | 2025-06-29 00:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 0eb48cde-feb6-3286-87f4-25fb5bda6a99 | -12.6128 | -54.2107 | 2025-06-29 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 72ea8b2f-e6d8-33cc-85b0-a878f87bcaf4 | -10.962 | -45.113 | 2025-06-29 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| bee96d00-16c7-3b3a-8b5c-d93d789d942c | -11.2666 | -52.7318 | 2025-06-29 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 42439dd1-174f-38a1-a60c-0aa5195a620a | -6.6338 | -47.296 | 2025-06-29 00:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 2d29e11a-39f5-3ec4-bb5a-04519f3e3b6c | -10.5387 | -52.0517 | 2025-06-29 00:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| f713559e-4719-3954-b44c-c4e9c9256579 | -11.0356 | -56.2644 | 2025-06-29 00:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 339.1 |
| dd14fd21-f8be-322d-8f6e-8eb8b73da5f7 | -11.0166 | -56.2859 | 2025-06-29 00:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 392.1 |
| 53d22c06-27c6-3dba-82e7-7067ace6585a | -6.6153 | -47.2754 | 2025-06-29 00:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| b28f6e29-b57a-3ef1-b675-cbceb27c3576 | -10.539 | -52.0307 | 2025-06-29 00:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| c4d348f5-60d1-35f0-a793-f1d2d6aa5ecc | -6.6151 | -47.2974 | 2025-06-29 00:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 89327fb6-20f7-3430-bd16-d1c22003aa26 | -10.5579 | -52.0289 | 2025-06-29 00:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 187.3 |
| 29445c86-09c7-3ee0-93f0-7784fe93c7b8 | -10.5576 | -52.0499 | 2025-06-29 00:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 243.6 |
| 698d5edb-a1b0-3134-8e2e-aa697e200fba | -22.4056 | -46.8205 | 2025-06-29 00:00:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 3061ca65-dc9f-37b2-b0f4-1b5df8fdbecb | -10.5765 | -52.048 | 2025-06-29 00:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| da47e3e0-33e4-3ebb-a94a-20f82101cfaf | -10.9811 | -45.1104 | 2025-06-29 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 249.6 |
| 7d7ea238-e26f-3554-b4ab-821d66893653 | -11.017 | -56.2458 | 2025-06-29 00:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b292efcc-a556-3f86-854c-622b28f002db | -12.6319 | -54.2087 | 2025-06-29 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 0f212c5b-f7d0-3389-955d-c985f303f746 | -11.2664 | -52.7527 | 2025-06-29 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 159.9 |
| 0d9e0b1e-0609-318e-ba50-590737cc99cc | -11.2474 | -52.7545 | 2025-06-29 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 9a74bbeb-096f-3110-99db-45175a23ae46 | -11.57215 | -44.84016 | 2025-06-29 00:01:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 85495d53-2fbf-3355-a9b6-963e6c8f4f61 | -10.93108 | -44.16563 | 2025-06-29 00:01:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 4afbb5ad-39db-30ab-a14c-da1dcaf00d6a | -10.92915 | -44.1496 | 2025-06-29 00:01:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| f16685c2-9e56-3897-9dd1-50a34a992e51 | -10.5464 | -42.535 | 2025-06-29 00:01:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 32.4 |
| 840c047f-3e2a-383f-a11d-11c8c33f83d5 | -12.06968 | -48.48039 | 2025-06-29 00:01:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 1ce2fddc-bbe2-3b59-bfa4-084603ec47bf | -12.05305 | -48.4823 | 2025-06-29 00:01:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| ced1bfd4-3947-3908-ab8b-28a2a779f5cd | -10.9777 | -45.10797 | 2025-06-29 00:01:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 426.2 |
| b1637207-fcc9-34d4-ab1f-4849403ef93c | -10.3599 | -44.24831 | 2025-06-29 00:01:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 365e9c7c-76a8-394e-80ae-7b8d4728fd44 | -11.58455 | -44.83855 | 2025-06-29 00:01:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| f0b567b8-3ce6-3f47-85d3-4a9ab512fd14 | -10.9212 | -44.15643 | 2025-06-29 00:01:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 51d718ee-a9d6-35f8-8911-2113e470926d | -10.54796 | -42.54737 | 2025-06-29 00:01:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| d20d92ba-fd17-326b-a12e-4b33cac6fdd2 | -10.53622 | -42.53658 | 2025-06-29 00:01:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 37.3 |
| c9c2a563-6946-3803-9620-5cac8b166298 | -10.98 | -45.12717 | 2025-06-29 00:01:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 09418595-7c4e-3fd8-81fa-d898d9cc6f59 | -10.53776 | -42.54878 | 2025-06-29 00:01:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| c6c3f13a-f6be-3a94-8369-1dd1f0cfe26d | -6.62533 | -47.28271 | 2025-06-29 00:03:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 252.9 |
| d5cbe2c1-193d-3ef1-b36a-fffb8e55a64a | -7.25868 | -43.13908 | 2025-06-29 00:03:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 4a192d2d-ec2d-3c76-b0d8-a8df730e901e | -7.1941 | -43.71555 | 2025-06-29 00:03:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 35db2468-2d8e-3fb9-ab48-af8b6206b5a0 | -7.5588 | -45.84765 | 2025-06-29 00:03:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 4753361d-968e-3cc4-bcf0-9beda2436f53 | -7.10049 | -44.37518 | 2025-06-29 00:03:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5e42a7b4-84e4-32e8-9dcd-008fe43aaee0 | -7.26881 | -43.13765 | 2025-06-29 00:03:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 868ebaf7-84e2-36af-9b82-299df3d4c8df | -7.09806 | -44.3666 | 2025-06-29 00:03:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| aff12606-943f-3048-9e2b-4b1e7c5e5c35 | -6.62824 | -47.30676 | 2025-06-29 00:03:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| f211814d-4901-32f0-8b85-096436c9de68 | -6.62027 | -47.28982 | 2025-06-29 00:03:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 142.3 |
| f1247d03-ad8e-33ce-821e-9ffca64a99a2 | -4.38846 | -41.91574 | 2025-06-29 00:03:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 56e04567-2681-34fe-ae3d-a89c4071f419 | -4.17465 | -42.03116 | 2025-06-29 00:03:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| a2a1c63f-3040-3ecd-92aa-7b5580a1b04d | -7.55553 | -45.83514 | 2025-06-29 00:03:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 357cba91-794e-31df-b279-6fe15ee5c9a5 | -7.19003 | -43.7234 | 2025-06-29 00:03:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b8e77fb7-7aa9-3b5f-a7eb-98a4cb2e70ae | -4.54422 | -48.02117 | 2025-06-29 00:03:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 0b3a45b1-cd4e-3af4-8f2f-db7c2548a876 | -4.5414 | -48.02826 | 2025-06-29 00:03:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 073afd9b-827b-352f-82b4-d56c4127c0cd | -4.37933 | -41.917 | 2025-06-29 00:03:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| dc49d4c7-efdd-3c70-98f6-9d70d710b795 | -7.09867 | -44.36082 | 2025-06-29 00:03:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 50c5a1ff-dee5-3bc9-96ba-c24a85c8f2af | -7.19237 | -43.70267 | 2025-06-29 00:03:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ba94dce9-c12a-3ecc-96d4-876bc305921b | -6.63425 | -47.28793 | 2025-06-29 00:03:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 3b585475-44e4-3188-9567-00db59cb225e | -3.81369 | -42.54766 | 2025-06-29 00:03:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5e5f1ee5-9de4-33ef-a052-499a434f31eb | -7.19895 | -43.70904 | 2025-06-29 00:03:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b74faf45-2a27-37f0-8dbd-1888fe4f8205 | -7.18838 | -43.71044 | 2025-06-29 00:03:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 61142ee3-ee60-3c26-b246-1af868d654dd | -4.38718 | -41.90628 | 2025-06-29 00:03:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5f24b7cb-72eb-3058-8b7d-f71037ef887e | -5.57129 | -45.22573 | 2025-06-29 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 54b6ff8b-8d9f-3115-a1cb-f714db13e884 | -3.62632 | -47.54581 | 2025-06-29 00:05:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 1f6118ba-2500-3970-8d38-444a49968fae | -10.5579 | -52.0289 | 2025-06-29 00:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 209.7 |
| f3322600-ce2c-3515-90bd-942ba758793b | -11.0356 | -56.2644 | 2025-06-29 00:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 163.3 |
| 2b50b8a6-9d50-3e24-84cd-4d84bede97f1 | -6.6338 | -47.296 | 2025-06-29 00:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| d41b9683-856a-39f6-903d-39c149a5c9ab | -10.5767 | -52.0271 | 2025-06-29 00:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| cc122c83-91e8-3f08-9b66-a99211d5dc63 | -17.4045 | -42.6186 | 2025-06-29 00:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 71.1 |
| c2ad8d65-496a-3fd8-a883-8019c3bce198 | -11.0166 | -56.2859 | 2025-06-29 00:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| e31cb22b-9eeb-3ace-834d-ddf2e6312f54 | -6.634 | -47.274 | 2025-06-29 00:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| ee2ad242-ed03-3367-a5d5-00544ccdf770 | -6.6151 | -47.2974 | 2025-06-29 00:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| e4b52c53-4518-363f-a4b8-2666efee1381 | -11.0354 | -56.2844 | 2025-06-29 00:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| b9adc341-7cdc-38bf-8618-3e5ef681faf9 | -10.9811 | -45.1104 | 2025-06-29 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 212.0 |
| 14580334-ba43-39d7-ba28-e83b754376d2 | -10.962 | -45.113 | 2025-06-29 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 0239f235-df0e-32d6-8038-aa044ac8691a | -10.5576 | -52.0499 | 2025-06-29 00:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 231.9 |
| d52a37f6-8517-3c2c-89ff-a1818fe05fc7 | -11.2474 | -52.7545 | 2025-06-29 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 01f92017-f499-31fb-805b-63f25c6b33ce | -10.9815 | -45.0874 | 2025-06-29 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| c26590b7-3f7e-3aab-ab84-2dc58c8689fc | -11.2666 | -52.7318 | 2025-06-29 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 8c6ecbda-1088-32e2-b7d9-394d198e3244 | -11.2664 | -52.7527 | 2025-06-29 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| cc1518a1-0dec-3a3e-8fd8-12e3cf6f4dd2 | -6.6153 | -47.2754 | 2025-06-29 00:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| b01f4072-d570-3074-be21-8959086de2d7 | -10.539 | -52.0307 | 2025-06-29 00:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 57f8743b-e7b4-3923-8cbd-c74c58bcf8fd | -10.5765 | -52.048 | 2025-06-29 00:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 7d745ee8-af66-3e23-bbc0-426834d454f3 | -11.0168 | -56.2659 | 2025-06-29 00:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 146.1 |
| 93b030e6-3b6b-3312-adc9-5dfb8b5bf50a | -10.5387 | -52.0517 | 2025-06-29 00:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 6601e455-9e3d-3171-8a1d-884767547d93 | -22.4056 | -46.8205 | 2025-06-29 00:10:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 97.7 |
| bd9cefee-ffa1-37b6-be43-cced3c1cad30 | -6.6338 | -47.296 | 2025-06-29 00:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| e7140ebf-5293-32df-822e-09f44fb4268c | -11.0168 | -56.2659 | 2025-06-29 00:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 180.1 |
| dde28c98-77a2-349f-b252-bd74c0c6cbe4 | -6.634 | -47.274 | 2025-06-29 00:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 22573712-807a-3008-a84b-465ec8c96abc | -17.4045 | -42.6186 | 2025-06-29 00:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 07f2b64a-c9f2-3d44-8813-d1859cd9993c | -6.6153 | -47.2754 | 2025-06-29 00:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 3098389d-9fe3-37c9-9b2b-97b45310ffe0 | -17.4038 | -42.6435 | 2025-06-29 00:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 52.8 |
| a081e91a-9be7-3cf8-a278-d1b6a57260de | -10.5767 | -52.0271 | 2025-06-29 00:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 8b616e11-fdae-3511-b3aa-531eeb7dd0dd | -10.9808 | -45.1335 | 2025-06-29 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 565b8687-418e-3227-a70e-a7fcd5489244 | -11.2664 | -52.7527 | 2025-06-29 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 390051fa-f6f3-3a0c-be93-4d4f05be234c | -22.4056 | -46.8205 | 2025-06-29 00:20:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 52d82c4a-7f0e-3c0d-a6c6-1453e1527ea4 | -10.9815 | -45.0874 | 2025-06-29 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| bbee5686-49dd-3e27-9d9f-a491a6b2418f | -11.0354 | -56.2844 | 2025-06-29 00:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 229.8 |
| 35fd3bff-44e9-3106-b6c9-6bb1e54f0062 | -11.0003 | -45.1078 | 2025-06-29 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |


[Clique aqui para ver as próximas entradas](README2.md)
