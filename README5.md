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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f044f4f9-8041-3064-bfb4-fa48f146b1da | -12.02252 | -47.77798 | 2025-07-17 00:24:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| fee7eb12-b198-3ffe-af53-e99c022d4288 | -14.03494 | -51.23794 | 2025-07-17 00:24:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 2ddcc961-8110-3327-a106-a94ff331ec3f | -7.20365 | -45.3364 | 2025-07-17 00:24:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1cc0318c-ddf2-3465-8fa1-69d0ae35a29f | -8.54064 | -47.8447 | 2025-07-17 00:24:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b790877a-1c9a-36c2-97eb-5d1b149ac04a | -6.97096 | -42.80316 | 2025-07-17 00:24:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f3525613-5299-35ec-a5cd-f2bc7b77ff25 | -12.41076 | -50.04659 | 2025-07-17 00:24:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 9c0b5430-070b-3a2e-b9c1-25289f292404 | -12.03394 | -47.78799 | 2025-07-17 00:24:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4f3d0229-ba3b-35cf-9737-d72ececd4b5a | -12.19285 | -43.47036 | 2025-07-17 00:24:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3802d83a-b9f7-3480-8cc3-fc066ffe247a | -14.32126 | -48.65392 | 2025-07-17 00:24:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5e774700-4a19-36b7-9c52-fc0148c8cace | -12.03248 | -47.77669 | 2025-07-17 00:24:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| d58fa760-fd54-3183-a23e-e9a08ed20b08 | -11.94173 | -48.41375 | 2025-07-17 00:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 1d15c7c4-6095-3fee-acce-0cb1b86d1e2c | -11.94969 | -48.41988 | 2025-07-17 00:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 9cecb801-4097-3b4c-b77a-13193d326aa5 | -8.09362 | -43.15075 | 2025-07-17 00:24:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| f27eaf80-a017-30b6-8cce-824c85ae2de9 | -11.94335 | -48.42635 | 2025-07-17 00:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 28fb29cd-850e-3adf-988d-5ac8acf6c283 | -7.23753 | -43.49747 | 2025-07-17 00:24:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 33173456-4417-3547-a688-54083da976fb | -8.10899 | -43.15308 | 2025-07-17 00:24:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 195.6 |
| 9fef73f2-db87-39bf-9515-05d919858d2e | -8.0415 | -49.8805 | 2025-07-17 00:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| e9dc6dbd-bbb4-3844-a178-e9fc755dd23f | -12.41685 | -50.03928 | 2025-07-17 00:24:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| a481b6ab-4aba-33d1-b60b-17f58bb0d021 | -9.88482 | -47.80934 | 2025-07-17 00:24:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| eb2af544-ad76-35f9-92d5-dedd8e5a6f71 | -17.0445 | -43.7789 | 2025-07-17 00:24:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 933f896a-f021-37fb-8f7b-7bee1abd206c | -11.53035 | -48.95015 | 2025-07-17 00:24:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4254a06f-0841-3a66-a76e-715e2f5d3abe | -10.65863 | -49.47844 | 2025-07-17 00:24:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 61e01646-9ae6-33e6-a8f6-9a735a115242 | -10.21867 | -47.33087 | 2025-07-17 00:24:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 93c43cb8-1b14-3a1d-93dd-10c2075a12ea | -6.97257 | -42.81412 | 2025-07-17 00:24:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 13279fde-8ded-3ae5-b0d3-3fe9b7cccaee | -12.09806 | -48.20357 | 2025-07-17 00:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0491e0c9-7228-3a0c-9ba5-fc41d7bb76f2 | -7.88955 | -55.38541 | 2025-07-17 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 4c06e607-ae81-3d58-92f1-e02303a433b1 | -6.88678 | -47.24722 | 2025-07-17 00:26:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a3823db6-b64d-340c-8ef0-775160010a60 | -5.65828 | -43.71641 | 2025-07-17 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 540.7 |
| 33af6ad6-9df8-384e-bcaf-10467b12d3b0 | -3.39459 | -47.49326 | 2025-07-17 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f91b8204-9585-3182-b200-b293443802e0 | -5.78678 | -45.08432 | 2025-07-17 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| fadc9674-1acd-3f5f-89f9-b553a3ffcc3c | -6.73162 | -44.3329 | 2025-07-17 00:26:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 99be0dab-6415-3b8a-a7c0-d10004a4a962 | -5.57436 | -44.29112 | 2025-07-17 00:26:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6348b0b9-eb10-32d3-9b71-e22ef61f88e2 | -5.66769 | -43.715 | 2025-07-17 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 163.8 |
| aa9885ae-997c-3ec2-ab05-e0e74415b8bb | -3.39335 | -47.48418 | 2025-07-17 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| ba8c3a75-1b85-31d3-96d0-2433f37da577 | -5.78929 | -45.10232 | 2025-07-17 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2e3e63bb-b398-31b9-9c04-3b8e1db559c8 | -3.66552 | -48.3194 | 2025-07-17 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7c044b87-0468-3230-a0b0-7812b0038432 | -3.58365 | -47.52893 | 2025-07-17 00:26:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 4af8eb04-7fb3-305b-a68b-3cc59855544f | -6.71081 | -44.31681 | 2025-07-17 00:26:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 392570f6-8a9e-30ca-bfbc-a43882868afa | -3.04393 | -49.43161 | 2025-07-17 00:26:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 66cb439a-9909-3234-b80a-10ed42c7723d | -3.41504 | -47.509 | 2025-07-17 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 265b3e97-96fc-3dc7-ad1e-30eaef48bc57 | -5.53542 | -43.87941 | 2025-07-17 00:26:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 16e60db3-fc32-39cf-8044-a48c16b6b719 | -4.78189 | -45.34108 | 2025-07-17 00:26:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 91829895-c73f-378d-8a64-53782aafe2de | -3.39709 | -47.5115 | 2025-07-17 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0863da65-ce90-3a31-82e0-cfb019fe585d | -5.91288 | -45.58808 | 2025-07-17 00:26:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 59fefbab-aec6-3957-a450-92091f45cc95 | -6.3143 | -43.66037 | 2025-07-17 00:26:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 56631798-dbbe-3574-91d2-bfdf6766e23c | -2.9254 | -48.23909 | 2025-07-17 00:26:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a04d5279-b78e-367a-a246-4b080e928596 | -6.62731 | -49.74879 | 2025-07-17 00:26:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7b90c1a9-4c7b-376b-ad92-01c46afe9a1a | -3.03116 | -47.86388 | 2025-07-17 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| ee483667-abf7-314d-ae8f-19ee91e953f3 | -6.84784 | -44.76629 | 2025-07-17 00:26:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| b850b989-4b6d-366a-b7d5-dbf1b43e6fc3 | -2.44338 | -47.33894 | 2025-07-17 00:26:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c23cdd4a-7820-3613-8c8f-e7a3cbcd7bb7 | -4.65246 | -43.12361 | 2025-07-17 00:26:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| eb235b20-e1a7-3a6b-8f29-4a618fe1dec4 | -5.79946 | -45.11001 | 2025-07-17 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f73e5e41-e567-33dc-bdbf-e6d4fefb3c5b | -3.40606 | -47.51023 | 2025-07-17 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 15fdbd08-05d4-3244-9d12-d29e9c859410 | -7.1529 | -46.091 | 2025-07-17 00:26:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0f39704c-4a1e-36ec-83da-b76f4201d7c1 | -5.66913 | -43.72515 | 2025-07-17 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 5c6e30f9-f145-38b3-baab-bcc87288cb47 | -3.3819 | -47.46727 | 2025-07-17 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ba921bbf-b726-31fc-b58a-630e3970be34 | -6.73028 | -44.32354 | 2025-07-17 00:26:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 151c7294-3c14-3fa3-b25b-8c387a3d1fbc | -3.38438 | -47.48542 | 2025-07-17 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 8489935b-94e1-3cbc-9582-f8974e03c657 | -2.91855 | -48.24597 | 2025-07-17 00:26:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 37577f23-ca21-3c1b-8845-dccee2a4286a | -6.8491 | -44.77528 | 2025-07-17 00:26:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 16c132f9-7020-3c73-8c2a-800f07c0ce6d | -5.52607 | -43.88069 | 2025-07-17 00:26:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 4e534396-011f-3d72-89ce-f75ed8e70469 | -4.30615 | -48.10254 | 2025-07-17 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 129e8fbc-1048-3852-8725-852d7178a79a | -3.39584 | -47.50235 | 2025-07-17 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 63879c83-293c-37c8-8b97-1dc64b7433b0 | -5.65971 | -43.72647 | 2025-07-17 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 89f1c634-86d2-35d3-9e14-894151a0c832 | -3.84458 | -47.75278 | 2025-07-17 00:26:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| b081d781-c264-37d4-b95f-05cf579b590c | -4.59816 | -43.31758 | 2025-07-17 00:26:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e83ed4af-0973-35da-83b4-5480f35b0e5a | -6.72255 | -44.33422 | 2025-07-17 00:26:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 99ef0895-d1b0-3c36-aada-9f630dc32d54 | -2.90805 | -48.23773 | 2025-07-17 00:26:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 901a4031-7b31-303f-ada3-fbd69b5fede8 | -5.65683 | -43.70623 | 2025-07-17 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 8e9fd129-2a53-34cc-b2e1-0c1f5418e174 | -6.30183 | -46.33575 | 2025-07-17 00:26:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f73baa91-bdd3-30c4-999d-2a65425a39da | -6.73295 | -44.34225 | 2025-07-17 00:26:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 2e6325c5-5de3-3f17-81db-338d9ec3e314 | -3.3921 | -47.47509 | 2025-07-17 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ed42caf6-fcbe-3fc7-92d2-18c58bac36e0 | -6.8855 | -47.23777 | 2025-07-17 00:26:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ede09070-5e40-3e30-a3eb-8ad29b9132ff | -4.45621 | -48.99608 | 2025-07-17 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 79ee1b3b-5d55-32c3-950a-7c4c592b39db | -6.33632 | -43.74854 | 2025-07-17 00:26:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6ea35330-6862-315c-a4b9-d8541c43a147 | -5.7957 | -45.08304 | 2025-07-17 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 28226c35-4977-30c0-82dc-272e1d2bf9fb | -2.90937 | -48.24725 | 2025-07-17 00:26:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 3ef53b27-51cc-3288-a0f1-9424a52b5c8f | -5.91165 | -45.57924 | 2025-07-17 00:26:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5ecef56e-ab6e-30aa-83ab-163e91550c93 | -3.40481 | -47.50112 | 2025-07-17 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| c07c92fb-c927-3382-9a22-762a7a3999c1 | -5.53681 | -43.88931 | 2025-07-17 00:26:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a021e42e-217c-38de-a01f-919f59e24db6 | -2.47949 | -47.207 | 2025-07-17 00:26:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ed60bff-5a3c-37b6-b006-e4765bf9baed | -6.72121 | -44.32485 | 2025-07-17 00:26:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 503f3ddb-9630-39e2-bb44-38212c9e190f | -2.44215 | -47.33002 | 2025-07-17 00:26:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 6c4bff94-f88a-34cc-9c99-6dece8936412 | -5.78804 | -45.09332 | 2025-07-17 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 8ee7e530-6af5-37bf-adfc-bfd6bb9f6b1c | -6.3107 | -46.33448 | 2025-07-17 00:26:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| fe1adcb8-db53-35fc-8e63-ce728ed0c85e | -5.79821 | -45.10101 | 2025-07-17 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 1dfcc604-b220-3b67-9d55-dba41a81a60b | -3.38562 | -47.49451 | 2025-07-17 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d2842681-d79f-3e1a-9452-f734486aaca1 | -5.79695 | -45.09203 | 2025-07-17 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 58a5e40c-5f94-3a0c-93a8-a6e78a949115 | -3.02431 | -49.43433 | 2025-07-17 00:26:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6ec68976-5f5e-3d90-9023-cbaa49970c61 | -6.71215 | -44.3262 | 2025-07-17 00:26:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| d6d1ac99-33be-37ec-a06a-0194b7af12e0 | -5.59099 | -45.79354 | 2025-07-17 00:26:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b44fe7dd-5549-3af8-8a81-e5465ded64c6 | -7.09242 | -49.16824 | 2025-07-17 00:26:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 88a47c5a-b596-3c47-a72c-aa338c8a270f | -3.02282 | -49.42338 | 2025-07-17 00:26:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ee17c52b-aa3c-38d7-81d3-eb3a353b56e0 | -6.71349 | -44.33553 | 2025-07-17 00:26:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| abf35ef2-ed53-3c69-bbbc-74feb200fd51 | -6.63788 | -49.74736 | 2025-07-17 00:26:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 01551fab-ee23-3787-9501-857ce59d8631 | -7.15412 | -46.09991 | 2025-07-17 00:26:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9a88eca1-8b0b-363d-825b-209a5854af38 | -5.52746 | -43.89062 | 2025-07-17 00:26:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 3d5f5850-b988-3da0-86ed-e5e54acd49a9 | -4.80121 | -43.2252 | 2025-07-17 00:26:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0c046c49-4a05-39a4-9e18-3c8e2619a72f | -2.91722 | -48.23643 | 2025-07-17 00:26:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e65ebc11-9d33-326b-8333-53d7fba9d608 | -7.09504 | -49.17381 | 2025-07-17 00:26:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 24.7 |


[Clique aqui para ver as próximas entradas](README6.md)
