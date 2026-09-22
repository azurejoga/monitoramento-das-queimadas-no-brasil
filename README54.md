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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75d1552b-7b42-3fc7-9639-ede799988401 | -9.2374 | -57.14824 | 2026-09-22 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45d2922f-6de7-3876-a9a1-ddbdf858baa7 | -6.5763 | -44.1623 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c1c8060d-8df5-3268-94c8-ca6f19d14732 | -3.24 | -53.9531 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b6fb7672-41b8-3910-b196-e042363bc2c3 | -8.93685 | -50.55368 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f597cfa-ec93-3ca6-a792-2b9a4aca7d49 | -6.63961 | -59.92477 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| cfb03943-954c-39d4-b523-e45b71b2dd05 | -3.72115 | -54.11136 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0592e3fd-b0b9-35c2-b518-1266ec788e52 | -3.13041 | -51.6069 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2ce6799d-e9e6-3576-8c1d-82567d34189f | -6.46112 | -49.87801 | 2026-09-22 04:46:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2518f15e-e47e-3179-a8fd-53fc7d5638d2 | -3.00549 | -54.17374 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6fcad3a-d827-3357-890c-c2ab4f02a9be | -4.35191 | -55.65202 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e39409d4-49c9-3791-8321-b5060193344a | -9.58002 | -55.11928 | 2026-09-22 04:46:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc94abf5-b194-3952-a08c-04df9613ee46 | -7.41302 | -44.73938 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27ebc50a-2122-3666-a4c5-47acf4526ea6 | -8.79394 | -48.72931 | 2026-09-22 04:46:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b537a8bb-2a03-3598-a521-388ac19b855f | -3.03381 | -51.33298 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f832c7ea-4de0-3488-8ad1-4047562c7372 | -8.3226 | -50.83588 | 2026-09-22 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73ae5ba9-9ec5-391f-8031-6b5f3397aece | -5.83651 | -51.7074 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01376d51-d2eb-3d68-b569-85cb79012405 | -5.89242 | -52.28317 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 234019ef-f5e6-3e48-b70f-9a0afecbff4b | -5.88365 | -51.5798 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a91ae040-27ec-3a31-8f0f-f42b48c97905 | -6.07412 | -57.72883 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20d99e1d-86da-3c8c-9d5b-7077bb5ed115 | -10.49294 | -51.29038 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 89e5cfec-8a54-3bbf-bb2a-0dad54f09ed8 | -7.56976 | -57.68145 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ecba628-429b-3251-860e-556bfdecb5cd | -11.41353 | -45.37392 | 2026-09-22 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f6330bf-8e5d-31b8-901f-a8a83472b067 | -9.73236 | -54.80621 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b5ffabc-154a-32dc-959a-305e39219034 | -4.34791 | -55.65143 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f61c091-2dc7-3d9a-b829-37ddfe359a72 | -9.8984 | -48.4139 | 2026-09-22 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0aba83e3-99c5-31b1-9c67-5572b940c7ab | -5.78276 | -43.77062 | 2026-09-22 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 423d5662-bf28-350e-9d70-fbe0d69f6899 | -9.27818 | -46.21094 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27b05e34-e7e3-30fc-8a45-61fb185c2d0f | -3.3972 | -59.52985 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5af056ac-f5d6-3370-9e50-b1446082e4b2 | -5.80882 | -52.0785 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 192e1916-2699-36d1-b711-ba28f2322bd6 | -4.01796 | -51.06575 | 2026-09-22 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 646b23e8-af7d-3738-bbff-f18fa08b1320 | -4.30052 | -55.07478 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c581027-0042-3c53-94e9-5880e4e82b4b | -8.92028 | -50.92897 | 2026-09-22 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d2d0f3d4-8271-373d-8c77-acc9a27253e3 | -5.75344 | -45.08499 | 2026-09-22 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 5320b3c9-e5f9-3664-9c29-18820af82e48 | -9.62395 | -43.93468 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 01498031-ddc2-30a4-9dc6-b0ee9f68d1aa | -2.8871 | -54.07667 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bb26f29-142c-38ad-bc11-2f6e82bf3e86 | -8.25517 | -55.25344 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73f49cca-08f4-3109-bca0-cde09077864c | -8.618 | -54.62679 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5966e1a8-7003-3ac5-9592-257436e5bcfd | -2.91952 | -57.78643 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ee61f94-e153-33cd-9646-ace96f87a939 | -6.14307 | -43.84608 | 2026-09-22 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8bde905f-e031-3cdd-aadc-3f330e950a02 | -6.64293 | -50.06576 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a7a9eaf-994a-3585-be59-bcb61ab6ac79 | -5.8718 | -51.93761 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4edbdadb-c492-32b6-9770-95b08fc80eb4 | -3.44634 | -50.61302 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc1fe151-65bf-3068-a5c8-e494f557b436 | -8.74104 | -52.36329 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f69b208f-7162-34f8-a71a-d890c57d17ce | -8.83721 | -49.23948 | 2026-09-22 04:46:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2adc6ae7-57e4-3311-9f09-0235fd136462 | -3.20176 | -57.83925 | 2026-09-22 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bd5871a-0e4c-35b7-a559-19e443498788 | -9.97322 | -50.2614 | 2026-09-22 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89fec409-218e-362c-be24-179e84f2b3c5 | -5.55064 | -45.20134 | 2026-09-22 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29a9c3c9-9cba-3157-8a5f-753741133b9f | -6.11799 | -57.75821 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b52cb3f2-2694-3ea1-ac3f-06d2a640ca3b | -7.56098 | -42.65514 | 2026-09-22 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 17cbf845-c2d2-39d6-818d-60628c000242 | -8.14974 | -54.80307 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb0dbf52-778a-3f16-a2d3-b3ff67057782 | -10.03768 | -52.09985 | 2026-09-22 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83d4acf8-678a-3526-966f-4a96a84c4556 | -6.90553 | -41.69675 | 2026-09-22 04:46:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 63e2b4e1-6e30-3c98-a076-13192a51bb29 | -8.79202 | -44.28429 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b94f6a90-23ca-3cdc-9d7a-a2adf5e0cb7a | -8.24125 | -55.2753 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 566691b4-fb05-38b7-8573-acb9218e8b37 | -7.18536 | -47.4479 | 2026-09-22 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43ea325e-b215-3c64-890a-12adec5da798 | -6.66926 | -50.88704 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d74ed9a-8fb3-3117-93c5-77bb95ef2516 | -2.41297 | -58.27967 | 2026-09-22 04:46:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 714e73f0-f613-3589-89eb-d1d618022b6b | -4.20719 | -59.9127 | 2026-09-22 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8a8d4aa-103a-3472-bae2-a72775408ac0 | -9.24275 | -46.1583 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 31e7a7cc-2f0c-3ac3-8127-4160faf790f0 | -11.67353 | -43.46237 | 2026-09-22 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d20f7da8-93d0-312e-b9b1-d77b567de5d9 | -10.0516 | -44.88605 | 2026-09-22 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d932d6fb-eca7-39ee-a4a2-a82d09895f40 | -8.37359 | -47.2933 | 2026-09-22 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 45e3611b-c7c9-38d1-9340-ad57bb1485e3 | -5.87828 | -53.63852 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9ae8073-2f1f-3488-8c15-cabc7745fca9 | -9.62178 | -43.95157 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 795bd20c-f2de-3451-95ce-c02cc79b9b61 | -7.61537 | -55.35454 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd23d843-1061-30b5-b648-aa0fc23acb6c | -10.75828 | -50.72899 | 2026-09-22 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bd50f02-a694-3467-ab31-62bb137e22de | -3.39153 | -50.43945 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f604acd-d54b-3d94-b983-de0a0561202d | -9.53637 | -45.38828 | 2026-09-22 04:46:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a334125b-a83e-31b2-b6d0-8d8c0b7d638f | -5.81862 | -57.74017 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8961c110-7c3c-3777-979d-92b407fad1aa | -8.61022 | -54.6297 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd4312ea-961c-3373-a592-2f7f6204be70 | -5.83975 | -53.47766 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3786e913-dc94-35b9-ac01-8666934e6353 | -6.75683 | -56.32896 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 847a7d1d-6681-3afc-af94-71f75608ae86 | -9.28454 | -46.19623 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3a2a4639-5df2-3df8-ba72-0e140f193bec | -9.30573 | -58.91446 | 2026-09-22 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aaf52210-b87e-3867-b379-a1ca18df8ebb | -7.292 | -59.52214 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e292a32f-58e5-328c-bb58-566b972931cf | -8.48579 | -44.73886 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23064c1d-82e4-3731-9047-eee870759c63 | -5.5303 | -45.67032 | 2026-09-22 04:46:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3f1be97-81c4-34a7-b0e7-d1a57bdaa3e7 | -3.95752 | -49.04786 | 2026-09-22 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d289110c-b498-3b39-ba89-f83bed6f398d | -10.67628 | -50.73541 | 2026-09-22 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56b59282-fbf8-3926-91a6-37f2bb5f7684 | -7.13137 | -42.06855 | 2026-09-22 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e03e773d-abca-393a-995a-4ec82e25db8f | -6.71083 | -59.45784 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b36e638c-f558-3065-a314-7c66eeede2eb | -6.83241 | -49.09768 | 2026-09-22 04:46:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f291ec95-727a-3d67-a0e5-68c2ffc2fe45 | -3.73991 | -55.97803 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9e423a0-b841-3d97-9dd6-8acf0bd5c40b | -7.57338 | -57.68636 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d103049-bca7-3527-823f-f3a46cc1b660 | -3.0108 | -54.18807 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9dc98050-6176-3295-aa5f-92667c84594f | -3.75552 | -59.42155 | 2026-09-22 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05b04181-1abf-3489-ac10-3206a73b655e | -9.66741 | -54.33667 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| efa2edba-6be6-3d56-a303-560b530e9f3b | -5.20742 | -46.21003 | 2026-09-22 04:46:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2cc6431f-67bd-300c-bbdb-f049ff1ed029 | -10.45306 | -51.28405 | 2026-09-22 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d0066709-d981-3ef5-87cb-623fe2a32046 | -10.45707 | -51.32448 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ed23419-c25a-39bb-a847-916728a55ddb | -6.52986 | -55.36063 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 487326c4-1fd3-3b2b-b9bc-082052ca190f | -2.56886 | -57.50479 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 985a7970-59b7-34d0-95af-4c4b89aa748d | -11.10497 | -48.30703 | 2026-09-22 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e89adaa3-4dca-37b7-9ff2-703dbada5bac | -6.62882 | -59.92605 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9d434e60-9b72-3d3a-aca7-a2e08dcc7634 | -3.05299 | -54.40963 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82a5e472-99bb-3c4b-9e16-01ab7ced6b7d | -4.64829 | -50.99588 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b06b6d85-0572-322f-8372-70737ab1a5a0 | -3.58606 | -59.06712 | 2026-09-22 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1feb1b5-d966-3b1a-a225-377d745e503a | -6.69612 | -55.36636 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c68bdf71-fd31-35b2-8925-b88ee0332f82 | -2.86986 | -57.794 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 025d5544-a6a8-3cd6-bc51-36650c1c789f | -5.98646 | -57.70504 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README55.md)
