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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c8a3121-daef-3215-a121-02cec45f2a59 | -9.21582 | -46.0567 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6abdb7e-ffac-361d-a9a5-2f07373f73ec | -5.18132 | -46.77023 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86310b91-3dd7-34c1-94c9-08a4a693a4d2 | -4.57255 | -50.16816 | 2025-10-19 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4854f30f-a958-312e-96ae-75ca317ade6b | -12.45947 | -45.43262 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c78a3e6d-8c63-3fb1-8176-22e4f00ee694 | -11.8948 | -45.43834 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6daa4937-c32c-31e8-83e5-ff9b7bf5bbc8 | -12.18659 | -45.10367 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e851c45d-d456-3322-81a1-0cec2f9971cb | -6.5575 | -45.94866 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b59ee60c-4e2f-3ba1-989c-319fb94a629e | -7.40542 | -44.81079 | 2025-10-19 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2efffc0f-4e01-3338-8fc5-ad562d1b798e | -8.44445 | -44.16832 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0821a19e-2827-3b55-9fa8-f2ba0329486e | -9.22908 | -46.06265 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4ca5bf8a-3eb4-3d13-902d-24b88636467b | -10.23496 | -44.89582 | 2025-10-19 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c9a6c9a-aede-36d8-8ba2-8016396c1b45 | -5.92377 | -45.44676 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 219d848c-3d4e-34c2-a332-9510b7416631 | -7.95819 | -48.12114 | 2025-10-19 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5889302c-2271-341e-99bf-728745e44eec | -10.9357 | -50.11293 | 2025-10-19 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b15b864a-e59e-3b89-abda-79c700b0a67d | -10.98539 | -47.94033 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8479714-0244-33ae-aad0-2eacaf045db7 | -9.67772 | -44.55486 | 2025-10-19 04:32:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbf64ba3-d90e-34ac-8821-bc5667a0a2a9 | -11.62699 | -44.07089 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 089e78d0-2642-30bd-a1bd-1327923b9148 | -12.45514 | -45.4365 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 85acabcf-4b16-3b97-9d0e-44482f922e80 | -12.69303 | -46.96047 | 2025-10-19 04:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb57d7cf-ccb1-3bef-bd10-0a26bd869d47 | -9.22306 | -61.83758 | 2025-10-19 04:32:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 640d3969-7632-3b95-b3d1-9ddbefff5d90 | -7.6299 | -48.39206 | 2025-10-19 04:32:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5186a7b-46e9-30ab-8ade-781cd84416aa | -5.31451 | -44.84721 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08fefbdd-6916-382e-ae8f-d3c2b670b5a7 | -5.72086 | -49.09575 | 2025-10-19 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2cda5798-8f60-3ec2-9367-d1dfc1b8d125 | -10.87853 | -47.46276 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a97a545f-c2fb-38f7-b74e-370111ec9f22 | -9.60248 | -49.02083 | 2025-10-19 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 624f603d-b458-38d7-80e7-f4827a9e7a0e | -12.01192 | -46.48358 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf87f06f-0e88-39e6-9c60-f09a6853879f | -12.45753 | -45.44595 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 012e6b66-eb9a-397b-bf62-f325864508c5 | -8.5982 | -45.4346 | 2025-10-19 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28d6ee13-4078-33b9-b0a5-04ff8d31a181 | -5.63781 | -44.81282 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 60ae946d-ed0a-3b61-9fd0-e7359885fcb0 | -5.71256 | -46.45532 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fc53e3b1-075b-3a5e-99cd-1c417b162c92 | -5.88637 | -43.92586 | 2025-10-19 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 065aff80-d927-35da-9a53-fdf82ea9742e | -7.12775 | -45.7446 | 2025-10-19 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28c74449-c8f8-3dda-95e9-92dfa97d6279 | -10.36475 | -47.47489 | 2025-10-19 04:32:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa828196-4045-3a12-a040-175821683ec3 | -9.21556 | -61.8357 | 2025-10-19 04:32:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dad6dab7-8906-30a9-a724-0aa91e94da7e | -6.23534 | -44.14233 | 2025-10-19 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4399b433-cb19-3180-bc63-ad50dd6fad71 | -5.30063 | -45.07915 | 2025-10-19 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1f30379d-b65f-36af-85c5-3430e4159375 | -7.15428 | -46.52916 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97965483-b6c7-326c-a65a-8c1e503905ef | -5.30772 | -45.0095 | 2025-10-19 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 506b78c9-1d79-314b-a98c-d8427910962c | -8.24605 | -43.99332 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33413829-9002-387e-ba0f-90b0c1b54689 | -6.31562 | -43.97781 | 2025-10-19 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0e249689-3576-33bf-9767-0dd1e85dcb6f | -5.31861 | -44.8439 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f5e7343-3da0-3bef-9a2f-9d14d16bba6c | -7.24627 | -49.51686 | 2025-10-19 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4be29387-1323-3b7f-ad41-56c677aec749 | -11.88064 | -45.45852 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88337e50-c373-3aaa-8df7-4c75aa8a1f72 | -6.35073 | -45.74389 | 2025-10-19 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dca5acf-f935-3127-83d6-b211d7596ef1 | -10.645 | -47.8795 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90c7e299-1031-3cc3-a2c1-d99d8c68862a | -4.9709 | -56.27365 | 2025-10-19 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9cceed0d-e6f5-35c6-ac55-9ae499d3289a | -9.54553 | -45.23846 | 2025-10-19 04:32:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ccc1f0c-f1ef-3e70-9cfe-1a83cfe66e8f | -8.44511 | -44.16372 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e35d2dde-3425-3774-b198-18a6758b2614 | -6.12725 | -44.21478 | 2025-10-19 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 073ea7cc-291b-3f3c-b3aa-324b0eb4055d | -12.15297 | -45.09813 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54a5b248-2d81-34ed-ac44-9e3355ef7853 | -6.60577 | -48.05785 | 2025-10-19 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4e37b21-6203-3cb9-813c-4c93547768ba | -7.41486 | -40.07541 | 2025-10-19 04:32:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b5c80746-a83b-39f9-b735-855586e61f30 | -4.45112 | -50.39685 | 2025-10-19 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6ef4e2f-6a3b-3267-a703-18996bc66f17 | -5.23343 | -50.95173 | 2025-10-19 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 205ced7d-b880-320e-9cee-66ce21aae10e | -9.98792 | -47.05552 | 2025-10-19 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cff36aa-2a63-367e-a1f7-c0e30f7a023a | -12.49413 | -46.93478 | 2025-10-19 04:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8375d2c7-cc05-3631-b824-783ac0a78d77 | -9.22274 | -46.05777 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14d1b000-54b4-3c0c-9062-031423f300de | -11.15757 | -43.4794 | 2025-10-19 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dcd52768-0be4-38f2-89be-2de2eecff2ba | -10.36754 | -47.479 | 2025-10-19 04:32:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 701f44d5-83a7-3f20-8403-cc2827b9aa38 | -5.89583 | -46.69651 | 2025-10-19 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12a9bbb6-613d-3104-a689-9e9a22ca805a | -6.35688 | -46.08957 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 708aadc2-9e5c-3b58-b492-a5cc940ac7dc | -11.45099 | -49.10584 | 2025-10-19 04:32:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b7f5531-d9a7-354d-9f2a-e2295e35b934 | -9.88938 | -47.65163 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05757341-2bb3-395c-bcfd-dbaa54ce07ee | -7.19279 | -42.21812 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 621150a8-643c-3686-b5f0-37f94a753398 | -13.20983 | -43.15366 | 2025-10-19 04:32:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d6579f33-9a47-35de-8da0-1beed34cc8eb | -5.88957 | -49.55529 | 2025-10-19 04:32:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 814b8aac-9754-33ab-9618-67b5ec8aa709 | -5.30004 | -45.08302 | 2025-10-19 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 19501fa8-cd56-3e94-b52b-0c86a317aaab | -4.64913 | -50.95654 | 2025-10-19 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acc960f9-0a23-31c7-bf7b-90a6e53b56d5 | -12.15363 | -45.09354 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 120904ab-787a-33ed-8fe4-51b2adab7f9a | -9.93541 | -47.66249 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57bde0ac-3417-3226-b701-526aab42bc59 | -10.95637 | -45.471 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47d888d6-2a4c-30c4-90fd-d19a2aca9904 | -7.30833 | -42.46942 | 2025-10-19 04:32:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f929d651-9a74-368e-8f00-3d2344faacbc | -5.26401 | -49.85148 | 2025-10-19 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1821b5f-c60b-350e-881b-17398c53335a | -7.61623 | -60.93112 | 2025-10-19 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 31a04385-2e62-31b4-8153-5f133566213f | -11.36295 | -49.25359 | 2025-10-19 04:32:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fedd7365-f66f-346c-bfae-57cd4722e5da | -5.15136 | -46.26817 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e35f367e-00cb-3b4c-a90b-4c1b83f3c36f | -8.8331 | -49.66298 | 2025-10-19 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54be65d0-2b6e-3ded-9cde-8b8b7846e0c7 | -6.85791 | -46.92863 | 2025-10-19 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6743b8fe-a7aa-30a4-af57-81194faa518f | -7.19335 | -42.21428 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b803a381-1ff2-3de5-9ffc-8998d348742f | -6.66938 | -49.83191 | 2025-10-19 04:32:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42a4d68c-d8d4-35bc-ada7-64615a268dfd | -12.33846 | -41.3909 | 2025-10-19 04:32:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 819d2d0b-81e8-3421-a030-9f7c2dab0415 | -6.12296 | -44.2184 | 2025-10-19 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 80855358-f8c1-392b-91c5-a6db99ad0cbe | -9.33346 | -46.11338 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79700541-2618-3ef3-a7b6-a5cadb81ef9e | -4.89758 | -48.60785 | 2025-10-19 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8b7b3ad-def9-3c94-942d-9fbbdab9d511 | -7.74183 | -42.51576 | 2025-10-19 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 31927857-ffe9-374e-9783-fb75f2d024ec | -11.40961 | -47.69669 | 2025-10-19 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 31462bf2-49bd-3d79-8a28-8bdb87b07fe9 | -7.84298 | -40.26386 | 2025-10-19 04:32:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4d8bfc03-5592-318f-b009-ec404cebb207 | -8.61375 | -40.19297 | 2025-10-19 04:32:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 29.1 |
| 204d001b-4c4b-3956-bcf6-83f6ca0dbcad | -12.0189 | -46.4847 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acebd650-a303-35fd-bab9-88533691c573 | -6.61159 | -44.22278 | 2025-10-19 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1d619505-3f4d-3a07-a480-9f79f6871090 | -7.18284 | -46.56663 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6ffdaef-33ba-3bcd-ba4e-9afeef04c419 | -5.86342 | -42.35273 | 2025-10-19 04:32:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 68512749-2887-3987-b933-ec7ab641518f | -5.40308 | -46.4149 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00248b22-f485-3c0e-9177-f036b8383c00 | -7.29127 | -47.84797 | 2025-10-19 04:32:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d75d3c2-36c8-305c-b9aa-5db104051729 | -7.16248 | -42.36563 | 2025-10-19 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f8364ab8-f97f-3ae6-b71a-c7f3e4b2c389 | -11.13276 | -45.0815 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 632a1865-022e-318a-9479-0b1561159f71 | -9.04744 | -49.51232 | 2025-10-19 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84cbae77-2ea6-39ea-92bd-2455baa5abc4 | -10.68915 | -47.94471 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d235a248-281e-3828-8732-078c0c68e6b1 | -9.93928 | -47.65951 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63ad1853-cd1f-35e4-bd31-595adf80c38d | -4.59263 | -50.76823 | 2025-10-19 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README44.md)
