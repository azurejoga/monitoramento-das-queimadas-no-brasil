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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48afbcf9-9c1e-375f-91d5-2169b554a503 | -4.15607 | -47.98528 | 2026-10-09 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ad2104ec-81f8-3fe8-8eb0-6af4b69273fe | -6.25648 | -52.86141 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5261e4ed-17eb-3608-8a1e-96aa6c248619 | -6.16939 | -52.8585 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0507c90d-f2b9-30a5-a6e2-3079cf93afc8 | -3.29932 | -53.69915 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb5447ee-467b-335c-bbd3-3b372a59dc0e | -5.82932 | -53.54268 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d38ec777-ba01-3d27-a675-060d675d508f | -3.26285 | -54.05602 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a117585-627a-3635-8a3f-31716bf62afd | -8.01499 | -47.16222 | 2026-10-09 05:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02e99f09-7080-37f5-9a3b-af10ed56ec8e | -7.08437 | -52.68001 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a0b34b5-5d90-3926-97c6-265c64baeebc | -5.70912 | -53.48715 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b3c332fa-08e4-3196-84c8-64734dd4c358 | -3.44891 | -59.55769 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15687595-f70d-39ab-a28d-7a7c8ddd392f | -8.03992 | -49.39885 | 2026-10-09 05:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4c4e750-d13d-317e-846a-ea01cc12f3b5 | -3.01659 | -54.08513 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0a3e59e-76ad-3af5-8f27-ac1059a76322 | -2.56485 | -56.15848 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ef12b3a2-2fce-34dd-b331-a7176d89b7c3 | -6.99596 | -59.11297 | 2026-10-09 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12cbcfc0-95cc-3d68-bbe9-2542b1f0db83 | -4.52307 | -54.98476 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 260139ca-d40a-338b-b12f-d5cdb40c409e | -2.55299 | -58.04225 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 341fbe28-8e9b-3f33-83b7-75ed03f0bb5b | -6.23316 | -52.87912 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae15b2fb-750c-3fcd-a1e4-16203206bb09 | -3.71626 | -60.16357 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbfd427f-3c7a-3653-b71d-12e6634dd4f5 | -5.70746 | -53.47603 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cd798767-fddc-3b2e-aeaf-d729e412274b | -3.70858 | -61.32808 | 2026-10-09 05:04:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76a814dc-e57f-3ac0-9950-ad3f818e11ab | -4.93695 | -45.72854 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d521162-5212-3d22-a7df-8395f295444e | -11.06135 | -44.06126 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa9d4cfe-4132-32d0-b02d-34f0123d0589 | -5.74604 | -45.34385 | 2026-10-09 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7da9552-0a71-381d-b712-a0d94274ed6a | -2.99957 | -54.09916 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 000659ae-b530-3e28-af91-09baeea66642 | -9.79743 | -44.7718 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1aa09ef5-f7e9-3375-aaf1-c403efd85039 | -4.40457 | -50.79402 | 2026-10-09 05:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a00ac51-6ce8-34da-a4c6-1f0ec50e28c4 | -3.05223 | -53.95364 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 677f27f5-d970-39c4-8674-94b34fe65e26 | -11.20725 | -45.25547 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acaab878-f440-303c-a743-f0b1ce966e40 | -3.71278 | -59.65498 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 68313a43-3e19-33cb-a2ce-c7dcfcf116f2 | -3.30498 | -53.70775 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0dd6ce21-a574-3d99-b5db-854318b94649 | -6.00324 | -53.49797 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0667b51-068c-3b62-aa09-f87aed22a00f | -2.99969 | -53.91887 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 2ba317d8-69c9-3170-a74e-7b053dc0821c | -2.62433 | -57.71114 | 2026-10-09 05:04:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf089870-60c0-3c4e-b7dd-4b99b9615d99 | -9.87777 | -50.48751 | 2026-10-09 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 877fde50-96d8-3e74-8e7d-b57f96176c21 | -3.53457 | -54.65519 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb2ca417-c2dd-32f7-bbf3-6b499a04ec5d | -3.30769 | -54.04356 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1335e76-334d-3a9a-bc50-e5eda1c3635a | -3.56709 | -54.6919 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fb4be5a7-edad-3194-8430-29604bcd0e58 | -3.26554 | -54.01729 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1d7cc14-6ff4-39c6-b591-9fed240c868b | -9.71751 | -46.94485 | 2026-10-09 05:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ef1c235-d403-3ba8-a8e2-674da4f70f86 | -6.01223 | -53.48488 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec01d1dc-809f-3ffb-95e0-a209fe33250e | -8.90532 | -50.59405 | 2026-10-09 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3fb9a0e-57ec-3fd3-a7d7-7c9568d3d328 | -6.15309 | -47.9568 | 2026-10-09 05:04:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88ed5b90-8f68-32d6-8a0b-4fd8f2e2e27a | -3.53393 | -54.65919 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd4a354b-a3b4-3df7-a4bb-c5b71f107dc7 | -3.5469 | -54.66956 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfb60e9d-73be-3951-9ae8-834e3fd06555 | -7.5145 | -47.32719 | 2026-10-09 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 75a02daa-3ce0-375d-bc9b-6824cb0463dc | -6.22708 | -52.79636 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 770379c4-8de1-3d90-9967-0efe7089e19c | -4.11913 | -55.03431 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3957c732-546b-39d9-946a-9c87d4b1a622 | -3.10737 | -54.19392 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e2c6e33-cab3-356f-a5da-64f35ab5fc1a | -3.47871 | -54.72879 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e404076-f258-3a51-b38a-5c0625d1a52c | -6.00679 | -40.9584 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 48fa4f23-ccb9-3ec7-9bb1-79b8df9688a6 | -5.96502 | -55.34188 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1edf641-492f-3107-a84a-53f86d5a1c11 | -3.60223 | -54.56629 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e25b66ba-343f-3683-b557-cbb07ba674f7 | -3.71507 | -59.65677 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 043c4c06-d63b-31ec-8ba7-b112cc14ef93 | -3.93539 | -55.71498 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd8f5d51-9212-34e4-ab7d-f6c911872950 | -3.85519 | -51.11157 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10e78d42-28a1-3df4-af44-7f3a88e373e0 | -8.74836 | -62.6216 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e724bbe-e90d-311a-ab5e-66159bffcd1c | -3.46533 | -59.25565 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9658d8cf-e8fa-3cd7-8500-b56204aeb2ce | -3.74617 | -59.48122 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d86a2588-3b41-352e-802c-726044491b17 | -9.92279 | -44.79016 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91f485ed-2fe2-32c6-99f2-d6d4530cbd49 | -6.9584 | -45.28373 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 96a2e084-6c31-330a-862a-43133c3fa05f | -3.17336 | -58.62889 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 225f50d8-1b0e-3176-8e5f-f65d5146782c | -6.22486 | -52.78887 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8189bc2f-f268-3f1b-a2d0-6ce245e90184 | -8.23132 | -54.73563 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b85ded4-b838-3b6e-909d-87283ae709cb | -6.16606 | -52.85798 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0754dd4-aeb6-32f3-beeb-ed1426407e12 | -3.44584 | -59.54621 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf5d8bc0-c06e-3471-9cdb-c275dcad0c7d | -3.11135 | -53.78514 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c05d2520-da25-32d5-a539-9903ece503a0 | -3.28781 | -53.70495 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31d4c6bf-ebd2-39aa-a800-95498c353020 | -7.25083 | -48.05968 | 2026-10-09 05:04:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56ba4f58-ebf6-394f-87ad-27ca5a3b70e0 | -4.5244 | -54.97664 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 282e97d7-1b2c-32cf-be25-000bbe259569 | -11.09288 | -44.03712 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acdbd051-0875-3060-b3c1-81547907772d | -2.98104 | -54.0804 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 853670df-cb18-3f71-8d4b-577c1afca773 | -9.09331 | -61.01201 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a8588f0-6540-322b-a9da-b6885fe1ceef | -2.88368 | -54.19203 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50549e0f-3b9f-3391-9990-0421bf4ca3bc | -7.47775 | -42.84909 | 2026-10-09 05:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 03e27506-fc3f-3b79-849a-b5bd423f5b6e | -5.85257 | -53.46262 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3b3fb9b-329f-3a9b-b86c-92567e72d866 | -7.58413 | -45.63924 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0eca6af7-c57a-3737-a86c-6bbc5873fa0a | -3.00368 | -54.09586 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa80e0d3-cf53-3e2b-a97a-12a28b9f3e3b | -3.83455 | -55.97909 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e814d68-f690-3a79-9732-933b345a5a01 | -5.81609 | -53.86138 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 904fbf4b-8dca-3e04-ba01-fffb2e7564ec | -3.89877 | -55.89256 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0936846e-3346-3bd9-b1a5-456144732b19 | -4.29092 | -48.60466 | 2026-10-09 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 879b3758-6869-34a3-b12c-05ab27e22178 | -8.75448 | -62.61903 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8e571a4-c3ae-34b5-89c1-c5ce4d521099 | -2.94355 | -54.15758 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf8a996b-680f-3017-8cc5-0cf7da1d8970 | -4.10928 | -54.62255 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 801657fc-cff3-3f92-be9b-db088f67cfd7 | -3.65661 | -54.52224 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38692643-de05-340e-b92d-7ff9a819d286 | -4.56411 | -54.95819 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc14038e-b66a-3ab1-93a0-6fb26847fc7b | -3.51802 | -54.59919 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d0e63fe-0b9b-369d-af2e-ed729af338f1 | -5.09588 | -46.21568 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 437ddf52-8291-3746-8e79-5167cf17dc1b | -3.65864 | -55.47419 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 339136c8-7655-37e6-803e-4e444bbc0f9e | -2.91188 | -54.10889 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4a98e26-e56b-38f5-ba44-ecfdfa8a354f | -8.796 | -47.58833 | 2026-10-09 05:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6030b31d-4d95-3f3a-bd1a-75bbfba9e8aa | -4.73687 | -55.6584 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89da3084-289d-3b7a-b96d-3a154fe53068 | -6.06727 | -53.6031 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5af7d4e0-d888-30da-adf6-a2d4edd5a292 | -3.85418 | -58.89895 | 2026-10-09 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1da1e0b-a0e7-3c26-9788-2772354f1ebe | -6.49308 | -55.95942 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 028f4c10-7ba5-3d96-a43a-057aa7a16aef | -3.30543 | -54.0354 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22880851-6f5d-3f5a-b159-0c279e44d038 | -6.50136 | -44.36584 | 2026-10-09 05:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f66afa3-953a-3783-91da-a3b2845d68a3 | -3.48367 | -59.37996 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6200e8b6-7373-3fd3-8d5d-9013e79fbe90 | -5.95852 | -55.33665 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95bf2446-245f-3c37-b746-4956fe0fda55 | -6.2232 | -52.7993 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README159.md)
