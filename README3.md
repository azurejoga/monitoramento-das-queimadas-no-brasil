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
| 4096c3a3-6053-35c0-bea8-5fab3aa9c0fa | -19.02694 | -57.54192 | 2025-10-13 00:50:00 | TERRA_M-M | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 19f4d7a6-3323-3304-9f0a-42ee6111b741 | -17.78098 | -54.9425 | 2025-10-13 00:50:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4baeb7b9-be75-3489-8fbd-a5cfa67227b5 | -17.32491 | -53.82419 | 2025-10-13 00:50:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 09e094ff-8981-307f-bd08-f2096d161ea7 | -17.32362 | -53.81426 | 2025-10-13 00:50:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 40.7 |
| bc5c59c0-f921-31c7-ad3d-0c7adf054df8 | -16.35559 | -49.38561 | 2025-10-13 00:50:00 | TERRA_M-M | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 26405711-4788-312d-ab46-ff5eea4afd78 | -17.34059 | -53.8016 | 2025-10-13 00:50:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 3c3d8fe6-d2f1-32c2-a0d7-d2d8e8e4d291 | -16.13103 | -53.97534 | 2025-10-13 00:52:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e06c034f-f761-3b9b-842b-dc567b89485a | -14.20848 | -51.5182 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 615d77c8-01b6-3da1-be61-1ddb4557ef71 | -14.28383 | -51.52956 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 597ec74e-7087-319a-8e68-e36a0a951a8c | -11.87324 | -54.67738 | 2025-10-13 00:52:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c0dfa4e4-54ec-3cb2-bf39-dc20e426b26e | -14.26448 | -51.5229 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b31475af-c262-3198-9ca3-4926e8a40177 | -14.29688 | -51.55647 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 864e879c-46a8-36a0-a2ef-689d2bd00f84 | -13.80747 | -52.78902 | 2025-10-13 00:52:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 109d084f-6912-388e-8a17-a6a28b1e3a2b | -14.26311 | -51.51345 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| b22123fc-8bd3-36cc-aee4-f2850ad0cb5b | -14.29418 | -51.5376 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| deacd3bd-aeef-3120-b8db-e80d20bf7e0f | -7.54819 | -46.11839 | 2025-10-13 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 8cdd6cd1-4392-3ab5-a5b8-26006e69a3fa | -14.30587 | -51.55507 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.2 |
| ec2f8735-47fc-34b1-8f88-6afb512d3ad4 | -11.74105 | -54.7216 | 2025-10-13 00:52:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 2d8f9793-c30e-3818-a27b-dd3adbfe8ec9 | -14.27075 | -51.50259 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 76a12d2a-2871-3c14-942d-5933ee10b0be | -14.30722 | -51.5645 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 4c97387b-1161-3333-8e32-6de8d0431174 | -12.04552 | -55.34883 | 2025-10-13 00:52:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a70fa98b-3698-3cc0-b42b-d0a27891db99 | -14.27484 | -51.53095 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 147680cb-cef7-3d4c-b47c-8c1a77780a73 | -14.26175 | -51.50399 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| d828e1af-090e-34a5-b374-0ffafe886efb | -11.75008 | -54.72032 | 2025-10-13 00:52:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2da24670-a5fc-335e-8c54-a373898c33c7 | -12.79478 | -56.96352 | 2025-10-13 00:52:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a5711008-657f-35a4-b6bb-1e8bdb93b02a | -9.67394 | -62.52113 | 2025-10-13 00:52:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 990a2f1d-13b2-344f-9221-8bfd6b73aa7c | -16.1209 | -53.96325 | 2025-10-13 00:52:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 458ea263-28ba-3a6b-a8f2-dbe57dfc5026 | -13.51403 | -51.30698 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 2b802df2-b2f6-3bb3-b0a6-39f432c9d0df | -13.49579 | -51.30983 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 963e8d71-c683-3e99-b75e-800cdd8cecea | -13.50491 | -51.30841 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 9e564645-c63c-33a4-b06a-c81dcf97c939 | -13.51263 | -51.29728 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fc8bd77c-29ad-314c-adda-f31c3d275124 | -11.7423 | -54.73104 | 2025-10-13 00:52:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 96a1a6e7-a0af-3847-a1d8-002d40fa76f4 | -14.25138 | -51.49593 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 5e8e9bfd-f4dd-398b-b3e6-be18395f627a | -11.73979 | -54.71218 | 2025-10-13 00:52:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b2cf350a-5326-310c-85fa-8142d13783ab | -8.32329 | -46.25772 | 2025-10-13 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 1e799ada-47f7-3376-a46f-ecd3d65cb27c | -14.20983 | -51.52766 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 116b040b-9c1d-3f29-a52e-630a0f851631 | -16.1222 | -53.973 | 2025-10-13 00:52:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| b431c03a-f73e-3838-840d-1a5d4d102097 | -14.29553 | -51.54704 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6a34aef7-40d3-3766-bbe7-3fd5d05dcb99 | -8.87913 | -45.27546 | 2025-10-13 00:52:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 435.1 |
| 0bde91f0-e426-3afe-ab79-f0d02dcddd35 | -13.5035 | -51.2987 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 32.4 |
| b55c2324-1688-3954-9c9b-653efbdcd48a | -7.54388 | -46.09138 | 2025-10-13 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| b05b148f-f094-3042-a355-695e870ed34b | -14.27212 | -51.51205 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 3fd98262-42be-3c1f-b899-a8d42d29ee99 | -15.33438 | -50.94815 | 2025-10-13 00:52:00 | TERRA_M-M | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8ccd12c4-00d5-3a58-bdad-3b5fc2ea2570 | -14.21883 | -51.52626 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| fe29dad9-c060-3c83-a590-39d7a47200a6 | -14.25001 | -51.48646 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4b626b7a-1967-39b4-a1b0-cb845346a9bd | -13.49438 | -51.30013 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5b1317a4-c1fd-39d5-becf-0b922402212a | -14.27348 | -51.52151 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 93f9160e-d856-3716-829e-c8ac689a1fa1 | -14.20712 | -51.50873 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 07db7f35-202b-3015-b941-cc3ebdf6acf5 | -14.19812 | -51.51014 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0f317c0b-98cf-369e-b582-a6743d3b0e11 | -14.28654 | -51.54844 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 7aa43c6f-57f0-33a2-ba9b-1b5e28bc7b3a | -14.27891 | -51.55927 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ac7182dc-8f16-3cd8-a8aa-b7cc68b16d81 | -14.28519 | -51.539 | 2025-10-13 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 6d820943-108d-3ca0-a950-708cf52ab747 | -16.1235 | -53.98276 | 2025-10-13 00:52:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 013b7683-a1e4-3ce3-add4-113463e92565 | -8.87424 | -45.2457 | 2025-10-13 00:52:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4df64c61-1aca-32be-884d-2a853db91790 | -10.97869 | -59.01895 | 2025-10-13 00:52:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b9a5256b-c609-359e-afc0-64085b65c48a | -16.12977 | -53.96558 | 2025-10-13 00:52:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 35cc2641-e6dd-37ae-8449-61aa74eb39c6 | -8.33054 | -46.23706 | 2025-10-13 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 5e3d2ac6-c7c8-311d-bc80-586ae473ff1d | -2.54786 | -47.80315 | 2025-10-13 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 05dda618-cbf4-3abc-bba8-bae85c52b0a0 | -3.09357 | -50.37663 | 2025-10-13 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| e9f70df8-d2e3-3e84-b476-37cc8f3d41b9 | -3.27529 | -50.04326 | 2025-10-13 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e3cec309-0d0d-318b-9017-1cdb3b14a914 | -3.26586 | -50.13943 | 2025-10-13 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7d676697-5d9b-31d6-9fef-f0cfabed0155 | 1.89201 | -55.76711 | 2025-10-13 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 1c7bee9e-a525-3768-8c64-4caa0fbace48 | -3.60882 | -48.91409 | 2025-10-13 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 40e7417b-2111-30f1-945d-d4b98f1c00bd | -3.12827 | -50.21827 | 2025-10-13 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 1dc06f6c-84b2-3b8a-936b-9d8b1f9dfb51 | -2.88122 | -50.73474 | 2025-10-13 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 8fa15f7d-7da2-3daf-b7df-825decc85f23 | -3.0659 | -49.40398 | 2025-10-13 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| ac3a1d0a-803a-3cec-87af-9b8e0837e720 | -3.92661 | -50.01533 | 2025-10-13 00:54:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| d2c4d3de-3fc9-3aaf-bea3-764354bfcc5c | -3.09216 | -50.36831 | 2025-10-13 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| dcf0bc04-c86e-315d-8bd9-d8024cb4df22 | -3.09422 | -50.38304 | 2025-10-13 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 5a80d1f3-d8b2-3781-8b32-24a247712aa2 | -3.23215 | -50.05608 | 2025-10-13 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 87bacdb4-a4e3-397b-ae57-d6ab3b19fabc | -3.81419 | -51.15525 | 2025-10-13 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 96678a51-2fb1-3333-b189-e6c4f7b652ba | -3.26361 | -50.12407 | 2025-10-13 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e51fcfc5-bee9-3456-9122-c2128f77dd32 | 1.89443 | -55.74951 | 2025-10-13 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c97ab521-14b1-3f1f-83b0-13205a20109a | -3.13966 | -50.21667 | 2025-10-13 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| a8ad6dda-6f0e-3dfd-ad9e-63fe8621f35c | -1.89423 | -51.00748 | 2025-10-13 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2fec751c-a25d-3304-886e-aa7e097e89df | -2.99038 | -50.29713 | 2025-10-13 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0b065bb6-a9da-3f0f-90f8-ffc4f05653cb | 1.89322 | -55.75831 | 2025-10-13 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 81d14a1b-babe-3d21-94bf-06d8da9f7d2b | -5.04585 | -49.88348 | 2025-10-13 00:54:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 945e4363-3b9b-374e-b857-dcd7c87cd6ac | -5.21605 | -50.95313 | 2025-10-13 00:54:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 37f38632-b684-37c8-b0f2-9a0e3fe35bbb | -3.9152 | -50.01694 | 2025-10-13 00:54:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5628f005-9c4e-3989-8d70-34a4bf9e39a3 | -5.22642 | -50.95155 | 2025-10-13 00:54:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1d4c54d0-9ab5-3024-9daa-09c27d924885 | -1.89829 | -51.0146 | 2025-10-13 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| aea32f5f-b335-312d-ae60-c63fef530358 | -3.09572 | -50.39119 | 2025-10-13 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| fd320abe-4fbf-3437-9d11-6ac5061fa31d | -3.22925 | -50.04996 | 2025-10-13 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 15ad11fa-5e55-3bbe-9e03-ba8d13c62186 | -2.53868 | -47.79801 | 2025-10-13 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 30ddf04f-d148-3b01-a02b-939df8715661 | -2.91477 | -49.17376 | 2025-10-13 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| f92fd0cf-fe21-37f4-a362-88ed8a4274db | -2.91279 | -49.18068 | 2025-10-13 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 987650de-46c1-3172-bf94-134f7e453218 | -5.43997 | -51.36196 | 2025-10-13 00:54:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 85f2ed38-6dad-36c5-83e8-71854bc1e1bd | -3.13748 | -50.20133 | 2025-10-13 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 96c05c82-fd48-3ca5-9c79-63404185e566 | -2.5339 | -47.80554 | 2025-10-13 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 1b5a0b47-4425-3edc-ae43-d23acbdf4414 | -3.41302 | -51.224 | 2025-10-13 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d1239783-28d3-3d5b-ae20-3d224e02f3eb | -2.98894 | -50.29175 | 2025-10-13 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 03a4cfef-619a-3f3c-a787-87950a50cfd9 | -2.54232 | -47.8223 | 2025-10-13 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| ec29756b-21b7-35cc-ac53-1370191eda6e | -2.70249 | -54.65227 | 2025-10-13 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cf848547-f9e8-3721-b73a-8e6de3fc4e32 | -5.91421 | -45.42377 | 2025-10-13 00:54:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| bbadf1b1-f701-38df-8c2e-54ea41f2d4e8 | -3.0685 | -49.42164 | 2025-10-13 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 7234e2b5-a525-36a2-8018-10161167a653 | 1.92059 | -55.69031 | 2025-10-13 00:56:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b3e39a26-bbfe-3543-a246-722c58184bf8 | 1.91298 | -55.68026 | 2025-10-13 00:56:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 07187faa-9d4c-37e9-a5e8-d10f63f97103 | 1.91937 | -55.69913 | 2025-10-13 00:56:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| af700c93-b016-3179-a85b-8217dfa4c7fc | -14.3015 | -51.5573 | 2025-10-13 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 143.9 |


[Clique aqui para ver as próximas entradas](README4.md)
