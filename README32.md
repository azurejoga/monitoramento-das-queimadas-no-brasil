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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0fa5ac3-09d3-3640-a4d0-20f1d2c22607 | -4.68423 | -40.14736 | 2026-09-21 04:19:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 97acef05-f7eb-3443-af96-e2dcaaa4bf3c | -5.84594 | -53.52234 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cef0a483-c803-3fdc-88c7-5f62b712268b | -6.56396 | -45.55341 | 2026-09-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93856630-b4f5-3d45-9073-ed2a19ea5900 | -6.03469 | -53.27647 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afb538ef-b024-3e3a-8ec3-f869d4bda703 | -8.45424 | -45.8772 | 2026-09-21 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09ccdd6d-c85d-3d9d-a576-5131d73f96b1 | -9.37062 | -40.31651 | 2026-09-21 04:19:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1b3601dc-64fb-3d15-8f4e-f23fd201963d | -7.56882 | -57.68625 | 2026-09-21 04:19:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d5c4b92b-4e3f-327f-b232-6681f932441e | -7.73725 | -49.38875 | 2026-09-21 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f66c7af-f08e-3dcb-befd-2ad3690af967 | -8.78008 | -48.73391 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c876fcf-0e73-311e-a8ab-05d6fdb83e6e | -6.98254 | -42.1724 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0f8d8841-79db-3fb8-b156-6faabdc3437f | -6.99444 | -43.37185 | 2026-09-21 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7e8afe87-20c4-3b49-ab15-ff7683588fc9 | -4.5645 | -42.97162 | 2026-09-21 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92e5f219-4656-31f0-8904-d3c6bec526dd | -9.24904 | -46.18478 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7bc8e62-c920-3138-9c65-1fb9acfe1d56 | -8.77634 | -44.28016 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a473a05d-6663-31ed-a081-aaa596e799fc | -9.26633 | -46.18765 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c63a8de4-377a-3c30-80b3-47de7d18ce4b | -5.8716 | -51.58495 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e500c39-3e52-3274-9cee-3384a11ec0b5 | -8.82879 | -50.48963 | 2026-09-21 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6e49cf9-c297-3a03-97e6-34749b1fb6a5 | -8.47366 | -45.08696 | 2026-09-21 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c942ab62-2470-3b60-966e-6653496847ec | -9.01935 | -49.82877 | 2026-09-21 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5b102b0d-6081-32b0-a638-c2385cf5d2da | -7.25047 | -46.90611 | 2026-09-21 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c26f4778-d179-3f43-a56d-f8b621a8f87d | -4.68073 | -40.14661 | 2026-09-21 04:19:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ca212edc-4b59-3315-b5f7-fe19a011d8e2 | -8.78806 | -48.7476 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 89d7b19a-0ac4-3acd-9f79-1326e7923cf2 | -7.45092 | -46.87315 | 2026-09-21 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4171d8e0-e5fa-3384-b37d-30422338962f | -7.42055 | -44.78861 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f15d18c-a700-32a7-9d7f-33fc91e9f247 | -7.32665 | -55.21349 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fdb95ff7-f7e4-3311-839b-ce9ee52c0a7d | -6.30001 | -41.76302 | 2026-09-21 04:19:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8de17e7e-6d93-3968-9974-2acc0f2ce20c | -8.77441 | -45.87071 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0b1f9e6-2500-325e-ba7c-5e7504c34fd3 | -4.84663 | -40.5234 | 2026-09-21 04:19:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ebe5d717-a2d6-3670-8d71-e40461f198c3 | -8.77798 | -44.29116 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f878dbd-8aca-3936-bfc2-6c6aace7338d | -3.66397 | -54.27862 | 2026-09-21 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0664e6d9-5ef1-39c0-aced-8ff49811ebe3 | -5.85028 | -53.53136 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 299633f1-d6d3-3c49-8425-1c6ec446ac4b | -8.7708 | -44.29358 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0294b93-b148-3ed2-a7cf-a63504aea050 | -9.45399 | -45.38609 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 21ecbede-8805-3580-aa5b-3b902c3213d0 | -5.37913 | -55.90094 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba56c8f0-2c9d-3afc-b40a-a05b42dc0c98 | -4.74559 | -41.10523 | 2026-09-21 04:19:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3cbce427-6e62-3920-a45f-44c5f6d2a922 | -8.76636 | -44.30005 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14506c4f-ef14-3cac-b10f-41eca06c9e44 | -4.3404 | -55.6684 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9c46f14a-e8bc-3f32-9ff2-506842674ee3 | -6.21277 | -53.57243 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5481390a-ddaf-3f0f-9843-e11f1e9f34e1 | -3.39429 | -50.43948 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f416142d-9ee0-373d-9982-0f6fc74e0746 | -7.456 | -44.73937 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 126384f3-091d-3e83-ada5-65531b3aa83d | -8.37456 | -45.63371 | 2026-09-21 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7165890-ea38-344c-9b4b-29f154f6b305 | -6.7369 | -55.09717 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c69299b1-2949-3b46-a242-42ed0a5d637d | -5.72651 | -53.45532 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8fcb4ee-4f0f-3106-aeb2-4e192de28d40 | -7.45264 | -44.73885 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9e55421-e629-3719-b36c-28d203df6b07 | -6.46792 | -42.76971 | 2026-09-21 04:19:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bbff76c5-05c2-3c72-8617-ef539c8b866a | -2.58562 | -48.43814 | 2026-09-21 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49fd5ed3-6781-3522-a7b7-0ce8dadca69d | -2.826 | -46.7044 | 2026-09-21 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b011531c-29c9-307a-b00b-9dc28d840160 | -6.89127 | -41.70367 | 2026-09-21 04:19:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9a090a98-7c4e-3198-a86a-5bc5606c19fa | -6.77125 | -55.49331 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acb18944-3dce-333f-b9fe-b45564c6018b | -7.02791 | -42.08044 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2b284740-e85a-3689-9b8e-e73d6791c228 | -7.55241 | -44.94572 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42e8b783-3c8a-3066-88eb-21eae8a085c4 | -5.81004 | -53.52399 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 809a811e-fa95-3e28-8db2-7ec00f23aeac | -8.77743 | -44.29465 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 23942456-f2f7-38d6-a48f-d31cfc43fac9 | -3.00688 | -54.18148 | 2026-09-21 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9e26c73-7a66-3499-8416-8422d24277a2 | -6.91803 | -43.72523 | 2026-09-21 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54851bf8-c520-379f-af61-057a48db7b06 | -7.57736 | -57.68043 | 2026-09-21 04:19:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a0ee19ea-b652-36d0-b490-6d3d277ecb7c | -7.32761 | -55.20835 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 88885202-bf95-399b-a144-02b222280478 | -8.77085 | -48.74005 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a703d43e-8122-3f12-b971-45c82eb11240 | -4.22023 | -48.61612 | 2026-09-21 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c59fefd8-87e7-3b79-b796-36d41eb71f0d | -8.94306 | -49.05602 | 2026-09-21 04:19:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdefcd9c-67a0-36de-902d-32227a403e77 | -3.44791 | -50.60006 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ae8b2e2-f3f8-378f-951b-c7e7bce8b76a | -8.13195 | -46.81684 | 2026-09-21 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9ad2a50-994e-39a2-8fdb-8d599b4813d8 | -7.88435 | -44.84473 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc48d5a8-6e9f-3f5f-9cb2-85eeff82451a | -5.84029 | -53.55431 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 380caba2-38d8-3044-90b7-a98415fc8ef7 | -6.56112 | -45.54904 | 2026-09-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa83271b-1282-3bdc-bff8-5952fa855dd8 | -9.02222 | -44.90847 | 2026-09-21 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97c90037-447e-3eda-bb04-af6ed260569e | -7.3959 | -46.16568 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5726ee15-5041-3fca-b22c-963c6c3bda7f | -7.41834 | -44.78094 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1ea65483-a577-3ef9-8132-2555b7dc52a9 | -3.39338 | -50.44481 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7b489967-dd3d-3bda-b74a-a284d7272f95 | -3.38946 | -50.43841 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f52e9331-b33b-3692-9491-933d668acd41 | -7.12784 | -42.07039 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0c65efdb-802c-3fd0-a77d-c73eaca5b3c7 | -4.22383 | -48.62079 | 2026-09-21 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dd7b1138-ebea-328c-9d01-e864a7ee884a | -6.99823 | -42.20404 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5041371e-48eb-3072-8bad-d3b4e26f1867 | -5.20566 | -56.10493 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7d90698b-fb82-3a5f-8dc1-713d1f8902f9 | -8.37517 | -45.62992 | 2026-09-21 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3143d855-62b7-31b3-8ec6-1ea1c78af51e | -4.40967 | -55.24556 | 2026-09-21 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4853a7c1-467a-3bd9-94a3-391788c02936 | -9.02454 | -49.83033 | 2026-09-21 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 07e45f22-5f68-35bb-8217-6695ab5f2a70 | -7.29586 | -46.76897 | 2026-09-21 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15519e1e-3030-3c0e-8ab1-d35a7ff42a23 | -2.26322 | -48.75372 | 2026-09-21 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ceab12a-82c6-32ef-895a-eca4b9ceefc1 | -7.53754 | -45.8801 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08ea2f7d-206b-3b52-b09f-db53659e652d | -9.27201 | -46.19636 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49e3fd35-0efa-3ce8-a645-2906e03db6b6 | -7.42342 | -44.77078 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1816e67-969f-30dc-867d-84bb0f574787 | -9.44565 | -45.43702 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b9a7d05-ce3f-3d84-925b-a7f65dc47f41 | -9.46232 | -45.39862 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dec93518-59bb-31fb-80ff-fc68a5fe3f4e | -6.90715 | -42.93529 | 2026-09-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 305a1da1-51a5-31b4-832c-e7bf85211d7f | -7.06011 | -49.90695 | 2026-09-21 04:19:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ed68c8d-58be-36e9-b03e-837808f71776 | -9.309 | -48.21494 | 2026-09-21 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a746e3f1-ccb9-3a07-9357-b02345242c88 | -5.83368 | -53.49122 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72816609-f737-31a4-967d-b4c57df64502 | -9.46272 | -45.41735 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a9846a0-7061-30af-b1f6-2724b535602f | -9.44944 | -45.39278 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 00624bf6-46ae-3f12-a090-b35c2a434dc4 | -7.41795 | -44.7407 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 409e5d12-5620-3051-9094-ee60dd9db098 | -3.00229 | -54.1707 | 2026-09-21 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8042b531-0f5e-33d9-a68d-11485b0a2a05 | -7.11612 | -43.56894 | 2026-09-21 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b0f8da7-4334-3718-b301-636e21d0404e | -7.12238 | -43.72203 | 2026-09-21 04:19:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec380fae-a57e-3583-bf3e-e2854e0ea706 | -7.88156 | -44.84064 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19999e9e-a593-3a63-9cd9-b9ae92ed7c89 | -9.45082 | -45.42662 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3261d7ce-af91-3d7a-811f-926f138fbcc9 | -4.74218 | -41.10474 | 2026-09-21 04:19:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6fee181e-3891-33f4-b6f4-c537b87795fc | -9.47301 | -45.39664 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7607d6c5-ddd4-30e2-8897-e6052acc68f1 | -4.3449 | -55.66629 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d95b203b-27c1-3a2e-bcd0-f3d37dc269bf | -5.87965 | -53.63483 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README33.md)
