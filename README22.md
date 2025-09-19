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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31378131-6eeb-3582-b665-e4a23e3d6fce | -4.68945 | -43.24486 | 2025-09-19 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d1259bc-c95d-3a68-99c7-441286accb42 | -1.75961 | -48.04982 | 2025-09-19 04:44:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3d305c23-12ff-319b-8bf0-3e5a54356674 | -3.07961 | -49.46785 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c728084-adef-3250-87d5-86f05a584054 | -3.53582 | -53.02337 | 2025-09-19 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c62713d-0235-3c94-8cfa-0b7634d5bd0f | -5.6334 | -43.89429 | 2025-09-19 04:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 950596a0-0f43-3654-a73e-daf364c46ce0 | -3.86443 | -53.53279 | 2025-09-19 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66ca615a-1e46-3804-8b29-e73b3db0e663 | -4.41012 | -47.59762 | 2025-09-19 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 467f0e4e-5ea9-3166-a0b3-3b7b3dc02762 | -11.09331 | -41.06586 | 2025-09-19 04:46:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| b276317e-2e82-3fef-a5b7-7a8dc61e3d30 | -7.44748 | -42.62534 | 2025-09-19 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 56113017-b408-3d30-8598-3d25f2294896 | -12.09715 | -44.84486 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa5a6203-4d6a-33d2-8dfe-d82cf9bf1517 | -8.74828 | -44.23205 | 2025-09-19 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d6d6da9-c033-3607-84e6-48530cb3548d | -8.05206 | -45.72445 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 750fdcdb-7fc0-38e4-a8e1-2bf7f706a5b9 | -7.58162 | -45.47876 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c8e8b93-f8e9-3b69-8a2c-93ce3d2ee78b | -7.25952 | -46.34523 | 2025-09-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4b1f44d-ba78-31e2-80bd-03a30b035c65 | -12.08788 | -44.83745 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87b36d7e-4101-3335-95c4-c387c249884e | -10.6814 | -46.47194 | 2025-09-19 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15ec899f-9dd7-3224-a8f1-ae456b301567 | -5.83197 | -46.28316 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e8544de-5b59-3b89-8e9f-86920aca96a7 | -8.03204 | -45.71341 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c74c0ccc-0590-3415-9704-3c79524856a6 | -3.92619 | -56.03556 | 2025-09-19 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b0f8072-96e3-34fa-bf5b-529bc5f7deb9 | -6.39336 | -50.91203 | 2025-09-19 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f761b5d-cfbf-30a1-a696-3f81803f5fa9 | -9.17895 | -45.31779 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0f3a68b6-723f-3706-9baa-1bc915263e9a | -8.63332 | -45.70873 | 2025-09-19 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 570b14bf-c709-326f-b9a8-86a71a740937 | -9.17069 | -44.6553 | 2025-09-19 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b5e9bcec-d63a-3ee8-b580-2e98b98db905 | -7.54721 | -45.50616 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf3f2eeb-dfac-33d1-8fc3-f13524facc95 | -8.95265 | -44.20576 | 2025-09-19 04:46:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01016c56-55bd-3d4d-9d6a-ef2436135695 | -7.57792 | -45.47419 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e6dd284f-e1e5-38a6-a379-8dbbcaf1f415 | -7.70297 | -44.46797 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 082dffb7-7ca4-3487-83cb-7a5c87609979 | -7.81427 | -46.1699 | 2025-09-19 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e1737b59-13af-3aaa-a50a-830daeec6aee | -7.26407 | -46.34225 | 2025-09-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d1a444d-1aaa-3b06-abf1-42f8f3a1f1d3 | -8.03238 | -45.74171 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3b6ad881-f6b2-337e-8334-d71daa73e317 | -11.16216 | -45.32892 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 019111f9-90e6-31ec-9d43-f953ece46585 | -6.58485 | -45.58366 | 2025-09-19 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ded6377-3881-3c34-b186-171ee418c405 | -8.1379 | -43.62499 | 2025-09-19 04:46:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6f9b5ab-17e4-3a92-98a6-7c3ce21c98f0 | -6.38409 | -43.32924 | 2025-09-19 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebe3bdcc-81bb-357a-8003-49c0a36937b8 | -9.02645 | -44.89046 | 2025-09-19 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cacbfb9e-2ea2-362b-8122-6802bc37221b | -7.57849 | -45.47022 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ba80ea3-3c37-3d33-952c-c0d87a73ca93 | -10.03325 | -46.22795 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93d8a465-5c2b-38cd-9ca9-16768bcc4b4c | -11.59906 | -49.82656 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d6d1afb-6a4b-3074-952d-111b84b49dbc | -12.09653 | -44.84986 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21e78c3f-b54f-3e57-8689-12f5c5f3382c | -11.21074 | -49.63718 | 2025-09-19 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ab89d043-25f7-39a1-867f-606f9a240f97 | -5.46891 | -47.4542 | 2025-09-19 04:46:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ae9c2ec-7df6-338c-89c4-a8fc3822a3b9 | -7.83695 | -46.21237 | 2025-09-19 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b97272d1-766c-32b8-b62d-f985dc2dcc41 | -10.02909 | -46.22703 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a6457e1-6dbe-3f81-b716-eca56de5fcc4 | -5.81244 | -45.71284 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5c0e2c0-cb4a-3d4d-9539-778166aad587 | -5.86783 | -45.90265 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 156902c1-4462-32dd-b407-9cd0247cba99 | -9.1657 | -45.31582 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98de95ae-10dd-30ce-a926-db82910ce656 | -5.79549 | -45.36425 | 2025-09-19 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd141d3f-173e-35a8-b562-400d096ff7d1 | -4.94084 | -49.92495 | 2025-09-19 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1421ef06-905c-3a5e-b846-f5e21da5557a | -6.54712 | -49.50031 | 2025-09-19 04:46:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7b0b86e5-1786-37fa-ae26-ffbb17949318 | -7.566 | -45.49646 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 403628cc-e2ee-3c1b-a0f4-c1441b283ce9 | -7.00936 | -44.63652 | 2025-09-19 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 464d3f4a-a248-3159-bdb7-045d36c0a448 | -5.67289 | -45.34678 | 2025-09-19 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4745d31-3054-3b0a-adba-5bcd03201e5d | -5.89497 | -45.85907 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d280e5d-f6ad-3a7d-97fe-92d22dead388 | -9.45329 | -48.92186 | 2025-09-19 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9109172d-48b2-33dc-8a98-641b47b10778 | -5.7733 | -43.90223 | 2025-09-19 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f8cd7bf2-b35b-33eb-9bf8-53332efd21ca | -10.29919 | -50.22364 | 2025-09-19 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4ba15f7a-531e-3f6d-ac90-0d88ffbd1abe | -7.87136 | -45.62798 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d74551f-e5fa-3f8c-8aa4-9248492e52b3 | -13.12255 | -41.05148 | 2025-09-19 04:46:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9f43726a-f65c-3cf0-b250-02e7269a6aa5 | -5.95801 | -47.09622 | 2025-09-19 04:46:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6a0cb6f-3d6c-3b7d-8716-b00ac0e2ab27 | -6.58009 | -45.58711 | 2025-09-19 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4f69cb7-4f0a-3090-bf20-573679d18397 | -7.92575 | -43.88825 | 2025-09-19 04:46:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d76cee78-61ab-3cc8-b455-0dc3632ef5c9 | -7.99256 | -43.93509 | 2025-09-19 04:46:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59209ddf-1e2e-3921-a132-1ca0709368b7 | -7.24588 | -48.33767 | 2025-09-19 04:46:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13328f30-6c78-3232-80fa-3a679b4608eb | -7.92514 | -43.89239 | 2025-09-19 04:46:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1326c230-b34a-3d84-a83a-148d2d4a8cdb | -9.02471 | -44.97058 | 2025-09-19 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a8a682c-0a39-30c5-8586-eec0a78a5d51 | -7.8544 | -45.62537 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6243ba64-4219-3acd-b7db-56592b9e0618 | -7.56995 | -45.46893 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c1631db-1c73-3e52-bfb8-f6073588da1f | -12.09239 | -44.84413 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24ac1f8c-155c-3489-b997-f802ae62c1f9 | -8.01554 | -45.73889 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f622c023-f0c3-34ea-90b0-f1cf63b601b4 | -9.17835 | -45.32219 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57f176bc-abef-31d0-b28e-3ec560f22c26 | -5.80334 | -45.36924 | 2025-09-19 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f36ec1e7-826d-3120-ac4d-a5999adcd673 | -12.24613 | -49.1641 | 2025-09-19 04:46:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1c334a7-4ad5-3e8f-881b-bb854bd44677 | -12.10074 | -44.81342 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79099ccf-8b23-3090-a17a-0ed38502acac | -8.04671 | -45.73179 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b69fe38-86c4-3607-b654-821d96fd1f41 | -5.80781 | -45.71582 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a3fe393-6606-347d-9203-ea6feb9d3032 | -6.91007 | -44.76911 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 05f3b0d3-270a-3074-8ec1-36b6018240df | -5.89436 | -45.72169 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bc7eb47-ffe8-356a-a61c-c6104d2b5a94 | -7.87019 | -45.63615 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75d6740d-e11d-3014-b814-9b3f3c5b4c35 | -7.35843 | -44.58618 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f5c8bc9-054a-3f40-81eb-46e0c3a7fde7 | -12.09679 | -44.80861 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ccd9baf-72ca-33fe-8570-6e85a74dee0e | -5.63241 | -45.94709 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7316365f-17a1-3241-ae74-2ef4b073de4e | -8.14563 | -46.78208 | 2025-09-19 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa780d8b-3013-3a21-9bdc-b07687903814 | -8.03258 | -45.70949 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52bb14e8-504a-33c1-94c4-1b4ac7053052 | -9.8667 | -46.43764 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 93beb52a-d330-362b-9414-5f771a158de8 | -10.28566 | -50.24433 | 2025-09-19 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b22bfc10-b27b-3ccc-8a8b-a8058bd4f3a9 | -7.86274 | -48.14507 | 2025-09-19 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9d1cc51-0dd8-3771-8598-cff8ae5fbca3 | -7.65475 | -45.13145 | 2025-09-19 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f447bb19-7a0a-325d-a6f3-52bdd9ee947e | -7.54028 | -44.79341 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01dd7974-f75f-3f9e-8e15-abc3f4044a74 | -6.19066 | -41.19893 | 2025-09-19 04:46:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1d33d9d8-2a38-364d-b2c7-9fedcb97dcc6 | -9.03744 | -44.87788 | 2025-09-19 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dedbe19b-26fd-3773-a254-8ce9e8cfe504 | -12.096 | -44.81252 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b40f972-0f31-31be-845b-4402bd67f801 | -10.24497 | -48.04118 | 2025-09-19 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ea869c32-4c32-371d-990e-dc890b9a27c9 | -5.86379 | -45.90199 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd992508-de96-3ff3-9b19-ba1ed73c72cc | -5.89091 | -45.85842 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62447981-1d4b-3435-af04-d5e7dcebc63c | -9.18639 | -45.29645 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 358e6c9d-bd46-31b0-baa9-5ec029f2c596 | -7.86962 | -45.64012 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d0bbc4b-5c2b-3145-9c17-ff5c6975209f | -6.93488 | -44.75427 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aae53da5-c21c-3569-9dc1-7bbe1fbd95ff | -11.18066 | -45.37256 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72c975d9-8988-3f4f-8a0f-9cf7b2f87d38 | -10.36723 | -42.46168 | 2025-09-19 04:46:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| baec9a4b-b984-34df-9313-edc84cb58c5b | -7.87503 | -45.63258 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README23.md)
