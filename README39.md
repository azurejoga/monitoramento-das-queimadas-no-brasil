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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98f7f515-293b-31a5-b874-916e323660de | -7.28183 | -49.39389 | 2025-08-21 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa331dd5-2083-33f8-ac01-8a741bfd5f5d | -5.5025 | -45.53777 | 2025-08-21 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad96e9b1-201d-32e2-93f8-5c527ceff2f2 | -6.5796 | -44.46552 | 2025-08-21 04:38:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d86768e3-b080-3752-b5fe-2a42081ec6fa | -3.81869 | -41.56582 | 2025-08-21 04:38:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0a94093c-c992-3164-a715-c37a9c8c8027 | -6.27321 | -43.71547 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d0162ba-fa0b-333f-9ee8-12ef510de072 | -9.10555 | -45.17891 | 2025-08-21 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4860279a-ff43-3d24-ab59-5b583758d20c | -7.02048 | -44.63189 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| cbe6fd20-5d0a-39e7-b52b-4e95b753ec18 | -6.07127 | -44.11094 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3530ff53-1a02-33eb-8f7e-1d1124a45072 | -7.64396 | -46.27161 | 2025-08-21 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 235a26ac-881e-388d-a9b5-0c906406baf3 | -5.64615 | -43.72233 | 2025-08-21 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4aa671fb-5e30-35d7-8d5f-739760284041 | -6.42722 | -44.6723 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 256d0012-b3d8-3bde-a7ac-0fd565fdd432 | -6.56533 | -44.47852 | 2025-08-21 04:38:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29f0e811-ecc1-3dae-bb19-52ba74fee9d1 | -6.5637 | -44.48588 | 2025-08-21 04:38:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d49374b8-3170-3ae7-9f09-a4185546f6f9 | -7.64351 | -46.24934 | 2025-08-21 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5c2276d-fe12-3cf2-955a-052e6cd27f32 | -7.86741 | -46.73038 | 2025-08-21 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e320c7b2-7e05-3bb1-9dbe-e275033f08bf | -9.85243 | -44.68859 | 2025-08-21 04:38:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47a58265-1794-3c1c-b5f6-1b3a921c2d6a | -4.29149 | -48.05943 | 2025-08-21 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 243c70e5-9c69-3474-98f1-2421c180752f | -3.48242 | -51.18835 | 2025-08-21 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21e6db89-c1e1-3ec1-8181-c79255aa35f8 | -5.96168 | -44.1428 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5b7f682-5cd9-35d8-a670-78735577d03e | -3.81793 | -41.57085 | 2025-08-21 04:38:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 24cd87fd-ffcd-3487-a59d-f3757f4cec54 | -7.7355 | -45.73243 | 2025-08-21 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11b43cb5-83ea-3416-9935-01afe2088df9 | -3.98047 | -43.24582 | 2025-08-21 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2100b6d8-7919-3ff5-a92e-b17397fc6a3f | -7.02609 | -44.62169 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 25f43735-a7d8-3100-903c-fa9184ce9d84 | -6.91759 | -52.85402 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a184d09-2875-3fc2-ae5e-7ccec52ffe07 | -5.99556 | -42.80931 | 2025-08-21 04:38:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 24a67e8b-1193-3b6d-954d-a0afdd693790 | -3.83991 | -47.41505 | 2025-08-21 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7be8635c-70aa-312f-a22e-7668a6474118 | -3.48103 | -47.68196 | 2025-08-21 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88fa6e7d-def2-3c11-87ed-71fa95cd13c6 | -3.04028 | -49.42839 | 2025-08-21 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8a86637-b2b8-3df9-89da-f024fe0260db | -4.85868 | -42.54171 | 2025-08-21 04:38:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 40d9cf89-98ff-3c2a-a113-27b9f0172ac0 | -7.70551 | -44.01432 | 2025-08-21 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f130f53-2f7f-39f8-9470-e85b63049651 | -5.8251 | -51.69002 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f47571a8-423c-3a23-a068-c85478a26a0a | -3.73732 | -48.93055 | 2025-08-21 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29023c0a-403c-3537-9088-6572916fd602 | -3.9847 | -43.24646 | 2025-08-21 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfbf371f-54ee-3913-b5b3-ddf3bb50ee91 | -6.72596 | -43.98317 | 2025-08-21 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d4b0243-84e8-33b3-8c27-065b5b414244 | -6.04232 | -44.3573 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db901ddd-af01-30f2-aee6-8cd5e78249af | -7.01397 | -44.62003 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 53a59fce-6ec9-3184-be69-f4976fce0138 | -3.45622 | -48.9677 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bad3570-03b0-3ef8-8ae3-ae7c1c03490f | -9.31958 | -48.93055 | 2025-08-21 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f98aa6ca-975a-3e47-8164-48512d9a173a | -5.22307 | -47.46886 | 2025-08-21 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb7ed0ca-220c-3413-938d-ddbfb1558289 | -7.79178 | -49.32456 | 2025-08-21 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 31a55974-8da6-30dd-8dc3-8f1898ecd665 | -5.99937 | -42.81464 | 2025-08-21 04:38:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3480733f-db6a-396d-9172-2e89ed2d99c1 | -7.81491 | -46.87094 | 2025-08-21 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4902b6a2-47c4-38b3-a96c-f1e6a6ad28d0 | -8.16068 | -47.35382 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 615fd05b-a78f-3ed2-a5de-2f45670ce858 | -8.26478 | -47.2883 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68833da1-ed0e-35d8-8e2e-deb05f3df305 | -4.93771 | -47.45916 | 2025-08-21 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b85aa92-9d90-33d3-8cad-49a30e6612b1 | -3.87771 | -50.97767 | 2025-08-21 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5ac4077-7dc8-3160-a3b2-d676f5d6df8a | -7.62348 | -45.26921 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ceee6c4-7dd2-328e-8ff4-cdf87a4efd84 | -6.10247 | -45.40784 | 2025-08-21 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59dc64da-7f96-357c-9834-083408c1a01d | -7.85235 | -45.18528 | 2025-08-21 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed89b89e-846a-39a4-af2e-cd412c786edb | -7.02204 | -44.62119 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 4c440844-25ac-3c64-b802-8bddadb1841d | -6.34067 | -43.4316 | 2025-08-21 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9b3dfa4-59fe-3314-97a6-a411f834331c | -2.38108 | -47.66312 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9bbf5a86-1ec9-3084-bb18-53ced73b3258 | -5.73234 | -49.13857 | 2025-08-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a91017c6-9a85-37a6-9933-e7b860c4c1ef | -4.64428 | -41.41302 | 2025-08-21 04:38:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f9c339db-42e0-369b-9678-655a9eae6d19 | -6.06254 | -44.11309 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f12028a-9f63-3a9e-83f3-d27be83f426a | -7.63035 | -45.24997 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 602b62f9-9d37-3bb1-a4ed-d8e103720b6a | -4.81968 | -47.31441 | 2025-08-21 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19238bd1-fb80-3f81-afa7-9ebdabf1e919 | -4.24825 | -48.61899 | 2025-08-21 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 960609ee-4eb2-350f-a525-b13a5b964e75 | -3.72969 | -52.36618 | 2025-08-21 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33f21b66-c9ca-3eaf-9ba2-7468bc1cdf54 | -5.97041 | -44.14031 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e036fcd-5fbf-3b41-a71d-4e081c1ba27e | -6.95095 | -43.86361 | 2025-08-21 04:38:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27842488-d541-34e9-a8b4-0b92f12613cb | -8.09429 | -42.35348 | 2025-08-21 04:38:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d123e511-cc46-3917-8cbb-cbb151bbefa9 | -3.65209 | -48.32729 | 2025-08-21 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b82ec4f2-8ac9-382f-b2f2-3709950a3b69 | -8.30649 | -49.0279 | 2025-08-21 04:38:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c703ef7-02fa-3da3-bdf7-86622d6230ef | -4.78722 | -45.32898 | 2025-08-21 04:38:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd0c37a8-ac71-3452-b7dd-23f176111698 | -7.15067 | -44.65024 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2372e5dc-aabc-3ccd-9f94-8ac3d0f06ba6 | -6.12708 | -44.7173 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d5c5d80-0f5e-32fb-a67c-ce260ed4d4e4 | -5.25393 | -40.72008 | 2025-08-21 04:38:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a44d4058-c278-355b-8b89-2d30b68278c8 | -7.59645 | -44.38459 | 2025-08-21 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8eaecb5-acee-3a96-aed1-62ad188f422b | -7.23798 | -44.70646 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41c4e1a6-0021-39b1-98d1-10c47c77d06c | -5.78237 | -45.06839 | 2025-08-21 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 29fd2bb2-c04f-3d23-813c-01bf6a57a6f5 | -5.95848 | -44.14275 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c21171d4-7742-31df-9418-18a315df1f8f | -7.70522 | -44.01988 | 2025-08-21 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6bcc8ea8-4914-31af-b080-9a60dcf92ed4 | -6.19885 | -43.57508 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 41b193ea-bc50-34d4-8c8c-e819257f35be | -6.39472 | -47.34151 | 2025-08-21 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4be34547-24c9-3f66-997f-bb5a326165fd | -6.16423 | -42.71669 | 2025-08-21 04:38:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a1d90808-515f-3e2e-8dde-a8fcbf15ab69 | -3.82958 | -47.73552 | 2025-08-21 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc68f09a-30e4-36db-a7ff-6283d844fb19 | -5.87869 | -50.14834 | 2025-08-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b03708f3-eb75-3a55-ae9f-a9a29a87c340 | -2.76571 | -54.43101 | 2025-08-21 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d37f44c-c7bb-3878-827f-fb5f6f9cfb27 | -5.87758 | -50.1553 | 2025-08-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f519fd77-488a-34e3-9bd0-59a91ce61f05 | -5.96578 | -44.14336 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 091b8785-bea1-3735-921f-153877b9a800 | -5.82559 | -45.62537 | 2025-08-21 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86aba848-0f2e-31a5-9f61-d64b75be4d97 | -8.14433 | -47.34324 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c9cf88b-a63e-3e7c-a5e1-849e225da808 | -5.78862 | -45.07918 | 2025-08-21 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3883afd-83b3-3ba2-97d0-855ff177eaf4 | -2.30502 | -48.1453 | 2025-08-21 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 733fa88f-e171-37b9-a378-45feeecf8892 | -4.31271 | -48.09865 | 2025-08-21 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 39d6abdf-8fc0-3dd0-bd1d-36c40f72a7f1 | -7.70432 | -44.02283 | 2025-08-21 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b331771b-5a6a-301d-9eeb-2e8a7edbbbff | -6.21544 | -43.33867 | 2025-08-21 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d827831f-9386-3f7e-8aa2-a1a5898c1997 | -5.67769 | -43.86679 | 2025-08-21 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3a56a7f-1a0e-3fed-815c-5b2b868c8aa9 | -6.4302 | -45.48993 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbc1d76b-8138-3c9e-a0ec-dc8b892ba820 | -5.08898 | -47.72007 | 2025-08-21 04:38:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 781b6fb8-6586-3a04-8064-14cb429c7542 | -5.77941 | -43.61024 | 2025-08-21 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6504628-f5c1-32ad-800e-16d92e2c7100 | -8.83428 | -52.03776 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f48cea75-f7a8-3485-92e7-94a7cc20a7a7 | -6.08311 | -44.42167 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 579939bc-faf4-3038-b9c9-bcff0ee3879c | -6.19338 | -48.10197 | 2025-08-21 04:38:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3825c4e1-7169-3258-9c9b-d9aba4e2f2e7 | -9.31567 | -48.9336 | 2025-08-21 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0db5125c-3f0a-3d8f-862e-882e42626b0d | -6.04287 | -44.35368 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13da3268-9f18-33c8-977b-d449fc80073b | -5.12455 | -43.21264 | 2025-08-21 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 754393d7-ad80-39ef-9951-3ff5af559ffa | -3.48158 | -47.67842 | 2025-08-21 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e02cd843-9809-3c9b-b535-2c7492198ea5 | -7.53352 | -45.01267 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README40.md)
