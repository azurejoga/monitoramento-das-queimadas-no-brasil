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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25160e46-4c96-3ea8-b738-1c9107d47226 | -14.3067 | -41.8364 | 2025-09-24 04:00:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 133.4 |
| c3a24345-7401-3fe6-956d-483904f6f0f8 | -3.4099 | -52.6805 | 2025-09-24 04:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| e76ed547-5bc8-3aa8-bf96-8947688ade9d | -7.37261 | -47.03237 | 2025-09-24 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| fb00d575-7a6e-3ec2-9fb4-07e36e9790f6 | -3.79762 | -47.588 | 2025-09-24 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2deccc7d-cb31-3155-901b-30074d03badd | -5.75544 | -42.61103 | 2025-09-24 04:00:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6cb8f444-db9e-3525-a7d5-b6b50b355f73 | -7.7818 | -46.19981 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e2e2e48b-d4e1-3ab3-989a-482f164f47a5 | -6.53233 | -44.22004 | 2025-09-24 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f7fd4c43-26f4-39f0-a855-2a7ee0bff72b | -6.41317 | -43.08635 | 2025-09-24 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| c0c1f704-bb24-3294-b48b-e09a5395401e | -6.94823 | -44.64346 | 2025-09-24 04:00:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cdce6b2-8d15-3af0-8344-2277424b23e1 | -5.7616 | -42.59547 | 2025-09-24 04:00:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7437cb46-0bff-3c53-b26b-99ec786f563c | -5.49125 | -39.17082 | 2025-09-24 04:00:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 257e0d27-1133-3ed8-aede-49542d34ca23 | -4.31396 | -48.09895 | 2025-09-24 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dd921664-a9dd-3abc-8524-b9aafeb433d4 | -4.4857 | -47.68319 | 2025-09-24 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4c7d975-9b72-3f7f-9234-70ad07b043c3 | -5.38682 | -42.2683 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e40a1746-2816-370f-ba6c-98fe09e08361 | -5.64813 | -43.61179 | 2025-09-24 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd306ab5-6bc8-37cc-b941-8255e70e422b | -7.91677 | -44.10787 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f2cd463-3bf6-38d4-bebd-3a8dd4e09ca7 | -8.16865 | -46.24217 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38ed12c3-f844-32c1-9d52-a9b8d5d3fe19 | -7.17829 | -42.24159 | 2025-09-24 04:00:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6a84af41-e2a3-32ff-ba52-7b92bd3ed951 | -6.42403 | -43.08808 | 2025-09-24 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 705aa31d-aa39-3aec-9a61-1d4c58c82c8b | -7.78251 | -46.19554 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a64d2034-05f3-360f-828a-a9ade4c11924 | -4.79949 | -42.75814 | 2025-09-24 04:00:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 132e5b31-032b-3857-a195-75f681e29f92 | -9.20703 | -43.13128 | 2025-09-24 04:00:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 11329609-7065-3e58-bdf1-5593cc1667d5 | -6.42334 | -43.0923 | 2025-09-24 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| fdcd2d39-8a45-359e-8699-b0a3f34fa615 | -4.74007 | -42.10115 | 2025-09-24 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4b1f1553-f9db-39e7-87d9-e6541becbe33 | -7.36644 | -47.04083 | 2025-09-24 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 82f11f02-e599-3cc8-9cbb-aa03f17cbbbd | -4.31552 | -48.08962 | 2025-09-24 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 66bcc4a6-7193-3a66-bbfb-6d0348b1e836 | -6.72777 | -42.73637 | 2025-09-24 04:00:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d8c258d3-e009-3976-ba12-cda81723465e | -5.37211 | -42.26999 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2f9c3748-50f2-3eb7-9a52-d68f2670dfe0 | -6.42765 | -43.08867 | 2025-09-24 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e69e3bdd-9926-3f7a-b0e7-6981767bac4f | -8.5476 | -44.96369 | 2025-09-24 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63f4f4ec-c37f-3e0c-b04c-6c828b46c976 | -7.2618 | -43.01237 | 2025-09-24 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ed8e9814-0c07-3bb7-8625-881d5bca1c52 | -6.11506 | -41.79208 | 2025-09-24 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 17228f09-d0ab-37b4-b312-0da9031f9c99 | -6.39494 | -42.26746 | 2025-09-24 04:00:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7c356ce7-d6b0-3395-9425-d85294ed971f | -3.51658 | -49.44617 | 2025-09-24 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a637d4ed-1a6a-3974-87ad-ab3d1745956e | -5.76515 | -42.59612 | 2025-09-24 04:00:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 91ee1a6a-d104-3c59-b507-140b6834b5e1 | -6.12954 | -44.43962 | 2025-09-24 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d17436e5-b1d9-30b2-ba76-e2a40f8593d4 | -7.3793 | -47.04813 | 2025-09-24 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cb065c0-1c47-3669-b03e-3b425d0e2971 | -5.49511 | -39.16787 | 2025-09-24 04:00:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 54f94be4-0e0d-304d-ae2d-8b86ff20f649 | -7.94786 | -44.11134 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab3234b6-0da1-3bb2-9e0a-524378c04724 | -6.907 | -45.67813 | 2025-09-24 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d93ef43a-ed59-3f4a-9ef2-fcdf93c04fe9 | -8.02897 | -42.40308 | 2025-09-24 04:00:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5443811a-b5e3-3462-a141-c092ce632d4c | -8.44266 | -44.82063 | 2025-09-24 04:00:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6ae86f1-3353-324b-8f6e-8ee0fd058838 | -7.94564 | -44.10166 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 27078e61-0746-37ee-97ea-1b0974c16be3 | -5.97194 | -44.12442 | 2025-09-24 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 49ace939-7cb2-3258-bedf-0dc69e687253 | -4.70505 | -46.47358 | 2025-09-24 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 201eb617-0024-3ab0-b940-28861f6d77e5 | -5.63609 | -45.72836 | 2025-09-24 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7d3a9bcf-ceb7-3e41-a283-902b8f863dd5 | -7.94342 | -44.092 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37581943-c091-3aa3-908c-f43489e0bdc8 | -4.30932 | -48.09492 | 2025-09-24 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 42b038f5-8d33-38fc-8c37-b33193a73841 | -4.80019 | -42.7539 | 2025-09-24 04:00:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5d4c82b-a1d6-338f-a1ec-07c1c4be1fa4 | -6.95213 | -44.64429 | 2025-09-24 04:00:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17eb1213-5a36-3303-a13e-1bdc533042ae | -5.47892 | -36.66754 | 2025-09-24 04:00:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 448b6fa5-23dc-3282-b1cb-ca23ae7ee57f | -6.20264 | -43.61311 | 2025-09-24 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 088ac419-3f11-3890-bf00-7045dfbd1a79 | -5.42605 | -41.32072 | 2025-09-24 04:00:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f93b5d97-73d9-37e0-9856-fa61cbcd2e25 | -5.73404 | -42.6078 | 2025-09-24 04:00:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5d53575b-1376-370a-8ff3-78766f9fc864 | -3.04999 | -46.92882 | 2025-09-24 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7ddc1cb-cbac-31b4-87a0-60d5b3af07e1 | -5.36329 | -47.21769 | 2025-09-24 04:00:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09e66a5b-8321-30e8-bc74-0177d19df618 | -7.28538 | -41.8632 | 2025-09-24 04:00:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aca70e5d-a054-3f44-87e6-a8c40104b078 | -7.17421 | -42.24485 | 2025-09-24 04:00:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d56ae71c-d8f3-30cd-aeed-62eb952f475f | -5.84761 | -42.64581 | 2025-09-24 04:00:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| d09d561b-f1a4-3689-9688-328dfa83398f | -5.59782 | -45.36355 | 2025-09-24 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7af726f9-ae47-3658-835a-8f840afa8952 | -5.15331 | -45.24742 | 2025-09-24 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b375fb77-2db6-3968-aaeb-e96e3d2132fa | -5.77562 | -41.76605 | 2025-09-24 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 367f0775-9263-3436-af2c-6cbfb154ce46 | -4.29151 | -48.26594 | 2025-09-24 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e20890c-f3d9-31df-95e2-ea63ad47f7d2 | -6.53149 | -44.2251 | 2025-09-24 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b7718ed9-033c-3722-a511-bd78ded28a89 | -7.19867 | -46.67854 | 2025-09-24 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c010f41-0f73-3340-9cdb-61b51c5aa6f6 | -5.30648 | -44.80978 | 2025-09-24 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e603bab0-c7b9-36be-a694-0f8ad9f9856f | -8.69104 | -44.02405 | 2025-09-24 04:00:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0deb2712-b903-3648-87cd-77385698702a | -5.7298 | -42.6114 | 2025-09-24 04:00:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 060326f0-fe25-360b-8b8a-edb6bc0e3994 | -9.20769 | -43.1273 | 2025-09-24 04:00:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 72f15f91-bdc7-3a59-876a-65f16c7321b0 | -7.77677 | -46.20343 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0362a652-a84c-3c65-8bf3-dfa7ccb25540 | -4.79155 | -43.53634 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 59d55089-a0c7-3305-afdd-2177406bafee | -8.79189 | -43.03268 | 2025-09-24 04:00:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f5256103-cd57-3d5e-89aa-e8956f2d576e | -6.41972 | -43.09171 | 2025-09-24 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 92645706-03b0-3428-88b6-e378182db08b | -5.61262 | -42.98743 | 2025-09-24 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8fdc4033-1567-337e-b6bb-75db66463faa | -3.2169 | -49.17579 | 2025-09-24 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ed7d172-baa0-32ef-8e55-43e862ee1cf3 | -7.7925 | -46.17877 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0586408f-67cf-300a-ad00-e0376b58818c | -4.98793 | -45.14552 | 2025-09-24 04:00:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3110b27e-33e0-30a4-93a0-73b94067532d | -4.7777 | -43.21518 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0f203de-e8db-358c-a34a-972aae882892 | -5.24255 | -43.71994 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 946cb6bb-2112-3278-a358-ee76d4095800 | -5.46848 | -44.68906 | 2025-09-24 04:00:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcb11012-4f33-332c-b971-8e057da899a8 | -6.14182 | -45.9692 | 2025-09-24 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c646c1d9-21c9-38ec-9df2-1e125f226be6 | -5.91654 | -43.93385 | 2025-09-24 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20ff27e6-ed30-3dfe-b21e-33d6a477d5a9 | -7.5045 | -43.67212 | 2025-09-24 04:00:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 923d9742-b2d4-325b-9917-cfa2820bbd44 | -6.35451 | -43.35215 | 2025-09-24 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8c5387c8-a9ba-3b4a-9984-c1fff794cff6 | -6.96751 | -38.54753 | 2025-09-24 04:00:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 87a38473-2957-38da-a90e-dc1d3b41b488 | -5.76095 | -42.59954 | 2025-09-24 04:00:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5b81135b-dd4a-346a-953e-ec8ac4374cff | -5.30985 | -45.32094 | 2025-09-24 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 609aa14b-2948-39c5-abc0-edd86d82e296 | -7.82259 | -47.8673 | 2025-09-24 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f919a953-6f37-3617-a6c3-f08eb150fc3f | -3.61146 | -47.53529 | 2025-09-24 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 890f2f3d-affc-39cb-bce2-f45d452078a7 | -5.58988 | -38.12667 | 2025-09-24 04:00:00 | NOAA-20 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 169db380-afdb-35ef-974b-fe67082748c9 | -5.68741 | -41.39845 | 2025-09-24 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dfb970c0-9344-30d5-831c-e858ed647468 | -8.78772 | -43.03604 | 2025-09-24 04:00:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3fe133e1-4826-36f5-9884-22d246ff9417 | -5.75609 | -42.56181 | 2025-09-24 04:00:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ca486a1b-796c-3ea3-98bb-9e3b13b25895 | -5.37879 | -42.25086 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6a296362-7b7e-318e-93a5-8222775d3b5d | -3.3911 | -47.50138 | 2025-09-24 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fff48320-5bd8-3f45-b105-a519677b7c0e | -5.92114 | -43.92977 | 2025-09-24 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c888002a-af08-3028-b149-76f4fe51cc81 | -5.38619 | -42.27225 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 393fa740-3e07-3b9f-94e2-fb3659cc4371 | -6.94482 | -39.7759 | 2025-09-24 04:00:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 56bfcf68-228e-3aca-ba73-6ac13ef3cd2d | -5.3218 | -42.74308 | 2025-09-24 04:00:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5ce5c705-15db-3423-a561-997f1a98f0aa | -5.91031 | -43.85896 | 2025-09-24 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README6.md)
