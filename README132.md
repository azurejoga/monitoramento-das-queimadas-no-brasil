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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f948578-5e59-3d4e-af0d-dba56cfe3c9b | -12.6825 | -45.2977 | 2025-09-11 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| d159b5bb-0a12-337c-be03-79d6d3f348ad | -12.8448 | -47.9682 | 2025-09-11 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| c5e865e4-08dc-3760-8c86-65b8e4639b69 | -15.118 | -52.4066 | 2025-09-11 11:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 38c34db5-180c-35ef-aaf2-5bc6bf69f73e | -8.7547 | -47.1107 | 2025-09-11 11:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| ea0489c7-69ff-3fce-9eaa-10643ddbddba | -15.1367 | -52.4466 | 2025-09-11 11:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 34dffa32-3a41-33db-a5eb-46b84672b625 | -15.1561 | -52.4439 | 2025-09-11 11:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a9fcc700-c08c-37d6-bbef-36395c404a38 | -12.6632 | -45.3008 | 2025-09-11 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 24dd733f-5d62-3cd6-be2d-a1ad617f52bb | -15.1565 | -52.4226 | 2025-09-11 11:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 0c369b56-4fe1-371e-8637-677161f41887 | -15.8703 | -54.9358 | 2025-09-11 11:50:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| cbdcd79d-b861-32b8-87a8-b16c8b8005eb | -15.1016 | -50.1468 | 2025-09-11 11:50:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| b1cf44f8-2208-3a35-9e04-bb620ef6a788 | -10.1844 | -46.1927 | 2025-09-11 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 176.8 |
| 8cd9491d-5889-3631-948d-0e76e5da2b02 | -8.8755 | -49.5613 | 2025-09-11 11:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 371571d7-c0cc-306e-bbc9-6a78fd6bf4ae | -12.6829 | -45.2746 | 2025-09-11 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| cf71095a-b158-3acd-af0e-8e81bd5fc43a | -10.184 | -46.2153 | 2025-09-11 11:50:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 190.6 |
| f0b2e664-6abd-3eb6-9254-c51816b3a353 | -3.69978 | -42.19131 | 2025-09-11 11:55:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| ba2a64fb-ca7a-363c-a18f-7246dcbf78c2 | -4.44472 | -38.05681 | 2025-09-11 11:55:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| e8593168-d4da-3a56-b8ee-2e423134c529 | -3.48946 | -41.54585 | 2025-09-11 11:55:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| b395392a-5dd8-357d-b917-8750f9358455 | -3.60265 | -42.85622 | 2025-09-11 11:55:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2e8fc7fe-d577-3cdc-a746-43ff0773128a | -3.48054 | -41.54461 | 2025-09-11 11:55:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 2278c898-005a-3320-9e89-2b0a0ce8372d | -3.57159 | -43.76332 | 2025-09-11 11:55:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 15aba888-cf16-3db4-a800-bdd4a7bc334f | -3.92315 | -41.4129 | 2025-09-11 11:55:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| debe5a77-589a-34c6-a2d5-6e81d1e14f36 | -4.44621 | -38.04597 | 2025-09-11 11:55:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 2e4dbb38-c5fa-3214-8d57-bbd60e05fec9 | -3.40665 | -43.00116 | 2025-09-11 11:55:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1c377a9a-f605-3e17-bffe-38e1381e0bd0 | -3.40912 | -42.48014 | 2025-09-11 11:55:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 89b1f37f-af61-3535-beb6-a21186d5bd43 | -3.92186 | -41.42181 | 2025-09-11 11:55:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| d7bc553a-2ab9-3998-be1d-7780c97ad4a0 | -6.6824 | -44.12326 | 2025-09-11 11:57:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| c63d76e9-bf1a-37b5-81d5-260722c99052 | -6.67269 | -44.12179 | 2025-09-11 11:57:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 53732650-ecef-3731-a262-9531e949fa0c | -8.58443 | -45.58852 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 33da4349-dac6-3be5-8de6-11108cb08360 | -8.87469 | -49.54418 | 2025-09-11 11:57:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| a770e2d0-936e-3807-8e63-a776779d1438 | -11.47801 | -43.62299 | 2025-09-11 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 22f29831-8ab5-3338-b8c0-439910e5ec5b | -7.03907 | -42.12597 | 2025-09-11 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 47215247-324b-3efc-8e93-030076bea932 | -8.16313 | -46.10297 | 2025-09-11 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 469d6295-8f20-3c2a-8fd6-b61c04d1d315 | -6.17611 | -41.07634 | 2025-09-11 11:57:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 1389a373-c325-305a-8960-2a5402516669 | -9.13013 | -46.9814 | 2025-09-11 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 41987886-f88a-3000-a004-582660cdcb37 | -9.30131 | -46.77704 | 2025-09-11 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 5390b2f2-591d-33a6-879f-ece0a527fe5a | -11.37482 | -43.50937 | 2025-09-11 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5bb3a8a5-4fc9-3479-bdaa-c2ceddc4027c | -11.77589 | -46.48675 | 2025-09-11 11:57:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 90bb127c-0e22-36ef-baa9-24cac3a98299 | -8.51645 | -45.68277 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 03a4b76b-f49c-319b-8627-3c44c8147682 | -11.50315 | -50.39684 | 2025-09-11 11:57:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 54a9211c-cce7-37ac-81e6-a0c537b483c4 | -10.57647 | -47.23339 | 2025-09-11 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d382b481-b062-37f7-977f-235a1fafff14 | -7.71425 | -44.76736 | 2025-09-11 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| f78606b9-383f-346e-aaf8-d05b181e9295 | -10.67683 | -48.63033 | 2025-09-11 11:57:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 80911769-be01-31b3-b6f6-3bac678a8ca8 | -9.90388 | -50.16908 | 2025-09-11 11:57:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 446d453a-6a28-3b12-87e8-70d3298ab5a2 | -5.474 | -43.43083 | 2025-09-11 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0ef737ee-d718-3194-bef4-b86d725966ce | -6.85639 | -47.86966 | 2025-09-11 11:57:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| c683e92b-3546-337f-9cd6-da0a0de6a920 | -11.34413 | -46.47202 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 7389f80f-df2b-342a-b3cb-a188ebb33784 | -6.06641 | -44.68423 | 2025-09-11 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| d8ab8c06-872f-39cf-b4b5-518fdfcbf13c | -11.37345 | -43.51867 | 2025-09-11 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d6455009-1a78-3f33-b769-81c22738374e | -8.04163 | -44.50251 | 2025-09-11 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.9 |
| d417e41f-b63a-3c99-85fa-540f005fa943 | -8.08695 | -48.23209 | 2025-09-11 11:57:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| bc15cb55-66ad-3e2e-a05b-45c79a390ed6 | -8.73457 | -47.09883 | 2025-09-11 11:57:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 109349b6-58b8-3062-a791-7d9d30bb049e | -7.26494 | -44.62202 | 2025-09-11 11:57:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 604899e1-4558-36dc-8b68-6ce3872cd4dd | -8.51439 | -45.69604 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.6 |
| c6beb6fc-6eaa-329f-8d4c-5b50a4e40b9b | -12.13964 | -44.86198 | 2025-09-11 11:57:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c9a26e9e-aed1-31b4-9754-53211c211007 | -11.42554 | -43.54194 | 2025-09-11 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| a8dc4b11-cb72-33cb-802c-88634e6b8e11 | -6.40563 | -42.61121 | 2025-09-11 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| c9cc25e5-8e2e-3697-9e7b-f1b24bbd9fff | -6.46816 | -44.05708 | 2025-09-11 11:57:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 2177d42c-5322-3490-80a1-a8d77122af85 | -11.77186 | -46.47935 | 2025-09-11 11:57:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 1b7b1c2f-900e-3e7c-b5df-5c3f16cca322 | -6.22612 | -43.33229 | 2025-09-11 11:57:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 3326b518-d371-3b61-b9e8-03f9177c660d | -13.02485 | -41.58812 | 2025-09-11 11:57:00 | TERRA_M-M | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| e18f568e-4f09-3f8a-89cc-38213396c6e6 | -11.56479 | -38.87598 | 2025-09-11 11:57:00 | TERRA_M-M | SERRINHA | BAHIA | Brasil | 2930501 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ab24f201-045e-3a8e-9a34-1381f010b752 | -8.87346 | -49.57695 | 2025-09-11 11:57:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| f1492aa8-2524-3308-a046-8dd5e2c26ffa | -9.06367 | -47.04259 | 2025-09-11 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| ff4e0c37-1b2c-32fc-8850-25f628ca5294 | -9.90419 | -50.17604 | 2025-09-11 11:57:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| cce416ce-d0f6-3a09-b263-920a378795dc | -8.11169 | -45.5252 | 2025-09-11 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 25.4 |
| cf02a204-4643-36ef-94c5-4a0c39b5018c | -7.42827 | -45.85002 | 2025-09-11 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 3328f77f-5596-3ab2-ac3b-237b5bee4ffc | -7.41535 | -45.86202 | 2025-09-11 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 7e29800e-1a62-3961-80ca-9872aaf0b0c3 | -6.67794 | -42.45306 | 2025-09-11 11:57:00 | TERRA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 64e39d17-aa1e-3ea2-ace7-d934aabf4edf | -9.03071 | -45.75435 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 75d8f858-4397-365b-8540-d77c30ae2e2a | -6.25743 | -43.48579 | 2025-09-11 11:57:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| bb2d25d4-ccce-3447-81ee-4a6db9147004 | -6.2465 | -43.49453 | 2025-09-11 11:57:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e62c8fdb-6588-39f8-8b44-39df47f7e8ec | -13.02616 | -41.57877 | 2025-09-11 11:57:00 | TERRA_M-M | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 38ca78be-ffd1-332f-8c7a-016f07719bdd | -11.53343 | -50.4095 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 9fe9f9e1-3825-31e6-9be4-05d992747f4d | -11.35908 | -46.51537 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 8bcef51a-068a-30b6-8ec5-bca2c2dda9ce | -6.32782 | -44.85161 | 2025-09-11 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0abd8090-3703-3141-a1a6-6ebb79927aaa | -6.67114 | -44.13225 | 2025-09-11 11:57:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 286e7139-5e2f-3776-983f-0e0cdad47edc | -6.85454 | -47.88391 | 2025-09-11 11:57:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 92b7c745-0bf4-3eba-98b2-d7fd8d98df9d | -9.72279 | -43.51656 | 2025-09-11 11:57:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 035f9fc7-df50-3aca-8187-24bd2063f8f1 | -8.08286 | -45.57349 | 2025-09-11 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| cc2426d1-18b5-318d-9c92-9358d382203a | -11.16748 | -45.31007 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a8b8d4b1-4f17-3784-9e28-a1321d980881 | -7.86998 | -45.5086 | 2025-09-11 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 01b42444-b66c-34b8-a73d-38403ab676d9 | -11.74561 | -43.37217 | 2025-09-11 11:57:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a66bf39a-0d1c-372f-9535-25586898b7a5 | -11.38129 | -45.58438 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 89acb849-2fbb-3647-97fd-122a11accb03 | -10.43415 | -50.56757 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| a2bd9425-bfb8-3805-98b7-1df457f5ec68 | -7.42621 | -45.86369 | 2025-09-11 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 3e233148-16a2-3e1b-bf56-26f62731c2e5 | -6.46977 | -44.04633 | 2025-09-11 11:57:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 8d520985-d9de-3e93-9ca6-199fdca0ac17 | -11.78029 | -46.49417 | 2025-09-11 11:57:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| f2d79171-d980-331d-85d0-af5b254fd2c9 | -7.35626 | -43.93058 | 2025-09-11 11:57:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1721819f-5ad4-3ab0-b13c-8bc553693863 | -9.08919 | -47.08833 | 2025-09-11 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 15b5241d-4ff9-3929-bff1-6f36c70cc5e2 | -9.04016 | -45.73533 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d12161d8-1068-3af0-917d-8a4197e840fa | -5.56745 | -43.55531 | 2025-09-11 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 4e07dbdf-97e0-3b72-aff6-9f72d928c1de | -8.97232 | -46.06839 | 2025-09-11 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f75fd8ea-8991-34dc-8033-fdafa47e2658 | -7.92411 | -44.86944 | 2025-09-11 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9baf211d-980b-3cfe-8e32-c3a5397b73c1 | -6.54494 | -44.7733 | 2025-09-11 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| ceaac021-cd8d-31fe-b4f9-f4643f112d74 | -7.86652 | -45.50167 | 2025-09-11 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 51b2d5ab-cc72-367f-bc00-239a36d9bb49 | -13.00704 | -40.09107 | 2025-09-11 11:57:00 | TERRA_M-M | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 4109e108-1cee-3005-85ac-56b7fec686a5 | -8.10973 | -45.53811 | 2025-09-11 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 5ee7c213-e6ef-3468-a810-67441683abd0 | -11.77386 | -46.49993 | 2025-09-11 11:57:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 706ca18c-e39c-3545-ba35-3f1f655eb1b4 | -11.03103 | -45.06167 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3ad9ea63-8faf-3334-9a8c-f80693d60eb3 | -9.09312 | -47.08213 | 2025-09-11 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |


[Clique aqui para ver as próximas entradas](README133.md)
