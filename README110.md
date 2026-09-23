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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 032ce7f4-5cdc-33d3-932d-002325bccb30 | -2.85853 | -60.9177 | 2026-09-23 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7ae9836-d159-33be-8ed1-ff430d26faaa | -3.69242 | -60.54978 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07f802e4-1808-3f9c-ab81-d08f47f32d0f | -3.41014 | -61.29275 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb1fa340-f465-3dde-95ca-9045e45633e3 | -3.78889 | -58.85797 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f543155c-f0ea-3bbb-aef4-9e7cabcf4e1d | -10.69695 | -48.72153 | 2026-09-23 05:23:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0963fad2-51a5-35ec-b048-dad9250cb341 | -4.86742 | -55.85272 | 2026-09-23 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a90aeb70-f428-32a0-afb4-8ee389e83f32 | -3.42688 | -61.32424 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5a93a54-fd99-3720-bc01-68a8297f406b | -3.83138 | -59.40091 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f750274b-a312-3795-85ac-84583b4f05e3 | -6.18042 | -52.80321 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85828efe-ec3e-3c39-a4c6-6a53f758dabf | -4.25667 | -60.01073 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5110393-f6d8-372c-a674-e037e1560a9f | -3.02133 | -57.93224 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd31c828-01c4-302a-bb63-5b94d237c1b4 | -3.86728 | -57.15099 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8245b73-8a7c-3d69-8b53-020449acd272 | -8.6417 | -67.02587 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c745a7b-e609-399d-a4d8-1cb2ac208c3d | -4.06778 | -56.22594 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9af214bb-6706-34c3-8286-47bd4e3fe237 | -4.45263 | -55.07637 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9eeec723-0346-36f2-8755-91ca4a92caa8 | -9.55753 | -65.98104 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0b4a1a1b-8dd5-35de-8d61-e909bfb8aac8 | -3.05944 | -61.26978 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66c24b21-bb22-3240-8f4e-d6bc0a79b63c | -3.73869 | -59.42926 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 51c69852-655f-3a43-8d0b-995d512ba530 | -2.86371 | -57.79036 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0cd68cc0-8480-3130-8a18-cd484c1e3612 | -6.17305 | -52.05107 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f11822f0-6145-31c6-a376-6387385577c4 | -10.29499 | -50.5251 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3dc0b710-e1e1-3f87-b9af-bd5a340ab614 | -9.65437 | -54.34273 | 2026-09-23 05:23:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ecc3c35-7dbc-32ff-9cf9-9d0d4aec9598 | -10.29781 | -50.5038 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| edc0996c-0f63-355c-9167-3f5885e9735e | -3.68181 | -60.59404 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bdedc11-3d1a-3c46-b665-2bdd23b8b237 | -8.243 | -56.17128 | 2026-09-23 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbb52a07-83d9-3a8d-a6a3-2dfe8d608da2 | -2.70362 | -59.51101 | 2026-09-23 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cc1155a-7a27-317f-8fbc-364621b7bc35 | -2.94888 | -54.08413 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a87b48e-6885-3ab0-b2fd-53881563d7a5 | -3.44967 | -50.61155 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 608dfb42-7715-3701-9810-b859da23192d | -9.11474 | -60.94844 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 94dcab14-69bd-3a80-93fb-5b4c2d07f8fb | -3.06666 | -54.40113 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76a1bbb6-c56e-3bd1-a0b8-d384592ba359 | -1.25392 | -54.22475 | 2026-09-23 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0368b785-c675-389a-9cb6-95b589cbba23 | -3.11131 | -60.71915 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4358e103-43d6-30d1-8232-95d621cb90bd | -5.61885 | -45.24947 | 2026-09-23 05:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 352dd7bc-8ffb-32eb-9a14-0c2d6a0058b7 | -11.08582 | -48.34507 | 2026-09-23 05:23:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 47b4f903-a53b-31ff-9516-3867738f24c1 | -2.56345 | -57.51992 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87f6a58a-d3bf-3ed9-be1e-741421282170 | -4.22195 | -63.07965 | 2026-09-23 05:23:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6a25022-fca6-3b05-bd17-6200ab139824 | -3.07605 | -58.40266 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d84f3ed-c673-3f83-9122-d283814448b5 | -3.11334 | -60.68428 | 2026-09-23 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc0013fd-afdc-3e0c-bb4a-be576a856ce5 | -3.19214 | -60.43433 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d0085d6-015a-3198-b477-3efd7dcc3b3a | -3.44889 | -50.61687 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2e6638d-207c-3f4f-82e0-2f5475a3aa0c | -9.10784 | -61.4383 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| cd428a3e-fdd6-34d0-b0bf-fde4934cb009 | -3.6999 | -57.29379 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5efa4375-cf81-3f06-a0c9-de8d80e0b7e7 | -5.8962 | -52.08844 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 356c46f3-1458-3535-949c-eb3dc9468ac8 | -10.30922 | -50.5085 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 505fb317-c3ca-377b-a8d9-a4831182375a | -12.3059 | -46.39996 | 2026-09-23 05:23:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8924b262-da65-3b54-9a06-d3e4bbc60706 | -10.2934 | -50.54613 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd871066-a781-3678-90f2-63a6b8167ae1 | -3.4713 | -59.57018 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 671aadc1-efda-380d-b5c7-3b4630113c10 | -9.58741 | -60.52757 | 2026-09-23 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5787d716-c20a-3e71-bd98-ed2f0f3378b7 | -12.36617 | -50.15371 | 2026-09-23 05:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 855efe92-4a50-3ed5-8658-0ed133aeef5a | -3.66814 | -55.53588 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8d2b65d-0fb7-3cde-b6fe-700a109f5731 | -11.09216 | -48.34585 | 2026-09-23 05:23:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| eb071d35-12de-3126-82a5-9000e374583d | -3.83361 | -59.38696 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83d1a311-1a2a-3b83-b429-0c1dbb301cca | -10.45109 | -50.36225 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f748c263-23d3-3e21-b574-bb822a488ad7 | -3.90489 | -59.70721 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21f83829-0bdb-3391-ae4d-692097ffb1e8 | -6.84794 | -45.55645 | 2026-09-23 05:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2573667f-143d-3512-af85-dd1612772d96 | -8.37535 | -62.93718 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b92235d5-13df-309d-9b13-7a87fb1121f6 | -3.226 | -60.81473 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dab27c1-2b88-30ee-b056-3f93ab5e7453 | -10.30643 | -50.48639 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a3aef1b-6957-3826-b53c-4ff4d6fa69d7 | -5.80961 | -47.76786 | 2026-09-23 05:23:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65658f06-e30a-320e-9172-46ebaf60552a | -12.41831 | -46.97216 | 2026-09-23 05:23:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98e51db4-3267-30f1-9fc5-52df7895a949 | -3.20137 | -60.42052 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 910d110c-431e-35d2-9ef1-ea454bc46587 | -3.73535 | -59.42873 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 651dbe02-4df1-32b2-b1bd-8e3e49748cbb | -10.30877 | -50.51205 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 42a68f9a-4d47-30a4-8c7f-5d678fbbb6e5 | -2.96933 | -50.39725 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0411691f-7cd3-392e-ad02-fefd41bd4b9b | -9.22012 | -67.39669 | 2026-09-23 05:23:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a2f4c28-ff7b-3a11-bb75-f9f9dd0dcfd2 | -10.29327 | -50.50273 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8e30bc1f-e347-397c-a3f4-477884b2effe | -10.29405 | -50.5322 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6694bfce-b086-3514-ac31-73a28ccd1a7e | -3.19448 | -61.12572 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afd46ff3-8252-34c1-be02-c1a79c84de32 | -6.78328 | -48.68551 | 2026-09-23 05:23:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b7b4e5ea-ea6d-30d0-8283-a430b332ed1f | 0.78607 | -59.19176 | 2026-09-23 05:23:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9831eb4d-51a2-38b2-9fba-28302109f829 | 0.7844 | -59.20318 | 2026-09-23 05:23:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1e3c354-3dfc-322c-9716-eb5726dd77c0 | -3.11742 | -60.68103 | 2026-09-23 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d03e1bf1-c7e4-3de8-bf83-eb39a77f2b79 | -10.29593 | -50.51801 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bb8a290a-cf15-3c2a-aca7-ac0d5e9af0a4 | 1.08074 | -60.67574 | 2026-09-23 05:23:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d05b43e6-bc4e-32a3-9641-d3cf3b78bdb4 | -3.88147 | -51.95531 | 2026-09-23 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c69df0fe-9f15-336c-9ce4-88796604ca53 | -3.0398 | -50.26781 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a089b83d-8be4-37f3-b1c1-b5abf5ba1d5f | -3.58475 | -59.07312 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a47169d-1249-3e50-9f58-6b35ae959614 | -3.50712 | -61.1413 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 094221fa-210f-3e28-b42d-7bb0f3fb219b | -11.10944 | -51.05902 | 2026-09-23 05:23:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 964b39ba-4f0d-3175-800a-07a996974829 | -3.81498 | -59.01414 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cff92e11-f5d2-3c3b-8a69-cbc30521f21b | -8.48898 | -57.61015 | 2026-09-23 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2f31691-a29b-3967-ba3e-659cebb8b8e4 | -2.86973 | -49.62984 | 2026-09-23 05:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3d54d50-44cd-3fe2-a821-6ca186cafa1f | -4.27497 | -55.42696 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80b0d6ec-315e-359d-ae80-8a2841f4a8b7 | -5.81277 | -49.15079 | 2026-09-23 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22ca9455-7304-36e0-9b51-17994a50d716 | -3.83694 | -59.38749 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fda3d630-de91-33bc-9457-6d169ef38143 | -2.94503 | -54.08354 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50e33551-5a14-32be-8586-6255fe8ec568 | -4.55885 | -54.94105 | 2026-09-23 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1cae4cff-a821-31ea-9b75-fd83abde879a | -2.53469 | -57.55105 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc098959-8178-3ade-b5ae-196033d3ce13 | -3.92246 | -60.55845 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daf02542-48cd-3534-839e-7a5dd173432e | -10.29141 | -50.51019 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9c4ac8bf-f190-38cd-a9c8-47f7cada18fe | -8.22626 | -62.84053 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6c03fd5-6224-3cbd-a6c9-15cc6ffa94dd | -3.16158 | -58.12003 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 9615dce4-05b8-346a-baa9-920f74efb3e2 | -3.68017 | -60.58228 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 30df9a56-75c8-33b0-92a1-7fa89b30c026 | -8.02597 | -61.33961 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26960a8b-8103-375a-9de6-6a20d986b81f | -3.76932 | -60.72667 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 786f9432-ffde-3d9d-8081-c21d83f1dd07 | -5.82938 | -50.21525 | 2026-09-23 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36f777c4-3333-3570-be5e-8d1b0ab20766 | -7.56 | -61.4874 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20926a1f-df18-32b7-af4d-ccb31ac114ea | -3.74294 | -58.86801 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf0fffcd-827d-3e1e-98af-5681ae040a4a | -1.912 | -58.265 | 2026-09-23 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecd773a4-9797-397f-99ed-321e4d52e5c0 | -10.2915 | -50.51697 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README111.md)
