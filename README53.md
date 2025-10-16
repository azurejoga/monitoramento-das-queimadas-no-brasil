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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0b61a31-4020-339b-b5d5-c93985eb9595 | -5.21049 | -43.79649 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a77ed0a7-02c6-390e-b749-8dfa97c888d7 | -2.44306 | -47.18216 | 2025-10-16 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86f49ac8-6509-3215-b27d-b799cbcaeb4f | -7.87489 | -44.93763 | 2025-10-16 04:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 44f0b2d5-dda5-342a-81c0-eb7bec4ccaef | -2.59966 | -51.34747 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 442b5114-da7e-350f-9c06-797750dfed3d | -6.1775 | -44.30317 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a7dfebc-06b7-3394-ad22-54ce680f9ee5 | -5.42217 | -44.23125 | 2025-10-16 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50bef60f-943e-3757-beef-e7a8f38df63b | -6.13964 | -41.74625 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 82be5983-3042-3f1f-b82a-fd6e2537448d | -6.57692 | -42.97421 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 956976cc-19e2-3ecd-8b86-ee30f3faf04b | -7.40178 | -44.74868 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 655e79f0-d3eb-31f2-a448-234d0b1646ae | -6.1864 | -42.60374 | 2025-10-16 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 139f4186-1010-3d77-8cd0-de7810853c5f | -5.45275 | -41.02385 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0522c8c6-40a1-38e7-8288-827c562af6c3 | -4.25258 | -48.56295 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc4e9fed-c202-318e-a772-529c09033582 | -2.72625 | -48.30882 | 2025-10-16 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf480b54-a17a-338f-88c5-43234e068957 | -6.56804 | -42.97292 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6c53ad0c-6cd3-35bd-8812-52d226fd24cc | -3.07291 | -49.50776 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5aa69620-95f7-3d02-95c5-485b699573c1 | -3.28901 | -50.14746 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c68b38c9-d00d-351e-881b-805840b203d7 | -5.87807 | -43.90175 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebc02600-71b2-37da-9a0a-3ff52d14b091 | -5.87767 | -43.84745 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3a8d494-7735-36e4-ad43-1808b6bfdb12 | -4.61781 | -49.5567 | 2025-10-16 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 927aff47-73ef-3252-9ef1-e94400212529 | -7.06665 | -48.36211 | 2025-10-16 04:38:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e97db21e-66a0-32e1-b032-a2fe78572c1e | -2.81479 | -54.38536 | 2025-10-16 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccd770fd-37fb-3cb1-ba1f-bd4f3b0e6ebf | -7.24841 | -49.51514 | 2025-10-16 04:38:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48fc5127-7f11-3ae1-b399-ee8b1550c98a | -4.17365 | -50.40351 | 2025-10-16 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68421e0a-2f5d-327f-8ecb-640f0189458e | -5.42011 | -47.11475 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc59879d-469b-3d3b-bb2e-1f38d5815471 | -4.67333 | -44.09876 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 196.0 |
| 42400963-fdf1-3e80-bcc6-8466ceb28f07 | -2.52342 | -47.12206 | 2025-10-16 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fc009ff-c486-3de5-9c7d-2b208dc3fc53 | -5.68129 | -44.35941 | 2025-10-16 04:38:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1edda6b-17fa-3f5f-b01e-607a9e6fda68 | -3.00823 | -45.38343 | 2025-10-16 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a199f777-c346-368c-9420-02858fc5d42b | -5.89742 | -42.82321 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eea3261f-54f3-3801-ad09-0fd726634988 | -3.88029 | -52.34413 | 2025-10-16 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76d5c1bf-fccb-3636-9e0f-23cf15985427 | -7.21525 | -47.55734 | 2025-10-16 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3149cd45-0ba8-3cf3-ad68-f8110138f41d | -7.57749 | -42.68299 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c6f2abdc-1774-31a9-8952-a2479b2ae5f0 | -5.32396 | -44.83895 | 2025-10-16 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b98bb99a-e6de-3555-bc49-c20515b229cf | -6.06748 | -41.90711 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d8f343c6-b643-3b34-93ed-f747c8988904 | -5.70449 | -49.30898 | 2025-10-16 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 157e48c7-2064-33bd-a3bf-e9489c19216a | -6.17654 | -43.43479 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eaa9f453-64ae-3783-b679-d3df5719a848 | -2.9526 | -48.58328 | 2025-10-16 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 958c4da6-3558-32dc-b948-6032232d858e | -6.25385 | -42.90651 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfd8d7ec-0b15-34e1-bcf4-c803b495833a | -6.26271 | -44.4925 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d48acc5f-e224-34ce-a069-287f6122d89d | -4.36134 | -45.5269 | 2025-10-16 04:38:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4e078f4-789c-360f-bd1b-73b30bbc69b1 | -5.73488 | -41.31423 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9ee8903c-13db-35f6-a266-190c4eac4b01 | -6.29279 | -46.77286 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7197aeea-8691-37c4-a228-93668061f47f | -3.09556 | -42.49703 | 2025-10-16 04:38:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3b80b3c-e5ad-311d-92a7-280668c82766 | -6.15833 | -40.91764 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 322c5ecf-08dd-3bde-bfdd-4d92f708f7a4 | -5.56243 | -51.01134 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65a39ef2-ef82-3565-b96c-6e93d28b343a | -2.26716 | -47.85279 | 2025-10-16 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 838fcf36-261c-3d9d-9b92-4050a631a328 | -3.12304 | -49.1015 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a75c1b43-87b4-3c01-b38d-63b25c3deab7 | -5.87861 | -43.89809 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b69ca1c-0a65-357b-8cee-df6f6b58babe | -7.30256 | -41.85852 | 2025-10-16 04:38:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5e93723b-0cff-32af-a333-7d3a3f071c6c | -7.93239 | -44.12458 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2ab618dd-4627-31f5-aa10-cb5a0a3b85e7 | -7.27897 | -41.95899 | 2025-10-16 04:38:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5d016b9b-1cf1-3de1-8334-b2343a6d5013 | -6.94879 | -47.73845 | 2025-10-16 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf540c1b-72bf-3aca-9d5a-b66b3a4f3ffa | -4.56241 | -44.00645 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d06b0abb-4275-3e85-bac5-240e1883da35 | -6.71338 | -44.39694 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8428295c-b101-3917-92d6-600ce1939786 | -4.66588 | -44.09404 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| dedf995f-39fa-3bf4-8977-67a81b9f5ec8 | -5.47733 | -42.9261 | 2025-10-16 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 503d2a5f-29ef-366e-a5e5-2828dee40c25 | -6.46666 | -41.85706 | 2025-10-16 04:38:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 903bc49f-ad0d-3340-85a1-2494e2ac2371 | -8.25599 | -44.09717 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9a79884-6980-30a9-8cdb-75b4a2d170b7 | -5.86795 | -43.88472 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| edcc1c77-bb5d-3235-a015-3615ec67eb1d | -4.84874 | -42.79108 | 2025-10-16 04:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c246af92-ec02-3cbe-b858-b6ab40f9e694 | -5.30175 | -41.17853 | 2025-10-16 04:38:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5506f304-afdf-3c91-b288-dc649d414af7 | -8.2311 | -44.02594 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e97d1e3d-c431-326e-afd9-1cb50d54c5d6 | -4.67199 | -44.08068 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34c9b92b-c5f4-3a47-9860-e7b8b7277fd8 | -7.52216 | -46.93185 | 2025-10-16 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f7172bc-fff9-330d-869e-b55a4a9129d5 | -4.67935 | -44.09927 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aaaf8b2a-9f87-3ff3-b806-416eaeb0dba4 | -1.42785 | -55.25294 | 2025-10-16 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e419740a-ddfa-390b-a715-bab80c5cfc2a | -1.65776 | -55.1429 | 2025-10-16 04:38:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 731e5728-ea84-3974-b946-1f728ef5b1f2 | -5.45712 | -41.0246 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a743b147-ec1d-36fa-98bb-48270533b294 | -3.81924 | -49.22245 | 2025-10-16 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c015abf-572f-3e20-8af7-c10e96a1f27f | -8.06878 | -45.41807 | 2025-10-16 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f54a187-483a-3cac-9afc-2f30418b70d8 | -2.26058 | -56.0563 | 2025-10-16 04:38:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c12b04ce-4206-3a30-9c58-f56d1942a9d7 | -7.97007 | -44.12997 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 11e4b298-465c-32c1-ad5c-5b9f2ccbafe2 | -4.66136 | -44.09684 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 81deb6e7-e802-3b9d-a4a0-ce34e5124fd0 | -6.45295 | -44.0363 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc0aea3b-7bac-3e1c-b967-f3e80a6e32b0 | -7.0556 | -46.6862 | 2025-10-16 04:38:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 99d601bb-b94b-3ea7-b97f-539b804dc398 | -8.21134 | -43.98243 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df990a5b-c45b-3746-9c2c-d40845e5a8ea | -4.18584 | -48.92525 | 2025-10-16 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81eb663d-b0aa-3c63-a6ed-39df5558d39f | -5.8873 | -43.86799 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ed669f6c-fe74-3a15-95bc-7bbf1ea63869 | -2.30364 | -48.57581 | 2025-10-16 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 682aff75-081d-3320-9d20-f7167e5be505 | -4.84811 | -42.79529 | 2025-10-16 04:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42cf2dbb-e306-30c5-867a-401812949e72 | -3.43533 | -50.2513 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab8ec16f-37d2-3ebf-82c6-08e8c44a4cc5 | -6.02469 | -44.31721 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 062b3f16-566e-3ef2-bcec-279a87b08519 | -5.90755 | -42.8158 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2e427ee7-055b-3018-b0d7-d1c773c093fb | -7.47309 | -42.14854 | 2025-10-16 04:38:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 920f4a89-1029-3e21-b0f7-adb5f24f26c9 | -4.8432 | -46.87248 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6a125e1-be2f-3daa-b117-8caf5b28b7a5 | -3.59713 | -48.87783 | 2025-10-16 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b24c469c-ca36-3e8c-a103-322aa9c0913c | -6.06847 | -41.90827 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 22443a05-8469-3b35-b8d9-79fed14babee | -1.65697 | -55.14011 | 2025-10-16 04:38:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc1e1154-a4b9-315f-8a10-3b8b597e74cf | -5.88157 | -42.80734 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 596be14a-a73d-302e-acb5-53493abe4dbf | -6.03619 | -41.92295 | 2025-10-16 04:38:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 75427045-792b-3f78-832c-1475cb435a07 | -7.46587 | -42.67729 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ca7a4ec2-a8ff-3150-84c9-80d0069c9f63 | -3.17385 | -49.75286 | 2025-10-16 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d68a5845-53bc-3618-9ebc-b19bd8d22ea4 | -5.24576 | -43.40954 | 2025-10-16 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a3528c36-d75a-30f8-b904-6ee9625a01d6 | -5.72883 | -43.83718 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49eeda43-e8f2-3a3d-874a-91cf83ab7ec6 | -4.24372 | -45.76 | 2025-10-16 04:38:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2cd38a7-ab14-3030-8344-5f9949bc558f | -7.95531 | -44.14378 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e862d15c-8ff7-36cd-9819-554ee80c24f6 | -7.53339 | -46.6405 | 2025-10-16 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39bd6ed5-c280-3490-b80e-3449e8982c51 | -8.26516 | -43.43877 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce72a6af-7510-3e31-b029-7cd4c6347215 | -6.5501 | -43.92106 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b15d3d77-b1fe-398b-8c1c-06213d8eff98 | -4.97165 | -43.60284 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README54.md)
