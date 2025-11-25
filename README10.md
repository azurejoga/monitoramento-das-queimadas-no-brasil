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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea46e603-44b6-3ebf-90c1-5072cf118001 | -6.68826 | -43.94316 | 2025-11-25 04:18:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| abcca75d-adef-39b9-9edc-7f5e7f3eaa40 | -6.08879 | -41.68917 | 2025-11-25 04:18:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bf9512e7-d08a-3b3e-9582-e7af44e30971 | -5.57005 | -44.97709 | 2025-11-25 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22d9d68b-baa6-31fe-bb0a-88251a3ab8ff | -7.25415 | -46.05445 | 2025-11-25 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e05a8312-5602-3cac-8336-61b2107e9704 | -7.40832 | -39.0392 | 2025-11-25 04:18:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0f9daee6-6edb-3154-bc64-cd085612a5cf | -8.06278 | -43.13106 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 81ae764e-117a-3db8-bb4c-86cf6d2d240b | -7.53498 | -46.56924 | 2025-11-25 04:18:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 288cf080-69e5-3889-9e7a-8c6fcd772042 | -6.07675 | -39.54562 | 2025-11-25 04:18:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 93afaea5-443e-35ac-8176-415ee3209fa8 | -6.31577 | -43.81897 | 2025-11-25 04:18:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af7d3b15-38c5-3f76-b83f-17e78c45134b | -9.11758 | -44.43815 | 2025-11-25 04:18:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c5b586d-663c-36d7-b05c-dd4e2c076756 | -7.165 | -44.99276 | 2025-11-25 04:18:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8904195-f75e-3a12-8dfb-6e5452463174 | -5.74192 | -42.373 | 2025-11-25 04:18:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ab6d50aa-c771-33ea-9fea-108d5615bf49 | -5.99965 | -44.72153 | 2025-11-25 04:18:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1eddff8-e28b-33f9-9ed1-2a09da9cb8da | -4.75396 | -45.10837 | 2025-11-25 04:18:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 626c6452-c42d-30a8-9416-725cf83ed9af | -5.59424 | -45.17932 | 2025-11-25 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5791bfb2-3db2-394f-b907-dc9e4fc39f19 | -5.03693 | -43.26228 | 2025-11-25 04:18:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50d95586-0d49-3241-b54f-b1feb1e25769 | -6.60423 | -43.68998 | 2025-11-25 04:18:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff88e994-991f-39ae-8d1f-5d01d0c892d5 | -8.05727 | -43.14446 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eee9db7d-475d-3560-84a0-af9fed0600ed | -7.28934 | -42.51808 | 2025-11-25 04:18:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 57a0e4bc-f669-3741-9afd-80728a72aecb | -6.55901 | -39.51062 | 2025-11-25 04:18:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| eadc8920-4be5-3f3b-862e-39a5e5dad591 | -6.86609 | -39.11133 | 2025-11-25 04:18:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9690c6f0-8bae-3cf9-b8a4-d37da4e0dd1c | -6.69159 | -43.94371 | 2025-11-25 04:18:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c24e9ae-d1ed-3362-a0c2-876593e2799e | -6.4623 | -43.55674 | 2025-11-25 04:18:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8ddaf7d-920b-330b-8f27-067670f8a725 | -8.80253 | -44.39803 | 2025-11-25 04:18:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1792588-dc36-3100-bc52-1c6829821475 | -4.18178 | -48.63723 | 2025-11-25 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdf797fc-05bd-3811-92db-ab60df042a74 | -5.42907 | -44.83677 | 2025-11-25 04:18:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 892a2480-22b6-3d3d-a950-e0fc13efefa6 | -4.75047 | -45.10786 | 2025-11-25 04:18:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2d01c44-463a-3504-b488-3507f8cc976b | -5.85052 | -42.93373 | 2025-11-25 04:18:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 21f920a0-01dc-33db-b2f1-3514a47e7de1 | -8.05891 | -43.13402 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 8f0b1973-63c7-3b21-873d-68de0acadb70 | -8.06114 | -43.14151 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| f05b951d-5c40-3316-a117-a952758814ce | -6.99612 | -43.15802 | 2025-11-25 04:18:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 27d62c50-ff71-3657-920e-bdbaa5ec73fd | -12.19437 | -47.96674 | 2025-11-25 04:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c64168d4-5a32-33dc-946c-c474758cef35 | -17.6203 | -50.93783 | 2025-11-25 04:21:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef0e104e-2dd5-34d4-a5b3-3b78dadd0b90 | -12.19132 | -47.97307 | 2025-11-25 04:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 20174cdf-5c52-3c43-b790-e3e53433a398 | -12.77976 | -38.4969 | 2025-11-25 04:21:00 | NPP-375D | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0e35bbdb-d7f9-3c2b-b111-2a1a91a7c085 | -17.29317 | -49.99078 | 2025-11-25 04:21:00 | NPP-375D | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27c01fcd-9cdd-3417-b322-4c72b4f94212 | -12.1936 | -47.97118 | 2025-11-25 04:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8419a64d-35c1-3702-8288-27a9f08e9b92 | -12.78256 | -38.49898 | 2025-11-25 04:21:00 | NPP-375D | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3f8b1c89-043a-30c5-b2a7-54926993fd2b | -16.30464 | -52.92338 | 2025-11-25 04:21:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc226fdb-877f-35ee-b543-c824d572e047 | -12.00447 | -49.27496 | 2025-11-25 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2204fa3f-eec9-3447-ab63-e97ef96efe6a | -12.77823 | -38.49843 | 2025-11-25 04:21:00 | NPP-375D | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b87095a0-7757-3430-a529-ec0a018c6333 | -12.18839 | -47.96796 | 2025-11-25 04:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f994b10-0d21-3bfb-8f11-229c579ba2dc | -12.18993 | -47.97053 | 2025-11-25 04:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a9641c1-da60-35c7-99ef-a7945fb32ccd | -12.19207 | -47.96862 | 2025-11-25 04:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8a478d90-1305-3211-acef-9c6901909b18 | -17.62431 | -50.93868 | 2025-11-25 04:21:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b309f45e-718f-38d1-80d9-75549ffa4536 | -18.11256 | -54.51649 | 2025-11-25 04:23:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e19604e3-e52f-32dc-9b84-855fc2c38107 | -17.24482 | -56.02302 | 2025-11-25 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b5132ae5-db42-3fc9-a13b-f4b789fd7bd9 | -18.11897 | -54.51751 | 2025-11-25 04:23:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5255efe6-7d04-3794-80a3-f16d57945f78 | -21.25106 | -52.05802 | 2025-11-25 04:23:00 | NPP-375D | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ac6fd1b-8697-361c-baa0-0d3f65cc15ee | -28.71322 | -52.18894 | 2025-11-25 04:23:00 | NPP-375D | NOVA ALVORADA | RIO GRANDE DO SUL | Brasil | 4312757 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c111e6f0-23c0-338e-9d63-569063bc331c | -22.47794 | -49.13345 | 2025-11-25 04:23:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42faa325-b5d3-3596-97ab-d53d66b1352b | -22.39768 | -47.24247 | 2025-11-25 04:23:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0aa34641-0370-32e1-9eda-72f4b78adb39 | -17.24564 | -56.01912 | 2025-11-25 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e5916da1-1282-3e17-b608-1c666b6e7fd5 | -19.33409 | -54.35682 | 2025-11-25 04:23:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ad6f10dd-ef69-3292-9635-ff0044b16781 | -18.11756 | -54.51757 | 2025-11-25 04:23:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4da9aa67-7062-375e-bf39-b3a238bbd706 | -28.71349 | -52.18628 | 2025-11-25 04:23:00 | NPP-375D | NOVA ALVORADA | RIO GRANDE DO SUL | Brasil | 4312757 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8187a957-0890-3f6f-9c94-72fd0ab441d3 | -19.33521 | -54.35123 | 2025-11-25 04:23:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9958fe45-2fac-3824-ae21-c504cbed3ddd | -18.11398 | -54.5164 | 2025-11-25 04:23:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90f6ec99-a5d3-389b-9f94-38c2ea47ebba | 1.70984 | -50.74757 | 2025-11-25 04:36:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb251781-99d4-3a90-820f-cfdc3148ad8a | 1.70202 | -50.74457 | 2025-11-25 04:36:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82055dff-1524-3e8f-8e63-4cae2e388bc5 | 1.70689 | -50.75224 | 2025-11-25 04:36:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f59e1e12-a581-3187-bbe5-dd8e7ba61d0e | 1.70625 | -50.74812 | 2025-11-25 04:36:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dff9ef9-7b90-32cd-be7c-36d29db2cb2a | -4.04749 | -42.51655 | 2025-11-25 04:38:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7c221d74-7e7c-3033-ac9d-da89fc43484e | -1.14917 | -54.21765 | 2025-11-25 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d428b1c8-0594-3369-92bf-2d1c34c6f8a9 | -2.87573 | -51.80508 | 2025-11-25 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 369677b4-21c7-36ce-be95-5a2ee5683f25 | -3.9315 | -50.18372 | 2025-11-25 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e01fe513-ac1b-3c09-93ba-646174557d67 | -5.83313 | -42.92542 | 2025-11-25 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2b84fbf8-976e-3575-9e85-648b136818ed | -3.77575 | -44.05014 | 2025-11-25 04:38:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 660ecc1e-2913-302b-87f3-e1847378893c | -2.49062 | -47.82108 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b310a3d-6459-3581-8beb-128658aafcfb | -1.86036 | -46.37169 | 2025-11-25 04:38:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c926da38-aa5e-3321-8335-528a699ebaeb | -3.90152 | -50.35065 | 2025-11-25 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3564a9ec-0043-3388-91f7-92fd077fc811 | -4.74649 | -44.4459 | 2025-11-25 04:38:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48461d3d-2a38-30b5-877e-ff78e58d08ab | -4.31332 | -45.3518 | 2025-11-25 04:38:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f724440a-a3e1-3908-9391-87afe8c29b23 | -4.1694 | -45.73225 | 2025-11-25 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cf7de6c-2c16-315b-bfec-a887cc30fff2 | -2.46768 | -48.22488 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4551c118-9675-3cf5-85e6-02ac1b1a017b | -6.68457 | -43.94316 | 2025-11-25 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d9d30919-0e7d-3faa-8918-018f75bad6ef | -2.88518 | -51.81506 | 2025-11-25 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc184887-17d3-3dbd-9d4c-5db51b2494d6 | -4.08474 | -47.09806 | 2025-11-25 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eec7a003-427c-3275-b453-304bd6c55816 | 1.35864 | -50.677 | 2025-11-25 04:38:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f629a5c4-32bb-365e-81ff-718a8c40ecdf | -4.30906 | -37.99312 | 2025-11-25 04:38:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b9fc1007-a611-325a-91b4-61d7da033ef5 | -4.33758 | -45.6358 | 2025-11-25 04:38:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4a75c90a-8164-360e-b925-5c84d40707bc | -3.9438 | -50.61573 | 2025-11-25 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85c4ee18-5789-3a33-9572-7c1d125b6c7c | -2.87639 | -51.80097 | 2025-11-25 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19d487fc-fcff-3b7a-893a-a8b5812b012b | -4.17945 | -48.63845 | 2025-11-25 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7393fde6-242a-3ec9-8c1c-31a3f848bb01 | -1.66389 | -52.05063 | 2025-11-25 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe558046-f1a1-3ee3-8ba1-3c45dd086774 | -4.81782 | -50.74195 | 2025-11-25 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb177a19-de0e-3c1a-aed2-a2dc92ed5df5 | -6.68513 | -43.93922 | 2025-11-25 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 4627288c-ed76-3b46-aab6-04e08eec5d31 | -1.67612 | -52.09315 | 2025-11-25 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2843eaa7-5d28-3505-97c6-6140f3e223a9 | -6.67683 | -42.48408 | 2025-11-25 04:38:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f5f7e2ea-270c-3c6a-b62a-9060032622a7 | -1.644 | -52.05645 | 2025-11-25 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f1b69b86-8ce3-3522-888d-8fc7b408c75f | -5.1269 | -43.02582 | 2025-11-25 04:38:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 27fdca74-19a2-3205-95c0-8e381d4b1a0c | -4.0697 | -44.59277 | 2025-11-25 04:38:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3e88e579-e5e0-3ebc-a0a5-dcf0dca2730e | -1.1461 | -48.09468 | 2025-11-25 04:38:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fde6b44-2368-32c3-bf53-1e99b3ac092a | -5.99924 | -44.72378 | 2025-11-25 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56b1360c-3ddc-30e3-8d81-4cea690f4945 | -3.00883 | -49.55223 | 2025-11-25 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f476eaf9-82b8-3752-924c-6045f44cec10 | -3.41039 | -49.4627 | 2025-11-25 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65155f8b-2a33-3556-99b0-65439b103187 | -2.39954 | -45.62788 | 2025-11-25 04:38:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d2357a7-4218-3579-be89-231cbe3b7a9b | -5.32167 | -44.82801 | 2025-11-25 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3f7a34b-4650-3f73-be7d-c337244ff0b4 | -2.93832 | -48.23495 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d27df31a-810d-33d9-b587-94ab89ea8438 | -1.86094 | -46.36794 | 2025-11-25 04:38:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README11.md)
