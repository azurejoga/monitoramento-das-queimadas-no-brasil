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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71e42a9c-2c1f-3225-929a-519ac53cba98 | -6.31273 | -60.01344 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a99a56d-fca9-368f-b5a9-e3d3f54adcf0 | -7.59698 | -57.67405 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e70fe3d-0d70-34c6-baf2-612b75ae6865 | -7.57481 | -57.68479 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf001979-0b9e-3bd9-bddd-8b5afd781a54 | -3.46931 | -59.55104 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5612795-1a3b-3456-9826-748f2afe9a67 | -11.75968 | -50.82313 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56736a66-287f-3bcb-919e-305164f7ab84 | -6.62561 | -59.92796 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| a4658900-169f-321b-9c41-4a6b9bd3bfec | -7.08548 | -61.08366 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 740ce69c-df2c-31ad-97c0-59190e45e656 | -3.75635 | -59.4221 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 451894e0-1af1-376f-adba-298561a6ed92 | -7.58367 | -57.67193 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4721184e-000d-316f-b971-1c3c872f58f8 | -8.31529 | -44.75048 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 396e5f3c-72b2-3d28-9f4f-a31aed395c7e | -3.00573 | -54.17401 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca00a4fc-74c5-396c-b2a0-5d49d6761d83 | -11.87812 | -46.85393 | 2026-09-22 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f7aa96cd-f0d2-3b1e-9ffe-8e51058247c5 | -11.32938 | -51.35933 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd8541e1-2972-3b2b-9406-27c38e02e619 | -3.40491 | -59.58634 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88a4dbef-1a46-31ab-857b-14b8f5da7373 | -7.58202 | -57.68238 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5f998b5d-70e4-35ba-898f-bb5279c0a787 | -6.42967 | -55.61036 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac3de2cc-2794-3165-8c4d-17a1d65d8d7e | -3.03439 | -54.40904 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad4cd3fa-7ce6-3ed7-865e-b0321c50fa17 | -6.73662 | -55.09219 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 070767db-18ec-3bb2-aa02-26f3e9c8e0e6 | -6.03953 | -53.27163 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e73c2f73-e7b7-3754-93da-8699576f6cc6 | -3.90319 | -51.88755 | 2026-09-22 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b846b02-63c1-39db-84e8-02035af46078 | -5.7255 | -53.45913 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f3cc01d4-e1a4-3ac6-9806-263013a86f3c | -3.30116 | -57.86427 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43b5e5a1-3640-31c0-af9a-e51c21cd684b | -6.42625 | -55.60983 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33a4a9b6-b1c3-314b-b7b6-b84ae72631f5 | -2.86468 | -57.79931 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 27392366-774c-3385-a9a7-aff20caec70f | -5.7553 | -45.08832 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| a1c2d73d-1ec0-3c1b-84e8-d865b3140632 | -3.0522 | -61.26336 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2f5ce9d-0168-33f4-888e-83f04219576e | -7.3851 | -51.77251 | 2026-09-22 05:23:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ed4ce51-0321-397a-9df0-51906380e6a5 | -3.38644 | -50.43852 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a25e661b-ab1a-3136-b922-bf39ebee4d7f | -6.75053 | -59.07139 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ce3d886-a7c6-3763-b5b9-bc04ff4500bc | -7.5942 | -57.67004 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e2262f1-2e2a-3b2f-b418-e65c8d8aef16 | -6.64159 | -59.91853 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a302e5a4-8c52-31d5-b93a-439646386e8e | -9.6135 | -43.93815 | 2026-09-22 05:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4b5c354e-4086-3251-9792-1e1c58bece63 | -8.39472 | -50.24808 | 2026-09-22 05:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf83bb69-7cb4-3cc9-97c1-6cfd37e2018f | -6.6784 | -59.10915 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7764c143-3236-3437-8c5d-c9b24b03de8f | -12.93694 | -51.04182 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c9de589c-e59e-3c6b-ba1c-2bf06422b8f1 | -5.45778 | -49.01696 | 2026-09-22 05:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 313ec0f5-b575-37a7-9f79-c7aa3ec608b4 | -6.00479 | -45.24368 | 2026-09-22 05:23:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5faec90d-e1a8-35d4-93da-2451b5472b26 | -4.30744 | -55.59169 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc129ab0-a1b5-3fb5-8622-eec06d4c1893 | -4.56593 | -54.91992 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aafb3d6c-a928-324c-8331-9a716b208f27 | -3.38223 | -50.4075 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1e6c7d19-6a7f-36ec-ac1a-cb357b66fd1f | -7.5809 | -57.66792 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a68ad18-ca55-3495-b4d4-c56826286291 | -6.17643 | -56.13576 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 388a4b64-1b34-33af-b045-6afc264a92a9 | -6.07051 | -57.86996 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72695118-957d-3faa-8e08-85aaabbe17d1 | -7.42116 | -49.84795 | 2026-09-22 05:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 95a4eb4b-7d73-3dc7-90d7-b3f5ee538d73 | -5.94071 | -57.70641 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a873541-fefa-3355-8fac-207f31d239b0 | -6.62209 | -59.92738 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e9d9b172-160c-3e08-ac30-c2f481ef2b7f | -3.41502 | -61.29698 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17d2a85e-33d9-3487-a769-a2a10a6f88ec | -11.67952 | -50.98542 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fdef7174-4ad1-357d-b49b-a5ee0656463a | -6.25299 | -57.78432 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fea7bb6-5eda-3678-9bb5-460201a2a3fa | -12.93392 | -50.92879 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 8ffdfe07-9051-34ed-bed2-8fd455ca168a | -6.13268 | -59.93998 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c71ab0c-8f89-3ffc-9efd-3eaf69899e5c | -6.13292 | -59.96048 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bd5aca3-cfbf-39e4-9a6f-17f5e5564774 | -13.86785 | -48.58242 | 2026-09-22 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88768e4a-b358-300e-b374-083586cbfb45 | -5.99831 | -45.24287 | 2026-09-22 05:23:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bb54c29-2911-3064-acf3-1217039ca9dd | -13.52262 | -51.51379 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 7df18160-93b8-37a8-a070-64ffe13aeb27 | -6.72969 | -55.06739 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1cdc437-0ae1-3ac1-a559-9cec1b712111 | -3.90264 | -51.89108 | 2026-09-22 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f8f7980-f203-3d99-a550-78fe6b328353 | -5.89377 | -53.64445 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14c44aad-dd53-37d4-96eb-431dad410591 | -6.1446 | -59.93378 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abc6337e-e504-3399-8042-826afee8583d | -4.41448 | -55.24556 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77bdbf7e-f221-3b27-addc-2f6d58f8b4eb | -4.5377 | -54.96556 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a494f635-98db-33d3-81df-a1bb4020f6f4 | -2.9766 | -54.15359 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b92f0dc-8fe7-3291-887c-1ba20864a118 | -2.66406 | -54.96789 | 2026-09-22 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f1add5b-82ee-3e54-a559-5cf9bd452cf8 | -13.30267 | -51.79346 | 2026-09-22 05:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4d555af-937d-396a-9fd9-72b242c07e7d | -3.49547 | -59.5831 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bb64bf3-3a78-30dc-b5be-6bc71c2f6677 | -8.83186 | -50.49632 | 2026-09-22 05:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 68118057-8580-3ced-993f-1916af785b7f | -7.56137 | -55.01963 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7369614-2311-3e8b-89c2-bd4b0ba2b508 | -2.90597 | -48.90348 | 2026-09-22 05:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d51deeb9-b6a4-38bc-ba46-9f5752bdaf94 | -11.68435 | -50.98886 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f73bf79c-bdc0-3029-948a-b21a43dab6d6 | -7.60675 | -55.34129 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0cb20a3-7bde-3f58-89f4-481dcd709fe9 | -2.92954 | -57.79111 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 263e8879-24f0-3305-93a3-27245ecd29d7 | -5.83087 | -52.04472 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6639261-795a-3afa-b689-fe6910a539b7 | -1.37827 | -55.22228 | 2026-09-22 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6b8228b4-3628-30ce-9c29-d0523395fb31 | -3.63367 | -59.73763 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04d43210-c1be-3e24-a7f8-2a68623730c1 | -6.1413 | -55.69461 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99a2a347-5ce7-3f28-8e98-8ee3c71f7a94 | -13.51787 | -51.51317 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 33.6 |
| ee5bfa87-dbda-3fd7-84e8-ac45c0e31324 | -5.80457 | -53.5241 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e515561-6dc0-386f-b6d8-a6d3cfce99fe | -6.13226 | -59.96447 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 60563366-c8a3-3747-b0bd-22e4c96dffa2 | -5.75644 | -45.08834 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 88dcbd57-059b-3dd0-8f7c-56ffeecce99d | -3.33031 | -59.81644 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 736adf4a-1fed-37e0-bd46-7e504a809baa | -1.68145 | -54.93523 | 2026-09-22 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f452d8a5-e774-33ce-9c49-8e9285f8d5f7 | -4.67989 | -55.62326 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a7409c89-58b0-35f3-9a0a-b9e21346fe5c | -4.4466 | -55.59861 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0aed99ab-679a-3123-a149-56cd65249ea2 | -6.29956 | -59.93792 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf8491f9-a87f-3827-a712-c7d30f395b83 | -6.35533 | -55.84259 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e8438fb-5b0c-39f7-bdd7-695f8295ce0c | -12.02791 | -47.81379 | 2026-09-22 05:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f56456f-fd92-3dc7-a406-0fb7330eaa7c | -5.85885 | -49.78101 | 2026-09-22 05:23:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2914377f-2d60-3a16-8a0c-8d81ff9b724d | -5.87233 | -52.06547 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7f75095-b22e-37fe-b3f2-63df30feb660 | -4.5154 | -54.98195 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d470b01c-4966-3cbb-8a02-0dfc642ff0fa | -4.08917 | -62.0841 | 2026-09-22 05:23:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59a85d95-3d3c-318a-b0d5-607fb5d92235 | -6.09777 | -57.67772 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c74781c6-3dcc-38ef-bdb1-9fad9a9b6dbe | -1.69529 | -57.40538 | 2026-09-22 05:23:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 361b2551-8e10-3015-bccc-69ef0bb5ccf1 | -6.19751 | -57.77565 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 31371e1f-81a0-342f-885a-8d88f43c69b0 | -7.32776 | -55.60095 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7dcc679-cf46-3e56-8ed9-bab508aecd93 | -7.35628 | -45.34109 | 2026-09-22 05:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1d0fdde-c178-38d2-97f1-d84e2cd1ca5b | -5.92829 | -57.68248 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa1aeaf7-e7f6-34e2-8fb0-a9a3c57e517a | -6.28422 | -55.2677 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed7d62f7-64d1-35ab-ba3f-d8b6621ea85f | -6.13556 | -59.94455 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56e73aa6-0a9a-3d41-b402-1068f9f03444 | -3.75245 | -59.31232 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0a61c51-a713-39ba-9b46-c462f62032b0 | -12.94698 | -50.92021 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README87.md)
