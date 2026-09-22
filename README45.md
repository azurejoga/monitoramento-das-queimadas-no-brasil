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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9697d534-bffd-3b0b-9db4-39917ec6d634 | -6.7442 | -55.09277 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22bd0322-6501-3a6d-ae2a-e75a3677395d | -5.45672 | -49.01709 | 2026-09-22 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d82fb468-981f-3358-b945-048fe22e2533 | -7.58277 | -57.68363 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6736493e-da7a-3efa-af85-922d98f359f1 | -10.2606 | -49.98202 | 2026-09-22 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b3e39f5c-ef6c-381d-aac2-73a24988514a | -7.23089 | -55.58554 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c5d6e75-74bc-372d-8f6e-8a6aa6f77bb7 | -10.24924 | -45.49964 | 2026-09-22 04:46:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df0e68f1-ddff-3393-b493-775afc2aa620 | -8.34361 | -50.83191 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 571f1fce-f903-3d23-9c19-00e9e9ca585b | -7.39637 | -55.22416 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d7e3da3-5684-3683-b978-0c5b8a2492b8 | -5.98471 | -44.73151 | 2026-09-22 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9d2fa96c-52a6-3052-a2d5-1fa0fa715f7a | -8.61733 | -54.63087 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3eb6909-0c4b-316f-bdad-b4ee25f9f988 | -3.38493 | -50.43843 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77fcef8f-1f49-36bb-9824-e4656cf45d7c | -9.72834 | -54.34659 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59671a75-cb49-374b-a55f-2ddbfdd2ff55 | -8.11587 | -49.58426 | 2026-09-22 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36ee18b1-bdaa-3ecd-85fa-9ca07a6220ea | -7.55536 | -42.65749 | 2026-09-22 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d3ff21ab-a1e8-3229-b53b-195ec34f0d54 | -3.8699 | -51.18685 | 2026-09-22 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 056dd217-832d-3c69-ab44-49a314d13d46 | -6.47191 | -48.45401 | 2026-09-22 04:46:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eac92382-9e74-326a-821c-6b01c5c25f61 | -6.31058 | -57.74846 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f4eebe0-0711-39b3-8a8c-57d8795f789f | -3.05527 | -54.41927 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e20fe84-733b-3056-b680-8e22334c0bba | -3.44196 | -50.61938 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ded0710a-8171-3cc2-bd07-dcb6fce8cfc4 | -2.93598 | -57.80456 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7da6b7a7-f8c4-327c-a115-1b18d0a6f447 | -2.95794 | -52.14374 | 2026-09-22 04:46:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bffb1387-0f65-34ff-9799-b473a93e5e6d | -4.51742 | -54.98204 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbb42bb6-e23e-3ac0-b662-75fef2b6bbdd | -5.74996 | -51.93293 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52780e83-c6f8-367e-b568-1a60c9f460c6 | -9.72113 | -53.96194 | 2026-09-22 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3300b03f-f5b0-3d16-9de5-500fc31d2ad4 | -8.26474 | -55.28674 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b36c4842-1f8f-31db-92c2-e93e80c3d98b | -2.56916 | -57.51234 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f706f87d-28c0-33ec-8325-714027a48222 | -6.29723 | -57.74626 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5ec5b462-7978-3e46-8eeb-90b16e0b4914 | -6.22353 | -56.04256 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 283d43ef-0af7-3e75-9bcc-db63bae1e53f | -6.19239 | -57.77991 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9aa86903-b126-355f-9d6f-c50bc195f4b1 | -3.23687 | -53.9497 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6c9fcc6e-f416-3d31-afa2-2657a3e344db | -6.58247 | -44.14604 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1d668305-c919-3341-8017-df85ac181d3b | -6.67731 | -47.73869 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6aaacfcf-bb41-3d8e-8f28-e26579af205b | -6.30632 | -60.0079 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d0ca5fd-5d64-3882-b354-097220d360a3 | -8.91696 | -50.92844 | 2026-09-22 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a94e2890-f2ec-3dd6-a1a2-e41f5ab1efc8 | -2.56389 | -54.73979 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e6ef1776-8de9-35a2-88d5-af4fd065611f | -6.39847 | -55.26167 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16875d67-7ef4-32a7-bd9d-a7ec2684b56a | -5.99917 | -44.72487 | 2026-09-22 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 09323b2e-d0ba-3675-ad6d-abe0cf3442ec | -5.91484 | -57.67659 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d2184f9-030d-3772-93f8-a33acd38f089 | -5.8952 | -52.28725 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 490756ba-8fc3-35e7-9044-ae3012c9a105 | -6.7625 | -48.0429 | 2026-09-22 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c92d48ac-f57f-3784-9d16-463732577e0a | -6.04871 | -57.82593 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 543a86ef-a965-34e3-bdda-b4099673c86f | -6.43367 | -55.61977 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c180bb9d-d75a-3e6a-93e7-d9721e3b3ead | -7.51647 | -45.44217 | 2026-09-22 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2f30ed4-f77d-3b52-bdcf-8b87e0ea6f86 | -8.60157 | -54.61577 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78c3a6ad-bc98-3f70-9e3f-57fa55f94d92 | -10.74565 | -50.81262 | 2026-09-22 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7345eb55-cc91-3cfc-8329-ec4d421960bc | -3.68661 | -60.58188 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3359cad5-71bb-3b21-bf6f-9443f4138476 | -8.15334 | -54.80366 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e352d712-b02e-3c0b-b73b-d660d0cf52f1 | -3.48194 | -59.57087 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4fdbe910-7fe0-379c-bcfc-22d662dced38 | -6.3566 | -58.29194 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 203c5f53-190d-3e9c-8766-1157f40c7860 | -3.00478 | -54.17817 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10f6264c-d24a-3473-8d14-ab187aa6851c | -3.17277 | -51.35865 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 308001d9-056a-3584-acc3-885358b574e3 | -6.64999 | -47.43554 | 2026-09-22 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d128a0b-cee3-3622-bbdc-982f69c51ae1 | -3.39826 | -59.52337 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d21ca0a1-b7ae-3ec1-aaac-545188a14fa9 | -4.0546 | -56.31015 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db8a1d3b-ef3d-3bfd-93fd-4ecd66ad588b | -7.40282 | -44.812 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 529e8e8d-c38d-395d-9980-37e98e02f303 | -4.63855 | -55.7681 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff60fc87-da84-3d8c-bcb0-bc084179c44c | -8.18855 | -54.72399 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8695718-47e5-3264-9a20-863d477be8cb | -6.12803 | -57.40463 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b02ae4b2-1ae0-3b95-a54f-c0c79c082346 | -10.91025 | -47.37888 | 2026-09-22 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 611cb4d8-c7e8-3df6-94cd-f5ef2084c5a7 | -6.74302 | -59.07313 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26a58479-6887-3e72-b15c-054d3ec38408 | -3.40407 | -59.58186 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9acabd10-6be7-3235-9c93-f6ebd75563b8 | -6.73097 | -55.62679 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f85fcd76-10e5-3754-8462-116063084cde | -9.2459 | -46.16648 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a787029e-9530-379e-a10c-754b5088493f | -7.59075 | -57.68924 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84e883af-15db-376e-8fac-6c87ed7ce951 | -3.45125 | -50.60324 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbbf93cb-2173-3a0d-ad28-46e186345865 | -3.06327 | -54.41314 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3b468b3-7927-3ff6-a2d4-ba01e5d8f118 | -9.6611 | -54.33165 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dde36411-9ba3-372c-9b5a-dfc1dcf0b522 | -6.78369 | -48.67091 | 2026-09-22 04:46:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3539f64c-b32a-3fd1-bcbe-922dfaaff59e | -6.57237 | -44.1568 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 20dd616c-7d28-3823-bef2-48956fd39c55 | -7.83434 | -44.97231 | 2026-09-22 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 032a1d1c-d77b-3e3c-be01-5c5cbfe7035a | -3.45624 | -50.61455 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72cd6c36-c125-3168-b3b1-26bfca8c7d09 | -6.39004 | -60.02471 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b4fc900-49e0-3f84-9532-ae9cadb11527 | -5.88072 | -52.05368 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c09b5248-7d2b-3df8-a8d5-6b98c105861f | -6.11602 | -59.88918 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6937084e-1d24-37ae-8d0b-9a27027bae46 | -6.76185 | -48.04715 | 2026-09-22 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b59c8cc-b410-374c-ad00-e5799652d2f5 | -2.56527 | -57.50674 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33f45e6e-ada1-3e59-a857-10ddde26dbbf | -3.38246 | -49.51315 | 2026-09-22 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34ff3295-b98a-3042-bf5c-049e425ba9c6 | -4.41333 | -55.24508 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e2714488-58f9-3907-9565-2967268ac2cd | -6.46561 | -59.98866 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1c94c279-6449-34e0-bd5f-699847533ebe | -6.71221 | -58.99962 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 731dca1f-8021-37a6-b8f9-d40353ea8b40 | -5.01153 | -56.09397 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4503528d-4748-346f-ab55-1dbf28dcd2b9 | -6.65502 | -59.92736 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 968357d9-54ab-308d-8328-8a7a7ae74bea | -7.42663 | -49.85152 | 2026-09-22 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5dc15da7-af85-35d2-b232-8ec5dff9674c | -9.72576 | -48.16041 | 2026-09-22 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a76b76ec-0bf1-3e77-a4bc-857a2990103c | -8.26476 | -55.26399 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e29dbb6-2058-320f-aa68-3f8baf0767ee | -8.32124 | -44.74557 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3595962-8738-38a5-bb7c-8e3ab7713d2b | -6.46579 | -59.96728 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd5a9c43-b37e-31ee-a865-83d6e6dfe3d5 | -6.72329 | -55.08019 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19cd52c0-7efc-3d4b-9760-d67cf15268f1 | -5.88706 | -51.69041 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31448c46-a1ce-353e-ac57-87771d7dffbc | -4.18754 | -51.24402 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0b8d274-8763-35e4-b9e7-a694c8a99f19 | -8.23243 | -54.68028 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d8310dd-ba66-3049-bdbb-e0088a8b289c | -6.64988 | -59.92652 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 8df22470-bb08-3603-a746-95cc30f3da54 | -7.39716 | -55.21946 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ba24655-40a2-3897-aa27-dc09708cd6a9 | -6.90595 | -41.69701 | 2026-09-22 04:46:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ddbef79a-a6be-3877-b409-1aa76ba2e689 | -4.51904 | -55.75879 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4798acc0-e468-35f1-8a44-8fc10a52baa7 | -6.72482 | -55.09433 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1ed53ef-59e9-3557-bfa8-213d7e6b00b3 | -7.57481 | -57.67799 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f70b45c8-417d-3cc9-b30b-1945e28b53d2 | -6.33639 | -55.28508 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94d09e3f-a100-3c2b-89c1-44ab75c60327 | -5.81118 | -57.72968 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ba0cdb4-886f-3c88-ae98-6abb32489385 | -6.62368 | -59.92518 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |


[Clique aqui para ver as próximas entradas](README46.md)
