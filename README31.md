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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 023ffddb-3b42-319f-9652-75e261d67a74 | -2.96124 | -48.0392 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f08db7f-4191-32b1-9bfb-37a3be85e9ac | -2.5287 | -46.21575 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fad20049-3c07-3b41-b0c7-5004f3b5a552 | -3.7365 | -45.65479 | 2024-11-16 04:23:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0644622e-610d-3f8b-a7ef-a84f8e0a444b | -2.39873 | -49.03852 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f33a02ab-2f19-3a6c-9547-337738d4c0a1 | -2.29187 | -48.18726 | 2024-11-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bec7c59b-c8fc-315c-be14-44e5d85941c8 | -1.21443 | -53.56244 | 2024-11-16 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ffb3f57-11b3-3a5a-a526-cf0f649e139c | -3.55185 | -51.46388 | 2024-11-16 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1004cb7c-8a00-3fcc-97fc-45db9ddf3f02 | -3.24862 | -46.51977 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14445899-8dbb-35f7-abb8-6b8c54d6d555 | -3.49998 | -45.44086 | 2024-11-16 04:23:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa902dde-7c7f-37a2-93f9-61ede7188cf2 | -2.25139 | -48.15648 | 2024-11-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 474bd6e5-28a7-365c-a02e-5ddfe1ef5d01 | -3.75004 | -44.38089 | 2024-11-16 04:23:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| deb228a5-629b-3bc8-83cb-7f7067282396 | -4.45014 | -42.92942 | 2024-11-16 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2116e391-bce5-3a7e-a2a5-d9717dee1339 | -3.6914 | -50.11266 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e0b9c0ae-8593-3004-942a-5908b32c1c74 | -2.05103 | -48.8972 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8414868-6191-3dde-91bc-e260b0673f3a | -2.47738 | -46.36658 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f79a6bd4-27a4-3be7-a0a1-c3bda69fdc23 | -2.0848 | -50.49107 | 2024-11-16 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 153eb7b5-80a5-3f6d-8999-24bf1b6e4f00 | -1.58452 | -50.44286 | 2024-11-16 04:23:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c156f5de-0ee5-3b5b-8ab1-2cc0670134d5 | -0.75269 | -49.47299 | 2024-11-16 04:23:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67ddf7df-1ca0-35ac-abdf-8cf88aa2edb4 | -3.5033 | -45.44138 | 2024-11-16 04:23:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9380567e-4a69-3982-a615-c99c98204c97 | -4.36068 | -45.8624 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10fa028a-0113-3b1d-b854-79367a8d79d2 | -3.19604 | -45.54499 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 70beff11-dd85-3df3-b769-c29b744ce9d6 | -1.85773 | -46.28484 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13e15930-5b3f-301f-905e-6977b354b999 | -2.78807 | -48.56107 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f766dcb3-2df9-300d-a250-2248d54369dd | -3.61608 | -44.78872 | 2024-11-16 04:23:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d1617cc-3a14-3900-be44-604bdaa9a7a3 | -2.03273 | -46.37339 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd351be2-b3f8-3bbd-9f3c-da9a6891b83d | -3.11968 | -45.9865 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc6a19d3-6e39-38f0-b713-8c1735671a09 | -2.31103 | -48.46511 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bd9af39-3ca0-3a63-aead-2b85108a6c4d | -2.23066 | -53.61705 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c75efd6-6c0d-344c-909d-de6b06055b43 | -3.76314 | -50.79346 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e555fe7e-a5d8-380c-88ac-4d8b73571b6f | -1.1647 | -53.50269 | 2024-11-16 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8840ee8-be04-3ed6-946c-8b39e550c66b | -5.33393 | -40.89487 | 2024-11-16 04:23:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e00dbcfe-553a-38b5-8b39-7986906d78ad | -3.98125 | -43.72457 | 2024-11-16 04:23:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3389c528-5c4e-3f00-9a08-21582596682b | -2.8224 | -46.66071 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f415aeb8-7a88-307d-9054-b2f6890e1b08 | -3.25198 | -46.54205 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1df1e5c1-8435-3fbd-854f-4ca0ec0a5ef9 | -3.97416 | -46.70586 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6ad6ca5-b916-3a21-8f3f-f342b4c38b5b | -5.15608 | -44.09294 | 2024-11-16 04:23:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bc97f2ba-77ac-3d34-ad07-a50f25ca06ea | -3.99052 | -45.85004 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b180624b-4a25-33fa-ad7d-3327e659cc79 | -2.23179 | -46.83534 | 2024-11-16 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 741d7333-db76-35fc-b987-a637cad5f768 | -3.1955 | -45.54844 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e219da2f-95ac-3fc4-bf7d-00369dd40c8e | -2.67898 | -46.70123 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ceb503c4-b872-3d28-a9be-226c6b138235 | -2.25275 | -48.15599 | 2024-11-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77c35053-7f5b-3732-9b4c-d7a7848070e2 | -1.21498 | -53.55904 | 2024-11-16 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b887bb5-b367-36fe-a210-194a30c90179 | -2.20498 | -49.28255 | 2024-11-16 04:23:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0f4d24a2-723a-3558-8f4d-fbec4c6c6801 | -3.11672 | -45.89719 | 2024-11-16 04:23:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38d4c671-06db-35d0-930b-3ffa6b75b1fc | -3.99275 | -45.85747 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eae79e6c-ec99-3ca3-9d6b-3ea06c08e741 | -1.97008 | -46.36744 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98507fc1-e4f3-3e0c-8c40-6dca1d9d4335 | -3.12779 | -45.89182 | 2024-11-16 04:23:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83d2d3c8-d818-318c-b524-e0fd24560509 | -3.15953 | -46.60381 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e948cc5-c071-35f4-be1e-2aa043dd1eac | -3.27679 | -45.5052 | 2024-11-16 04:23:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e666011d-f69f-32aa-8603-452aed66d516 | -2.28503 | -46.45319 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0b5b2b8-469d-3e6c-a720-0fbfacb7ec84 | -3.03173 | -48.09401 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e86c681f-1686-30c6-b947-aab7c9f23d0e | -2.63011 | -46.19252 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1534d389-0a4a-3d13-b42d-05f31ce16957 | -2.61506 | -46.17941 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcc47a61-a674-3e2c-998f-c70558b81323 | -3.20501 | -46.46951 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8560417e-3a48-3d8b-929d-b7f57a901615 | -1.68843 | -48.46193 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6b77a6b-231c-3ecd-bc76-e0adbf799559 | -2.65961 | -46.17921 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6675c65a-f6a7-38f2-a180-603964a769c7 | -3.76374 | -50.7897 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e5363cc5-8cdf-3fc1-9fdb-c9448102f57e | -2.37147 | -47.93965 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56813677-413f-3206-84b3-5fd8ac3c0507 | -4.95266 | -44.726 | 2024-11-16 04:23:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b714bbc5-3444-397c-a8bc-9a5a7569fa25 | -2.14429 | -46.39479 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 402c02f4-3da0-3158-8367-d1ca0efd27cf | -2.58558 | -47.48222 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1a5ad1e-f6e4-389c-b541-5cf368c304d7 | -3.24863 | -46.54152 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83d50ad6-5997-39b2-8fd8-8ffaf5d73726 | -2.63066 | -46.18902 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7801626-a33a-3a94-9dd2-3982150343b8 | -2.9461 | -48.02055 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7244128d-b2ec-383c-a2a9-5913101fe3f6 | -3.95402 | -46.70273 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b409364-59a5-3bb2-9b09-2eaf25cdcc6f | -2.9454 | -48.32109 | 2024-11-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6d846875-9686-383e-845c-7b5042debeb1 | -4.48552 | -48.12076 | 2024-11-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b682fafe-f5ab-3be3-8cee-48840dc3e115 | -2.89285 | -46.87387 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 061c7efa-6887-3eeb-8990-d7a5a2a51df0 | -4.00505 | -44.33308 | 2024-11-16 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4af701c0-226a-35cd-9957-f0e8378214ab | -2.61287 | -54.53831 | 2024-11-16 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c49a47e0-804a-3cd9-963c-eb5f974350f9 | -2.29961 | -46.44822 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ac1449f-7c48-381b-ab4e-6fabb2c339a8 | -3.74259 | -45.65927 | 2024-11-16 04:23:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| bb710678-6b5f-3853-bde3-7b1e212665d4 | -2.31065 | -48.46648 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f7a2b17-ce70-3e0d-a8fa-dadcb0d0b58b | -3.16233 | -46.60788 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5791c442-8b36-343f-af2c-f9e0a44669d2 | -2.57371 | -46.54926 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97a26dd5-e1b3-3491-adda-e22745915b51 | -2.66699 | -46.84334 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84156605-7f38-3f8c-840f-39ad13778662 | -2.71292 | -47.98927 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 795e2dda-8b5a-362c-bbc5-39754eb1e6d6 | -2.63421 | -46.52583 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 775afa89-4103-367b-b6e9-340bb881c552 | -3.19218 | -45.54792 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bd91e24d-db43-3b83-b1a5-8ef2b58e4cb5 | -3.0156 | -48.0397 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 505062b8-59a2-3be2-8c24-07220bde0e13 | -4.3724 | -45.6203 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6469173f-c93a-3460-9752-afad0f230220 | -3.4241 | -46.09492 | 2024-11-16 04:23:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f70321f-11c5-33da-aaa7-97321845eae3 | -3.95047 | -49.75662 | 2024-11-16 04:23:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44112c4a-b401-3398-8345-28223cf5bbf2 | -3.59175 | -47.35246 | 2024-11-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| deba4b8c-6eb2-3ba9-9991-20110673267e | -3.05705 | -48.00473 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc73dc2b-9a13-3cce-88cd-bf49fe021d7d | -3.01497 | -48.04367 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2b4c1ff-326a-3007-9f98-c39b44179c81 | -2.61784 | -46.18343 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d15065f5-9295-3ca8-bee4-b69d4f228a07 | -3.09579 | -45.96499 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a4f6ac0-6689-3222-ac12-192df44c24d0 | -2.37439 | -47.94419 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b341d391-7ec8-3ce2-8322-3bb2d267b146 | -2.22059 | -46.35953 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 964cfab7-0b1d-3391-8703-4d46b86d32dd | -3.03325 | -47.97373 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86f47b24-728f-32e3-927c-324d80ba22d2 | -2.20333 | -48.81109 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1faf270-9437-3081-8584-2275c83d42c1 | -2.20282 | -47.56936 | 2024-11-16 04:23:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a00d0f6d-b8b3-3de9-9f54-8f23e60e6583 | 2.66268 | -50.90028 | 2024-11-16 04:23:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7473fe07-daf7-37be-8c38-50f584e1de36 | -1.15904 | -53.50504 | 2024-11-16 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5b72414-c40b-3285-8f36-ea5582f48eb0 | -2.63735 | -46.19007 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edb233a8-0aca-32d2-b0dd-0b4f20ad4bb7 | -5.66532 | -35.64913 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0e07b55b-8d5d-35cb-b198-ad89b2d1918e | -2.115 | -50.68326 | 2024-11-16 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d86530b9-23c7-35ab-b366-08fe004bcad7 | -2.14306 | -46.55533 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 149ea157-0eba-313b-838e-8d0d322ddd83 | -2.40182 | -50.32052 | 2024-11-16 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README32.md)
