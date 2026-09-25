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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc368151-a67c-325c-8343-6458fdbdfc54 | -3.72974 | -43.18443 | 2026-09-25 03:47:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4f0428f2-a2c8-3f6c-a118-74bcda4addbe | -4.46148 | -47.92297 | 2026-09-25 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 07a6382d-cc82-3e35-8ccd-28142b33eff3 | -5.12147 | -42.69043 | 2026-09-25 03:47:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5a046d2-e450-3d41-820b-363489a41023 | -5.09778 | -45.52206 | 2026-09-25 03:47:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10f1da4e-b23a-3377-b997-7b3791cc1cb7 | -3.23887 | -46.93644 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| ec95a75b-caf8-3dc2-8bd3-ba1a71982708 | -3.44867 | -50.07861 | 2026-09-25 03:47:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 24176e29-c105-3831-b6e6-7b22d2ce3d80 | -3.6915 | -38.83531 | 2026-09-25 03:47:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e08ad3ca-2e11-36e9-a870-9271daca443c | -3.49365 | -48.96591 | 2026-09-25 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5055d7d1-bdd1-3f29-8e4d-d28c18aa1dbf | -3.45578 | -50.07977 | 2026-09-25 03:47:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e5eb1ce-12a7-3e61-9bc2-a6de95a4fb23 | -5.12575 | -42.69118 | 2026-09-25 03:47:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 600d3318-a406-3787-81d8-63a449aa1824 | -3.44637 | -50.09216 | 2026-09-25 03:47:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e0318ba-e94b-32b3-aa6f-b54ec9f67734 | -2.92158 | -40.89804 | 2026-09-25 03:47:00 | NOAA-21 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| ddd975cb-4b40-3bea-8ab7-7b9d29f19dbd | -3.25864 | -49.19066 | 2026-09-25 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4d7756f6-3eed-3ae5-8db3-50c953291164 | -3.17813 | -48.01513 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0e836329-63f4-3893-93b6-9b24a4da587c | -5.48098 | -45.12365 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c84f738-322b-37c3-b32b-fc55de4f1e3d | -11.51818 | -45.3952 | 2026-09-25 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecc2958d-d6af-3493-8827-44fb825a3987 | -7.59512 | -41.78799 | 2026-09-25 03:49:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bc5b6bfc-89ba-36e3-9d35-871b2e410dfc | -9.63255 | -43.93798 | 2026-09-25 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d5815a39-09d7-32e8-bbe1-52b35ec8845a | -9.63322 | -43.95974 | 2026-09-25 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 32f3d7f5-2185-3293-b491-e9f81d3664d0 | -9.99951 | -39.1746 | 2026-09-25 03:49:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fceaf04c-edf1-3a73-b8b3-ad5d1489e7af | -9.62889 | -43.95892 | 2026-09-25 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 827032ad-5972-3a62-a663-5f58be863500 | -9.63469 | -43.95131 | 2026-09-25 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 237f75e2-eae1-39f8-81df-a8808fdeddfa | -5.46948 | -45.1004 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a30c47e-ce0a-3686-98eb-947e2a04e606 | -11.52281 | -45.39603 | 2026-09-25 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 804795f0-1e6f-3ea8-bfca-a36adeab34f9 | -9.48211 | -40.32771 | 2026-09-25 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6b67ba26-7c51-3e6e-938b-5a50b4c62845 | -11.6282 | -41.83374 | 2026-09-25 03:49:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ec4b814c-f163-3157-b6db-1d48ff24033e | -5.47012 | -45.10064 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a81f8856-8662-367a-847a-ad32cb9c3621 | -12.65165 | -43.15759 | 2026-09-25 03:49:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d2227c24-db0d-300f-a5a4-60d42a02f36d | -6.89276 | -43.74488 | 2026-09-25 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ada13839-bebf-3b82-961c-1bc28b5661a4 | -5.62049 | -45.24297 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7f7ff7dd-95d9-3855-8c20-49c073b1956e | -10.24741 | -44.63456 | 2026-09-25 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79baf7b2-2ebd-3c49-b84e-01c5705fac55 | -5.486 | -45.12461 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7279f6ad-1fc2-32e0-9008-9ab3a813b8b1 | -11.6465 | -43.47929 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50ce9f7d-40fc-3dc9-8adf-1c7df5904bf8 | -12.85155 | -41.16896 | 2026-09-25 03:49:00 | NOAA-21 | NOVA REDENÇÃO | BAHIA | Brasil | 2922854 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7570fb62-b9ec-3436-b14e-3732f6544683 | -7.95069 | -37.28106 | 2026-09-25 03:49:00 | NOAA-21 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9a9b1dfd-8fce-3867-ab4e-fa426ee87088 | -13.40186 | -40.96417 | 2026-09-25 03:49:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7a1047be-5c16-35bd-98d0-e19ae38d7b0f | -11.67456 | -43.51083 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 459e7aa7-3344-33fb-bae9-867fd9f00b50 | -11.74544 | -50.54742 | 2026-09-25 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 271fd02c-0fb2-35a6-a9e9-2150f3fba338 | -8.59456 | -48.36984 | 2026-09-25 03:49:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 67429e40-d048-3a05-83dc-9da25a8a6309 | -13.06733 | -43.27318 | 2026-09-25 03:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b1f73ee1-2ded-3715-acb3-9c811a44e655 | -6.92372 | -42.87912 | 2026-09-25 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 65ee5923-b595-3819-a9ec-ed6c526ce65c | -5.48655 | -45.12147 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31662005-6243-34ed-ac69-d16c08d479bf | -11.64259 | -43.50138 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c6d6450-ad70-395c-ae41-189fd9c1a84f | -9.6311 | -43.94629 | 2026-09-25 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 80845df3-443f-361c-a7e3-e03c1b933458 | -10.95716 | -43.87794 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4b62eb7-904c-3711-b0e6-6084607a6ed2 | -12.65546 | -43.16136 | 2026-09-25 03:49:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 48583117-e77e-3631-981d-d788aadf70f7 | -11.36865 | -43.39145 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26cff461-0786-3777-874e-8400c727ec98 | -11.74214 | -50.56363 | 2026-09-25 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| eaefb75b-2b48-325e-ac5b-fc4c30302491 | -6.82337 | -43.55994 | 2026-09-25 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4924ff39-596a-311b-82f0-ebba51528835 | -8.33475 | -44.14314 | 2026-09-25 03:49:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 04673e1f-c297-3eb6-b49b-300bb3a359c5 | -9.40859 | -41.1814 | 2026-09-25 03:49:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8f4a3dd0-daee-33ab-8fcd-06a5f5fdb547 | -8.38714 | -36.70639 | 2026-09-25 03:49:00 | NOAA-21 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fb200fd1-f5ab-39a4-a24f-ae6ef4b792f8 | -11.66705 | -43.50572 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae98f946-c865-33c3-bd2d-014d2ba9dd50 | -9.47443 | -40.33054 | 2026-09-25 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 55917a2f-50ac-3034-b8c6-783b6ad98240 | -9.63107 | -49.02231 | 2026-09-25 03:49:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37f1d92d-2c42-3dfe-b8e3-9d2e292d8526 | -5.48152 | -45.12053 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c43ef344-47f2-3253-86da-691dc9e4b097 | -5.47158 | -45.09189 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01c5ed24-14d6-3d02-84cb-054b8fe834f8 | -9.47794 | -40.33111 | 2026-09-25 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 43db3006-fa48-3d35-968e-ef2588eba021 | -7.12232 | -41.72488 | 2026-09-25 03:49:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9971ff86-0639-37e3-8f17-495a362367d2 | -8.32278 | -44.13196 | 2026-09-25 03:49:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8480cfe5-58fd-38ce-a4ef-6741612471fc | -12.01483 | -42.92232 | 2026-09-25 03:49:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 7c3969fb-0719-3cde-be70-3219256e4d3a | -12.71651 | -44.89644 | 2026-09-25 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2d64e02-e247-3f66-be4c-22a05999aa7d | -6.89725 | -43.7456 | 2026-09-25 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23f8468b-f3b0-380a-8e27-327301d2bf05 | -6.70701 | -45.99232 | 2026-09-25 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7de7faca-371b-32f5-93fd-005e21214104 | -7.0256 | -41.55153 | 2026-09-25 03:49:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 880e6ffb-e4a2-34f8-afd4-e578355e245e | -11.25494 | -41.90434 | 2026-09-25 03:49:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cfa27647-99bb-3c6f-b391-c9a22ac72784 | -11.65825 | -43.50797 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99f4f962-ec65-3b89-b6ad-e1ae894a8b3b | -5.77796 | -45.10578 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| de501c01-3161-3062-b8fa-7507c1b81f33 | -7.35523 | -42.06699 | 2026-09-25 03:49:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 65d8a650-06ae-3e1d-9c72-7e63f5d839af | -7.1224 | -41.72173 | 2026-09-25 03:49:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5821809b-a56f-3393-9bff-e7f90750a7c9 | -11.66297 | -43.50501 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 598072cb-96db-360f-b17b-2955c23a8f45 | -5.77443 | -45.09614 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d709158c-57ee-38dd-bd51-052cc0027e74 | -13.07123 | -43.2769 | 2026-09-25 03:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a37a7768-f988-3584-8888-fba33c598018 | -5.46509 | -45.0997 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49169378-d3a8-3445-ba1c-d2a60dc6ee6f | -7.12144 | -41.73003 | 2026-09-25 03:49:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 86d73aa7-fbd1-30ff-809e-0fa6d60bd936 | -8.03904 | -39.89274 | 2026-09-25 03:49:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7cd6e810-9131-3677-a8b3-2c5454b3734b | -13.20308 | -40.46367 | 2026-09-25 03:49:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 441bf862-be87-3cca-a2e1-5eda78cdd6df | -5.77846 | -45.10279 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 93a97b28-4b99-3e8c-b266-ab99c26c89a6 | -5.47048 | -45.09467 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 273ddb53-93ed-3191-8015-229a00a2b119 | -9.63249 | -43.96395 | 2026-09-25 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9aa3e6db-63c5-3754-bd6f-04c130950e78 | -9.62815 | -43.96315 | 2026-09-25 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 87c4e383-5e8a-37cd-8a4f-567ea4e054b5 | -6.92548 | -41.69646 | 2026-09-25 03:49:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| de0bd4b6-40e5-3b6e-9362-ed3d4d477e23 | -12.65458 | -43.16651 | 2026-09-25 03:49:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d168108f-53db-3ea7-a655-6cc5c62c81d9 | -12.41098 | -43.27002 | 2026-09-25 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 406273de-41e4-3981-9796-57903ab11c5c | -6.16711 | -44.15508 | 2026-09-25 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71ac82c8-9388-30f5-851a-3c6aa24c1894 | -10.04006 | -50.1573 | 2026-09-25 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 736145b5-c87a-3dbe-9f9b-9c07752831a7 | -9.63396 | -43.95552 | 2026-09-25 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7ab6f642-0ede-3886-b149-845dcb331768 | -12.65153 | -43.16066 | 2026-09-25 03:49:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 5333ab17-229e-3c3e-ba66-fb61abe4feb4 | -11.74434 | -50.55282 | 2026-09-25 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| e0b26424-0378-3bea-9210-a2aa7476833e | -8.62232 | -36.92205 | 2026-09-25 03:49:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e99e48d9-0d93-3cd9-a606-c6c62b2fa29d | -5.47101 | -45.09166 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d5a7b80-eb8b-3e06-be40-490ca7d61997 | -11.34575 | -43.40246 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93e51a37-a46c-3b94-8a77-9d6abccf18d1 | -11.67048 | -43.51012 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13918ec6-d162-3de3-b393-00bd3fd16e63 | -9.99006 | -48.31729 | 2026-09-25 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a7b5fec-4ed2-3abc-b189-98d6c79aed0a | -11.52368 | -45.3913 | 2026-09-25 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f22fbc2e-e7c6-39f0-a6bc-034075c8f3be | -11.36801 | -43.3951 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d0478f3-3871-33f6-9951-1c477825676d | -11.73794 | -50.5515 | 2026-09-25 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| c9559080-5c28-3624-9a92-4ecd1b19f952 | -5.77393 | -45.09911 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d8ebab8c-b67f-3d88-8473-4188d0e83b6d | -9.47508 | -40.32656 | 2026-09-25 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 445d00b9-d85a-31a5-ae3e-f8e17cf969db | -13.07034 | -43.27903 | 2026-09-25 03:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |


[Clique aqui para ver as próximas entradas](README12.md)
