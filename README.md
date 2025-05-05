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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc9c75c4-2eca-3fa7-adb7-66cfb697110f | -5.171 | -45.105202 | 2025-05-05 00:30:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9df8caf2-73af-33ed-a081-161f8e6c6ec8 | -13.0361 | -53.7244 | 2025-05-05 00:30:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0602de8-5bce-3098-bfe3-3f632431fc25 | -13.0458 | -53.7225 | 2025-05-05 00:30:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab2c07fe-2509-3b3e-a2a3-3edd93a062f0 | -13.0478 | -53.7048 | 2025-05-05 01:18:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fbfd81d7-e767-3299-b736-0f161cabbebf | -13.0429 | -53.725601 | 2025-05-05 01:18:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57ce290f-a83a-311b-9800-d3cdcd69cdfb | -13.0525 | -53.723 | 2025-05-05 01:18:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2275c83f-800d-3be6-9d32-575a2d7ea3d4 | -13.04859 | -53.74188 | 2025-05-05 01:30:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1aa12ee2-6f80-3eb1-b8e5-8430a8398d31 | -13.04561 | -53.72386 | 2025-05-05 01:30:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 4d5cf1e4-8e2e-3a1f-a84d-25ab73e9947b | -9.67683 | -37.88498 | 2025-05-05 03:21:00 | NOAA-20 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5ba5e85c-eb74-30f2-9f8a-188d4c8daff3 | -10.69497 | -37.0499 | 2025-05-05 03:21:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 797313a5-0284-30c6-9e36-a03b24270664 | -20.34704 | -40.36149 | 2025-05-05 03:25:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 82297fe5-3bf1-3ed0-93af-02c77c38f56b | -21.17893 | -43.98111 | 2025-05-05 03:25:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 785ae1f7-22a0-3e1c-abd9-7cc7ab9cf1fb | -6.5631 | -51.1126 | 2025-05-05 03:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| dd2060ee-f8e5-3329-b994-b8de393ba6c1 | -5.16572 | -45.10378 | 2025-05-05 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b249604-290b-3e97-b209-117b5defcbb5 | -6.4744 | -37.09862 | 2025-05-05 04:12:00 | NOAA-21 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 19438eda-1ed7-3500-91a5-eb754d0dbca3 | -5.16857 | -45.10818 | 2025-05-05 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6381705-529b-33c2-a515-2abc50acaf6f | -6.68895 | -35.24537 | 2025-05-05 04:12:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 54de63a0-4b9a-3230-9321-ea5ddf602c92 | -5.16226 | -45.10323 | 2025-05-05 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f95e4a5-f04d-3486-b28c-a6970dc276c2 | -7.55535 | -45.83656 | 2025-05-05 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bec6288d-daf3-3396-bf1f-2b43655c0b1e | -11.39569 | -52.94547 | 2025-05-05 04:14:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| da7e8fe3-ad54-34d7-b7aa-65944485f7c0 | -10.64309 | -44.4855 | 2025-05-05 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6f6e19a-3215-3e51-b237-35edd0a25bf1 | -8.12822 | -42.97047 | 2025-05-05 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 540b100a-89ed-3c2e-9c71-5fcfdef8c2d8 | -9.19274 | -45.34081 | 2025-05-05 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44dd4d2f-98a4-30cb-bf92-7df9e1cd7a05 | -9.18318 | -45.33549 | 2025-05-05 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1d4e452-53eb-3d60-bd1a-2051d14ebc5d | -9.18598 | -45.3397 | 2025-05-05 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c49ad7b4-6495-322d-b996-6e3bdc79d965 | -10.64695 | -44.48253 | 2025-05-05 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e863735-4599-3fda-a7d7-37682c23c7d2 | -6.30895 | -46.06211 | 2025-05-05 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e26e2ac-81f4-3ec1-95fc-e660fa0319e6 | -9.18259 | -45.33915 | 2025-05-05 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74997ba5-a4fe-3dfc-8647-b3d05049807c | -8.26667 | -49.30309 | 2025-05-05 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2176034c-f12e-33a2-9932-0eb5cba0e084 | -8.07678 | -34.97614 | 2025-05-05 04:14:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4bd454f1-1c0c-364e-8fba-566edda16105 | -7.60474 | -36.81659 | 2025-05-05 04:14:00 | NOAA-21 | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8ea93768-44c9-34e7-8b70-e1452e40b6f7 | -11.39511 | -52.94857 | 2025-05-05 04:14:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f526b43f-0369-3b7c-b446-c4412ca6ee42 | -9.65838 | -37.3257 | 2025-05-05 04:14:00 | NOAA-21 | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 18d174bf-9c23-31bc-a618-d789327d3659 | -8.26663 | -49.30321 | 2025-05-05 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb103e84-4039-3a44-a589-22160082c9f4 | -9.19215 | -45.34446 | 2025-05-05 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc2f9c0b-1af9-38b7-89b5-7d07bdf96814 | -6.30723 | -46.05872 | 2025-05-05 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bea6e72b-649d-3efa-82b0-c99c67f8aa43 | -19.51398 | -44.27829 | 2025-05-05 04:17:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fea66182-75b6-3721-8d6c-edfc6f498ece | -13.04891 | -53.72781 | 2025-05-05 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| efd5108d-b7e6-3b5a-badc-187154aa1392 | -20.31848 | -46.75178 | 2025-05-05 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7c8bd33-4c20-303d-bd51-4526e297be88 | -18.01219 | -49.39435 | 2025-05-05 04:17:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02831bfc-48fd-3bfe-b740-b8d45d15f054 | -17.00894 | -49.78168 | 2025-05-05 04:17:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dde9ec0e-49e5-397d-b68d-c68b9615b667 | -19.67856 | -45.37922 | 2025-05-05 04:17:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94b9973d-4b85-36af-9f0d-25c0c232c535 | -17.80396 | -44.3616 | 2025-05-05 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb65aaf9-8e32-3216-ac20-184dbb53ef15 | -19.97105 | -44.21756 | 2025-05-05 04:17:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 73655aad-02cb-351a-a9cd-19c23496ccb6 | -17.00875 | -49.77917 | 2025-05-05 04:17:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f370bbe-f33a-3e26-a1ac-c7f01534c77b | -13.05017 | -53.72133 | 2025-05-05 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ea7712f-08cb-3fd5-84f9-2b17712e9996 | -13.04624 | -53.7137 | 2025-05-05 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ccacdea-9e1c-36ee-8bed-652eb5a6a76e | -15.89182 | -43.45588 | 2025-05-05 04:17:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 30.0 |
| ce4a539f-6f03-365e-b4bf-a1af950ccc7a | -16.67977 | -43.88546 | 2025-05-05 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7bc7d655-61d8-317f-9b81-b08ad4de0196 | -25.19325 | -49.32841 | 2025-05-05 04:17:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5a5847c4-148f-31ef-968c-2460ebd007c4 | -15.07818 | -48.94507 | 2025-05-05 04:17:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ad0ce9c-d823-310b-8b29-b8876407802d | -13.04434 | -53.72342 | 2025-05-05 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a99b1a2-bf5e-3514-b07e-80383fcd4ddc | -23.40908 | -47.38985 | 2025-05-05 04:17:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ef5a4eff-c630-3ca1-bc75-7d23fd369c72 | -18.00853 | -49.3937 | 2025-05-05 04:17:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1555dfda-06c1-38dc-8e89-e2923143c459 | -18.94189 | -48.05699 | 2025-05-05 04:17:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7721cc48-bbc7-31ec-93b2-be33f1864f7b | -18.94183 | -48.0561 | 2025-05-05 04:17:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0b01a50-4b3e-304d-b6c7-2cf6b26c12f8 | -13.04686 | -53.71049 | 2025-05-05 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 292df515-67f0-3c3b-a7e6-0404a018ff48 | -13.04954 | -53.72457 | 2025-05-05 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2518356c-618c-337c-9f0d-0e909bb0251e | -15.88842 | -43.45533 | 2025-05-05 04:17:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d75a5e4-322c-353c-96b8-b1cbb932c363 | -13.04371 | -53.72667 | 2025-05-05 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 944d12ac-6712-394c-b57e-4add60a0fa97 | -20.31907 | -46.7481 | 2025-05-05 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05208f6d-fc8a-366d-abbf-bf63506ff0f8 | -13.71432 | -45.20308 | 2025-05-05 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35864db8-8389-34ae-b184-f921080b57d6 | -20.37831 | -45.60209 | 2025-05-05 04:17:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 272eb10c-48d4-303b-87a7-a61b81fa098e | -19.43879 | -44.34078 | 2025-05-05 04:17:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12948d5a-474b-341f-a276-94e26f9aa19e | -17.67516 | -42.74539 | 2025-05-05 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ffd80d5-1828-3a39-ac16-1c033d194e07 | -17.6787 | -42.74595 | 2025-05-05 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 106df6c5-f7d3-335f-b5c3-adbb43e9a27c | -15.08015 | -48.94327 | 2025-05-05 04:17:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfbbf48d-9a12-3c46-972d-980e1d723b22 | -15.57086 | -47.85685 | 2025-05-05 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 421f6316-3dd0-3d1b-bf64-fc4514cb9ed8 | -23.40617 | -46.55762 | 2025-05-05 04:17:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ffb39661-eeb2-3aa2-afcb-bd0bbaa526fb | -23.59518 | -47.43927 | 2025-05-05 04:17:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 65abfdb5-0ee3-3ce0-9cc0-4e950f5148db | -16.68314 | -43.88602 | 2025-05-05 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0715b1b1-1f5d-3800-9d31-5dd9f0422c0f | -17.58075 | -45.38351 | 2025-05-05 04:17:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad18cb67-e3b2-3166-82ca-c8a52df00992 | -23.63342 | -46.42662 | 2025-05-05 04:17:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 126713d5-fe4a-3eca-9b27-c5cab115851b | -20.02027 | -44.59743 | 2025-05-05 04:17:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7b9784e-1836-3968-835c-3fdb595fcdeb | -24.2443 | -50.73914 | 2025-05-05 04:17:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3b6852b7-f8fe-37a5-bbc9-27ff7c06810c | -20.99627 | -51.79393 | 2025-05-05 04:19:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5eee6c09-bd5c-339a-b919-cc50f979d515 | -22.54142 | -48.8133 | 2025-05-05 04:19:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34bfb3c2-05a4-36c6-ad7f-4d7c0d3acf51 | -26.11311 | -52.14989 | 2025-05-05 04:19:00 | NOAA-21 | MANGUEIRINHA | PARANÁ | Brasil | 4114401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5c2bb8de-43d1-31c2-b5ab-4f74bc14a719 | -20.76466 | -46.77063 | 2025-05-05 04:19:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 581dc469-2dd6-3943-9760-7e3ea87b1e1f | -22.85754 | -42.98298 | 2025-05-05 04:19:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 30b2e5c3-2266-332d-a61e-e15a7c989ec9 | -27.63612 | -48.90553 | 2025-05-05 04:19:00 | NOAA-21 | ÁGUAS MORNAS | SANTA CATARINA | Brasil | 4200606 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d85999c8-e5d8-3304-8b2a-f16fe01f3646 | -27.19872 | -51.44205 | 2025-05-05 04:19:00 | NOAA-21 | HERVAL D'OESTE | SANTA CATARINA | Brasil | 4206702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fc051fad-bc4b-3d9e-affe-c6fb34c3871b | -27.19703 | -51.44049 | 2025-05-05 04:19:00 | NOAA-21 | HERVAL D'OESTE | SANTA CATARINA | Brasil | 4206702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6b432800-07bf-3f03-a93a-91de8e048d01 | -21.29121 | -49.18239 | 2025-05-05 04:19:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 444b9371-be78-3372-924a-b1d631c827d6 | -5.167 | -45.10521 | 2025-05-05 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac496361-e38d-3632-a68c-dec14466e6c7 | -9.19211 | -45.3411 | 2025-05-05 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3e19dc9-b948-3765-bf16-7051fd7ffdae | -5.16845 | -45.10806 | 2025-05-05 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e9fad40-28f5-3616-9069-dbd264dfcb40 | -5.16534 | -45.10286 | 2025-05-05 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9613427-5c1d-3915-8729-fef782cf51a7 | -9.18415 | -45.33996 | 2025-05-05 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d4916d8-9a6c-3753-83b6-7b66e81d1c42 | -7.55739 | -45.83521 | 2025-05-05 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e7a9ba5-d6a1-3055-9ef1-513e407b786f | -17.57773 | -45.38408 | 2025-05-05 04:42:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6ada7fb-52ca-3c44-b2df-2e596d3c53dc | -13.04889 | -53.708 | 2025-05-05 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef8bd8c0-225d-32e3-9b9c-48adec3d5279 | -13.0497 | -53.72482 | 2025-05-05 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 903fe9c9-59f4-3821-b407-bb5de2d57fd7 | -15.07764 | -48.94254 | 2025-05-05 04:42:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfa8596b-f37c-354c-9580-2451d4f2b97a | -12.29316 | -55.29567 | 2025-05-05 04:42:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1f8b1e7-69ea-38ae-923c-ec0f7d749657 | -13.04821 | -53.71203 | 2025-05-05 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| adc48115-19ef-34be-9c65-7c1d831e1229 | -15.89161 | -43.45387 | 2025-05-05 04:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ff0530df-1498-3680-87df-d14348088f8a | -13.04262 | -53.72353 | 2025-05-05 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ea38a29-47f7-3842-b3bc-c4748b10a133 | -15.88596 | -43.45888 | 2025-05-05 04:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 837d2d16-5e3e-3d7f-9495-a7ee28a0f1ab | -13.04616 | -53.72417 | 2025-05-05 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README2.md)
