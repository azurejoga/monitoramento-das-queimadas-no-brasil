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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c05e05c0-b547-332e-969e-a5677b6b4604 | -12.7647 | -54.804901 | 2025-09-06 00:15:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c9f7fbf-e28c-3a9f-b038-356831a68256 | -4.8794 | -45.132401 | 2025-09-06 00:15:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6aaa70a2-bba9-30d3-8066-a10e018098b5 | -12.5925 | -48.206501 | 2025-09-06 00:15:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c5e105d-da63-366d-ab26-16b0d670f868 | -15.4975 | -53.620499 | 2025-09-06 00:15:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 867c9dd8-f350-33cd-87c2-90fdc4450df8 | -11.8064 | -47.820801 | 2025-09-06 00:15:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36921e4a-7339-35c1-8f51-ebd1e81e81b2 | -12.282 | -53.862701 | 2025-09-06 00:15:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1855b2a0-37b4-30f3-833f-d411811fa634 | -11.0248 | -55.0453 | 2025-09-06 00:15:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71eccd54-c886-308e-9897-f5bf8f8a5933 | -3.54 | -44.416698 | 2025-09-06 00:15:00 | METOP-B | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 227b1439-3665-3334-b2f5-41bb66cb42c2 | -11.0124 | -55.034 | 2025-09-06 00:15:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 17d8b4b2-d436-3354-92a9-68ebdf213b95 | -7.3983 | -44.713902 | 2025-09-06 00:15:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 15fca153-1922-335d-ac4a-e1d0b6fb4b77 | -12.8144 | -54.851501 | 2025-09-06 00:15:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 09785233-10d5-3137-a87f-b022636daab2 | -10.5787 | -47.814602 | 2025-09-06 00:15:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d623e0c-0730-3885-a732-a9797905014d | -23.9657 | -49.571301 | 2025-09-06 00:15:00 | METOP-B | SÃO JOSÉ DA BOA VISTA | PARANÁ | Brasil | 4125407 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| e15f4d18-89e2-3be4-8350-5deb09a2eca3 | -8.1499 | -52.576698 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b6ee963-e639-35b4-bbcb-2dbdcf5a68dc | -12.3211 | -53.854698 | 2025-09-06 00:15:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50a20b7d-1829-33ac-8c7d-b118756869c7 | -20.1611 | -48.6889 | 2025-09-06 00:15:00 | METOP-B | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 95d598e7-20dd-3498-9e8c-048f09d0aefc | -14.3728 | -48.064701 | 2025-09-06 00:15:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 477448b9-7717-3177-9728-d1e3b647ca7b | -8.8766 | -47.038502 | 2025-09-06 00:15:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef751c17-081a-3ec1-8aa3-01b4a3b03a21 | -5.7781 | -43.6539 | 2025-09-06 00:15:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8fd11f7-8dd3-3e2d-85c9-7a4deb67cd44 | -13.7034 | -48.062801 | 2025-09-06 00:15:00 | METOP-B | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 57bb998c-09a6-3781-ab52-c27a897b061c | -13.4003 | -43.1754 | 2025-09-06 00:15:00 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 42822a6c-9563-3557-afc1-26b1810691bf | -5.8158 | -46.730202 | 2025-09-06 00:15:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dfb29926-cddc-36f6-8d47-9127e6ce3a92 | -2.6523 | -49.5397 | 2025-09-06 00:15:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44cf1b98-6d2f-30ee-9aea-d074b7958628 | -10.1033 | -46.451401 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd6a6e72-13bb-3696-a7a4-983a17662804 | -12.7673 | -54.818501 | 2025-09-06 00:15:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0f676458-d747-3ff9-8c5b-887a979891f1 | -15.1678 | -46.451698 | 2025-09-06 00:15:00 | METOP-B | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 738610df-752b-3489-af03-d9685ac7d579 | -9.7742 | -51.688801 | 2025-09-06 00:15:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 492127b2-1713-3bf2-96cd-9c5f92ec8d3d | -6.2033 | -46.131599 | 2025-09-06 00:15:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35bbdfc4-25ec-3b1d-848c-297148f3503f | -23.9524 | -49.554001 | 2025-09-06 00:15:00 | METOP-B | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| 6ae0a480-426a-39fa-9fbe-0acacdebade9 | -20.3244 | -46.149101 | 2025-09-06 00:15:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8044df32-7d6a-387a-98ba-9e7e79b68ce9 | -5.7952 | -49.2672 | 2025-09-06 00:15:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3da1437b-51c7-3e5b-a69b-3359b5d3d1e9 | -7.8576 | -52.4105 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b15ff67-5ea9-3bf8-85b3-cb7fd9846c69 | -16.342699 | -42.385101 | 2025-09-06 00:15:00 | METOP-B | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 84c9c4a1-4e55-36fe-90c7-79c391f0c264 | -10.5772 | -47.807598 | 2025-09-06 00:15:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9255523f-961d-3e63-a62f-136ade95bcc6 | -14.3867 | -48.128201 | 2025-09-06 00:15:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8fa7c353-d65c-3598-8571-2daa52ba6e0a | -18.0602 | -43.066399 | 2025-09-06 00:15:00 | METOP-B | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 67d32231-2b39-3261-a246-b38c39c8003f | -12.0962 | -50.029099 | 2025-09-06 00:15:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1d2a3a8-d7e6-3e0a-b20c-e5b7202a80fa | -9.8705 | -48.1017 | 2025-09-06 00:15:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd14df27-e5ae-330b-87c9-10e31957dd68 | -10.1192 | -51.479801 | 2025-09-06 00:15:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8d06fd1-134d-3c81-bcdc-63d1dbc7801d | -8.5724 | -49.666401 | 2025-09-06 00:15:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7ac8ad1-c585-3e30-aa76-8b87b29eda2d | -4.1808 | -48.0989 | 2025-09-06 00:15:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7e6b379-149b-3858-9736-0574a0a70a8f | -16.3472 | -51.775101 | 2025-09-06 00:15:00 | METOP-B | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| af5c59e9-47b0-367d-8ce0-35aa792dfa51 | -9.5232 | -51.095501 | 2025-09-06 00:15:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bcd96f3-d9cf-323f-aa34-b92fd4def63b | -5.6262 | -51.601898 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dae5fb8e-a318-360c-aece-91b1a4c1c137 | -2.2707 | -47.8083 | 2025-09-06 00:15:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd1cd115-180f-32d2-9153-4da48f60e118 | -11.8048 | -47.813801 | 2025-09-06 00:15:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc17c466-c17e-3986-9c5e-cabdee0093a0 | -6.8473 | -44.387901 | 2025-09-06 00:15:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61c46ad5-394e-3eff-b06d-99125e3a4213 | -5.9511 | -43.2122 | 2025-09-06 00:15:00 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 19f06c90-4c70-3f73-bd94-980c0beda735 | -16.339399 | -51.787102 | 2025-09-06 00:15:00 | METOP-B | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9a050b0f-3b12-39d4-8838-380efc3d4895 | -15.6487 | -52.312401 | 2025-09-06 00:15:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6ddda8a7-9136-33b4-ba9a-44b3565cc25a | -12.9878 | -44.520599 | 2025-09-06 00:15:00 | METOP-B | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 10dfeadf-f2db-3492-a46d-0068ab41635c | -3.479 | -49.048401 | 2025-09-06 00:15:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6339c1ce-9896-3a07-9144-54de23e90e73 | -5.6587 | -46.1385 | 2025-09-06 00:15:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4764e816-ca57-3409-9af5-e7a3a391e7bd | -13.0829 | -46.852798 | 2025-09-06 00:15:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4688a37b-4995-35dd-8ed0-d19b1656a115 | -11.1872 | -43.5961 | 2025-09-06 00:15:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d4721713-de9e-3a17-9239-034179c780b0 | -12.2867 | -53.885799 | 2025-09-06 00:15:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d341d594-52d7-3357-a348-6bf63730a92d | -13.3538 | -48.1576 | 2025-09-06 00:15:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 60f00071-2785-378e-bfb2-248cf1fc452a | -5.72 | -46.403999 | 2025-09-06 00:15:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 989b4010-a978-39c7-b16a-3fd739d85be2 | -7.5122 | -50.362202 | 2025-09-06 00:15:00 | METOP-B | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28221ab8-06ad-3d82-a32f-23da6f58b391 | -3.7801 | -47.922401 | 2025-09-06 00:15:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cf5e78e-d593-30ba-9537-78fa2c99db21 | -3.5373 | -44.4049 | 2025-09-06 00:15:00 | METOP-B | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8c335a5-a06a-3012-9255-c82375f5d017 | -10.391 | -44.369801 | 2025-09-06 00:15:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6bf7e8b3-c805-335a-9e2c-bc8a2cefc5ff | -22.059999 | -48.776199 | 2025-09-06 00:15:00 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6ad0fe5f-b1d6-39df-b4ef-b98dcf95b243 | -15.522 | -53.589699 | 2025-09-06 00:15:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c7014259-01db-3741-b1ae-ae62ebf04fac | -7.8231 | -44.810902 | 2025-09-06 00:15:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 778471b6-b585-3e1c-9903-39b3cca24606 | -6.6472 | -52.8377 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da2d2de8-3f26-337f-ae11-023a4a44ec2d | -9.4922 | -51.142101 | 2025-09-06 00:15:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06407560-dc9f-301f-819b-68685919cf6b | -15.3813 | -52.918598 | 2025-09-06 00:15:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 66a4ba56-5167-32ca-ad63-db701c2fa4f2 | -8.6598 | -52.0397 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2263b57f-b13f-3dda-a4e1-46edd01321b0 | -12.8604 | -47.146198 | 2025-09-06 00:15:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 681a68e4-2254-3e1b-bed1-f2208b7ee1cb | -18.069901 | -43.063801 | 2025-09-06 00:15:00 | METOP-B | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 76ae6bd6-2136-3050-872c-36322450144f | -6.0402 | -43.3274 | 2025-09-06 00:15:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| ff8b5e93-9546-34b1-8e17-b38ff6de864f | -12.77 | -54.8321 | 2025-09-06 00:15:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 58110cb2-d709-36ed-a94d-66ded7d738c2 | -15.6606 | -52.320801 | 2025-09-06 00:15:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0fd49668-c1b1-3a8f-b74d-bc6c6125c6ac | -16.125299 | -52.980301 | 2025-09-06 00:15:00 | METOP-B | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9a739a88-1395-33d7-8d4e-7e4bcb9ce241 | -5.4215 | -45.028198 | 2025-09-06 00:15:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d397d39b-0ea6-3184-8c8e-0a82f02ff351 | -21.1036 | -48.593601 | 2025-09-06 00:15:00 | METOP-B | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 016d8c5e-f458-30c7-9273-f8c5c1f44b09 | -12.4941 | -45.012798 | 2025-09-06 00:15:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 47c9e82b-60a3-355c-a02a-bd84e201caf2 | -8.8783 | -47.046001 | 2025-09-06 00:15:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e28b15dd-bce9-39e3-b076-9a1d11b53305 | -8.8539 | -50.4762 | 2025-09-06 00:15:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 680fe900-ed4a-38e6-a4a8-c38ee169ec18 | -3.7766 | -47.907299 | 2025-09-06 00:15:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64a6833f-3fba-3856-8b8f-667e49ae6ae2 | -21.569799 | -47.316799 | 2025-09-06 00:15:00 | METOP-B | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 51ff5645-cd65-3603-8909-b0e445a1371e | -13.3906 | -43.392502 | 2025-09-06 00:15:00 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7e1b6454-29b9-3321-be4f-d94d9edd6e9b | -6.0669 | -53.4716 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a964729d-09ae-3ecf-9723-da3503417e52 | -3.0443 | -50.8246 | 2025-09-06 00:15:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c34d04f5-de33-392b-81a2-13b18e413b61 | -12.4843 | -45.015202 | 2025-09-06 00:15:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 01cd24a2-62c6-354c-aedc-4497e62f2441 | -12.3346 | -48.111301 | 2025-09-06 00:15:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f59ae68-92af-3c6a-af64-726cc608e22f | -13.7019 | -48.055801 | 2025-09-06 00:15:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 495d6277-4611-3ee8-ba87-f7608e696cdf | -15.2463 | -47.1716 | 2025-09-06 00:15:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0368d209-8416-374f-90ee-717cf233be68 | -12.277 | -53.887798 | 2025-09-06 00:15:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd4b1b2b-801d-396c-ad49-b37ca56cff70 | -5.9835 | -53.276798 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7da8e47d-d00f-3275-9eea-a66018e44cb7 | -13.1886 | -44.627701 | 2025-09-06 00:15:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f7424a4-33b7-326a-a035-b31b7bee8ed8 | -7.5287 | -50.343899 | 2025-09-06 00:15:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d054b27-f4fb-3e13-8d7f-873854a5e732 | -22.065599 | -47.683102 | 2025-09-06 00:15:00 | METOP-B | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| eb007fcb-5d9a-3483-a302-41ed82ef23f8 | -9.4888 | -51.079102 | 2025-09-06 00:15:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06510e45-4a09-391d-bffd-eadcbb69d4aa | -12.3331 | -48.104301 | 2025-09-06 00:15:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08b1cc93-4669-3431-b3da-ef8726f9f6e8 | -10.6913 | -51.661999 | 2025-09-06 00:15:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c9062c8f-0c84-3393-8d1d-e3c07e68e4ab | -5.7827 | -53.626801 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 553b184c-8194-3d43-b081-1a577287b0e4 | -16.0982 | -45.732201 | 2025-09-06 00:15:00 | METOP-B | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2051fd59-4842-3a89-bbc2-6cea34414790 | -12.3315 | -48.097301 | 2025-09-06 00:15:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
