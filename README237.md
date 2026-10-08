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

## Dados Diários - Página 237

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 427782c6-c042-333d-88bb-1a08ebf1b983 | -6.52417 | -43.53724 | 2026-10-08 15:41:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 35af7bab-9209-38c2-8f7b-081e46c3a1f9 | -6.93152 | -45.2564 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 806868f1-6a7c-39f5-a478-5171646de187 | -8.67555 | -41.19081 | 2026-10-08 15:41:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 9.2 |
| cd93e573-0477-3d35-879a-7b813b3fe84d | -6.59341 | -44.8535 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c9173ed4-f943-319f-8141-ec9567b6195c | -6.21978 | -44.85732 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| afef633c-040a-3615-b212-848d30e9ca1e | -6.15359 | -39.43728 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 984a893c-1fce-3de4-8b97-7af5d7d405a0 | -9.892 | -44.86332 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 296.9 |
| ff27bcd9-751e-3765-abf7-835394732186 | -5.75552 | -41.62682 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ba1a8136-a7f6-3c6a-aa24-eba956944b60 | -7.03678 | -45.45759 | 2026-10-08 15:41:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3dfdefad-a262-301e-a442-154ac5a0aa4e | -5.94786 | -45.688 | 2026-10-08 15:41:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 58433ba9-03e7-3944-b17b-1886a6d86bfa | -6.41273 | -39.26184 | 2026-10-08 15:41:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 15.7 |
| a198729a-7c15-3590-9ff6-1dcca241416b | -7.45604 | -40.17429 | 2026-10-08 15:41:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 27.4 |
| ff0914a9-6ca0-3514-9698-0247f89a407f | -8.95627 | -45.15911 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 63d01538-66e2-3a74-a27c-d0d519764bf8 | -11.19972 | -45.22455 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d0e3b98c-6d2a-310c-9be8-08b52bff2ee0 | -7.76659 | -44.17084 | 2026-10-08 15:41:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7d37406d-2c15-3150-942c-c8092a787071 | -6.60069 | -44.84439 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fbc0ef7f-1554-3a77-81d7-50e4ee368ffc | -10.58267 | -41.20043 | 2026-10-08 15:41:00 | NOAA-21 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 49.7 |
| 6b9fdc4d-41bc-310b-a8d1-73a7de338f90 | -6.12197 | -44.14249 | 2026-10-08 15:41:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf64a618-b84d-3a78-8f56-e44ee1d1f7c6 | -8.94697 | -45.18139 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3d6c2296-aaa2-3b4e-b9e8-b23a5889db54 | -5.45024 | -42.90553 | 2026-10-08 15:41:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 698966d1-66db-394f-a6f9-9da1b4c23f68 | -9.97034 | -43.50077 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 80df6529-6384-350a-8ea0-a4a65eda1b23 | -8.95698 | -45.16497 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b4214064-7a14-36ec-bd39-83fae6f54216 | -7.26199 | -43.50795 | 2026-10-08 15:41:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| d1b0ce0f-ee44-3ff6-9215-736e35a3ae8a | -7.46098 | -42.83338 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 27.5 |
| 950778c2-795c-341c-b844-dc203ec601fb | -4.96627 | -42.68774 | 2026-10-08 15:41:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 835178a5-2b20-3354-b10b-a8d9bcde22bc | -5.73439 | -41.76954 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f1777a61-3265-3aa5-80f1-d93cb84302fa | -8.94969 | -45.15986 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| a16d9292-2d59-3716-aa66-f73e7ab85101 | -11.27401 | -45.1944 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4e912d5d-1362-3367-97f7-7766473009cd | -7.76117 | -44.16963 | 2026-10-08 15:41:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a5d83573-66c9-3522-aac7-b005fba82fcb | -6.53606 | -45.38239 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 2f82bbe8-440d-3759-b5c8-83c4162c7714 | -7.0542 | -44.32169 | 2026-10-08 15:41:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 2da134dc-b1ea-3272-ae27-175abc28f6a1 | -7.17222 | -44.82778 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 76822d65-af45-380e-8fd4-af604c827e50 | -6.16937 | -44.85975 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| c1543147-aa38-3a8c-a69e-032a556a1ae0 | -6.164 | -42.58603 | 2026-10-08 15:41:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| b00e358d-1cbd-3216-b58c-5d4b39b9e19d | -8.93066 | -45.16817 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 6677b855-fd51-3c6b-8b50-3929556dd2be | -5.77442 | -45.39008 | 2026-10-08 15:41:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 96130751-0823-3b8c-ae1d-a37bda3d7552 | -8.63619 | -41.04641 | 2026-10-08 15:41:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 56fb6cb1-73b4-3977-af19-7f130c5c29d4 | -7.53596 | -42.09233 | 2026-10-08 15:41:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| 419cf28a-e8d5-35e0-ac09-df1c2cad8b7a | -7.84003 | -40.48424 | 2026-10-08 15:41:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4d3d19ff-7de7-3629-b8bb-82132326135f | -6.40864 | -37.79419 | 2026-10-08 15:41:00 | NOAA-21 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 19.5 |
| f0f6a252-65b7-3ef4-bf9b-eeb3a378d487 | -11.00359 | -45.41516 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2c72405a-0709-3b6d-8aca-ee0f695f7799 | -9.2273 | -45.65968 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 07da2092-5a99-3494-af62-92b6ab7a7f7e | -6.15299 | -39.43317 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 17c4fe4d-c25f-39bb-a327-1551fad27576 | -6.92579 | -38.55415 | 2026-10-08 15:41:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 9.4 |
| ee3fe33d-42de-3347-b066-bbf4be4006e1 | -5.45409 | -42.9065 | 2026-10-08 15:41:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 88cee3d4-9602-3aec-be34-1d76a8843d67 | -6.85142 | -39.46551 | 2026-10-08 15:41:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 123.8 |
| 1fcd1c17-e849-3433-b1cd-72ae23fefbcc | -7.87728 | -44.14914 | 2026-10-08 15:41:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b9614136-01d9-3790-8159-227d68313ee3 | -6.59948 | -37.89344 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 4a21b580-af9e-307d-bfaf-716698180f81 | -8.94901 | -45.15423 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 77d1724f-13a4-3729-bede-3452a90e04c1 | -11.11102 | -45.68909 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| df5bfe4a-23c6-37f0-bd66-2a5d7dceee7d | -9.94078 | -43.5587 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 27996e69-22c5-337c-a22b-d281e09b608f | -6.54107 | -45.37098 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| e08bad1c-e624-349f-8487-bf628c99fe36 | -9.51542 | -45.61326 | 2026-10-08 15:41:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 28c5e629-6c77-3937-8745-fe4d74c23e48 | -5.71949 | -41.73229 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 3a6383d6-e2c4-3ff6-9c16-3fccf271ddb5 | -9.81977 | -45.6852 | 2026-10-08 15:41:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 08a65075-330a-3702-bb95-baaea21d7fdf | -6.39356 | -44.94869 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| bb20f84e-ea57-30ec-881a-a151a305702c | -6.23708 | -43.85697 | 2026-10-08 15:41:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 13b15110-4669-3143-b0e8-7d213617c2d7 | -6.85109 | -41.74738 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 183.2 |
| 9d900cc0-3674-382e-9797-1bca33fc168c | -5.77665 | -42.05522 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| df9cddf9-6ac5-3e76-90c7-10e256c3c126 | -6.38965 | -44.94819 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0ff455dd-e22f-3804-bf5e-7f6817de7d14 | -7.13723 | -41.80859 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 963ea0e9-08e3-3fdf-8665-a3b1e7066741 | -8.07138 | -45.61978 | 2026-10-08 15:41:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| e16b422b-681a-35b3-a0b7-2f0b78b32b5b | -5.45568 | -42.90488 | 2026-10-08 15:41:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 3070853d-9eed-345f-8bf2-b4cafe44d84e | -5.74836 | -42.07782 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 750c3c1a-c2b8-3c25-8b8d-de66b0ddd68f | -6.85233 | -41.75642 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 25.4 |
| 541f2e39-5459-36e7-a7a3-9bc55629c243 | -7.77644 | -43.81353 | 2026-10-08 15:41:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| a91880b3-62bd-3799-af19-e9f93e062f5d | -6.91271 | -45.47232 | 2026-10-08 15:41:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6098727d-d4a6-3966-8aec-21ad7f6dbfae | -9.89989 | -45.19436 | 2026-10-08 15:41:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| b732ac08-f0f6-3560-9601-a4b41985cc21 | -6.8515 | -41.75039 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 131.1 |
| 7687b23d-fea3-3144-8855-d7e1fb23f85e | -7.47467 | -42.85063 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 46.9 |
| 3826eb77-6c61-335b-a7bf-9aeccbd3b344 | -6.21914 | -44.85262 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 2df54bb2-9e44-3e16-a662-f3795ccc451f | -10.35876 | -42.48562 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 0777e91b-de77-3e7a-b348-99432792da65 | -7.14872 | -45.01194 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4a972e4-4e35-328e-a1cd-f2c182b9f5cb | -7.24858 | -43.75897 | 2026-10-08 15:41:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 021136c9-68cc-32ed-960b-ca3d635ec9e3 | -7.27546 | -44.18987 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 361826f1-568b-3510-8983-67f8576531c2 | -6.35855 | -42.56225 | 2026-10-08 15:41:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 1c604c07-6b9d-3cb2-b49f-1fdab78cec7b | -6.85359 | -41.7656 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 21ec4a33-1ba4-395f-8f88-6a6f7ac6880f | -10.34574 | -46.23792 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| ce30cc9b-5395-30e6-8ba1-a51d3cc2a501 | -5.7625 | -42.06641 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| a9144db4-0d04-38e6-a4e9-48edc5bf2093 | -8.20762 | -46.40323 | 2026-10-08 15:41:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 386.6 |
| 043f5376-b9c0-3562-afe8-9906ac63ff01 | -7.69981 | -44.75489 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9e39f49a-a115-34bc-8e01-5371ead975e3 | -5.88269 | -45.94704 | 2026-10-08 15:41:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 334a9bd7-bc5e-386f-b7f4-209636d74ea5 | -10.58306 | -41.20355 | 2026-10-08 15:41:00 | NOAA-21 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 9a556fb6-edb0-3163-bf8d-2ca85ecb7fb0 | -9.36527 | -45.93711 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 37c2e9e4-f6f3-3978-9447-68f3c8b28e5e | -7.87018 | -44.15054 | 2026-10-08 15:41:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 9d14b037-4394-3599-b36e-45a82870af6a | -9.78385 | -46.26823 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 92839740-3a57-3186-a3a6-e0edce6d0df1 | -5.77417 | -42.05957 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 27529019-b362-3598-a09b-3949ff86a868 | -6.89026 | -45.9011 | 2026-10-08 15:41:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6a071dbf-3f60-363a-884c-77012977f55c | -9.53735 | -45.62323 | 2026-10-08 15:41:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 7300fcaa-8f21-3e6c-b082-6f0f3b375c13 | -7.18816 | -44.28868 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ea41848f-8a9c-3eeb-9d03-ac23fd9079ba | -7.30791 | -44.53344 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7407399c-e88d-34b0-9303-5e99fcaec12a | -8.19976 | -46.39721 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 6980818d-0a1d-33f8-9740-dcd30a841a35 | -8.93448 | -45.18833 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 189.5 |
| b4b0c348-61a4-3dee-bdb0-c823eda32a9d | -5.73054 | -41.77903 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| fea53153-4b8e-3b44-a479-a6db9d7921b1 | -5.97799 | -41.35896 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| d1d1a92c-414f-3953-9152-58816d69a1a2 | -9.43552 | -44.60268 | 2026-10-08 15:41:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8a17dc04-e7fc-3671-88b8-9188f72844b2 | -6.3215 | -43.34878 | 2026-10-08 15:41:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ab2f12a2-5b40-3cad-b8b3-57181a7936ff | -8.07011 | -39.56904 | 2026-10-08 15:41:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 64e46b66-bcaf-3c35-8d0c-89fd91175eb0 | -5.53247 | -44.28694 | 2026-10-08 15:41:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 6ab9d5ac-afdd-3ad9-a396-2e5dc9aad02c | -5.77709 | -42.0583 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |


[Clique aqui para ver as próximas entradas](README238.md)
