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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a44f4ef-285d-36e2-916c-06733fae541a | -13.22472 | -46.94535 | 2026-09-20 04:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b48805b-9bc4-3cc8-8cde-dd4de8cfa145 | -14.79777 | -48.53327 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58835562-e3ca-3abd-88d2-0238df2d2105 | -19.69101 | -44.6145 | 2026-09-20 04:21:00 | NPP-375D | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| aaf2ddfa-9ab9-3d54-8d9e-7da41ce5efa6 | -12.15358 | -47.031 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8aa08779-43f4-39de-a3bc-6aa2d9d932f2 | -11.8688 | -47.6673 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6dfcc236-38a5-3fa2-ba73-29ad137df481 | -14.14027 | -45.56559 | 2026-09-20 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 614c97c8-c37c-3f09-b551-d7b8886bce13 | -15.86834 | -49.9076 | 2026-09-20 04:21:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e06960ea-36f1-30fc-8a30-91ac0dfd52d7 | -11.87826 | -49.00434 | 2026-09-20 04:21:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 714c630d-b93e-3e12-8590-2012471dfa62 | -11.85276 | -46.86734 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae53e9c9-7f7f-37d6-a686-41340719859e | -20.33946 | -47.49588 | 2026-09-20 04:23:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9c6cb2f7-c651-31a2-be52-880d189f3fc5 | -20.34017 | -47.49176 | 2026-09-20 04:23:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8cb40166-99ca-3a02-9194-cb32183c495b | -20.77616 | -47.16592 | 2026-09-20 04:23:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14c8aa5d-2dfb-3d48-b949-2710b54b6581 | -20.2656 | -45.56151 | 2026-09-20 04:23:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38bc039d-7d05-33fd-a7a4-eba50998f02b | -19.87748 | -49.00616 | 2026-09-20 04:23:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8eb5c1bf-4d14-3305-961f-fd42e30c2933 | -20.26499 | -45.56524 | 2026-09-20 04:23:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5091d024-9a8c-3658-bba3-4127652b37cb | -20.3821 | -47.43445 | 2026-09-20 04:23:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 372ccf3b-26cf-3471-b329-405421fe9b2c | -20.87865 | -43.91011 | 2026-09-20 04:23:00 | NPP-375D | CASA GRANDE | MINAS GERAIS | Brasil | 3114907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cc0465f9-01e5-3ac0-bf1a-ba6c804b9608 | 2.51473 | -50.84741 | 2026-09-20 04:36:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6e7427e2-e861-3dd1-b8e3-94c8ddfc7ea4 | 2.65265 | -50.86603 | 2026-09-20 04:36:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 350622f0-4fe7-3ebe-8f29-72424a306a5c | 3.64714 | -51.81319 | 2026-09-20 04:36:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b00e389e-1feb-342c-ab20-49379e158b17 | -5.77836 | -50.1808 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f9855bb-8011-3f44-9abd-05397a256050 | -3.90321 | -49.0659 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 105db485-43bd-31de-8603-c2c0a9c1a700 | -1.25352 | -55.76399 | 2026-09-20 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48f6be91-028b-341c-8577-d957f3a59bc9 | -3.01229 | -54.16699 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32dbceac-4793-3e1f-803c-aab32d65b0a6 | -6.68114 | -43.01311 | 2026-09-20 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97d72f45-ac95-34dc-a6d3-0178c37da408 | -1.25325 | -55.76587 | 2026-09-20 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70becd18-9813-3b2e-9cf3-56b8fbb0cfec | -3.69223 | -60.63662 | 2026-09-20 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14c9f9a3-f97f-3939-986d-fce7c8cb50dc | -2.9114 | -57.79522 | 2026-09-20 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c87f52da-9f9b-363b-b665-243336a8b21a | -6.54772 | -44.92712 | 2026-09-20 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45847958-719b-3693-90ba-be5f792b75e1 | -5.73271 | -51.75915 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f70638ea-0664-3759-9b27-e462a31c749c | -0.51676 | -49.15131 | 2026-09-20 04:38:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24230514-e96f-3154-8d34-d66d6c459a6f | -5.22637 | -49.30358 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 397ace36-dbbd-3e4d-ae23-7c8889c4b45a | -7.1249 | -43.10321 | 2026-09-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 89a9a2b0-6cba-345a-ad1d-b580724751e6 | -5.79295 | -51.86251 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c54b8466-8da4-380d-8577-d967d7dfdfec | -3.33943 | -57.87163 | 2026-09-20 04:38:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c0f3bdca-2ace-3446-a665-3575d95552d5 | 0.69401 | -59.55173 | 2026-09-20 04:38:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 83dda04f-0743-33ba-b4aa-f0d1d0269c7f | -3.4806 | -59.59676 | 2026-09-20 04:38:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71537e08-2b0e-3153-a62f-007de88f2999 | -6.30539 | -47.63389 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3f0af44-e5f1-3a00-bea0-84ab8b08afde | -1.31746 | -49.28083 | 2026-09-20 04:38:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 619b5244-69cd-3e7b-b6ae-e78ca2f2a2b9 | -2.4551 | -49.21752 | 2026-09-20 04:38:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 41d51d88-4f41-3244-b603-d69eed8806c7 | -4.624 | -55.75518 | 2026-09-20 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e86fb363-8700-341c-a210-4f16041b9b30 | -6.51634 | -47.1342 | 2026-09-20 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3caa272-1b37-3264-93d3-ca9641f5f4a7 | -6.54084 | -44.13863 | 2026-09-20 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2312959c-7ee3-36e1-9f60-52dd10649080 | -6.36165 | -43.36286 | 2026-09-20 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 08febbc6-ed77-3d50-84a2-aaffa20e455d | -6.49077 | -47.57804 | 2026-09-20 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4dc6079-2295-3eaf-980c-329bd4b64ef2 | -1.253 | -55.76715 | 2026-09-20 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdacba57-795a-32a1-b3c0-12f88f67f8df | -4.4324 | -49.11195 | 2026-09-20 04:38:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5711ad83-593b-379f-826b-3c63ee237fd8 | -2.86715 | -49.62606 | 2026-09-20 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa77d2a7-3912-3544-b8e7-2d756560a193 | -6.30594 | -47.63043 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd247512-8a68-394a-a823-d98cf882ba16 | -3.12692 | -44.47961 | 2026-09-20 04:38:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2aef6ce3-1eb1-3e68-9032-54e0d0852db1 | -6.31919 | -47.63251 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4725e2be-f88d-3b42-855f-b8b6b9588b52 | -6.61078 | -43.75438 | 2026-09-20 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 52e153a0-fb29-3726-b6b6-09c14774e960 | -5.22748 | -47.57687 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3d55363-4b1d-3728-af49-a06ad3411de5 | -6.02494 | -45.40873 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53613b07-1a08-3fa5-9766-386d394f2b5e | -2.97457 | -54.76681 | 2026-09-20 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0ab42e7e-414b-36ce-8524-c991ced71794 | -3.84056 | -49.05957 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ef8d249-b695-3870-8788-107c239c0e2b | -7.12437 | -43.10677 | 2026-09-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 16e2576c-3f27-3096-98f7-397f1ac70add | -3.95519 | -49.04451 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c00cb81-009f-393c-9660-82619830709f | -6.17477 | -47.4921 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d6f524b-c7f1-3ad8-ad55-c8cc70269e23 | -5.57794 | -45.53769 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edea7b71-8b40-3bfe-8521-91e186a3e438 | -6.31256 | -47.63147 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a29d0811-954d-3e1c-884a-5954cb99fe87 | -5.33477 | -49.23221 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e97f5b8d-aeb6-358c-a881-2765cc1dce68 | -5.58826 | -45.56277 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85b364d2-966f-3bbc-88e7-3115dc3d6fb2 | -5.35374 | -45.74118 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf8241e9-c40f-3b0b-acd7-631127bd0707 | -2.9053 | -54.19032 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a1a1423-acd1-3e29-b520-a2b4116651b6 | -6.71903 | -46.07957 | 2026-09-20 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0878397e-8ee2-3802-aa8f-b0e0c8a45926 | -4.494 | -55.4874 | 2026-09-20 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0507fae9-bed3-352e-ab7c-fcd14d1f04fa | -4.84375 | -48.64492 | 2026-09-20 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c7fed50-e6a1-38ee-bb7f-4a12e8fc4ff5 | -3.06762 | -51.33629 | 2026-09-20 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0130bf1-ea4a-3ca6-a2cf-250738279684 | -6.28165 | -41.77781 | 2026-09-20 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| faa70bed-439c-3aed-9389-949e441e9516 | -7.09661 | -42.08117 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 48a7c83f-4fb6-392d-88c5-6ab0a598c5f1 | -4.07287 | -52.1163 | 2026-09-20 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d943916a-ef9a-3c8c-bf21-145d0ccf0abc | -3.89983 | -49.06535 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0cc0726b-d008-3e7f-be1d-506d0fa0e8dc | -3.96833 | -47.20467 | 2026-09-20 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fdd3bf7-209f-39ba-9637-d439118421c6 | -2.93841 | -50.49679 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48aaa054-94c2-394f-b343-24cc43eccea2 | -6.223 | -45.17759 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47bb9183-6fa9-30c5-83b9-e2660cdfc2d0 | -4.68593 | -46.40097 | 2026-09-20 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a92d9f6b-d76e-3624-8b60-75ccd6238ee0 | -1.25821 | -55.7682 | 2026-09-20 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 781b1c7c-56d4-3bfb-830e-ffc578babde8 | -2.45854 | -49.21806 | 2026-09-20 04:38:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1ae1924e-4641-3e3a-b403-94d399ec0a39 | -2.81606 | -54.71489 | 2026-09-20 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3d2fe38d-9fc0-30c7-b946-48263d1aa963 | -4.36589 | -55.04994 | 2026-09-20 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5fcf2f1c-24e5-36a9-8c24-7147744db4e6 | -4.51229 | -55.46809 | 2026-09-20 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 356ec7d0-4791-369b-bb13-ec351ab447f0 | -5.2181 | -47.57187 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecd68b79-bc40-398a-a0e8-dfc8e4f6adce | -4.78482 | -48.07601 | 2026-09-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d8a98dd-80b1-3a45-bc52-aea870954e77 | -5.51614 | -50.02765 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21fa9bfe-42ed-3bb9-8906-a4f68d5e7cc3 | -5.856 | -49.78896 | 2026-09-20 04:38:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b0708899-e2ae-33e1-8c5e-fb3c898c1726 | -6.17078 | -47.71168 | 2026-09-20 04:38:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df04cee8-b6ae-3b8f-a1b9-dda0d999b239 | -2.87063 | -49.62661 | 2026-09-20 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 999593d6-6597-3cd1-8fec-5e1dbdb854a8 | -3.43168 | -50.66799 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fe2e9fb-282f-3af7-b940-93790b7d8f02 | -2.6133 | -54.75391 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 66b8e578-1aef-3804-92ed-5e10d994663d | -6.14874 | -47.7224 | 2026-09-20 04:38:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8f7bfa2-4b81-367c-826c-0141be0749a5 | -3.04284 | -51.10546 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3cfe1158-dfbf-31f6-b3a7-8a0dee9a41bd | -3.77605 | -49.76904 | 2026-09-20 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 939f7f62-ec14-33ca-bd2d-4a7268cd2e79 | -4.87786 | -45.60063 | 2026-09-20 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fe3ddfb-f19d-3dc7-abd4-e155f2aeb2f7 | -6.51693 | -46.77854 | 2026-09-20 04:38:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e8aa9b6a-00c8-3178-9284-09c989268e38 | -6.17686 | -47.71618 | 2026-09-20 04:38:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee785983-6890-30cc-b9b7-f746bf3dbaed | -6.59617 | -45.8798 | 2026-09-20 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76068980-1f90-3806-bc68-52186f8dfcf5 | -3.42805 | -50.6674 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c72dee7e-6d26-39a6-9545-120a5bc700e4 | -5.79024 | -47.36756 | 2026-09-20 04:38:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66e5f239-cb9f-3b4c-b169-7af36439a71c | -3.89259 | -55.88882 | 2026-09-20 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README49.md)
