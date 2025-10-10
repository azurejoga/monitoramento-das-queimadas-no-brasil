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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 288efb77-e9a5-3033-b4e1-d0573d6726fa | -7.45051 | -37.33427 | 2025-10-10 04:00:00 | NOAA-20 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 81101fdb-1968-3bbb-899e-bced1b0d62a0 | -7.68695 | -42.38859 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9b197330-53d9-302f-bf7d-d54fda3e7e3f | -7.26229 | -44.10365 | 2025-10-10 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41d8594f-ee5d-393f-a40d-bb91abd0bc72 | -7.11398 | -44.08945 | 2025-10-10 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d7ab963-e75e-376f-96b3-9e650ba3a2e6 | -7.76387 | -42.40837 | 2025-10-10 04:00:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4d74e067-03db-3ebb-806e-a9770f8046f4 | -4.56587 | -44.04078 | 2025-10-10 04:00:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31c401e5-98c0-34c0-ad5a-858f29603079 | -7.79738 | -42.60508 | 2025-10-10 04:00:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 60021005-eaec-3fc6-bd9a-579d9b79f98e | -8.20106 | -43.34875 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2767bf4e-a0ee-3d77-8776-8cea9aa66a0d | -4.24345 | -48.20484 | 2025-10-10 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6606bc6e-0597-3734-b735-e4b9673b5cfa | -7.70618 | -42.37989 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 706cd482-e488-3ca4-949e-b6233ffb4131 | -7.85962 | -44.13022 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a346affd-9b3e-3ecc-ba3c-d5cd4dd96543 | -5.98395 | -45.91782 | 2025-10-10 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0f36d76-472f-395d-9b67-1b38224ca774 | -4.5667 | -44.03574 | 2025-10-10 04:00:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c55e8b7-a132-3b99-a17c-175dba6d9961 | -7.49849 | -43.11539 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 465ef30c-5454-38a4-9268-26d2116f5a58 | -8.19589 | -43.33503 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 3f827285-5a7f-3bdc-8925-74dbad0e0710 | -8.50332 | -46.17554 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abf17098-f508-3d05-b36d-41ab1f294a35 | -5.84086 | -42.44456 | 2025-10-10 04:00:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4ff6c5cc-7b8f-3ff4-b3d2-2c534b0d1e96 | -6.58795 | -44.62824 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 83cf3f5c-3503-35c3-ad71-294ef420ff8a | -8.83068 | -44.42606 | 2025-10-10 04:00:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9e07117-29e3-3ecb-841a-e987033fd47f | -9.0936 | -45.03254 | 2025-10-10 04:00:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8df9bbbc-8f4e-30a5-ab2b-7293109c9757 | -8.51253 | -46.1731 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbed29a1-cf05-3897-bd8c-764be4348287 | -8.19366 | -43.32608 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 9de0a65b-5f05-39a0-a8d7-912789442cb8 | -4.8952 | -41.54177 | 2025-10-10 04:00:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3bc304ef-bd02-36f8-9095-a4e258f5644c | -7.33023 | -47.81813 | 2025-10-10 04:00:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9247fea7-aa69-3f89-928b-3f46b3d78f64 | -4.65656 | -43.20497 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 81f5f1f1-d92e-32c9-b534-dba5c8a3bd74 | -8.20174 | -43.34459 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a156761b-5f23-300a-b7fc-c7ace3d49a1d | -7.28855 | -41.96714 | 2025-10-10 04:00:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a7192067-ecad-3177-983b-1b0cf497dfd6 | -6.64191 | -43.6832 | 2025-10-10 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1204736a-db87-3b77-af12-40db47ef66bf | -6.58227 | -44.62869 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0838224d-8a2c-30a9-a576-835a017e6e21 | -5.54137 | -45.37912 | 2025-10-10 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5078c2d1-f030-3352-b4dc-4a7a53eabc73 | -5.75115 | -42.52491 | 2025-10-10 04:00:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2b7a7d2e-477f-3440-8729-15da1bca7949 | -8.20759 | -43.35414 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| e294cbec-8c84-37ff-98ec-fbdc76f891d2 | -8.44514 | -36.33781 | 2025-10-10 04:00:00 | NOAA-20 | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c4954606-c709-3fa7-a38f-85f6034da703 | -6.17374 | -42.55602 | 2025-10-10 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ede07d8d-0d0d-3b41-a490-80a5eefd4334 | -6.59448 | -44.79824 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b8031c7-adfa-322d-8b11-5de3a2dc0696 | -8.20753 | -43.36121 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b5378097-efc7-3611-90b0-201a4f16bf69 | -7.50446 | -45.14543 | 2025-10-10 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db4c02ca-43a1-3fc6-92a6-75e703a1cfae | -7.61126 | -43.069 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 495299ae-bdc0-3475-8c02-6882bd4feab9 | -7.76671 | -42.41277 | 2025-10-10 04:00:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 60030901-4e88-3c07-86b2-d18549573fc3 | -7.66654 | -42.58082 | 2025-10-10 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4c64f60d-4211-3f04-a6d9-4d344780f76b | -7.1453 | -42.20057 | 2025-10-10 04:00:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9864899b-8c5b-3b1e-81d2-df0a4a8a4c1f | -7.79903 | -44.12069 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a4eaa54-b6a0-3f1e-9bb9-a9bcd3415e18 | -6.584 | -44.61859 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| bf8087fe-70fd-3594-a8f7-ffabb3be6eaf | -5.74565 | -42.76 | 2025-10-10 04:00:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6e5d83b5-5e9b-3a2b-b128-e2fc7dd5446f | -7.79805 | -44.19617 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95a3ca07-8123-379b-b60b-8c242331d6f7 | -6.58315 | -44.63264 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e52cfd33-60f1-36db-8cc6-d91671652430 | -7.67131 | -42.57357 | 2025-10-10 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0de163c0-052d-3e55-b3a0-e2d16bbc62a0 | -6.59177 | -46.68921 | 2025-10-10 04:00:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb5148e6-ff55-3ea2-918e-51b9ad8c9f48 | -6.07677 | -42.5957 | 2025-10-10 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b285b9d0-9bcb-382a-95b8-e4b724a9fed1 | -8.83691 | -46.05758 | 2025-10-10 04:00:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 232fece5-8f0c-37e6-b589-0bfe330d4a08 | -7.50844 | -45.14654 | 2025-10-10 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0076099c-0d29-3803-93e7-6fd0be384fb7 | -7.26315 | -44.91599 | 2025-10-10 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b3ffc01-2a8d-3587-a2e8-56839049610b | -8.20834 | -43.37844 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f1ccf59a-835c-3737-9ebc-62d675500d7a | -7.79984 | -42.40632 | 2025-10-10 04:00:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cba2809b-783b-3dde-af0e-7db2df8d539c | -6.56826 | -44.78258 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b7454ea-db2d-36dc-beba-9eb8417e1d2d | -7.24435 | -49.51736 | 2025-10-10 04:00:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61d1fce0-b6d9-33ba-abfd-330fa8e65344 | -4.23362 | -45.99383 | 2025-10-10 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83fe7de2-d0a3-31ca-9dea-32e0d1ad7328 | -4.89581 | -41.53799 | 2025-10-10 04:00:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fdedae9b-bdca-3b8c-b21c-0be71adba4a4 | -7.21227 | -34.90332 | 2025-10-10 04:00:00 | NOAA-20 | JOÃO PESSOA | PARAÍBA | Brasil | 2507507 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7c4ab2de-feb0-3db2-ae2e-70a8ec614a22 | -4.84093 | -45.41515 | 2025-10-10 04:00:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c99907ed-6816-370e-9a90-f9bcaf503f55 | -6.74559 | -42.85342 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ca07b736-f700-36d3-98f0-d7238e5f6142 | -6.66307 | -47.75106 | 2025-10-10 04:00:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3027b5b6-32fd-3532-8090-f9834511e53f | -6.73551 | -42.84757 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9d1b9d35-a77a-351a-b7e5-373ee20d3774 | -8.17633 | -43.31888 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 50b45d2e-014d-324c-9d76-dec9dbcd71b5 | -8.52253 | -46.16608 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be2db0a0-456a-3005-b4d6-fe00190cdd78 | -6.82293 | -42.79767 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 7c5a44b4-ebeb-3a5d-9fcf-9a9ea9b9044e | -7.79797 | -42.41788 | 2025-10-10 04:00:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d558bf0c-f9bc-347d-8c77-2dd874f5cb68 | -6.03996 | -43.40556 | 2025-10-10 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2fa4182f-c926-385f-8eb4-e683f96aa6dc | -7.79689 | -46.01908 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f2a34177-1ef0-3569-9c22-ebf89870b690 | -4.74189 | -46.50053 | 2025-10-10 04:00:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81c2cdd6-795b-34bc-83ae-04edf9a700f1 | -8.19297 | -43.33026 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| b5d661da-6152-3e24-9bd0-4e0d3e53234f | -5.33767 | -45.5658 | 2025-10-10 04:00:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7815ddb8-d5b1-3bf1-aa95-cacf24fe14e6 | -10.0971 | -40.77226 | 2025-10-10 04:00:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 18a69a79-0dbd-3923-9a36-b7f68e9ee1ae | -9.09753 | -45.03318 | 2025-10-10 04:00:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 85cf0841-404e-3ef2-aa55-6a59af21c96a | -7.78364 | -44.05091 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 658f4a2c-3cf5-3f1e-94d6-a710af2f17f0 | -9.43538 | -45.45779 | 2025-10-10 04:00:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fee35fec-d724-3fce-94c9-7ebc7b59f539 | -7.66717 | -42.57691 | 2025-10-10 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b147e054-a5a7-3699-ad88-078120572008 | -7.1134 | -44.08719 | 2025-10-10 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56426a85-3130-37c6-8469-49ba818fbffe | -6.8236 | -42.79359 | 2025-10-10 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 81880c84-9122-36ea-a149-3c8690d0899b | -6.99582 | -46.99427 | 2025-10-10 04:00:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca3fc4a9-333f-3d8b-a2c3-bfe816d009ea | -8.84008 | -46.06325 | 2025-10-10 04:00:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8459e838-821d-3b50-a221-3dd1dee89949 | -5.65467 | -45.9685 | 2025-10-10 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8865aa27-25a4-348b-a484-0a2ffc13e717 | -5.40734 | -40.99176 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 710f6c81-287b-3b87-84ad-25e9741ca22c | -7.53131 | -44.30288 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2facd2c8-3bbf-31ec-9277-787f037b0847 | -7.6233 | -46.65899 | 2025-10-10 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d584d2fe-d1d2-38f8-ad08-b4a1ca3e0162 | -6.4615 | -44.58918 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 688e3223-7422-3152-a058-80055c5de939 | -7.42595 | -42.98578 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3f6fe320-88b5-31b2-912c-b9ec20f94efc | -7.95411 | -40.87471 | 2025-10-10 04:00:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b46f46af-75b3-3b71-9e98-c58ef75b083f | -5.3394 | -45.56853 | 2025-10-10 04:00:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 35660a4b-fb18-3baf-b617-e0dbe013d0d6 | -4.23437 | -45.9893 | 2025-10-10 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17939d7b-10f1-303b-8785-277fa21b6b04 | -7.77247 | -44.04627 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90ee97c8-8e21-3307-b2a9-96b1d4d4515e | -7.14654 | -42.19291 | 2025-10-10 04:00:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| af6ce602-26b6-3944-b12e-d8e0118ee06d | -5.30755 | -45.40236 | 2025-10-10 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e0aa693-6cf9-3219-973c-95d47faf1117 | -6.58711 | -44.63334 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52394df8-d263-35eb-8b5b-072927f8562f | -5.28219 | -44.88146 | 2025-10-10 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 87b099a1-6f6e-3a42-97ca-715d83cc690e | -7.26031 | -44.90834 | 2025-10-10 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f8b74c8-daaf-3fad-bf62-0a9fe7bb23d8 | -7.54885 | -44.60183 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 230ae182-eeda-3015-b3c7-42fe9d04a7b1 | -7.7904 | -44.05676 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e2448a0-9ea3-3bbf-968a-a7221d5763d9 | -8.82726 | -40.55331 | 2025-10-10 04:00:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 57653b56-4e14-32ae-b952-0161ded4b349 | -8.07083 | -42.94457 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README25.md)
