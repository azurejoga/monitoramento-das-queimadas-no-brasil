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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 397fcd42-225a-3202-a979-7fd92d1da9aa | -12.42968 | -58.48236 | 2026-06-05 04:44:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dee1359c-f352-36d8-a612-8ca4e86980bd | -15.47323 | -55.84285 | 2026-06-05 04:44:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7a52d5c-e576-328a-8bdd-5047afc67cf1 | -14.77044 | -52.67683 | 2026-06-05 04:44:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e734eb5-cf07-3542-b225-36797e60a01a | -13.42979 | -49.64549 | 2026-06-05 04:44:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d425e174-6bdc-373f-9369-99309c6aba9d | -9.76059 | -50.01302 | 2026-06-05 04:44:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 5942b900-886d-325c-9eba-01b9a789bb14 | -12.5323 | -45.67722 | 2026-06-05 04:44:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4660ff38-26ee-3c44-a52d-593d1c3f56df | -12.44579 | -58.47497 | 2026-06-05 04:44:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc5e7a6b-a029-39b6-b8b3-45c6dede9785 | -11.26893 | -53.97298 | 2026-06-05 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75fd8b9f-7863-34b1-8596-aeac5307219c | -12.03245 | -45.88854 | 2026-06-05 04:44:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f5d3d65-e0db-3d10-a968-735d84a4dd44 | -10.70128 | -49.62303 | 2026-06-05 04:44:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 706bf322-b6cc-364c-9781-27e3ab94161f | -9.37404 | -50.54371 | 2026-06-05 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fde24ac9-c352-3e60-89a5-c1a382ee7f24 | -14.09992 | -59.38225 | 2026-06-05 04:44:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f8c76db-4c98-34b4-a2d7-5be76400dd32 | -14.09886 | -59.38773 | 2026-06-05 04:44:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb05a71d-8389-3bc7-8308-de8aa94f3c84 | -11.55643 | -52.79939 | 2026-06-05 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 984c06a4-893f-382f-91ef-9ef58a410ff5 | -12.44216 | -58.41529 | 2026-06-05 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d3bcd178-4ab7-3340-a7b8-1db568ea70dd | -11.01642 | -54.31421 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c92898e-0d90-368c-8fec-fbb93acece60 | -10.90667 | -54.1395 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c01af23-9122-398d-bc12-0bb1f4d3837c | -12.43938 | -58.40397 | 2026-06-05 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b8d93a9-f0f1-3cdd-9820-d9bbace0b480 | -10.38582 | -49.44617 | 2026-06-05 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d04e727-eec3-3317-a065-4d2e8e64b49e | -10.86619 | -53.73717 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b92f872-2068-3fa0-aa00-1884cd41409f | -12.43819 | -58.48946 | 2026-06-05 04:44:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 92a94383-92eb-32e4-8dc1-063a2767d02c | -14.15299 | -51.59555 | 2026-06-05 04:44:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad62acda-3a78-37fb-821a-dd2dd39f0864 | -10.90743 | -54.13504 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4f050cd-0fd6-31e9-a060-ffebae190ff9 | -12.23059 | -57.27544 | 2026-06-05 04:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f28df40-313b-3201-bee8-b17f54c0ac88 | -12.14779 | -54.65088 | 2026-06-05 04:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a306c03-c5c5-302f-a497-231cea67257e | -11.00526 | -54.31222 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4d3c72e-d916-3382-aaf7-46cd5af16794 | -14.04857 | -53.36873 | 2026-06-05 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6fec4fd-10cb-3334-acb6-7d6b5f27967d | -14.37604 | -45.58274 | 2026-06-05 04:44:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14fd078a-d5a8-3f0e-9810-79c1814d6afd | -12.44292 | -58.49044 | 2026-06-05 04:44:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 927187b2-7106-36ad-b4e7-0cc42571e6d9 | -12.44686 | -58.41633 | 2026-06-05 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2e8373c0-d70f-34dd-b2bf-bfd925043dea | -9.08783 | -50.61246 | 2026-06-05 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba9147b0-9e15-303b-b0ca-0529be09b68d | -11.9999 | -45.35501 | 2026-06-05 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d8121a1-3260-37d8-8f5e-b53c6093cc0b | -11.88086 | -57.82427 | 2026-06-05 04:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 217c182e-7f45-3768-83a8-2169c9319b10 | -10.97716 | -47.07979 | 2026-06-05 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b6ffe30-ee6b-34f7-9c72-b48f4003897c | -13.66625 | -47.75572 | 2026-06-05 04:44:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36fcc3d3-f1de-3488-ba81-57d0e4f42f10 | -12.72811 | -54.73754 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6729626-dcc5-39ab-aeb3-ae047f67d790 | -11.62793 | -55.19114 | 2026-06-05 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ede184af-a46c-37d6-abfc-e47df4738deb | -11.33086 | -51.39384 | 2026-06-05 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 411959f1-e644-3863-bae1-07b8e92d94c5 | -9.08395 | -50.61542 | 2026-06-05 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6c74921-fc02-32d2-8b8e-06f1d0c463f1 | -12.73263 | -54.73362 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 573980ba-9c6c-355b-b484-d5e93fdf31e8 | -9.18151 | -58.06197 | 2026-06-05 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e57f3262-446c-3227-a044-00b5492d4ae2 | -14.15356 | -51.59199 | 2026-06-05 04:44:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdf7c187-86bf-34e0-9e1d-1abfab2f04b4 | -11.54323 | -48.26907 | 2026-06-05 04:44:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83d51213-c64d-3792-a9f0-ebfa24dbb370 | -11.04812 | -49.61575 | 2026-06-05 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8903f89-3ae7-32eb-996e-f34af4b33354 | -9.8057 | -48.23572 | 2026-06-05 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0dd0a9f2-1b0b-3ac8-aeb7-d1636e3c2bfe | -12.09035 | -51.99049 | 2026-06-05 04:44:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 261903e7-24dc-3b2a-9025-23653d726533 | -11.87629 | -57.82334 | 2026-06-05 04:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a3c773d-904e-3ce5-bc09-08c3a78288b9 | -12.73342 | -54.72908 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9f2681f-bbc4-33fa-b467-2e7e207a7ecb | -11.05458 | -56.91937 | 2026-06-05 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8745bebf-26ea-3117-9c01-20f7ff0a9320 | -14.09399 | -59.38668 | 2026-06-05 04:44:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7a55946-46a4-3558-9fac-a2ec73420aac | -11.38764 | -47.8132 | 2026-06-05 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83a61905-3655-3da9-a196-c0de036b8d03 | -11.63792 | -47.87717 | 2026-06-05 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9210eb7e-667e-36cf-9480-242c05a10228 | -10.8669 | -53.73296 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 409cafad-d2ce-34c4-a7a3-5021f0cbb03d | -12.73873 | -54.72067 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7eac2035-72ed-3a89-af9b-0a13a8160ec7 | -11.88456 | -57.82994 | 2026-06-05 04:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a1dd82a0-fcdd-307b-8dfa-f57d3699bf67 | -11.60218 | -49.32836 | 2026-06-05 04:44:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3bf29e8-bd79-3ecf-85d0-a6334297d8e8 | -10.93149 | -46.95725 | 2026-06-05 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 429b82dd-87f7-35e7-aa00-9872fbc167b6 | -11.55925 | -52.80382 | 2026-06-05 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2a138100-afc3-3a14-883c-767aaf9e4e5b | -10.38915 | -49.44671 | 2026-06-05 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fcf8cbcd-0343-3986-bb7a-b2609e14cbcc | -12.09252 | -51.9983 | 2026-06-05 04:44:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4f8dda1-3066-301b-a874-1ba8fd2ade0c | -10.85533 | -53.73528 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 567d746a-fa28-34ee-8229-6b5996740ec4 | -10.85605 | -53.73104 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83c76c71-1ff4-367b-bb22-79df9ed52a39 | -9.89263 | -52.44133 | 2026-06-05 04:44:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6759ff7-acc7-3862-b2ed-a65fb24fd7a3 | -11.00975 | -54.30834 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90932e64-2983-30de-a44a-fc71a0dac39b | -14.37552 | -45.58667 | 2026-06-05 04:44:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d49afaa3-8967-39cc-ac48-8cfd79836a43 | -12.31219 | -54.12708 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2ffd3b2-c5f4-3274-bce1-cb8ad832abe1 | -10.58579 | -46.77367 | 2026-06-05 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4b2a72dd-3633-36ab-942b-dd81091b9821 | -10.85967 | -53.73169 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10746241-717f-3af5-bd8f-890bf65e651b | -9.18247 | -58.05654 | 2026-06-05 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6e5e1c94-7260-3b85-82fe-84fd668f34c6 | -12.02998 | -45.87755 | 2026-06-05 04:44:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47ec71dc-72f5-34ec-b8cd-c2985fbcb69c | -12.43746 | -58.41426 | 2026-06-05 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a64f87d-477e-374d-8aed-4b7a36fe3d6d | -12.44407 | -58.40501 | 2026-06-05 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51dda73f-958e-3fab-9be8-83c5400a8626 | -11.26967 | -53.96862 | 2026-06-05 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4b6ffb7-3617-3f04-9c37-2446181ab49b | -11.75816 | -47.07721 | 2026-06-05 04:44:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6758f0f-c42b-3db4-9be8-33082c0e0d97 | -10.84885 | -53.75155 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00f2d93a-b81a-3417-b450-d874e031becf | -12.44672 | -58.46991 | 2026-06-05 04:44:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fbac5996-7dea-307f-8359-04df6ad7cdb0 | -11.55171 | -52.80648 | 2026-06-05 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 27b2e737-f0aa-3238-9ce2-71f4affd1900 | -12.51456 | -48.27319 | 2026-06-05 04:44:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd6422b3-2b54-3d66-8d1e-5bbf41257020 | -9.0917 | -50.6095 | 2026-06-05 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65e321cb-10cf-3da8-9027-8909efb9f4b7 | -10.32055 | -55.1142 | 2026-06-05 04:44:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ee0ab5f-d296-3120-96be-45173c5c3c4f | -9.88918 | -52.44075 | 2026-06-05 04:44:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fa38e76-f058-365d-9e58-4ed6a2aa7b35 | -11.03915 | -44.31975 | 2026-06-05 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| adfddc70-0dae-3edf-b126-bd4e93bd0d47 | -12.00452 | -45.35187 | 2026-06-05 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f500915f-4ce9-31ad-b839-cf532b271ff7 | -11.0447 | -48.92105 | 2026-06-05 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0273321-1b3a-3a35-bbab-8529dd81e80b | -11.56333 | -52.80059 | 2026-06-05 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59fd023e-a9bb-32ab-b054-22cc9da0d257 | -9.18449 | -58.05897 | 2026-06-05 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 343cf7b8-e91c-3bb4-9ae9-c23521fadeb1 | -14.26993 | -53.24518 | 2026-06-05 04:44:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 53fc628f-df3a-31e1-a889-fdf707465fa9 | -12.44312 | -58.41013 | 2026-06-05 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d142715f-cfac-347e-8812-f826f2f31447 | -14.7738 | -52.67743 | 2026-06-05 04:44:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4321ab5-062d-37f0-958e-2481a42dc2f8 | -9.73178 | -48.42252 | 2026-06-05 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b194af33-4413-3458-9821-4883951cb583 | -12.73049 | -54.7239 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5685843b-f278-3e38-8d3e-04adc0f209e2 | -17.86266 | -51.78325 | 2026-06-05 04:46:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a47d551-1328-3944-a109-04e1f8f708ca | -16.12528 | -58.50758 | 2026-06-05 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3d38ef22-8afd-3aa1-a889-d54b2e6baaa5 | -17.78203 | -50.46662 | 2026-06-05 04:46:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8ca0d75-3c87-387d-bfae-371fb42acc0e | -23.25253 | -55.07764 | 2026-06-05 04:46:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0fdc9afe-a243-3feb-a9b5-bf1103c6c934 | -22.09145 | -47.06664 | 2026-06-05 04:46:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cee54ae8-5563-3a62-aed0-d010bfff3106 | -19.16936 | -55.18422 | 2026-06-05 04:46:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ac046ddb-8cb7-3e94-8ca5-9a1804a13140 | -19.72568 | -54.6544 | 2026-06-05 04:46:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| daa978e7-f8a0-3cf4-95b3-5b0b4e73b5c6 | -20.90313 | -50.43299 | 2026-06-05 04:46:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8fbd2f98-5bab-3606-bf4e-ce749ea5753b | -19.16885 | -55.18693 | 2026-06-05 04:46:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |


[Clique aqui para ver as próximas entradas](README13.md)
