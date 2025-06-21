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
| 6a0bcff0-3ec5-3176-8928-737ce80d7575 | -11.885 | -54.6926 | 2025-06-21 00:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 3009f765-6867-3a40-99ed-73fa2bb645c7 | -9.465 | -57.8252 | 2025-06-21 00:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| d04f61a5-2f57-33d6-b1d7-a079f935bb8b | -4.5427 | -48.0367 | 2025-06-21 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 4ffa8eea-df2d-3be4-865b-662872180c28 | -13.2535 | -49.845 | 2025-06-21 00:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 5a94ed76-1f4c-3435-b875-e102a10e4fb5 | -3.6366 | -47.5127 | 2025-06-21 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 3899c643-b7e8-393b-9b16-dba9f60edbe6 | -11.8855 | -54.6517 | 2025-06-21 00:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 218.3 |
| 0304205a-be48-37b5-957b-35836573fe75 | -13.2343 | -49.8475 | 2025-06-21 00:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 512c4e02-9778-3b50-b655-8b164b333beb | -3.967 | -48.15 | 2025-06-21 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 55078968-f944-3c32-982a-558bdcde8cfe | -4.5243 | -48.016 | 2025-06-21 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| d4d7fcfe-9494-3790-868e-a2802fe29a50 | -7.2219 | -43.0682 | 2025-06-21 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 264.3 |
| ddca097c-605c-3918-bec9-65f006fc2043 | -7.2222 | -43.0447 | 2025-06-21 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 7171ce48-2b79-39d8-9bbc-3fdf18499315 | -3.9671 | -48.1283 | 2025-06-21 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 183.4 |
| a0da752a-c745-3a64-b109-c3abd921a9c6 | -4.5614 | -48.0141 | 2025-06-21 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 96f14d72-f9cb-3e08-9c6c-c2e4720402a9 | -12.2727 | -44.5967 | 2025-06-21 00:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 7c4faf57-012f-3381-b414-ea6d3709dee0 | -4.5244 | -47.9943 | 2025-06-21 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 996fee73-086c-347c-b727-7794e5e71f90 | -8.0152 | -47.6656 | 2025-06-21 00:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| b7757783-fb75-3a28-8abd-e5de5a5d471b | -13.2346 | -49.8258 | 2025-06-21 00:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| c429cfd8-26fa-3e40-8421-825388beb84f | -9.2624 | -57.5228 | 2025-06-21 00:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 57b5e4f5-5405-3208-805b-9005e4f0555e | -8.034 | -47.6639 | 2025-06-21 00:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 26dd5737-2bfc-3e34-8c18-4089888e39ae | -11.7983 | -57.2231 | 2025-06-21 00:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 141bfffd-347c-32f7-92f1-26af958cc91a | -3.9486 | -48.1291 | 2025-06-21 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 3a720c5d-1fdd-3199-b563-8996ba319251 | -8.0154 | -47.6437 | 2025-06-21 00:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| b770d508-d0e0-32d3-a52e-02cfb9fe829a | -11.9518 | -58.7574 | 2025-06-21 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c8dc1c83-3194-3b4a-86f5-0425ac06037c | -11.798 | -57.243 | 2025-06-21 00:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 142.1 |
| 5109586b-589e-3149-8d55-8da22c2b3c54 | -3.9671 | -48.1283 | 2025-06-21 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 147.2 |
| 98b93dbf-6e66-3e8c-a73a-9bf8ccec9d68 | -7.2222 | -43.0447 | 2025-06-21 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.6 |
| efaa1e91-27b9-33ce-b56f-79be36365717 | -9.4648 | -57.8449 | 2025-06-21 00:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 2d310385-4b6e-3b62-accc-3b7ab9742b4d | -8.0152 | -47.6656 | 2025-06-21 00:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| fc59bfb4-7b22-33ee-ba97-c24985990860 | -7.2219 | -43.0682 | 2025-06-21 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 232.2 |
| 6e83dab8-90c6-3d58-960c-f784f5d72eec | -9.2624 | -57.5228 | 2025-06-21 00:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| c3efb167-0d3b-3eba-a103-9dcd36c8c996 | -11.8663 | -54.6739 | 2025-06-21 00:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 284.5 |
| 84525ff8-4c3a-32ba-99c2-cfdc5cd1b8ff | -9.465 | -57.8252 | 2025-06-21 00:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| fa15f9a8-3f82-3fd1-bd36-7cab13aaf8b8 | -11.7983 | -57.2231 | 2025-06-21 00:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| adc49278-45c0-3011-9ffb-a414765446b5 | -4.5429 | -48.0151 | 2025-06-21 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 179.2 |
| 3892d8cf-6b18-3c33-9bb6-e3322e6558a3 | -9.4837 | -57.8241 | 2025-06-21 00:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| c95a893a-1a9c-38b5-b868-3efce2dcbfc9 | -10.883 | -56.4567 | 2025-06-21 00:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 62852fb3-4302-3689-8c3a-864b0851f87a | -7.2408 | -43.0664 | 2025-06-21 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| e5a79a85-b5ed-3210-96b6-1e90f1592fb1 | -13.2346 | -49.8258 | 2025-06-21 00:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| a4d5604c-bcc5-3c6c-b771-b53173d5718e | -4.543 | -47.9934 | 2025-06-21 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 70ad8326-8c2e-3bbb-ad60-c230bdf98efb | -11.8666 | -54.6535 | 2025-06-21 00:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 4ed410c5-a311-3112-93c0-376617ad6af7 | -11.8855 | -54.6517 | 2025-06-21 00:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 206.9 |
| c98d58a0-8680-38b5-a142-f0aac1fd6d07 | -9.4835 | -57.8438 | 2025-06-21 00:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 399a60d9-a716-3b31-b430-61c61590caad | -3.967 | -48.15 | 2025-06-21 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 15fcd965-485f-3511-a150-53df32775260 | -11.8853 | -54.6722 | 2025-06-21 00:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 551.0 |
| 8990a002-5e20-3e58-8406-5e73188fa76e | -4.5243 | -48.016 | 2025-06-21 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| fcbda77f-824e-3588-8141-ad8998749466 | -11.7794 | -57.2246 | 2025-06-21 00:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 3fd5a3e3-b373-3959-b982-e7bf2f2beaaa | -11.7791 | -57.2445 | 2025-06-21 00:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 688719e7-4508-37a8-abb8-5068c0d04da9 | -3.9857 | -48.1275 | 2025-06-21 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 32671013-781b-319d-8e70-ba94d243a2d4 | -11.885 | -54.6926 | 2025-06-21 00:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 5d9cbe93-b598-3c0c-b6eb-c63603a73741 | -13.2343 | -49.8475 | 2025-06-21 00:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| abac9ee4-5a0d-386b-9bf6-34a5749da397 | -11.866 | -54.6944 | 2025-06-21 00:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 8bfb17c1-1243-316b-9ca2-6dd03597205f | -9.4648 | -57.8449 | 2025-06-21 00:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 8aee15fe-f2be-3f28-8517-6000fe6c4f16 | -4.5429 | -48.0151 | 2025-06-21 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 189.8 |
| 47268a0c-9287-3060-b297-3f8da63f9898 | -9.465 | -57.8252 | 2025-06-21 00:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 73b3f0af-a1ee-3cd5-a3ba-7f18b8771741 | -4.5243 | -48.016 | 2025-06-21 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| a90140a4-eb47-320f-b073-4be790261a18 | -13.2343 | -49.8475 | 2025-06-21 00:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| f3548dc9-b739-36ef-b47d-6382217858bf | -11.8855 | -54.6517 | 2025-06-21 00:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 223.0 |
| 22bdc3d0-23c3-314e-9bfa-41b49e729b62 | -7.2219 | -43.0682 | 2025-06-21 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 207.0 |
| d380908d-655d-3364-86e6-2a51f65da7d3 | -11.798 | -57.243 | 2025-06-21 00:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 165.2 |
| 5d16bb13-2bb7-3cf2-bd78-5472e94da6e0 | -11.866 | -54.6944 | 2025-06-21 00:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 2ba91236-04d5-3875-9de5-59b15774dc3b | -11.7983 | -57.2231 | 2025-06-21 00:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 7e06e0d4-c92c-34ef-9830-ef69f9b097e7 | -4.5614 | -48.0141 | 2025-06-21 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 13bf97bd-4e5b-3611-ba17-8530bc0ae8a9 | -9.4835 | -57.8438 | 2025-06-21 00:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 1306c8fa-63d5-3d4a-9c75-feb41d3d7761 | -3.967 | -48.15 | 2025-06-21 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| a64254dd-8945-37b3-91f0-bcaf6e66228d | -11.8666 | -54.6535 | 2025-06-21 00:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| cbebfe5b-cc8b-3cd5-a3cb-7cfd84f7b6b5 | -11.9518 | -58.7574 | 2025-06-21 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 535a7e5b-d495-3bb2-8bec-19e0f7910946 | -4.543 | -47.9934 | 2025-06-21 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| b906b072-c045-3940-a073-b45895532624 | -11.7794 | -57.2246 | 2025-06-21 00:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 2d849faf-a586-3ba3-be44-da5b022c7d65 | -4.5244 | -47.9943 | 2025-06-21 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 891ff6ae-d630-3215-b307-f58025fd4d36 | -9.4837 | -57.8241 | 2025-06-21 00:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 347fe6ad-9c4a-3242-97ce-363109995900 | -13.0392 | -53.7107 | 2025-06-21 00:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| f3a6e793-fd3f-3473-af07-964e60eb33d0 | -8.0152 | -47.6656 | 2025-06-21 00:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 050cbb0d-7c8d-35db-9ed8-f559afb0e2b6 | -11.8853 | -54.6722 | 2025-06-21 00:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 503.8 |
| 3ac4c18b-3bca-3421-bd23-d3a38f86d1ae | -7.2408 | -43.0664 | 2025-06-21 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| b2dd142d-c60f-3b79-ad12-51667e3bd535 | -3.6181 | -47.5134 | 2025-06-21 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 6ad8abff-3255-31ac-af93-4514e390d1d2 | -7.2031 | -43.0701 | 2025-06-21 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| e7d0ff51-c548-34bc-9d25-faa0950137e5 | -13.2535 | -49.845 | 2025-06-21 00:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| c867215e-ff50-3746-825d-21eee09394c9 | -11.885 | -54.6926 | 2025-06-21 00:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 65ff517f-6034-3df1-bce6-fe9feda309c6 | -3.9671 | -48.1283 | 2025-06-21 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 165.1 |
| 445e2a97-1da7-3401-aa1c-197796e6da0d | -7.2222 | -43.0447 | 2025-06-21 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 47ac5fc7-7ea3-3aeb-b626-76ce52e90e3e | -5.7871 | -45.9155 | 2025-06-21 00:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| ea77ce2f-1881-3a06-a3fa-d26344f04eda | -5.7873 | -45.8931 | 2025-06-21 00:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| e3572e42-7216-3837-bd7c-292113ddcfa1 | -11.8663 | -54.6739 | 2025-06-21 00:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 253.0 |
| f180f6e8-1608-379b-a7fe-ad057958a93e | -11.7791 | -57.2445 | 2025-06-21 00:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 142.1 |
| c79cbd30-b8eb-353c-87d9-1c4a1a676550 | -9.2624 | -57.5228 | 2025-06-21 00:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 3139528a-6e3a-30aa-9509-8bad2ec239bf | -11.8855 | -54.6517 | 2025-06-21 00:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 36cf66e2-edfa-3edf-9fc2-12d479761369 | -13.2343 | -49.8475 | 2025-06-21 00:50:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 89e83d28-a71d-3a26-8e34-5e1180bfa646 | -3.9671 | -48.1283 | 2025-06-21 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 158.6 |
| f64d706d-aad7-3e73-80fe-b01f9d0542a4 | -9.4837 | -57.8241 | 2025-06-21 00:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 95f2b255-c30e-3204-8147-8fdf6e09e93c | -7.2222 | -43.0447 | 2025-06-21 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 95b6342f-be98-31a9-b21d-c4ba0973aa7f | -5.7871 | -45.9155 | 2025-06-21 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 3fb183f1-be74-3e75-8a06-5acb2ede3048 | -11.8853 | -54.6722 | 2025-06-21 00:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 339.9 |
| b9c4e20f-8c39-33bb-908d-b3206bf3f4ac | -11.7983 | -57.2231 | 2025-06-21 00:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| a86fa479-9ddc-3748-a90d-111b1b7e4189 | -9.465 | -57.8252 | 2025-06-21 00:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 750d4399-6c68-3cb9-a4b9-aef8c77648e4 | -11.9518 | -58.7574 | 2025-06-21 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 371e8fd4-7590-3922-b6c2-d23e9b5b7cd3 | -5.7684 | -45.9168 | 2025-06-21 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| e1d8847f-9256-31ce-81ac-76e4872298e8 | -13.2346 | -49.8258 | 2025-06-21 00:50:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 61514086-c3d1-3d77-99db-b7b20e0803ff | -9.2624 | -57.5228 | 2025-06-21 00:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| bbc3949b-0b79-3317-a18a-f0f5e0dce93e | -8.0152 | -47.6656 | 2025-06-21 00:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 958687d9-a68c-3644-9de7-62c36780d377 | -9.4835 | -57.8438 | 2025-06-21 00:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |


[Clique aqui para ver as próximas entradas](README3.md)
