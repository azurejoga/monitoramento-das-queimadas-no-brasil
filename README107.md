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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb1d381b-3f33-3995-b75b-f4698082fcbd | -10.41603 | -50.59843 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b9c331b-51e4-392c-bae9-3377e9789436 | -9.21812 | -59.38234 | 2025-09-12 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8931817f-e119-3977-bc11-f487c3d0cf2f | -10.67831 | -48.59735 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 19e8cc33-ff21-39df-b608-28130ac87c72 | -9.06556 | -47.03673 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| af6ed682-e4f3-3899-9f26-ff7709189977 | -10.43295 | -50.61816 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 770d1467-8c16-3089-a334-c61923d37176 | -9.046 | -47.0657 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2df9f5e2-8c94-381c-9926-7599b602bb5f | -11.87601 | -58.81134 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06ea1798-2bca-3789-89f0-5fe60d90f147 | -12.92955 | -48.0139 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ea679c6-2c00-307c-bec7-84053705fef1 | -12.86958 | -47.95156 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a171fa7e-d82a-34ec-89c0-2165d4600d81 | -11.54037 | -50.3971 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| cace4c83-ec9b-3d98-9ab8-c400c4fa54a8 | -7.51625 | -55.0198 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8779d509-5367-3e26-be68-4428c8d406cc | -10.67912 | -48.64137 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d2b0c98-aee1-3907-a178-1572173197ff | -9.45905 | -47.6459 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c16bdd40-d9d4-3c6f-9467-0ed42a7c6c7c | -8.89618 | -49.94345 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7f0e8b33-8fae-32ab-9124-0673b5bfe060 | -11.22773 | -54.99521 | 2025-09-12 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93d8a7d7-24e8-34e8-b9e2-e93228a50aae | -9.91158 | -51.62352 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96427b0d-0a62-30bb-bde8-6af895e70fb8 | -9.72402 | -64.9229 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56737bc8-c951-37d2-b6f1-4865ccd3d16c | -7.57243 | -61.16184 | 2025-09-12 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1606d2d-ba8d-3c8c-921c-34dead0ed6ec | -9.03685 | -47.08609 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7f642653-2392-3e3c-a171-95e96fa0fd94 | -10.56209 | -51.4853 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 46f52da5-7f05-3132-a8b2-d406f2098403 | -11.98304 | -51.15078 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08b6693d-9c54-32d0-b535-27b7cd2f1265 | -11.53161 | -50.60925 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c95a01d5-4d42-3ac5-b7e9-a33758a38add | -9.74767 | -48.34184 | 2025-09-12 05:18:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21b48e60-b597-3099-8a4e-6468031b2efc | -11.53293 | -50.59837 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ecba7bab-8c74-32d7-b05c-2d00b0f737bd | -11.70714 | -50.59815 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfabc6bd-05c4-3676-a6e8-142b039189b9 | -8.08252 | -54.73894 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5af42737-f688-36b1-88b5-d80dd6dbe38a | -9.95853 | -51.69571 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 80b310ee-e4b2-3fbf-a843-31dee3cb6d2c | -9.25687 | -57.06674 | 2025-09-12 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de833f21-4b7e-372d-9656-1005b8e31e5f | -11.52833 | -50.59035 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 8c4f1af2-ab8b-3eef-a74f-eb430b1eb208 | -9.72032 | -64.94418 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff316b48-47e5-3a88-9eed-16c6dd7d6a71 | -9.34386 | -48.95034 | 2025-09-12 05:18:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3e62df7-ed77-383b-a39f-04746ad97402 | -10.08277 | -47.16422 | 2025-09-12 05:18:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a37b50c-cd4d-374d-b694-dfb7034ac3c3 | -7.78675 | -50.78386 | 2025-09-12 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbc8d2a6-184c-32e1-852a-7a762f878569 | -11.01321 | -51.34551 | 2025-09-12 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4bf34dd-7eaf-3fd3-bb4d-c905549f8528 | -11.00803 | -51.34481 | 2025-09-12 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78679469-d93d-3d6f-80c4-15c081f8762c | -9.07203 | -50.50084 | 2025-09-12 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ab97842-dbc6-3083-97e8-b16ab86d8e19 | -9.69543 | -47.55014 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 505e8264-902c-33b8-ae7e-24ddd90fcbd2 | -11.94266 | -51.18217 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| db7565e0-832f-3b51-b0d2-7bf4c7586dc1 | -9.70734 | -64.92371 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f13a366c-f804-3a32-8daa-0faf598b58a5 | -16.24004 | -48.45513 | 2025-09-12 05:21:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3c767917-e98e-3aa7-9ee3-35feec3ab437 | -13.90772 | -48.23354 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b354e898-9a28-3420-bda2-3acf5445833d | -15.69431 | -47.02888 | 2025-09-12 05:21:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c818b0b-4e6f-3f0e-95f6-54781796584a | -17.37662 | -52.91634 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 646e6805-6fc7-37c2-baf0-a7323087c27e | -15.11993 | -48.60918 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 679f8ce5-3661-33f0-9bee-c7f60bb0d03d | -15.14521 | -50.14892 | 2025-09-12 05:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d8d14832-9571-3460-be7c-35b2d6d6e368 | -18.76538 | -48.53249 | 2025-09-12 05:21:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7b660fa-8cfa-34c1-b951-a54efb1a440a | -14.27038 | -54.77878 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40d96aab-28d6-3899-9e84-292bd9aede16 | -15.08739 | -52.43364 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 752c2e44-ab92-3c43-96a2-2af78d1d6b42 | -13.90292 | -48.2735 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 31.3 |
| ae82578c-21e9-34be-bb85-757bf9363a09 | -12.92038 | -54.7508 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3c8cbfaa-2031-38e0-b369-cb70d4a3b3fb | -15.11943 | -48.61421 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2734d613-1593-31cb-bc50-b3fdc60da300 | -15.8801 | -48.18017 | 2025-09-12 05:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51ffa202-d9e1-3c88-a686-b397ebc4df0e | -14.72332 | -55.60848 | 2025-09-12 05:21:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd2c5469-74b8-3eca-8e49-3eae1a695390 | -13.92016 | -48.23487 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f8e714f2-3bbc-329d-84f4-920704c22038 | -14.26444 | -54.79065 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2fe87fe-9cc7-385f-9db2-e396ee0b5ecc | -14.51505 | -53.90346 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c379dbe-b803-3341-9846-771735f9f112 | -18.65861 | -47.65247 | 2025-09-12 05:21:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7fd6eb03-27d5-370d-986b-14945b2cedc1 | -15.78722 | -52.24695 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1f59748f-000e-385d-8288-c2aeaf454efc | -12.9183 | -54.7666 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67b5e9b2-7a3b-31b1-a37d-e085d8dab90e | -15.57728 | -54.76664 | 2025-09-12 05:21:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69f69176-e96e-3d73-93ce-5c6e46019d02 | -14.31979 | -53.33913 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b780009-9eb4-3865-b5b9-5f18f573374d | -14.42313 | -52.92783 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fa783cd-a87e-3fe9-9e98-7424d060fb51 | -12.9209 | -54.74683 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae62285f-b4c5-3a68-9e90-dd7f834e2544 | -15.13303 | -48.60698 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8dc65395-d605-3cd4-90ef-a449cc6b8014 | -13.38701 | -51.82615 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b63e0c0-d1e5-37c1-8aa6-c2b9b2192b8b | -15.08091 | -48.03405 | 2025-09-12 05:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29304841-2396-3c30-af08-4d6a5a0cc1e3 | -15.15487 | -52.46172 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cc3a4045-2f0d-3b0d-9ad2-0273cd2e5734 | -13.9049 | -48.25928 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e559bb08-c74b-335b-9541-981f50a6835e | -12.92408 | -54.75538 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 76267de1-0b34-3595-a762-dfe9c0415265 | -12.41951 | -63.8909 | 2025-09-12 05:21:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2b7a47e-285b-39b9-8f2d-7c2ca574da5b | -19.19913 | -48.00912 | 2025-09-12 05:21:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bce1d7f3-f342-3183-9b4d-fc6eb57c61d6 | -18.78011 | -48.54433 | 2025-09-12 05:21:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7c0fa83b-1608-3c6c-8446-e0e918a6e4e8 | -15.13364 | -48.60115 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9fb5646-49f8-3a18-b192-e6db4db4999c | -14.26499 | -54.78649 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| efe3b705-80b7-3a73-b8fe-30167cf13015 | -15.79352 | -52.24839 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78343f31-d6d8-382d-b1af-6bfb3bb9e20b | -15.15413 | -52.46812 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ef501e75-ed2d-3167-8c32-79d1a7f86664 | -12.9415 | -54.75373 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebc95ff5-fe13-321a-b4ae-74d9f8e007f7 | -18.75059 | -47.6266 | 2025-09-12 05:21:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| edc6bb0f-ec89-342f-92ad-be3537100c49 | -18.75116 | -47.61966 | 2025-09-12 05:21:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4bee0e0c-5f42-30c6-9ccc-94378c0d6d05 | -14.72213 | -55.62093 | 2025-09-12 05:21:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86e90732-3605-3ee3-a129-6b75056b19ed | -18.0628 | -50.73308 | 2025-09-12 05:21:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a14cb49-c5ea-302c-a67f-6e3ccba631c9 | -12.94204 | -54.74969 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79676984-0f4e-3d36-817b-a1423db27d23 | -15.4922 | -47.34404 | 2025-09-12 05:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 230e9148-3aad-305c-a865-b5685d32f13d | -15.11902 | -48.61838 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2e0eede-47e5-33ed-9fad-e16c78d65bf4 | -15.60647 | -52.737 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8740d319-02c0-3a57-bc24-88c15d10d284 | -15.49152 | -47.35127 | 2025-09-12 05:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d94177c9-7a3c-3673-85cc-1694168c61c1 | -14.55549 | -54.52238 | 2025-09-12 05:21:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3ca0cd5-9ace-340b-a24e-226c55dfcf98 | -20.23003 | -49.2598 | 2025-09-12 05:21:00 | NOAA-21 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be98d309-1236-3202-9cfb-4eba2c58e3b5 | -15.58252 | -54.76479 | 2025-09-12 05:21:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04c278f1-253f-3a26-9906-684ea8c67d70 | -14.43781 | -52.92951 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61c42463-838d-3144-8cae-67ff5a317ba2 | -12.92936 | -54.74799 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57b32091-6ce3-37f3-be6e-ac1a834499f9 | -19.24592 | -48.04202 | 2025-09-12 05:21:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a2357c03-3767-30dd-9129-f67a77cecc03 | -14.74334 | -55.61483 | 2025-09-12 05:21:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3efb1f2a-c799-38d7-8819-78aa7ba63396 | -15.14477 | -50.15321 | 2025-09-12 05:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5831e019-f1ba-3bfb-9f0d-62b5dd088e26 | -11.10375 | -68.69419 | 2025-09-12 05:21:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a70669e-4523-38bf-9101-9af42d51eb75 | -14.49828 | -53.92537 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8203141b-44e6-347f-9f0d-a4a6c82c8bae | -15.08194 | -52.43602 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea95b0bb-1b58-34d5-939e-397e399e2c7e | -17.2037 | -50.14853 | 2025-09-12 05:21:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4944c516-7b38-3f72-bc2e-3c7b231bb135 | -11.77497 | -64.94038 | 2025-09-12 05:21:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a892e6f5-412e-32ee-9c1d-c6c47e3fc4b5 | -15.68852 | -47.0126 | 2025-09-12 05:21:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README108.md)
