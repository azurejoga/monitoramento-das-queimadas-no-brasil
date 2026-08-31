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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 181faf7a-0bd6-32c6-94ec-f61ffeebe142 | -9.94152 | -60.51336 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e40c9d5-a03a-39a3-ae3d-810ec5d77462 | -8.59732 | -54.80926 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47b7d9f8-be6d-3b58-b1cb-9a6ea36bd060 | -10.15602 | -45.7263 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a634431d-3de4-3ef1-b4d1-f0ca8e08ef2f | -9.80364 | -46.44185 | 2026-08-31 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7771e9b-b30c-39d7-9f35-7ff348f270cd | -12.94334 | -45.91709 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9852cb9-38c6-3cc2-b63f-76e494ad7650 | -14.4659 | -53.35182 | 2026-08-31 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8884b2c-ec54-37db-8fd4-1759312ad412 | -9.51697 | -58.38719 | 2026-08-31 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe600323-7666-387e-ab49-93e2884ef3df | -9.93897 | -60.52813 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5991f469-decd-3633-94e0-a00ce166bf96 | -9.70879 | -60.75048 | 2026-08-31 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19f52589-8764-3012-b0b9-804ee1dca8eb | -9.16477 | -59.37306 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc61d7b0-1923-3da8-a369-c76fbe18772e | -8.8727 | -66.78192 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 599a0b3f-31bd-3aab-bccd-010b42f436fa | -11.03158 | -57.237 | 2026-08-31 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 873fc9a2-517c-3579-9a20-77b359ba3cee | -11.214 | -45.09615 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 35e4b51c-8436-3e95-89ff-28a9fc120c36 | -11.2023 | -43.37452 | 2026-08-31 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 4c03144c-9f9f-392d-abb5-479d9c3c4e62 | -10.99057 | -49.68543 | 2026-08-31 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4fb386d-0c49-37e0-b20f-404b31622be3 | -14.20362 | -46.56236 | 2026-08-31 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9710c3a1-c8e9-39f9-a358-ade26d26df94 | -8.03314 | -61.25603 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5c246ea-7bbd-39de-b2ac-d4211ee78449 | -10.74654 | -54.0475 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d8390a37-6fed-3fc9-9eeb-d3e8bfad7f94 | -9.0552 | -65.40691 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f65d365-7edb-3c16-b243-8f4ad786fd08 | -8.59498 | -54.75909 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5df4774e-d1b5-3870-a645-006a6e0eb4fd | -12.13593 | -47.25852 | 2026-08-31 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c499eb4-b895-35ae-a69c-74b8560e2f88 | -9.97014 | -46.31023 | 2026-08-31 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1b52e1a-1dcd-336a-b005-e01c0bf8ff71 | -9.87331 | -60.30226 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecd416b1-9b51-369b-a8be-e5b97fd78629 | -9.00438 | -60.59727 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8430ca4-bfed-391e-9b76-1f4578c2ae27 | -11.20172 | -43.37961 | 2026-08-31 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 130dd4d4-f40c-3d47-bef5-7f2c27fca670 | -9.17803 | -59.62949 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83b78813-4865-3b5e-92ce-055b34eacdf6 | -9.83986 | -64.98178 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 424db61a-b2f3-34e8-bb00-7b0f57b2c420 | -13.45426 | -57.04942 | 2026-08-31 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19a55668-585d-3719-99d6-7ce427f55924 | -8.61434 | -54.78704 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7384576-4f81-36e3-84ab-b0cdeadc4400 | -10.73647 | -54.04594 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0175a52a-e10b-3372-a648-33b7722bd723 | -8.67461 | -66.51881 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 504dde92-ed53-3234-9101-c620f4c0252d | -14.19434 | -52.87429 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58563b77-57de-3665-9b5f-4306063ec677 | -9.00855 | -60.59804 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 073c5807-1695-3aa8-8bda-19af34a93be3 | -8.55476 | -55.27616 | 2026-08-31 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e361874-b61f-371f-8853-9eba32235422 | -9.0079 | -60.60191 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 85eeee63-5e6a-3f73-9873-978cb547facd | -14.3996 | -52.53261 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0bdcf74c-6208-35b8-a5ac-9a040b96d9c2 | -12.92201 | -45.85689 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 386e1332-202c-3c7e-9eb5-90ba56d20fdc | -11.37071 | -45.20861 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c2ae11e-cd1d-3971-8453-dd9694ec13dd | -14.14075 | -52.80225 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82e32e7d-e8f1-3dfa-9f6d-004f42ae4975 | -14.38715 | -52.56727 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a2b197dd-44fc-3548-9881-d40c3909a5a4 | -12.09963 | -47.26558 | 2026-08-31 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c15ed427-c542-336d-91cb-7e0c6c9ec82a | -11.21927 | -45.14941 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b645cc1-b6c5-3ae0-bc0d-7eaee6aa7e61 | -11.16072 | -45.04244 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8144f7a7-59c9-3a49-86b6-2bee5ffecaa5 | -10.80223 | -50.66101 | 2026-08-31 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dee33d3f-9320-3834-9908-1fee8b7ca803 | -9.13824 | -60.53371 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4fabbab-854a-3b01-88a6-10f3fd78bf5e | -14.1823 | -52.88112 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f68b18cf-2727-3c26-a1bd-cdf0966fed6a | -10.83996 | -48.34771 | 2026-08-31 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7cc7df04-13bb-3116-8234-cacc4f0b87ee | -11.92565 | -45.07115 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a257f2cb-fbdf-3491-aae2-b2fb28a1a044 | -10.15958 | -45.72786 | 2026-08-31 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2e66456c-4d41-3812-ad22-04e9a7125bd9 | -9.0709 | -60.41755 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5909ee44-98a1-3038-80cd-507fa59d6c11 | -11.21824 | -45.1095 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2558cd9e-007e-374a-bb78-2eb80ded0160 | -13.06359 | -45.18224 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf9e2713-e26b-30b5-bcfe-f04ac067e1b6 | -11.33613 | -45.1588 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9889d069-27aa-3cd6-9cc0-fc25894724f4 | -14.60239 | -54.12261 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70dba369-94b3-3288-b6b7-3b679b7fd60f | -12.39918 | -46.45368 | 2026-08-31 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7ec20e44-fb0f-3d15-b486-6f0eb56a5130 | -14.2143 | -52.8378 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d53455a7-ea2d-3a1d-96ac-4cf8823d80d1 | -9.9662 | -46.30887 | 2026-08-31 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5b1a5cfe-798c-3db7-831c-adc79d479895 | -8.94005 | -62.37191 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f01abde7-5ec0-3538-9b4a-92db75108333 | -8.94276 | -62.0691 | 2026-08-31 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1686807-ba19-3865-97dc-8e4803442aa2 | -11.48465 | -58.52147 | 2026-08-31 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c2c7243-1919-3063-a43f-ffc60a1ba190 | -10.98059 | -48.41375 | 2026-08-31 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3ad1d16-4fd6-33cb-9a9b-0bb511e84737 | -9.08704 | -53.03481 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfd894e4-e4f7-3a17-970d-bbfeb7d3d7fc | -7.52075 | -61.37391 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ff23c1a9-e9c9-3fe3-9a99-8cc3e0f52813 | -10.73726 | -44.88113 | 2026-08-31 04:59:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad49cc6e-e122-326f-abb2-14074bf8ee7b | -9.93551 | -60.52369 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72f9cfbc-0025-3d8b-9140-d4aa6383cff4 | -10.77114 | -54.04396 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93542cd4-f5e3-3ba0-afa8-ca200b47b794 | -15.67474 | -45.93758 | 2026-08-31 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 363214d0-8fe3-3c21-882b-6eadd62d44f4 | -9.89501 | -60.27266 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26fee2e2-1de1-325b-86cf-7dd9309e96d3 | -12.13991 | -45.83879 | 2026-08-31 04:59:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 524c28cc-e140-3a75-b195-1310194a867c | -14.17869 | -52.88055 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c8cd6fc3-4c64-3593-b9af-15cb9e305792 | -13.46211 | -57.04328 | 2026-08-31 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85ab6f1d-6dd2-3a7e-a1a8-b2f8ecc64968 | -9.40374 | -51.60723 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 003d9dd9-032b-346b-b9f7-9f64940354f5 | -10.13999 | -45.72187 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6c3cc06-913a-3f24-a2e3-2214f05a62ca | -8.8671 | -66.89646 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 04607094-58e9-3089-b577-85095227cd86 | -11.21164 | -45.11599 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bccb133-459f-3b3c-88ce-2aa311196d42 | -15.09519 | -48.10941 | 2026-08-31 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 16fe9ef3-d63f-3b66-a271-ea8094e6a177 | -9.94561 | -60.5141 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c14862d-edb6-3475-ab21-ef979bb825a6 | -11.17471 | -55.09152 | 2026-08-31 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5cbdcfe-10ad-3c64-9f04-0396c1e95299 | -7.5792 | -61.34109 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a56afbc-0a23-36a0-a03c-ab2ecee481c9 | -13.63124 | -51.84538 | 2026-08-31 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8dda274f-feb9-3b32-b430-bccb6c29fbb8 | -10.57426 | -57.50071 | 2026-08-31 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 947f7d58-86a8-360a-b7fd-5045e7be8996 | -9.71721 | -65.00132 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fcabff83-5e70-3ad2-b17b-b02107480648 | -9.84538 | -64.98277 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4e58ffb-2552-3aa1-99f6-14c5fc7f58ed | -9.79634 | -60.16436 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d05cbfae-de77-371d-80d7-5b2168be2ee1 | -10.48102 | -59.60579 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d85a29c1-36a1-3190-88c9-9928a25b58ed | -12.11302 | -45.03412 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7918b0a6-04fe-337a-9796-9489dedb1e31 | -12.92758 | -45.85775 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35ec557b-b686-326c-8fdc-b5b9b2c6199f | -7.39859 | -60.58404 | 2026-08-31 04:59:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71d0e139-01c7-3cf1-899c-64a28bc17983 | -10.56807 | -50.36329 | 2026-08-31 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a30e05c-4f5e-3873-984f-6a32b73ae9e9 | -7.69599 | -63.32366 | 2026-08-31 04:59:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b965cafa-93e6-301d-aceb-e45af59146d2 | -11.16022 | -45.04649 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6325cd0-0320-37ae-a126-9f791aaa761d | -14.39082 | -52.56787 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9c190636-0f90-388f-bf76-22c6a1726aad | -11.68693 | -47.61995 | 2026-08-31 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6a4730ab-6a5b-3e1f-a4d8-7256cf8866a6 | -10.74646 | -54.0253 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 778d22ea-a640-35b4-9e6c-08ec02727d53 | -9.05867 | -65.42011 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48f19fb1-e49f-3f9e-ad5f-3bdafc1e194a | -11.68862 | -54.60091 | 2026-08-31 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4486516e-6e78-302a-8f69-0d96b71d1f59 | -12.13556 | -47.26148 | 2026-08-31 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f12110ea-ef3b-3705-9f72-8f4658b26487 | -9.84503 | -64.98672 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1616bf4f-f246-3652-b597-84849d631a9e | -11.67777 | -47.61396 | 2026-08-31 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 64db7cc8-2dbf-3e11-b5b0-45dda5cdfb38 | -10.75544 | -54.03411 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README53.md)
