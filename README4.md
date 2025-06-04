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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38813e43-aefa-3e92-add2-2706a0cf7c2a | -10.68013 | -44.38522 | 2025-06-04 03:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb6d2371-2325-3e44-a2c8-344e57713956 | -10.25793 | -48.45951 | 2025-06-04 03:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 856a54e5-5de9-3da2-adfd-e37b8f7c47f6 | -7.88646 | -46.19644 | 2025-06-04 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6c7ee25c-9a6e-3a38-a087-60744f593d12 | -7.88859 | -46.18546 | 2025-06-04 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 284ba4dc-1195-3161-849d-cf226977f329 | -7.22972 | -43.12257 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6c5ba31e-bc94-3d5f-bd5c-ac7641bfefa8 | -9.49842 | -40.31237 | 2025-06-04 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cdc6ca20-2aa2-3062-81f6-06b0782220dd | -7.01188 | -44.59523 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 648ffcdd-7f56-31fb-9bb2-d1b1bc3d0b9b | -8.95379 | -47.28208 | 2025-06-04 03:38:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39832655-3711-3a2c-bd8c-e27b777ac6c4 | -10.20538 | -40.54786 | 2025-06-04 03:38:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c5c19ffd-f646-3984-befb-08e6bbb15ed9 | -6.96158 | -42.91199 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c86cd4fe-d622-3a27-bcbc-3ddd41d88b27 | -7.55378 | -45.8356 | 2025-06-04 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce6c88cc-eaf8-3167-a320-6225815ef2e5 | -7.21109 | -43.13342 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0b57ddb4-d312-3a0a-addd-490b958d17de | -6.96807 | -42.90638 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.5 |
| d94ddac4-61c4-3524-876e-b80be5d72817 | -7.01334 | -44.58707 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f932c142-68ee-34b3-b52e-0a84ac68393e | -8.07433 | -43.11549 | 2025-06-04 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 4f11d9ab-753a-3fac-9bc1-88ab21ba9fb8 | -7.00793 | -44.61721 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26969620-126b-332f-9d7c-3d052d3fcc84 | -8.07962 | -43.1165 | 2025-06-04 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| edd6c517-c3f5-33dd-a0d4-de0295556ffe | -7.15335 | -44.0423 | 2025-06-04 03:38:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30c53997-eea6-32c1-a78b-13759470b298 | -7.6872 | -44.56836 | 2025-06-04 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da43ef4d-2208-3cbc-8899-ad39af44cb03 | -7.01111 | -44.59949 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3909733b-6c1c-3525-89a0-39f5693a0174 | -8.36245 | -45.06514 | 2025-06-04 03:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f041e61a-e779-36a8-8d1b-e348ef918f30 | -6.96217 | -42.90869 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 8e37447d-e9f0-3166-8ac1-bf30700f2d4e | -6.96866 | -42.90308 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 07f9027f-a023-3a11-9446-d5bd67594dce | -7.58232 | -45.8656 | 2025-06-04 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c4e7995-c136-36d9-9f63-5492f642c74c | -8.36844 | -45.06624 | 2025-06-04 03:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aac2f81d-0b4d-3baa-83a9-6e6eb5a57eeb | -10.67948 | -44.3887 | 2025-06-04 03:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 686010ab-fc19-3fa8-b19a-97ea5d54d88c | -6.37116 | -43.68636 | 2025-06-04 03:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98c282da-eedb-3bd5-9594-34d89ec1982a | -7.32603 | -45.55932 | 2025-06-04 03:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb438079-50a2-338d-bbee-4a9b3d57dba8 | -7.01439 | -44.59811 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2585ff63-1431-3d3d-b1f3-4426abcd4090 | -7.88762 | -46.19302 | 2025-06-04 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60399b30-1804-337d-8f3b-6a5287e1585e | -7.21648 | -43.13435 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 944bafcc-620f-31d9-b20b-781103341eca | -4.81726 | -44.3546 | 2025-06-04 03:38:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 555143a9-a42b-3655-bd8f-216a007ad0bd | -6.35177 | -43.38787 | 2025-06-04 03:38:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a69b9f11-de37-3de7-b2fa-a5442925487a | -9.13929 | -41.00577 | 2025-06-04 03:38:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bd49a54e-3874-3698-83f5-7450fdc55e2d | -8.06904 | -43.11449 | 2025-06-04 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| c873161f-8740-369b-a5dc-91e8ea6b2092 | -7.01034 | -44.60381 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 51eb8b76-e47e-380f-9a7d-1b68cb3431aa | -6.20874 | -43.33227 | 2025-06-04 03:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83d3d67a-641a-330a-b182-7b93943b0bae | -6.96924 | -42.8998 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 27e1eeb3-5a59-3520-b113-cc43464cec42 | -7.14763 | -44.04126 | 2025-06-04 03:38:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe95646e-1fae-3204-945e-27e90125204a | -7.0194 | -44.58745 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6d5efc99-efa0-3876-ac58-aa3f7a6d8d07 | -7.0136 | -44.60236 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ca910d60-5fcd-3fae-bef0-4caaea55f263 | -6.2143 | -43.33321 | 2025-06-04 03:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5eb70f6-9d5a-3a65-8b6e-8a43e6f516f4 | -7.88863 | -46.18757 | 2025-06-04 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9542685c-8a86-38e5-a240-bdd0d9b60af1 | -7.01261 | -44.59114 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 346b8e77-019b-3d7f-8610-9b43252253d7 | -7.00873 | -44.61276 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86c6b5c6-94f1-3d28-bf28-63958d67ad13 | -7.15267 | -44.04601 | 2025-06-04 03:38:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2ec233f-f518-37a4-a1b4-44b8d70205e0 | -8.07373 | -43.11876 | 2025-06-04 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 1143dd74-9a5b-3a39-9bdb-6c7bcd938e03 | -7.21587 | -43.13778 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c324d39c-a45d-393f-88e0-2653a93a8103 | -10.70616 | -48.78363 | 2025-06-04 03:38:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de9eb379-7e62-3132-a8ae-4551cc5e787b | -4.82333 | -44.35561 | 2025-06-04 03:38:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78818d25-e382-3329-bd3d-44f8661bb3d5 | -7.01114 | -44.61549 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3ba630f8-97e8-3154-84d1-622080891be0 | -6.68764 | -43.68324 | 2025-06-04 03:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f13af611-6f29-322f-bbfb-11b79e2f2e82 | -7.01197 | -44.61107 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| af5fc8f6-051a-32de-a0bc-e5c263115e96 | -6.20806 | -43.33607 | 2025-06-04 03:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e07bbfcf-7ec1-3851-9d26-4cf54217218a | -4.80657 | -45.26371 | 2025-06-04 03:38:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bf1e5800-622d-3032-9a92-fe07eb9afc20 | -8.68904 | -36.24846 | 2025-06-04 03:38:00 | NPP-375D | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1b789e33-9d3d-395f-a2a1-2a043f0673b1 | -7.21047 | -43.13686 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e327607a-d711-3116-be83-aaa2d5cb06a5 | -7.1419 | -44.04028 | 2025-06-04 03:38:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66b3e290-acea-3cd1-8368-0459df5f6a40 | -7.01475 | -44.61342 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c5840a3a-6274-3270-a13b-219b8aa91074 | -6.35111 | -43.39162 | 2025-06-04 03:38:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f0c5c3e6-1d06-37df-95f4-9c8ade50ac5b | -8.68709 | -36.24874 | 2025-06-04 03:38:00 | NPP-375D | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4b9c8594-8bf0-3c15-a0ad-94832e14b30f | -7.21772 | -43.12751 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e772ffcf-088f-3925-8a5e-eccd00782275 | -6.9602 | -42.9052 | 2025-06-04 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.1 |
| 2f641be1-e80a-3d64-81c8-95d7dfb2227e | -11.53705 | -47.31427 | 2025-06-04 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b47c45d0-5ec0-3d29-b599-aba4c774c973 | -14.71247 | -45.09715 | 2025-06-04 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61c0d1ef-d38e-30c2-8dff-0a4ac31d3f1e | -14.70787 | -45.09229 | 2025-06-04 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 794849c0-334d-3f4b-b068-78cc98e1ca0c | -12.31836 | -47.26216 | 2025-06-04 03:40:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2fbc50e3-201c-35c9-852f-922b60de3c98 | -12.31645 | -47.26561 | 2025-06-04 03:40:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2127cba-5a44-375f-bf11-0fbb22be2294 | -14.72309 | -45.0998 | 2025-06-04 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 448c10c6-5800-316d-a8fc-c004ea4b3324 | -16.02642 | -43.68322 | 2025-06-04 03:40:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57b0da2c-84eb-3fa1-814f-fe1a151bc7df | -14.71176 | -45.10066 | 2025-06-04 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 905c6652-4fdc-3b0e-9f10-b473aceea417 | -12.31948 | -47.25677 | 2025-06-04 03:40:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f017f1f5-b503-31a9-b602-866250b3ceee | -11.90309 | -47.45278 | 2025-06-04 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 528a7b72-ea62-315f-9d71-6207bffe8bd5 | -14.81478 | -48.46185 | 2025-06-04 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c514a30e-c321-3916-b9df-dfaa255f7c0f | -14.71638 | -45.10546 | 2025-06-04 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a377d4a5-a5fb-35ba-a66a-fcc6e45a6deb | -11.53504 | -47.31691 | 2025-06-04 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 492fd55d-7173-385f-a0f6-97aadff496a6 | -11.53395 | -47.32214 | 2025-06-04 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a63e15e6-ae22-3380-8e7f-9f6749c2ea97 | -11.53615 | -47.31153 | 2025-06-04 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d01e083b-07b5-398b-b732-d1040b146ef3 | -11.57353 | -47.45999 | 2025-06-04 03:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 506c2661-8c43-37cb-beba-cf0a14c0af40 | -11.89546 | -47.45697 | 2025-06-04 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30f535e2-af5f-309b-9ff9-193cbc1d246d | -14.7139 | -45.09004 | 2025-06-04 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c04d4382-46c3-3831-bc66-99a22c3970c3 | -14.72238 | -45.10337 | 2025-06-04 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b9d27a8-419d-34ad-a575-520acae57ad0 | -11.57453 | -47.45506 | 2025-06-04 03:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b3f8643-1b67-3be4-9199-296777d28603 | -14.71318 | -45.09361 | 2025-06-04 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db610405-5677-3a5c-8382-0618649e672d | -17.096 | -43.80536 | 2025-06-04 03:40:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dba785b1-df21-3185-8d0c-fc8805d260fd | -14.71778 | -45.09848 | 2025-06-04 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a34ec79-1d3e-36f5-8b1b-c6c8b50349a7 | -11.90425 | -47.44708 | 2025-06-04 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f4782fc-49f5-30e6-82d2-f6fc90cfbbb4 | -14.71849 | -45.09494 | 2025-06-04 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71709e26-10d3-37be-81c7-0b897562780c | -17.78186 | -42.8119 | 2025-06-04 03:40:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fa7a4b9-b69d-3af4-9c5b-dea16d86ea67 | -14.71707 | -45.10201 | 2025-06-04 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7fb4628-9dc8-3362-b303-51ea0d4e7520 | -19.49934 | -45.08486 | 2025-06-04 03:40:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f88b090-8f34-3a2a-ab65-5150f6ee44fc | -17.77836 | -42.8065 | 2025-06-04 03:40:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90758ec8-a9fc-3619-a170-3cd771601249 | -16.18529 | -43.72794 | 2025-06-04 03:40:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c22674b3-4ce4-3e00-9fad-61ee71cf1d84 | -12.31752 | -47.26027 | 2025-06-04 03:40:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8657c0a-b66e-32a6-89b1-270a3de38814 | -16.02752 | -43.67773 | 2025-06-04 03:40:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1eaf781-20b5-3b10-845b-b74cbca38f3d | -16.02748 | -43.68028 | 2025-06-04 03:40:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a57ef904-acc0-3559-8c48-5679cb99e8ed | -16.68147 | -43.88655 | 2025-06-04 03:40:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44448c2d-7a05-3883-9c89-8f5783530758 | -11.54349 | -47.31584 | 2025-06-04 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa4bd74e-6e2e-3e8d-818b-d641c53032cc | -11.53597 | -47.31965 | 2025-06-04 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fba95ecd-dcda-35cc-aa5c-b903cfa23cd3 | -22.54132 | -48.81183 | 2025-06-04 03:42:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README5.md)
