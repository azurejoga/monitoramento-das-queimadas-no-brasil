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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b4296d7-1e08-346c-9e27-150e1bb39312 | -10.92322 | -44.60892 | 2025-08-27 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 074a3e64-6438-3c83-936d-4ca1225f4150 | -12.92903 | -46.31507 | 2025-08-27 04:04:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b82acd6-4d46-3136-8e72-ab9af8458fae | -12.25139 | -45.05553 | 2025-08-27 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2d675f8-e9ca-3719-bfb5-3d1940a94104 | -8.25795 | -45.11778 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 92c5a4cb-2e7d-3dab-ba1c-aceaf031f789 | -12.69575 | -47.34328 | 2025-08-27 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b68b572-2ff5-335e-a0e7-d24ac399ae0b | -7.1677 | -43.85516 | 2025-08-27 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1850ef8-b463-3de6-ab8f-d4ddad62b2cb | -11.03848 | -45.13753 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c1c63864-1dea-3781-9119-50db5652b56b | -10.85948 | -47.32796 | 2025-08-27 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c8dda03-babc-3af5-b56f-830dba63e78c | -7.70719 | -45.76862 | 2025-08-27 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f72f8f7e-9391-3519-b8a7-c1485815236c | -13.45697 | -46.98635 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2001bb25-1e2e-3a40-8eb1-8ceff2fe09d1 | -6.43907 | -44.60344 | 2025-08-27 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c5eb672-37c2-343d-a7fd-dc0a929da2f8 | -9.08907 | -49.56895 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 85530e32-e2c5-3060-8399-cb912a89c225 | -12.75918 | -48.18274 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2deeaa79-26fd-3b72-9e4a-15533281a11b | -8.09571 | -45.01737 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c80bbda6-3b6c-3297-b4e3-3cdc13564c31 | -8.26196 | -45.1184 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ff6d52ba-cd1d-35a2-a22c-9d8ad3802b42 | -11.21111 | -41.5981 | 2025-08-27 04:04:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1d88befd-5dba-377c-9510-1e540e0e529e | -12.93206 | -46.32715 | 2025-08-27 04:04:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7304ef41-e14f-342c-a0f5-4af8fe23fcb5 | -8.45393 | -43.67634 | 2025-08-27 04:04:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9104f946-2b58-35a3-a880-cd612e2e4659 | -8.90488 | -45.71363 | 2025-08-27 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e7902c6-0c44-334e-9e4d-153d31dd2631 | -12.76997 | -48.17503 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cc40ba18-a7a1-36a4-b03d-78f216380885 | -12.70223 | -48.18595 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f61d050a-4cd9-32d4-ae57-4b7aeda7d7a9 | -7.17617 | -43.84953 | 2025-08-27 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3fbaf9ac-a8a0-3ba4-bebb-fa216d379970 | -9.95178 | -46.49443 | 2025-08-27 04:04:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b86760b9-b173-3edd-864e-4bf39fbd7605 | -13.38773 | -46.9197 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 977fd01b-624b-3178-b710-840fb4fa3ff8 | -13.16728 | -45.28913 | 2025-08-27 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84b721ae-63b1-3aed-929a-d49c2f4699e8 | -11.25543 | -44.97502 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d224d5d-0d10-3843-9b3f-a59fe25ae792 | -8.56089 | -51.3545 | 2025-08-27 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7e95d7a-9a66-3897-b941-f8539d880099 | -9.50486 | -46.70814 | 2025-08-27 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfb308fa-7f8a-3a7a-8578-0e5d5919e288 | -10.76246 | -46.38747 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a81ecb33-3efa-3aeb-b11f-b7b44f327ce7 | -7.17595 | -43.85196 | 2025-08-27 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ee3528b-e354-369e-8d78-b379040936cf | -7.64888 | -42.66942 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cfd8d3a3-2ec0-3345-a310-1a18e75ed257 | -8.48018 | -43.65417 | 2025-08-27 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a68204f4-eb2a-301d-9656-3eddc7ceb964 | -12.7074 | -48.1839 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0c1612dd-c27d-313d-af43-aa6712353446 | -12.8975 | -44.64138 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 11f91451-43bd-3f46-8357-97cb3654537a | -8.24816 | -45.14547 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 668b025b-6a36-31e5-bbd4-207209805554 | -12.7839 | -48.12447 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 18fba309-34ab-3d1b-bbdd-cb10467be27e | -9.21346 | -46.72783 | 2025-08-27 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bc87b52-386c-3e7a-b29a-e1ad87568327 | -6.39052 | -45.32217 | 2025-08-27 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ed7a9c3-2523-351c-86a4-a372773270ea | -9.7525 | -45.69253 | 2025-08-27 04:04:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c591950-bb39-3f00-a2a6-13fe57461275 | -13.64878 | -45.70424 | 2025-08-27 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8dafee40-f6ae-314d-a17f-8a243142be06 | -8.45464 | -43.67203 | 2025-08-27 04:04:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85d8c5d8-4048-3bba-b288-2ead6343f8c4 | -12.90065 | -44.66296 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 605b0c1e-d760-31b8-b879-b1e33aab333f | -7.12476 | -43.67281 | 2025-08-27 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1570940b-13a1-3c85-b5e5-3cc8b9108dcc | -6.9613 | -44.0942 | 2025-08-27 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ad209df-e198-324a-9943-53d0d39ad46c | -10.31187 | -46.80822 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56815b77-ec7b-3219-9489-b9a579fe76b5 | -9.09608 | -49.58057 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a82ed78a-7d11-39e4-8154-d08da4871df7 | -8.13566 | -49.58693 | 2025-08-27 04:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3b5fd61c-d877-322c-ad86-40fc3db4c3e9 | -10.31854 | -46.77024 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f44d1013-e90f-331b-9cb2-2c246cee8c4f | -13.45227 | -46.98874 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d258a972-5c91-380c-87ac-ac898d91f0cc | -11.03163 | -52.03134 | 2025-08-27 04:04:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3cc7d087-b8e0-3d3a-9db4-5921530ba30a | -11.25298 | -44.98924 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0aff5f93-6927-3ad9-90cc-83758f9504c1 | -8.8838 | -47.18414 | 2025-08-27 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdb215a8-85a5-335a-a930-09776c8155ea | -6.95666 | -44.09844 | 2025-08-27 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c618ca4-0f4d-3a0b-be99-f2cfc2cc5520 | -11.06219 | -44.59253 | 2025-08-27 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5debc0f7-76af-3661-9859-67eca07fa433 | -12.76724 | -48.16437 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fd335187-5460-36c0-8ab4-cf972beb88cb | -8.87842 | -47.18803 | 2025-08-27 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3276b84-7c6d-3b5c-aa9b-d9a2b5730758 | -11.20777 | -41.59755 | 2025-08-27 04:04:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ba14eac9-be6b-3f58-9c66-977f150a1d3c | -13.60918 | -48.14408 | 2025-08-27 04:04:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c89e18ac-4a4b-3a82-b8b4-a1a2d7fc09cb | -12.24685 | -45.05941 | 2025-08-27 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0effd1a4-fe7f-359b-bba5-3e3527137546 | -9.01482 | -40.34323 | 2025-08-27 04:04:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3de0cfec-7a7f-3a1c-8b4c-9ce2102356e0 | -10.25695 | -42.53004 | 2025-08-27 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a8642d40-664a-3d9b-b146-ce5d6c779156 | -8.86789 | -47.16421 | 2025-08-27 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 136446be-7807-386b-923b-c6a787d88c52 | -7.65721 | -42.66273 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b0e7257c-5c49-38ab-b272-a8361694b7fb | -10.82104 | -46.37183 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cbb9fb6-6411-37c8-9456-b21fe134a0c0 | -8.15741 | -45.05075 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da0578ed-31ac-3b69-af00-f8faae138113 | -9.5009 | -40.32397 | 2025-08-27 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0b8ef2b1-e7ef-3db4-a067-1b4894f36921 | -8.08247 | -44.99904 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9418ab2-2471-3a1c-914a-ddce96d22d5d | -11.61677 | -46.40782 | 2025-08-27 04:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| afe1a911-842e-3fbe-bf0a-0696cb260fdd | -7.12626 | -43.68678 | 2025-08-27 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44a03919-42bf-38cc-b1dd-287e5bf86a1c | -7.0815 | -43.64926 | 2025-08-27 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38efcfad-7c93-33c0-95da-c7fbc4878e80 | -12.75735 | -48.19267 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4d267685-f849-3deb-ba44-8239b3f691ec | -6.71125 | -43.10593 | 2025-08-27 04:04:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ef393c5-073c-348a-ac6a-0eca4da87482 | -7.43663 | -42.04391 | 2025-08-27 04:04:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b1ae1a33-cb82-3c25-9c09-84831790e874 | -12.74285 | -48.1949 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1c96223-240b-3de3-b68d-6db1ef91b22f | -12.41987 | -46.48775 | 2025-08-27 04:04:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45776d18-1fec-3b86-83d7-c84b0d75fc29 | -6.57063 | -47.38398 | 2025-08-27 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7bd56ec7-fe60-34a9-b848-528056efb5a9 | -7.59998 | -43.95233 | 2025-08-27 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9b07285-3e14-3d31-a3b7-8b43c05bdf5e | -7.17166 | -43.85334 | 2025-08-27 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba87cc29-6b65-3d56-b746-b8e72288d294 | -8.56009 | -51.35888 | 2025-08-27 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33b282b5-b3a7-37a5-94bf-e0f560059186 | -12.76442 | -48.15424 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ed5c13fc-25c5-304d-886e-ef9f1e0fd9f3 | -12.70293 | -48.18265 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 65be6aa1-a2c3-3ea5-83e3-ff50b6ac7915 | -7.64215 | -42.68848 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9d039b59-bfea-3e44-97f9-160d0b2deb91 | -12.75 | -48.08053 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 785de6c1-c9bc-3ee5-afdd-1ea98be46667 | -6.79127 | -44.34517 | 2025-08-27 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22858280-5aa3-3fe2-92f6-2384d5c688bf | -13.45442 | -46.85641 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d256cb13-3169-3967-a741-82d90c9444a0 | -13.17559 | -45.28585 | 2025-08-27 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 46241df9-e429-3ef7-86b2-3970d5a5bb1c | -12.95611 | -44.57999 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2b4b11db-c9bb-3500-8e55-5a430f30553b | -12.90148 | -44.63645 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e61cafb-9078-3ed4-ba35-faa3ca395a62 | -13.60466 | -48.14357 | 2025-08-27 04:04:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5af0a698-c8e2-3098-b8ea-f7af7404b14b | -8.45903 | -43.6683 | 2025-08-27 04:04:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b497d1b8-5836-38a3-822d-da6bf2e2048c | -13.42832 | -46.85995 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e92330b-07cc-3596-b680-8cad78f03253 | -7.59941 | -43.95439 | 2025-08-27 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9b80534-a953-3c04-b550-9dbb128349fe | -7.04743 | -44.29823 | 2025-08-27 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 073e1951-2837-3048-b934-4e5ffecebdbf | -11.03765 | -45.14242 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f2333877-de6f-3885-b43b-05d1591887e7 | -9.09733 | -49.57394 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fb32d518-28bc-31a2-aade-bd3d50a5b088 | -13.42939 | -46.99706 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37e17168-2542-3f28-8cf8-727ade3d43d7 | -6.46019 | -44.57493 | 2025-08-27 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| eb33173c-221c-32b8-97ab-6da469757a36 | -13.06896 | -46.30515 | 2025-08-27 04:04:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d054afed-f570-338c-b592-6752bdbb0779 | -8.09173 | -45.01666 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4718deb1-e431-340d-997d-55335e81d0dd | -11.64602 | -44.86184 | 2025-08-27 04:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README27.md)
