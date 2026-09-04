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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58ffaf2e-b4c0-3424-b976-96d0422c22df | 2.37831 | -50.76344 | 2026-09-04 04:36:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3df72f5f-78d8-37fe-811a-08665395b0c4 | 2.37753 | -50.75842 | 2026-09-04 04:36:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd42dd58-eeb9-3ef4-8da9-89fcdf59642d | -3.8981 | -52.04613 | 2026-09-04 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e4267d4b-3903-3b1d-8fe4-562870d53f2f | -2.32519 | -47.20169 | 2026-09-04 04:38:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7be61ae-6c24-3618-8c2f-56a0ec5e54ae | -5.91574 | -52.19034 | 2026-09-04 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75832cdf-50f1-39ce-ba61-465508f7da20 | -4.99335 | -50.43639 | 2026-09-04 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac9f3538-a1ca-3555-aa23-7394edeafe61 | -4.12264 | -48.93276 | 2026-09-04 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cdb6f70-92d9-3018-8031-964311847ca6 | -4.31128 | -46.77781 | 2026-09-04 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f279e028-d7fd-3bf0-b4c2-81846dce3013 | -4.36664 | -46.7076 | 2026-09-04 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e244e220-731f-31a5-b272-2995a6984a4f | -3.19336 | -48.79779 | 2026-09-04 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 859733c3-7939-3ed5-98af-5e20ac9fce02 | -7.59541 | -44.74786 | 2026-09-04 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6274065c-8126-30b7-b849-84408d8386f9 | -6.11487 | -44.67991 | 2026-09-04 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1222241c-e100-3c82-bf5f-01c0ff92ec24 | -4.11122 | -51.03023 | 2026-09-04 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f93e1d8d-848f-3073-b529-d55ba4fd8fc4 | -1.24656 | -54.53334 | 2026-09-04 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b2c42030-310b-3589-ab5a-243e9806c108 | -4.30795 | -46.7773 | 2026-09-04 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97d4eb97-5bc9-3680-a1e5-6a0de84618d5 | -6.30656 | -46.08844 | 2026-09-04 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5acdb77e-8de6-3bf7-9fea-87b3507fdae9 | -3.24444 | -47.25529 | 2026-09-04 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91a0f5af-c8ab-3057-870f-486939a35340 | -2.32628 | -47.19482 | 2026-09-04 04:38:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1cfe4657-e7a6-3f46-9e44-6afef2c1e913 | -6.35546 | -46.11071 | 2026-09-04 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3cd87fd-ee30-39bc-b87f-3d1bdc486b60 | -1.02057 | -53.72334 | 2026-09-04 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1230488-ae94-32c9-be6d-77334d15ed7c | -2.76012 | -49.47458 | 2026-09-04 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5f300eaf-a392-3d24-bf98-e644ba66c6f0 | -3.20136 | -48.72559 | 2026-09-04 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62574297-196b-3d1e-b261-a7b872b9f7ad | -3.77178 | -47.54993 | 2026-09-04 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e5c3162-c6e9-3c88-90bd-6b18945fa439 | -3.59413 | -49.86098 | 2026-09-04 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a771aa9-9081-348b-a2a0-f635043be807 | -3.12046 | -51.73735 | 2026-09-04 04:38:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7d355f69-f29e-3023-b911-a058fcf772ef | -4.36474 | -47.77454 | 2026-09-04 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f97649e0-03c7-30a4-b6b6-12a51f85e229 | -4.47961 | -55.07911 | 2026-09-04 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 85006ec8-d7ad-3431-8a06-da04cd3371c2 | -4.99399 | -50.43243 | 2026-09-04 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f4b729e-fe77-32b6-a87c-61905b495f80 | -1.03622 | -47.5531 | 2026-09-04 04:38:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f984f0de-c338-390b-bdce-fa380ee6be08 | -3.22012 | -48.81321 | 2026-09-04 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a6a6840-521c-35be-af04-672708dcc8be | -4.34678 | -44.33906 | 2026-09-04 04:38:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b1a4f70-449b-3b78-81ad-8e4e64f1ebb3 | -3.43016 | -43.20614 | 2026-09-04 04:38:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2702d43e-541f-353c-8f18-5e398d9f1630 | -1.02046 | -53.72424 | 2026-09-04 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cef4ffbc-7aa9-303e-a958-ca71f5053e4d | -3.24498 | -47.25185 | 2026-09-04 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 11f78afe-2bb4-3fa0-af37-7068ec65081a | -3.18941 | -48.80085 | 2026-09-04 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71bbc19b-f7f8-3ec0-8da0-84549acd5df2 | -6.82371 | -41.67527 | 2026-09-04 04:38:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ec0a686e-e320-3596-91cc-9bab5c127e35 | -5.38151 | -42.85822 | 2026-09-04 04:38:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a5693d44-b328-33d5-8581-a574cfd18a75 | -4.24889 | -46.63561 | 2026-09-04 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9db62cd6-2988-3db8-9a9b-219bc7ab9b53 | -4.96902 | -55.85424 | 2026-09-04 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5512683d-b893-37ef-a30b-dc6dbd06f092 | -5.38707 | -54.44839 | 2026-09-04 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 56d5a150-b191-3cf1-b4b7-e0179364a19b | -6.31341 | -46.08951 | 2026-09-04 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a5816061-04d2-3fe5-982b-fd91abe91671 | -6.82817 | -41.67583 | 2026-09-04 04:38:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 153d22e5-a504-3673-a3d0-a4dc8a29537c | -6.94215 | -45.19384 | 2026-09-04 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc546a6e-81fe-3ed7-81e7-62c5e0cfde77 | -3.07488 | -61.09039 | 2026-09-04 04:38:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2712fbcb-41c4-3ffd-97fd-2be5f1453321 | -1.09217 | -48.05653 | 2026-09-04 04:38:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dabb7967-3c25-375b-bb44-b5cda542bdc5 | -4.9141 | -40.66515 | 2026-09-04 04:38:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e7db0565-fafc-37c2-8da6-364fb70b49e1 | -5.96688 | -46.67749 | 2026-09-04 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f65f7f7b-0123-3ead-8beb-2e65ae631c9d | -3.24595 | -47.90861 | 2026-09-04 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f281bb48-cc55-3260-8b4c-194eb78b23fc | -2.82888 | -48.64862 | 2026-09-04 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fa37bdb-59a1-3eab-9dd7-aeed77f94b32 | -5.80004 | -43.64843 | 2026-09-04 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e383bc65-c73e-3b3c-bf08-d3270fe26459 | -3.49994 | -49.72835 | 2026-09-04 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e51ab421-c2cd-3a6c-80a9-e7e3f3448d8b | -2.75952 | -49.47838 | 2026-09-04 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 595a9d8c-aa85-3819-8a5b-4c48856a883d | -3.98861 | -47.2528 | 2026-09-04 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8eb5da8b-9f36-37b6-85b3-0ccbab0058bc | -7.12187 | -42.25017 | 2026-09-04 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 27be9db5-fee7-3fd5-bb85-4a2c87c319a1 | -5.20997 | -38.03172 | 2026-09-04 04:38:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f82edcd3-c3ac-3f90-816e-fcabd16e8563 | -1.0341 | -53.72689 | 2026-09-04 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d77fd4a-5f60-3597-9327-f7bc548a2fe4 | -5.55141 | -43.43207 | 2026-09-04 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ce8c951-a33f-3526-9cc0-d9817998d8c7 | -4.14536 | -51.076 | 2026-09-04 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8309f5c3-6fc9-3eeb-bb3f-374e4fc094b8 | -7.11759 | -42.24949 | 2026-09-04 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 9f16c556-01d6-333e-8487-3029592be774 | -3.28998 | -57.88678 | 2026-09-04 04:38:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f23d66b-3573-342a-89b5-0de1a308b972 | -4.14845 | -51.07518 | 2026-09-04 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36bc4688-d3a2-37bd-988a-c4fef96901e8 | -4.62913 | -55.73393 | 2026-09-04 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f89fb89-9ecb-3e91-880d-8e065da598f7 | -4.96803 | -55.85994 | 2026-09-04 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 178fe8f7-c0ce-3bbd-90b4-9a016f7a419f | -6.14533 | -57.75961 | 2026-09-04 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ed500ab-6d50-33ce-b9eb-ea314ba83e8d | -7.35223 | -45.4709 | 2026-09-04 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b10f1332-e21d-3768-8c2c-8f0faf2f78a9 | -4.55348 | -47.76228 | 2026-09-04 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd67eb3d-cc4e-3c4a-be06-36f3f4c0919e | -4.34583 | -44.34 | 2026-09-04 04:38:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 712192d5-ebde-30b4-9496-9f992a309a73 | -0.93016 | -47.19341 | 2026-09-04 04:38:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4c19c5b3-eac5-34a6-86ea-fe3a953000a2 | -3.61207 | -60.56945 | 2026-09-04 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 052259c7-8907-3cfa-8ea4-3485c55c97e1 | -3.23015 | -50.57155 | 2026-09-04 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6e7d354-959c-3c47-943e-7b70d52fc28a | -3.61749 | -60.5747 | 2026-09-04 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 470848d8-62a7-380c-83a3-00da0d29e026 | -2.6179 | -48.27035 | 2026-09-04 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b1516b9-5e4f-352e-86ae-4985788b4f69 | -3.23082 | -50.56736 | 2026-09-04 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dcd06f2-8f07-3a20-8541-0115859025ac | -3.33771 | -39.77276 | 2026-09-04 04:38:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f41bcdf9-bf9d-3ae3-99b8-40f98a591ec4 | -4.11193 | -51.02589 | 2026-09-04 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41675d72-feb2-3944-95c8-04b8621b3279 | -5.8983 | -52.1049 | 2026-09-04 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13632263-bfb2-3f89-9c8c-033761c7c536 | -3.24167 | -47.25133 | 2026-09-04 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 41a5a8d9-8d8f-388e-a5fe-f4ce59a46b85 | -4.90308 | -43.47337 | 2026-09-04 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 956b71e2-ac27-3432-b8ae-0966b44ffae3 | -3.40615 | -50.12576 | 2026-09-04 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dbc290c-b46d-3fba-ad37-3e9df2c0a90e | -2.94027 | -48.73946 | 2026-09-04 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b31648f1-e1ad-3aac-b6aa-5e58aa3f9aed | -6.07222 | -49.48416 | 2026-09-04 04:38:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f22c14f3-700d-3a4a-8022-e1d93459bc45 | -1.74171 | -54.99107 | 2026-09-04 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 09c0473d-b9b4-3ae8-b465-e6c878e9db2a | -1.54972 | -53.10097 | 2026-09-04 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e585e42-ac75-30ba-aadb-087fa44e73e4 | -4.4835 | -55.08492 | 2026-09-04 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 483b4135-7517-3f70-9b93-c775eb1feaf3 | -4.3675 | -47.77851 | 2026-09-04 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1cfbc5b2-18b9-360e-bcf3-a55fd42c96d9 | -4.36805 | -47.77506 | 2026-09-04 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9a96554d-897c-336b-8bb9-c96414c5d3d0 | -6.30998 | -46.08897 | 2026-09-04 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c4e3fd7c-f40c-3060-9e98-f40deb6923d5 | -6.11356 | -44.68845 | 2026-09-04 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5de6828-32b6-3b47-82d7-bea1ecadea48 | -5.29798 | -43.06403 | 2026-09-04 04:38:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb3ddc8e-f5dc-396f-89d5-e55a33e4d469 | -3.77483 | -51.36162 | 2026-09-04 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6b81244-09c8-3a40-9acc-5cc55c00a1cb | -1.55052 | -53.10273 | 2026-09-04 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78622a40-6b33-33b4-ad52-4c75ef322db9 | -4.14903 | -51.07671 | 2026-09-04 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3115b868-d911-3921-8d93-0d39d039a2ba | -5.97024 | -46.67799 | 2026-09-04 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31ab9c7a-921b-3953-88c6-bd84db4b8ea2 | -4.35303 | -55.03986 | 2026-09-04 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0683a964-5580-34af-ac12-be98d0d64466 | -6.15671 | -57.76443 | 2026-09-04 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ab9a052-abe1-3a8e-bf43-6b3ef5004a14 | -4.73785 | -48.035 | 2026-09-04 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6725b922-0772-37c0-8126-dd591178c0c9 | -4.57758 | -45.67318 | 2026-09-04 04:38:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41e9f48c-a570-31fb-ba7d-d7b3d2a16136 | -5.5465 | -45.19992 | 2026-09-04 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3445bc40-de8a-3392-b38a-a5f01aa4ee72 | -5.2994 | -43.06326 | 2026-09-04 04:38:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edb7415b-7f41-3e60-833f-9f11336bb31a | -6.15734 | -57.76083 | 2026-09-04 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README16.md)
