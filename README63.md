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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa53474c-84ff-36b0-a6f5-a56e243f8edc | -10.21109 | -49.88807 | 2025-10-28 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d88785a-9ba1-3306-89f1-db099d2c7c79 | -12.70659 | -46.32711 | 2025-10-28 04:44:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 671ab1d3-0475-3028-a3f0-d88132bf79c4 | -8.267 | -46.8956 | 2025-10-28 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4793d61d-920d-3932-82be-5506d398cd98 | -14.44091 | -44.79909 | 2025-10-28 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 723e8884-af44-307d-b5d2-a8b81a55a5c3 | -9.56454 | -46.97609 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f02b16d-3a7b-3650-ad6a-57073eab25e0 | -14.76414 | -44.95569 | 2025-10-28 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f8540c1-4a96-3f36-9acd-27ce7d164ebb | -10.5718 | -49.76826 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8de37de6-fc39-3f1c-b5c6-19d1fa758b6c | -10.52534 | -44.91962 | 2025-10-28 04:44:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3614c40d-d427-32ad-986b-b84f4ba84191 | -12.64648 | -46.71894 | 2025-10-28 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7f64cd6-b4b1-3cd6-a6ef-a89860292a5a | -9.18545 | -44.61216 | 2025-10-28 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4730b577-0652-37fb-893a-85cac7c40cea | -12.18429 | -47.01431 | 2025-10-28 04:44:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ae1188b-094b-3b7f-a56c-c98c05cddbc8 | -13.72443 | -51.45978 | 2025-10-28 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70526217-a3c7-317b-835d-cec020c85262 | -10.58072 | -49.79868 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa731e00-c1a4-3e93-8423-bb3c7811d282 | -9.99717 | -48.07822 | 2025-10-28 04:44:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2c699a0-5d93-31d4-b8f7-dbbdf26f7410 | -10.21943 | -49.90022 | 2025-10-28 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdcfa726-da5a-3e37-8442-d1c077a6fa72 | -8.5742 | -47.03144 | 2025-10-28 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26d901a0-22c7-3716-91c2-dc7722492ded | -12.95808 | -44.61786 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8de8dfe8-73c0-3de9-9233-7f92f2c60cc9 | -9.35493 | -47.7033 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00fc7513-4177-3032-9303-5259a4c747ea | -10.54651 | -48.01563 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21b962f2-2e66-3f6c-b6d7-8d1395d222a0 | -10.67468 | -48.04657 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c90f3d91-51a9-346c-b2d8-a5abcda759d9 | -8.5659 | -47.01329 | 2025-10-28 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7824ecc-7d31-3528-b2d7-b066df9265c8 | -10.58127 | -49.79515 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d30ea15-325b-3b49-8f07-87b6a34d9f17 | -10.9711 | -47.82185 | 2025-10-28 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 231d6dcd-730c-3200-a288-34ce59aec747 | -14.41714 | -47.85729 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3f3d087-781d-34f4-8aad-87983380406a | -13.2536 | -47.96306 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d700aff-fb01-3d74-b445-015c35afe5d5 | -8.71632 | -50.01247 | 2025-10-28 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e27d57e-9dc6-3aba-91b2-66aada4b4c11 | -13.32063 | -48.34748 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84d21ea7-0eb2-3d7e-b308-9e26907877f5 | -13.62485 | -46.79473 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e154a9db-08da-3b3f-b5f0-822a9aa7e27b | -14.61966 | -48.41348 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e05c0562-7ce9-376a-a0dd-33c7cc7c9dbe | -14.55731 | -47.99123 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcb6335b-b86c-349d-88cf-b55c9d54f1a3 | -12.86794 | -48.63807 | 2025-10-28 04:44:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87280a7f-25e7-305a-ac9f-a2ebf077d983 | -8.7062 | -44.42073 | 2025-10-28 04:44:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0487b230-0515-3a94-a954-3935c0a05ccd | -8.31575 | -47.86149 | 2025-10-28 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9000eaab-beee-31e3-bd3a-cf06739d06e8 | -8.63976 | -45.29037 | 2025-10-28 04:44:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| b7f19b67-aa76-39da-9ffd-a50f06b3ce73 | -9.03741 | -46.94407 | 2025-10-28 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b50a342e-f69a-364e-956b-2443aa38bd20 | -8.63642 | -44.77544 | 2025-10-28 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2526fcb1-0e41-319e-ac49-74f0d2d6b827 | -9.91528 | -47.6871 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80cfc3ea-ef24-3dc6-9e74-0f7c54d7fcca | -10.29849 | -47.17069 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d860d5fb-2e81-3e55-b391-4cc04abe2cdf | -12.89823 | -46.80842 | 2025-10-28 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b5d495b-9481-3871-8d30-b50c5a0f0e86 | -13.56099 | -49.59055 | 2025-10-28 04:44:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9771f0b3-d6ae-3cfc-b81d-7fe7d055104b | -9.79798 | -47.00758 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84131786-faf3-37d2-9184-7e351af51162 | -13.22877 | -47.08017 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51cf45cd-7173-309a-8078-5b1189b4925c | -10.03616 | -47.15999 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| deff9372-e8d5-333e-b8ef-afde479358ea | -9.28696 | -45.22318 | 2025-10-28 04:44:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 937120ec-7398-3593-a6fa-fd71b6d7ce5e | -8.51654 | -47.1973 | 2025-10-28 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1de8035-1028-38ad-b93a-2b340e3ec07c | -11.10204 | -44.02725 | 2025-10-28 04:44:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4023241-5308-383f-9c17-2d3576cf2131 | -13.79623 | -48.65921 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 37f4c25c-a2a2-3aa7-850d-fc95f9b16125 | -11.6049 | -48.5386 | 2025-10-28 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8686018c-cdab-38d0-9cba-32c0d5ff6465 | -9.36004 | -43.59872 | 2025-10-28 04:44:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4b5e2398-a043-3a93-bdc4-24d436b1ea7c | -9.07742 | -45.15619 | 2025-10-28 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08c7a5b0-77d3-322a-bb8c-f13941be3114 | -8.62479 | -51.57899 | 2025-10-28 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b50d4875-b21d-3f13-8c35-57cf1e6fb4e5 | -9.46547 | -46.89322 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae7fb363-3048-3915-95a4-c6f59ff689ad | -9.88895 | -44.89062 | 2025-10-28 04:44:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ca798057-9f3c-39a4-90bf-f37510cff872 | -13.15333 | -48.21591 | 2025-10-28 04:44:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 626cc862-b0e0-33b2-b1d6-7f8a3b6df54d | -7.70631 | -55.49682 | 2025-10-28 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0635e766-6ed3-3215-9e3e-9adb44b5a79d | -10.95775 | -50.27759 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80f8c655-ec48-3f2f-8a43-6d68e2173803 | -8.57123 | -47.02678 | 2025-10-28 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdb9a6d0-1ba3-3f2a-96ed-33b79cd3be78 | -14.5342 | -47.97563 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 172c5d93-63cc-3659-b315-e26a94cca5a5 | -10.3338 | -47.77582 | 2025-10-28 04:44:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 869a1a43-bc51-3aaa-9863-510c5c08acbc | -13.54709 | -47.14117 | 2025-10-28 04:44:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4645f480-a0ad-387d-9dc7-5c6077c0ab81 | -10.95808 | -48.05154 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aeda3e07-f1af-35eb-9b08-8e9cfac063c1 | -9.95085 | -47.10591 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4532807d-41a4-3d8e-8412-303e026cf148 | -9.34056 | -43.09534 | 2025-10-28 04:44:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f7f3af7c-06e5-34d3-b9c2-71755da0bcf8 | -10.62506 | -42.31063 | 2025-10-28 04:44:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| e15e8848-edd5-3f99-a73c-7c238408252d | -13.6707 | -46.51684 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f0986330-b8bf-3570-8f83-1469c39a69ea | -12.70407 | -46.31662 | 2025-10-28 04:44:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8089b7c9-ee85-351c-84d0-ddb0d3495260 | -13.22486 | -47.10744 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1bafca8d-ba9a-331d-9411-89c2612dc907 | -10.85702 | -47.91188 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fafd19b-fed1-3b9f-91a3-2cab3ec0b2a5 | -13.55135 | -44.26373 | 2025-10-28 04:44:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 648c1be0-e4e7-339d-9180-f10707a4d753 | -9.54049 | -46.93731 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6b3ad24-22aa-3e97-8fea-1468bfaf0151 | -9.5179 | -40.31559 | 2025-10-28 04:44:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 484201cb-3fe8-377f-8e99-30c3b0f6974a | -13.86739 | -48.51787 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1a5be08-a83c-3c77-a8bc-2dc6e8a55b75 | -14.77184 | -44.96579 | 2025-10-28 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 534b11ba-047f-3a4a-96cd-5bd72e00fe53 | -13.00179 | -48.77269 | 2025-10-28 04:44:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fdeda74-ff02-3ef9-8edb-e6e9ece57e94 | -9.88482 | -44.89001 | 2025-10-28 04:44:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb62e7e4-f789-32b2-9945-858dfa19c0c4 | -11.9267 | -47.65526 | 2025-10-28 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86761eba-511f-30f8-8356-efb2a4ed39ce | -10.21998 | -49.8967 | 2025-10-28 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d04916c-b251-3bd2-a877-09c1963c1f5e | -10.35916 | -47.16133 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 302fc4b3-f970-3e52-9305-c1a70d44c72e | -15.07905 | -50.53853 | 2025-10-28 04:44:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d11f6e0d-4238-3d4b-a84e-d0027e2a3d73 | -13.56546 | -49.56085 | 2025-10-28 04:44:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64aafd5d-b8d1-385c-ad29-5793c8a46e93 | -12.1905 | -47.02419 | 2025-10-28 04:44:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 389102f9-fee2-38a0-8262-7744030e1a91 | -9.95148 | -47.10167 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa87d2a2-9224-3177-a3e2-0844d789cf1f | -12.08818 | -45.67256 | 2025-10-28 04:44:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13d93d08-e9ff-3d2b-8cb6-4633928d2e65 | -12.08302 | -45.64975 | 2025-10-28 04:44:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1147ba6-7398-36ec-ae55-027595be4d02 | -14.44035 | -44.80354 | 2025-10-28 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b72c3397-6a5a-3464-87c2-e64007406b90 | -8.71797 | -50.00201 | 2025-10-28 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10e360f9-0b4f-3bb4-a4c5-d60da8cec046 | -9.0185 | -43.97289 | 2025-10-28 04:44:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87cbcccf-caa5-3f1c-adc7-001cb2f519bb | -8.24834 | -46.89737 | 2025-10-28 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77cb228f-0984-3fb6-90e5-5531c72f8e6d | -14.53175 | -47.98706 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89806f19-bc29-38bd-9956-bb0c5c8f29c3 | -12.21559 | -46.52913 | 2025-10-28 04:44:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7fc064c-2a24-3025-9c6f-af1f402f6526 | -10.88137 | -47.98778 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 290ceff4-3c89-3950-9280-5e22ea52088d | -8.13737 | -47.75392 | 2025-10-28 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c477256-388f-3481-8a56-1935f3872415 | -10.07388 | -48.20454 | 2025-10-28 04:44:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91579074-6198-3c02-90df-8d714b28264d | -11.04315 | -50.34184 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4101ed78-446a-3f4f-9a80-e72a079ebbf0 | -13.65373 | -47.63519 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e956a67b-6f3a-3030-b054-3c493cedab8e | -9.41521 | -49.33189 | 2025-10-28 04:44:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71ae6988-f056-329f-b1dc-d03dcd418b73 | -15.98903 | -45.65104 | 2025-10-28 04:44:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a5b9c54-a669-3285-a649-4388b0ca51fe | -10.58295 | -49.80629 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2b167fc-a6c4-3b46-8df1-b6b89cbe886d | -10.56012 | -49.77728 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7197f7ed-441e-31d6-ba50-9a82e634a20d | -8.17618 | -47.30748 | 2025-10-28 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README64.md)
