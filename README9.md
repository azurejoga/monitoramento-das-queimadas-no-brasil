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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 614c723d-7d6a-3c89-a202-a64151a88c81 | -9.11338 | -48.89291 | 2025-09-26 04:14:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9da1226-ddee-3b22-86ba-3ef8d5d9d471 | -3.44936 | -44.12927 | 2025-09-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5fbcafd-4639-391a-bda9-d9d91123e9e3 | -8.06934 | -42.94828 | 2025-09-26 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0c99fec8-9b9c-3888-b8f6-aa046838b433 | -5.1219 | -45.50188 | 2025-09-26 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b731f86-9f22-32fd-bdc7-d92b3295afac | -5.73295 | -44.99218 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd0eb57b-386d-31c6-a6cf-c2c77270fda2 | -10.57352 | -44.08115 | 2025-09-26 04:14:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8f03f1d-b32b-3561-b32e-6ec859cb4e18 | -7.11584 | -43.73608 | 2025-09-26 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50c579c2-7b8d-3e07-961e-1236ce4ba6e9 | -8.79653 | -43.01976 | 2025-09-26 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| edaa9cde-a9e5-3cc6-b973-2bf940f167fe | -10.19165 | -44.84325 | 2025-09-26 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fa02c82-b187-319b-b2ba-a700ed48443f | -5.24273 | -43.07164 | 2025-09-26 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80e143cc-fe36-372b-9fab-4aa6a5248616 | -10.19161 | -44.86492 | 2025-09-26 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4354bb05-8218-3121-89d4-4c79c6c4a5f8 | -5.63841 | -43.93198 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 29f1b795-072b-3cb3-afae-362a8fa0370e | -3.81056 | -52.08769 | 2025-09-26 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1f0ab7a-6f13-3e97-9e2b-625ed8315dd1 | -6.07285 | -44.73384 | 2025-09-26 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25a70daa-9d98-35ec-aa67-748cff75adfe | -10.17895 | -44.8376 | 2025-09-26 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23b96f2a-32e7-3a66-b760-d48fa350ad18 | -4.03592 | -46.93287 | 2025-09-26 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 223411a7-353c-3425-860a-49f53589eb67 | -6.96503 | -42.30236 | 2025-09-26 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 063de083-2ddc-3fd4-9e1d-e4d84c6ba07a | -8.71683 | -50.05295 | 2025-09-26 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d76c5bd6-3f9c-3698-851f-34ec991f192f | -10.23978 | -47.03096 | 2025-09-26 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2f10a8d1-b9e7-33de-b60b-d564af79c957 | -5.75969 | -42.90293 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 903b3f11-4562-354d-b8cc-3864abd621e1 | -7.67935 | -45.99446 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84635999-bd33-3199-9dc6-f8280b59bd08 | -5.30103 | -42.76385 | 2025-09-26 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0c95f154-4966-3e04-a1cb-ee5fc6c5f2c5 | -5.74673 | -44.97143 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 4841b728-2623-3237-884a-34ede0b57433 | -6.57155 | -43.47628 | 2025-09-26 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4d0e9fcc-33a2-3b09-9ae3-e1425c8d5961 | -5.73131 | -44.98043 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86cdcfce-20e7-30e8-b059-8e9d6ffe12d3 | -5.74496 | -44.98262 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91625a97-d2dc-3436-b9d8-f12688bcfe8f | -10.81163 | -44.43055 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4011f57-4821-3dab-a077-332430d7fe0d | -6.892 | -44.75952 | 2025-09-26 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 008865a4-5672-381d-a881-202ab82a6f4b | -5.75213 | -42.55589 | 2025-09-26 04:14:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8fe4d64f-88b6-32da-90e6-349bf3531b89 | -5.78302 | -42.8185 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 073c715c-7755-3cb3-b8c3-d9f3ae4dea3e | -5.1794 | -45.09348 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d64dcc7a-c1e1-3319-aeef-c85829a8c10d | -7.11792 | -42.1708 | 2025-09-26 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 640d4033-4247-31df-859d-56fa3f448bda | -7.0099 | -45.46508 | 2025-09-26 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01bc60ed-d52a-3b4a-959e-56ebe7c3530c | -10.57736 | -44.07819 | 2025-09-26 04:14:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8709705d-83ad-350a-9ecf-503425b1a2eb | -8.51783 | -44.62276 | 2025-09-26 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 615e43f8-c101-3c4e-ac21-331abce3d508 | -6.1334 | -43.44921 | 2025-09-26 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7d7da195-1e94-3908-b7e7-9f9b33d751b5 | -4.81134 | -42.74268 | 2025-09-26 04:14:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea52377c-8334-3740-a545-9a64b8ccbbca | -7.6028 | -42.99613 | 2025-09-26 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 50efe5c6-41e1-36a9-be7c-65bb74bcde58 | -5.78884 | -42.75943 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1c570e56-e9e6-3688-95d3-59170b83c138 | -7.67999 | -45.99056 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ed329bd3-8eb9-32f8-8f4c-b789fc275ad3 | -6.12957 | -43.45212 | 2025-09-26 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b2f1769d-d210-314f-a5d5-a34f665ea1b7 | -10.82751 | -42.69637 | 2025-09-26 04:14:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a9512288-65b5-31d2-bbbf-15f3d004b36a | -8.65176 | -44.01413 | 2025-09-26 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba00c995-6bd8-3195-ae22-657365ea5d0a | -10.92919 | -44.28867 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee2abc91-cbee-3572-9ad6-ec3012f78967 | -5.76406 | -42.89656 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8b481a60-ad14-359e-9f38-5d8f8a2742c3 | -5.78961 | -42.81953 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 6d3d5809-bef5-343a-b8aa-2f038f6a2178 | -6.87268 | -39.26439 | 2025-09-26 04:14:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 01120de1-7477-3d10-9fca-c6c1a0c42ca2 | -7.58968 | -42.33022 | 2025-09-26 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 64f1a773-ce62-341c-843c-aa2fd76b2c52 | -9.69582 | -48.9447 | 2025-09-26 04:14:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 1e6ffee4-27dc-3d34-93c5-7700d62bce90 | -5.72448 | -44.97939 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6d25358-a016-36c6-a027-6a82efd7e353 | -5.37538 | -36.81502 | 2025-09-26 04:14:00 | NOAA-21 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 08d965aa-dd29-3725-89fb-baef0007ba98 | -5.69678 | -44.44536 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 366ec5c6-b530-3ab4-b20a-8a1d5b127bf6 | -10.93273 | -42.78745 | 2025-09-26 04:14:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7b048346-42a1-3bbb-9f5e-9f26e4bda40b | -9.79984 | -42.21027 | 2025-09-26 04:14:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 42e57aa1-14a2-3e94-a349-d95622ae6e6c | -10.40467 | -46.16264 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d06f507e-524d-3891-9b83-997c90aa5311 | -6.25934 | -42.49017 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7514a4a3-bbed-36a7-8f49-38f75fb84753 | -5.91223 | -42.99081 | 2025-09-26 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5d2c622c-fafa-32fb-863d-4e205e71406c | -8.27525 | -48.00196 | 2025-09-26 04:14:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd98b8f1-1bf5-3130-82b3-ec2b11463974 | -7.55097 | -44.06549 | 2025-09-26 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91aade68-4f7a-3585-879f-eae2bc6c30f2 | -5.34175 | -43.19982 | 2025-09-26 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 16ce69f5-f2bf-3036-a39b-5c9456bc7317 | -6.91168 | -44.74427 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f94e23eb-8729-3fba-8df9-c2b29ee6eaf5 | -7.05667 | -43.03013 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d4ad9519-de6c-3c40-bb71-6b1329ac1530 | -5.20221 | -43.72 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eee50901-721e-36dc-9bfb-144047a182f4 | -9.34114 | -48.54567 | 2025-09-26 04:14:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| caf7504e-b48b-36d8-8dfa-13855ec34788 | -5.13689 | -45.38453 | 2025-09-26 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3224831-cbd6-3f9b-ad15-0d310955a18a | -5.03881 | -42.54624 | 2025-09-26 04:14:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e950c7cd-4649-3b13-88b7-b8c57dcad524 | -5.12252 | -45.49795 | 2025-09-26 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77508601-a088-3cb1-852d-0fe37a9b86c5 | -6.29063 | -45.04534 | 2025-09-26 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cca58b26-d6df-33aa-8b4e-4fdd2b3962a4 | -3.80298 | -41.56844 | 2025-09-26 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2b44c0fe-92b5-308c-929a-b9d0281a9f3c | -7.59022 | -42.32667 | 2025-09-26 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 598bb915-4f58-35b4-a59d-f47022ede923 | -8.73374 | -47.06859 | 2025-09-26 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da7e6954-e656-3fac-a94f-5974f2e9c462 | -9.03426 | -45.52826 | 2025-09-26 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a557cba8-65dd-36e3-8dc5-e41b5910806e | -10.39811 | -46.13827 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3741f5ea-532a-3c7a-aeaa-d01f7f177511 | -5.4825 | -50.12862 | 2025-09-26 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96cffab0-7af4-3b27-b8ba-3c562cba08ce | -5.46073 | -43.07049 | 2025-09-26 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f41786bd-0d31-3dec-a13a-4d446678db6c | -5.74114 | -42.56129 | 2025-09-26 04:14:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c0be7615-34d8-3e63-8698-0c6f688c41d0 | -5.51189 | -44.23703 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15d6b51b-d4ca-3d69-a1ce-63b7f18d90ea | -7.63816 | -47.69318 | 2025-09-26 04:14:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12643b26-5f73-315b-809f-36581c4c2cdd | -5.43047 | -41.31815 | 2025-09-26 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| afe0fe25-2029-331d-b627-0e917bbe0da2 | -5.70884 | -43.07116 | 2025-09-26 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d2233c02-82ad-352a-844d-75f4de1b8fdc | -4.38754 | -41.92386 | 2025-09-26 04:14:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d533810e-6190-3573-8d1e-6ea04ab87ea3 | -10.57461 | -44.07418 | 2025-09-26 04:14:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bd6df0c-ef26-3fda-b22e-1ff2130834eb | -5.12369 | -45.49808 | 2025-09-26 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bd82b144-8871-3102-a41c-f4e182a4d0db | -4.00995 | -43.27156 | 2025-09-26 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16924537-5802-3801-b257-84870696b921 | -5.40167 | -42.27053 | 2025-09-26 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1d84c07e-8bc1-3a08-9a5d-42d793881e64 | -5.74507 | -44.9598 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 40838b5a-8fcb-3b22-a089-0a26ff0d4823 | -2.91696 | -48.63245 | 2025-09-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 265463d4-c8e3-3fd4-83e9-2852168705e8 | -5.31741 | -43.13964 | 2025-09-26 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b4e64fa-8a0c-3067-b4e0-feb471a03c76 | -10.80888 | -44.42653 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4023e1a0-2800-39aa-a4cf-de7e46118913 | -5.73821 | -42.29452 | 2025-09-26 04:14:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d147171b-52ec-3f0f-be27-173017992ef7 | -5.63896 | -43.92848 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9ab74b15-4f76-330d-a78c-0e79e0ee4a60 | -5.1375 | -45.38063 | 2025-09-26 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| decbffc7-bd01-34a0-8af6-c6112d3bde79 | -4.8841 | -44.96277 | 2025-09-26 04:14:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2fc7fdc-9125-3b1d-a4b7-a83f38f4acd2 | -6.12288 | -44.22528 | 2025-09-26 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0f99123-bb56-3253-9b37-340e870da061 | -9.35516 | -43.25492 | 2025-09-26 04:14:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9b34db78-2459-3108-9b6e-2dd010ad0358 | -7.57337 | -42.41458 | 2025-09-26 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bd7e73ca-a4a7-3dc8-affd-e2f74b8e7ac0 | -2.9427 | -49.3368 | 2025-09-26 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ee093da-399c-33fa-8713-792664df810f | -5.75296 | -44.97623 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a802a702-2257-3b81-af65-e3513e8a6158 | -6.00827 | -42.72704 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1d9607f5-4645-3d58-bbb7-0897756f07ac | -5.37141 | -42.29072 | 2025-09-26 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |


[Clique aqui para ver as próximas entradas](README10.md)
