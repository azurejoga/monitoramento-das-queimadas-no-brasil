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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7779291-99a2-37c6-b741-e4d3ae47932d | 2.00109 | -55.70593 | 2025-12-03 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9d7320f-2b13-31ff-a2ca-59df11bef85f | 1.99091 | -55.71769 | 2025-12-03 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1c5aa043-9922-325d-a96d-22c9aec81ba1 | -2.99187 | -49.52811 | 2025-12-03 05:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae046398-d2b7-3645-988a-3815c2b832e0 | -2.80046 | -52.90563 | 2025-12-03 05:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c9d453ca-a4de-3e4d-8b7e-554c9045d2fd | -3.77134 | -50.13643 | 2025-12-03 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3316fe0-9f67-3e4c-b05e-2e275c509c49 | -3.06455 | -54.02757 | 2025-12-03 05:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9b82ab9-455d-3f99-83ff-5767daec5b8e | -2.98069 | -49.5154 | 2025-12-03 05:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f41d4de-70ff-36fe-a1a8-22d6b4da6294 | -3.30723 | -52.57248 | 2025-12-03 05:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5757418f-3833-3964-acf4-c335c172b5e9 | -3.63068 | -48.89508 | 2025-12-03 05:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2675adbb-5284-31b8-8708-726a2a785182 | 1.98699 | -55.71828 | 2025-12-03 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1dce9d4e-1047-34e6-94eb-8fd3c020da08 | -1.1977 | -53.09318 | 2025-12-03 05:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aadd3161-03a8-35a3-868f-4acf6c59cfe9 | -1.19497 | -53.08841 | 2025-12-03 05:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| db248754-5dee-39de-8544-b57d490b9fe5 | 4.15833 | -59.9347 | 2025-12-03 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67e3303a-2431-3383-8b8f-7d77f4b1ff6e | 4.15562 | -59.91755 | 2025-12-03 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ff63c49-523e-33ea-b1ee-9a03da066273 | 0.72614 | -60.47889 | 2025-12-03 05:29:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5cc03c31-303b-35d5-93e4-7aced96e9884 | -3.30769 | -52.56932 | 2025-12-03 05:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd296f90-20e2-3852-8616-6ce1422e5975 | 2.87472 | -60.26384 | 2025-12-03 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab41ff8a-861d-3ad8-9316-4d08e92c3ef2 | -2.38126 | -49.38908 | 2025-12-03 05:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e04c9e6-2c50-39f5-ab0e-315b5cba8b16 | 4.16438 | -59.93024 | 2025-12-03 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9778c1e6-9682-333d-b13b-84da702db3ce | 1.99012 | -55.71274 | 2025-12-03 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7b6e899f-b37c-3710-a683-cada0b684994 | 1.98306 | -55.71887 | 2025-12-03 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c89bbe70-54a4-3ddb-bbc1-8d50fe599521 | -2.98548 | -49.52709 | 2025-12-03 05:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e2135f6d-9981-3308-9f84-291cde1c1383 | 4.15232 | -59.91806 | 2025-12-03 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b280a92-0575-30b7-83f3-2b5f6a515503 | -2.21157 | -48.00632 | 2025-12-03 05:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 80a007f0-0d55-3fe8-aa6e-38cddda77586 | 4.16542 | -59.95819 | 2025-12-03 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc9ee82b-d78c-3f5d-bb4f-903e38506bf7 | -2.35841 | -50.10911 | 2025-12-03 05:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 255af561-c924-39fc-9195-1175f6c8b9a6 | 0.48124 | -51.15291 | 2025-12-03 05:29:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1de2719d-e099-364c-ae78-796d7a5c8e85 | -3.63367 | -48.8976 | 2025-12-03 05:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6d5d8c2-7506-3508-9c2d-cbbcdc42b44d | -2.20563 | -47.99891 | 2025-12-03 05:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cd745e34-f33f-324c-9944-9a4e953dcee0 | 2.00502 | -55.70537 | 2025-12-03 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f417a011-cfc6-3d3b-b4e2-30a48e4f8e6c | -2.09143 | -53.41579 | 2025-12-03 05:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58c6d1e8-ef95-38b7-a879-0e0f6709e186 | -2.35159 | -50.11283 | 2025-12-03 05:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90fc6b9b-bc2b-3544-98c3-205b3da247a6 | 0.00254 | -60.58561 | 2025-12-03 05:29:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a7eb9f5-4203-3d36-96bb-25cdb7080928 | -1.06612 | -53.6117 | 2025-12-03 05:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b22ee1c8-93f7-38f9-b91d-d038aed45aa2 | -2.20484 | -47.99899 | 2025-12-03 05:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f780fe84-351a-3700-9aa2-315b6d01a53c | -3.30783 | -52.57161 | 2025-12-03 05:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99ef549a-c4a5-32d2-b6eb-496080298f57 | 1.97682 | -55.73001 | 2025-12-03 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d090921d-f546-31e0-940a-bb6653390b4b | -3.7443 | -50.97734 | 2025-12-03 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 66fd0f6c-775b-3a4e-ae94-e1e3f4ba00ec | 2.01683 | -55.70377 | 2025-12-03 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d41163f-da48-39ec-a7f1-181d458d668c | -2.20388 | -48.0054 | 2025-12-03 05:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4f867133-b2e7-3a71-afb6-34bab3a984e9 | 1.99405 | -55.7122 | 2025-12-03 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30b32e35-33ce-3b1c-8ada-09c8eb05a914 | 4.15449 | -59.93178 | 2025-12-03 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d1dd849-ebff-376a-aa11-9fd053024ba6 | -2.38244 | -49.3907 | 2025-12-03 05:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcb75497-a76a-3968-9d3b-518da3cb37cf | 4.15503 | -59.9352 | 2025-12-03 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e4a08b2-fb0f-322b-82fd-7bbbeb915e78 | 2.87748 | -60.25989 | 2025-12-03 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5cac6716-f23c-3b97-8f2b-7a8f76b4ede4 | 1.97994 | -55.72445 | 2025-12-03 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd0eb125-5a96-341e-a11d-62d72b59ca09 | -2.68713 | -51.7976 | 2025-12-03 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3538713-9c9e-3373-9b8c-f7073633a1c5 | -2.83816 | -50.46442 | 2025-12-03 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22fbec15-89c8-308e-95d0-1e62dbeeedcc | 1.98386 | -55.72385 | 2025-12-03 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7bb9be1-58f6-315f-bdc6-03edf38551d1 | -2.70553 | -49.31074 | 2025-12-03 05:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d701ec5a-17c1-393c-815b-48fcb0e69609 | 1.08729 | -60.65384 | 2025-12-03 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 43716e82-1cb7-36de-9745-223bcb1ee06b | -3.14947 | -50.56245 | 2025-12-03 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff684f61-6d2b-3f08-9763-f06180810a00 | 2.87802 | -60.26332 | 2025-12-03 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fc4a8be-d9ad-304e-b6cb-d18590c64ee4 | -2.83748 | -50.46888 | 2025-12-03 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23841074-770d-3fba-9189-4455775da432 | -3.7706 | -50.14134 | 2025-12-03 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07f6167b-6709-3cb3-9d0d-35e96b642bfa | -15.11619 | -52.94637 | 2025-12-03 05:31:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9425e6ec-0abc-355d-b29e-21821588e876 | -15.11569 | -52.95097 | 2025-12-03 05:31:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4688fd7-cee0-3879-a54a-b4a9fcff6b1c | -15.12172 | -52.95188 | 2025-12-03 05:31:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c06eaca8-eac2-317a-9999-2cc07544a6bc | -19.63244 | -56.77962 | 2025-12-03 05:33:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f79cdc7a-b2bf-34fb-adb8-5cf3070073fe | -19.61479 | -56.80172 | 2025-12-03 05:33:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 45187c5c-eb89-309a-a31d-e208886570ee | -19.62677 | -56.78501 | 2025-12-03 05:33:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 541df254-9b64-392c-b55f-3bf98d77cd49 | -19.63177 | -56.78562 | 2025-12-03 05:33:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| e47a4f82-58b0-3652-b5c2-8010d3cd7a53 | -19.62244 | -56.77841 | 2025-12-03 05:33:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8e3be236-266f-383e-86d9-d51799ae5658 | -19.61611 | -56.78979 | 2025-12-03 05:33:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 68f18ca5-6248-3b2f-b690-fcc39c29ed38 | -19.61978 | -56.80234 | 2025-12-03 05:33:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 12dd76f4-83e6-34c1-9c37-b7a9a5a8b356 | -19.63744 | -56.78024 | 2025-12-03 05:33:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fb0b1129-9e65-3249-a8fb-be49dbf1e790 | -19.62744 | -56.77901 | 2025-12-03 05:33:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 031ff528-8118-36ff-826d-8753cf770373 | -21.62124 | -56.13371 | 2025-12-03 05:33:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59607690-2428-3d71-a909-640c106b5644 | -21.62621 | -56.13797 | 2025-12-03 05:33:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6a86624-d141-3fed-a5e3-ab30e9b1d8ee | -19.61545 | -56.79575 | 2025-12-03 05:33:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 239877b8-3754-39a6-942f-ba130610c4ea | -19.61678 | -56.7838 | 2025-12-03 05:33:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| db2cb420-a135-36ce-8142-17e0dc58e8f6 | -21.62658 | -56.13435 | 2025-12-03 05:33:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb190d3d-ff67-3dc0-945b-e23fe4a5ca39 | -19.62177 | -56.78441 | 2025-12-03 05:33:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1764a7f2-5864-3446-b2ac-9706d1b56ede | -21.62087 | -56.13734 | 2025-12-03 05:33:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c3247b9-4b21-32ab-ba60-b564ce05c215 | -8.163 | -43.229 | 2025-12-03 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 62bbdc90-556a-309c-8d35-ed9b78b10e00 | -8.163 | -43.229 | 2025-12-03 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 6c4e0442-466b-307a-93e0-6e6882e6e63c | -4.3892 | -43.1263 | 2025-12-03 06:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 596f361f-4144-337d-9237-ee7bfea73ec0 | -8.163 | -43.229 | 2025-12-03 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 53d55762-0118-30c5-8131-cd3e682fb088 | 2.87223 | -60.26477 | 2025-12-03 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20b6dda4-6755-317c-9381-d299d080ef05 | 2.87879 | -60.26358 | 2025-12-03 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a3996797-423a-3520-bfde-6f891559cce8 | 2.87783 | -60.25791 | 2025-12-03 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f0e18655-b673-3dda-933d-d997d713631a | -8.163 | -43.229 | 2025-12-03 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.6 |
| 773345a3-1b4b-36ca-95f7-87fca0d4f0ae | 3.48493 | -51.25313 | 2025-12-03 06:22:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 24f4acd6-4085-3daa-b3d5-e27c1063bd8e | 0.4842 | -51.14741 | 2025-12-03 06:22:00 | AQUA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 073b6a88-4982-323e-a903-4ef746383eab | 3.47575 | -51.25446 | 2025-12-03 06:22:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 99d0e4e7-012d-3934-a0ac-21319a4b3c01 | -2.17062 | -48.36335 | 2025-12-03 06:24:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ca68d583-0c50-36e9-bf4c-ba5d94e09903 | -4.39429 | -43.11612 | 2025-12-03 06:24:00 | AQUA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 6d5478a3-51a0-3c91-8340-0cb659a34f45 | -2.38877 | -49.38691 | 2025-12-03 06:24:00 | AQUA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 583632c0-2098-30b0-b1d3-55b0c0ccba02 | -4.39557 | -43.12345 | 2025-12-03 06:24:00 | AQUA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 35ef1896-3d87-3959-9315-09537f91e249 | -2.37983 | -49.3856 | 2025-12-03 06:24:00 | AQUA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5c3388e9-493c-3d27-af8e-7cce26dfd3ec | -3.59344 | -47.25835 | 2025-12-03 06:24:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| eb5bde1a-253b-31e2-bddd-4daf3fc6d73a | -2.69635 | -49.30985 | 2025-12-03 06:24:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e5e8f5e5-53ac-3dc8-b8f9-70abc5b55511 | -2.98734 | -49.52049 | 2025-12-03 06:24:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c4237708-74aa-32df-b8bf-56b14d36b38a | -2.83705 | -50.45868 | 2025-12-03 06:24:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0aec2fec-b818-3ab3-8de0-c31b98b6aa84 | -2.70533 | -49.31116 | 2025-12-03 06:24:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c52bdbc0-252f-32b1-8bfb-9822302e17ba | -2.98871 | -49.51141 | 2025-12-03 06:24:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ecec8bed-d97d-3de8-bae5-a0df297e22df | -1.20064 | -53.08686 | 2025-12-03 06:24:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 89f93271-9818-336c-a278-0e0ba5ca1365 | -3.05083 | -48.42295 | 2025-12-03 06:24:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 711aca3c-8d01-32e7-9e37-c7334c11bf5a | -2.91871 | -48.23167 | 2025-12-03 06:24:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5d7375d8-8c14-3355-a6fd-588c4d156b53 | -10.52654 | -48.88654 | 2025-12-03 06:24:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |


[Clique aqui para ver as próximas entradas](README21.md)
