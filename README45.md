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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21f9b1cb-d45d-3185-9253-0d0a06445f1c | -6.19587 | -44.24543 | 2025-09-27 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d19e40be-1a75-32a9-ae5f-5235a5f0acba | -2.17807 | -47.08221 | 2025-09-27 04:44:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 198cdfeb-f469-340f-bd17-1a40e69f2d87 | -6.99138 | -42.38773 | 2025-09-27 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5b82842a-c20e-3611-9aaf-1bc644a8b03a | -3.316 | -44.18985 | 2025-09-27 04:44:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fb9a58b-9b4c-3e46-a99d-ec479ce48d96 | -2.85356 | -49.49182 | 2025-09-27 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69e96cb4-c4ab-377e-b351-7656bcc337ff | -6.07011 | -43.20273 | 2025-09-27 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ab2e123a-b092-3dc0-a787-7b47f08a1cd5 | -6.22742 | -44.18582 | 2025-09-27 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b29bec7c-72be-344b-a6d8-f9199ba09817 | -3.80996 | -51.39265 | 2025-09-27 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad76b078-ca83-3d72-afe7-96e480419fff | -5.03812 | -38.01265 | 2025-09-27 04:44:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c6159972-2d67-3881-9249-3f942ac200bf | -7.86593 | -45.29099 | 2025-09-27 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a38ddc4-5101-32da-971f-292dbedf8b19 | -5.62888 | -45.3358 | 2025-09-27 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f16f4be-d737-33ce-b9ce-8c0e63b98866 | -7.87415 | -44.0187 | 2025-09-27 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 401b5960-453d-3903-8234-b2a47925a6da | -6.70148 | -42.75573 | 2025-09-27 04:44:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8d47d388-a96a-3f69-b3da-a55fd08995e0 | -9.96331 | -43.60696 | 2025-09-27 04:44:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ca42626-f258-39ce-af15-abfd97f65314 | -7.77881 | -46.94108 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| edc7d7ba-f940-3d85-ac6f-31cf3234a3a7 | -8.81979 | -46.26711 | 2025-09-27 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebc218bf-4298-30ba-914a-d9f015b1608b | -7.87744 | -44.02934 | 2025-09-27 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4e59212f-5b7d-3912-9227-b60d6d2ee3b6 | -3.2195 | -50.6402 | 2025-09-27 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3c3c41d-46e1-3ef5-927b-81923de449a4 | -9.00611 | -47.83698 | 2025-09-27 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f81cb2c-4abe-3604-9f21-4f3ce22c35b5 | -9.11535 | -45.88055 | 2025-09-27 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66471f95-5297-378a-b7f0-58de7622dbde | -7.77953 | -46.93623 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c70ef41b-d4a0-35ca-ad99-b84a4e36d99c | -4.57368 | -44.07865 | 2025-09-27 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d5a9151-84a7-3af2-920a-1835d5753b25 | -2.4505 | -49.02922 | 2025-09-27 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbb547af-f61c-3063-a790-f6a0ad0e40c9 | -8.32662 | -48.00804 | 2025-09-27 04:44:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 455903e7-4be5-39a1-b97a-0cb8ece0e5e5 | -6.27141 | -44.07398 | 2025-09-27 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 024c0dfd-3e86-3272-beab-e7075e93b37c | -4.11415 | -50.05098 | 2025-09-27 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ed2f20c-22b3-3535-82ac-35d8c6ed4b5d | -7.652 | -43.82872 | 2025-09-27 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7dbc4046-ee56-3816-8d99-b484de79e426 | -5.79591 | -42.83324 | 2025-09-27 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 433d29e7-c792-3008-b9fe-fd543dfb92be | -2.33018 | -49.0824 | 2025-09-27 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2540e7b6-d0c3-3b15-abd8-57316d7e90e5 | -8.85814 | -46.61393 | 2025-09-27 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8320785e-b7a3-3c8d-acf5-be41fb76c102 | -4.0073 | -46.96916 | 2025-09-27 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf960616-765e-381b-b74b-b1c139e86831 | -8.69435 | -47.02906 | 2025-09-27 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ba3fa98-1838-35b6-ae85-9e91231611f0 | -5.07753 | -44.85789 | 2025-09-27 04:44:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d4a03b00-671b-3272-be72-747fd57caff4 | -8.72443 | -46.69134 | 2025-09-27 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28e9e802-a4b2-3412-bb3c-8dbb07ffefd9 | -6.99698 | -42.38539 | 2025-09-27 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 220a4c32-38b0-3898-91ca-272a1596c425 | -5.22972 | -50.73123 | 2025-09-27 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bb19aa8-8cab-3709-9978-24b10a5634fd | -3.99996 | -46.96813 | 2025-09-27 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 740775a9-1368-383c-ad84-1346656f88fe | -4.5721 | -48.01899 | 2025-09-27 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80a5c9ce-9fe6-33b8-ade6-a685168f6e04 | -6.15708 | -43.99203 | 2025-09-27 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f544406-555f-35c0-a44a-07ccf6bd04b2 | -4.80526 | -46.81308 | 2025-09-27 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7cfd045-1ae6-3b2c-971f-fd7479ddf295 | -6.05968 | -44.0808 | 2025-09-27 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 532a18e0-9f92-3057-b8ba-7da0f83338fc | -5.79173 | -42.82724 | 2025-09-27 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e4e9a61a-b03a-3e59-bc93-f2690750e860 | -1.17754 | -54.13931 | 2025-09-27 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7eb39be-3d5e-3519-a4cb-a0b43dbde383 | -7.61707 | -43.82746 | 2025-09-27 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca83bb72-1167-33d5-85f3-b9e2836bef67 | -6.53555 | -43.83515 | 2025-09-27 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f879de31-fb25-3bed-91e3-ec8ef2390fe2 | -7.62436 | -43.84401 | 2025-09-27 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e1c7642-3b70-30bc-af15-6bdc50dcdde4 | -6.54955 | -43.83695 | 2025-09-27 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9daade9-795e-3ce0-94ec-c25943bacaf3 | -5.74383 | -44.96712 | 2025-09-27 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29ec2821-6e57-34a5-9ba4-e7b5893b3f50 | -3.33603 | -50.20362 | 2025-09-27 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37bc6668-6595-3207-be2d-f282c73e958d | -6.6998 | -44.58469 | 2025-09-27 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c7b0043-4841-3949-9d17-9c63e170a30c | -7.64723 | -43.82827 | 2025-09-27 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c33d37be-e8b2-3748-b3ac-53590f20e4fc | -6.99572 | -42.39463 | 2025-09-27 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b4c61de2-e635-3507-ba17-a24b7022dfb6 | -6.9953 | -42.39768 | 2025-09-27 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 45d0a6b0-dbde-3cd7-bf34-fe76472ee41b | -6.54881 | -43.84205 | 2025-09-27 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3726d1b8-78a5-378b-b4bf-8ae320e40bf1 | -5.80321 | -42.81754 | 2025-09-27 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7d9c8b9c-a71a-3474-a189-35f0cd1e1706 | -5.38284 | -49.66637 | 2025-09-27 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63a3b2f5-fc10-360d-a020-17a1bea31490 | -6.95585 | -43.35483 | 2025-09-27 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e4ff602b-fef7-3797-9fef-303553e0eedd | -4.67087 | -50.97888 | 2025-09-27 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 246cee7c-9bdd-3e77-9eec-abaade051f85 | -1.13048 | -54.21146 | 2025-09-27 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7788760d-e789-3820-b7b5-9038d782b43b | -6.70039 | -44.58052 | 2025-09-27 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 53aa060f-f695-3777-a202-d8938bd1dee5 | -7.62541 | -43.84674 | 2025-09-27 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 43b6455c-cd7f-3e5a-a826-04d5242db584 | -4.58896 | -50.65876 | 2025-09-27 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da4463a3-f694-3f11-9919-a00b7261d522 | -9.99999 | -44.17426 | 2025-09-27 04:44:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccaeb05e-f468-3a83-835e-ac7b73bbdccd | -7.34244 | -42.09455 | 2025-09-27 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3c1a98a7-8ba7-3d2c-b99a-e51be499a3e3 | -2.91707 | -48.19372 | 2025-09-27 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 363eb861-6ed7-3679-b6b3-61267b9e44b5 | -6.54414 | -43.84148 | 2025-09-27 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39d2f2bb-4766-37db-847a-27d9860758fc | -3.58677 | -43.09871 | 2025-09-27 04:44:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ee13087-82ea-34de-b2e7-7ddebf605958 | -9.97402 | -43.6026 | 2025-09-27 04:44:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f69b964f-854d-3f2c-84f0-b77a3c29b856 | -9.24178 | -48.56246 | 2025-09-27 04:44:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51dc707e-1f88-329a-a790-cb9d2eb03f81 | -7.62908 | -43.84472 | 2025-09-27 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ccdbb1ed-5295-3a1d-9af2-e924ba2f2e70 | -3.44279 | -44.12287 | 2025-09-27 04:44:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97b49472-cd63-39b8-8d82-0a13d777c172 | -9.11698 | -45.86903 | 2025-09-27 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5909ae5e-f75c-3b8a-96a3-06bd3ac5e110 | -1.16309 | -54.20668 | 2025-09-27 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e909a76-9cbf-3c45-9d6b-79448c77273d | -3.84093 | -49.25853 | 2025-09-27 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78c62116-7097-321d-bf8f-7b9839e9f6fb | -5.46854 | -43.07389 | 2025-09-27 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3489f2b4-5b09-3148-8179-4ca6bd7f8fc1 | -6.92904 | -44.6462 | 2025-09-27 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e01a3adb-3003-3910-b06d-399c078711d2 | -8.67299 | -43.99389 | 2025-09-27 04:44:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af34227f-4c36-3f55-a737-31372d77a58e | -6.70273 | -42.747 | 2025-09-27 04:44:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1c05ca7d-8ed1-3e9d-a70a-189e475ecee0 | -7.14454 | -45.51092 | 2025-09-27 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f9cc0e3-eeaa-3ace-9e96-f02aacd9b9c1 | -7.35158 | -42.09597 | 2025-09-27 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 38b885f9-91f7-370e-99e4-14b4a930b4fd | -6.2685 | -42.49362 | 2025-09-27 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e4c2ee05-e6f9-3997-8fe1-666f02d90315 | -7.60349 | -43.06059 | 2025-09-27 04:44:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 99c2d883-07d2-3550-91df-55f20b2cf617 | -7.62362 | -43.84911 | 2025-09-27 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1310ef61-206d-3a3b-bdc9-8bedcf45e121 | -6.25619 | -42.47035 | 2025-09-27 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 95469b16-9b32-3763-9c13-596d97c95a4e | -3.05766 | -48.70849 | 2025-09-27 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 401a1675-d76d-36e0-9c32-05185c39d397 | -4.00427 | -46.96449 | 2025-09-27 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5cb32611-1584-36ef-9115-54dc3780d33c | -7.72115 | -47.30618 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96dc7f16-cef6-3ac1-9034-c58f1778324d | -8.3174 | -47.037 | 2025-09-27 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2589eaed-6ade-3838-a8da-40d61fc6e0e7 | -3.82853 | -40.99281 | 2025-09-27 04:44:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| edd93cfa-0b7f-3592-818f-b3cd537d2683 | -6.33568 | -43.35861 | 2025-09-27 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fe9392a-277e-375c-b476-78e43aba3280 | -7.71671 | -47.31019 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c81fccc8-4eda-33fd-8b19-36083dab1276 | -6.81396 | -44.4742 | 2025-09-27 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8c96a2b7-28b3-3139-822a-8bbbaf4ceaf5 | -6.63042 | -43.82542 | 2025-09-27 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fda7c82f-6412-36a7-85c0-7a2e0a3c48e3 | -6.32175 | -43.45723 | 2025-09-27 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a5d9810-e190-31f5-afb0-fb35510dbd7f | -5.67382 | -44.85 | 2025-09-27 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4cc178e-a7e1-3a4d-84d6-4b46dfa99817 | -7.12023 | -42.18612 | 2025-09-27 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 944fe94c-094a-3cbc-be28-eed83453ebf7 | -7.79068 | -49.5639 | 2025-09-27 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5bf34f58-fd17-3121-aef1-37c8584d45e2 | -7.64216 | -46.77739 | 2025-09-27 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05cdf601-3615-3046-bf2e-c34222f49567 | -4.262 | -48.55494 | 2025-09-27 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0277ebcf-463f-38a1-81e1-1f560d16572d | -3.44341 | -44.11871 | 2025-09-27 04:44:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README46.md)
