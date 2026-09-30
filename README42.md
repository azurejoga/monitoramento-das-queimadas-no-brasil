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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a50f9e8b-0a20-3431-91c7-fe306b65924b | -9.96846 | -47.98341 | 2026-09-30 04:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff6f8314-b5ff-3118-aff9-9662c108a590 | -16.41987 | -43.30117 | 2026-09-30 04:53:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0bd396d-465f-352c-9d1c-56da2f62898c | -11.63134 | -43.53271 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 556f53ed-d4af-3b2c-9bcf-1b0dc40c448e | -3.38238 | -50.95969 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af6ac355-9549-319f-9e48-3a857ce8f8fc | -3.01363 | -53.8768 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a411da81-8560-3048-a871-142e05e8342b | -11.18241 | -44.84229 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6362a924-13c2-3b70-910b-5af858bacd24 | -3.38293 | -50.95624 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1991fe33-6b92-3482-8ae7-45e38cc73184 | -8.48481 | -54.90776 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8bb396c1-8702-33ea-8646-beec5b3c35e2 | -3.82852 | -52.20553 | 2026-09-30 04:53:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c2b6147-f75d-340d-a0a8-2126e2af7a12 | -7.83565 | -45.8189 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4e5b6353-eece-3f1f-90b2-ed5e6f1bbb08 | -4.02519 | -54.19601 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1025912e-cc60-3664-beae-09c5310d4e32 | -17.10492 | -46.47205 | 2026-09-30 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e4c23c8-839d-38cf-b664-f7c7fa6223b0 | -6.33606 | -55.32996 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92a1339d-badd-33fa-adb8-023f0baaa7ec | -8.25117 | -45.44496 | 2026-09-30 04:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52f913f4-cce8-3c85-8b6c-65cded41e5c7 | -9.82375 | -48.20358 | 2026-09-30 04:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae47dd3d-d1cd-30aa-9fb9-4e40bb083080 | -5.8168 | -46.21754 | 2026-09-30 04:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82cea8ba-0083-3508-bf5a-a6240d99c2ff | -8.31469 | -54.75772 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 064bf530-42a4-3791-b1d0-49d6f3bec5b2 | -11.263 | -43.52585 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dabd05f-e4c9-3d06-a25a-0b0005e2eada | -4.02882 | -54.20265 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32afd233-9a10-385b-952e-a92737678f76 | -14.13039 | -46.26159 | 2026-09-30 04:53:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31b93d8f-ea5c-38a0-a6d9-ffb5593c5e9a | -10.57847 | -50.84827 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 971597f5-b094-3ca9-9c27-581b7b6daa39 | -5.73431 | -45.16581 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 95403888-fbda-39f8-bc04-5dd19ebe49d2 | -6.296 | -43.65302 | 2026-09-30 04:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 868d98fa-6148-3675-8108-081e56a44bb1 | -10.90761 | -43.8511 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c31945a-0173-3527-bc05-dfb4bac5fc5e | -2.86491 | -54.12252 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b71055c-80aa-32e0-9773-9b72cf95d312 | -3.18103 | -51.2435 | 2026-09-30 04:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 98a83341-103e-3608-b211-0ab2007969b3 | -15.83534 | -42.56038 | 2026-09-30 04:53:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| df449e3f-673c-3c46-8801-9c56429ae20c | -4.4793 | -43.65647 | 2026-09-30 04:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 442cca0c-adae-3561-a2b0-d6435c8bfbd5 | -11.41123 | -43.41697 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 975c6307-86d0-3ef4-a11f-b7fe92a486aa | -2.89308 | -54.11339 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1900f3d5-fad0-3936-a4eb-9c5a4810ff03 | -7.84407 | -45.82025 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b09987a-495d-3512-a58d-b52e0f67e1de | -6.79099 | -55.81777 | 2026-09-30 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60461c89-4e99-3eb7-9523-d0e251a618ff | -6.16521 | -44.61709 | 2026-09-30 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 853427dc-488b-31ba-84f2-30375a2c39c9 | -5.75512 | -45.17273 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| db1e894e-2c42-3c71-8d1e-759d023774a6 | -8.12219 | -54.85268 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ba750b9-8fdb-372c-9a85-591d90ec41c1 | -3.38181 | -50.94191 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6d441405-d186-3c6f-85c0-e26a9e6f2ef1 | -6.30296 | -43.60194 | 2026-09-30 04:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 93b64c08-3bd0-3b36-b004-93bb28d3055c | -7.47671 | -45.79321 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78ff9b24-43e3-395d-991a-00e49946d8fa | -3.86024 | -49.74334 | 2026-09-30 04:53:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28381c1c-16fd-3030-9926-2d9d228bc91b | -3.0057 | -54.22983 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a95923d-3edd-3fe5-b0d5-0b6162eb8726 | -6.33353 | -51.15939 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 40c9a4b9-15b3-3ea8-943b-aa6c2515e2b6 | -3.01293 | -53.88106 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cd9efef4-20d5-3f8f-bf3c-a7bd15205ade | -14.52942 | -48.2924 | 2026-09-30 04:53:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0ab49023-431e-3f7b-8a8a-2377a8bc8847 | -6.19394 | -55.54474 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f829b18b-bee5-359d-beba-b27687c899c8 | -10.77408 | -47.25284 | 2026-09-30 04:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43bf5e9c-58c1-3a26-86e7-af8662617aa5 | -5.84185 | -50.14175 | 2026-09-30 04:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1251850-e19d-3359-98bf-2f4cb5778895 | -11.16367 | -44.76624 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2171917-4760-34a4-ad3d-9d44004ec095 | -6.12726 | -53.28509 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b902c0e-a3cf-30d6-a8f2-2ca766fa161f | -4.02212 | -54.19738 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90f6da77-3d5b-33e1-9092-f7d364c218c6 | -6.72989 | -45.61556 | 2026-09-30 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a2d5cbbb-8c89-3306-b93a-029b1b90cf0b | -8.3672 | -45.38718 | 2026-09-30 04:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8f392db-2503-37a7-bbaa-63f3324184a3 | -15.20367 | -46.14367 | 2026-09-30 04:53:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e271f613-7a60-326c-9f1b-68878f946896 | -4.80997 | -45.64541 | 2026-09-30 04:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed768d50-016a-3ce2-8e23-e07f3b45eb9d | -16.67614 | -41.85534 | 2026-09-30 04:53:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 5c232770-afb5-3d2f-aae9-d18732500144 | -9.27817 | -46.41399 | 2026-09-30 04:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd2e18a6-04e6-3bce-928c-5a9df2d221a9 | -10.52508 | -50.75821 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46e730e1-e65a-3752-bdc8-51e48a1e7609 | -6.1623 | -44.61863 | 2026-09-30 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e516ef4-76a2-357c-9fb8-449386ae47e9 | -15.77644 | -46.02855 | 2026-09-30 04:53:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 45e566e5-3145-3581-ba65-1969603e2150 | -11.16688 | -44.81428 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0473b1b7-5ff0-3294-a595-6d040ba91d6c | -8.98612 | -44.17366 | 2026-09-30 04:53:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8afee9f7-28c0-301c-83ea-adefb1a31156 | -6.19588 | -55.54874 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5d0f1dc-78da-39c2-af6c-ca79c086b91c | -11.38389 | -43.37902 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1ef3ed8-db25-37b1-9425-64197ea491b1 | -11.31964 | -47.75219 | 2026-09-30 04:53:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 630a6546-4fae-33e4-915f-30a6bb9d1f30 | -9.70497 | -46.71308 | 2026-09-30 04:53:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66ebc389-8416-3701-bf37-0962c2a47bd7 | -14.91681 | -51.86805 | 2026-09-30 04:53:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 115c8977-065e-36f0-bad2-50272652a8a0 | -10.71297 | -44.42435 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c3ac3e3-80a0-35db-aa8f-b135f4987703 | -5.55796 | -45.33518 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5904c91a-4915-3f0c-b23d-442ba0e25a05 | -6.12787 | -53.28129 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb26ba59-eb0e-3194-997a-30584c5208b7 | -17.12732 | -52.13257 | 2026-09-30 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d305c63-1f14-3428-97f9-aabfac0bdd64 | -8.88648 | -47.87813 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 273d041c-d676-36fe-94a1-2ccd39f6c971 | -3.14552 | -54.0831 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b146d32-df2c-35e8-a47a-02d583d680ea | -8.26198 | -54.75458 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb256c4e-5d0a-31bb-a2ff-c828e0ce5aa1 | -6.07164 | -47.28161 | 2026-09-30 04:53:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 7255cea1-4479-394b-aabe-00c365289f0f | -15.20542 | -46.13019 | 2026-09-30 04:53:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 319b2d16-cd6e-3bd3-b070-1f57528d176a | -5.09214 | -46.04213 | 2026-09-30 04:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96c782c1-30a4-3bb4-aa8e-819a0f58ae21 | -6.29564 | -43.65469 | 2026-09-30 04:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| ac18e8fc-1c37-30a7-ac2a-85e552e4e3be | -7.1893 | -46.50824 | 2026-09-30 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 966c89a2-6068-3e01-8f4d-018745ca5c9a | -4.11839 | -48.81768 | 2026-09-30 04:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d3f3d3e7-6ae3-3f7b-aa0d-ad5ebf7f9908 | -6.11485 | -55.70149 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e30dd029-36a4-3aee-8b99-c9c166887603 | -8.83473 | -49.70698 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0e3940ef-634f-3832-b25b-3f7b0dbc9841 | -10.4225 | -53.77217 | 2026-09-30 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 313b477c-c482-36d4-8939-8f545e7b70be | -18.07751 | -44.36354 | 2026-09-30 04:53:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce24b947-de9f-3e5a-8961-907787b11549 | -9.08699 | -49.88692 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e606194-a81b-3905-b345-33080b1b28f8 | -6.72656 | -45.57958 | 2026-09-30 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cb7de58b-e57f-31ae-a0a5-d0e86432da73 | -9.41652 | -51.72629 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a5071bd-fdc9-3155-9588-43920673d35c | -16.64868 | -49.38981 | 2026-09-30 04:53:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f14ab47b-94a1-3a30-940b-8c4f7e7dc94c | -5.02796 | -43.56894 | 2026-09-30 04:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dac534ee-0e4e-3ca0-ba2a-e1af58525ea8 | -10.28823 | -44.64169 | 2026-09-30 04:53:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6b392e60-6cd8-30ec-89c9-0185512ab1cb | -9.81492 | -48.21164 | 2026-09-30 04:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da677842-810b-33dc-bbdb-8185ef33bd50 | -8.60656 | -49.45531 | 2026-09-30 04:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 93fc7ffb-5861-3f16-8291-0a77d369a23e | -9.06697 | -51.53058 | 2026-09-30 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0c342d2-5b17-3ff3-8844-d48018907056 | -5.74228 | -45.17096 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ff0926b-a2a9-3a91-982a-73539c7516e3 | -7.02426 | -44.62168 | 2026-09-30 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 838e776a-e743-3950-8125-0d8d46684182 | -8.95379 | -49.79802 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d36bbaf7-9626-35a8-a0b4-3a990e5f22ea | -8.2828 | -50.2682 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5176e676-f4ed-3ba2-b650-fc841c849d14 | -7.50632 | -55.03897 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bafb4967-3c3e-31e0-8c77-84637468159c | -10.41451 | -53.77838 | 2026-09-30 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fbef120a-f34e-3b14-b8da-f91ef52ae81e | -2.88185 | -54.87544 | 2026-09-30 04:53:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9bb6d310-f19f-3a29-8f71-cad0197c7d4f | -15.37585 | -47.9181 | 2026-09-30 04:53:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7006ed2e-fcdc-3c48-8387-ce062a282d29 | -10.82922 | -48.6983 | 2026-09-30 04:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README43.md)
