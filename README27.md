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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f6e0c66-0031-3282-a830-f9d3fd6c5199 | -6.54899 | -43.84456 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 471c5a9a-4ece-35dc-b8c5-a8538703b6ba | -5.47992 | -43.07048 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95cd1e28-6193-3a3a-b3af-61e39dcf6278 | -5.80789 | -43.8306 | 2025-09-27 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d63267f9-14ab-3941-9606-9d680252d657 | -4.37544 | -48.20864 | 2025-09-27 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ac7ac99-1d32-3252-bd32-6f9c0b4f7ce3 | -5.48841 | -43.08289 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3d83a03-a6dc-3f30-b367-39ae45444ebb | -6.60605 | -42.93709 | 2025-09-27 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 550454be-82b7-3fcc-bac8-ec304734fa9e | -5.09143 | -40.23671 | 2025-09-27 04:21:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dc7e917c-9c06-3728-b225-3a08fa8035bc | -5.49234 | -43.05757 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 626c9904-c710-3d40-b60f-fdd28dfcfc56 | -7.60195 | -43.05964 | 2025-09-27 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f65af59f-5462-353d-a3af-76c658034726 | -3.35836 | -43.37706 | 2025-09-27 04:21:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a07bfc2-bc66-3f2a-9773-b93d0c43f415 | -5.67455 | -44.85001 | 2025-09-27 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a4c5f68-4c0b-3850-b06c-4da45d3bf6c2 | -6.80946 | -44.47397 | 2025-09-27 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e4688e7-fa12-3206-9e6e-64ebd816edea | -5.79393 | -42.82307 | 2025-09-27 04:21:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e356980d-88d4-392a-8d1f-0f561a82ff42 | -7.04764 | -43.0374 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 63a03927-9e42-3625-9289-bdeefc0e13b7 | -5.07828 | -44.85203 | 2025-09-27 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e84a7465-70e7-3efd-ad0d-c6f73f642ccd | -5.74072 | -44.985 | 2025-09-27 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 65ab7c44-4fea-3650-8a23-cc94f2c98ff6 | -5.0901 | -47.47931 | 2025-09-27 04:21:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba646126-2076-36ae-8a77-61f747aa7bd0 | -5.05281 | -42.90165 | 2025-09-27 04:21:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f7de77c-6dd0-3d07-adb7-3980a1d63029 | -7.62639 | -43.84815 | 2025-09-27 04:21:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05b7f4e5-ccae-32f6-a42f-ec1ed4027fc3 | -4.88074 | -38.90153 | 2025-09-27 04:21:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8c827a35-43c2-37bb-b6ab-cb500672732e | -6.60663 | -42.93336 | 2025-09-27 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9694eb8f-bee2-3f8e-aa0a-afca542552e5 | -6.49316 | -43.28045 | 2025-09-27 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d8497a5-0a58-36b7-a5a7-643b9878fe75 | -4.74336 | -43.6115 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81ec1d03-3d99-356e-bedf-64a9eae81637 | -6.70579 | -42.73734 | 2025-09-27 04:21:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| da077ded-a118-3bf5-bcb1-e7d013095037 | -5.82144 | -41.29728 | 2025-09-27 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0804c8d6-4648-3f90-8816-26788246eb7d | -7.61624 | -43.82458 | 2025-09-27 04:21:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 38880a12-f911-3c4e-9354-660ef6802526 | -6.31905 | -43.46025 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8871e33c-3d37-3d79-b711-7c794a770538 | -7.04861 | -46.41476 | 2025-09-27 04:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 301ee056-c9a7-30cb-be4e-8548086bf35b | -6.42103 | -43.07157 | 2025-09-27 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a681fe84-8bb8-36d8-85b4-a771c1fd0f9b | -6.31334 | -43.3858 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0371d649-d35a-3ae1-b5ef-7e09cae58f54 | -6.68589 | -43.11861 | 2025-09-27 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b5b54ed-52b9-355c-a2ac-ddef050d8ff2 | -4.53263 | -48.64569 | 2025-09-27 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7943b8fb-4671-3b90-92ac-aa68347d0fcc | -7.35009 | -42.09685 | 2025-09-27 04:21:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 681e9057-8561-3b2b-92ae-d7b1afdfaf11 | -5.73794 | -44.98098 | 2025-09-27 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8643c33-b923-3ef7-a8c1-c82e8e2e4d66 | -6.89805 | -44.16171 | 2025-09-27 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e923cbdd-a38b-3193-84bc-d3c5a06e48c9 | -4.33381 | -48.39294 | 2025-09-27 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96ffecff-a73d-36c5-a30e-8e02fd2ea896 | -6.92791 | -44.64566 | 2025-09-27 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aae80b10-47f6-3fb7-932f-75316c97ecd7 | -7.63962 | -40.15913 | 2025-09-27 04:21:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1884ad1a-b8bc-305d-b80b-eb0e78d6cb13 | -3.83013 | -40.33788 | 2025-09-27 04:21:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fdb71f59-3549-3fe3-a9c1-90cab2b7d7ee | -5.47768 | -43.08492 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0c466df-7e31-34bb-8608-56f3b66a7ddd | -6.7863 | -44.8586 | 2025-09-27 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 694600f4-edea-3d12-b27e-a7c4aaab8d03 | -7.00382 | -44.7005 | 2025-09-27 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 850b16a9-f85a-3e99-a0c8-78d25e13b61d | -6.58596 | -44.43188 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa103a41-ba8b-375f-b164-d194288cbdda | -7.11641 | -42.1913 | 2025-09-27 04:21:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2752a329-e56c-3117-8f5b-bcdd931a85f5 | -5.9429 | -44.88141 | 2025-09-27 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2125112a-e737-3252-a693-7d1492d0ad22 | -5.49178 | -43.0612 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22fd12bd-6433-31f8-b98b-1870362a17f4 | -7.28027 | -42.97673 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 00fda69b-b6d9-3c9e-96aa-15c7eb96ff7a | -5.19267 | -43.72379 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbb72725-09b2-35a0-b80f-af042bd4727c | -4.97094 | -43.19848 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e1c4fa8-38ea-3444-9977-ed426cde226c | -5.47597 | -43.07358 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef92c180-4e14-3ca1-9fc7-71f01463fbe8 | -4.53183 | -48.65064 | 2025-09-27 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d9c99aa3-3bd2-3053-ac8c-0b4350180b1b | -6.99645 | -42.38813 | 2025-09-27 04:21:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1ada3043-7d4c-35d9-9871-812cbaca064e | -6.53668 | -43.83539 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b0de179-2416-30d1-9e49-0eab62c32617 | -6.22584 | -44.18629 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37b0dd41-cb1a-36f7-901a-aff954a7069b | -7.15714 | -45.52164 | 2025-09-27 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb68c277-94d2-346a-bfc9-4799be3961a0 | -4.97902 | -42.7229 | 2025-09-27 04:21:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b386f7c-ad8c-3dfd-8aa6-e084996dbe59 | -5.24004 | -43.08896 | 2025-09-27 04:21:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed4831bb-94dd-3098-97f2-83f38e5d4a87 | -6.62802 | -42.04121 | 2025-09-27 04:21:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b61c5025-b890-333c-bec1-01767dd0e5a6 | -4.00299 | -46.96189 | 2025-09-27 04:21:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f99fc479-82ca-3178-b799-78b1b63ab22a | -7.28371 | -42.97727 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b6ced238-9c03-36a3-99e8-53286b64113a | -4.16737 | -44.26788 | 2025-09-27 04:21:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8049cccf-ff96-3810-9a62-27fea4c55041 | -4.70161 | -46.45778 | 2025-09-27 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f632eebe-8b56-311f-bdb3-bf256a2f4b9d | -7.05279 | -43.02682 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b1c0f051-42e2-3381-8464-70e66ca855f9 | -5.50297 | -42.19489 | 2025-09-27 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f6adf9ef-d92b-3f02-a57a-649ef016a8e0 | -6.25181 | -42.47713 | 2025-09-27 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 76de75a5-a773-3d88-a188-0e58c9bcf8fe | -4.07098 | -48.04014 | 2025-09-27 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2de3eca1-53c8-38d8-9827-1dafcecf9723 | -5.08742 | -43.05875 | 2025-09-27 04:21:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 77619f7d-82f8-300d-b520-afcb1bbdb9aa | -3.64874 | -43.11062 | 2025-09-27 04:21:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef310817-f991-3338-8d43-2f268bb347ac | -5.94235 | -44.88488 | 2025-09-27 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e33ad0a9-3e02-3007-9b05-db06a2a07378 | -6.79893 | -41.74988 | 2025-09-27 04:21:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e38e5317-369b-3370-abeb-4d7ef279e2a2 | -3.33448 | -50.2476 | 2025-09-27 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a751549a-301c-3559-942b-348bd3f5d2b0 | -4.40218 | -44.08514 | 2025-09-27 04:21:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 31ffcd31-220a-3bd2-9f14-4a9b2902cde3 | -5.80828 | -44.88168 | 2025-09-27 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ca2a9e3-9032-3c18-b49d-a00abb908e98 | -6.33471 | -43.35974 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3811d2c3-7437-3788-95fe-692f80678227 | -5.4867 | -43.07153 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8aace866-6ae8-3ad7-bcf8-7e8133244c41 | -2.85296 | -49.48932 | 2025-09-27 04:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb906bd9-9283-3930-a364-dff3051c332a | -4.70445 | -40.62513 | 2025-09-27 04:21:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8f8371b4-6e7d-3039-906d-11bee8e7b843 | -4.48425 | -47.67482 | 2025-09-27 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ea12e8e-21b4-3802-b445-243fff5029c1 | -5.47996 | -43.09264 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfca81f6-5f3c-3d92-afc4-84a604d2437a | -5.85772 | -47.26906 | 2025-09-27 04:21:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef7d7e6d-a0a6-36a1-bf43-279788ce5240 | -5.86425 | -47.2691 | 2025-09-27 04:21:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5725941e-ab70-3c95-ba0f-198b7704fa00 | -6.32348 | -43.38737 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00aadc58-a7f7-3d67-8719-83477554af10 | -4.38525 | -41.92575 | 2025-09-27 04:21:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 306dac9b-1e83-3b30-b7aa-15b48855bbc7 | -2.26525 | -47.85706 | 2025-09-27 04:21:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07c71e9f-d412-35c7-a93e-89dcb2a11f7d | -6.99294 | -42.38759 | 2025-09-27 04:21:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| db44b2d7-0c73-3a79-87d2-6289ef7c579f | -5.40438 | -42.27424 | 2025-09-27 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8306e6a4-876f-3980-a68e-2adb8fb72c56 | -7.00019 | -46.99099 | 2025-09-27 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbf0b7ea-c9b6-386e-acdd-9f20648187e9 | -5.80653 | -42.44625 | 2025-09-27 04:21:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cbca2648-3721-39ab-8871-23f8c20ff0a9 | -5.72461 | -42.29791 | 2025-09-27 04:21:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a9c8b3e6-7cac-34b2-b964-8aea45fcb14d | -5.73682 | -44.96653 | 2025-09-27 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58044bd8-0c6f-39f3-84f4-d4b25d78e3a8 | -6.22281 | -47.3285 | 2025-09-27 04:21:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 81a0fcdd-d71a-3807-b656-974b7ec0f111 | 0.60043 | -51.57876 | 2025-09-27 04:21:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b69576f8-0f5a-308a-84ee-6d5736a16dcb | -4.68024 | -46.44712 | 2025-09-27 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2b96656-0934-3470-a862-f75cafe160a3 | -5.53585 | -42.73146 | 2025-09-27 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ae3e38e3-1c30-354f-af78-daa0d70ace69 | -6.26681 | -42.49521 | 2025-09-27 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3dcdb980-47c0-3992-a486-0591e754d60a | -6.21154 | -42.85136 | 2025-09-27 04:21:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 927f725f-5031-321b-add3-2e9db7991277 | -4.70836 | -40.42292 | 2025-09-27 04:21:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| c743f487-a2f1-3f9f-acf5-50575d5ed5f7 | -6.81334 | -44.47101 | 2025-09-27 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a9b603f-17cf-32ad-96be-b707398d2350 | -5.38406 | -42.29065 | 2025-09-27 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d4a5e52f-80d2-3daf-b500-44446a58de35 | -6.52663 | -43.83378 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README28.md)
