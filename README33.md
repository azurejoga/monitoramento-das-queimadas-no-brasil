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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04b2406a-c248-326c-8b2c-8b1ce5b05b5e | -6.24649 | -51.70311 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efe4d031-9584-360d-9bb7-e10071319767 | -2.67767 | -57.53567 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d20e7d08-e4db-3a0f-a69d-9d80e77ca179 | -4.92295 | -45.83183 | 2026-09-13 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 63b97c94-df3e-337e-9206-5a88e6c836dc | -3.04839 | -51.26157 | 2026-09-13 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a601202b-a2e1-3991-97c6-8dc10c139962 | -4.15369 | -50.21043 | 2026-09-13 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb4a29c0-a737-3e61-bf03-1b10f0dd1e1e | -6.23571 | -51.68165 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d3aa741-e9ca-388b-8fd0-94b529ed52a1 | -7.3843 | -45.35976 | 2026-09-13 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6da843d-7ce2-30a6-8504-e6eca39bbb75 | -3.79136 | -48.93161 | 2026-09-13 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8213c4a3-6d39-3eb7-a46f-4574134506df | -5.05415 | -42.93932 | 2026-09-13 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 599676b8-e83f-3040-8194-72d647374e69 | 0.14253 | -51.47207 | 2026-09-13 04:49:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f691b8d-71b6-3d99-af7e-8f615aa4af51 | -3.40815 | -48.89297 | 2026-09-13 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 239e4fc5-110d-3e99-88f0-24fb624b4f87 | -2.95578 | -50.40718 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5098ed85-bce8-3011-9b65-89739ecbdb7d | -5.48334 | -45.60114 | 2026-09-13 04:49:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0d4e1fa-bd20-381c-a2c8-280d4eaa8f3f | -2.96037 | -50.4004 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| addcfeb8-4f87-3472-a4c0-69404dff3045 | -3.04198 | -51.25652 | 2026-09-13 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d8cf555-4c9b-3164-ab04-e0c206f71791 | -6.22403 | -51.6876 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 589c5ee6-8dc2-3e36-804f-b12422ee8022 | -1.22999 | -54.12112 | 2026-09-13 04:49:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f5ac4a6-7a9c-3606-94ba-f9f8f8b833da | -3.15866 | -48.60925 | 2026-09-13 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56cac367-e452-37f1-acb5-643aa1ee3eed | -7.47185 | -42.11463 | 2026-09-13 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a5e757c8-aaa6-3f6a-a413-9c2b51a26635 | -3.32878 | -42.29644 | 2026-09-13 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5bd290e9-26a4-3ba4-bb90-6f37ac5e16b4 | -3.40894 | -59.25115 | 2026-09-13 04:49:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bbd7343b-aaab-3526-a3f6-5c4048ebe84e | -3.21694 | -48.9687 | 2026-09-13 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb66fefa-4693-370b-8d4e-915223337361 | -2.93991 | -50.48373 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b60b4bd9-34a1-3d64-bcbb-2c9d09418102 | -7.0155 | -44.61575 | 2026-09-13 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c8671e4-30f1-3383-af24-f23dd13efe12 | -5.89701 | -45.54137 | 2026-09-13 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e80e421-fa31-3309-bae6-b3c43aa50a38 | -6.66184 | -44.96155 | 2026-09-13 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b215532-47d7-3490-a64d-f87dac7b3334 | -2.78329 | -51.36337 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 974bcb4f-71dd-3957-b2c3-172c87bf15cf | -5.0535 | -42.94356 | 2026-09-13 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3476dbc7-6125-32c3-9cb0-21d60951bcf6 | -7.0215 | -44.63115 | 2026-09-13 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| df94b6b2-b6b9-3db1-a8ee-81abe78e5824 | -1.22029 | -54.12698 | 2026-09-13 04:49:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b406ef19-47a4-3998-becf-c6c2a744975e | -2.6682 | -57.52746 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed3682e6-e0a0-3921-8c9f-b18ccd0ac5cc | -6.85865 | -47.42907 | 2026-09-13 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0f45213-80a8-3598-822f-6466440099ec | -6.72575 | -45.40933 | 2026-09-13 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2784a031-ff83-39f4-8d21-e74633f5000f | -2.8488 | -49.54117 | 2026-09-13 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 872757f7-97aa-35c6-8714-fafed47e6151 | -2.6367 | -54.75719 | 2026-09-13 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52187fc9-bc0d-33d1-8770-affbb147178d | -6.22751 | -51.68817 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2c89709-0003-3d1f-93a2-4130726866aa | -1.22087 | -54.12336 | 2026-09-13 04:49:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 72ee51d4-c601-3f10-a8f7-ac9c7416fdd3 | -2.68294 | -57.53656 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71707cc0-af97-37dd-8b8f-b3da32eb476c | -5.86018 | -46.22766 | 2026-09-13 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5dee3b8b-722e-3403-b27f-1ac0cce8021e | -5.19898 | -45.26469 | 2026-09-13 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e83a4c1a-bcff-352c-973b-1266eb84bf16 | -3.70679 | -45.388 | 2026-09-13 04:49:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b40c7210-eb0d-3da8-9337-dda523742c4d | -2.82976 | -49.23075 | 2026-09-13 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de898f2b-7f92-36ef-aaa5-5fadb3f8bb43 | -3.33594 | -42.29624 | 2026-09-13 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 43942f37-5a44-32de-9cf5-194c459759cb | -2.95473 | -50.39202 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc40b156-06ab-330b-ab2d-e55ad58ced64 | -7.77046 | -46.69093 | 2026-09-13 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 289b9413-5546-3602-a23e-46c8ed813731 | -10.03876 | -48.2155 | 2026-09-13 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33dbe466-852c-3c80-b9ed-d9862922a841 | -13.38064 | -48.01252 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 240d93f3-0e48-3460-b088-9da2374daf6f | -13.45124 | -48.49472 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a048f393-cf62-3a4f-9a39-b1f1c136be52 | -8.1165 | -54.79493 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7922a76f-c8d5-3159-846f-5a0d59739667 | -8.1714 | -55.10479 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a59a4386-82c5-3725-ad77-287967184070 | -13.46008 | -48.48379 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1c006b6-e0d6-3bba-87d9-141c62d1f08c | -10.31069 | -45.28708 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fee31e7-cf12-30c0-85b2-ffae64354157 | -10.89707 | -47.82095 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1b7bd55-8511-3d8b-a567-fe4f8504caa6 | -9.89521 | -47.5905 | 2026-09-13 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 45acbf30-6084-3367-ac2e-722e5060a6c9 | -13.56577 | -51.4635 | 2026-09-13 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2025769-6ab1-3865-ab05-7ca7fe1d193a | -13.78333 | -48.7991 | 2026-09-13 04:51:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a72b9fe2-8d18-3964-919f-e229183dc8d5 | -10.57699 | -51.36506 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bc3d5f6-3e9c-3312-bbc6-890a2c88b694 | -10.25343 | -57.70441 | 2026-09-13 04:51:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d69f2a2c-6cf1-30e6-a8cd-bf146c32b107 | -7.49207 | -49.57844 | 2026-09-13 04:51:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4068e88f-1359-39f6-891e-9a05fa173ec3 | -6.29939 | -59.95329 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed8b7563-966d-3584-87f8-974d154eaed1 | -7.75298 | -49.44143 | 2026-09-13 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f540cc0f-0938-3409-8772-c3a332d59b9a | -6.27416 | -59.93122 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bee88cac-2592-301c-bbc8-648273f3bef9 | -10.31122 | -45.28342 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e019004f-8632-3c38-80c6-a995ad0e732b | -6.3146 | -59.96888 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a37b1cba-88f2-336a-835e-2505e54d9f62 | -11.72079 | -46.7378 | 2026-09-13 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ccea3a5-2837-33d2-b6ce-27e47d11f318 | -12.6702 | -54.71925 | 2026-09-13 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ffe4176b-e8b6-39a7-9b3b-55c82fb04384 | -6.31053 | -59.96355 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ee27b1e-55e2-3eba-9c0c-a6cdb17b3faf | -8.76851 | -61.40129 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7454e0a7-f90c-3f2e-bc08-852221bc26d6 | -7.24454 | -46.69929 | 2026-09-13 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2876ccb-eec2-3521-b72f-55d7151e4550 | -6.10265 | -55.66954 | 2026-09-13 04:51:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bbc4ac9a-57c2-38a6-8694-6cdaace335af | -8.03621 | -54.84885 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 347c4bcd-25f5-32bf-980f-8bd685c160ba | -11.80936 | -46.38522 | 2026-09-13 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 016079e5-d75b-3947-b581-720b05b10ca5 | -6.08832 | -57.90509 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23f62a8c-5d09-39f7-96a0-991f6e68ed2e | -11.18264 | -42.79517 | 2026-09-13 04:51:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 736b682c-a5f8-331d-a09b-2c523723c451 | -9.79695 | -55.30703 | 2026-09-13 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bdb1d69-ee21-39a0-a5b6-d31082820402 | -6.30519 | -59.9545 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ef1e6e4-863b-38fd-a2f9-582abaf0457e | -6.96183 | -59.74522 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f47e521-394e-3694-bce0-2c72a558610a | -10.56867 | -51.3526 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4efb232-2957-3a4b-aab6-f5fe6c80cb1c | -10.45468 | -48.66648 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e05f3e98-172c-3464-8796-4691808223d2 | -9.88457 | -47.58887 | 2026-09-13 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee99445e-9216-3086-9285-d684a190f2a3 | -13.626 | -47.88168 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ab80f9a6-631f-39d1-bc8e-356f6db3c367 | -11.8195 | -46.39725 | 2026-09-13 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ee39fdcd-d8a1-39f8-af59-fbf8662b8f19 | -6.1034 | -55.66518 | 2026-09-13 04:51:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1fd5bca0-6ce6-3bb7-8a7a-5ccf80384268 | -11.72464 | -46.73592 | 2026-09-13 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 874b2014-9614-3739-a0f1-0220922bdd51 | -7.28606 | -50.7845 | 2026-09-13 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c1cac58-5018-3368-b9f9-e6ab2fb43822 | -10.5872 | -51.35624 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5d739e7-d7cc-38ad-95c7-fbdd0c1194e7 | -6.10189 | -55.67393 | 2026-09-13 04:51:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 495eb525-3c64-33a7-8828-e1bd7242359c | -10.30824 | -45.27543 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa7cc2f9-4fff-3335-8e54-5a275019b53d | -13.30077 | -51.72292 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3e4d806-eb76-307e-b158-e8a10f5e0829 | -10.47014 | -48.63449 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e01f827-1916-39c8-a558-bdf692a85fb8 | -7.86255 | -54.69388 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdbd7986-cee0-38a1-9cb0-13d21e55ae29 | -10.68735 | -54.16431 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb1b48bd-9b81-3f59-a300-28712d3e17cc | -6.60146 | -58.84743 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfe42b9d-affd-3aef-a133-c1c63357c50b | -7.87055 | -54.69525 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17602f65-5376-360c-a92d-087ed8e94d86 | -6.08539 | -57.8614 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b0931738-4d7a-3d7d-a24b-48bc82233238 | -11.43965 | -45.15385 | 2026-09-13 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04140954-5cf9-3ea9-be85-f134288704f3 | -9.37877 | -50.11254 | 2026-09-13 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2cc7dd03-8464-323d-9a48-d991fe749486 | -10.94571 | -48.35339 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65fa5359-eb0e-3114-bfb8-8c518166c0c6 | -6.59336 | -58.83845 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17a5d38a-d20e-32ec-845c-cfe04f179576 | -7.28269 | -50.78395 | 2026-09-13 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README34.md)
