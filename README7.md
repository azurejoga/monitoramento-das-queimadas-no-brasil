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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb66e81d-0178-3440-8e15-993b71a2d22d | -4.38392 | -43.14586 | 2025-12-02 03:46:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e2f616a-02a8-3a69-ba96-7475df2beb07 | -3.42827 | -39.04646 | 2025-12-02 03:46:00 | NPP-375D | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fd415f3d-7f14-36c4-af18-5dfa72cc9ff3 | -4.68391 | -40.06565 | 2025-12-02 03:46:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 660ef3c2-cf43-320d-a706-6ce21ccf9baa | -7.95463 | -35.26151 | 2025-12-02 03:46:00 | NPP-375D | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6dfbbfc9-b13d-3114-bac1-cbc2a5b49234 | -8.04476 | -43.10704 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 3f793232-b47b-3999-ad2d-7577aa9c4d2b | -9.29858 | -40.36624 | 2025-12-02 03:46:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f269c38d-cd3f-37cb-ab79-f7a5ba2cdaaf | -8.04418 | -43.11026 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| bd61da89-d6c8-389c-97a7-c687999b999a | -9.67806 | -37.31138 | 2025-12-02 03:46:00 | NPP-375D | PALESTINA | ALAGOAS | Brasil | 2706208 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a2d38c62-80fa-364c-9480-c5c7a0def795 | -5.11732 | -43.28817 | 2025-12-02 03:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2349c282-0aaf-34ef-a5ff-a5f50cdddbb0 | -4.38443 | -43.1429 | 2025-12-02 03:46:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba93c622-9161-386d-a433-ff810673c9b3 | -1.48704 | -45.79282 | 2025-12-02 03:46:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 3e892ada-edb9-34a6-9f9f-5bcc17e75c3f | -7.34374 | -34.89034 | 2025-12-02 03:46:00 | NPP-375D | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0fcbbe84-e07b-3709-bd43-8296458cab0e | -8.17122 | -43.22223 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.0 |
| 6d84c849-f00c-3358-a024-b1021509800a | -3.32575 | -42.50286 | 2025-12-02 03:46:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9cc207fb-9586-3fac-8818-e61b4b916634 | -1.68763 | -45.80108 | 2025-12-02 03:46:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e6d9a36-3cfe-30a7-897c-cdd0859ea300 | -8.93806 | -37.36629 | 2025-12-02 03:46:00 | NPP-375D | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c5a752f3-febc-36e0-af4b-ff6f0a475587 | -4.01546 | -42.44814 | 2025-12-02 03:46:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9932137d-b2a8-33b0-84b4-a4f3d955858d | -8.0468 | -43.09509 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4330c0a8-5efd-3b0e-8f45-93b151a82306 | -6.68432 | -39.50759 | 2025-12-02 03:46:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d34fd465-047d-3cdc-81f1-9409227f5f36 | -8.04384 | -43.11217 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| d751ced6-8837-39a4-addd-9faa33efdf5c | -6.6862 | -43.5512 | 2025-12-02 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd898552-77ae-3103-8608-c18f1be0b540 | -7.91183 | -43.78614 | 2025-12-02 03:46:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 559147b9-0d1c-3c76-85bd-63f7a6f5c2f5 | -3.24404 | -45.57362 | 2025-12-02 03:46:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| eb76eb38-8f43-3119-80b3-94f82655093a | -5.13047 | -36.42494 | 2025-12-02 03:46:00 | NPP-375D | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fd98b989-86d5-397b-8e04-a911d45cd8e2 | -8.05157 | -43.09586 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2577c9fb-5372-39d6-b469-c0ed02485e56 | -8.67496 | -44.2247 | 2025-12-02 03:46:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 261eda68-1f2e-32c7-a9f0-303cd2a9a941 | -1.48155 | -45.78656 | 2025-12-02 03:46:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 5a902085-126c-3a6c-9c30-84302c182138 | -6.28624 | -39.68746 | 2025-12-02 03:46:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ed4ba5bc-9813-3b7f-84e3-c8254fe4022e | -7.52252 | -35.16803 | 2025-12-02 03:46:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fe988754-d831-3519-a13d-ce4c3b9607b4 | -5.59467 | -45.17756 | 2025-12-02 03:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05a12035-5667-3426-a865-7d6077850d72 | -4.37475 | -43.15079 | 2025-12-02 03:46:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71160f12-194e-3ce3-be8e-7a1e7289e84d | -5.58966 | -45.1726 | 2025-12-02 03:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 133fb7f5-1e99-3861-b080-9ecba01fdd25 | -4.01456 | -42.45352 | 2025-12-02 03:46:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f4c876ed-20e0-38a4-a19a-c2539d7a214d | -8.04567 | -43.10198 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.7 |
| aa983eec-bd8b-329f-b1ad-3284a95ac516 | -4.37935 | -43.14205 | 2025-12-02 03:46:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dd0a812-60cd-3b34-89e1-b4395b97b837 | -8.05611 | -43.09855 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 306bcc3e-848d-3c28-b5eb-16228938c232 | -6.28233 | -39.68682 | 2025-12-02 03:46:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0b723716-b146-3677-a004-fa972b91b5e6 | -8.05044 | -43.10279 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.7 |
| c9732ff9-394d-3056-810a-55c89e8cd306 | -8.66989 | -44.22366 | 2025-12-02 03:46:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b30f9c7-6f02-31d6-b493-08ca86469844 | -4.38289 | -43.15179 | 2025-12-02 03:46:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6880a672-8a2a-3018-b904-d0a4599eb2d3 | -1.48073 | -45.79168 | 2025-12-02 03:46:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 7b2f4e59-8bbb-32b1-b541-f06291cdae27 | -8.04119 | -43.09918 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 66876111-755a-356f-a057-e43db52af2c6 | -6.62436 | -43.86848 | 2025-12-02 03:46:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fc7fb0f-85cc-364f-8df5-e2cb1323f94d | -8.17215 | -43.21698 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 3e4ac2b7-bbc5-39ae-85a3-bc7a62e625a1 | -3.25773 | -45.56661 | 2025-12-02 03:46:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d296697a-ea6b-38f7-bc1a-0f5173a7d409 | -7.91123 | -43.78748 | 2025-12-02 03:46:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7a5e9bd1-f782-3090-92a3-fedc23ecad55 | -8.17308 | -43.21175 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 069e5b41-b65f-31f6-a16d-3f4d1891ff85 | -8.16048 | -43.17187 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 781bd382-fb62-3850-a66d-937ae9e410a8 | -1.4763 | -45.79156 | 2025-12-02 03:46:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37e7f103-04aa-36c7-b49a-340447d6e3b6 | -8.04031 | -43.10425 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5ebab28a-aea9-345a-9f4e-c4fd7d4a7240 | -7.72512 | -35.15423 | 2025-12-02 03:46:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 985515a4-73a8-3bdd-9768-5cc8419621e4 | -3.24482 | -45.56907 | 2025-12-02 03:46:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| bd8da72d-3492-3bec-955a-11bb3bc0de02 | -6.99343 | -38.14799 | 2025-12-02 03:46:00 | NPP-375D | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2aba67ff-0df2-35c0-bfe0-69bbae8f9da3 | -7.43701 | -42.5453 | 2025-12-02 03:46:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 751e4349-f94e-3acf-bd51-657c4af9cbaf | -8.03973 | -43.13609 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3059f80b-d335-3016-832e-5c6c11295605 | -5.11681 | -43.2911 | 2025-12-02 03:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7315910c-9623-3834-b311-b6c0357ce905 | -8.04983 | -43.10598 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.2 |
| 09422a5a-941d-34d9-b2a2-0e58521e8695 | -8.38782 | -36.05476 | 2025-12-02 03:46:00 | NPP-375D | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1ed253aa-528e-312f-b010-c643336a2ba8 | -3.23952 | -45.56358 | 2025-12-02 03:46:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 87e4fc0f-ab7e-37c6-88d8-045a7c816b6f | -4.68359 | -39.69147 | 2025-12-02 03:46:00 | NPP-375D | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 12dc97d2-e387-34b0-ada0-ee56c3d23d16 | -9.71693 | -36.25482 | 2025-12-02 03:46:00 | NPP-375D | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ef5432e2-6b16-3dc3-95cf-e479b42d00e7 | -8.05428 | -43.10874 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 3cb7b3b2-6349-32bb-9097-4c2b1cf5660b | -4.37524 | -43.14784 | 2025-12-02 03:46:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81e83bc3-85eb-39d5-8fa8-80392dbe9028 | -4.19496 | -38.36082 | 2025-12-02 03:46:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0438e277-ccc9-311b-b459-2c6c2f7e1364 | -4.37573 | -43.14488 | 2025-12-02 03:46:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db370412-d163-3843-a82c-1b0da5473f99 | -1.68614 | -45.79475 | 2025-12-02 03:46:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f8e30b7-3ff8-33cd-8779-f1f1fa843529 | -8.04594 | -43.10009 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.2 |
| 7c6424ab-978d-39da-89ed-56aa06c95d1b | -4.38494 | -43.13995 | 2025-12-02 03:46:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e8f7d5c9-ecc8-3caf-bce8-2bb4cd2174e3 | -8.0552 | -43.10361 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 69c7a700-696c-3bf1-a474-0153565668b4 | -6.31105 | -43.81305 | 2025-12-02 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12df83e3-c099-3413-804e-aa31d74ea15a | -4.3773 | -43.15385 | 2025-12-02 03:46:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5565d8ab-2745-330a-af70-1baa491a0841 | -5.08724 | -40.23858 | 2025-12-02 03:46:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6b2576ae-ac4b-3b93-81b8-27a38c205c12 | -4.19356 | -38.36258 | 2025-12-02 03:46:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 58d23334-48f7-303d-9261-6f08ab7251f6 | -1.48261 | -45.79269 | 2025-12-02 03:46:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 509a9fbc-01b4-3b74-8120-82ab2a8f088f | -8.0507 | -43.1009 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.2 |
| f1e34823-5be8-3f30-aa7f-0c2e40caf434 | -3.23874 | -45.5681 | 2025-12-02 03:46:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 3e416138-b293-3594-a229-11afc8d882e2 | -4.38238 | -43.15477 | 2025-12-02 03:46:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbc5a3a6-635a-3fa1-a248-072ce247c75c | -4.0274 | -40.21562 | 2025-12-02 03:46:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b996680b-2029-3d06-877e-ab6d3e3c9728 | -8.04952 | -43.10789 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 03f7b1a3-825f-3515-ae62-6c9acb946c8e | -8.16737 | -43.21609 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 1e583d66-2170-34a9-b6a5-c64341d28145 | -8.05134 | -43.09776 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.7 |
| 0a5145b6-f754-3a72-aa41-b85c6e5e7737 | -3.2585 | -45.56208 | 2025-12-02 03:46:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2716ad00-87fa-3e0a-a4a1-8c3a2aee36af | -9.80406 | -37.65047 | 2025-12-02 03:46:00 | NPP-375D | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 330cb3c5-4214-3b2c-b406-ec3b4b0e75f7 | -7.80172 | -37.6458 | 2025-12-02 03:46:00 | NPP-375D | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b8990ba1-f708-3661-9423-87bd0e51e0cb | -8.16166 | -43.22044 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 4d6e2be5-824d-3d31-a1b8-2bae4d1b4b9d | -9.72026 | -36.25536 | 2025-12-02 03:46:00 | NPP-375D | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 98bdbc08-63ef-379d-b316-30efd2298263 | -5.15533 | -37.68976 | 2025-12-02 03:46:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9c875bd1-fd9d-3809-8652-80cd3f5162df | -8.38459 | -37.43961 | 2025-12-02 03:46:00 | NPP-375D | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fc9539bc-dccc-3ea5-97ea-6f689d509f69 | -6.31621 | -43.81392 | 2025-12-02 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9648ee12-788c-326a-850a-c6740bd79abf | -8.04657 | -43.097 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.7 |
| cde972ce-e52d-32cf-8ed4-5012b79239fe | -7.43619 | -42.54998 | 2025-12-02 03:46:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eb80c79d-5272-39bf-ae5c-f239c7657dae | -1.68533 | -45.79978 | 2025-12-02 03:46:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1389d6b7-9001-33ba-8d24-8182b7f5acfa | -6.6192 | -43.86768 | 2025-12-02 03:46:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38d03660-fa47-387e-98bf-8fa39910043b | -4.37832 | -43.14795 | 2025-12-02 03:46:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e586bc94-be49-35af-afd5-99e3be10996f | -9.71361 | -36.25428 | 2025-12-02 03:46:00 | NPP-375D | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b459f3e7-5273-3b0d-af33-821de6ce8b95 | -7.34707 | -34.89087 | 2025-12-02 03:46:00 | NPP-375D | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0d49b299-bb7d-34e2-8406-8985a3a0501d | -5.59535 | -45.17367 | 2025-12-02 03:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5210493-d8e2-3472-be3b-518fee814db0 | -4.38122 | -40.7099 | 2025-12-02 03:46:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bd1a68a1-d231-3103-a90d-bde7516bd998 | -1.48177 | -45.79775 | 2025-12-02 03:46:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 4db63f87-9d75-34c2-8676-ac355aa50cfb | -11.1702 | -43.57526 | 2025-12-02 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README8.md)
