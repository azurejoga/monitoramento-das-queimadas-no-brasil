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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb2a9f5b-023d-3c3b-b4b5-6a41bc5a3888 | -6.5616 | -41.4894 | 2025-07-26 13:50:00 | GOES-19 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 203.2 |
| 40b8a593-3620-3187-bee5-576df3b65679 | -6.8576 | -43.6867 | 2025-07-26 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| f268dd07-07ea-3a0f-928b-576db1d323ed | -6.6206 | -58.8483 | 2025-07-26 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 525.6 |
| 713513d0-a258-31fe-94c9-fbeabdf02210 | -18.4011 | -44.1853 | 2025-07-26 13:50:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 5146377a-6438-3f5a-9261-b73239a221fc | -3.4367 | -43.1298 | 2025-07-26 13:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 69cf7c37-5f8a-39ce-83ad-993438a88e67 | -3.4366 | -43.1532 | 2025-07-26 13:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 180.7 |
| 54d92208-c55a-3b6a-8375-7af5a111c8dc | -10.6523 | -46.6303 | 2025-07-26 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 08858d70-3bb0-30c1-8821-cd7e0b5b06c3 | -4.0567 | -42.5354 | 2025-07-26 13:50:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 54929a99-1cb6-3fa9-82bc-41647096fbc3 | -3.4367 | -43.1298 | 2025-07-26 14:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 147.1 |
| e943fcd5-c16b-3882-b43b-50e8aa029aad | -6.5613 | -41.5135 | 2025-07-26 14:00:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 234.2 |
| 5f02f953-7444-3cc3-a1c3-72b45176c5e0 | -7.2826 | -39.6224 | 2025-07-26 14:00:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 216.2 |
| 16e6192f-772a-3ce7-892a-297d456cd71e | -6.8576 | -43.6867 | 2025-07-26 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| b9fa224d-0fe5-3ae4-9e23-c27145c552ce | -18.4011 | -44.1853 | 2025-07-26 14:00:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 119.3 |
| bfb74bd2-bfc9-3887-8b6f-e718917f4055 | -4.0567 | -42.5354 | 2025-07-26 14:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 57e17189-a5e7-3fbc-8a30-e147545e0193 | -7.2957 | -60.169 | 2025-07-26 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| e457f7b7-b566-306f-8578-9dbf2bb902eb | -4.0754 | -42.5344 | 2025-07-26 14:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 0ff6d08a-a1da-3454-afe8-016174e85daf | -6.5616 | -41.4894 | 2025-07-26 14:00:00 | GOES-19 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 199.6 |
| 775a6c3a-56a8-3071-a31e-b73dd17534e8 | -3.4366 | -43.1532 | 2025-07-26 14:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 257bb2fa-0d6e-3aba-b32d-d393f491417a | -6.8764 | -43.685 | 2025-07-26 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 81737f2f-4cfd-3f1a-b718-1d23f508d754 | -7.2823 | -39.6474 | 2025-07-26 14:00:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 110.7 |
| fae452c8-c9ae-3b44-9ca6-461ea5dd7df9 | -13.5271 | -45.5073 | 2025-07-26 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| c8f3352a-0cde-3dc1-bd4e-80bfb165ba34 | -6.5565 | -45.6111 | 2025-07-26 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 286b3193-cdfc-33f1-9972-21496a41cdcc | -7.2826 | -39.6224 | 2025-07-26 14:10:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 231.6 |
| 015e98c8-45c6-3691-902b-db2d1229e0ba | -2.9555 | -42.3293 | 2025-07-26 14:10:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| f347c314-568d-3cf2-9820-7192335406e4 | -3.4366 | -43.1532 | 2025-07-26 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| f2c3f13f-f60c-3514-8170-ad36f70c7d20 | -3.4367 | -43.1298 | 2025-07-26 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| b0e198eb-20d2-3473-a3cf-a5e7642d59c5 | -6.5613 | -41.5135 | 2025-07-26 14:10:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 272.0 |
| d5d3195c-97f2-3a50-9c3b-532fce2fff04 | -13.2507 | -51.1596 | 2025-07-26 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 169.2 |
| fa39e4e1-2510-338e-b13c-80de69e68aef | -7.5151 | -45.3931 | 2025-07-26 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| e3aacf41-6931-3800-9ea8-2f97a3388b9e | -18.4011 | -44.1853 | 2025-07-26 14:10:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 87.0 |
| cc3e6413-f8ce-351e-9f7d-6dba4c27c295 | -7.2823 | -39.6474 | 2025-07-26 14:10:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 132.9 |
| 583f1865-fb9e-3e08-ab7a-c6d657e7fc64 | -4.0567 | -42.5354 | 2025-07-26 14:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 136.4 |
| 63c111d6-ffea-357c-8af6-9445a1798506 | -6.5616 | -41.4894 | 2025-07-26 14:10:00 | GOES-19 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 252.0 |
| 52415129-18a4-3ae0-aef6-669dc6e055b3 | -13.5266 | -45.5305 | 2025-07-26 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 2dbad44c-e680-3d37-8386-84a811949ed8 | -13.251 | -51.1382 | 2025-07-26 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 143.6 |
| edd7fed3-f1ee-3154-85c8-232e3fc2dd0d | -8.07 | -63.8576 | 2025-07-26 14:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| da2a8072-6fa7-3a7b-8eb7-60575bc73632 | -2.9554 | -42.3529 | 2025-07-26 14:10:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 3576ab94-2bf6-3664-b5e5-84c7846e6eec | -6.8764 | -43.685 | 2025-07-26 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 4141b3b8-7d2c-36ce-ae95-06d6c548f8da | -7.534 | -45.3914 | 2025-07-26 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| b2af0901-f9f1-3cdb-b6d3-f8ca32525623 | -10.6527 | -46.6078 | 2025-07-26 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| a306ad1d-d0c0-3086-a320-ae411c7de407 | -4.0382 | -42.5129 | 2025-07-26 14:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 0e5a60c5-443c-37fb-b7bb-3c1cb388ac2c | -10.6523 | -46.6303 | 2025-07-26 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 161.3 |
| dcea65f6-2032-3ff9-b77e-bca97f553730 | -3.3957 | -47.5003 | 2025-07-26 14:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 1c974fd2-815b-36a3-9156-8972d6cf33de | -7.2826 | -39.6224 | 2025-07-26 14:20:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 243.3 |
| 8b976e6e-a7c8-3063-a48c-3b43112f0c26 | -6.5565 | -45.6111 | 2025-07-26 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| b2860238-e29a-3f5a-89fc-29ad7a39f9fc | -10.6714 | -46.6279 | 2025-07-26 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 0c25ced5-f831-3383-88c7-d6742120c8a0 | -7.2823 | -39.6474 | 2025-07-26 14:20:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 130.6 |
| 96b26751-dff8-3778-bda0-d8d0edb32f30 | -6.8764 | -43.685 | 2025-07-26 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 135.6 |
| e2d1a521-6bcd-32f7-b40b-c05b63931702 | -3.4366 | -43.1532 | 2025-07-26 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| fa2c1e6b-bae3-367a-9398-baf1c9a411b7 | -7.5151 | -45.3931 | 2025-07-26 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 6818a1c3-0dea-3e87-a8ca-0fc71446c63a | -4.0754 | -42.5344 | 2025-07-26 14:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 129.3 |
| fe5627f3-931b-33e4-958c-93b6911cb34a | -6.5616 | -41.4894 | 2025-07-26 14:20:00 | GOES-19 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 278.6 |
| b8e4f868-976e-35d4-9c7a-e95d376b25e8 | -6.5567 | -45.5886 | 2025-07-26 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| be13c6fd-b900-38ef-81ea-177c45efd635 | -6.5754 | -45.5871 | 2025-07-26 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| d6531ddb-14bb-3d5d-81fd-14e711b2e8d8 | -6.8576 | -43.6867 | 2025-07-26 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 539a14fd-26b8-304b-b6a4-dd5d20bf52e5 | -3.4367 | -43.1298 | 2025-07-26 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 9dc2f305-80a6-3788-8923-7091d9519f14 | -6.5613 | -41.5135 | 2025-07-26 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 339.1 |
| f6045497-092c-3258-be21-773b54771462 | -8.07 | -63.8576 | 2025-07-26 14:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 6cbc2c31-6dbc-311c-95ff-20c36a217a56 | -4.0567 | -42.5354 | 2025-07-26 14:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 129.9 |
| 73766cbc-2af6-379d-b5e9-72ac7fe21d8d | -18.4011 | -44.1853 | 2025-07-26 14:20:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 92.6 |
| b423fc60-fe6e-32a3-b5fc-a77be75fd84f | -3.4366 | -43.1532 | 2025-07-26 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 0da938ba-2025-356c-8e71-0c9102183ef0 | -10.6523 | -46.6303 | 2025-07-26 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 8ce9403f-7c8f-3f32-9796-45fd5a91f2a7 | -6.5616 | -41.4894 | 2025-07-26 14:30:00 | GOES-19 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 153.2 |
| c7bb277f-8ca6-3876-9ea9-583705b2624b | -6.5567 | -45.5886 | 2025-07-26 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 77aed1c4-b633-3fee-b60e-fa9d1fbc8701 | -13.251 | -51.1382 | 2025-07-26 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| d602fdce-c553-3ddc-8a88-d61e47b8af1e | -6.5613 | -41.5135 | 2025-07-26 14:30:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 179.9 |
| 114daad9-9007-3dae-84dd-b86743e9eb95 | -4.0754 | -42.5344 | 2025-07-26 14:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| b76af68b-8112-32fd-9408-bad1a2b47231 | -8.07 | -63.8576 | 2025-07-26 14:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| a0d9257c-ff9a-306b-bef2-f40c8d95ba22 | -11.344 | -51.2122 | 2025-07-26 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 7b8b4e71-20f2-35c7-aed8-9aaeb98d0b2a | -10.6714 | -46.6279 | 2025-07-26 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| c26cc984-c1e6-3e45-96fd-314fc1e1f9cb | -7.534 | -45.3914 | 2025-07-26 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 81008a3c-7d1d-3d0b-a031-f4b4b01dda67 | -7.2823 | -39.6474 | 2025-07-26 14:30:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 08326bb4-a821-3ee6-bef4-9102cf8238ef | -7.2826 | -39.6224 | 2025-07-26 14:30:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 138.0 |
| 220c960d-3e4c-37ce-b233-c907fc796010 | -7.2957 | -60.169 | 2025-07-26 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 63ceb88a-bf99-3d24-9854-653b52f6f779 | -18.4011 | -44.1853 | 2025-07-26 14:30:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 37e1efa1-d80b-3227-9b87-e775e7c8ea70 | -3.4367 | -43.1298 | 2025-07-26 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| da5d2337-d91a-33df-807c-3268e86efc8d | -7.5151 | -45.3931 | 2025-07-26 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| f25517e9-79a2-3d20-9718-b71d0c051083 | -4.0569 | -42.5118 | 2025-07-26 14:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| 1bd036e4-1538-3d2c-afed-5076165316b0 | -6.8764 | -43.685 | 2025-07-26 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| bf32fde6-41af-3f9a-b9e8-266f1380e60d | -6.8825 | -43.1241 | 2025-07-26 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 1787a125-e204-3a8a-bbce-b8bda0ef6bbb | -6.8576 | -43.6867 | 2025-07-26 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 9a365e1a-c3dc-365b-8200-a40e6f449c4c | -4.0567 | -42.5354 | 2025-07-26 14:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 184.1 |
| de92beb1-8bfd-3131-907f-58fa6bd8370c | -9.1291 | -45.8632 | 2025-07-26 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 7cf319b0-31e1-3c96-ae57-7cdcdd43c63b | -7.5151 | -45.3931 | 2025-07-26 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 4c951e1e-3257-393d-823b-8b3983b6c07f | -3.3957 | -47.5003 | 2025-07-26 14:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| de8c0505-eb2f-3fce-bf8b-0ad015451fa8 | -7.2823 | -39.6474 | 2025-07-26 14:40:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 110.7 |
| 8661ffde-cb7c-3c16-bf81-30ddab5a42b4 | -10.6714 | -46.6279 | 2025-07-26 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 154.8 |
| c7b0d78a-4cd0-3e70-8037-6f4d20f9d6fb | -10.6527 | -46.6078 | 2025-07-26 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| cd0b531d-0a2e-3683-a35f-8c37cafd4d03 | -4.0754 | -42.5344 | 2025-07-26 14:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 48a2ebf0-d9b2-3c19-a2a7-bfbbe7665ceb | -10.6523 | -46.6303 | 2025-07-26 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 188.4 |
| ef66895b-f06d-3d10-beb3-5268d362c44a | -7.2957 | -60.169 | 2025-07-26 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8cb752ea-4d36-3061-aaeb-fcc3c73502f0 | -3.4366 | -43.1532 | 2025-07-26 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 58dd85cf-d754-31e8-acd5-e4e6d5574029 | -9.1288 | -45.8858 | 2025-07-26 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| e9ef9003-6bbb-3424-9e8e-0dc8ee3a9641 | -13.5077 | -45.5105 | 2025-07-26 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 147103ba-4f5e-35f1-a58d-88d6490c77b8 | -3.4367 | -43.1298 | 2025-07-26 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| beb841e5-fe4f-386b-a438-5611638b1c59 | -4.0567 | -42.5354 | 2025-07-26 14:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 175.7 |
| 9f6954c5-0d3f-34cc-b99f-f32eac10b727 | -6.5613 | -41.5135 | 2025-07-26 14:40:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 141.5 |
| 69a659ea-038b-343d-9056-22710134d557 | -6.5567 | -45.5886 | 2025-07-26 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| fb52a549-cf6a-34aa-b7ce-a7c35d06162f | -7.2956 | -60.1882 | 2025-07-26 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 6007ba73-f966-3d91-a7a5-5bf194994d00 | -11.344 | -51.2122 | 2025-07-26 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 146.8 |


[Clique aqui para ver as próximas entradas](README35.md)
