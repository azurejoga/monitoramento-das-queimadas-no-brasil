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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a524af1-2e19-3326-af81-25a8b15d8d80 | -15.1852 | -46.1179 | 2026-09-29 18:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 517cdd55-b1b1-3bb2-8bed-35657eb9f4a5 | -8.5489 | -44.0502 | 2026-09-29 18:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 3dc80f78-c16a-3eb2-9656-8f70fbe2cc12 | -0.4889 | -49.1327 | 2026-09-29 18:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 5fb61409-1e0a-3ed2-b6de-765c338de374 | -10.7255 | -44.4291 | 2026-09-29 18:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| ff71cc01-f030-3211-b813-4c0bf29eb7de | -12.4346 | -44.1733 | 2026-09-29 18:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| c4d4c7ac-d630-3526-849c-f007c9669036 | -11.8167 | -43.3044 | 2026-09-29 18:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 231.0 |
| 58f10a70-ead1-3922-b268-3f845f527670 | -11.4119 | -43.415 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 845c9878-a767-3b51-b791-0aeaecbcd0c3 | -11.6784 | -43.5158 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 8ae5052f-7afa-32c8-8a64-5dc2df4ff6ad | -11.64 | -43.5218 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 12fabaaa-1d52-395a-acdd-e5487bab364b | -11.1273 | -43.2687 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 113.9 |
| 505478ae-3d92-36e2-878f-a1b620ed32bd | -11.0241 | -49.7088 | 2026-09-29 18:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 7f73d2e6-a1f5-3e8e-8482-a1e20d34498a | -7.8613 | -71.7654 | 2026-09-29 18:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 2e667cb4-77c8-34a4-b073-1a66230b202d | -11.6404 | -43.4981 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 7479810f-fe80-3cd7-a9ea-97fb97a93275 | -14.0915 | -46.3096 | 2026-09-29 18:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 2b298f4c-ee93-3714-b50b-251f0ff21050 | -11.4307 | -43.4358 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 182.7 |
| b54b36a0-b3d4-3485-a219-1a7f5d33962e | -0.4889 | -49.1327 | 2026-09-29 18:40:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 365479f9-d87d-3a1f-97b3-4ee9d6bd4115 | -11.2561 | -43.5568 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| de8712e8-32f0-3176-8be4-5bfba0b6bf08 | -8.8548 | -49.7345 | 2026-09-29 18:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| c83d2f45-24a9-391f-bace-e19bfbedcff6 | -10.7056 | -50.8341 | 2026-09-29 18:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 244.3 |
| 6d5553f4-64b6-3e08-ac4a-8fa2c5f8e15e | -11.2566 | -43.5331 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.0 |
| e6d9a9ca-71b4-3fdd-97aa-e51bbc5a6dc0 | -15.7547 | -46.0347 | 2026-09-29 18:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 128.7 |
| cce2ba6d-a297-3a10-a271-129faa7b8499 | -11.6986 | -43.4654 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 204.7 |
| 533138ec-8564-3031-997d-4aa21886589a | -7.473 | -45.8035 | 2026-09-29 18:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 26994e66-fc40-3241-b868-1e794d52653b | -11.4495 | -43.4566 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 294.3 |
| 6dde6e03-5234-3237-a665-33128b7e294c | -8.2283 | -72.821 | 2026-09-29 18:40:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 4671e62a-241e-30af-93bb-f6886ec62eea | -11.3931 | -43.3942 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| f44e0b8e-44da-302f-9ed5-33167b31ec64 | -11.2753 | -43.5539 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 6f6effd9-7ad8-3e42-be85-c6f30b3c1523 | -11.449 | -43.4803 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 163.0 |
| f5d0ceb9-d91c-3d3d-a8a6-004bf3e07de8 | -10.5197 | -45.3784 | 2026-09-29 18:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 114a088d-299c-3daf-9eb8-e6bdc04e0112 | -10.1051 | -43.9306 | 2026-09-29 18:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| ab0556b9-22e2-3070-8148-727713e0699d | -11.4791 | -49.743 | 2026-09-29 18:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| c34dde99-0e95-3783-93aa-bb3af46b238d | -8.9294 | -49.7706 | 2026-09-29 18:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 758fb98c-dbfc-3f28-ba2b-0b997b00ad27 | -9.0783 | -51.5346 | 2026-09-29 18:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 25310d43-eea5-3a4f-b0ff-c45f2441722b | -0.5073 | -49.1326 | 2026-09-29 18:40:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| f506fa73-69c2-3867-8baf-186b4c46e164 | -11.8167 | -43.3044 | 2026-09-29 18:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 238.0 |
| 52b745c7-a21d-307f-b9ed-625a4796e57e | -14.1309 | -46.2801 | 2026-09-29 18:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 256.2 |
| 2a2b65b0-7e59-3916-b89e-a88f874ab2f8 | -12.4351 | -44.1497 | 2026-09-29 18:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 721894bb-9660-3980-acbc-0c04c6ee5495 | -11.1958 | -44.8269 | 2026-09-29 18:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 10a70256-3c09-356f-9cbf-6bbecd1592c4 | -8.9823 | -44.1633 | 2026-09-29 18:40:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 5c61c8bd-6848-328a-b73a-c0f28dff926a | -11.6207 | -43.5248 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 1ebdba6e-5d2b-3438-8084-37047c68e769 | -10.9637 | -43.8821 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 204.5 |
| 033d9eb7-f6e1-34cb-b3fa-dd35533abf57 | -15.1986 | -41.4228 | 2026-09-29 18:40:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 76.8 |
| 9a4c4756-9c72-3ac8-9222-dd5b8f87fb94 | -11.6212 | -43.5011 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| f6bdc17c-a65d-3c72-9bba-570adfd32a8a | -11.4311 | -43.4121 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| db8d03c2-9d0f-3e06-ab1b-a91886f2c9eb | -11.1815 | -50.6347 | 2026-09-29 18:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 81e095c4-7d6f-3a63-931b-5f10c0690d07 | 2.569 | -50.848 | 2026-09-29 18:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 78.4 |
| ecc03429-1682-3ee2-b2f9-d13f0dd823e7 | -9.8613 | -44.9577 | 2026-09-29 18:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| fd15db17-d04a-3a1e-8ba0-7f1def009f17 | -11.2758 | -43.5303 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 85df58cf-d460-30ed-9f35-0119ac5c4832 | -16.9411 | -42.0873 | 2026-09-29 18:40:00 | GOES-19 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 132.3 |
| 8f72f36f-80ff-3039-a061-abec8f884f31 | -10.6505 | -50.7123 | 2026-09-29 18:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 6932e028-0494-3f78-83a9-c582614c27c9 | -11.4298 | -43.4833 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 226.0 |
| 3400eda8-3a09-3f39-81e2-168d648e9aa6 | -9.9595 | -50.1431 | 2026-09-29 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 5fb22a82-51a7-3206-b2d7-d52ebac63eb2 | -8.5051 | -72.4721 | 2026-09-29 18:40:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 32d47823-aa29-337c-9e52-bd926d493573 | -11.7178 | -43.4623 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 220.0 |
| 249e4354-c5cf-3e27-8527-78bd800f8e7c | -10.8851 | -50.1539 | 2026-09-29 18:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 192.7 |
| ae7e6b28-a00e-3e7e-b46a-a13d030debfc | -14.111 | -46.3063 | 2026-09-29 18:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 86de2864-5072-3e18-a803-0b937ebd1ade | -6.9795 | -71.7732 | 2026-09-29 18:40:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 184.8 |
| 490df4bc-64f6-3096-924d-c18eb71e881e | -12.3363 | -44.2829 | 2026-09-29 18:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| b89e751a-10be-3450-82cb-f31883a2e9cb | -9.0783 | -49.8853 | 2026-09-29 18:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 626a1b34-f668-3224-acb0-85cd2af22c0f | -7.7874 | -71.9851 | 2026-09-29 18:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 252c1459-f7d8-3216-a3af-88d1e8efdba3 | -10.5201 | -45.3554 | 2026-09-29 18:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 40b5726b-bc5c-3e84-ad82-57011d4b892b | -10.2843 | -44.6274 | 2026-09-29 18:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 001b801d-8ad7-3459-a6a4-4f15df8740da | -13.1803 | -48.5409 | 2026-09-29 18:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| e5262054-46e7-3bd8-87e7-cb42435386ee | -9.434 | -41.8356 | 2026-09-29 18:40:00 | GOES-19 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 4855b218-36ba-3669-811c-267550df0da9 | -11.699 | -43.4416 | 2026-09-29 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 254.3 |


