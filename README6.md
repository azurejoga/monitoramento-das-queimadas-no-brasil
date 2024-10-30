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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49e2571d-6ddd-37b0-b095-75e6787684e4 | -3.7852 | -51.1651 | 2024-10-30 00:25:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| fae18e32-4498-3e0a-875e-485d893f5b32 | -3.8036 | -51.1852 | 2024-10-30 00:25:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| fa0a0afc-7b98-3b1d-b9b7-a5d89475f7df | -3.8037 | -51.1644 | 2024-10-30 00:25:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 215.0 |
| 9cdf9f46-ebdd-3622-8621-27aa4fb0c676 | -3.8038 | -51.1436 | 2024-10-30 00:25:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| a3258fde-e4e6-3e19-b835-50bc1de063a3 | -3.9326 | -41.4957 | 2024-10-30 00:25:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 132.4 |
| 9c82113f-ddb7-3ab9-8dcc-05e72b24e7e0 | -3.9327 | -41.4717 | 2024-10-30 00:25:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 8419597a-2216-3887-b839-e299ae7644fa | -3.9513 | -41.4946 | 2024-10-30 00:25:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 82eab4db-bb05-33a2-a0ae-1e80d9281c38 | -3.9514 | -41.4706 | 2024-10-30 00:25:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| 8de610ca-d776-31ff-8d30-08892aabb570 | -3.8221 | -51.1637 | 2024-10-30 00:25:28 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 07ce2703-7351-3402-939b-9b0e0de85a64 | -3.9486 | -48.1291 | 2024-10-30 00:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| d5147d20-9968-3435-9851-3ec5576d553f | -4.0681 | -50.024 | 2024-10-30 00:25:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 89984dcd-2ddc-383f-b768-26873ef00fb2 | -4.0911 | -45.9488 | 2024-10-30 00:25:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 85325f35-f7be-3a96-93e4-8c42e5ac77bd | -4.2561 | -43.46 | 2024-10-30 00:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 10372e29-28b2-3f5e-87e8-afd65fdca9dc | -4.2563 | -43.4368 | 2024-10-30 00:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 154.3 |
| af8d45e9-82e4-31cf-88f5-58534e4cb66b | -4.2748 | -43.4589 | 2024-10-30 00:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 4a21c2fb-548c-3e37-9b2c-6e639a2d24c1 | -4.2749 | -43.4357 | 2024-10-30 00:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 7b1a5b48-d5c1-35b1-a878-001643ffc6e2 | -4.3473 | -43.779 | 2024-10-30 00:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 6cc3b6a0-5d22-3d71-ad74-877c606312bb | -4.2495 | -50.6886 | 2024-10-30 00:25:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| f0d4f166-f2d6-3502-ac14-7ff1499cbc9f | -4.2496 | -50.6677 | 2024-10-30 00:25:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 978a703d-7957-351d-abd4-6f30c4f5e51e | -4.2679 | -50.6879 | 2024-10-30 00:25:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e144c5ca-c73e-3d64-b9cc-4634d5fef1e9 | -4.2681 | -50.6669 | 2024-10-30 00:25:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 489afbf8-4957-3c80-a985-2e1b8d5c1938 | -4.5012 | -43.143 | 2024-10-30 00:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 43c658ce-8385-321a-bc1a-19a9ba7b353d | -4.5014 | -43.1196 | 2024-10-30 00:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 31ac6045-c9c1-367f-9a09-0de45852f83d | -4.4269 | -45.8199 | 2024-10-30 00:25:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| e4fac4c6-1d2a-30c2-8bc6-cbc15f6a8df2 | -5.2306 | -47.9566 | 2024-10-30 00:25:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 65bbe258-0fd1-3cc8-ba82-00f6129fd5ad | -5.2308 | -47.9349 | 2024-10-30 00:25:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| df456a72-c915-3ee0-8616-ff4365025a3a | -5.9788 | -45.3621 | 2024-10-30 00:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| ad79f107-6b76-3857-9cc3-f9264dff6529 | -6.8408 | -59.0519 | 2024-10-30 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| f46e351b-953c-37a7-8a9b-bef46395c79b | -6.8592 | -59.0511 | 2024-10-30 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 132.9 |
| d948504d-2d85-350f-bb14-dc037d9a1f1a | -6.8593 | -59.0318 | 2024-10-30 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 9aab89bc-f7f6-386a-b360-9139c27192f1 | -7.8736 | -46.9065 | 2024-10-30 00:25:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| e42a10b6-f2fc-3f51-9179-11f1ec85fec2 | -7.8739 | -46.8843 | 2024-10-30 00:25:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| ca7e2ef8-f437-31b7-a992-300f8c56efc7 | -7.8924 | -46.9048 | 2024-10-30 00:25:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| ae580a01-81a1-3ec7-acd5-fdab46731c8d | -9.1552 | -45.3385 | 2024-10-30 00:25:57 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 48.1 |
| c527314a-427d-3270-a657-71ba56d8c421 | -9.5563 | -63.1411 | 2024-10-30 00:26:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b9289154-61cc-3587-9f4a-952e096862ee | -10.7171 | -44.9391 | 2024-10-30 00:26:06 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 32cf7ad5-0829-3958-ac22-d35434100bde | -10.7175 | -44.916 | 2024-10-30 00:26:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 222.5 |
| 16e9f564-1a76-322b-9130-bc5812474785 | -12.6536 | -43.8075 | 2024-10-30 00:26:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| e0b6d5bd-8344-3c00-9833-1e0483160ba0 | -12.899 | -45.0549 | 2024-10-30 00:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| b486ccfe-3094-3ece-8569-d293a7187e19 | -13.6891 | -46.1017 | 2024-10-30 00:26:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 9fb457ab-9fd6-3869-be3f-1090a432f2ac | -18.2454 | -55.9793 | 2024-10-30 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.1 |
| df836cac-5c29-36b7-a86e-0cf7686260cd | -18.2652 | -55.9766 | 2024-10-30 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.6 |
| 3f6f1830-9d6d-3d50-af73-dc81fe6f24da | -23.9923 | -54.1106 | 2024-10-30 00:27:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 45.8 |
| b776e724-2ce1-34dd-ba9c-7f3b9c68f44d | -15.81403 | -42.49788 | 2024-10-30 00:28:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 0a63607d-ab87-35d0-9529-2ac8afc86a74 | -15.81269 | -42.48771 | 2024-10-30 00:28:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 52896bff-f724-3721-8c5b-0e5949f43700 | -15.65231 | -39.18493 | 2024-10-30 00:28:00 | TERRA_M-M | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 32a3d45f-2f67-355e-876a-4c8f3c7bebdc | -15.60591 | -43.72616 | 2024-10-30 00:28:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 24.6 |
| d16990ab-e748-3d80-8739-c858e2c13316 | -15.6044 | -43.71433 | 2024-10-30 00:28:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 5d6f554d-5701-3556-9901-bfb1e6634852 | -15.57416 | -40.65552 | 2024-10-30 00:28:00 | TERRA_M-M | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| f08b7025-f279-3864-83e9-1be3869b2b34 | -15.36913 | -42.05667 | 2024-10-30 00:28:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| be742bfa-c318-331e-af3d-ad5646afa6d7 | -15.36783 | -42.04687 | 2024-10-30 00:28:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| fc39d4e2-3bf0-31db-8b03-038034c5d90b | -13.93451 | -42.9533 | 2024-10-30 00:28:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 102c5cd1-49a6-3556-8b96-dc4e42a567c1 | -13.91847 | -41.93808 | 2024-10-30 00:28:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 16921879-e920-359d-a52b-6635e8ed36f4 | -13.90871 | -41.93618 | 2024-10-30 00:28:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 4bac9f16-1b70-3b49-a41b-1d4c73c48402 | -13.89596 | -43.35928 | 2024-10-30 00:28:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 9f2817c0-fe6a-37bb-8f9e-c2a785f4d1ea | -13.89456 | -43.34858 | 2024-10-30 00:28:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| a90bb6eb-faa3-3d86-9995-a235fc5bfe9c | -13.86668 | -43.06332 | 2024-10-30 00:28:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| e9a217f8-0a9b-325e-8599-39ec9e889b89 | -13.82637 | -42.35048 | 2024-10-30 00:28:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b0aa784c-7188-37d7-9ca3-5af47b5eb96a | -13.77473 | -40.68905 | 2024-10-30 00:28:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| bc65bdc8-97f5-37e9-b553-ae27b20183d4 | -13.69432 | -46.11431 | 2024-10-30 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| abfe95c8-defa-3711-bd58-ddef5fa32a58 | -13.69236 | -46.09823 | 2024-10-30 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 82d78fae-5835-35a3-befb-327b1e46299a | -13.68269 | -46.11567 | 2024-10-30 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| e2b73a1c-bf6f-3a7f-9e4b-0119a1a0edb2 | -13.68073 | -46.09949 | 2024-10-30 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8ab66e0b-0041-351e-abea-90ae2266c175 | -13.61001 | -43.98568 | 2024-10-30 00:28:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 183b0064-e6d9-3f42-81fa-feb673541644 | -13.47655 | -43.25839 | 2024-10-30 00:28:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 27.9 |
| e9e3b060-3586-3719-9dc0-6bc89000ff16 | -13.25504 | -43.67679 | 2024-10-30 00:28:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 69f10337-6866-30cd-a65c-fa89f4d1548a | -13.05462 | -40.34966 | 2024-10-30 00:28:00 | TERRA_M-M | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 6889e08a-d650-39eb-b708-273cf4810fcc | -12.63059 | -46.89253 | 2024-10-30 00:30:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 872ead1d-5272-3adf-a8fe-9024083282cf | -12.62438 | -46.88184 | 2024-10-30 00:30:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ae72eb56-b1f7-3b43-b601-04c36645aed8 | -12.62862 | -46.87562 | 2024-10-30 00:30:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 94a425d7-7492-370d-a9cd-280d88c3e7d4 | -12.42935 | -46.63148 | 2024-10-30 00:30:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8bf3ddef-197e-3f9c-8cda-e6678456ad4a | -12.09577 | -47.24425 | 2024-10-30 00:30:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f7c19772-6a53-32b0-b1d2-2f807e580877 | -12.00235 | -47.65449 | 2024-10-30 00:30:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| f90a9b8d-9ee6-3b12-97f8-81cf0bc55407 | -11.88095 | -46.53287 | 2024-10-30 00:30:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 896bc63f-f054-3ba2-a84e-e0cb2a9751e5 | -10.61562 | -47.71621 | 2024-10-30 00:30:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 48ab7dbb-492d-3596-89fa-142ab1069d6d | -10.50726 | -49.01603 | 2024-10-30 00:30:00 | TERRA_M-M | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| ed2b4907-92cc-3a23-a586-82afcee0980d | -10.50203 | -49.02192 | 2024-10-30 00:30:00 | TERRA_M-M | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8e5d6e10-a3ef-3d89-acc2-05c9f1848dd1 | -10.20183 | -49.15147 | 2024-10-30 00:30:00 | TERRA_M-M | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| af1bae2b-6b7f-3dc4-b470-d5f554b33879 | -9.93985 | -36.47218 | 2024-10-30 00:30:00 | TERRA_M-M | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| f2734fbe-f519-31f3-9b7c-7e080d9733da | -9.85712 | -44.78427 | 2024-10-30 00:30:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| efd943dc-8750-303e-9d75-19ce9bd87ca3 | -9.52113 | -35.72393 | 2024-10-30 00:30:00 | TERRA_M-M | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| e60c32c4-4078-3bad-8fdb-9e3b0afe9cec | -9.47295 | -40.38242 | 2024-10-30 00:30:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 48a49b87-0934-3667-bb5e-d3c49022ac29 | -9.1352 | -40.92416 | 2024-10-30 00:30:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 24e52aa6-02de-305f-b1f5-b0334fce12c6 | -9.13392 | -40.91508 | 2024-10-30 00:30:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 1df9d154-f3be-36e5-9ca9-54363bbe88c9 | -9.1123 | -43.21413 | 2024-10-30 00:30:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 0f9ddcfb-8a75-3abc-af5d-9b580ce52f68 | -8.62542 | -40.57909 | 2024-10-30 00:30:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 51d3a860-c0e3-32e2-a109-a532a97b8b64 | -12.90286 | -44.60038 | 2024-10-30 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 42949932-4530-3fa7-8215-fe10aa5e5fc5 | -12.9004 | -45.05938 | 2024-10-30 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 14c76d50-e492-34fc-8f18-d417d5540599 | -12.88982 | -45.06078 | 2024-10-30 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| b1e89606-8093-314b-83e6-00ea6b576d05 | -12.88543 | -44.6278 | 2024-10-30 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a45b9057-bce7-3925-b886-9feeea2e2fd8 | -12.88392 | -44.61557 | 2024-10-30 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 10928701-d5fa-3955-86d3-14a6496a36e5 | -12.8765 | -44.62227 | 2024-10-30 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 2c9a273f-69fa-3194-b804-62d018b23f07 | -12.67035 | -43.82162 | 2024-10-30 00:30:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 619851eb-e447-3588-bb5e-b02385c0da62 | -12.66066 | -43.82296 | 2024-10-30 00:30:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| ff223bac-64d7-3589-9a85-d2972f8b9471 | -12.65923 | -43.81203 | 2024-10-30 00:30:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 2c8e906b-4ab8-3f34-93d6-399d0cb50fd6 | -12.65096 | -43.82428 | 2024-10-30 00:30:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| d661b96e-f0fd-3da5-b839-da74dead7eaf | -12.64954 | -43.81336 | 2024-10-30 00:30:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f5fc5b4e-1ce1-3ef7-80cb-5d361f09cdda | -12.37073 | -45.66711 | 2024-10-30 00:30:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| d583c7c1-8b0c-37aa-8144-a6ff39dd314e | -12.36929 | -45.67363 | 2024-10-30 00:30:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| cd9c5b68-4d8d-3bc6-b93c-f47dae2e0de6 | -12.36748 | -45.65934 | 2024-10-30 00:30:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |


[Clique aqui para ver as próximas entradas](README7.md)
