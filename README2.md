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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07f47bf0-a7b3-3de6-9c17-44db9f5d8a1a | -1.64408 | -45.85863 | 2025-01-03 03:59:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4769e1d8-7304-3e5f-aff9-7d3b4d548370 | -3.05806 | -39.92801 | 2025-01-03 03:59:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ebd8a610-8722-3da4-afd4-4a0fe63d419e | -1.37537 | -45.86048 | 2025-01-03 03:59:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59b31189-c1a0-3cba-8aca-b98dd7437187 | -1.77508 | -45.92076 | 2025-01-03 03:59:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 629a7be5-4e5d-38b6-a8c9-046e3fe3302c | -1.81465 | -45.90783 | 2025-01-03 03:59:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 877e5963-a060-3466-90a4-e6b1c2d4183c | -1.64682 | -46.13158 | 2025-01-03 03:59:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1082fd54-d288-3a56-9901-b3ea31bb93a1 | -1.81391 | -45.91249 | 2025-01-03 03:59:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c3822118-297e-3955-8f7d-52b866a05b2b | -3.00775 | -40.22616 | 2025-01-03 03:59:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9197c5d9-5332-38f3-a9b2-73d256f833c3 | -2.92809 | -41.23839 | 2025-01-03 03:59:00 | NOAA-21 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1e83ccb0-cc2d-3ab9-b442-bb68dbb63b4f | -5.50583 | -44.82903 | 2025-01-03 04:01:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa1e4289-f046-3924-a97e-2ead4d281fe9 | -10.99121 | -37.27528 | 2025-01-03 04:01:00 | NOAA-21 | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| a47efc27-7ac4-3c5d-8ef4-ec900224db5f | -4.16598 | -42.02415 | 2025-01-03 04:01:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0bd540e0-908b-3dde-a9bd-843088c9a858 | -5.18835 | -37.63809 | 2025-01-03 04:01:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| fc34143c-a6ea-330d-adf4-14582c751f23 | -7.56745 | -39.03413 | 2025-01-03 04:01:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 77e1a54a-d086-3a8b-ba7a-bed8839bef05 | -6.91791 | -38.72171 | 2025-01-03 04:01:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 18ee4b99-9405-3681-b8d0-a82bddbbb856 | -9.02396 | -40.26219 | 2025-01-03 04:01:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 66544ff4-e7ca-3e78-b918-d5c7beeea770 | -7.76625 | -38.80651 | 2025-01-03 04:01:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 63f92569-648c-329e-abbe-d05aee0bdbc8 | -4.75361 | -44.25371 | 2025-01-03 04:01:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f102f7ae-501a-3fe7-837e-d94365c19e75 | -6.75852 | -35.06456 | 2025-01-03 04:01:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ddf30a02-e019-32c4-846d-fe433d697208 | -3.86511 | -40.35688 | 2025-01-03 04:01:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 467ad539-1943-305f-bc9f-0959a8f57882 | -5.97155 | -44.29249 | 2025-01-03 04:01:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df9af00f-d635-31b2-b9f3-36e755417e05 | -5.18258 | -41.53106 | 2025-01-03 04:01:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| df1d32e6-7cf6-39b4-8b66-22bcc7ed5f21 | -6.60695 | -39.11435 | 2025-01-03 04:01:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 892e41d5-1cfb-301d-868b-5a80f90d2e89 | -5.92633 | -43.78777 | 2025-01-03 04:01:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7194c9d8-7a05-3e55-89b2-aeb675a760f7 | -3.97689 | -40.9189 | 2025-01-03 04:01:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 39ff976e-bbf5-3c3b-8420-9db27d0ba7fc | -4.1625 | -42.02359 | 2025-01-03 04:01:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 99a01f4e-01fa-3dc5-8727-ed62e2b53d14 | -6.97889 | -43.55021 | 2025-01-03 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f0a99a90-0041-3294-a5bf-a5155f130c85 | -5.2312 | -41.03957 | 2025-01-03 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 48048aa5-7b4d-3a93-8367-df83a3d93bc1 | -6.97456 | -43.5539 | 2025-01-03 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2d1d793a-2540-3dba-a97a-871d6f1eb635 | -9.1841 | -43.11885 | 2025-01-03 04:01:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f7ee0c20-6836-359d-9ee5-9eecbc1f6d83 | -5.50183 | -44.82836 | 2025-01-03 04:01:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8892750f-3835-36f6-b325-fd19ccc624c0 | -10.79746 | -37.27462 | 2025-01-03 04:01:00 | NOAA-21 | AREIA BRANCA | SERGIPE | Brasil | 2800506 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 38f4b028-114e-36b4-aad6-a1bf42d1eea8 | -3.71496 | -43.77524 | 2025-01-03 04:01:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4dc08bc8-30ee-3287-ae04-37c6b70dd623 | -4.80498 | -43.30215 | 2025-01-03 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0b2ec212-046a-3fd2-b002-2259f31e76d6 | -2.43353 | -45.76746 | 2025-01-03 04:01:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e5d2eb2-ba7b-3ba2-a66c-2f013b1f19a1 | -6.56834 | -39.0326 | 2025-01-03 04:01:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 076b7e4f-6096-3cf4-a5f3-86dd05c985d1 | -10.29222 | -37.53569 | 2025-01-03 04:01:00 | NOAA-21 | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 9a2b528d-abd4-3a69-9cf1-98eb0758d214 | -3.90608 | -47.05066 | 2025-01-03 04:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e545e556-94fd-3964-abef-58d22abaf85a | -9.27084 | -35.61891 | 2025-01-03 04:01:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4f66414c-bf19-336f-9395-146a6b70d1b2 | -5.62757 | -44.83557 | 2025-01-03 04:01:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a0e0bcbe-30f4-3d33-a479-8e1215c94ab2 | -3.90512 | -47.20674 | 2025-01-03 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d405eb2-aa23-3f06-ab12-ddd801002ae4 | -5.70352 | -44.79773 | 2025-01-03 04:01:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68eaac70-130d-3a38-b391-b934cb9b5ca6 | -6.69469 | -43.0639 | 2025-01-03 04:01:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ecae0ba-99be-3dd2-b447-9f0860cbee56 | -9.87344 | -36.2881 | 2025-01-03 04:01:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d7317f96-e6d6-343e-a83d-93b7e04759b6 | -9.17203 | -43.14878 | 2025-01-03 04:01:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 17810dc5-fe21-36f3-8d0c-5166fb883453 | -6.75878 | -38.72295 | 2025-01-03 04:01:00 | NOAA-21 | BAIXIO | CEARÁ | Brasil | 2301802 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3790a184-05a8-3f28-9f70-72a150528e6f | -4.52465 | -44.39706 | 2025-01-03 04:01:00 | NOAA-21 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40420398-a992-33f4-850b-b169da38f024 | -6.23975 | -39.62064 | 2025-01-03 04:01:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6c732f86-f420-3f24-8b70-f1a0fb8c9c36 | -4.16126 | -42.03135 | 2025-01-03 04:01:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 8e86d640-3374-35ec-bd9d-93b6a74118f0 | -4.80867 | -43.30274 | 2025-01-03 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b21436c4-9e77-3778-a1ad-082508d6f5fd | -5.02031 | -39.71442 | 2025-01-03 04:01:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| afd5288d-f37c-38d8-bab2-56c57f77abc3 | -9.56303 | -38.28801 | 2025-01-03 04:01:00 | NOAA-21 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9ec72d65-9a12-3be5-9307-73c907879b98 | -3.00832 | -46.70681 | 2025-01-03 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a4d7774-d851-3b6f-8955-4b180606a334 | -5.67362 | -39.62695 | 2025-01-03 04:01:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b68b8661-21a7-3374-9528-a40a9419d48a | -5.70603 | -44.95969 | 2025-01-03 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f5c3ffe6-e409-3ac6-9818-b113bff6854e | -7.1818 | -39.66243 | 2025-01-03 04:01:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f5ec585c-416e-39e0-b30d-b7bfda7cb2c1 | -3.27004 | -43.51943 | 2025-01-03 04:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2669f24-f781-320e-9acc-1aa1a3897f38 | -5.04749 | -43.62023 | 2025-01-03 04:01:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97519a20-b349-397b-abaf-8d92a2ead72a | -7.04025 | -37.31948 | 2025-01-03 04:01:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f14510ee-fa8f-30c0-8c49-4c9df9075909 | -7.72954 | -40.25245 | 2025-01-03 04:01:00 | NOAA-21 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 286a5715-9fa3-3021-9917-2644c192d25c | -9.56361 | -38.28412 | 2025-01-03 04:01:00 | NOAA-21 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 26d6c50b-6172-37de-bfe1-e4708dc999ac | -7.81204 | -35.23193 | 2025-01-03 04:01:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0a83cd0e-5e48-3b8f-b33b-788541ed6ea4 | -6.39375 | -39.91685 | 2025-01-03 04:01:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6f0f31b6-2c1e-3257-84ba-e70ef0892670 | -4.16536 | -42.02803 | 2025-01-03 04:01:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| e8eb4008-a0d9-319f-a284-5ff502f7704a | -5.92259 | -43.78722 | 2025-01-03 04:01:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33ec6ac0-8bc4-334b-b6a1-81d667f41bc7 | -4.82751 | -44.02102 | 2025-01-03 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 603af4fa-b7ad-3d4d-b934-b2601f3108c6 | -7.08034 | -35.28043 | 2025-01-03 04:01:00 | NOAA-21 | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d190c8e4-2e85-3414-9537-a32e4b3f0a67 | -4.87585 | -39.04882 | 2025-01-03 04:01:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3a23104a-c89d-3757-99f2-4767cbd47987 | -7.039 | -43.96517 | 2025-01-03 04:01:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 000ddd66-8ebd-3746-8c42-5e05e549d90f | -3.68841 | -38.83207 | 2025-01-03 04:01:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1cc1b031-436a-333e-8ee6-2d3217aae447 | -7.47602 | -35.0506 | 2025-01-03 04:01:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 00e16ca3-ce39-3ae9-8c95-cff44fcdeca8 | -8.43338 | -40.538 | 2025-01-03 04:01:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4227a845-fadb-3d5d-99aa-26aa7c77b91c | -5.70708 | -44.96004 | 2025-01-03 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f50c524-c724-3773-97bb-f927322a3f72 | -6.97091 | -43.55333 | 2025-01-03 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f2810669-7dcc-35aa-9a7d-59cca5244d50 | -6.48683 | -43.11536 | 2025-01-03 04:01:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ba0fde9-8869-30e6-9933-a9f1bf4569c7 | -9.30742 | -41.06212 | 2025-01-03 04:01:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe04d771-2bcb-30b4-bb2a-731d1c43efa9 | -4.74233 | -41.82294 | 2025-01-03 04:01:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4c58711e-6be8-3e00-a164-d7f7c1faf9eb | -3.46267 | -39.58226 | 2025-01-03 04:01:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c0743ec3-1a7e-3c35-98de-b01cad869c89 | -3.48874 | -39.50194 | 2025-01-03 04:01:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f9af1824-9c58-326d-907f-7e3540c7a30e | -10.78956 | -37.25031 | 2025-01-03 04:01:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| eba2d5de-7221-3103-af60-5720bfeca5ab | -7.13571 | -38.94535 | 2025-01-03 04:01:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| e0c23b34-53f5-3188-808e-1ea5d13f0811 | -3.98025 | -40.91944 | 2025-01-03 04:01:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 102b0d9b-4f0e-3e55-b769-c0ea53248186 | -8.07548 | -35.13564 | 2025-01-03 04:01:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a4e4718e-27de-3c80-921c-a793cefe7fac | -7.67871 | -40.5561 | 2025-01-03 04:01:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 432061c7-c501-3044-bddb-deb7281adaf7 | -5.63158 | -44.83617 | 2025-01-03 04:01:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c2564922-e3c6-3efd-9155-432f01fc95ee | -4.7389 | -41.82239 | 2025-01-03 04:01:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 17d989f3-29a2-3c58-887f-b4dbc5a4891c | -8.07494 | -35.13935 | 2025-01-03 04:01:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| eb387833-c1e8-3bfd-a483-96c314ae95ec | -7.76962 | -38.80703 | 2025-01-03 04:01:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c01aa258-81ff-399d-9936-afe1f6d934fd | -2.30358 | -46.41169 | 2025-01-03 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18f1bc2f-0e45-3598-8486-cd3ba2c7397f | -3.67633 | -45.22191 | 2025-01-03 04:01:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c56a114d-8b28-3e2c-a8ee-f8c0969c6c1f | -10.77307 | -40.36288 | 2025-01-03 04:01:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| acef8ea7-653f-3f9d-81a5-f56862408cbd | -4.89681 | -40.82779 | 2025-01-03 04:01:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d6c35994-0b17-3600-a799-446e9fe29f17 | -5.1535 | -38.48456 | 2025-01-03 04:01:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 3e57b249-3309-3e9e-bcc0-a51ac60ad60b | -7.20833 | -39.73397 | 2025-01-03 04:01:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d34db910-e48f-3e0d-9ac9-8f5c75dc4452 | -7.20502 | -39.73344 | 2025-01-03 04:01:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6125942f-e704-3d11-8ba2-a26583b5772a | -8.07085 | -35.13874 | 2025-01-03 04:01:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5a3c2c71-6b62-32e3-b0cb-41e7c29f244b | -4.89347 | -40.82727 | 2025-01-03 04:01:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ebe00831-fc0e-3455-8a65-addcbe7d184b | -4.80057 | -43.30595 | 2025-01-03 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92826263-976f-3ccb-8605-32a5ced3b620 | -10.99186 | -37.27073 | 2025-01-03 04:01:00 | NOAA-21 | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4b1a16f5-9879-3acf-806f-f4d2590c041e | -6.16348 | -43.16386 | 2025-01-03 04:01:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README3.md)
