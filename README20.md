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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcec39a5-c5c4-338e-b2c3-9e9c6f9ccdad | -3.80523 | -43.22252 | 2025-07-18 04:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d35c794-6009-3af1-84d4-999c5264cc36 | -5.66124 | -43.71934 | 2025-07-18 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 7a14c8ca-7038-382a-893b-1a2a6ebcca98 | -3.39204 | -47.48364 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 5c867884-44c4-3e81-843c-d215e671c8d6 | -3.3952 | -47.48908 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 2614b9a1-ce24-3020-b000-c721ba86eafe | -4.15106 | -48.21835 | 2025-07-18 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9526cee0-8af5-3a70-9253-e224ea4e4a83 | -3.85964 | -50.08564 | 2025-07-18 04:51:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6967552-2bb2-3224-91a4-5ba4b115245e | -5.78399 | -45.07436 | 2025-07-18 04:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d721d1c2-13e6-3b60-982b-74abaf2f7591 | -5.66216 | -43.71289 | 2025-07-18 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 53a294c8-339c-3e07-af61-b84d0d251f70 | -5.6617 | -43.71613 | 2025-07-18 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| eb0eee00-b9b1-3da6-9a54-4c9ca5a1ae14 | -3.58602 | -48.93997 | 2025-07-18 04:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5de5807-7cb9-3973-a113-2cd60ebc83fa | -5.75539 | -43.40024 | 2025-07-18 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15460393-aa2e-3f3e-9170-ef8e54be0051 | -4.80442 | -43.22388 | 2025-07-18 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47cd5ff0-b2c8-39b4-a1ba-5abaa10dd149 | -5.6565 | -43.71531 | 2025-07-18 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 17f55ae8-dbe6-3aa6-9545-427355ef1a9a | -3.73544 | -53.99218 | 2025-07-18 04:51:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4bfe25ee-5167-3758-987b-a0542faf88ae | -5.64654 | -43.7105 | 2025-07-18 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5e01cfb0-075b-3399-9abd-e6ffaf591f6a | -5.19717 | -45.4884 | 2025-07-18 04:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 13d9083a-e2e6-3348-bcde-cadffa625e98 | -5.16617 | -40.76099 | 2025-07-18 04:51:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 88edb461-38b5-3e98-adbb-a86ec421bb4c | -4.79909 | -43.22313 | 2025-07-18 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b579d59-a301-37e0-b4c7-b549cf0e5550 | -3.21482 | -48.97117 | 2025-07-18 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ad4ee0b-03b5-3849-a407-6e1c125b8859 | -2.58677 | -51.9251 | 2025-07-18 04:51:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d4c9296-5d0a-3670-a987-63cef68c3863 | -5.19785 | -45.48373 | 2025-07-18 04:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 870cb9df-967a-3dbd-9868-9e061517c717 | -6.93494 | -43.8056 | 2025-07-18 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5860237f-b55d-3143-9abc-fb7f23a89183 | -5.48772 | -43.07912 | 2025-07-18 04:51:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e19d32ef-cea0-342e-8ae6-350b021bd3f7 | -3.73339 | -53.98857 | 2025-07-18 04:51:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c77d868-e0e1-302b-b3eb-fa2206bb92c4 | -3.84767 | -47.75085 | 2025-07-18 04:51:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88bcaad7-5747-3b07-a02a-d055aaad038d | -6.14439 | -47.76527 | 2025-07-18 04:51:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fcf5f1c-5db5-3261-b2ff-dcdb74bc585c | -3.11649 | -47.01054 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 540b583a-8d99-3d28-a74e-54c6f3c870d2 | -5.65605 | -43.71847 | 2025-07-18 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 63c2ecee-d96b-310b-8e23-481042cdcbdd | -5.78873 | -45.07513 | 2025-07-18 04:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e21f6d52-fd80-3d27-9ee6-d942ce23b203 | -5.73273 | -44.50056 | 2025-07-18 04:51:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 902d9121-b436-3afc-8e43-4b8c73680b22 | -4.9627 | -43.22932 | 2025-07-18 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d86bf3d-3fc8-34ac-a84e-426bb532315a | -3.44978 | -49.56556 | 2025-07-18 04:51:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aad438ad-63b7-309e-8b60-8d846929e610 | -3.38889 | -47.47821 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 57e2b198-f154-3440-9d74-589a539bbb2b | -3.82703 | -47.74587 | 2025-07-18 04:51:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 32ba9f89-ae63-3690-a9ab-7ea018dea522 | -2.90825 | -48.2428 | 2025-07-18 04:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cae21d88-b96c-3f5c-a2e8-7b9a4194dc67 | -5.73255 | -44.50701 | 2025-07-18 04:51:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27d6de6c-00a4-3085-b24b-1a4483b93865 | -5.74238 | -46.257 | 2025-07-18 04:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ca9254c-8009-38c6-a910-fbd8f756d518 | -3.20193 | -54.59018 | 2025-07-18 04:51:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88942b6f-3856-39dc-8c2d-f9c4e2715db7 | -3.20506 | -54.5897 | 2025-07-18 04:51:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c1db3192-8c8d-3f1e-8052-0446c3fc173c | -6.16099 | -45.09386 | 2025-07-18 04:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 196393c3-f0d3-3086-878f-1497459b9c94 | -4.64937 | -43.12275 | 2025-07-18 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ec80180-3686-3bb4-a3f1-676c3ac795d0 | -2.63674 | -47.30431 | 2025-07-18 04:51:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e3cbb3e-8027-3799-97f2-b612b28ae369 | -3.19441 | -60.60637 | 2025-07-18 04:51:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf061faf-5abd-31af-ace9-b4c080aa96d4 | -3.59529 | -51.06513 | 2025-07-18 04:51:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ef73535-5bfd-37c3-9785-596ab26831c5 | -5.48723 | -43.08252 | 2025-07-18 04:51:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a31b40fe-8ea0-324c-985f-813a86807e3d | -2.65296 | -48.80385 | 2025-07-18 04:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 736ee06a-397e-31cc-8334-3c6778dc9bbf | -3.84557 | -47.75355 | 2025-07-18 04:51:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02792767-9acc-3ae1-a5ce-717b1bc8c9ca | -3.04586 | -49.43056 | 2025-07-18 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 966edf13-6281-3f03-a95e-e87333835a0d | -5.43773 | -46.28885 | 2025-07-18 04:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d3d9d01-dd00-3394-be56-ee7a0caa8c3c | -3.80476 | -43.22575 | 2025-07-18 04:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba96b7dc-b1c3-3c69-86f1-b39681ceb931 | -2.9136 | -48.24692 | 2025-07-18 04:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa05f6e7-3aaa-3a46-96c5-f8fb06835d58 | -5.78472 | -45.06928 | 2025-07-18 04:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5682850f-9c0f-35fd-a8e9-a309ceb82c78 | -2.91492 | -48.2382 | 2025-07-18 04:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c67af90-268b-304f-a423-f186fa456a58 | -5.6574 | -43.7089 | 2025-07-18 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f05ffa18-e0e3-3962-94fa-1cfa49e758d3 | -3.732 | -53.99163 | 2025-07-18 04:51:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bf958486-eb85-35f7-8ca5-6bf8fb90e51b | -3.12049 | -47.01115 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| a0076b0b-d724-3ce7-af9b-41fcf577e87f | -3.07605 | -52.42678 | 2025-07-18 04:51:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4e7c762-9a5a-3161-9356-2e4496e42b2b | -5.85593 | -44.97624 | 2025-07-18 04:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f55f2f7-cb25-30a6-bcd9-be96c854e4a9 | -3.65408 | -48.32001 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0790bdd3-531f-319b-a156-7292e0fc431f | -2.44496 | -47.32987 | 2025-07-18 04:51:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4add9d1b-ec15-3267-b7bf-005ba2bf3313 | -4.80394 | -43.22714 | 2025-07-18 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2b1de6a6-f72a-3d29-b888-bd3724033bf4 | -3.38351 | -47.48734 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 67e35c05-515a-3f99-9930-16fd6726f8fd | -3.83088 | -47.74649 | 2025-07-18 04:51:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d6ddb2a0-91bd-300a-8899-8ff0e4630aeb | -3.29855 | -49.1916 | 2025-07-18 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 367565a1-b34d-3002-b40b-13510028ffaa | -4.10726 | -48.20227 | 2025-07-18 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0dcc5f3-fb7d-3dc2-abf0-029613a91150 | -5.59058 | -51.19201 | 2025-07-18 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf62bfb4-7212-3c69-acd8-3e40cba830ff | -5.73191 | -44.50607 | 2025-07-18 04:51:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30007951-c40d-3cba-92e3-5a75dd06db21 | -6.33938 | -44.7556 | 2025-07-18 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe4c7da2-d801-3352-afb4-ea5c83e6e700 | -3.03386 | -47.86273 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94ebae5b-2bbe-387e-83b8-b882f3dc52ae | -3.11971 | -47.01633 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 72e32409-0654-3674-855d-9697806c3ab9 | -5.65219 | -43.70814 | 2025-07-18 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 11a3ba6f-1df2-312d-a48b-11c95683dec4 | -4.54229 | -45.15797 | 2025-07-18 04:51:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 219097a4-bc62-36ea-aea2-8c59a0a063d9 | -5.20244 | -45.48436 | 2025-07-18 04:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 611f25d0-5ac5-3c2b-941b-d579d199347e | -5.75587 | -43.39693 | 2025-07-18 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51f2254b-cfe8-30c4-a4e8-65bf4d7a8db6 | -5.91476 | -43.47412 | 2025-07-18 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08ab748b-433f-38ab-b10c-1cd1bfcb403a | -3.39279 | -47.47877 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| adfe6c8b-05ad-3d35-912b-8184be3b7887 | -3.38814 | -47.48308 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 3d7319f8-3a0f-3c39-be8a-718661dfbae5 | -3.40058 | -47.47995 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e133dc3b-bcca-3abb-a6f2-99b97cb03ec8 | -3.94266 | -48.09346 | 2025-07-18 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a58fd6db-eb90-3e20-8415-fb8ed8010415 | -5.85666 | -44.971 | 2025-07-18 04:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 275d7aea-1d0a-32a6-b765-7ac51998e2f6 | -5.83684 | -44.09681 | 2025-07-18 04:51:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b04d8047-463b-372c-bb59-d38b6efb4c94 | -2.63284 | -47.30371 | 2025-07-18 04:51:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74979068-9032-38f5-a81c-c7275725ce95 | -5.59003 | -51.19557 | 2025-07-18 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 946ba5bb-98aa-384d-9a54-96e074272746 | -3.65261 | -48.32196 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f822b07d-8a2e-341c-84ce-5a2e681e508e | -5.79676 | -43.63226 | 2025-07-18 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| afa24732-c980-3498-8474-10c7222af818 | -6.71597 | -44.32724 | 2025-07-18 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c5775dd-703e-3e18-8af1-f2bf581aaf51 | -2.925 | -49.06876 | 2025-07-18 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb13cc3d-995d-3c7a-a736-ce2dde6ce48d | -5.4889 | -43.07811 | 2025-07-18 04:51:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 358d9014-4c48-3612-93e6-17ef6ba5331a | -3.38499 | -47.47762 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a0e56aa9-ba1d-39b9-861b-06063ccc5a3d | -2.65654 | -48.80439 | 2025-07-18 04:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f00a16f0-7321-3249-8a13-1a044e842749 | -4.58838 | -43.31404 | 2025-07-18 04:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ef2dc3cc-83e2-3ca5-a50f-1e5026de5faf | -5.48179 | -43.08179 | 2025-07-18 04:51:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 863bb8ba-b288-3c69-b649-f8250bcfec9a | -4.87553 | -48.91007 | 2025-07-18 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af928c3a-a41f-3ace-a3d6-c80ad8ca2d2f | -4.58744 | -43.32038 | 2025-07-18 04:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 056fedd7-2c02-3ea6-b889-5f685634efe8 | -4.15037 | -48.22286 | 2025-07-18 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b81b5235-6446-3074-938a-affd5da0d927 | -3.3976 | -47.4994 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5142b5aa-d166-36d8-9126-cb20c2d1d03b | -3.51687 | -47.21402 | 2025-07-18 04:51:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b99df3a2-34c0-32a8-bb88-982185eab1a6 | -7.05913 | -42.98595 | 2025-07-18 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 43e4381d-32d1-3435-8578-bf5a56be75ed | -4.10968 | -48.21177 | 2025-07-18 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 339e4d9e-9b14-3e22-979e-970f78f5b4c5 | -4.21443 | -48.61026 | 2025-07-18 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README21.md)
