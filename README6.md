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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 951818dd-e8b6-3628-9cb5-31ec59d350b7 | -13.30446 | -45.22322 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f89ab422-228c-3491-a76f-6a7caba374d8 | -12.55445 | -45.01973 | 2026-06-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1071e514-bbcc-3422-83ab-64337140205d | -13.29973 | -45.21435 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66946060-ed2b-3c51-9557-45a7f1ec6b25 | -12.79022 | -44.48168 | 2026-06-20 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| defa3db2-3b2e-36ff-807e-3f47321b01a3 | -10.76947 | -54.10788 | 2026-06-20 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 37e1a011-3b5c-3717-a76c-58d197ce492b | -12.78901 | -44.48908 | 2026-06-20 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0e1177f-d590-345f-b1b5-13ca096bff2d | -12.79142 | -44.47429 | 2026-06-20 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8be46591-e316-3abb-b7ec-e6edd4644389 | -13.11502 | -53.78565 | 2026-06-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 135144b9-5162-311b-bd5e-115ff879522b | -13.29691 | -45.22596 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72ba26b5-002c-3315-9b9a-1c8b2a823c68 | -12.78745 | -44.47742 | 2026-06-20 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0a82e96-9237-341f-adc6-b0d7a01d3df5 | -13.13815 | -53.78859 | 2026-06-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 91a68e0c-d50e-3406-9644-a6ca32fe1e2c | -13.30036 | -45.22652 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a179d607-2077-3723-b1ce-fd467176af2a | -13.30381 | -45.22709 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7a7dc1db-e06a-350b-a3bd-75f06e08c8d8 | -22.60603 | -47.04807 | 2026-06-20 04:12:00 | NOAA-21 | HOLAMBRA | SÃO PAULO | Brasil | 3519055 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 76735990-cea8-3ff8-8760-39e764bff283 | -23.60733 | -46.37658 | 2026-06-20 04:12:00 | NOAA-21 | FERRAZ DE VASCONCELOS | SÃO PAULO | Brasil | 3515707 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c35e3518-1e7f-38a1-9a35-0d074f9e9945 | -22.32252 | -41.79414 | 2026-06-20 04:12:00 | NOAA-21 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 5c54ed90-5047-3b5d-b55a-d9aaa440a232 | -22.8583 | -43.37947 | 2026-06-20 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6d0b2e86-47ec-39d3-aea7-f44d95a68a7b | -21.61502 | -48.72696 | 2026-06-20 04:12:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a027bcdb-a330-34a0-95d2-040fd9493e55 | -23.81737 | -48.71474 | 2026-06-20 04:12:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8ec6b403-f478-3d68-9841-4e2ab92146fc | -19.96729 | -44.71769 | 2026-06-20 04:12:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1801ed0e-b34a-37f5-8c72-3e5725161a91 | -20.92212 | -43.08646 | 2026-06-20 04:12:00 | NOAA-21 | SENADOR FIRMINO | MINAS GERAIS | Brasil | 3165701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 62015cf5-c038-3a85-84b2-7fa4df2dc596 | -19.8283 | -43.38359 | 2026-06-20 04:12:00 | NOAA-21 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fa580a7b-795a-3be7-ac4e-6bff1dd666af | -19.70049 | -47.32905 | 2026-06-20 04:12:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9dba683e-6feb-3355-ae07-08bf7e56a843 | -19.15924 | -48.38816 | 2026-06-20 04:12:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf43ff8b-6ccc-3d43-a3fc-066386f1712d | -19.913 | -44.06023 | 2026-06-20 04:12:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 62f7f058-7e97-3c3c-975f-5f794684805c | -19.5262 | -44.73122 | 2026-06-20 04:12:00 | NOAA-21 | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1137902a-9271-337c-8146-1fb8ff91d904 | -20.7269 | -42.93725 | 2026-06-20 04:12:00 | NOAA-21 | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c874c44f-c824-3574-996e-cd557cf89aae | -20.82048 | -45.17608 | 2026-06-20 04:12:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a3cae44e-5c61-3724-a9ae-1b760cead079 | -12.5531 | -45.0174 | 2026-06-20 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 043cb901-3d7c-3ed3-a86f-4bc655721920 | -12.5339 | -45.0204 | 2026-06-20 04:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| dec76ce4-ff46-3e45-9a85-9348513e1469 | -12.5531 | -45.0174 | 2026-06-20 04:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 32d68a70-0e67-3da2-886d-6c1f7bf8bc94 | -12.5531 | -45.0174 | 2026-06-20 04:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 76d166c7-ab93-3453-aa29-01b8e735b11c | -12.5339 | -45.0204 | 2026-06-20 04:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| e1280043-957d-31b9-94a8-200ab0bf1768 | -6.78541 | -46.33144 | 2026-06-20 04:42:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99a12147-b779-3674-8c7a-e8322cdd2574 | -6.15337 | -48.49228 | 2026-06-20 04:42:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f70264ab-d497-372a-916e-ae6251575255 | -5.81271 | -45.07784 | 2026-06-20 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b4cd4662-1a23-3aca-b47a-62b67e346a73 | -5.81567 | -45.08238 | 2026-06-20 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d7dbc75c-1b86-3d74-9346-e928ce1e079a | -6.35838 | -43.59651 | 2026-06-20 04:42:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61126aff-c0b6-3428-a9fc-07eafe82c20b | -6.99327 | -42.77905 | 2026-06-20 04:42:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6d44385d-3214-39f7-a56d-bff63418fe43 | -6.32792 | -48.42014 | 2026-06-20 04:42:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0a0c416-e202-3ea7-af98-b994f38c6c52 | -3.60606 | -49.45366 | 2026-06-20 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3176b69e-8b24-36ab-be9b-816af1372ced | -4.45607 | -48.02314 | 2026-06-20 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 081a99f0-6425-3007-a8f2-9ec584cc8a5a | -6.37015 | -43.59808 | 2026-06-20 04:42:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c58e4ddb-0cc9-37f2-ac52-57747853c5d0 | -6.36622 | -43.59758 | 2026-06-20 04:42:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e0b35ce3-72b3-3ff4-8462-c871411ac496 | -6.7824 | -46.33156 | 2026-06-20 04:42:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2833666f-a880-3d8c-ae78-3fb4a8a29e54 | -6.3623 | -43.59708 | 2026-06-20 04:42:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a05d1ac-8b8b-3f9c-b05a-222298cc9626 | -5.8024 | -43.7914 | 2026-06-20 04:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7df0792f-25b7-3157-84b3-2aefc37fc383 | -5.80851 | -45.08139 | 2026-06-20 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2be74f73-fa02-3186-930a-8eb96524a179 | -4.35097 | -47.76515 | 2026-06-20 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94eec61a-6d77-3512-ac74-0d12e0790eb5 | -6.78484 | -46.33514 | 2026-06-20 04:42:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 68452ab9-6fc1-31ba-a64f-7173a44767cb | -6.83736 | -47.91706 | 2026-06-20 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a3c8532-19e2-302f-b31a-552cfa8d5ffa | -6.93802 | -48.1964 | 2026-06-20 04:42:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e86f519c-c452-3bc7-b683-306beb02128f | -4.48624 | -48.27718 | 2026-06-20 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c14ebc2-c0cb-35aa-ade6-2e56fa93549c | -6.39843 | -44.18196 | 2026-06-20 04:42:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c019c91a-3d44-3313-9d94-4e02a47b205b | -6.36696 | -43.59262 | 2026-06-20 04:42:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b5ccbf42-0094-335f-9538-64140ac581e3 | -6.99481 | -42.77531 | 2026-06-20 04:42:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 463ffdf1-9605-3eae-b607-81734a694a8f | -6.1456 | -48.49816 | 2026-06-20 04:42:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff0bf2fa-22ce-3881-ba38-61003a787843 | -6.50384 | -42.22068 | 2026-06-20 04:42:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3703307a-cc09-369a-b80f-7836ce932316 | -6.39774 | -44.18654 | 2026-06-20 04:42:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8d852ef0-3b55-3a71-86ac-4bcd73835673 | -6.77897 | -46.33104 | 2026-06-20 04:42:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ef5b6455-2c9b-3b28-853b-51cef1b02524 | -6.99383 | -42.77531 | 2026-06-20 04:42:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 84cd1c66-c531-348b-a0ad-50ba233a18ac | -7.55003 | -43.43016 | 2026-06-20 04:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8370da71-b30a-356e-8f22-82820b5cefee | -3.9762 | -49.11027 | 2026-06-20 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f4fe70b-88fb-321b-af4a-7ed93ff3ed6d | -5.81209 | -45.08189 | 2026-06-20 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1b1aebc0-9442-3c19-8e76-e53a9036ff99 | -6.83403 | -47.91653 | 2026-06-20 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98e95374-31a1-30cf-85df-a5cc8bc62ef0 | -6.77839 | -46.33472 | 2026-06-20 04:42:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 09f52798-0eda-3971-8d14-1de23aeea8a0 | -6.78182 | -46.33525 | 2026-06-20 04:42:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| adb51968-c45f-3452-be5d-f5b622c77126 | -6.15004 | -48.49174 | 2026-06-20 04:42:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 47d4b74f-0ff1-3bc5-9d44-f9a4f6c83d68 | -6.14615 | -48.49468 | 2026-06-20 04:42:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cc80b91-0e38-3945-873a-95dc0f6ac63c | -6.9028 | -42.84616 | 2026-06-20 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dcdb57d4-461d-3fe4-9496-328378eed190 | -5.81394 | -45.06974 | 2026-06-20 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 964f2e59-19df-3542-ba18-5cd8e3ca7414 | -6.30628 | -48.42746 | 2026-06-20 04:42:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e18d2e4-ad6e-330a-acf6-ba9495b84e52 | -6.30464 | -48.48067 | 2026-06-20 04:42:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 874e9a57-5396-35ab-aaee-faf457274100 | -5.73245 | -49.09265 | 2026-06-20 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f67363f-68ea-3b4d-99a9-f4ece616512c | -5.81148 | -45.08593 | 2026-06-20 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 620d3fc7-5d06-386b-8eef-7332e9e84ef5 | -6.37088 | -43.59312 | 2026-06-20 04:42:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 67006d97-0be5-3c52-ab13-c634f4f6515e | -6.78141 | -46.33463 | 2026-06-20 04:42:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 27b15933-bfb9-35b1-b552-73ded6e30bc2 | -6.36303 | -43.59212 | 2026-06-20 04:42:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63dcc09e-37b4-3a42-a12e-eb214cee1be6 | -5.81035 | -45.06924 | 2026-06-20 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae8b907d-fe0a-35c6-9874-887e4f7d9939 | -6.78198 | -46.33093 | 2026-06-20 04:42:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6790fdb-5199-34ce-88bf-8bfc1b0a4363 | -4.35429 | -47.76567 | 2026-06-20 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3468d8ed-b55e-34d8-805b-1bdca9756ef4 | -5.79786 | -43.79553 | 2026-06-20 04:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfbcc6b8-43a6-3fa2-841b-eaa6423587b8 | -5.80912 | -45.07734 | 2026-06-20 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 221c317d-57fe-3abf-9335-512fdc5a0de4 | -7.25883 | -44.22155 | 2026-06-20 04:42:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db74a05d-ebf5-3d70-89b8-3017e4e246ee | -5.81506 | -45.08643 | 2026-06-20 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 769cfc0f-c0df-3900-bcc7-21561bcb1db2 | -4.35152 | -47.76169 | 2026-06-20 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 334d9004-28e3-3785-b8ca-3771e65c8782 | -6.14948 | -48.49522 | 2026-06-20 04:42:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51a51367-1d1b-304a-b873-71ae596185ce | -5.79856 | -43.79082 | 2026-06-20 04:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a083921c-d39b-356a-b54d-08907d7b9dd6 | -6.99428 | -42.77907 | 2026-06-20 04:42:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d138d4b1-4fe1-31e2-a00b-5ee22287f6a3 | -6.30409 | -48.48413 | 2026-06-20 04:42:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4930837c-1fe1-30c1-a593-25bbe206543d | -5.80973 | -45.07329 | 2026-06-20 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33fb5114-3ec0-3e53-b39c-99e274baa633 | -5.81332 | -45.07379 | 2026-06-20 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c78b36c5-e995-356f-84b4-9c45ccbcb1fb | -3.42156 | -43.16533 | 2026-06-20 04:42:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d859b57-864f-3c31-abaf-2a8c456117ad | -12.7919 | -44.47807 | 2026-06-20 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e8cae4a-6b0f-3c05-82b6-a30c797a1eb1 | -11.89267 | -43.8339 | 2026-06-20 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e8724c12-ac13-36b0-8d24-3342fce1f6a1 | -13.29631 | -45.20616 | 2026-06-20 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a031721a-f61f-3b70-a72d-732822989b0d | -11.63566 | -48.53651 | 2026-06-20 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d8bee5e-fe30-3a6f-9132-167972e84efd | -11.89182 | -43.83065 | 2026-06-20 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5ea9054b-7ef9-3ab4-a1a2-bff442dc8b6b | -10.90395 | -44.49255 | 2026-06-20 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8bf8685c-9e92-3ab7-b659-4db4cff5231c | -12.78639 | -44.48825 | 2026-06-20 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README7.md)
