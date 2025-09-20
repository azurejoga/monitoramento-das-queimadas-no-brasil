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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7759ecce-65de-3543-abb2-c42b7653d45a | -6.11969 | -47.81263 | 2025-09-20 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b08d45a-99f7-301b-9e6d-58a980e6093b | -3.29444 | -52.58068 | 2025-09-20 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c8cd536-097d-3f6a-a97d-9de703498862 | -3.51322 | -49.44717 | 2025-09-20 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 52db72ed-24f5-389f-adce-8f7953b9d63d | -6.23001 | -47.31325 | 2025-09-20 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b1078d2-55f3-3853-a784-2e8778d5f8ae | -6.09266 | -42.82397 | 2025-09-20 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8c1d87f7-a094-3995-946e-1c4580ea9ce1 | -5.83991 | -46.28909 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53e96151-81a2-3fa0-a358-446f35d04b82 | -7.8369 | -45.63103 | 2025-09-20 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5818be8-8ab4-36db-9899-b4a4338d869c | -5.82779 | -46.28015 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 243d0d51-5c8b-30cc-99a8-e57337c68b27 | -7.11376 | -47.85656 | 2025-09-20 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 592bb3b8-5671-3e21-9871-37c35a900411 | -8.89462 | -40.43981 | 2025-09-20 04:25:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d18a76dc-abe5-3b62-b0c1-7a155ce372bd | -7.18799 | -42.23626 | 2025-09-20 04:25:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8cfbd5c8-b489-31ec-bfd1-8de67780242a | -5.7934 | -43.64869 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 945a1762-4e90-3937-a6fa-81316c095e84 | -5.55511 | -42.20662 | 2025-09-20 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0cae270e-9f5e-3bb2-ae68-4c23a69c4a6c | -5.31569 | -43.33349 | 2025-09-20 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 226f7d4d-c5cc-3e26-a490-6f3dfc75d5a9 | -4.86972 | -46.83211 | 2025-09-20 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 929b4ad8-3302-3ae3-89f4-11ef15912b14 | -7.57789 | -45.50054 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 999b21ae-a9a9-362d-a51d-5b718be33446 | -6.38946 | -43.31918 | 2025-09-20 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb2a82c9-52a4-3360-ac61-092d2d9bd69c | -6.37566 | -43.33805 | 2025-09-20 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4dc3fc2-c572-39c0-8cd2-a04395a21eaf | -7.60562 | -45.47586 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 782efc30-7204-3984-989f-e5bbc1180217 | -4.47685 | -54.85257 | 2025-09-20 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ea0ec30-0018-3bcd-a7d3-f6be6066a013 | -5.54712 | -47.45517 | 2025-09-20 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9de8104-9a1d-3c93-b761-18551906cb4c | -6.37443 | -43.34633 | 2025-09-20 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a6567b07-f547-3cb4-890f-a5aed6a80114 | -7.38247 | -47.04029 | 2025-09-20 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8489dfbc-966c-3886-b95f-2dd40f3e9353 | -4.94091 | -45.4877 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc024041-e9f9-3cc0-922a-e2f281d3e718 | -5.59336 | -44.08954 | 2025-09-20 04:25:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 937b77d2-73f7-30c0-b5f5-7b9955efdded | -7.25376 | -45.48643 | 2025-09-20 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3c65ec00-31ba-39cc-9c61-ca3920c95785 | -3.51693 | -49.44775 | 2025-09-20 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6719834e-9fa3-3321-b777-04874f9b087f | -7.60617 | -45.47231 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6966a562-21f3-398c-b28b-a3639bc322cb | -6.08966 | -42.81903 | 2025-09-20 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dc30932c-4e72-384a-b926-1d471db7388e | -6.10207 | -47.85794 | 2025-09-20 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c072736d-96fa-3a53-985d-77b22577bf99 | -7.56733 | -45.50254 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65069ae5-e6ca-3247-9d18-b0b6a6e5206b | -5.4499 | -49.46542 | 2025-09-20 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c825b55-b0ad-337d-a43a-e93076ed464e | -8.48747 | -44.73052 | 2025-09-20 04:25:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f3e2f92-f961-31a3-9f15-90df1c3b9b24 | -6.06193 | -42.70365 | 2025-09-20 04:25:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1774a648-8355-3c5d-b3ed-34c464b20f2b | -5.04016 | -47.90328 | 2025-09-20 04:25:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8925b2b3-5794-37ff-ac99-6260d8eaef3f | -3.34728 | -48.39051 | 2025-09-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 97583d69-4862-35bc-8eee-0894c228ae18 | -7.59343 | -45.48845 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 346cbebf-637b-36fa-b7dc-0146a24754d6 | -6.1858 | -45.422 | 2025-09-20 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06a733c0-e63c-3b9c-bc9c-a8ebd4e53a23 | -7.43705 | -42.62392 | 2025-09-20 04:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 78df162a-be98-3d22-adb7-767c64c70bed | -2.94897 | -51.76136 | 2025-09-20 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51f1a979-28f1-3230-8eed-86a8960e68b6 | -4.35515 | -46.29343 | 2025-09-20 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45c699d1-70a7-358c-9845-cb8b15a26012 | -6.08681 | -40.89302 | 2025-09-20 04:25:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5f4d67a4-5862-3ad5-8fc2-7ae34d21bb3a | -8.82034 | -43.04274 | 2025-09-20 04:25:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b7623c0e-d65c-353f-93f3-63d47392be89 | -6.30696 | -46.08761 | 2025-09-20 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6061e47-b049-3f07-99a8-a5e4b46372b7 | -5.55429 | -42.15725 | 2025-09-20 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0be7f4ef-334f-370e-9a53-a8f520db16c0 | -7.18729 | -42.24108 | 2025-09-20 04:25:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0f2af4c9-22ce-3097-af2e-ab13e40a8c03 | -8.89906 | -40.44044 | 2025-09-20 04:25:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 099f9c21-5f5b-3c05-bdf2-e28aefd938dd | -7.24069 | -46.62067 | 2025-09-20 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe011f1e-2cd6-37f1-ab74-085b925da3ae | -4.65806 | -46.03525 | 2025-09-20 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87e7a7a4-90d6-3eab-8973-be0735534d2c | -6.65007 | -43.34769 | 2025-09-20 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| abea9f07-2ab5-323a-b681-bd0ff05995eb | -6.93426 | -41.88227 | 2025-09-20 04:25:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 48ed0b52-cb46-30db-977e-52bde87e52cc | -5.75888 | -42.77843 | 2025-09-20 04:25:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 80c16257-b1e6-3201-989d-014ca50463ee | -8.89967 | -40.43607 | 2025-09-20 04:25:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8c512349-6743-3a4c-8682-6bd0be29ae47 | -4.94145 | -45.48423 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d298fec9-0d94-3392-b7af-1c6e360be3b3 | -5.97038 | -46.67359 | 2025-09-20 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffc00eef-dd6c-348a-89f7-8732ed0a8a44 | -6.33343 | -42.38897 | 2025-09-20 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 60790ad4-0f56-3b72-a40a-7916bc36605e | -5.04752 | -47.90079 | 2025-09-20 04:25:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b52a318c-dddf-3a38-9cce-a61999df25ae | -5.71486 | -47.43039 | 2025-09-20 04:25:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f2355db-2a9d-3836-88a4-bf5b56f36428 | -5.1957 | -45.48875 | 2025-09-20 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ca342ade-d8ac-3da2-9cdc-c5bf9e7150c1 | -3.45655 | -51.21526 | 2025-09-20 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 72e209c3-7356-3ccb-a607-f7a54776238a | -5.05092 | -47.90137 | 2025-09-20 04:25:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a96845cd-ee76-3c2d-84cf-bc5ec1a0e0fe | -7.83635 | -45.63456 | 2025-09-20 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d77a6928-3370-3b74-a928-17aab9189530 | -3.38946 | -50.14942 | 2025-09-20 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37183707-f76f-359f-bc2f-4b679e595029 | -7.58737 | -45.50565 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70514962-d725-3a7b-9316-e88771466220 | -5.04507 | -43.08928 | 2025-09-20 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a698fd5-edee-37c4-bb9b-71542b7dad15 | -5.63049 | -44.83302 | 2025-09-20 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27c18ed7-bf05-34d1-b9ba-09939a183720 | -7.59405 | -45.50667 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba9c5bae-8858-3c30-9e98-56973c46c8d5 | -5.79517 | -43.63692 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07234e07-39da-3d2e-a2c1-11cca4a2de65 | -3.84037 | -52.31453 | 2025-09-20 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8967b4bf-c6d3-36dd-bc09-52867d696ee3 | -2.99045 | -52.62508 | 2025-09-20 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2177ff32-4700-3c64-a3c7-a2c70a7e1770 | -5.79281 | -43.65261 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74b51d35-b76f-3f2f-8123-4087e29edafb | -8.37768 | -44.69086 | 2025-09-20 04:25:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62632749-a448-3480-a039-bb6035d23b33 | -5.57102 | -43.44006 | 2025-09-20 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfc32a39-cd9a-3744-9294-711df84266b9 | -7.38908 | -47.04134 | 2025-09-20 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 60650888-df2b-36c7-8607-c3275d8def3f | -5.93587 | -45.08042 | 2025-09-20 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c348be5b-ea70-30ad-8285-65b502dc6bff | -5.8865 | -45.63939 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a357d894-69ea-3bf7-ac4e-c1ae026551a0 | -2.43603 | -49.33582 | 2025-09-20 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d5ba03c-6a22-31e3-b3ec-7f004a6c4ded | -5.69588 | -51.74038 | 2025-09-20 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9819a917-a7f4-391b-a7ff-315f7d5f86e8 | -8.4726 | -44.71246 | 2025-09-20 04:25:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfdbfc8f-9713-3559-9914-0eb50ba5f6d5 | -3.86228 | -40.34854 | 2025-09-20 04:25:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 39c254b7-bbb8-37e2-9b60-92d15480d494 | -6.64726 | -43.41454 | 2025-09-20 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58f91a60-8d53-37b0-b5ff-9d0f9317ee99 | -5.57098 | -43.44278 | 2025-09-20 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9b8779a-6845-311b-9e63-f16a7bdcc2c6 | -8.14912 | -43.63562 | 2025-09-20 04:25:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b64c494d-bb3b-3153-9fc1-51c4a6be20d6 | -5.93642 | -45.07688 | 2025-09-20 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 542b2493-e6e7-3d15-a1c4-846fc0fa5259 | -5.79399 | -43.64476 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1314eb35-bf74-3703-8cb4-407283d36b22 | -6.37504 | -43.34219 | 2025-09-20 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b568e475-b5d8-3cf0-9f4f-6ba8da3dc005 | -3.50331 | -40.40594 | 2025-09-20 04:25:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 54fcfe94-4ae8-31a4-a340-47fcd5282737 | -1.76119 | -48.0519 | 2025-09-20 04:25:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11973469-661f-322d-862b-6018c6db24e6 | -5.04317 | -45.57421 | 2025-09-20 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df3d6e6d-8f06-398e-9c80-6f0edb9e59c3 | -5.97363 | -47.66479 | 2025-09-20 04:25:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0298995b-1f07-3a48-8bf5-7e75a46e2e77 | -7.23571 | -46.60928 | 2025-09-20 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 273637ed-0263-3e14-b1b5-c160b76789d8 | -4.66565 | -49.32704 | 2025-09-20 04:25:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d46f94aa-88ca-3445-98db-aaa72229be7f | -5.93976 | -45.0774 | 2025-09-20 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 578b3e8e-e9f2-3285-8654-30bcf11db550 | -6.2014 | -41.22161 | 2025-09-20 04:25:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 56f71994-cc6a-32dc-bb5f-d3bf34f9b492 | -7.58954 | -45.49145 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c100ee9e-a387-36b0-9ebe-15081436881b | -6.17083 | -43.68806 | 2025-09-20 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 676e5755-2526-3d6e-bf18-537a198ef06f | -7.62492 | -44.45161 | 2025-09-20 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9583919-8677-3a40-93a8-e24badf4de80 | -7.29917 | -44.12988 | 2025-09-20 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0c260d81-2b85-3e47-bda2-17429c2fdbd8 | -5.69661 | -43.33083 | 2025-09-20 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4abd0e8-51ce-3264-a0ee-a2fab37e5db3 | -7.60897 | -45.47635 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README13.md)
