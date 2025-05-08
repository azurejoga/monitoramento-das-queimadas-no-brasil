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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d02bf470-2056-3472-86bc-1f8891704bed | -14.6414 | -45.1263 | 2025-05-08 02:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 6df3fff1-f4af-39b4-8d7c-ed273d025cd8 | -8.07 | -43.1216 | 2025-05-08 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.0 |
| b043b9a2-d673-3251-bf00-11ac79526345 | -14.6409 | -45.1497 | 2025-05-08 02:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 6ae9c880-3b13-3eca-9992-6b7f081c6a50 | -13.5093 | -52.9692 | 2025-05-08 02:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 652e3bba-37ff-3485-b587-dbb53d69cdc9 | -14.6414 | -45.1263 | 2025-05-08 02:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| c75ed994-c673-3dfe-8783-ac6967c1167e | -14.6409 | -45.1497 | 2025-05-08 02:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 903de3ac-ae6c-314c-bf46-7dd49af647a5 | -8.07 | -43.1216 | 2025-05-08 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.2 |
| 75fd9509-4fbf-3821-b1f2-0b3764de1a05 | -8.07 | -43.1216 | 2025-05-08 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.2 |
| 8193d526-580b-3531-921e-e3ffa3dbb5fa | -14.6414 | -45.1263 | 2025-05-08 02:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 4ad0ca91-2fdc-32a4-93d3-d857ac402883 | -8.07 | -43.1216 | 2025-05-08 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.4 |
| 63c2685a-48b8-39fe-9acd-b0b21e68b767 | -14.6414 | -45.1263 | 2025-05-08 02:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 8b2f04a1-dca3-3fb2-a309-9d5d83087c8f | -14.6409 | -45.1497 | 2025-05-08 02:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 482efd99-b971-3841-a891-4c97897bc2b8 | -14.6414 | -45.1263 | 2025-05-08 02:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| f6d6abf8-e91f-38d6-ba4f-104884399390 | -14.6414 | -45.1263 | 2025-05-08 02:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 50b20edc-3fa7-3159-9208-9bfe154a770e | -14.6414 | -45.1263 | 2025-05-08 03:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| e257cfb8-4bfe-3621-a10f-d91ab17bc682 | -8.07 | -43.1216 | 2025-05-08 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.0 |
| c9f97bdd-d1dc-3593-be0a-c437267434d6 | -14.6414 | -45.1263 | 2025-05-08 03:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 975b4249-dd97-3241-9296-ef6b675482e3 | -14.6414 | -45.1263 | 2025-05-08 03:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| b710eeaa-600c-3034-a41c-a58e61d6b782 | -14.6414 | -45.1263 | 2025-05-08 03:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 840e7f4b-9e6a-3c7a-ae65-154fd274ee21 | -14.6414 | -45.1263 | 2025-05-08 03:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| aa10a56a-91d1-37f1-8076-2b877b55dec2 | -8.07 | -43.1216 | 2025-05-08 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| fd1b5e8c-409b-3a19-ae93-f932c550178e | -3.99325 | -43.24556 | 2025-05-08 03:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00aae0e7-f6e5-3498-82f5-46a44bb885ea | -5.66924 | -35.49195 | 2025-05-08 03:42:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ff0c1149-df04-326e-8527-fcd345e65b48 | -3.99695 | -43.24907 | 2025-05-08 03:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44d6bec9-dc8c-3a65-9558-af63e8cc453b | -3.99645 | -43.25214 | 2025-05-08 03:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fbe5767-31e2-36ef-bc50-0c20470632f7 | -5.06564 | -37.66809 | 2025-05-08 03:42:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| d98b8202-8869-3065-a7a9-2e00b93ccbc4 | -4.89717 | -37.52876 | 2025-05-08 03:42:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e4962934-5edc-325f-9e69-50533070c077 | -3.99841 | -43.24642 | 2025-05-08 03:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c344c4f-c190-38cc-b87e-2f4a5bb1ecd5 | -3.99272 | -43.24862 | 2025-05-08 03:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1048404-36fa-374c-a1a3-7b5749353476 | -5.86472 | -35.34451 | 2025-05-08 03:42:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5ff622f4-641d-3a94-9485-e8bf422c8a3d | -5.16681 | -35.88607 | 2025-05-08 03:42:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d300c81e-0957-3e5a-90f7-b89e6336f34c | -3.99745 | -43.24601 | 2025-05-08 03:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e1e791b-460d-3832-867b-b4d295af97a8 | -5.0692 | -37.66866 | 2025-05-08 03:42:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5108cedb-d4b5-38d1-8bcb-66a02d86f404 | -4.21199 | -38.11819 | 2025-05-08 03:42:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 593edcb5-4db8-32b5-8edd-bb431594bac2 | -4.89363 | -37.52819 | 2025-05-08 03:42:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 264f0185-2a87-311d-829c-4c204e3c5bfe | -3.99788 | -43.24948 | 2025-05-08 03:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4715c3c-bba8-32a5-a6fe-7951508c274c | -10.71974 | -42.32359 | 2025-05-08 03:45:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d1ede30b-ed0e-3040-87ff-359424e5a012 | -10.72755 | -42.32217 | 2025-05-08 03:45:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4edabbcf-8b86-35e9-b415-788e9c9de648 | -10.72251 | -42.32552 | 2025-05-08 03:45:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fceb3e37-cde5-3d21-a72f-288b77a2354c | -7.30936 | -37.42307 | 2025-05-08 03:45:00 | NPP-375D | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| eb637802-4800-3029-8053-1e8580ea7914 | -5.6403 | -44.30198 | 2025-05-08 03:45:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb9dafe3-d9c4-3e5c-a706-f2d9d799de97 | -10.72482 | -42.32024 | 2025-05-08 03:45:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d37ca1d5-5f0d-3520-8d43-c756845e7357 | -5.16884 | -45.1083 | 2025-05-08 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 696c5ff3-1cc6-3f9b-95db-0353369ed237 | -7.1848 | -35.31842 | 2025-05-08 03:45:00 | NPP-375D | SOBRADO | PARAÍBA | Brasil | 2515971 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| aeead32e-56c7-324d-8a6c-d9985c951084 | -10.71891 | -42.32056 | 2025-05-08 03:45:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6480b5d6-5012-32bd-a548-f93f1feca751 | -6.84298 | -42.79036 | 2025-05-08 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b75b7e35-e212-321f-83d6-0c8635dae37d | -5.16223 | -45.10835 | 2025-05-08 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28a610c5-7d0f-3269-b7fc-9ed24cfa4124 | -5.79339 | -43.61717 | 2025-05-08 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3b843ca-7ace-3b6c-b6b4-ce584815aaba | -5.7939 | -43.61424 | 2025-05-08 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bd15bb4-1e1a-3631-a172-6e5e78b24b43 | -8.0715 | -43.12445 | 2025-05-08 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.5 |
| ce704afe-6516-3502-b263-a258edb0f6e2 | -10.9835 | -44.44719 | 2025-05-08 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f961a661-78c2-328c-9f42-ae57dc114fe1 | -12.443 | -38.16238 | 2025-05-08 03:45:00 | NPP-375D | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0ffc074b-4467-36c5-9f4a-935f7688b5f0 | -10.98351 | -44.44589 | 2025-05-08 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df279703-0821-3b22-afd4-b67e52e840f1 | -11.77104 | -48.7062 | 2025-05-08 03:45:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9904bff-b26f-32ac-8b6b-51669a092639 | -10.98952 | -44.44254 | 2025-05-08 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c29dd6af-44f2-38b5-bc6d-6d9b133a5ea5 | -6.9783 | -42.79963 | 2025-05-08 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 388948a2-2b51-3809-8040-b2ba42ed2e39 | -10.7205 | -42.31945 | 2025-05-08 03:45:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| aac1ef5a-2759-3389-81ba-1ec66728d5f0 | -6.37928 | -39.25214 | 2025-05-08 03:45:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 891080b4-6ea1-30c1-b1ae-c92192b6d302 | -8.07059 | -43.12965 | 2025-05-08 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| b1a94d24-9b30-3810-87af-1a417c34a451 | -12.29709 | -43.54236 | 2025-05-08 03:45:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45e4e52f-fefc-338e-8a6c-9cdbba53bbd6 | -5.16386 | -45.10318 | 2025-05-08 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0383b0af-cd1b-3f5b-b263-cd017cdeac06 | -8.07627 | -43.12533 | 2025-05-08 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 9acc0e35-00c3-31f3-95bc-550c558e809f | -5.16929 | -45.10155 | 2025-05-08 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e800495-f90f-3e52-8f6d-f79383109148 | -10.67103 | -44.38651 | 2025-05-08 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd904ef2-8d68-34dc-8bea-5cd24698120e | -10.98845 | -44.44692 | 2025-05-08 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fc1ba258-9034-328b-b22f-bde1879383f7 | -9.80102 | -37.48651 | 2025-05-08 03:45:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8c1ab58b-5a9d-30d9-97b6-1e8af323b239 | -10.98949 | -44.44124 | 2025-05-08 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a5396a9e-d584-3895-87bd-aeea4608b2e0 | -6.84212 | -42.79539 | 2025-05-08 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ae9de9bb-1b28-3d8b-a485-0163d30b14ef | -10.72323 | -42.32135 | 2025-05-08 03:45:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fd37277f-bb8f-3256-b70c-6af8fc6f6439 | -6.9839 | -42.79547 | 2025-05-08 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7524975c-a4b6-35aa-be62-da21b851e9a2 | -6.98305 | -42.80053 | 2025-05-08 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bf0371de-7c4c-3aed-ba28-8a76ad3217d5 | -6.69686 | -42.13371 | 2025-05-08 03:45:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 2484d2d8-cde2-3ad5-b740-eefd098ed77d | -6.97808 | -42.80142 | 2025-05-08 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f9aa068d-12b7-38b0-9b81-127bbc1d227b | -10.72913 | -42.32105 | 2025-05-08 03:45:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 05c78c82-5ae3-349a-9480-0357c1ce3187 | -12.29623 | -43.54707 | 2025-05-08 03:45:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52485575-9732-30c4-ac58-c524e44658cf | -8.65307 | -44.26554 | 2025-05-08 03:45:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3560b9c8-86c3-3451-b15d-a7312d54bdd0 | -6.70061 | -42.13922 | 2025-05-08 03:45:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| bf332ae7-96b4-3c48-8427-3e28d78ab49a | -8.06968 | -43.13491 | 2025-05-08 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 857856d8-f4b3-31f6-ae9e-00f5e463ae4e | -7.47588 | -34.84219 | 2025-05-08 03:45:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ebd1f06d-36fc-30f6-95fa-7795152c7080 | -6.9581 | -47.93475 | 2025-05-08 03:45:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe7605b4-08c1-3d9c-80de-9f168535683a | -10.72838 | -42.32518 | 2025-05-08 03:45:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2d6ec21b-4f29-34f3-acb0-8082a912e12b | -5.16291 | -45.1044 | 2025-05-08 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42bb22f7-acbd-3d9d-90a6-408c574ac9d9 | -5.16792 | -45.10957 | 2025-05-08 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2dd6f80e-e0db-3da8-a515-110948ab9840 | -9.76183 | -41.87835 | 2025-05-08 03:45:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ee783fc-c2b5-3fe2-b599-869ac4801ea3 | -6.98372 | -42.79727 | 2025-05-08 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a9d40084-960c-34a0-bb87-1305f8de4e15 | -6.98283 | -42.80232 | 2025-05-08 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eac938d5-143d-3ca3-bab8-cda9a516f50b | -10.66605 | -44.38564 | 2025-05-08 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0e96b9f-29aa-3753-b28a-d5aa6a78adb5 | -11.77768 | -48.70457 | 2025-05-08 03:45:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2050f98d-e568-31e7-8686-0a23ee7f2de6 | -10.67167 | -44.38454 | 2025-05-08 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5be7e88-1bfc-37c0-9c15-eb3e2244ee1f | -7.07116 | -44.38729 | 2025-05-08 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52b4dd7b-2532-38bc-9f6c-22fc6fe805cc | -8.07537 | -43.13053 | 2025-05-08 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 5e35777a-9123-3f25-bd54-43de7e8a76a4 | -8.65814 | -44.26672 | 2025-05-08 03:45:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27fb68f0-bddc-3bbf-b31c-91751ba5741f | -5.63968 | -44.30546 | 2025-05-08 03:45:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ffe8f750-f9e7-3aac-86f0-53d9f0864fb2 | -10.71459 | -42.31977 | 2025-05-08 03:45:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 40053373-ce2b-35b9-9fa4-ad2299034493 | -5.16956 | -45.10427 | 2025-05-08 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ecc0fc5-623e-37c1-b6b9-87946beead59 | -5.16357 | -45.10054 | 2025-05-08 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a845e852-db87-3722-b22e-e4f4f2d3d90a | -10.72406 | -42.32438 | 2025-05-08 03:45:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b0d26202-ca82-3222-9582-b1216c1e0344 | -10.98844 | -44.4482 | 2025-05-08 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ab636c5-9262-3c28-aa9c-82a470fdf3dd | -9.76111 | -41.88247 | 2025-05-08 03:45:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7a628506-da3d-3342-bf30-cb61d7fab24e | -5.16315 | -45.10711 | 2025-05-08 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README4.md)
