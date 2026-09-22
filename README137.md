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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01f3719e-169e-3b09-8bad-495b6f3ea1f7 | -3.2817 | -57.8685 | 2026-09-22 14:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 2bc6a756-eee6-3eae-b63f-db67adaffb43 | -10.8853 | -51.5347 | 2026-09-22 14:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| a101af66-c4c6-3040-8e46-d9b392b6efea | -10.11 | -46.0888 | 2026-09-22 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 2e33846d-903d-3dc8-9e0e-a27be38e0a66 | -2.9723 | -57.214 | 2026-09-22 14:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| ea5cf1b4-401c-3787-a490-78e37c43afbe | -7.9822 | -44.0879 | 2026-09-22 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 9a0013f1-fbab-3a63-a09c-fee8f07326ad | -3.3001 | -57.8487 | 2026-09-22 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| a0bd0add-1078-33bb-8827-00bca5cc879b | -4.2042 | -56.3412 | 2026-09-22 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| c7b9a103-1fd5-34c6-ae90-f1cda720745e | -12.2726 | -50.1441 | 2026-09-22 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 0c36fcb1-fb0a-3c75-aef7-3a582aaac38d | -9.859 | -46.4114 | 2026-09-22 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| fb187778-7627-3322-b0b3-d68ad82323e9 | -3.3183 | -57.8677 | 2026-09-22 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 3cc54612-a8da-3519-be47-7433998742ed | -5.9148 | -53.5372 | 2026-09-22 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| fec039d9-f69d-3a79-b343-a88733aa111b | -13.2033 | -51.7193 | 2026-09-22 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| a454b9e5-5864-31f9-a8d8-38cdcb523036 | -6.9174 | -41.6957 | 2026-09-22 14:20:00 | GOES-19 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 130.3 |
| 3f56ea82-14c3-31ba-87a8-f6285f9c76be | -12.3484 | -50.1779 | 2026-09-22 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 265.5 |
| 4ade4bbc-465a-3f04-9093-4d02d6f95112 | -12.3481 | -50.1994 | 2026-09-22 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 47834b83-3913-3748-a6b4-20a0afbc9b8b | -5.5846 | -45.5703 | 2026-09-22 14:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 0134407c-8091-31bb-a278-5734413535fc | -10.8848 | -50.1754 | 2026-09-22 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 22861cd4-2602-326f-b393-9220d9d72969 | -3.1901 | -57.8898 | 2026-09-22 14:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 460224ee-f2a2-3428-b122-c79e4cfb706b | -9.6298 | -43.9453 | 2026-09-22 14:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| 3edb2f5b-9752-3de0-b1a1-01bff4235b32 | -3.3492 | -59.867 | 2026-09-22 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| d095b533-22bd-34ff-a553-d43e40bb3836 | -8.6135 | -62.5171 | 2026-09-22 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 4a70f27e-c4e4-3efd-bdc9-2e3f6409279d | -3.2212 | -53.9422 | 2026-09-22 14:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| bcfeb26a-5ab2-3df5-b9d0-5b6b7124a62d | -6.7464 | -59.4223 | 2026-09-22 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 991b5606-5048-3bd9-93a5-2c136743fd61 | -3.7673 | -60.7339 | 2026-09-22 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 160.7 |
| 0ba0eadd-b921-30cb-aba9-fa6c9ce562b4 | -12.8053 | -54.0669 | 2026-09-22 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 9fd9d9d0-fb33-3270-99be-9a580c28b0a7 | -10.5748 | -46.7296 | 2026-09-22 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| a8935db2-232f-301e-b9f2-eccd48fc9dda | -5.4732 | -60.1767 | 2026-09-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 6fdb5acc-608c-3820-9d7a-a7375253877b | -13.9311 | -48.564 | 2026-09-22 14:20:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 7fef88a6-286d-38d8-9a97-8a4fedf32006 | -11.118 | -54.0268 | 2026-09-22 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| b38aebef-4872-3c17-a2c9-c27fc4dcd9c0 | -10.7626 | -50.8069 | 2026-09-22 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.5 |
| b6eaf537-6e7f-350d-8d51-829616dae9ec | -6.1836 | -47.5477 | 2026-09-22 14:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 12e588bb-f141-355a-b078-804bc8ab7cac | -3.2395 | -53.9618 | 2026-09-22 14:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 176.1 |
| 3eb23080-cdc6-3625-a4cc-0320262892f8 | -3.3493 | -59.8288 | 2026-09-22 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 8d3becd5-380c-30b8-b238-aac12eb70a2c | -8.7703 | -45.8793 | 2026-09-22 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| adbfca70-ec2b-3f95-99d7-e1f283acefd7 | -5.9333 | -53.5362 | 2026-09-22 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 8f9c92d9-4566-30af-842e-6cb42bf39329 | -3.4057 | -59.273 | 2026-09-22 14:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 92f9313e-5c01-32bc-b1cd-146e65b191db | -13.2671 | -51.3284 | 2026-09-22 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 78e11882-4343-3b9f-bd57-a79389550674 | -5.7875 | -43.7526 | 2026-09-22 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| f0c516c8-8487-33f0-8374-c92e4cd7176d | -13.2979 | -51.7926 | 2026-09-22 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 75ceb59a-baf5-35ef-900b-e40c1de74645 | -3.1851 | -59.6982 | 2026-09-22 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ffef0be6-e42a-3f89-9b10-72d202fe6f50 | -9.3797 | -48.3232 | 2026-09-22 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 4b09f779-fd85-36b0-a5f2-e85bd8d735f9 | -3.5146 | -59.5772 | 2026-09-22 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 5ed8bc72-275b-3961-8a54-5f8742b04da7 | -7.5247 | -46.2252 | 2026-09-22 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 023cec38-8a30-3eb4-afd7-fba9735a6870 | -5.8489 | -49.7875 | 2026-09-22 14:20:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| fab6be7a-ea67-32ee-8a7d-bae2c8e7f186 | -12.6799 | -50.9526 | 2026-09-22 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 9f6be5a3-ae20-30d5-ac2d-d18d2a07a056 | -11.3603 | -51.4009 | 2026-09-22 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| f37bf3f0-d652-39ee-a6c3-34e3252d36a7 | -6.0365 | -57.8235 | 2026-09-22 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 7b5c42f9-e422-3763-9a11-d1fc64a091dd | -7.1203 | -43.7323 | 2026-09-22 14:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 130.8 |
| d98347b4-9505-33dc-8c46-7ba93bac6b68 | -11.1563 | -51.0839 | 2026-09-22 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 261.6 |
| 2313e2d8-376f-3f92-8df8-742ec4b6a9f8 | -12.0836 | -50.0378 | 2026-09-22 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| c8384987-3187-3fe5-ae4b-c31ec3657b0c | -3.1901 | -57.8704 | 2026-09-22 14:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 2b9b7082-6663-3165-a3c9-20e64ddefccd | -4.2225 | -56.3406 | 2026-09-22 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 7cc5c7b3-0348-3b34-a2b2-78cce0ee1de4 | -6.7989 | -43.9008 | 2026-09-22 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 8bae11ab-45ab-39ba-8321-44c88f74b7db | -11.7076 | -51.0024 | 2026-09-22 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 6d817183-d29f-33d8-8a02-7e1d1f4f12b4 | -6.7963 | -47.8967 | 2026-09-22 14:20:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 2a368d01-9d2f-3261-9465-f6b39d51ebc2 | -7.0661 | -45.2521 | 2026-09-22 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 93c7865c-7e26-391e-87c2-5c2f62182296 | -8.7912 | -44.301 | 2026-09-22 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 60a87326-cc1e-355d-9688-d61ef40ae9a1 | -8.6136 | -62.4981 | 2026-09-22 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| bd9113b4-3e4a-39db-ae4a-dc4ef1d437bb | -8.6507 | -62.4966 | 2026-09-22 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 9a5cc4be-5718-3515-8fba-6020f01b2823 | -7.0352 | -44.6396 | 2026-09-22 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 57f31ee1-262a-3287-a4d5-e46a7768baa3 | -7.0763 | -44.3145 | 2026-09-22 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 182a0455-4613-346a-aca9-eb4df0cae673 | -8.6322 | -62.4974 | 2026-09-22 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 36673791-535c-38e2-8000-3b2545725dce | -12.2723 | -50.1657 | 2026-09-22 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 19b3c29b-6328-3b51-8161-adecb6c81334 | -6.3014 | -59.9579 | 2026-09-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 063fbf77-0134-3d6b-90fb-2f3bb7172963 | -6.3013 | -59.9771 | 2026-09-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 9670983c-fad5-365e-9133-f65ba90ecf75 | -3.2211 | -53.9623 | 2026-09-22 14:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c2c38143-d1a5-3e31-bf18-540fc05cac22 | -12.4004 | -47.0706 | 2026-09-22 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 13e18a2b-cea9-36c3-ab02-4763651522e1 | -3.8039 | -60.7521 | 2026-09-22 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 51dcf26d-0bc9-30ec-9ac5-2bf9e4feaa5c | -11.0991 | -54.0285 | 2026-09-22 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 7ec01325-a94c-3b14-aee9-8ff9a13b1b9a | -6.4486 | -59.9717 | 2026-09-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 36360564-faa2-375f-bde8-aa84981e64ab | -10.7437 | -50.8089 | 2026-09-22 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| fbcbe40d-6bb1-3c46-a2d4-23520e07da3d | -9.0286 | -44.9187 | 2026-09-22 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 43b502e0-34fc-39c4-8e26-5c5b1e3cd409 | -9.6111 | -43.9243 | 2026-09-22 14:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 278.6 |
| eefb0e01-9d0f-36ef-8cc6-e5d7e64f8367 | -7.9825 | -44.0647 | 2026-09-22 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 0b1729f0-af2d-30be-9c2e-281484922d19 | -8.4611 | -57.6292 | 2026-09-22 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 228b0c06-bd75-3fa2-a2e3-1eb4c0caaab5 | -9.2759 | -46.1852 | 2026-09-22 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 403.0 |
| 38083e0a-0ddf-3de0-bfa2-ea66d4fc7c30 | -10.5906 | -53.9918 | 2026-09-22 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| bd610134-719d-3356-b9a9-5ba8b520466c | -6.0926 | -57.6652 | 2026-09-22 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 6065c5a1-a7c2-39a1-860f-68ab8c832cd8 | -3.4049 | -59.5794 | 2026-09-22 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 501889f9-a4ec-36d9-a3c9-6296bde49042 | -11.3925 | -46.7598 | 2026-09-22 14:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 178.2 |
| d92abd17-c6b2-307b-8c57-a4e9e8457b72 | -3.6215 | -60.585 | 2026-09-22 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 46f6115c-eff0-3bac-9626-3df6292e5703 | -3.4598 | -59.5591 | 2026-09-22 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 98985469-bb5d-3f19-985e-60918f4ff21a | -10.0096 | -45.1915 | 2026-09-22 14:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 4979b1c3-3899-3ea2-99c7-9a758e01f134 | 3.7681 | -60.468 | 2026-09-22 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 6437b4b1-e0af-3157-a406-a7b384375aa8 | -5.7875 | -43.7526 | 2026-09-22 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 6bc46fdc-489f-357d-adde-8a772deb7a95 | -3.2899 | -42.6683 | 2026-09-22 14:30:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 8ea307ec-e6ed-3287-93f8-6578755d99e2 | -8.7703 | -45.8793 | 2026-09-22 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 77b158e8-4204-3b95-9be3-7f4234329cba | -6.3382 | -59.9566 | 2026-09-22 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 99b8af2b-81e0-30de-8df3-a22d1afe7d37 | -6.1651 | -47.5271 | 2026-09-22 14:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| b3a6f5d0-77ce-3fa5-896d-0952692c3b87 | -13.2979 | -51.7926 | 2026-09-22 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 6efc94b3-ce5f-3617-8095-5254c580cf6b | -6.1653 | -47.5052 | 2026-09-22 14:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| c3897006-3c91-3b0f-a2c4-3ae8ff1756df | -13.9311 | -48.564 | 2026-09-22 14:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 1c31b4d3-89ba-3e2f-9e2b-cd810e7402fd | -11.44 | -47.3579 | 2026-09-22 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| cb99f1d8-45f8-3807-9561-3e08998e26b0 | -6.7963 | -47.8967 | 2026-09-22 14:30:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| cdb4fa7e-128e-3c6c-81a9-d1de0e870665 | -10.5906 | -53.9918 | 2026-09-22 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 213ca0a6-138f-329d-a02b-195ee8efde4d | -6.1836 | -47.5477 | 2026-09-22 14:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| c2b76935-ab0f-3cf0-a684-27da21422f06 | -9.977 | -50.248 | 2026-09-22 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 8b83ffde-e3d7-3784-838d-181a53f603ad | -6.9762 | -52.8669 | 2026-09-22 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 6f3dcac4-b516-3a31-b85e-38e41bd2d871 | -12.1027 | -50.0355 | 2026-09-22 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 4694335a-c609-332b-8412-bb716a147dd0 | -6.2399 | -41.6394 | 2026-09-22 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 150.6 |


[Clique aqui para ver as próximas entradas](README138.md)
