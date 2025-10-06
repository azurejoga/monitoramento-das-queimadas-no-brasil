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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4b41b40-ea23-3596-a08f-a650cd17ea99 | -8.19814 | -44.17132 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49bb811b-42cf-3f23-964c-305f2ed8c94e | -9.06248 | -46.63156 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5074c7da-82d8-32e3-b060-4c259237da6d | -6.10134 | -43.41875 | 2025-10-06 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f293e23-28dd-3e02-ae68-a640d370cbe3 | -6.33435 | -41.62335 | 2025-10-06 04:25:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 03d6a3c8-ca74-3dbf-a40d-3fb38dd5da95 | -8.867 | -46.83497 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ea621fb-1af0-3a86-8dc2-f31280d4d528 | -9.30653 | -45.66507 | 2025-10-06 04:25:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 476f5d46-97cf-35a5-800e-ee0b4cdf9cf7 | -6.69746 | -42.15855 | 2025-10-06 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 25fad9e6-10d3-3196-ac84-4e1c6b8652d1 | -8.67851 | -49.46558 | 2025-10-06 04:25:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0655116d-e79e-3119-9e54-e675dbf5241b | -8.66547 | -41.67788 | 2025-10-06 04:25:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5c34af1a-bc9e-3cd1-9331-e61dafcd366f | -4.31882 | -48.07573 | 2025-10-06 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5689ce6a-8806-3928-93f1-3c21523cab76 | -6.63231 | -44.51809 | 2025-10-06 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 553c3f7e-6485-3712-9983-ecf5fa334dcd | -8.88031 | -47.61745 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe11f892-66dc-326d-ad89-e8470b2acf8b | -6.6233 | -41.9795 | 2025-10-06 04:25:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2c725b37-e4a1-3e09-95e9-907f60ce9a7a | -4.39181 | -47.8372 | 2025-10-06 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db570c97-685d-3146-9813-3e80611e109b | -5.70473 | -44.85108 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 945b3184-0cce-3dde-8152-dcb1b791323d | -5.46988 | -42.89447 | 2025-10-06 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c3c3bc10-df09-338e-8c88-0a99753071a1 | -7.53433 | -46.82758 | 2025-10-06 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17275612-57bb-3a36-a05d-0d4506a61bff | -7.54522 | -49.92646 | 2025-10-06 04:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87232cde-eb48-3808-9a7d-afaf6a929b68 | -8.87359 | -46.83601 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81f8230c-7b75-36ec-b1b3-a094a6df5c64 | -8.55344 | -46.25202 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b891d6dd-2174-3832-a7a7-ba235b1adb9a | -4.71518 | -46.13928 | 2025-10-06 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac76a6cf-7686-3917-8ab1-7254684940b7 | -8.26064 | -47.0144 | 2025-10-06 04:25:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34c55511-d8b0-3ad9-b031-1fe570640b92 | -5.46139 | -42.7954 | 2025-10-06 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| da895920-cab9-3e07-afef-989214b2683e | -4.19533 | -46.45982 | 2025-10-06 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3934b14c-3753-3ab8-bff9-9a55f63f9f29 | -8.15684 | -50.06755 | 2025-10-06 04:25:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7fccc2c0-2216-3eac-af38-be94d8b1baaf | -6.65816 | -40.9104 | 2025-10-06 04:25:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 63af87fb-beaa-3745-992b-771ea112c4ff | -7.77893 | -42.62304 | 2025-10-06 04:25:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3f2789e4-5d3c-38c6-b669-3f8c3be1ce46 | -5.09748 | -42.62862 | 2025-10-06 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fdcc49a-3fbf-32e1-a58b-e16536b60e39 | -8.61185 | -46.26838 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5ad10ad8-b11b-3585-8724-212ad03b6b54 | -5.28082 | -42.92808 | 2025-10-06 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a2affd40-8e40-3790-86cc-54ca9590c932 | -5.2278 | -43.69993 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 18c25ddc-2a71-367b-9cf6-e54b10dda759 | -7.92415 | -45.98867 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 496873a5-84cd-37b1-98f5-33c05915af1f | -8.68703 | -49.94464 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a8e7d95-1fa3-31f8-8855-6395dc854cd0 | -3.94297 | -52.15604 | 2025-10-06 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96de12c2-d845-3996-8607-93c02a92e48b | -6.07143 | -42.54638 | 2025-10-06 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c7b135c7-1bb7-3ca7-9b63-2a275a275591 | -6.55147 | -47.8505 | 2025-10-06 04:25:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3924a20d-b07f-359b-92e7-2637beafc34c | -7.78694 | -42.59876 | 2025-10-06 04:25:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0979b31d-2e2a-3966-b54e-c48fd5526d99 | -5.25899 | -46.49358 | 2025-10-06 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d68b491-5468-34c5-9e85-9c8d173d2247 | -7.65722 | -46.63106 | 2025-10-06 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9795a434-55d7-353e-bc32-fbda1752c54c | -6.09135 | -43.99022 | 2025-10-06 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 488b7c00-de79-3fbf-a165-2acb74d356c4 | -7.42312 | -41.11932 | 2025-10-06 04:25:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| adfa32dc-5817-3e92-87bf-b9ac6b019501 | -6.7013 | -42.15897 | 2025-10-06 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 75678d7b-2adc-3272-b00a-bd246148ca82 | -7.72159 | -46.61295 | 2025-10-06 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f02b7e67-5103-3c37-b6b3-825171175df0 | -2.78242 | -54.41152 | 2025-10-06 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 96372898-bcfc-37e5-a707-d4e774221421 | -5.47766 | -43.25596 | 2025-10-06 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f253748-35fa-3a96-b999-33133ee58dc6 | -7.36316 | -45.2375 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bfdd43c-771b-3db5-9bbe-a5866ef86d37 | -6.66642 | -42.7729 | 2025-10-06 04:25:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 98644700-18a8-302c-8833-e66d48644119 | -7.2117 | -45.88722 | 2025-10-06 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8b721dc-99bf-391d-9bfa-46e0af0c585b | -5.26683 | -45.59585 | 2025-10-06 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af923dfd-d491-30dd-b6be-ebd38b086711 | -6.30666 | -44.46256 | 2025-10-06 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 96d35a6c-9c77-3054-92a6-ad3f21144513 | -5.47349 | -42.895 | 2025-10-06 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| af439ec3-3488-379c-a57d-bb3726f7ce0c | -8.61913 | -46.30867 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2eae6b56-fb20-3db2-8ac5-82cf2572ae45 | -4.89739 | -45.73522 | 2025-10-06 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da5f2220-b3aa-3adc-82f2-7511124a1e61 | -6.46582 | -42.04623 | 2025-10-06 04:25:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 078d4312-19cb-3756-8899-4bb34dd328a9 | -7.47786 | -42.62055 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 23588a68-60e5-3d6f-802d-b29c1c3d45ad | -5.79861 | -45.47741 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac9d0d0f-9eff-3adb-8335-dddd0d5fc6cb | -5.64651 | -50.30797 | 2025-10-06 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| faec1123-4c8b-320d-8af0-6705030c3a2e | -7.62962 | -43.06694 | 2025-10-06 04:25:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a72e6fa9-5dfb-33a5-9aca-1609b4cda1e4 | -8.51593 | -46.38504 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 134258c7-2348-3a73-ba8c-878722cb32f0 | -7.61997 | -46.67474 | 2025-10-06 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a194cefc-473a-369a-8dd3-9a3597efe364 | -7.73466 | -42.3974 | 2025-10-06 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ad56c2a1-60e8-3460-986c-8ce009a200cf | -7.05714 | -42.79033 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e25384aa-fd12-3695-83a1-8e8eedae6e2a | -8.34535 | -49.65524 | 2025-10-06 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3abba4f0-884a-30f5-8dd3-29fe06a6bea7 | -2.81579 | -48.61522 | 2025-10-06 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7d1066d-197d-3efd-bf86-8c2d0f482ddb | -8.19126 | -44.20693 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06290883-9ed0-3694-a7f8-2c774d6fc0ec | -7.71986 | -46.25161 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5889fa86-5a8f-3124-a4dc-2ab5c18a4e14 | -5.71211 | -42.62535 | 2025-10-06 04:25:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c7ccf22d-5e55-32fe-af3e-e91402c3193c | -5.79397 | -45.8378 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96a9af32-0892-3cf5-af04-60e540f5470c | -6.64258 | -41.98243 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 715f419e-4fb1-3c28-a4b3-6b2b5e9e241a | -8.95477 | -44.60185 | 2025-10-06 04:25:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbc1439d-8044-3541-8ee6-4c7f62687600 | -8.5125 | -46.35908 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 977e8337-1ecd-3c8f-8e45-1b11f16179bc | -6.57669 | -43.46016 | 2025-10-06 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65486366-db3c-334f-b5ec-605b7faa28dc | -7.25457 | -44.13369 | 2025-10-06 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 82cc479f-bb9f-3097-bbe7-f50f69c11b42 | -8.25932 | -45.86528 | 2025-10-06 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8ba9083-2b2e-3beb-b481-b9beb19f50c9 | -7.06018 | -42.79528 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8f8de7af-168c-3ca7-a8ea-24707cb21c05 | -6.55762 | -47.85518 | 2025-10-06 04:25:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| a999798a-4982-3cf8-9bf0-6e6fd76db87b | -6.24924 | -43.06231 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 280eb38f-c788-3619-ace8-fc9e11c0828d | -6.29057 | -42.93543 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c32b4b19-3207-3436-b22f-1bdfd59826ed | -6.56429 | -44.15743 | 2025-10-06 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12fb6cda-3bb9-31e0-a6d1-e89654411fcb | -7.59206 | -47.06728 | 2025-10-06 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dfc95705-c5de-373d-86f9-3dcee453c50d | -7.80087 | -44.13732 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d9a3925-d35a-3816-b6ce-d0d0d83aa159 | -4.70593 | -50.86148 | 2025-10-06 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fed5dd95-7e7f-3ada-a61b-6302307469a3 | -7.0271 | -42.76321 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a04e957e-8a49-368c-ac8b-73e3d2e0b4ae | -3.53963 | -54.07012 | 2025-10-06 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8e136cb-af4a-33b8-bf7a-c04ce54039d9 | -5.61232 | -51.80238 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ff9c8cd-fca0-357b-9fad-98b7e327db34 | -6.74564 | -43.99969 | 2025-10-06 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc08eb0a-e4c2-3bf1-9738-a7be27b28ed5 | -6.24732 | -42.77475 | 2025-10-06 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 50d28582-9705-31d9-9df6-2550178f9b8b | -7.36091 | -45.22985 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50d06a30-8c07-358d-b62b-1d5e47ee6855 | -7.61249 | -45.47235 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41119a95-311b-3582-918e-e567fd4e5f08 | -6.18149 | -42.71383 | 2025-10-06 04:25:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 57473945-5c71-3cc4-b4e5-8b213a9e7368 | -6.25146 | -43.88473 | 2025-10-06 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9fffa38-b74b-31d8-9d92-6b4a57cfd021 | -4.92945 | -48.09993 | 2025-10-06 04:25:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 213d5b16-2940-3771-8cbd-f266793a47c6 | -7.00136 | -42.83581 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 697fbfb2-55e5-354a-b5cb-7cf2ad866285 | -8.52346 | -46.33642 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de9cbed8-36ba-3639-9027-416e06120309 | -6.28332 | -42.93417 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4dff588-37b8-3b0c-8ad1-2798b2c91cd6 | -4.93986 | -44.58822 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 725c29a5-d47a-339c-97b1-407b2f9db767 | -6.66176 | -40.91475 | 2025-10-06 04:25:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 007a5bb3-323f-3dc7-87b9-fb94a8e59f06 | -8.53574 | -46.38816 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b7e5d82-2c0b-365c-9810-a356405353db | -6.61663 | -44.31886 | 2025-10-06 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 90234bd2-1067-348d-8742-a5d2598caeb2 | -7.46921 | -43.06436 | 2025-10-06 04:25:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README31.md)
