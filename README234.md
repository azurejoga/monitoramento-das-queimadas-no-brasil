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

## Dados Diários - Página 234

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11b250fb-4920-38a9-9577-05013e8de277 | -2.9449 | -54.1099 | 2026-10-08 15:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| d017fe8a-150f-37e2-b671-adda92423357 | -3.0809 | -57.6593 | 2026-10-08 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| aeab2eb3-b7c3-3ded-8ea0-fc584c5cab68 | -2.6051 | -57.5905 | 2026-10-08 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 1d88abf4-9bc9-32c0-b80e-87305d1ec08c | -9.4818 | -66.8022 | 2026-10-08 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| c58d3bfe-bccb-309c-b57c-94ba87bf0499 | -3.8338 | -57.1746 | 2026-10-08 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 97b6de28-48f3-3596-aee4-e259d64a7510 | -12.232 | -44.7194 | 2026-10-08 15:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| d4271042-5cd0-3bd9-8471-2b6996583a3a | -2.3863 | -57.2247 | 2026-10-08 15:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| c95de53e-e895-3927-a595-343ff5e26b7b | -12.1545 | -44.7547 | 2026-10-08 15:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 221.8 |
| 83ad8977-8cec-3f59-8af3-391e61e62abc | -3.6448 | -58.8839 | 2026-10-08 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| f0c64bc4-48f3-3f78-b60c-cc9cf8f4d00f | -2.572 | -56.1646 | 2026-10-08 15:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 211d169f-351b-3f5c-93f9-265b6a11ad56 | 1.5283 | -56.0227 | 2026-10-08 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 72781470-b17a-3231-a2fc-e53289a56118 | 2.764 | -60.0297 | 2026-10-08 15:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 351.1 |
| b8abddf4-fa90-3cde-baf7-aa69c1412cc3 | -6.1971 | -52.8705 | 2026-10-08 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 21fee044-6bd1-39f7-9673-b8c28da5361f | -11.6382 | -43.6166 | 2026-10-08 15:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 218.6 |
| 38ad01b8-2924-3da6-9038-02efadebd8b1 | -2.204 | -56.9155 | 2026-10-08 15:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| f5c0ba6f-f65d-3b58-85a0-fdfeab2260d8 | -2.8163 | -54.133 | 2026-10-08 15:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 470ea6aa-504a-3b53-92c3-fc45e25bbcd8 | -2.2223 | -56.9152 | 2026-10-08 15:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 189.1 |
| df3ec7fb-de45-3618-8322-91ee60054a9c | -3.2451 | -57.8693 | 2026-10-08 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| e44aaf36-129d-3f60-b397-1e10416deea5 | -3.0631 | -57.4847 | 2026-10-08 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| febf297e-39ff-3575-9749-e9a92a793d0f | -12.1948 | -44.6554 | 2026-10-08 15:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 5bea727b-faf3-3dd8-8659-fb5c3740298c | -3.9483 | -56.0138 | 2026-10-08 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| fb90bd55-3c85-361d-98c0-cf4aa188b6e8 | -2.7981 | -54.0732 | 2026-10-08 15:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 7deb1b1a-ad23-3224-8883-6f24b0240764 | -3.0798 | -58.0276 | 2026-10-08 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| db474e8e-69a9-3422-bc72-bb5c2391e060 | -1.6213 | -55.1321 | 2026-10-08 15:40:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| d24c08c4-4804-35c7-bf9f-a6a0411d4b16 | -6.58806 | -41.58302 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3321ed0a-d229-3e6e-afb3-7759b9b5d447 | -10.57283 | -46.292 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 4665c863-ddbf-357c-9813-8a2215209818 | -5.54477 | -43.22675 | 2026-10-08 15:41:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ec241363-86ff-3752-a6ff-52834bfc6d83 | -6.18911 | -37.85575 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 8ccff228-3cd5-39fb-9d6b-ff50e0b727c0 | -8.60115 | -45.62641 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 43.5 |
| b4f0e6b1-4b3b-3325-af05-2d5a1ff9798f | -6.63572 | -44.884 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f6dda2f5-373a-3ece-bda9-3780ab64df01 | -7.48688 | -42.81582 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 7caaa6b9-b5e5-3e93-99d1-93badbfcaca5 | -7.26031 | -45.34469 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 057b1111-1bf1-345a-aa70-2e3f3638fde4 | -5.39069 | -42.96811 | 2026-10-08 15:41:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 13.8 |
| e71678db-97d4-346f-9f2b-ce8104916dab | -7.46993 | -42.81971 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 29c29ec9-a8dc-3d17-bc32-66171e3b814d | -8.80831 | -45.79827 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 5179ebed-d9c8-36f3-bbcc-e40b5c632630 | -6.53787 | -45.38906 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 36cd1c31-ebef-33c1-ac62-044893439614 | -9.13428 | -45.832 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 9a61b636-df06-3914-8fe7-412129f85fd3 | -11.20582 | -45.21776 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 04041bfe-a52d-3558-80fe-b36c52373856 | -5.63166 | -45.79615 | 2026-10-08 15:41:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| c7ff1354-d99e-3a12-890a-26e1566c0067 | -6.97544 | -45.14103 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| fec7efea-ecd3-3f8a-91d5-9dc47f272712 | -6.90977 | -43.93159 | 2026-10-08 15:41:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 75aba89f-3e7b-34c9-ae07-14b96c0b4094 | -6.31761 | -43.49058 | 2026-10-08 15:41:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 182c94c1-2c4a-3b67-a810-78caf68b8bd7 | -5.78012 | -45.38418 | 2026-10-08 15:41:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| ab6d81bf-6dfa-31bf-9b22-ea71975f7cad | -5.2398 | -38.54646 | 2026-10-08 15:41:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 12.7 |
| f8768836-41df-3858-864a-68fe98246c19 | -5.7522 | -42.0679 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 6980d285-a6e2-3acf-8a32-f7508c752a39 | -6.67381 | -45.37217 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 284.3 |
| 5898dc51-f55e-3d75-84d5-77c5d1a6f55c | -7.777 | -43.81774 | 2026-10-08 15:41:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 5704622a-a15e-390d-8114-79a208db6f5c | -9.89724 | -44.85164 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 1af472e7-c95e-3b5d-9edc-5cac5e9ea3ba | -6.21715 | -44.83805 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 97394bdc-bccc-3215-a503-e390c6dbcebf | -7.54082 | -42.08835 | 2026-10-08 15:41:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 1efa37d4-2de9-3f0d-82d0-558e8198fc24 | -6.32769 | -43.35185 | 2026-10-08 15:41:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e68dd2c2-8bc8-3ae8-bca3-f7a5aefd91ee | -5.75052 | -41.62749 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 1d5c1553-62c2-3ae5-b6a0-a28affd977af | -5.72213 | -41.64336 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 46.0 |
| 9c4a739f-fc21-37fd-a83f-f22ec8cad99f | -6.72391 | -45.18822 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 9e8e24db-4120-3fc0-b1bf-7ed486c1aba2 | -8.94244 | -45.15506 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 153e1e0c-fdb9-3343-ad65-ccd456f53f53 | -10.92988 | -45.38955 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 58bed81a-3447-3046-b2ed-1a8535c1cf2b | -6.46744 | -46.53958 | 2026-10-08 15:41:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| a445c745-a367-3bea-b082-98be2d254472 | -10.16162 | -45.96532 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 021bc93b-b3a3-37fa-8459-a500c9840da3 | -5.3616 | -42.83804 | 2026-10-08 15:41:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| e9f3c094-406c-3fb0-8527-b32edfefffa2 | -7.05098 | -44.33641 | 2026-10-08 15:41:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 837bb188-edeb-3bea-8a00-caec3403f374 | -9.07694 | -45.11049 | 2026-10-08 15:41:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1d2d7390-6f78-3de4-af32-a3ba3ad3f13b | -4.74888 | -40.50908 | 2026-10-08 15:41:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| ee67e350-f057-39c6-bb88-fe97b8990441 | -10.15614 | -40.53155 | 2026-10-08 15:41:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 39.1 |
| 01f0190d-d33e-3d96-aa45-a023f97aef2e | -6.40227 | -44.94696 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5057258b-d1a0-37de-8fa2-33115af15bb5 | -6.92956 | -43.06422 | 2026-10-08 15:41:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2e30f00c-722e-3859-970e-c8a589dd13c0 | -7.31757 | -44.00075 | 2026-10-08 15:41:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0286e3a4-b172-3c09-8387-3491ad4be6de | -6.36831 | -42.53009 | 2026-10-08 15:41:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| b9cad07d-0aae-3fbe-8136-d5b2697671d0 | -6.15666 | -42.58881 | 2026-10-08 15:41:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 3fca9544-29ff-3232-bb2f-1f779e973f83 | -8.20677 | -46.39634 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 1e97253b-8162-3c69-a057-97753d266da3 | -11.0043 | -45.4215 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6bc4f2be-0613-3911-9fbf-5865e2096fcd | -6.99163 | -40.03394 | 2026-10-08 15:41:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 17.2 |
| d79708e7-e655-3a7c-9eeb-880d84d47b8e | -6.01545 | -42.25893 | 2026-10-08 15:41:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 696de256-5960-367d-8f51-b9c7d71a60dc | -8.88502 | -45.61353 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ac62f9df-990e-37ac-8920-6a045ac523cd | -6.82207 | -39.54585 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 16.1 |
| feedb919-2288-3446-843e-a847de7bfb32 | -9.76375 | -44.7853 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 810f88d9-2b18-3eaf-9646-ca055a2f4095 | -6.9334 | -43.66249 | 2026-10-08 15:41:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 7caf34e6-7ef7-33a8-a51e-a3b9087fde5c | -8.07731 | -45.61317 | 2026-10-08 15:41:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b2e212ad-9f23-3dcc-b520-09f97e596bf8 | -10.9049 | -45.53667 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| fa9df6fe-6f95-35a9-8702-28313cfcc410 | -5.23577 | -38.547 | 2026-10-08 15:41:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 9bac44c4-80a2-3241-b716-2e7b4656ef48 | -6.82356 | -41.89224 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| ebac5d9f-d7fb-3261-b705-b5f43aa5927c | -9.90692 | -44.82197 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5bdfd830-fc29-3d8e-a9a3-e1dc21585a42 | -8.93791 | -45.17298 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 340.0 |
| a3c5575f-ec36-3cd9-b3d6-853632c3445a | -5.96417 | -43.90011 | 2026-10-08 15:41:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 5f6e39f7-3fb6-3b56-a95f-7e8aa72824b5 | -6.05075 | -42.59783 | 2026-10-08 15:41:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a95b907f-5c9d-38f7-8a46-6b6333d80ed4 | -8.95062 | -45.15758 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| bab89012-1819-33eb-a476-9184dc29dadc | -6.05122 | -43.14418 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 538de4dc-41b8-3923-9f3b-0ac3b7467e98 | -5.76901 | -42.06026 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 5e56749b-9d71-3eac-8696-24ad04c87a0b | -8.5848 | -45.69333 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 1739d812-aaba-3ab8-8930-a24c0a4c9a0f | -7.38417 | -46.23169 | 2026-10-08 15:41:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ff96ab25-7721-31e1-b00e-c25eadb25fd7 | -8.96755 | -45.13345 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bcb676e8-8ca1-3b26-ac73-68e7e2da173f | -8.93377 | -45.1827 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 189.5 |
| c1671a57-f868-34e8-90a2-7e050278f753 | -5.51623 | -37.48596 | 2026-10-08 15:41:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 66d166c0-83e0-3ec7-b499-ca874ec9f6da | -5.70395 | -41.73136 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.0 |
| ac5cfec9-c108-3637-9d6a-b522f03db952 | -6.55588 | -35.50507 | 2026-10-08 15:41:00 | NOAA-21 | TACIMA | PARAÍBA | Brasil | 2516409 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c6675332-5277-3899-b917-351599f90ae1 | -7.47569 | -42.85804 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 31.6 |
| 09f21ad5-da54-30b4-8992-ff57432656bb | -8.88797 | -45.39107 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 36.9 |
| da1e0930-7236-3bea-b8e1-0e9e728e4555 | -8.20232 | -46.41787 | 2026-10-08 15:41:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| ae90ad3a-d364-3faa-8e37-7aac80e82638 | -6.15965 | -39.43333 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 82ac8886-fd0f-3a69-be9f-42874ed78577 | -5.77194 | -42.05899 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 98b01fca-f6e3-33d1-b2dd-58a990ef6f5d | -10.90435 | -45.53612 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |


[Clique aqui para ver as próximas entradas](README235.md)
