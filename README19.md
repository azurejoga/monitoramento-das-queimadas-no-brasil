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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a80d4d4d-affd-39d4-a6ea-e424290e9914 | -5.25528 | -45.95684 | 2026-08-28 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b01bb65b-4a9a-3bf0-9db0-4e17a9bab892 | -7.09196 | -42.79425 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 94e3ba6d-1ccc-3b69-8ee7-571bd16f2102 | -7.09429 | -42.82312 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 93d9285b-bb40-3ed9-b9d7-c4dc33bbba99 | -6.27496 | -53.35149 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c8fa4c62-77a5-3102-9b08-7d14d846696b | -8.1143 | -45.82537 | 2026-08-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c7504f2-3f8c-3a93-b97d-3acb43c3216b | -8.17137 | -46.16264 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca24761b-c2f2-3767-89e2-f63a8dbf4e51 | -5.49328 | -49.2157 | 2026-08-28 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2d56542-6a1b-38dc-8790-5bc5964cda17 | -8.08597 | -45.80907 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 11378dc5-32cc-3b34-9be3-846d09c3c694 | -2.72194 | -49.47625 | 2026-08-28 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80315436-fc4f-3eaf-957d-668b20a9b39d | -7.88472 | -46.09416 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f79ed26-2a4c-328b-8d2e-7ca5496f2eb2 | -2.04575 | -48.03137 | 2026-08-28 04:14:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c30871db-06a4-3754-9b7a-ab82eef52f30 | -6.90491 | -43.64491 | 2026-08-28 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94107ee9-d2c8-3159-84d9-537fb795fbdd | -5.87776 | -52.1842 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98e92286-e8bf-35a2-9839-6378909cf658 | -6.50155 | -53.25457 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 837c5eca-86cf-3c93-9c80-f20431926c8b | -7.09142 | -42.79774 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9de66020-9434-3bc7-97d9-aa4459cbd906 | -6.30393 | -46.41849 | 2026-08-28 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b846b15-1700-3b7b-8056-0840ce1f0605 | -3.05881 | -48.7487 | 2026-08-28 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e2b82dc-27fc-3a96-89e6-741cf8956e8c | -8.17422 | -46.16716 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b15ae13a-bbba-37df-a001-1a1d3c5bbc0a | -8.17487 | -46.16319 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d79edb42-e8aa-3dac-afdd-346b7bedfc68 | -8.08252 | -45.8085 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1ce6b249-d97a-32b2-ab6b-d6a6132a4bb6 | -6.2788 | -53.3761 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ae0a2a4-67cb-3e09-9371-ecb18b30ed34 | -7.08034 | -42.20608 | 2026-08-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 24c443f6-c517-3dd1-a1c7-2c77d6bd5586 | -7.15796 | -46.54331 | 2026-08-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 218a39fd-8916-35e7-9ade-59231ac2a905 | -5.25529 | -50.961 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8bc05bee-f9af-316e-9514-f537c21bffd6 | -6.1837 | -45.93192 | 2026-08-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 534fcaa9-4bf9-3d72-8df6-41e89da99ed2 | -7.25108 | -45.8632 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| cb208e60-cfe2-33d7-8329-ad48731fa086 | -6.28021 | -53.36833 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 385b1d95-b7e5-3130-b79b-18ab62f8659c | -3.23124 | -40.02472 | 2026-08-28 04:14:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f0c84d6c-7dfe-3bf3-b6f8-867899f8e818 | -8.17005 | -46.17064 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f12d9a69-64b1-34ab-a897-808dde2b53e9 | -6.46208 | -41.56677 | 2026-08-28 04:14:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1c23dd2c-b72c-304a-8c12-213bca66ab90 | -7.39073 | -49.54636 | 2026-08-28 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2634059a-d20b-317d-bbe5-8157e127aee7 | -7.0673 | -42.15668 | 2026-08-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cb006b78-b422-3f68-8f5f-0892bd536f75 | -5.28941 | -50.93832 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ffc2918d-c06a-3eb0-8851-a85e4a80a055 | -8.09634 | -45.81065 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d522aa0-5d36-3cda-84bd-025049b24bde | -7.16975 | -43.16891 | 2026-08-28 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a4dfa6bf-0216-3792-939d-43ca80506de9 | -5.87654 | -52.19119 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c8bdaa4-71e8-3b18-bf7e-0759a9c3ed1e | -8.75886 | -44.2499 | 2026-08-28 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b2fc0cb-99db-3842-84a6-f49419280571 | -8.08128 | -45.81625 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 276e0468-3a58-3394-bda0-fdd2f877acc7 | -6.85299 | -40.90703 | 2026-08-28 04:14:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 544467f7-2058-36eb-b9a0-da8b46c0b343 | -8.01141 | -48.40899 | 2026-08-28 04:14:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07a843a2-8ec0-3ff0-8876-96940b9e4b22 | -6.15807 | -44.64745 | 2026-08-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad7190c0-c484-30c9-95db-2605c0e08306 | -7.07366 | -43.61103 | 2026-08-28 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ca9d730-32c7-3410-adf5-4022f54652b5 | -7.26725 | -45.3522 | 2026-08-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c333a625-3807-3cdc-9cd1-f5b4954a6976 | -7.16037 | -43.1639 | 2026-08-28 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c6d38868-99ba-3407-bb63-c806378b8696 | -14.07683 | -44.06359 | 2026-08-28 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e0ab5a9-c302-3a88-a6fc-1463dd92f2d6 | -11.01834 | -49.65565 | 2026-08-28 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e32fe58e-fee9-318e-808a-2c58d1b9e3ca | -11.64752 | -46.73989 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f27a68c2-88b4-3493-a5d2-b8bcc7676a31 | -16.12764 | -45.74674 | 2026-08-28 04:17:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11a4675a-7397-3b04-86fb-11eb040004fd | -12.42398 | -42.88831 | 2026-08-28 04:17:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 414a3b06-5982-3242-93d2-6e4b2f159446 | -9.4413 | -51.57478 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf20c184-ccd4-359c-975c-78325485c6f0 | -11.47858 | -46.95432 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b8750b6-3a12-3fa2-ae6e-d43d595d117b | -11.47356 | -46.94108 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57202099-14eb-3b98-b86c-937533077de6 | -10.83577 | -50.52053 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21c92db8-698a-3004-a4c2-7179caf2d1d4 | -14.07737 | -44.05999 | 2026-08-28 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 133d8171-29ef-3e59-89c4-54ad7ee8a86c | -13.60848 | -45.78102 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e30672cf-d38b-34ef-a8c5-a6979e50da2d | -13.32464 | -48.20532 | 2026-08-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 909163ac-51e2-3177-a37e-c50240cb2018 | -9.6157 | -55.1204 | 2026-08-28 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 55318463-ea8b-3d6c-861f-b056dd3b5a3f | -10.33171 | -46.75282 | 2026-08-28 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53664603-59af-3eac-8524-2a1317f55c96 | -14.87513 | -52.60117 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a6c4c359-3529-364a-8adf-f05253d86993 | -14.96337 | -52.59228 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d814ab0-1641-3f2c-b698-48af58a17a25 | -10.79527 | -54.01222 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5120e67c-655a-39ee-853a-5a4b53ad8d96 | -14.41564 | -52.58666 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b9e7e550-7e84-337e-ae0f-acb3df71f41c | -14.84755 | -49.21766 | 2026-08-28 04:17:00 | NOAA-21 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b19ae8b-2296-3a70-aea9-a4f37ac3edfc | -10.06133 | -46.94141 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 67ad690a-ea62-308e-ad1f-efb53f574952 | -11.61914 | -54.58875 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9aacd392-f86d-31fb-bdbf-f635700a24e5 | -11.01328 | -45.07247 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb154080-09d5-3dfc-a5e6-3f64a059d848 | -16.53859 | -43.35818 | 2026-08-28 04:17:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45e0f7d2-34c4-3fd1-b9be-71d02437a770 | -11.71368 | -54.5397 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a43e2e54-8b33-3b16-be8e-52055449612c | -11.73522 | -54.54792 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 77f0003b-128b-33c3-9bba-643f28fc403a | -15.06568 | -45.32077 | 2026-08-28 04:17:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52414281-de0a-3f72-ba1b-5e598c8190fd | -10.32435 | -49.96912 | 2026-08-28 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bd0d52b-bce6-37e8-b63f-aa5e74811677 | -11.27688 | -54.0284 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2ae85abc-1e78-3ab9-976b-a3c2eb0c3087 | -11.19657 | -51.24414 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| db45dacd-1605-3a01-b2d2-471c787b2953 | -10.96552 | -49.57448 | 2026-08-28 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69dae9b9-bb81-378b-a0d4-e395cf3bb050 | -11.19574 | -51.24879 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f20170f7-d297-3ac5-ae0f-f8ece6ae89cc | -11.38288 | -45.14345 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 109f6f11-01ff-3d08-8582-150801dc6323 | -11.65508 | -46.73718 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3d48f421-cb12-372d-aa8d-cb7fa793e2eb | -8.95275 | -50.17973 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06e13075-f96d-3e18-a071-ed2d76ff3581 | -11.24022 | -47.07914 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9601d218-b387-366a-86b5-053c2248df7d | -11.77195 | -47.65629 | 2026-08-28 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a932d4c2-2a92-36c4-ae32-4bf0769d6088 | -16.0811 | -47.9119 | 2026-08-28 04:17:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79f1f956-2710-3648-bfce-670141084e41 | -14.29751 | -51.72942 | 2026-08-28 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46ae61d4-8e92-3837-aa4b-774d08d284df | -11.53402 | -45.52274 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 843bb3a7-f722-324f-9228-8a54f565d95b | -21.08999 | -46.34044 | 2026-08-28 04:17:00 | NOAA-21 | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5dfbbaa2-5e68-3aa6-89c3-222a2d9f4df2 | -11.02179 | -49.66011 | 2026-08-28 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1148d313-d866-39d3-a5ee-18e7b69eeb8f | -8.8587 | -48.9054 | 2026-08-28 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45425cd8-cd66-3766-b9a2-d8998c999b1d | -14.116 | -44.38551 | 2026-08-28 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43d4cf0e-7ad1-337b-ae84-91df56883203 | -14.42672 | -52.60519 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 27636498-7f3f-34a6-92b4-b21694e3d036 | -8.77973 | -49.95094 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a9e5936-d660-3e23-a0df-1eb3edc24fd3 | -9.21649 | -51.56318 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc7ff6d8-ffe5-3928-ae5f-f66b48997d43 | -13.59458 | -45.78242 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59c9c273-2b21-3057-9cf5-267bd5c25558 | -14.88302 | -52.59477 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1a6dd9a3-c76d-36c0-bb8d-c6fa32d55dfd | -10.91465 | -50.53031 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a744d62c-7e99-3443-8d54-8caf8e4620eb | -14.98926 | -52.60795 | 2026-08-28 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2719900-1d3b-3bf4-bdf4-aedeeca18396 | -11.27825 | -54.02125 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1a79f9e2-6f1f-33ee-882b-cc7db10ff26a | -13.32022 | -48.2093 | 2026-08-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 913eda5a-abbb-3281-8694-9cc06c653a7a | -12.01933 | -47.17407 | 2026-08-28 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3dfcd292-e584-3953-9465-18d600b13a87 | -11.74664 | -54.51878 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2cdc867-7134-38fa-8c41-5ea923814b8b | -11.23612 | -53.9986 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6918cabd-9e59-3476-b309-d96ffc1ca2e7 | -10.78702 | -53.99569 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README20.md)
