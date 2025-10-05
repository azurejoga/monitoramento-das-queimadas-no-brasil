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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d557a2c-ef9b-3fa2-bf1f-f325aa23b173 | -10.05217 | -49.20834 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 8d6c2d33-3dc7-30e9-ba1d-c251a832576c | -9.1254 | -44.39125 | 2025-10-05 00:33:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 14f01fb7-c08a-35a8-94c2-77c04b75ec2c | -10.28102 | -44.35617 | 2025-10-05 00:33:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| bf446b12-0742-3625-9da8-3b99777d66f0 | -13.15097 | -50.96143 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 56f626e7-8ebd-3b8b-888a-5006916381f6 | -11.7063 | -47.50612 | 2025-10-05 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 88645fb0-f4fe-37bd-b668-ce9ef59c5cef | -12.46062 | -45.51049 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 5439deb0-79e0-379c-88a2-87f6e69efa10 | -14.67374 | -48.30829 | 2025-10-05 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| af8b29a6-1f6f-31e6-99fa-d9c3fa793f67 | -13.31121 | -48.11757 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 3ae9b8d5-4615-39ed-b1ff-8f60da01b3cf | -14.67231 | -48.36476 | 2025-10-05 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 6b64cfce-8ecb-3f25-9a78-e357cefddcfe | -10.20306 | -48.55832 | 2025-10-05 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a7f64f0b-edb9-3592-aff9-350657c32bed | -15.6015 | -52.50864 | 2025-10-05 00:33:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 6521a4cf-db73-3dbe-80a1-5565699b6473 | -13.14955 | -50.95005 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| ab26e3cf-a23e-31fc-994e-420323cbbf43 | -13.41009 | -44.38894 | 2025-10-05 00:33:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4aa0fb03-c694-350a-8a5f-facfbff87679 | -10.98772 | -46.66946 | 2025-10-05 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 939e58cc-ca54-3cac-80d6-cb247cd12232 | -13.14814 | -50.93869 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| c6f6bb14-0879-370d-a9cc-cf53bbbdbb46 | -12.70452 | -45.85044 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 82312233-437a-372c-b24f-a64ec7fd68dd | -15.23604 | -49.29278 | 2025-10-05 00:33:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6e8d75ee-7291-3f1d-a802-a4a284ea2fbb | -10.84135 | -47.19471 | 2025-10-05 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b2aa403a-f2fc-3160-855b-269b239bb3d0 | -15.35828 | -47.99066 | 2025-10-05 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dfaf2889-0537-3ac3-aaf9-ca3cebb88829 | -13.27035 | -47.61173 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 404339ef-e44c-348a-b3b1-0bab6326dc5d | -11.45483 | -51.50894 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c39693c1-27e4-3f48-a73c-3df0ed5bc985 | -10.35904 | -48.16003 | 2025-10-05 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9326afd9-bc65-3e51-9b89-ef0fa55dcd3e | -14.33809 | -45.86043 | 2025-10-05 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 49f1c792-5c7a-33c1-810a-97964ad9a000 | -13.08225 | -47.92452 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5030923e-5e5a-3bcb-9a53-3142d261a97e | -15.11658 | -45.76191 | 2025-10-05 00:33:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4dcf5926-2e46-3589-9ef7-b14655c8dc8b | -8.53222 | -46.32975 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 10efd56b-7dc5-3411-a93a-9c12f9d60fbe | -11.45634 | -51.52058 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7841097d-c3fb-3b21-ba69-1d9656992818 | -11.09823 | -49.85886 | 2025-10-05 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b1242d92-5b8f-3237-b2d2-83c2c2321bba | -15.39119 | -47.96709 | 2025-10-05 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2b4538c3-3f44-3944-816c-2468cef4496c | -11.113 | -47.87572 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 15b3bd3a-9233-380c-bc89-be67f961327d | -13.14524 | -47.97313 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| cb969277-695d-36ad-b78e-a5b55fc11e13 | -12.59941 | -48.15429 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 03129ab0-a8b8-3468-97e7-04037adbf8a2 | -13.28547 | -47.59112 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 652cc675-bee6-3757-81d4-25389c2acf03 | -15.80084 | -46.2809 | 2025-10-05 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 758d782d-2c99-3b8d-846f-b88020753f10 | -16.34771 | -51.45722 | 2025-10-05 00:33:00 | TERRA_M-M | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 8d7b9690-7b36-317e-a65e-92e410bb1972 | -15.29592 | -47.33995 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6daf1bdb-ac0e-31c1-8354-8f4341430355 | -8.81495 | -47.27726 | 2025-10-05 00:33:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 813f53e0-a9ec-3775-845c-4fcfb2a9f8bd | -13.97625 | -48.11857 | 2025-10-05 00:33:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| efd62f34-b5b6-3716-84ac-d5ecc8ddfbf6 | -10.73099 | -47.65299 | 2025-10-05 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 721b344a-8cd8-36bf-b78d-375b9ede8e37 | -12.8181 | -50.53827 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| f6d5e857-5630-3505-86c2-f08bed974c27 | -11.11767 | -49.86584 | 2025-10-05 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| f6f1ab0c-7587-3186-85f5-7b607bf0379d | -11.76358 | -44.7536 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6c4b557b-42f7-3ca6-9dc4-1ac959943312 | -12.78134 | -48.81453 | 2025-10-05 00:33:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 23102bbb-1cfa-3414-884f-413ffc77e052 | -8.95732 | -48.75079 | 2025-10-05 00:33:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 60eed999-ebdd-3590-9472-905785ef35cd | -9.94378 | -43.79315 | 2025-10-05 00:33:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 0b5bd2b9-7406-30a5-81e6-7f01cd85dde9 | -14.9232 | -46.84752 | 2025-10-05 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| aa5ad6a0-c5f4-3ce4-ad56-9fa0fa4d00a7 | -15.58824 | -52.49453 | 2025-10-05 00:33:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 885f787b-06be-31ef-a98c-f1c621bc4d03 | -13.68096 | -47.71943 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 67240415-db9f-3919-b478-231e23fa3d40 | -11.80501 | -46.84003 | 2025-10-05 00:33:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 10a26609-569a-3f98-82aa-4db95c7dfd56 | -14.91432 | -46.84868 | 2025-10-05 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d9f47dc1-4469-35d3-9f95-6d3539747eda | -12.40637 | -50.27941 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7fce2a18-d6fe-3a69-b0b3-4865cee0c617 | -13.74447 | -51.31294 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 983867d7-cf8c-3687-9903-07da4cad8dfb | -11.54194 | -49.80505 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 485b7de1-bccc-3d00-8f48-e751bf30d040 | -12.97102 | -51.0041 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bf39dcf9-cd14-37af-ae83-28a25056eb53 | -8.5566 | -46.26654 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| fbf0e4a8-db36-354c-8dc5-b36502f039a3 | -13.3163 | -48.0892 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 5e7c4610-876d-3854-84f2-fbf7d6ef9a5e | -15.98747 | -50.9133 | 2025-10-05 00:33:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 9e0c0ab5-04f2-3220-a44d-f98ee3880add | -13.5618 | -44.10352 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 85cfa0ad-d141-3e58-82e4-8ce9ccc2559d | -9.98709 | -48.26599 | 2025-10-05 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| accd3575-f7be-3573-9b6b-6215f4679c8a | -11.81476 | -45.09086 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 66ec1056-4bbf-3a75-82f8-71e7117cf951 | -16.34928 | -51.4706 | 2025-10-05 00:33:00 | TERRA_M-M | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 5368d9e2-87c2-307a-b3f3-529693fcf2cb | -12.81295 | -46.85792 | 2025-10-05 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4274885a-6495-3b2f-a5dc-801dd74edb33 | -13.27916 | -47.61041 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 4c0caae1-7b40-36e9-8c33-9589f31cbfad | -10.46762 | -47.81174 | 2025-10-05 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bc50a5a9-4c56-3b13-9021-4fd95d06682c | -12.8971 | -47.32256 | 2025-10-05 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| afa8d848-b3db-3188-b9cf-7773a364cb60 | -16.12096 | -53.97179 | 2025-10-05 00:33:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 047156b8-ff7f-3fe8-aae0-42723c7cb296 | -10.83259 | -49.38543 | 2025-10-05 00:33:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 31e8ffd5-c2dc-3267-9ead-132c00d281fe | -12.58039 | -48.16329 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 58721a35-3f12-34e4-a7b5-cb582adf89d9 | -13.73203 | -48.0895 | 2025-10-05 00:33:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c390a195-81f2-3227-9cfb-ca5e41b1798c | -15.7995 | -46.27157 | 2025-10-05 00:33:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 74c9f0e6-0da7-35b1-8ead-cebcf5a8ab12 | -13.74596 | -48.05978 | 2025-10-05 00:33:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 662f902a-e89f-3cfb-8121-4cfbd6a458b4 | -13.13767 | -47.98342 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| f90d87aa-40fd-3355-98a2-f1e438ef6437 | -11.07014 | -47.90669 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4b2d25ff-c678-3c70-beef-4af656f1d8b1 | -11.85354 | -44.93892 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 9e88b116-3135-3fa2-b093-0b65e11820b9 | -14.33091 | -47.69072 | 2025-10-05 00:33:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 171.3 |
| f6a2ff85-c4fc-30af-bec7-c9ac8641b80c | -14.67107 | -48.35556 | 2025-10-05 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 9d0d2e41-31d1-3daa-804a-2ff685846dce | -8.59794 | -46.28211 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 9ac8949a-e56a-3f23-89a1-938731d57aa3 | -14.32841 | -47.67265 | 2025-10-05 00:33:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 94306289-ac72-372f-b1c7-4eb955f7e74c | -9.04547 | -47.02129 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| faa64e7c-4d2f-3ced-bfd4-7422a3525f62 | -13.44395 | -47.27799 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ce532cf0-2364-3fcd-afa6-2631aea06667 | -11.4476 | -49.71784 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| ad91c4d3-3118-3f3f-9093-42ad2cabc654 | -10.19171 | -46.71986 | 2025-10-05 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fb331b0f-4fd6-38f0-af9c-c154d895a818 | -11.10292 | -47.73965 | 2025-10-05 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 87a822a8-1d86-398c-bd68-b8f307f7c3d7 | -8.58189 | -46.30573 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f933c36d-dfb6-3d0c-85ce-3f7b342546f0 | -8.59644 | -46.2718 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d69ace96-6a3c-3b1b-9886-207fe896ec99 | -11.83096 | -45.06469 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 87f1dd3d-892c-37c4-a2e3-1dd960a137cf | -12.28126 | -49.20466 | 2025-10-05 00:33:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 50a40846-d6b2-3f0f-8731-cd0fb7741ae5 | -15.23866 | -49.31319 | 2025-10-05 00:33:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6cf808e8-7663-3eac-bbf6-5c2fb74ef7f1 | -13.20421 | -48.53593 | 2025-10-05 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 83b684bd-7369-3992-8587-a7a78954192f | -10.35022 | -48.16139 | 2025-10-05 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| edce51eb-3504-3cdb-a5ea-8a03aefe1d8f | -15.91257 | -48.8374 | 2025-10-05 00:33:00 | TERRA_M-M | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 5686132a-72d2-35c0-953e-6f6b02715277 | -13.31245 | -48.12658 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9fd870ae-a736-3abe-ae81-d147c9afa17f | -13.2536 | -47.2355 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4ef3db2c-07af-3754-96b2-175bc5567aea | -14.79797 | -44.90023 | 2025-10-05 00:33:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 0d2e7dee-6832-3e54-9639-7ac4379d352a | -10.21187 | -48.55705 | 2025-10-05 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 1b6d0001-a008-3cb3-89f4-63768b07c08f | -13.13643 | -47.97441 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 17904471-e708-380a-8d0f-37f1ab83b64c | -13.30872 | -48.09952 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 31.8 |
| f0dee7ce-2188-3ff4-9d11-2a08ac7d7ca7 | -13.45645 | -42.38742 | 2025-10-05 00:33:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 48e59ec4-bd83-3b36-8bd0-dfa376b43604 | -11.91398 | -46.25288 | 2025-10-05 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f01d6060-3319-301a-b7a3-e027b1f88199 | -13.30939 | -47.56908 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README10.md)
