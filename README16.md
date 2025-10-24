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
| 0c2e6b03-8534-3ee8-b918-0346b037a05f | -6.99294 | -38.05324 | 2025-10-24 04:17:00 | NPP-375D | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b02da873-b7e4-3add-b23a-bcd950ec0b51 | -9.09119 | -46.53571 | 2025-10-24 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdf30bd1-9b95-37cd-8307-d7f7775fe92f | -9.8583 | -44.89872 | 2025-10-24 04:17:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ed6dcebe-c4a8-3878-a675-65b6dd4fa6f4 | -9.62703 | -46.88164 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d981ba98-6054-37d5-8499-f8d747b5c987 | -9.01045 | -47.84519 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab881097-f0ba-374b-bc03-385495f67ab7 | -8.82775 | -45.42029 | 2025-10-24 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 804aa8cf-faa7-3400-b229-e41f1103f911 | -11.98915 | -43.32546 | 2025-10-24 04:17:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01342f62-ddfa-3cc6-987f-c8852f13c9ba | -2.77215 | -48.60163 | 2025-10-24 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 338167a9-edd4-3200-9c3f-0717da8f7333 | -3.80893 | -40.84099 | 2025-10-24 04:17:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 84b3aa3a-65d0-37d2-86a5-5422b225f592 | -0.329 | -48.69815 | 2025-10-24 04:17:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c1b2795-8b7b-33aa-8adb-fa588f58a2ea | -5.65321 | -46.57628 | 2025-10-24 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f54f4e6b-347b-3252-b46a-485b774bede5 | -2.73232 | -49.55881 | 2025-10-24 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e92a0d8-f247-3f41-8f3a-722d9be198c2 | -2.80934 | -49.13151 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69ed4e46-3fc6-3d8a-a6ed-c2f71e3897e7 | -11.05775 | -45.39244 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3c007f7e-88e9-3137-ab99-d4b978ca3c7f | -4.70183 | -46.44193 | 2025-10-24 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67688484-0148-33aa-b3ae-503fd0ed628d | -2.74079 | -48.68447 | 2025-10-24 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da9f5d85-0d1b-3729-9db2-e067d420873a | -3.2963 | -43.49694 | 2025-10-24 04:17:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 213fb693-d186-3ec8-b595-f9ab2c3582ee | -4.28721 | -40.70468 | 2025-10-24 04:17:00 | NPP-375D | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a1a38d41-157b-32ea-ba99-9497c7f2ae52 | -12.06077 | -47.98575 | 2025-10-24 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e653ead8-620d-3edf-b7c5-643affe4c5dc | -3.70346 | -40.42181 | 2025-10-24 04:17:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fb0a91c1-7a3a-39e1-ae8e-4e76364460db | -2.77282 | -48.5974 | 2025-10-24 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebd58d15-6b14-3faa-a3c4-e796c38bf63f | -6.7241 | -42.14968 | 2025-10-24 04:17:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0818d333-9a46-3622-9f71-8e9d3c011f5c | -5.22357 | -48.0034 | 2025-10-24 04:17:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ecfe13a-b6a8-327c-b163-bdeb0f6fcd75 | -10.63891 | -42.30337 | 2025-10-24 04:17:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2367e273-7fda-3c38-afa0-cc9554a81346 | -11.99323 | -45.42402 | 2025-10-24 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf0475d2-1895-32bd-878d-b1b6641654cf | -3.13526 | -49.51816 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 59328b3a-48e8-36cf-8384-302e24cb212b | -5.02241 | -47.15254 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79f5a4de-e288-3fef-9b85-8ed662cef820 | -12.294 | -45.52922 | 2025-10-24 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6abe4f6-44f1-3ebe-b994-5dd0c82b61c1 | -4.63978 | -42.5158 | 2025-10-24 04:17:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0f0fa0bf-6fb1-3cba-9092-6be86dff91ce | -12.07177 | -46.44065 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b7045c78-b638-38de-890f-bfe55a7c7a3f | -3.82756 | -47.47594 | 2025-10-24 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32fd703b-c0a5-3ad6-b1cd-220fa27bdeeb | -11.36983 | -45.94629 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c8916a76-6be2-3597-9d4b-d728da185688 | -9.60356 | -46.91193 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1441dba2-19c7-3ffa-bd8d-9cad19681b98 | -10.63796 | -52.18111 | 2025-10-24 04:17:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 567ce78e-76cd-38e1-a188-801099abde67 | -6.83793 | -41.55363 | 2025-10-24 04:17:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 952bb4e4-1490-3804-ab89-57663841ff1f | -9.3018 | -45.19191 | 2025-10-24 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c59360f8-9149-3f77-afe9-9ae04367a3ae | -3.08861 | -49.51057 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0812054-2e1e-339e-acd7-c4ba406f4763 | -4.03861 | -46.20131 | 2025-10-24 04:17:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75df7916-7436-374d-9371-892a26e1f3a4 | -10.90142 | -47.98462 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 262cb951-75b4-3799-868f-b3dd249fbd58 | -1.54527 | -55.4069 | 2025-10-24 04:17:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb0cb648-f95b-38a7-baf2-e0732d5f2539 | -12.06241 | -46.41161 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33c0b6e2-c45f-3b3b-92f8-4e256301af7a | -10.00855 | -47.10369 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c0403a1c-9f07-37b5-9488-b30b4ece8b6c | -11.3618 | -45.95261 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbdb8e26-ce39-3a4c-8bd9-a5344d97147c | -10.01343 | -47.07441 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 010ac274-aea4-354d-9a0d-99f445d25fac | -3.15017 | -50.16273 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c25b94e-0834-3f42-a3ba-4dfe64afa600 | -12.24964 | -47.45834 | 2025-10-24 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55ae3222-60cb-3c30-8d80-2de9f5540e43 | -4.91359 | -47.32828 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef7f8707-da00-3de6-9e61-3574e4f4c5ea | -1.12259 | -48.86002 | 2025-10-24 04:17:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f477f93-5505-3a09-9e96-58e505515877 | -5.62939 | -42.58949 | 2025-10-24 04:17:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5ede90c4-2c6d-37eb-8393-11affd7de065 | -9.63284 | -46.89121 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc4b886e-9024-37da-9a78-81504ca808e4 | -9.34928 | -46.59403 | 2025-10-24 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e1e3785-2b2d-3aba-9287-a9d27b15e9d8 | -9.26775 | -46.45418 | 2025-10-24 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1d72866-21d4-3a0d-b807-e2bd410159e7 | -6.44314 | -43.82182 | 2025-10-24 04:17:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c50738f6-b53f-3b85-bece-d5ca7fc25da6 | -9.01123 | -47.84056 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a06574bb-5303-3cb7-a095-653eded0b3c1 | -3.59856 | -42.80867 | 2025-10-24 04:17:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1de6d487-6176-36a6-95ab-f81906ad9dbe | -5.83187 | -40.82401 | 2025-10-24 04:17:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9b8b2610-c277-3bcd-8d94-a9b58c77939f | -8.44591 | -49.57687 | 2025-10-24 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c7cf873-c24d-3ee9-a10b-e0b735747884 | -6.89356 | -38.27773 | 2025-10-24 04:17:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f1cc85ac-cd21-3d10-b7ea-4b2c3b4a6dbe | -9.26487 | -46.44959 | 2025-10-24 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e45dbb30-9b1d-3f5a-b70e-4a3c6382a815 | -4.91689 | -47.33084 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81c637a7-2113-305a-b670-b33636f2ed7a | 0.40522 | -50.95457 | 2025-10-24 04:17:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a90ae35c-4166-3470-8c01-37cf3ce8f932 | -9.26999 | -46.46266 | 2025-10-24 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a58de61b-06cf-3a61-8945-f7bbb028d61d | -4.4583 | -43.23579 | 2025-10-24 04:17:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 99e60098-9ee5-3987-96a2-25912b5aa017 | -3.78706 | -44.12013 | 2025-10-24 04:17:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b654fb3d-46d7-3448-8340-1bd657d59c23 | -12.12921 | -46.72666 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 31b94467-257b-3a97-a45f-713324095931 | -5.03988 | -41.94608 | 2025-10-24 04:17:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 051e819f-37d0-3a9b-bcff-347e460608b3 | -5.82098 | -40.80254 | 2025-10-24 04:17:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 40ae4f59-e09a-3f8d-9df2-4b3bc3992108 | -4.17687 | -42.98499 | 2025-10-24 04:17:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a062b82e-697f-38d1-8fae-6816030b0a3b | -12.64281 | -44.12587 | 2025-10-24 04:17:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c8c1e7c-bfe2-3337-acc8-e68b8686cb3e | -4.31498 | -45.06318 | 2025-10-24 04:17:00 | NPP-375D | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e133ad22-e67c-3839-8b7d-1a5a7d60ae63 | -10.88813 | -46.04724 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 953f2fe9-1f53-3072-ad69-cf040006df99 | -6.30294 | -41.87647 | 2025-10-24 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d5514b7f-0ea1-3f6c-a446-62927f2b0bfa | -5.38268 | -41.55551 | 2025-10-24 04:17:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8e2354a5-b448-3355-be00-f9ae0a315a30 | -9.18624 | -48.84375 | 2025-10-24 04:17:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbea3413-707f-3342-b566-dfa21e6128e1 | -3.68358 | -47.11422 | 2025-10-24 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 101148d0-326f-3ebd-b3b9-dc3ff15b30ec | -5.68348 | -38.59481 | 2025-10-24 04:17:00 | NPP-375D | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ecb3d91b-a5e5-300b-9d14-d55c03656ffe | -11.97294 | -49.18089 | 2025-10-24 04:17:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b14a720-db62-31ec-ad2a-ee96eba72fba | -2.95209 | -49.14777 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4536a9ba-a62d-312d-86ab-cd21c637ce84 | -6.89454 | -38.27093 | 2025-10-24 04:17:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eca8b375-c7fb-3d9c-8ddf-778a341bbec5 | -3.76525 | -40.78508 | 2025-10-24 04:17:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 64dd3735-2d6c-3872-97d4-3f4ab5d94a6e | -12.07335 | -46.40956 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d81a612f-bcfc-3832-b80f-768e0a76680f | -9.24382 | -46.40123 | 2025-10-24 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4685e4e5-0984-3398-a3f1-ea424ca30e84 | -11.46123 | -43.70757 | 2025-10-24 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1eb7f35-fa80-392a-bb89-769a0a2336a2 | -5.45271 | -45.41336 | 2025-10-24 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| cea72209-5c54-3fb6-a581-7e72070cda8c | -9.23709 | -45.58813 | 2025-10-24 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02899bf9-7e3a-3477-bc5e-ba496602db0d | -10.04227 | -47.0794 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 999667b0-2df1-34e0-8da5-9fa731481d92 | -5.84862 | -40.83052 | 2025-10-24 04:17:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 12b6b3ec-28e4-34d2-8dd8-63056e702b32 | -11.36058 | -45.96003 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c502b84-f624-3226-bed5-4a7fbadc2a3e | -5.84228 | -40.82562 | 2025-10-24 04:17:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 96a2182d-7d2e-3e35-b0fc-c9c8623c2653 | -6.4437 | -43.81832 | 2025-10-24 04:17:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84069a6a-fa00-379e-8ae7-7bee5fa1008c | -3.02595 | -49.49806 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d82257ec-73ff-3ffe-94ea-912f2326761a | -9.64068 | -46.88845 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99966c54-951c-3809-b579-92d34ee9bede | -11.16752 | -44.68641 | 2025-10-24 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| befa237b-6fea-3366-badb-b178363ea6d9 | -5.81636 | -46.21779 | 2025-10-24 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 757e0333-28e9-37f5-8adb-41ade0390116 | -3.13973 | -50.61834 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 530d3e3f-c9e9-3312-ac5b-c3d7845037ce | -10.27311 | -47.8787 | 2025-10-24 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0518cf61-58bc-3e76-8713-bfa5497542df | -10.65281 | -44.72565 | 2025-10-24 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2e8ffa29-cc94-35d9-906b-92ba53bfdc68 | -4.84806 | -42.95598 | 2025-10-24 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac106b80-9cad-34d2-8d90-f947712ac551 | -4.24131 | -48.20355 | 2025-10-24 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bf431ca-9f59-3dc4-aeb3-04d5efb045c7 | -11.47818 | -43.24574 | 2025-10-24 04:17:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README17.md)
