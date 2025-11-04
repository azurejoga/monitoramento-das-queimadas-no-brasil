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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7df1e47a-a162-3662-abbd-1e0976dffb89 | -7.85963 | -44.20976 | 2025-11-04 03:42:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc2928d5-5959-3e3c-9e20-87bc813fcb83 | -6.41696 | -43.07209 | 2025-11-04 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| dcb41616-42a5-3864-8803-94c0719eb407 | -7.06837 | -46.73281 | 2025-11-04 03:42:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e1544d22-5a96-3de2-8a59-3a1a4cc36d0a | -6.40593 | -43.06746 | 2025-11-04 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b0517a34-16ce-3236-a8bc-e4f176885676 | -5.23603 | -44.21075 | 2025-11-04 03:42:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1dc3f72-d019-3caf-8ee3-83cbf4ea3642 | -7.30028 | -39.35411 | 2025-11-04 03:42:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 66e762c9-88c1-302a-bc64-3e2d13e6f1be | -8.57148 | -39.25453 | 2025-11-04 03:42:00 | NOAA-21 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b07e2403-afc5-3200-98a6-e354b4902d97 | -9.85814 | -44.14405 | 2025-11-04 03:42:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f5d7271-360f-38b0-b790-a29eadd73db0 | -9.73981 | -43.86201 | 2025-11-04 03:42:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 99948cab-3956-30a3-87bc-e1684a6aacc0 | -6.41184 | -43.06251 | 2025-11-04 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8bc359a4-e564-314e-a9f9-576bd52a0fb8 | -6.12063 | -41.65676 | 2025-11-04 03:42:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0ba502e9-f0c6-3292-8844-806235acb475 | -6.06669 | -47.28613 | 2025-11-04 03:42:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9db385fa-05d6-382e-8829-fd8d63481a6a | -7.42723 | -40.72166 | 2025-11-04 03:42:00 | NOAA-21 | MARCOLÂNDIA | PIAUÍ | Brasil | 2205953 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 73b341b3-c7f5-3248-a74e-d676b21f2878 | -6.45897 | -37.514 | 2025-11-04 03:42:00 | NOAA-21 | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 22923201-ba7a-355d-83f2-c1a3112a626a | -10.86855 | -44.40848 | 2025-11-04 03:42:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1b3e2d70-fc02-3472-85e5-8ff407c655e8 | -5.75303 | -43.3931 | 2025-11-04 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab0691a5-5504-3333-9d44-e7992ef721b3 | -7.08324 | -38.82888 | 2025-11-04 03:42:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0b9f9a5e-2949-3344-92bc-8ebd88cc1661 | -6.76308 | -35.43074 | 2025-11-04 03:42:00 | NOAA-21 | PIRPIRITUBA | PARAÍBA | Brasil | 2511806 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 30e055fd-75eb-3f4a-addf-04c1bc8acb8a | -6.42287 | -43.06734 | 2025-11-04 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ff14ff7-e938-3490-9c80-f36df2ec80be | -7.7786 | -42.22038 | 2025-11-04 03:42:00 | NOAA-21 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| eea0cda0-a38f-3383-b88b-eb9cdee8da64 | -5.77953 | -40.80814 | 2025-11-04 03:42:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b6fbe0d6-a371-3116-8631-cb173d944c9a | -6.31892 | -43.80942 | 2025-11-04 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 557b2979-511d-3560-a312-c1c19085fce4 | -7.78392 | -42.21673 | 2025-11-04 03:42:00 | NOAA-21 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5046a144-caec-3399-8b1d-32c60d8cf65d | -5.36115 | -44.74487 | 2025-11-04 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f81f570-774f-33ac-ab68-6ab3b2e9d571 | -5.43097 | -44.66303 | 2025-11-04 03:42:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75809080-e69e-3815-b425-585efc6d3d63 | -5.84038 | -43.45235 | 2025-11-04 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef7385f8-c854-3c3b-8012-aea920f58a3e | -10.02211 | -37.38858 | 2025-11-04 03:42:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6d74f9ea-2d05-3690-9258-a91cf47d7877 | -6.10309 | -41.70475 | 2025-11-04 03:42:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a040e44d-6d9b-390a-994e-8d45c5f84109 | -5.93356 | -41.29749 | 2025-11-04 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6cfb2507-f66e-3730-92e3-199a98cf8d06 | -5.98577 | -41.91987 | 2025-11-04 03:42:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e44c2c79-f80e-31db-9dd1-c947b0768307 | -5.58086 | -43.79614 | 2025-11-04 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c8179ec-c7b3-3af1-be29-8b65211134e5 | -5.65274 | -44.06946 | 2025-11-04 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 468c0a14-3f44-3eef-9967-e3e30f00c702 | -5.9278 | -41.33234 | 2025-11-04 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5f195213-94ab-3e9a-b44c-9455cd791e89 | -5.23058 | -44.20996 | 2025-11-04 03:42:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24a488c0-835b-3702-a763-f1366a590c10 | -10.71974 | -40.15417 | 2025-11-04 03:42:00 | NOAA-21 | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eeb0900d-51cf-395f-8440-488de889ad91 | -8.57304 | -39.25745 | 2025-11-04 03:42:00 | NOAA-21 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c7fcf96a-b2af-3432-8692-4e09faaf1482 | -11.28013 | -41.7448 | 2025-11-04 03:42:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8cc04810-353a-36fe-81b7-c1e7be299b55 | -5.36536 | -44.74136 | 2025-11-04 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d04bcdb5-7ce5-3064-8e97-a00285a9c48f | -6.41793 | -43.06654 | 2025-11-04 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| eb596f31-116f-32a5-b57e-f9e1c14d2406 | -8.20769 | -39.34266 | 2025-11-04 03:42:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 60a4eb81-5e91-34f3-a0f8-4ab5a5a4756c | -5.93359 | -41.29607 | 2025-11-04 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1dbde0b1-dc51-312e-a697-abe64d4e75bb | -6.69743 | -39.6839 | 2025-11-04 03:42:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 40114f54-5531-3444-aac4-ee48c30396cf | -7.16596 | -40.08642 | 2025-11-04 03:42:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 14081aec-cce9-3b1e-9be1-298d3ed8eb1c | -5.23233 | -44.2088 | 2025-11-04 03:42:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5e88bd4-de32-322d-b893-8085c99f7f62 | -5.28064 | -44.61118 | 2025-11-04 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbb84ef0-1a4e-331e-84cc-d77c2c150870 | -5.89269 | -42.91468 | 2025-11-04 03:42:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 068971d6-896c-367f-9a57-d722c0392677 | -6.84358 | -46.30444 | 2025-11-04 03:42:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 51d0d518-6a50-3041-8014-523f60e3573b | -8.1099 | -43.81996 | 2025-11-04 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 89d3de92-fbf9-313b-a0d0-5b0d1b11b33f | -8.11109 | -43.81872 | 2025-11-04 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8ecb4136-2f0d-338b-bf9b-7132c5fe2fed | -5.2426 | -44.21402 | 2025-11-04 03:42:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 306cf023-a7ef-309f-aca6-5833c171823f | -5.92486 | -41.32272 | 2025-11-04 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cdc368f9-166b-3096-b120-904237fe1079 | -5.37095 | -44.74239 | 2025-11-04 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6c25f1b8-50cc-3ac1-b8c1-963239a1e3d5 | -5.61817 | -45.97926 | 2025-11-04 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 2022f6ca-9c0d-356d-8a31-439e88688001 | -7.16537 | -40.0899 | 2025-11-04 03:42:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b443507f-5e38-3300-bd3a-51ce230a6540 | -5.89524 | -42.91915 | 2025-11-04 03:42:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e84c6b15-5a18-3f7d-b708-931f0c22e8d4 | -8.10938 | -43.82281 | 2025-11-04 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9244d942-bdc6-36a4-9c9d-df2c55c7e395 | -6.70637 | -43.56876 | 2025-11-04 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46b42007-bf81-3a80-a4ec-9bfa7c1592ef | -6.6091 | -43.76189 | 2025-11-04 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d16edfa-e477-3567-83f3-c0f90cf15041 | -9.85315 | -44.1431 | 2025-11-04 03:42:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d0c33b8-bf64-3f5e-bb44-efe94fdb8c0b | -9.99947 | -37.67989 | 2025-11-04 03:42:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e519add1-f206-3782-bf63-d445d0b8b8cb | -5.85906 | -43.99846 | 2025-11-04 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b55a4f88-60b0-3f46-8c41-d63405d0f26a | -6.41398 | -43.06015 | 2025-11-04 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dacef9c6-7e96-3622-b97a-1d392e8bd967 | -6.412 | -43.07137 | 2025-11-04 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c65bf926-0657-3276-a4f8-09541eb3a4cd | -10.72877 | -44.01701 | 2025-11-04 03:42:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8de3209a-fd92-3261-a9b1-02da2e007a8d | -10.94358 | -44.19555 | 2025-11-04 03:42:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca1d37c3-2002-312e-93fb-8791d8cf9de6 | -5.92845 | -41.30101 | 2025-11-04 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f118da07-a59e-3ab4-8a4c-d78b654c2d4a | -11.11118 | -41.62506 | 2025-11-04 03:42:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ef4c2671-60f5-39b4-8e94-4ef1ca9ddd06 | -5.0625 | -45.90758 | 2025-11-04 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 0332ada2-2576-3631-a4e7-bf39b68d7705 | -6.85614 | -35.40282 | 2025-11-04 03:42:00 | NOAA-21 | GUARABIRA | PARAÍBA | Brasil | 2506301 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ae467c51-0f22-3616-a516-e31eba015a09 | -10.93763 | -44.20027 | 2025-11-04 03:42:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0279a59d-4cd8-3f7a-9464-f85e2bbd27a4 | -5.23661 | -44.20732 | 2025-11-04 03:42:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35e43e0d-1ce4-3a2b-8df5-cf085430003e | -9.31689 | -43.09843 | 2025-11-04 03:42:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cc6d2afb-cae0-39ae-ad22-e480e7b98a8c | -7.06743 | -46.73785 | 2025-11-04 03:42:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e62ec802-c38e-3794-b07e-908a5c817619 | -5.7525 | -43.39613 | 2025-11-04 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5b3a12f5-f785-327f-b5dd-63ed9d11a9ff | -11.17904 | -41.7995 | 2025-11-04 03:42:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| cf8c97d7-1526-362e-9308-c15f48085089 | -5.23778 | -44.20961 | 2025-11-04 03:42:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b9471b1-05d1-313f-8135-f2dc2044f85e | -6.78317 | -38.32473 | 2025-11-04 03:42:00 | NOAA-21 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1c02457d-d21e-3151-90fa-bd10de707dd0 | -5.83199 | -44.09075 | 2025-11-04 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7b93bab-f35c-3b9c-ad8d-128f47d7c8d6 | -7.01111 | -37.27813 | 2025-11-04 03:42:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ce4f3e1d-5ec4-384f-ac61-e00a3caebdb2 | -7.16574 | -39.50873 | 2025-11-04 03:42:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 85f51471-296f-34b2-8098-1e7fd9c2d75e | -5.57613 | -43.79218 | 2025-11-04 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8c97cb0-880a-33a7-aa68-c7d4ddaa69d6 | -5.30351 | -44.81059 | 2025-11-04 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c0947c8-7941-3f0a-b247-9aa239eba10c | -6.46755 | -43.22198 | 2025-11-04 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6825f9e9-00c0-3276-b8d5-2e953d2adcae | -6.14921 | -44.58199 | 2025-11-04 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d746df1-dca0-3675-8b6b-5768bca31ea9 | -5.3244 | -45.37856 | 2025-11-04 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85e206e9-f9c7-3f0b-9846-a060a8c623db | -5.23294 | -44.20534 | 2025-11-04 03:42:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a2197d3-4a01-32b0-a22b-c4064a76d7c5 | -6.10009 | -44.44021 | 2025-11-04 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abd7a6cf-e4e8-3b8d-8dcd-ae6a56f64261 | -5.83676 | -44.0635 | 2025-11-04 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8f7827a-fe48-319f-b5f1-f345f77964af | -5.36603 | -44.73753 | 2025-11-04 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cc934bb-ac97-338c-afdd-4bc11f2c5056 | -5.61896 | -45.97477 | 2025-11-04 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 000960ec-5b39-385b-b22c-7c74fb732884 | -7.60546 | -43.0096 | 2025-11-04 03:42:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| db655339-53cd-34ef-85b2-b754ddaf3606 | -5.92559 | -41.31831 | 2025-11-04 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 23bac233-1e92-38e6-9496-6817a7e9da32 | -6.48827 | -39.41824 | 2025-11-04 03:42:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9bb87310-c550-34d9-99b3-f8dc1b41ae96 | -6.61165 | -43.6129 | 2025-11-04 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9cc9b624-301e-3172-8e95-bf0175a3fd21 | -5.3237 | -45.38263 | 2025-11-04 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f8ab39c-aa81-34d6-9a36-f288c4482ecb | -6.13483 | -41.54736 | 2025-11-04 03:42:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4c8c5692-6d55-37fe-a2db-1f5a1ff7a4b6 | -7.6066 | -43.00775 | 2025-11-04 03:42:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b6a674ac-193e-345a-abb7-74548eb846f2 | -8.10927 | -40.78845 | 2025-11-04 03:42:00 | NOAA-21 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b33d079e-6532-3fb3-9202-d96e1dc147ad | -11.27946 | -41.74864 | 2025-11-04 03:42:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6f352c36-d516-35ee-be73-821ca7188aa8 | -5.92758 | -41.33079 | 2025-11-04 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README9.md)
