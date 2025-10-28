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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5720909a-749d-374e-8c35-31cbe01f831c | -7.85433 | -46.39176 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8593cc8-081e-3c50-a63d-3e0b482b768a | -7.07796 | -44.94223 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 343d64d2-e1ef-32f0-b5f4-62d2e6678764 | -7.98811 | -46.74001 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58deb138-1f92-3ee5-ab2e-87656096d6e2 | -10.583 | -49.79369 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c0cc50f1-334e-350f-96f4-00b3ad4e7d07 | -8.15748 | -47.0005 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ea65f0b-fba5-3574-9a1c-2f746386bd98 | -9.13603 | -51.30251 | 2025-10-28 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c08258fe-7437-38ae-aed2-98ed54790bdd | -10.56091 | -49.78587 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2adf690d-2fcd-32b4-ba27-1f6cc6034782 | -10.94384 | -50.27707 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a9a7887-bf4d-32af-8d1e-9e8ecd446cd7 | -9.46295 | -46.87844 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 471fb10d-cbb2-39c2-9544-b34794053e03 | -9.36469 | -49.26526 | 2025-10-28 05:04:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7720f5c7-d38d-36d6-9e1e-cb8808b768e8 | -7.96425 | -46.75455 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6e16f03-feea-3a65-b74a-aafa0bcfa560 | -8.16207 | -46.99879 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc76cf89-7031-3205-8259-d5e010e89250 | -10.29605 | -47.22202 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1359ccc2-6f60-3d23-aa57-4daca928df89 | -7.36568 | -47.79865 | 2025-10-28 05:04:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 898421d0-e4d1-3a1b-8ce3-ef849f61919f | -7.94585 | -45.48759 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c7fc1f6f-0dfb-38d2-bd4c-cafaec2b20b4 | -13.21995 | -47.10355 | 2025-10-28 05:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee3d8304-0079-380c-a413-22632594f88f | -7.99861 | -46.19581 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b16227b-1780-3767-835a-bc7de1ba95eb | -9.56429 | -46.97357 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f963eb93-2bae-3eaf-a227-00ec3ffb5c59 | -8.70505 | -44.42426 | 2025-10-28 05:04:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06993c0a-027d-355c-bced-11c53dd8ec46 | -7.53574 | -46.76366 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41ae7a55-828a-3444-9876-d4fcd99f090e | -7.45735 | -47.02995 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76f35190-807c-3046-8af1-53dc572c7252 | -13.56659 | -48.55171 | 2025-10-28 05:04:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bebd484-7dc2-3920-b96d-c782a45547e3 | -13.65996 | -47.64053 | 2025-10-28 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bed88fa7-0105-3828-984d-cd9ce3e8176f | -7.81545 | -46.47341 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51123add-3bad-375d-9d6e-6467c39039a4 | -10.87935 | -48.38365 | 2025-10-28 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35da128f-0eb3-3428-b8bc-af916aeecf5d | -12.7039 | -46.32359 | 2025-10-28 05:04:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c5cd0ff-8a9d-3764-8788-11ded1fbd9b1 | -7.96918 | -46.75875 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 97f73f43-e6a2-3a3b-8273-680d2816fb09 | -7.94581 | -45.52905 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 745d0138-8e07-3f9d-9857-d1646bfe2d63 | -7.84878 | -46.39133 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e830dd50-1ea1-3261-853f-9c5469cbb6ef | -13.31746 | -47.69518 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 330776f4-5695-39c6-b2ae-12366fea445c | -8.57094 | -47.02718 | 2025-10-28 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db5a639c-8722-3c8f-8541-ca138b94a138 | -10.28349 | -47.23459 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86f3400f-6160-395e-9e2f-3f6666f3486e | -10.57269 | -49.80171 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b646920-b962-35d1-b7a7-611ab38cce99 | -7.46667 | -47.15423 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2f0eb07-8724-39cf-968b-f7543d8ac76d | -12.6304 | -45.08194 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 542c8b7b-18ad-3959-a57c-2497e1aed994 | -8.05465 | -54.92957 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ffd730dc-c7ed-3d1d-9e28-891da131b0ac | -5.82362 | -53.45354 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68507f69-c27f-3ff7-919e-3df3f0ff6b99 | -8.15679 | -46.99781 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7af5677-3e25-35d2-b69c-8b4ec3a68f16 | -6.7482 | -48.6909 | 2025-10-28 05:04:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4c7fb19-478e-3a24-bc83-0130ac54c5d3 | -10.29301 | -47.2458 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9eeb4839-061e-3686-b84b-a6b82281cc3f | -10.34795 | -48.04934 | 2025-10-28 05:04:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a52a75c-24d7-339a-9c2e-48077f91697b | -7.45382 | -49.41277 | 2025-10-28 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e81129ef-2b2a-3dec-88c5-ecda49c1fedb | -7.00249 | -46.99141 | 2025-10-28 05:04:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efe3144f-7d14-3ad1-a461-8d43101debb9 | -5.61542 | -51.78958 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b19133f3-ba1e-3c55-9b25-03e08a65b144 | -7.98549 | -46.73897 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| faa2ab21-7087-3728-853f-00581d7b4d08 | -13.54543 | -49.5775 | 2025-10-28 05:04:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3e89cd51-6b48-358a-8dd2-cb54ee787490 | -9.33735 | -43.09634 | 2025-10-28 05:04:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b81b8693-83f1-3691-b8d0-7b2a0a16b0d0 | -10.56386 | -49.83348 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 01e641ca-7756-3fa9-b73c-f6b2754f95b8 | -11.37678 | -55.12843 | 2025-10-28 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16da04e8-d206-3e32-a660-f07ef11fc0e0 | -9.56476 | -46.96991 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 241e6a25-a56e-3566-a7cb-ecdf96efd91d | -13.22037 | -47.10001 | 2025-10-28 05:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9a25d2b-c0a8-3740-b4f3-a03238180123 | -13.63503 | -46.46775 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ef9b641-5dfa-326a-b597-8fdd354a6bf5 | -9.46322 | -46.88792 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ceba191-475d-3b5c-9cbe-161c50b90109 | -13.31702 | -47.69896 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cf83ed0a-40bc-3430-9cca-c91152a7bc8d | -10.67923 | -47.26202 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f9dc37a-b39a-3139-96c8-6ed73ff8eb07 | -7.2693 | -44.96488 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acf2f5f9-6915-34e1-a912-c53385139761 | -10.33008 | -47.7871 | 2025-10-28 05:04:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0047fb47-9910-3648-9f05-9ede928d8fba | -7.9491 | -45.50397 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 584728bc-ad16-3c85-b9f6-661d82a1c4cf | -12.16293 | -46.56252 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b362417a-647d-36f1-8240-2b60676da7ed | -7.12876 | -55.11734 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68a42a61-fa3d-3de8-aae0-9ec0ab7ae3c1 | -9.53983 | -46.93728 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c2be8078-ae79-3ec6-97ed-5fec54bfe3e6 | -7.76707 | -45.40591 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26d51ede-8f95-310f-8be9-0a0976c89288 | -9.56383 | -46.97719 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ffa5c30-7af4-3b20-ad7e-0984e6f4df90 | -12.65589 | -52.62654 | 2025-10-28 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4ee700b-9911-318d-9f73-5c341ae8e19c | -9.57198 | -47.89972 | 2025-10-28 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0ca40fe-11a9-3eaf-8fd2-5da54219ecf1 | -7.95546 | -45.50084 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01178357-bfe7-3d65-8a1d-4348c3646cda | -10.87262 | -50.1064 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d20c451-b842-38b5-bd60-618160cbcc01 | -9.53998 | -46.97734 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86413eeb-2dd9-330f-b743-d26cb13dea1a | -10.5603 | -49.79052 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58552be1-0c2f-3c24-99f2-14404ecca683 | -10.55803 | -49.83095 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2c35477-c92f-3c65-bed5-c55b75a117c3 | -8.16276 | -47.00137 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9b8ba77-5b48-318b-983d-eabd68ee76cf | -8.15168 | -47.00329 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27e9098f-9913-398c-8dd4-d3df0d6268c3 | -13.35882 | -47.39084 | 2025-10-28 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c7ac94d-a922-3600-9cc5-0ebb34647990 | -7.07739 | -44.94656 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 54ec2892-e6d1-3a03-b0df-c05eeed557a5 | -9.89238 | -44.90608 | 2025-10-28 05:04:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bb4a528-2170-38a0-aa0f-c8bbff353a23 | -7.70459 | -55.49664 | 2025-10-28 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae35d532-bf4a-3425-83a5-2a7334b8ea14 | -8.08484 | -45.96093 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e48a124-e5a1-312a-b8f9-ac5a2fab1786 | -13.2222 | -47.08464 | 2025-10-28 05:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2110a9e9-d3f4-3398-8bd3-f9d9d438093d | -13.62492 | -47.02828 | 2025-10-28 05:04:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d93a467-0c04-317c-9e5b-a9fb75bffa3b | -11.31381 | -51.45869 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0031fb4a-0c4a-3d69-a072-18c6c8ad8657 | -10.28804 | -47.24186 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f00dd51f-43ea-35fb-9e70-0de76e14cab4 | -13.67076 | -46.52335 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb14968d-b15b-3364-b71e-b0dab65e8b01 | -7.97504 | -46.75587 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d39f8cf-9640-390c-983e-d2bf60d216cd | -7.81182 | -46.45875 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d34b1836-964d-34c1-9af2-b3f402f7b65e | -7.97772 | -46.75533 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44c3ad2e-c403-31a1-a52a-534f56597aaa | -7.89346 | -45.70457 | 2025-10-28 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cf939fd-8258-3540-98cf-59405399b489 | -10.67879 | -47.26554 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c535352-e535-3c3b-8683-5df7a68fb428 | -12.18827 | -47.02669 | 2025-10-28 05:04:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4491ac86-91c6-3941-a932-5164a5ab36cd | -10.56708 | -49.79924 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3eaf6d92-6832-3da3-8fa4-dbf5feb7a849 | -12.08171 | -45.6538 | 2025-10-28 05:04:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00420909-8f44-397f-8aa9-f2f946a3408e | -13.63098 | -47.02598 | 2025-10-28 05:04:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ab98a736-84b4-36be-b797-5f56d161f1dc | -12.54716 | -44.93605 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cf02e52-2849-3267-b406-65872c22d7eb | -13.57453 | -48.52976 | 2025-10-28 05:04:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8ed976c-b048-349c-a7ab-4f040a88b81b | -7.97915 | -46.74506 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0007eb3c-e525-3f7e-8023-c7790ecd4b95 | -7.41002 | -47.77787 | 2025-10-28 05:04:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04ae969f-ee0b-3273-bcea-77f232e771a9 | -9.95399 | -47.09126 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad5dd39f-a4c9-3d12-b248-5c3624932deb | -9.22081 | -46.37082 | 2025-10-28 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1606d0ed-6c3e-3da4-a761-4dc3ebeb8adc | -11.92637 | -47.65676 | 2025-10-28 05:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acc0588c-c4dd-357b-9a16-139ed39d2bf0 | -10.36397 | -47.16441 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 485c712a-108d-3c0a-91c5-4ae8d630e289 | -11.79872 | -52.49447 | 2025-10-28 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README81.md)
