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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d97a450-a3ca-3b9d-bd20-461f45e5888e | -3.2306 | -47.1131 | 2025-09-03 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 273a8189-f89f-3399-915c-54c1d4e7fe6d | -6.4646 | -49.5364 | 2025-09-03 00:00:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 50f8446c-413b-3294-854b-93f61af4f9c0 | -5.6268 | -45.0025 | 2025-09-03 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 138.8 |
| ddf288c6-24b8-394c-82ee-79e51604f5f8 | -6.8095 | -52.8154 | 2025-09-03 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| c89d6bc9-5ce2-3715-9938-4bdc2e3f887f | -5.6081 | -45.0038 | 2025-09-03 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 3f3a2923-16d0-31f8-a70b-c8433a3f874d | -10.0932 | -54.7667 | 2025-09-03 00:00:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| d5d5940f-cb8f-3314-aef5-ca9096087069 | -10.1284 | -47.4288 | 2025-09-03 00:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 39732982-8696-3316-8cdc-d1cfe948bff5 | -6.4403 | -58.1186 | 2025-09-03 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 99c09ecc-4e3d-3f60-825d-f571da7f288b | -12.9573 | -56.9839 | 2025-09-03 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 6d6ca402-2e40-30e8-ae79-1d72753a0fab | -3.3788 | -47.1514 | 2025-09-03 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 337f7fe3-5066-3b69-84c8-b49342aa3e0a | -12.6341 | -56.9926 | 2025-09-03 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 500cae6f-153b-34d0-a48e-fe990f7ccae6 | -12.6531 | -56.9909 | 2025-09-03 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| a1ed4a73-d44d-38dc-bfdb-af585f1e4b89 | -6.3293 | -58.1814 | 2025-09-03 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 79e99ff0-ac26-30cf-bcc7-da0b42c7c453 | -18.1514 | -51.75 | 2025-09-03 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| edb2c703-6763-3140-84ea-e02c849bbbfc | -5.6935 | -45.9443 | 2025-09-03 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 62f1fd37-d2d1-3671-9861-c5f938ab8235 | -6.4648 | -49.5151 | 2025-09-03 00:00:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 478b786c-7edd-3fdc-872e-ea53ca9aa1bb | -8.3832 | -48.3099 | 2025-09-03 00:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 1e83089b-3bc7-354d-ad9f-1fbb6e66f322 | -3.212 | -47.1357 | 2025-09-03 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 129.1 |
| cc934cb1-fc5c-3d12-9336-8f12da40b12a | -20.8886 | -50.0937 | 2025-09-03 00:00:00 | GOES-19 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.9 |
| 17792a80-37f8-3c09-8f7e-8cbb85879f2b | -12.9382 | -56.9856 | 2025-09-03 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 105.1 |
| ac14630e-7181-3dde-a3be-789e73b4e33b | -6.4402 | -58.138 | 2025-09-03 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 94cb5710-1edf-37be-81b9-c03f8c6edda0 | -12.6151 | -56.9943 | 2025-09-03 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 2f0d7f48-798a-330b-ac91-afa924ccb553 | -11.6647 | -57.3533 | 2025-09-03 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 38ec853c-3441-3816-82a7-c215d1431dab | -12.9189 | -57.0074 | 2025-09-03 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| e0aa27fb-a215-330f-916b-b7dfda79f431 | -3.2121 | -47.1138 | 2025-09-03 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| eac770f7-52cd-3ebd-953e-954c4a3f5703 | -15.5656 | -48.3918 | 2025-09-03 00:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 60.2 |
| c5235600-4302-33a7-96d5-f0d09d8be731 | -8.3644 | -48.3116 | 2025-09-03 00:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 4e363ef6-212a-323a-bc66-b4e7efeb3dcf | -9.176 | -45.1993 | 2025-09-03 00:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 594ac331-ab0f-356c-8cfc-770efb0987d6 | -8.3834 | -48.2882 | 2025-09-03 00:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| fbe53df6-e2af-3a2c-b1a3-de889b0f8e4f | -12.6339 | -57.0127 | 2025-09-03 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| f8222202-39a8-3d30-b0c6-be597e5d2e06 | -12.9387 | -56.9454 | 2025-09-03 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 8ffdf6e7-f5cf-3b0c-816b-6597bb1ffbdb | -6.6982 | -48.4035 | 2025-09-03 00:00:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 0dc2afb3-61f8-3a19-8f7c-53bb667fb385 | -8.3646 | -48.2899 | 2025-09-03 00:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| d1ce4f82-2c6d-37b4-b8de-5078ca78af7f | -10.0745 | -54.7682 | 2025-09-03 00:00:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 5fb6d541-aec4-3b61-8ac5-083895669983 | -7.3357 | -59.6484 | 2025-09-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 11b7a377-a684-3aea-a112-1245f4e5f29d | -9.1949 | -45.1972 | 2025-09-03 00:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 164.2 |
| a12f941d-c53b-3413-9ca9-7c4898fa51ed | -9.3394 | -55.2277 | 2025-09-03 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| e8d56720-0e0d-37bc-8cf4-fe7592cbd592 | -6.8881 | -71.5008 | 2025-09-03 00:00:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 4613da01-1deb-3de9-97b8-abb8f06ab7ea | -7.9341 | -46.5453 | 2025-09-03 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 6e387949-aeaa-3939-b28b-98ebee6ccd83 | -10.5409 | -50.4256 | 2025-09-03 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 73894fbd-5454-3e27-9bd6-fb7d49204ddc | -12.9385 | -56.9655 | 2025-09-03 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 03460a2f-9393-3c1d-9c92-76d9b912c820 | -15.5652 | -48.4143 | 2025-09-03 00:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| a8b1e6a6-b905-3c45-acc2-1c1bcbce4329 | -5.6266 | -45.0252 | 2025-09-03 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 154.9 |
| db00f892-87e2-3c44-8d0d-2ef29f8020f2 | -3.2305 | -47.135 | 2025-09-03 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 197.4 |
| e768c1e4-8215-3cda-9a1c-1d2193613d7e | -4.1604 | -46.7881 | 2025-09-03 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 267c9a20-e52b-353c-a1a6-59dcc80d8973 | -5.6079 | -45.0265 | 2025-09-03 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 51e39fa7-6e20-3c65-93f7-13d86b31c42b | -10.1281 | -47.451 | 2025-09-03 00:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 31c0591d-96e1-3ca7-bff1-8c233f86c182 | -5.6266 | -45.0252 | 2025-09-03 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| daab3fee-0894-3d85-8f9a-de881806e796 | -4.1604 | -46.7881 | 2025-09-03 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 868f92e4-2e65-385e-bf5a-628cc3fceba8 | -7.3357 | -59.6484 | 2025-09-03 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| e3b4cd27-77d0-3a73-a33b-3a343b2ef2bf | -7.9341 | -46.5453 | 2025-09-03 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| fc23378c-d6e0-3690-aaf0-1df807171e08 | -5.6268 | -45.0025 | 2025-09-03 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| d177211c-9ea4-3a76-979e-c656df9668ac | -9.1949 | -45.1972 | 2025-09-03 00:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 8165b7d9-8605-3aed-ac25-254dcd1ed654 | -12.6531 | -56.9909 | 2025-09-03 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 47f1952a-2103-3565-a341-f0425213e807 | -10.1284 | -47.4288 | 2025-09-03 00:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| e580802e-694c-30a3-9c3d-ca0cdbe88d6a | -3.212 | -47.1357 | 2025-09-03 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| c908ffd9-bf41-3480-9882-da39338ea1a5 | -5.6081 | -45.0038 | 2025-09-03 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 186.9 |
| c2373837-a072-366f-a0db-7e7520e96db6 | -21.4534 | -49.6513 | 2025-09-03 00:10:00 | GOES-19 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.8 |
| 25ef5cd2-b2a3-3821-ac76-59a5357c5799 | -6.3293 | -58.1814 | 2025-09-03 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 9292960d-21c1-3051-9ecf-47b2b4d9eb27 | -3.2305 | -47.135 | 2025-09-03 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 249.4 |
| 23163622-444f-33f7-8bc0-3cca5faac5fa | -12.6339 | -57.0127 | 2025-09-03 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 70cbde5e-3f2f-3aae-9b1c-668b7904d5ea | -7.7036 | -48.7587 | 2025-09-03 00:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 66151c3c-502f-3db1-ab9b-507d56cfe984 | -12.4889 | -47.4837 | 2025-09-03 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| e47f8296-f874-3744-9403-ad75d16a391f | -17.9204 | -47.1992 | 2025-09-03 00:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 2fec2f54-90a7-3de5-a69f-2ed874f48824 | -6.4402 | -58.138 | 2025-09-03 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| fc07337d-4d23-3e06-b56d-fc431b7b2839 | -17.941 | -47.1718 | 2025-09-03 00:10:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 3f88ffd7-a68d-305b-8b87-f60d347cd568 | -12.6341 | -56.9926 | 2025-09-03 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| dca8b3f0-6dd3-3696-9311-1d857e937eb4 | -6.3478 | -58.1807 | 2025-09-03 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| ccccbb60-cf41-3ac3-a173-1942308973f6 | -17.9404 | -47.195 | 2025-09-03 00:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 3982bc42-c58b-3bad-a5bb-2cf0142cf01f | -10.0932 | -54.7667 | 2025-09-03 00:10:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| d7890f31-d040-3b78-9f44-52e8610db770 | -5.6935 | -45.9443 | 2025-09-03 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 4460c1b7-9f1e-3b40-9b21-1c56befdc0c6 | -9.176 | -45.1993 | 2025-09-03 00:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| f70b3d6b-da27-3bda-bd52-5006591f0f3c | -6.7909 | -52.8165 | 2025-09-03 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 848e5a70-0fc3-3fa4-a459-547974e97d3e | -8.3832 | -48.3099 | 2025-09-03 00:10:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 69c0cd06-2f90-3546-b8aa-875193de8ebc | -10.1281 | -47.451 | 2025-09-03 00:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 8a7ae363-74d2-3990-947d-c96abc787113 | -17.921 | -47.1759 | 2025-09-03 00:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 118.3 |
| a3fca096-bb72-36f7-a6bd-9a2921edd309 | -6.4403 | -58.1186 | 2025-09-03 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| d0528e1b-f8c3-3041-a36d-77df77aed230 | -3.2306 | -47.1131 | 2025-09-03 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 155.6 |
| 65a48323-0e99-379d-a92a-d4b6c9ceef82 | -6.4648 | -49.5151 | 2025-09-03 00:10:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 45b2e59f-0d95-3e1c-9deb-e8ff6a5de4d0 | -9.3394 | -55.2277 | 2025-09-03 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 0b286b2e-2356-37b3-84b5-09546ba2c4c6 | -3.3788 | -47.1514 | 2025-09-03 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 1e30f4b2-be1b-34a7-b474-c776b99a5c91 | -6.4646 | -49.5364 | 2025-09-03 00:10:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 5e4e96fc-3664-3951-a326-5b340817feb0 | -6.8881 | -71.5008 | 2025-09-03 00:10:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| d89ac60c-aaaf-33a7-b058-a55ffd2503b7 | -8.3834 | -48.2882 | 2025-09-03 00:10:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| b62c4c4b-8c57-34bc-b690-3673bebd1ad4 | -5.6079 | -45.0265 | 2025-09-03 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 192.5 |
| ab36264a-3887-31ed-8e47-4eec0dc14021 | -10.5409 | -50.4256 | 2025-09-03 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| e30d0f56-0fab-3a2f-9f6a-0c267be95a4d | -8.3644 | -48.3116 | 2025-09-03 00:10:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 77243b92-d458-3c91-a34b-cc0afa6d3d70 | -11.1146 | -45.115 | 2025-09-03 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| b5ea61c6-d32c-35c0-89fb-7daa3853327f | -10.45 | -54.7785 | 2025-09-03 00:10:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| b4900fd5-f376-39ab-a650-51f978eaffe5 | -20.8886 | -50.0937 | 2025-09-03 00:10:00 | GOES-19 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.3 |
| b79ca85e-0664-3f16-b53d-232b79c8ae2c | -8.3832 | -48.3099 | 2025-09-03 00:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 2275d0aa-868d-31b4-a0a1-0b073cf4a745 | -6.446 | -49.5376 | 2025-09-03 00:20:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 708f45d2-cf6a-390f-8050-657691bfd345 | -6.8095 | -52.8154 | 2025-09-03 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 52e640af-a9f5-31c6-9d4f-4c7f2d348577 | -4.1604 | -46.7881 | 2025-09-03 00:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 506e921c-0b1a-3fb9-8369-3d06179176ba | -3.3788 | -47.1514 | 2025-09-03 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 9f48b5c9-b14d-300c-997b-669fbce0bf37 | -8.3644 | -48.3116 | 2025-09-03 00:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 23c4c0fc-5f7d-3088-883d-fc337802f238 | -6.3293 | -58.1814 | 2025-09-03 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 0ba7b366-c8fe-3873-a406-b714906f3adf | -7.7224 | -48.7572 | 2025-09-03 00:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 2723273d-6349-38c1-8dfd-976676e92de1 | -5.6079 | -45.0265 | 2025-09-03 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 162.1 |
| d569495b-dca2-349d-9116-d26c9e23d995 | -5.6935 | -45.9443 | 2025-09-03 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |


[Clique aqui para ver as próximas entradas](README2.md)
