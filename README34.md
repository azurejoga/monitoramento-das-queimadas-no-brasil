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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6113c5f4-993b-3ab4-9953-610012af44aa | -13.3555 | -47.41668 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8e933b2-da69-31c3-8531-edd343ff9c3f | -8.20679 | -46.98327 | 2025-10-25 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ff24061-ff22-3af0-9d1e-550abf25a8c4 | -7.14849 | -44.12447 | 2025-10-25 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 923d53b3-d551-3ba0-bb1f-387541bd26e9 | -8.60278 | -44.81382 | 2025-10-25 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dee84fbc-56e0-3be8-a30a-3fc6bc7caf79 | -10.66193 | -48.0801 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e08a6a2-912d-37f1-b6e4-5d6c5b4bcba8 | -8.60967 | -54.66116 | 2025-10-25 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ddc48047-4d9a-3d46-8ddc-07bbd9291b14 | -2.89513 | -41.63595 | 2025-10-25 04:19:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b70acb65-74c1-3e79-9647-863e5caba51a | -12.2283 | -43.308 | 2025-10-25 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50c16dc3-9175-32a7-81a3-c178cddf0b8b | 1.64322 | -55.73521 | 2025-10-25 04:19:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f508ced-f1e0-3b5b-bf57-a882392dc26c | -12.47224 | -44.53724 | 2025-10-25 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e9f37956-78e5-37e2-9793-c1d899466701 | -7.15675 | -45.83335 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 432e354a-1cfd-35a6-80d1-9853bb317319 | -10.67738 | -48.09541 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70e335c6-110b-3f3f-9b76-f4a9121692cf | -12.06425 | -46.44862 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20f27ef7-14e9-3c46-a9e9-483ba3d36283 | -13.54896 | -47.56433 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89ffc324-8bcc-3528-9461-c11b49967860 | -12.18247 | -49.47717 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cebaf210-2890-33f6-85fa-0355ee05b834 | -9.26478 | -46.48031 | 2025-10-25 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0aca9113-8057-3d95-b88d-ebdbefd73fdc | -13.28295 | -47.49087 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe846aca-3dd3-342a-999e-74ad1bbc9c7b | -12.96053 | -48.50364 | 2025-10-25 04:19:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a2ab085-6d88-3447-b531-ba4ece82f002 | -10.63948 | -48.06383 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6297aa9-359f-33e4-b5c9-4acdc071ff52 | -10.65493 | -48.07897 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6987dbf-e654-3f2f-a3d3-7d0b0c9ad786 | -13.54225 | -47.56314 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42ad4810-e0ab-3ca0-9734-f3f6d17448a7 | -9.32625 | -46.98369 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f26beb6-320a-3e21-b356-22b810815d31 | -6.10805 | -49.03691 | 2025-10-25 04:19:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0e0a0a9-4166-3328-b2aa-fc6c8a487f22 | -9.24358 | -45.61827 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1cff593-ce00-3012-b162-90564442b227 | -6.24264 | -46.3969 | 2025-10-25 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f3f6618-5273-3f9c-bfb6-51fcee804952 | -9.24195 | -45.58584 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b2e2e54-b2f5-3ed8-b5f6-cfa4f30e3e3d | -12.83017 | -47.23955 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53f9c315-f941-332b-80aa-25b16362537f | -13.33094 | -47.94703 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c05e2491-b3a9-3079-866d-4d1d5669270e | -13.26497 | -47.98627 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 359eadfc-f20e-30a7-b8a0-9543b2fb276b | -10.42867 | -48.00133 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 783ccadd-2fa2-3531-9d41-31ca1c387fd5 | -6.44768 | -44.28405 | 2025-10-25 04:19:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 075b243e-f81c-3a4b-9d92-d03624bcec1f | -1.32769 | -49.11449 | 2025-10-25 04:19:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6085d7f-58d2-379e-bfac-52d9c7c1af69 | -10.48276 | -44.14777 | 2025-10-25 04:19:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9b0501d-e687-3025-956d-7b89654344a5 | -9.95675 | -48.26237 | 2025-10-25 04:19:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fc1c7e1-1e08-3190-a4ea-d1638e7a0014 | -6.95096 | -45.03348 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ad15a44-fdd2-39d0-852f-f631178986e9 | -11.42926 | -44.67372 | 2025-10-25 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 411ffd38-7694-330e-8d54-96bb62781d7a | -10.71226 | -44.7467 | 2025-10-25 04:19:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f8980d8-632c-349f-b59b-dc93f515ef14 | -6.42008 | -46.18712 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2452e16-68ea-3c67-8f8c-bf26ce8e0ae1 | -13.33748 | -47.92838 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e92a318-807a-3570-ae3f-0731fb609d09 | -8.69013 | -47.54739 | 2025-10-25 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c40d142-d38b-3b6d-8b32-7d90de3954e3 | -10.94912 | -50.29916 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f4a8163-9fcf-3e30-a525-8ae34e9a5b31 | -7.16842 | -45.84612 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f424926-59e2-3030-9ab7-dafca6338099 | -9.44252 | -56.65052 | 2025-10-25 04:19:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a447cc05-619e-3546-bc41-7402ccd99434 | -10.68156 | -48.09187 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9090a8cb-31ff-3cce-bec7-0de62947b2fc | -13.0369 | -47.39023 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4480fac4-2ac0-3000-aa17-c18562bba972 | -12.00792 | -44.02374 | 2025-10-25 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| de852015-76f5-31d6-8deb-e623a00a9ed6 | -7.33831 | -46.14474 | 2025-10-25 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0e81052-b265-3417-8218-5d15615332f2 | -7.55399 | -47.1132 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 623efabb-50a5-38bf-b7df-6dc1b7d659de | -7.41825 | -46.65439 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d452743-abc2-381d-aaa8-0d7e732e305b | -8.82956 | -49.72211 | 2025-10-25 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 050e76d8-0b0b-38d0-bd3a-49e6b9b37a57 | -6.8966 | -46.36739 | 2025-10-25 04:19:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae3ac3d7-feb3-315f-b69b-9bfe68e8735c | -7.9807 | -47.38296 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca1c3cca-1b20-30b0-90ff-f09e6dda7505 | -10.64366 | -48.06034 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0160b70a-0303-3268-b75e-2565cc802a29 | -10.62426 | -42.3159 | 2025-10-25 04:19:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3175a52d-68cf-3def-bf4d-833c592b73d0 | -10.51532 | -50.24551 | 2025-10-25 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5d487f2-59d9-315d-abfc-3292cd396d69 | -6.96791 | -43.49855 | 2025-10-25 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13d060fe-2f97-3707-9741-3575651c3b3e | -13.40627 | -47.95993 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58fc8757-b66f-3d63-aa3b-c0a68ece8779 | -7.96779 | -44.81207 | 2025-10-25 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8828d5ce-8d02-3da4-9c80-79dc2a7c44ab | -7.78067 | -45.39385 | 2025-10-25 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2c85332-6ab0-3bf9-bccf-80883ec0f056 | -12.23449 | -47.03675 | 2025-10-25 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d3f937f-4137-3af7-beb9-f7efb1f47431 | -10.6535 | -48.06599 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dab229ef-9955-3bf0-9836-423d88dcb4b9 | -10.41829 | -44.49709 | 2025-10-25 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04a28f37-4001-3dcd-98a7-521ca44f3968 | -12.83817 | -48.64782 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 2589b117-41b8-31cb-ba09-b963b0ddd6a7 | -11.91469 | -44.18 | 2025-10-25 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0a02ad2-7d80-3294-b8fc-2211ef45949a | -10.99572 | -54.26003 | 2025-10-25 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6be2c96-077a-3615-829e-c17f93f8e72b | -8.34042 | -46.18403 | 2025-10-25 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dacef4a8-617b-3cfb-9cf3-939e5c13ac96 | -13.27896 | -47.49413 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00535f4f-22ae-380a-823f-7477175cfd42 | -12.80457 | -48.67557 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c234bc6-7a66-3978-a0be-435691a0b7c9 | -7.64822 | -44.57714 | 2025-10-25 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccc7dc29-a1fb-3953-b5d8-b79b05a34560 | -10.52468 | -44.22395 | 2025-10-25 04:19:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 468a87ec-a93f-3c9b-a58a-29e06734295e | -13.20557 | -44.11043 | 2025-10-25 04:19:00 | NOAA-20 | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1dc9831-d340-36c9-a15f-bd377bd7bc42 | -6.51519 | -46.51191 | 2025-10-25 04:19:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 832420bf-26a7-354f-9c38-cd04ed0f0922 | -13.33715 | -47.90913 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71e3952d-0b98-3263-8e70-58f8e3b882fb | -12.11446 | -46.70849 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c7c76d2-f259-317c-aefb-55b0caecd8a0 | -12.04727 | -54.23938 | 2025-10-25 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 60528fad-3a22-381d-b23f-b1b2057cf375 | -10.06511 | -47.08072 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 14e30c51-8de2-3770-bb7d-7eea69688f90 | -7.08116 | -47.2776 | 2025-10-25 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a729a674-359f-38c6-a27c-84dd47f1672e | -6.41167 | -53.66307 | 2025-10-25 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e37d18a-5e1a-3cc2-b117-08af2adb0c3e | -6.91994 | -43.49836 | 2025-10-25 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6414fb0-fdce-3adf-8f1b-cc54cf1c0d74 | -13.05713 | -50.29076 | 2025-10-25 04:19:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e75acbcf-3192-38f3-b907-2e60fdd8b817 | -11.59578 | -45.06747 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 032d3361-67bc-311e-b253-31e322ce2950 | -12.12824 | -46.7291 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6bf6b8b8-1167-3f32-b19c-0839428ea049 | -12.12112 | -46.7096 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6db7590e-a906-32e3-af5c-a94a3057a602 | -6.64914 | -43.60518 | 2025-10-25 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bb1d10f-e2fb-3548-98bc-35a6291ae3cf | -2.00077 | -44.51361 | 2025-10-25 04:19:00 | NOAA-20 | CEDRAL | MARANHÃO | Brasil | 2103109 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7598ec53-1fbf-3b0c-9954-ca6946e63640 | -6.91547 | -42.24822 | 2025-10-25 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ca256ac5-e47f-3c8c-8761-486e321ec079 | -13.09535 | -47.01038 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd3c305d-8eb5-3d1d-8e7a-18fbe32d92f0 | -9.45235 | -49.75138 | 2025-10-25 04:19:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5cf2ba06-647a-30c8-a435-e570422758e6 | -11.00426 | -49.84306 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c59a342-1f08-3235-a25a-fa54e37935a0 | -12.48083 | -42.77119 | 2025-10-25 04:19:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2bb97083-a381-33e6-85d4-25db9bfbec10 | -10.82329 | -48.00141 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be026bda-487b-30e8-add1-f1b3adacd332 | -8.23209 | -47.86383 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8aa6ba3-65cb-3501-b38a-5a8a63882502 | -9.08811 | -47.81659 | 2025-10-25 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 512a1305-7356-39f8-ae7d-a8739564df33 | -9.70126 | -45.38902 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bad16449-8b62-36d3-8b52-a66aee3913a4 | -10.89722 | -43.82512 | 2025-10-25 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3d502e2-a4d7-3958-96dd-187242c80a7b | -6.11123 | -49.04052 | 2025-10-25 04:19:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51dc4ad6-9094-3b8f-937b-0eee4a7c021b | -6.79081 | -45.42123 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58167ed0-e5bd-3a2c-8f7c-a36f931eedc4 | -10.0014 | -47.59867 | 2025-10-25 04:19:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5ceefc4-5fed-3696-937b-9a22544d0aba | -9.58263 | -46.63854 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32ca4800-9641-31a9-a030-2d1696bf6101 | -8.13038 | -47.0446 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README35.md)
