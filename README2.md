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
| 5601e834-d0a8-3274-bc26-26aaeb6df0ee | -13.65854 | -44.40546 | 2025-11-01 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 48a8662b-acf7-3776-a616-597989b66f4b | -11.72879 | -47.47721 | 2025-11-01 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f497f7e5-5e46-382d-ac9b-96a12d3c216d | -13.16824 | -42.27883 | 2025-11-01 00:11:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 7ab260e7-8ef2-30c9-bd6a-9bd420e6b483 | -13.44125 | -44.43659 | 2025-11-01 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e255c5ee-7e3e-335f-85d7-8c04aef7d494 | -15.33582 | -42.81544 | 2025-11-01 00:11:00 | TERRA_M-M | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8c6604bc-0fa5-3a66-b107-82fe27a773b2 | -11.81978 | -47.23446 | 2025-11-01 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3ae32649-4e42-3c16-b7f9-3b31bf235d25 | -13.1272 | -44.02567 | 2025-11-01 00:11:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 75d15e4b-c471-3f43-8caf-8b952d953da9 | -13.0104 | -43.84628 | 2025-11-01 00:11:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9d273b06-f7d3-39b5-b3c4-918372af49c4 | -14.0256 | -43.26286 | 2025-11-01 00:11:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| ee2ff252-d196-3b69-b402-c76b0c470964 | -12.62771 | -44.26759 | 2025-11-01 00:11:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 483469d1-b0e0-31c4-9a40-e1a8d246d51a | -13.36169 | -43.78866 | 2025-11-01 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3088ad5d-817b-3df3-b224-43374e944f91 | -15.7251 | -43.16076 | 2025-11-01 00:11:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 01cff97f-8ed0-3057-ac49-2a5ecf283f62 | -14.26682 | -42.16187 | 2025-11-01 00:11:00 | TERRA_M-M | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 8433c457-9a94-38a7-84ca-2228e5de3553 | -15.27441 | -43.16625 | 2025-11-01 00:11:00 | TERRA_M-M | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 52ec97d4-a76a-3631-b1ed-550640f3bded | -13.51572 | -44.30706 | 2025-11-01 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e6e9176e-6ce2-3801-a8c6-23ed2f30b0ec | -12.65306 | -44.25469 | 2025-11-01 00:11:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8961e1da-50d2-35d1-ac93-f8c77d6788c7 | -13.35686 | -43.09075 | 2025-11-01 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 5461fbc7-d53f-31ae-9345-b09b25bcb5d8 | -13.75397 | -42.44071 | 2025-11-01 00:11:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 7906e2f2-87fe-3a41-a713-c0c45a838b9c | -14.97854 | -43.56046 | 2025-11-01 00:11:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 89aea64f-47dc-3c45-a3ba-0cd4c7b5b660 | -15.12002 | -42.26257 | 2025-11-01 00:11:00 | TERRA_M-M | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c2f82113-ea8c-3a81-8f28-8c570f9d7dd7 | -15.3626 | -43.54422 | 2025-11-01 00:11:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5c53c2bb-2b6d-3bd2-90c7-5b153399d02e | -13.23513 | -44.61029 | 2025-11-01 00:11:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a7666a9b-6541-3cc1-8087-164fdae45001 | -14.91117 | -42.8018 | 2025-11-01 00:11:00 | TERRA_M-M | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2a1723ab-e502-3540-afdf-644783200639 | -11.97515 | -44.81966 | 2025-11-01 00:11:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 3ee7e6f8-372b-3ad0-a85a-7ae5b5ac4105 | -13.46218 | -42.59499 | 2025-11-01 00:11:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a207c83b-f9ee-39f7-93c0-ed5663e4d96d | -14.97711 | -42.88509 | 2025-11-01 00:11:00 | TERRA_M-M | MAMONAS | MINAS GERAIS | Brasil | 3139250 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a85d953a-59f3-305f-8b9b-935439c98c05 | -13.12969 | -44.04379 | 2025-11-01 00:11:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41131ad6-9fc3-35b0-807c-c92e26c56505 | -12.71837 | -43.79689 | 2025-11-01 00:11:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| f7845aa4-b3ec-34ec-9893-9c2bd211b7c1 | -15.73394 | -43.15942 | 2025-11-01 00:11:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 7db89ced-508d-3e3e-a292-8bad78a6d228 | -11.84369 | -47.65723 | 2025-11-01 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ae73b3b9-abb8-3631-986d-79aabd4e7ea1 | -12.16624 | -46.67794 | 2025-11-01 00:11:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ef000374-efbb-327b-a1cf-0e020cdf0d75 | -14.15289 | -44.32278 | 2025-11-01 00:11:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| eb7c9197-7ca8-3142-884f-1ff39f5d8d5e | -13.1602 | -42.28641 | 2025-11-01 00:11:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 19502526-e0a0-3f02-bd2b-917149696bb7 | -12.19739 | -47.07633 | 2025-11-01 00:11:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4adb4d7b-96d9-3c5e-8d31-9c9919d85e93 | -11.739 | -47.47594 | 2025-11-01 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 43.5 |
| beca9ac2-feaa-30de-ad93-d2278b87b6fe | -13.78362 | -43.17244 | 2025-11-01 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| eb1ce06a-c81c-3f59-abc2-852926c77468 | -13.01164 | -43.85531 | 2025-11-01 00:11:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 31833484-f771-36ad-8c9a-dd5f0d337b4c | -12.73444 | -44.37541 | 2025-11-01 00:11:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d0a432f5-bfcf-366d-bed4-192dc6c5353d | -13.78618 | -43.25533 | 2025-11-01 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| b8d1f13a-4287-39d1-818e-7043fe0bbac3 | -13.16961 | -42.28826 | 2025-11-01 00:11:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ade21504-244a-3217-83ab-73c96cbda870 | -11.66326 | -41.68711 | 2025-11-01 00:11:00 | TERRA_M-M | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| edc532f1-4290-390c-ace7-e715fa2e4acc | -13.20799 | -43.13791 | 2025-11-01 00:11:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 1019aa57-1e57-3f9d-b09e-cad2b65a3542 | -13.13691 | -44.01831 | 2025-11-01 00:11:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 102052e3-f788-3803-8436-523da61e4ea2 | -15.99015 | -41.77658 | 2025-11-01 00:11:00 | TERRA_M-M | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| a61b191f-ea62-3604-8bb0-ae2865455b86 | -15.10975 | -42.25458 | 2025-11-01 00:11:00 | TERRA_M-M | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| fbd9dae9-f64f-325c-b802-013f9a0f7a6e | -5.101 | -44.2714 | 2025-11-01 00:13:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| bc068391-95e9-3afd-a967-414529ae5890 | -4.75946 | -44.46471 | 2025-11-01 00:13:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 53410a0d-1387-3a01-9767-18661ed097b0 | -8.21362 | -43.59895 | 2025-11-01 00:13:00 | TERRA_M-M | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ef9066e9-9a24-31a3-998d-db0e10a403a7 | -8.23854 | -46.25205 | 2025-11-01 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 71f676c0-0eb6-36f8-a143-ad87c9b65f55 | -6.62733 | -44.57784 | 2025-11-01 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 53625397-ed2b-332c-aa52-30c686376536 | -4.75054 | -44.466 | 2025-11-01 00:13:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 5dbeac8c-c1d0-396a-9f1a-58d3ffe5de4a | -4.94754 | -43.45111 | 2025-11-01 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 63b5ea29-4a4a-3cbf-9ae2-ff5c51fe33c6 | -5.72658 | -44.53148 | 2025-11-01 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 8422bcb6-b99d-3495-80d0-7d63bfa36c59 | -7.35015 | -46.21637 | 2025-11-01 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1362d671-4921-382e-a2b9-5d1960393b65 | -5.08685 | -45.42857 | 2025-11-01 00:13:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 56b78672-6a3f-3a20-bcf3-e14671f5b72c | -7.25802 | -47.71053 | 2025-11-01 00:13:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 10926dd1-eae5-3e64-b6c9-920e7bd92e9c | -5.52258 | -41.09292 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 50c0e313-13b9-33e9-abdc-28ea4b28bfcd | -5.22054 | -44.80338 | 2025-11-01 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9e6eb5f1-24fb-37c7-8781-4c0efb5dd63a | -5.46118 | -45.40535 | 2025-11-01 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0d8cbf77-c729-383f-8c1f-d72d21d44cd4 | -5.93241 | -43.3665 | 2025-11-01 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 36fdeb56-cc68-33cf-8dc9-55b06c2bee3d | -5.51687 | -41.08571 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 8dcd3889-e56b-37fe-8239-ade5fa0d9ef8 | -4.67975 | -40.3905 | 2025-11-01 00:13:00 | TERRA_M-M | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 15.6 |
| b7ea1dc0-b95d-3697-b7bc-b1b53fc10b68 | -6.13404 | -45.93783 | 2025-11-01 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| ed9e8d1f-93b7-3dde-93a4-2293f620d658 | -7.53075 | -47.29208 | 2025-11-01 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 07626a56-77a3-3dd4-99fb-e94c1a8f0098 | -6.43043 | -44.68164 | 2025-11-01 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d5ab9bcc-e348-38cf-b5cf-1bd1dcc72c68 | -6.40968 | -46.00079 | 2025-11-01 00:13:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b534f299-abea-3d94-8a4c-5ce8b7a41720 | -6.03856 | -40.24068 | 2025-11-01 00:13:00 | TERRA_M-M | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| f7926cc6-4a8c-3435-9f36-2374983e5eaa | -6.47011 | -43.19233 | 2025-11-01 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 664d49d0-c1cb-3c82-abc4-a6cfbb659a99 | -5.11624 | -43.39065 | 2025-11-01 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 04e90bb4-dfbc-366e-8099-d9d2cfb6ea90 | -5.63769 | -46.96363 | 2025-11-01 00:13:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 83f99133-3520-3f08-ac0e-1bc270c664bf | -6.87846 | -34.98358 | 2025-11-01 00:13:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 36.4 |
| b5254879-b1b9-3a3d-a033-149add5e1af0 | -11.56466 | -47.07495 | 2025-11-01 00:13:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 91f2f104-63aa-3ecb-92ee-90337e6d644f | -6.03943 | -40.24944 | 2025-11-01 00:13:00 | TERRA_M-M | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 81aa05b5-12f3-3ea3-a537-19dc19bc46b7 | -4.92076 | -45.96553 | 2025-11-01 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| e03a80d2-cf45-315b-8800-02afe658d299 | -5.23721 | -45.05373 | 2025-11-01 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 58c47956-f18d-3a3f-b607-1f4d647f3781 | -11.44039 | -48.17445 | 2025-11-01 00:13:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4a25fd8f-b600-328a-99c9-ed535fca3864 | -6.57781 | -48.72694 | 2025-11-01 00:13:00 | TERRA_M-M | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 52157898-2e0c-3cb7-b800-9d79f8c4b1ad | -6.27149 | -47.2181 | 2025-11-01 00:13:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 98b10bef-a484-3b2c-a55b-001ac88d4f02 | -5.22057 | -45.92629 | 2025-11-01 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c92eb403-d608-3b0b-a755-1f317e16c8ff | -6.26704 | -43.97812 | 2025-11-01 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7ca6d1e7-f45c-3e09-b84a-667bd4e1bc6b | -5.07065 | -45.11655 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 92970aed-7ba9-358a-bbf9-5b75114cd502 | -6.22741 | -46.75806 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 599c1ac7-b3ca-393a-8654-0257763e3d73 | -6.81606 | -46.76063 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b9b988b9-93ce-3de0-b193-3683c90eb779 | -5.03671 | -43.61562 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7b35b304-1bd8-369c-b030-d5c63a135765 | -4.80637 | -45.594 | 2025-11-01 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a885cf0d-9187-3ade-b636-c16c5bbe111d | -7.92377 | -41.60168 | 2025-11-01 00:13:00 | TERRA_M-M | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 638954f5-4b1b-3230-983d-99fa884726af | -8.88922 | -44.40882 | 2025-11-01 00:13:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bbda3eb9-5007-3ae8-8b2d-a6b653b8094e | -6.89736 | -35.02603 | 2025-11-01 00:13:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 150.8 |
| 2be75b2c-1c70-361c-9db2-123e57cc890f | -5.1176 | -43.40038 | 2025-11-01 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0bb6d6db-2812-300c-8cf4-2673d309ba6d | -7.45315 | -46.70932 | 2025-11-01 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ab9aa861-c3ce-3fcc-8c79-4a8429bd87dd | -6.88124 | -42.84002 | 2025-11-01 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 16ca6c47-8a2e-36d9-84d0-11e91b81b9a7 | -10.658 | -45.15403 | 2025-11-01 00:13:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| a1e36874-2b80-34e4-9bf3-58786362f06f | -4.7656 | -45.42918 | 2025-11-01 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c09679c9-b9de-354b-b034-0518ecb24974 | -10.33957 | -44.64562 | 2025-11-01 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9af0a9ea-ab63-381c-8cab-77a0ffb46c80 | -6.81478 | -46.75107 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fdba331f-a5ed-3808-bca6-d7efe2a7bca5 | -6.32911 | -43.63352 | 2025-11-01 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| e3b0c250-5c11-3644-b53f-92b87abef62b | -5.45235 | -45.40659 | 2025-11-01 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d28a5742-bb3b-30ba-bf19-f6b3a5d96142 | -11.37441 | -48.92789 | 2025-11-01 00:13:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 72f2d14d-f5cc-3b7d-8643-730da78566ad | -6.69255 | -38.19577 | 2025-11-01 00:13:00 | TERRA_M-M | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 13.0 |
| b55fdc72-324b-371c-a5f2-d2faacbb5c21 | -7.69776 | -45.99606 | 2025-11-01 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |


[Clique aqui para ver as próximas entradas](README3.md)
