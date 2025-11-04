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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96b27a67-de1c-3801-92cc-c58fc04c529d | -3.43466 | -50.23938 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ace1c16c-c610-3bf7-bdc1-da1f7ec8760f | -3.43659 | -42.54212 | 2025-11-04 04:10:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f7e9b8e-48b1-3b26-8523-505655aef816 | -4.61336 | -45.75952 | 2025-11-04 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6c3ac25-0b1e-30de-9cbe-d4fd3f551193 | -4.00836 | -45.30088 | 2025-11-04 04:10:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afb5c516-64b8-3154-a429-97eb993534a7 | -7.08413 | -38.82955 | 2025-11-04 04:10:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bf1c761c-8387-3651-a651-7a7f845ba3b6 | -4.6166 | -46.59703 | 2025-11-04 04:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cf8780a-703b-3851-91f3-2c98f9243f62 | -4.61027 | -45.75376 | 2025-11-04 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90bef8d0-6b68-36d9-bf4e-561d3efb940a | -6.40957 | -43.06429 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adbba251-e934-3eed-a8ff-36cd24483e11 | -1.22534 | -49.15287 | 2025-11-04 04:10:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 317eb960-0ef4-351c-8971-83f5f91e0a7d | -5.58265 | -43.79109 | 2025-11-04 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 083ef4cd-8dba-3a4f-9230-23829b32eb58 | -3.45 | -39.23191 | 2025-11-04 04:10:00 | NPP-375D | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4fbe9f1f-382b-37f8-9ea8-a4e42fb63d84 | -3.91976 | -47.69307 | 2025-11-04 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| bb4ff507-17fe-3a5a-a840-39f200d6372b | -4.45955 | -43.46022 | 2025-11-04 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8406cf5-e5cc-35cd-bd84-6caf4faf385f | -3.92354 | -47.69845 | 2025-11-04 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| fe0796aa-a4e6-3ec2-b2c3-75f13fa8ce9f | -6.10018 | -44.44108 | 2025-11-04 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e72330d1-af01-364c-a593-e2837064305b | -2.98695 | -48.70746 | 2025-11-04 04:10:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daa80391-c228-3e98-aa76-987d9b998f05 | -5.22549 | -38.60234 | 2025-11-04 04:10:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4a438459-5ab2-3fca-a768-4ada410843f4 | -5.36428 | -44.7406 | 2025-11-04 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65a1aabc-b7db-37f7-85e4-39f48e2d946d | -6.37007 | -43.56901 | 2025-11-04 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29b4baec-e33d-3a11-aced-3c4804f94410 | -4.18947 | -45.78115 | 2025-11-04 04:10:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| beaa94ab-e78a-31b1-9a21-9f8cb8fc0f23 | -10.94329 | -44.19919 | 2025-11-04 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 671bf790-d8ab-3e0d-b3f1-8780083d414d | -7.77949 | -42.21553 | 2025-11-04 04:12:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ef3ca355-a02e-3ba1-984c-730b05d6f04f | -7.60314 | -43.00757 | 2025-11-04 04:12:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4c7551c4-b544-37da-b25b-bceb39c3f836 | -11.73584 | -43.8435 | 2025-11-04 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ee11e4c9-467d-3c0d-bd2c-9cd061ad8ccf | -12.60632 | -43.05625 | 2025-11-04 04:12:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 365ab0d1-d3ee-309d-8b53-dbcb2f584b56 | -8.65454 | -39.7307 | 2025-11-04 04:12:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0c2b9d68-8c62-3ac3-b157-d1a66f797db1 | -13.31539 | -42.42191 | 2025-11-04 04:12:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 918a08ef-907d-31e8-9f0f-58aef2cb568a | -9.85548 | -44.13994 | 2025-11-04 04:12:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 80a26384-587a-3487-9581-12420f526d3b | -12.84848 | -43.32447 | 2025-11-04 04:12:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bf7cb9d8-15c6-3768-8c5c-9ab4f826442d | -7.49851 | -47.03482 | 2025-11-04 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efe059ba-94ea-3a07-8fe8-d0cac5982a7f | -13.31873 | -42.42244 | 2025-11-04 04:12:00 | NPP-375D | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e2494f8b-8df1-3aac-a034-3cd71ee26d52 | -6.84713 | -46.30195 | 2025-11-04 04:12:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72a6b6fb-2eae-32c9-a44b-185e10b6c463 | -13.60401 | -41.07765 | 2025-11-04 04:12:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e368cf6c-a306-3c6a-aeb4-e653a5666bfd | -10.93989 | -44.19862 | 2025-11-04 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff0bebde-27ff-3b85-a37c-daaf5dae002e | -11.17965 | -41.80116 | 2025-11-04 04:12:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 33f4012e-7f9a-3a97-954e-d78941cb273e | -11.84107 | -43.72453 | 2025-11-04 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9e606eff-1ede-3938-8aa0-c5cb7aa2f254 | -12.91561 | -45.09203 | 2025-11-04 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10859586-d31a-3b92-b645-bd78fd08988d | -10.02079 | -37.38852 | 2025-11-04 04:12:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4a181d48-3751-30b9-be67-76e0b590bb7a | -10.89157 | -44.00237 | 2025-11-04 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c72fb2f-7046-3142-a842-7c28b03ad6da | -6.84404 | -46.29611 | 2025-11-04 04:12:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| efc5bb7c-87fd-38ba-bfd3-47adc0557f12 | -7.6065 | -43.00811 | 2025-11-04 04:12:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3b14a072-9afb-3c41-bed6-64e7e662fe8e | -10.93491 | -44.1864 | 2025-11-04 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70541a36-c65b-379f-9038-15317d112690 | -9.74028 | -43.86012 | 2025-11-04 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 20a08dda-b1ff-3bbb-8fff-030a9b988a96 | -12.91216 | -45.09142 | 2025-11-04 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c6cff952-823c-3f61-8180-78eeb1237294 | -9.85487 | -44.14366 | 2025-11-04 04:12:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| a88bc1a5-bfac-3905-9624-850d03d3d9ac | -12.72557 | -43.43898 | 2025-11-04 04:12:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dbfb6806-1307-34b1-b5c0-aab4579909b4 | -12.0197 | -43.85318 | 2025-11-04 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72861ee2-8061-3093-bf02-6a0ab95524d4 | -11.83715 | -43.72755 | 2025-11-04 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ae119d33-b122-3792-9a31-cecba4de5150 | -12.91154 | -45.09525 | 2025-11-04 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8a7d6a8-e1b6-3ae8-98ed-b6899f4830bb | -13.31595 | -42.41833 | 2025-11-04 04:12:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 507b95a5-08b1-346c-a4de-a0f8d8e0fbe3 | -7.49687 | -47.03808 | 2025-11-04 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a78bf0aa-ef0e-37f9-88a1-6c5630ed9dd8 | -6.84799 | -46.29673 | 2025-11-04 04:12:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fcdd7481-6f0b-34a5-a9d0-147eba4f8b13 | -7.85775 | -44.20604 | 2025-11-04 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14f2cde6-0926-3cef-8952-0b28d223796e | -12.013 | -43.85206 | 2025-11-04 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6f3e7e87-2c6e-3d8e-9d03-3c21bc2b1bcf | -13.32643 | -44.48004 | 2025-11-04 04:12:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf8f0d29-22df-3f95-bc01-19821efef1e6 | -13.0149 | -43.61754 | 2025-11-04 04:12:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71bc30cb-296e-33c0-b011-38d1a999d3c6 | -12.91498 | -45.09586 | 2025-11-04 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f321575-1c68-3fdf-8059-d2ecfb35d7a3 | -8.11212 | -43.81846 | 2025-11-04 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 94d2ed21-42e1-3c5d-9f29-8514fef4716f | -11.84263 | -43.72429 | 2025-11-04 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 128cb847-aa63-3523-be66-f0fcf4b016b3 | -9.24243 | -47.54197 | 2025-11-04 04:12:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fcdb0b8-1a28-3181-9ccb-db58b81a587e | -10.64253 | -44.66685 | 2025-11-04 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 014a441f-e89f-3b24-b5b4-a61284dd8bf4 | -13.32246 | -44.4831 | 2025-11-04 04:12:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 776dc8bf-55d8-3b1b-8886-8110598def28 | -10.58167 | -40.51207 | 2025-11-04 04:12:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4232ec3e-d14d-3620-8165-8a030f2f0860 | -7.9503 | -40.1825 | 2025-11-04 04:12:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8bbdc481-2a15-3a48-ba10-76ff99ab30cc | -10.9337 | -44.19378 | 2025-11-04 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ceab195d-512e-32ed-908a-ccc4ab69018e | -11.11702 | -41.0924 | 2025-11-04 04:12:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 78914afe-e332-348e-9f66-1560a9fd06ec | -10.9377 | -44.19066 | 2025-11-04 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5aab2e75-e80b-3ca1-a7eb-9e5bb0c13086 | -12.01635 | -43.85262 | 2025-11-04 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f1018e27-fdde-3e83-8526-fe881750f921 | -10.93649 | -44.19804 | 2025-11-04 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d00b28e-7669-3598-b3dd-18775038a8df | -12.91623 | -45.08821 | 2025-11-04 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16ab6616-e2df-3a21-ab3e-49bd4558d4bd | -13.31968 | -44.47887 | 2025-11-04 04:12:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| acae9d7d-eb9b-3cf7-8bf5-fd2b20aa2085 | -12.7289 | -43.43953 | 2025-11-04 04:12:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b850f47-80f5-3361-87bd-a98c6f352bfa | -11.32832 | -41.67075 | 2025-11-04 04:12:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3014ee92-3f3e-33c5-9cf0-650733b1998c | -11.28045 | -41.74783 | 2025-11-04 04:12:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2ba6fc25-0c03-3c3c-aacc-a5e15208ceb4 | -8.10831 | -40.78882 | 2025-11-04 04:12:00 | NPP-375D | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 414ade2e-b5e1-3d22-831b-ef84b6429ecd | -8.5984 | -44.15763 | 2025-11-04 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 231fbc7f-64b4-3810-9cf1-f4a6cf6ba7f6 | -11.10919 | -41.62192 | 2025-11-04 04:12:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b7f4e1e0-5c85-32b6-bae3-36f7c79300f5 | -12.90809 | -45.09465 | 2025-11-04 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f77ba65-8566-3900-82bc-ffb597c3b92c | -7.07011 | -46.73597 | 2025-11-04 04:12:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f5d3e508-b7ca-3424-bde2-34dbc1c8f824 | -6.83923 | -46.30072 | 2025-11-04 04:12:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1e9b2d60-50d1-343f-a4f4-9859b1784b54 | -9.67038 | -45.3875 | 2025-11-04 04:12:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0c7ba4d-04b9-360d-a5cb-45e9b2f67863 | -7.85303 | -44.21304 | 2025-11-04 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2ecd6e5-1212-384b-8dd0-7de521f21ea5 | -10.61829 | -44.66291 | 2025-11-04 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b7c42ca-17b3-37a2-815d-5e5c94d503cd | -12.44872 | -43.8577 | 2025-11-04 04:12:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f56ed66-8329-35d3-9a08-e6171a8a90d8 | -11.72672 | -44.75047 | 2025-11-04 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a25f8e15-45c5-3cca-bd2c-7c8828aa8803 | -9.73969 | -43.86376 | 2025-11-04 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 896b3c6a-340b-39e0-9e50-6a2edcc89e4d | -7.61447 | -46.4757 | 2025-11-04 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 92805877-cbd3-3b63-ac15-ad8ef2da10af | -11.73248 | -43.84295 | 2025-11-04 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4037217-65a5-38fb-8dce-43910404a2af | -10.90226 | -45.10529 | 2025-11-04 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0186dcd3-c419-3333-9151-066c51af8d70 | -10.93091 | -44.18952 | 2025-11-04 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b800b22-ae83-3d5c-af1f-2184cce488d4 | -9.04296 | -47.00595 | 2025-11-04 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 993b0a56-5626-3f1a-a940-b51a29f7cfb9 | -10.9371 | -44.19436 | 2025-11-04 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5eb9f696-83bf-367b-8dcb-0add62d2b75f | -12.5812 | -43.36419 | 2025-11-04 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d3adb21-75d6-3498-b697-6632301d3ac5 | -7.77893 | -42.21901 | 2025-11-04 04:12:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1413a2b5-b692-38f7-bedc-68c821306d75 | -10.64598 | -44.66746 | 2025-11-04 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdc655d9-32b2-3d2b-82a1-78f1040db675 | -11.68461 | -41.11921 | 2025-11-04 04:12:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dd1a60eb-a565-3999-931e-1076c31a1a2b | -9.04605 | -47.01184 | 2025-11-04 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2701f61a-432e-3c05-906a-c60f605b97ca | -10.86688 | -44.40787 | 2025-11-04 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c4e726a6-471d-37bd-994c-9b87f2ea6c3c | -10.94389 | -44.1955 | 2025-11-04 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ddf61f2a-eab7-3761-b702-77570f5caac2 | -8.94184 | -43.95858 | 2025-11-04 04:12:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |


[Clique aqui para ver as próximas entradas](README16.md)
