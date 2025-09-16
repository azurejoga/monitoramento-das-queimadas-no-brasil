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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24c8fcc1-3d6b-3da3-8e18-8c3ca72e3cde | -22.2061 | -48.35545 | 2025-09-16 04:34:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 46cc4204-a9c8-31de-a4a8-8d8d2faa4b6e | -23.18943 | -49.7824 | 2025-09-16 04:34:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2edd375e-83e3-3a1e-9ac1-c583153aef28 | -23.25793 | -48.28495 | 2025-09-16 04:34:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3f12ea37-8733-36f7-95e0-ace3e4c0619c | -23.00092 | -49.78018 | 2025-09-16 04:34:00 | NPP-375D | CANITAR | SÃO PAULO | Brasil | 3510153 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b37a9f38-6113-3cd9-90b6-04ccd7ea0a32 | -23.23567 | -51.0056 | 2025-09-16 04:34:00 | NPP-375D | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c2a2de63-0ab5-3315-9f39-2ab3e2848182 | -22.99352 | -49.93762 | 2025-09-16 04:34:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6e1eb1ac-090f-3dde-9657-6b751d0c6a0a | -23.16088 | -47.63823 | 2025-09-16 04:34:00 | NPP-375D | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6236d86d-5790-320f-8f84-4efbd6031d73 | -22.98901 | -49.94453 | 2025-09-16 04:34:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| deb785c7-d477-3caf-8ee2-d9d2514b8670 | -22.60215 | -47.65641 | 2025-09-16 04:34:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d14bfb17-1c61-3750-bbba-aac329e54cb5 | -22.22743 | -48.6102 | 2025-09-16 04:34:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1254921b-1c37-3328-ac3f-18295b132d9f | -21.92263 | -48.2499 | 2025-09-16 04:34:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ada85134-d23b-3ad2-baf0-8fc446dcc783 | -22.33045 | -46.52728 | 2025-09-16 04:34:00 | NPP-375D | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3d8644f7-531f-307b-9915-6f14482eb177 | -23.34444 | -51.06459 | 2025-09-16 04:34:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2e8dc0e5-33d9-3648-a366-8103484812f0 | -22.98116 | -49.95082 | 2025-09-16 04:34:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6623e335-75f2-336d-974a-0be140657abd | -23.19884 | -49.63242 | 2025-09-16 04:34:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f6c1940c-cde7-3d51-a5bd-84f48bf75d2c | -22.9896 | -49.94077 | 2025-09-16 04:34:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 70d9f0c5-09d9-3b00-b3c7-72e6fa5d02be | -22.1687 | -49.61192 | 2025-09-16 04:34:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| df8350d4-a0a2-3c03-a5e3-34272f27bb30 | 1.59256 | -55.75538 | 2025-09-16 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| faba2d19-d83e-315c-a318-393c6085d29a | -6.55639 | -54.98214 | 2025-09-16 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a772f321-49cd-3bf0-a2bd-35012d1173cb | -6.46337 | -46.00832 | 2025-09-16 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d230cc3e-1ede-305b-85ae-26e4b26562b2 | -3.7385 | -49.04866 | 2025-09-16 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f1d9dd71-eeaf-3377-adb6-3481fdb47733 | -5.79456 | -45.94092 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb9815d0-ed95-360e-bef1-c1cffd174b18 | -8.12202 | -48.27083 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e2707bfd-c33e-3b2e-a358-5d27ecb09a3f | -8.00407 | -45.66514 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6c93768c-54ca-3634-87d9-13e221d38355 | -7.3157 | -43.96428 | 2025-09-16 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b5bec47-acd3-3daa-aea0-be08b3893191 | -7.38347 | -49.99 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3dd4e77b-621c-3d93-a88d-e73a27e90b64 | -7.9935 | -45.65711 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 258f0c99-4c21-395d-9e21-5a23aed0b529 | -8.12128 | -48.27594 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 442e9252-fa7f-3a17-804f-03b0d9e26322 | -6.16284 | -45.99598 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 338de08d-9972-3738-9d6c-ed6d191921eb | -7.99819 | -45.65781 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0e7becfa-5904-3881-a3e0-93a7c9b2c8de | -6.16037 | -45.11429 | 2025-09-16 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 72acc9a4-9072-3001-8de6-d9fe97127fdf | -7.515 | -44.66772 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3201400-014a-35e0-8b06-0183c8c38c62 | -7.97669 | -45.64022 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61e42267-afa0-36f7-85a8-65a28fdc9a9e | -7.68425 | -44.47705 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5df0f6c1-a115-39bb-98d8-7714be4ee543 | -7.67957 | -44.4734 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08951142-f9bb-3e2c-8a94-3da5751f2ff3 | -3.82593 | -44.11325 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0ae7693-fe49-324c-a9a5-a6b920136226 | -5.20781 | -45.18328 | 2025-09-16 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e231259c-f2b0-397f-bfe8-f97c3ef4b5c4 | -5.79349 | -43.94108 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b970c83-7d4a-3bc0-8135-06e1bcacc883 | -4.74215 | -50.94211 | 2025-09-16 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 261f29fd-9db2-382b-a16f-b7f507ca663f | -7.69401 | -44.66624 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85686768-3569-3b42-9c33-e13b4dc247e3 | -3.1269 | -48.59309 | 2025-09-16 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00e96389-b1e7-3897-a668-04a39e7836a2 | -5.77237 | -45.90575 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b13c366-ff1e-3b53-874e-c1f2b4ccc904 | -6.96913 | -44.44753 | 2025-09-16 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7186fb29-1d59-3a84-8667-8563d2e1f2ce | -6.22013 | -43.90493 | 2025-09-16 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2cbd0527-e636-3093-a00a-c0bcabaec8c9 | -5.55643 | -44.96952 | 2025-09-16 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0c0578e3-601f-3ff4-9864-6ffebca809c6 | -3.83334 | -44.09761 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 138f10bb-35bc-3a38-a6e6-e475a54f5a01 | -5.53286 | -42.66053 | 2025-09-16 04:49:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 8fdba94a-8d63-368e-9274-29d1913ab097 | -5.78568 | -45.93937 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5948ce3-9977-3ea6-9a5a-57b38ccde8b5 | -2.57056 | -48.39425 | 2025-09-16 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7616a78c-61dd-3656-bfe5-613e1da8eec6 | -3.89266 | -42.51709 | 2025-09-16 04:49:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d0e7d592-d938-326c-94da-8f4b0c0e6bd2 | -6.18811 | -41.18344 | 2025-09-16 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c0c609c5-dc80-3189-a822-57547d422378 | -5.9841 | -45.83649 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71350cae-e4b1-3883-ac78-b4ead3b7eff1 | -5.79586 | -45.93214 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45fa8503-e5d1-3c25-b67e-20f364f4bcb5 | -4.60052 | -43.32067 | 2025-09-16 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 646381be-2bf0-3ace-8f5e-5836a85050ee | -6.26629 | -43.4734 | 2025-09-16 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a539335f-1adb-3659-83fa-ace4fb1db5e1 | -7.13381 | -47.97122 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3703a9a2-91fd-343e-b289-f9e2c43d5ae1 | -6.08068 | -50.17061 | 2025-09-16 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a69d3e24-3b6a-394c-89ee-be0cfdc62881 | -6.18681 | -41.19309 | 2025-09-16 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f2fe327d-cd3a-3726-bec0-e1d78b81c3cc | -3.81857 | -44.10794 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17f9cfd7-d147-3cce-bb4a-3dfc88cff24e | -7.27849 | -46.60722 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1bb5afe-49d6-39ea-a1d3-b6f375bd17b0 | -4.05766 | -46.94023 | 2025-09-16 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2719e3dc-92dc-3621-8261-3b46d5593860 | -7.27153 | -46.59365 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 470e9105-cb79-3cae-800d-12840e4e827d | -7.72108 | -45.30662 | 2025-09-16 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3d80523-c211-375d-b777-20b7dfada1a9 | -3.07699 | -48.81878 | 2025-09-16 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ab09587-e340-358f-b582-cf7d7c435938 | -7.98876 | -45.65669 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59da7a82-ee70-3116-9939-2fb92fc20f69 | -7.31042 | -43.92464 | 2025-09-16 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8861877-3e4c-3788-b597-e157f425b2c1 | -6.62943 | -45.57507 | 2025-09-16 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d16b90ca-4046-37e4-a6ac-196e7cb61814 | -7.98401 | -45.65634 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d35b68fe-36b0-3ae3-9785-29fa3670d2a6 | -7.19237 | -48.60538 | 2025-09-16 04:49:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a640968f-2b2b-3bc8-8484-f1b65fe23f9f | -7.27211 | -46.58958 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 096cc600-40b3-3514-8796-3f0cf327b502 | -4.17782 | -48.5671 | 2025-09-16 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e0d3bf0-6fbc-3908-9b77-aaab9091db01 | -5.78794 | -43.94336 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 133f53b3-1c92-3266-a125-6303a6e3d709 | -3.22169 | -47.12816 | 2025-09-16 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3b5233b7-37d9-3529-a034-c0f79ea64623 | -7.70595 | -45.30978 | 2025-09-16 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae5c38d7-9b22-364f-84eb-f10791b5bd74 | -3.85748 | -52.16099 | 2025-09-16 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 342d6ea7-aad1-3e7c-89be-9b3fdcf8b007 | -5.34678 | -44.82877 | 2025-09-16 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0251c932-eac0-3b0d-a558-0b82d780969d | -5.98548 | -45.79493 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b79d64b0-5d12-3fb8-ac9d-1adad9ae2bbe | -8.19945 | -45.54975 | 2025-09-16 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4ba2ccf-6376-3cbc-b75f-595a1c634252 | -6.12775 | -42.94573 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c0ded356-6c70-3211-a8a9-17551cba1007 | -6.40866 | -43.34035 | 2025-09-16 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e103902-56dd-3cb6-849d-ac44f52a4b15 | -3.65084 | -54.05945 | 2025-09-16 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbc3ceae-8954-3f06-9bb8-705500ee6b1a | -7.14097 | -47.97755 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 54bb19b8-bc64-3623-8eec-45204934a002 | -3.85198 | -48.97839 | 2025-09-16 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92da9ce5-e9d6-3fd6-b7e5-2c6d349eb4ba | -7.672 | -46.30359 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73542baa-5646-373a-a000-aae6de02965e | -6.97678 | -44.53764 | 2025-09-16 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b96f34e8-632a-35a8-a808-0f62d73ea7ea | -7.43804 | -46.17732 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3ed8905-710a-34af-832e-c4d60ecbb187 | -1.64173 | -48.51498 | 2025-09-16 04:49:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55451424-0779-3eb6-9b65-98d2f7c39f20 | -8.12277 | -48.2657 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 61ea3243-3d6a-3fcf-94ed-75e067255ca4 | -6.1563 | -45.11586 | 2025-09-16 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a4caa99-614b-3e23-82ff-848d14445b63 | -5.78632 | -45.93502 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17614d22-02b0-3c79-b780-7838d3073746 | -6.43758 | -43.31012 | 2025-09-16 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b991219d-25c8-33f4-b13e-1690eb185518 | -7.26975 | -46.60615 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d2031969-5557-3206-b970-d978aa33598e | -8.00472 | -45.6603 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2e1608c2-f4f4-3e4d-9fa4-f2ceeccb14f1 | -4.48635 | -48.11576 | 2025-09-16 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 522e15c2-56c2-3340-84e8-a5cb9f15dbfa | -6.17841 | -41.21412 | 2025-09-16 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0976c727-4a25-30f0-9873-a2a38c3e5cc4 | -8.18841 | -47.11892 | 2025-09-16 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53956d0c-f490-3a2e-9df6-4798cad4506f | -6.44221 | -46.1118 | 2025-09-16 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53961a35-b99d-3360-b170-17cfc10c16b0 | -2.67216 | -54.78951 | 2025-09-16 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 699fbe2a-bd38-348e-b4e5-0a9c93d79098 | -3.73911 | -49.04461 | 2025-09-16 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8e94e6cd-3ce3-3c90-b507-fc62d80a76b7 | -6.52672 | -41.82668 | 2025-09-16 04:49:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README61.md)
