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
| 87e94a96-4cd6-30c5-a86b-6022f13ebb93 | -9.2624 | -57.5228 | 2025-06-21 01:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| f0931788-172b-37ae-a99b-1f6fa7e30622 | -4.5614 | -48.0141 | 2025-06-21 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| c01d1737-14ec-3a28-a911-24739b156275 | -4.5244 | -47.9943 | 2025-06-21 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 0aa2e91e-1bba-3245-8082-411e7f975973 | -3.9671 | -48.1283 | 2025-06-21 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 655010ae-a6e5-307a-af50-844e4b1017b1 | -11.7791 | -57.2445 | 2025-06-21 01:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| b29114f0-9c14-3456-bae1-74f7d2b12cdf | -11.8663 | -54.6739 | 2025-06-21 01:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 249.9 |
| 0d78a1b4-6a26-3a06-8d82-673910e2b336 | -11.9518 | -58.7574 | 2025-06-21 01:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 188ed921-0641-3823-840a-d31ba0960cec | -4.5429 | -48.0151 | 2025-06-21 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 350.7 |
| a738c09e-7b3e-31a0-bafc-396af02533c9 | -7.2219 | -43.0682 | 2025-06-21 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.7 |
| 7cdd4ce8-2b9f-3056-b25c-94fbbfe1fd07 | -8.0152 | -47.6656 | 2025-06-21 01:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 2d2ae2c3-5874-3671-8ad5-8676b001d397 | -11.7983 | -57.2231 | 2025-06-21 01:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 6dd551a2-95fa-3bf2-9acc-55a620ec7d58 | -4.5243 | -48.016 | 2025-06-21 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 167.0 |
| 5e87d037-8b46-37fd-b3b9-0f706cf157bb | -9.4835 | -57.8438 | 2025-06-21 01:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f89d43b9-cac6-36ec-939d-21847bb0fad7 | -11.798 | -57.243 | 2025-06-21 01:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 140.6 |
| be074c05-39ff-31f1-8573-f108251f1266 | -9.4648 | -57.8449 | 2025-06-21 01:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 76b2798b-4a0c-3e34-96d4-500b43245dd9 | -7.2219 | -43.0682 | 2025-06-21 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.4 |
| 851ded5e-4686-3269-a192-6b2afa01e9cf | -13.2343 | -49.8475 | 2025-06-21 01:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| aff97dda-1fcf-36d0-92f8-5e5ae0a153f1 | -4.5429 | -48.0151 | 2025-06-21 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 337.8 |
| c0608f6b-e348-34c7-b9d2-522e4b877f51 | -11.9518 | -58.7574 | 2025-06-21 01:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 4917ad01-ce09-3e06-8271-60ca00310229 | -4.5244 | -47.9943 | 2025-06-21 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| b915bebd-0a2a-340a-a14c-8d5e3a0c4ca9 | -11.8853 | -54.6722 | 2025-06-21 01:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 326.3 |
| 31c7dad0-1c65-3cf1-85f9-24a09d9ef7bb | -11.8666 | -54.6535 | 2025-06-21 01:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b9bf3d9d-b36d-39d1-b126-da4742d075c0 | -4.5614 | -48.0141 | 2025-06-21 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 93e0b15a-6447-3c1f-b9b3-bc10b8c594dc | -11.7791 | -57.2445 | 2025-06-21 01:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| c5bb7616-14b4-3776-8734-f21e22659e23 | -8.0152 | -47.6656 | 2025-06-21 01:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 006b2d96-e30c-38dc-a772-1cdfcdcab9c0 | -21.6835 | -49.5075 | 2025-06-21 01:40:00 | GOES-19 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.3 |
| 6c8577d8-183c-392e-b1b0-131f1929ed5c | -11.8663 | -54.6739 | 2025-06-21 01:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 201.0 |
| b5eb9ccf-5677-35d9-a3ab-7bca3c8b0c72 | -9.2624 | -57.5228 | 2025-06-21 01:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 4ac3ebca-2ed9-3a4c-a40c-508b9354243f | -11.8855 | -54.6517 | 2025-06-21 01:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 2196e0c2-3723-3ea4-8219-7ebacbcdd283 | -4.5243 | -48.016 | 2025-06-21 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 164.5 |
| a45ac7e2-cd7c-3d8f-9caa-dcc70f9bf490 | -9.4837 | -57.8241 | 2025-06-21 01:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 5842fa6a-8555-3afd-aeb8-dd7650e3f22a | -4.543 | -47.9934 | 2025-06-21 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| a81ac8ea-edd0-35d7-8ae8-415708796208 | -9.2624 | -57.5228 | 2025-06-21 01:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 4395fe23-1c07-3f4b-85ef-e999804c868d | -7.2219 | -43.0682 | 2025-06-21 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| bc1b45b2-fbfd-3ad6-8dc8-bed86e59f24c | -4.5244 | -47.9943 | 2025-06-21 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c525dbe9-34d7-3cb7-b6fa-b8b9932b18ae | -11.8666 | -54.6535 | 2025-06-21 01:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| e4d6fde5-bf8f-333d-9ee8-479af050868e | -13.2343 | -49.8475 | 2025-06-21 01:50:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 59941059-4f36-3c01-abd9-dc16f5132395 | -11.8853 | -54.6722 | 2025-06-21 01:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 214.2 |
| 56a00303-2249-3b48-993e-6b0bf82a191f | -4.543 | -47.9934 | 2025-06-21 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 1f5845d7-3257-3242-b928-ff51b874dac0 | -21.6835 | -49.5075 | 2025-06-21 01:50:00 | GOES-19 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.3 |
| 4ecd9a7e-d2f3-3842-ae84-c24111a7d728 | -11.7791 | -57.2445 | 2025-06-21 01:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 864c7c5f-a71c-3ae0-b2af-3e8519cd7c68 | -4.5243 | -48.016 | 2025-06-21 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 0041f5d3-7d35-350d-b2ea-0b05f380c9a1 | -9.4648 | -57.8449 | 2025-06-21 01:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| d339ac47-e567-3564-ad8a-e5ce94ca767b | -12.4767 | -54.4302 | 2025-06-21 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 685822bd-deea-310f-9d34-8ff96f384581 | -4.5429 | -48.0151 | 2025-06-21 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 145.5 |
| b64cc538-4b7d-3e65-b99d-4d4e75bbf9f3 | -11.798 | -57.243 | 2025-06-21 01:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 154.7 |
| 5fe5af72-dbcd-340d-bdb3-daadb149c2b6 | -11.8855 | -54.6517 | 2025-06-21 01:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 4fd8f61b-9dff-37dc-a26f-4ee4a504114e | -11.7983 | -57.2231 | 2025-06-21 01:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e8ad49e9-a739-3ee6-84bc-8f028e3b1ee1 | -11.8663 | -54.6739 | 2025-06-21 01:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 202.0 |
| eb3248b6-9ac9-3eb8-9e01-974206f3dd2e | -4.5427 | -48.0367 | 2025-06-21 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 87ee2c6b-e4f3-319d-af8d-1f1e7e8aa00a | -9.4835 | -57.8438 | 2025-06-21 02:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 1aa3536a-c4eb-35e1-bf39-bff0b890451f | -4.5614 | -48.0141 | 2025-06-21 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 5083e8dc-c792-3e73-8632-b8c27e619f79 | -4.5243 | -48.016 | 2025-06-21 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 158.1 |
| d28e2ba6-1b3c-3b4b-91e1-6ff7367c5db1 | -11.8853 | -54.6722 | 2025-06-21 02:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 258.0 |
| 47b1a2c0-cb56-33a0-9139-40227564be34 | -7.2219 | -43.0682 | 2025-06-21 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| c34eed22-be5e-3b0c-b14f-6fd12a378653 | -12.4767 | -54.4302 | 2025-06-21 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| de60bca7-0e73-3479-8134-8c23dbb9b734 | -11.8663 | -54.6739 | 2025-06-21 02:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 163.3 |
| 3ae2536f-dfd4-32a1-92b8-56689b7d0ce1 | -4.543 | -47.9934 | 2025-06-21 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 50659be9-49de-3952-b7b8-dcfa9e40bb66 | -11.7791 | -57.2445 | 2025-06-21 02:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 4e407b78-5c1f-3edc-969c-89e76ac979e8 | -9.2624 | -57.5228 | 2025-06-21 02:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 27ad9b06-29ec-373e-8bd4-fff4b1b98e85 | -11.7983 | -57.2231 | 2025-06-21 02:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 507a5b2a-df12-3372-8a9d-31c0fffd18ca | -4.5429 | -48.0151 | 2025-06-21 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 325.6 |
| df62b5b1-1654-38ef-ac26-c1c9274eb0e4 | -12.477 | -54.4096 | 2025-06-21 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 655027bc-c9d1-3514-89d0-e3e5214bd082 | -4.5244 | -47.9943 | 2025-06-21 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 1bc19ed5-ed68-356c-99c6-f507ab809945 | -9.4648 | -57.8449 | 2025-06-21 02:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 9e9ada91-50a3-3eb8-abae-f3a483f83061 | -11.798 | -57.243 | 2025-06-21 02:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 130.4 |
| c547bf82-1c4b-32b4-8edf-e0723b37004c | -11.8855 | -54.6517 | 2025-06-21 02:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 39a8948a-5c5b-32d8-b8cb-501a33752473 | -21.6835 | -49.5075 | 2025-06-21 02:00:00 | GOES-19 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.1 |
| 8f2b3048-8a0c-39ee-9ee6-c8cd71c062b7 | -11.8666 | -54.6535 | 2025-06-21 02:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 78fb3992-2909-3ff0-8e36-baeaac247023 | -3.9671 | -48.1283 | 2025-06-21 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| c32ce05d-a128-395d-9de8-fa7c150ec18c | -11.885 | -54.6926 | 2025-06-21 02:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 130be279-8559-39d5-9ce2-4e3bc0bbd41b | -4.5429 | -48.0151 | 2025-06-21 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 355.3 |
| 013780f6-4ba9-3a45-ae41-48740d40e138 | -3.9671 | -48.1283 | 2025-06-21 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| c860e2a8-1720-3a4d-b3b8-f193aeb25f8c | -21.6835 | -49.5075 | 2025-06-21 02:10:00 | GOES-19 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.5 |
| 97b5ae18-f0ff-357c-a206-c6cfc773e045 | -10.4564 | -47.0347 | 2025-06-21 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 9fe02c16-09d5-31c7-b84d-4ecc78bbda52 | -9.4648 | -57.8449 | 2025-06-21 02:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| d58cbb8b-02e4-3ea6-89a1-bc567e18180c | -4.5244 | -47.9943 | 2025-06-21 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 43e9d3ff-f553-314c-98e4-4c070f4dc572 | -11.798 | -57.243 | 2025-06-21 02:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 7df960c3-ec03-3f1a-a12f-0c0894e955d7 | -11.8663 | -54.6739 | 2025-06-21 02:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 92f0e431-e105-3374-aa74-034b0734ffa4 | -7.2219 | -43.0682 | 2025-06-21 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| f2a8c87f-51e0-3f3a-9b8c-e95de146ae18 | -12.4767 | -54.4302 | 2025-06-21 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 39925d11-a323-3efa-9781-63ee6d9b9bc7 | -11.8853 | -54.6722 | 2025-06-21 02:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 272.8 |
| 615e476f-a2cd-3370-9766-fa68cd0a7389 | -11.885 | -54.6926 | 2025-06-21 02:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| ae2a7f79-80ad-3350-8e11-5d071c5f280c | -12.477 | -54.4096 | 2025-06-21 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 101.0 |
| afd104fd-7900-3f19-a6cd-7aea9fc7c6c2 | -4.543 | -47.9934 | 2025-06-21 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 59126600-8f38-32a1-b9c5-c0c3dff38c1b | -9.2624 | -57.5228 | 2025-06-21 02:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 2911462f-3d14-38f9-8839-b7272048f201 | -11.7791 | -57.2445 | 2025-06-21 02:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 11df193a-ad92-3442-a8ce-f22e427960a5 | -11.8855 | -54.6517 | 2025-06-21 02:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| ad9dbbb9-06fa-3488-91df-0ee1b8a5bb14 | -4.5243 | -48.016 | 2025-06-21 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 5ae779ea-d5fc-35df-a0d7-0fe45c9b737f | -3.9671 | -48.1283 | 2025-06-21 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| cfde4a57-915f-3f78-9131-8ca907590281 | -4.543 | -47.9934 | 2025-06-21 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| bc0f25b8-170a-3714-9505-497e19e723b4 | -11.8666 | -54.6535 | 2025-06-21 02:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| e667d98a-041b-3290-b430-98df52389ff3 | -10.456 | -47.0571 | 2025-06-21 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 2828149f-ee9d-3ad2-aae8-ef5c2e75e54d | -4.5429 | -48.0151 | 2025-06-21 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 280.1 |
| 6dca2c9f-4de5-3098-ad27-062c90f9fdff | -9.4648 | -57.8449 | 2025-06-21 02:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| b1ecdc1e-1dfe-3efc-be05-e7b5a6fc8f79 | -11.8663 | -54.6739 | 2025-06-21 02:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 175.7 |
| 21a60e17-a574-3e24-ba5e-f24039d42c0f | -7.2219 | -43.0682 | 2025-06-21 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 854b2dba-0e39-3e40-8f9d-c43c420e070e | -4.5614 | -48.0141 | 2025-06-21 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 4bfbfb0f-0be6-3f69-af38-4e1ecc0e8716 | -12.4958 | -54.4283 | 2025-06-21 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 30bd6aaf-6b39-381b-93fb-f21f4af6acb5 | -4.5243 | -48.016 | 2025-06-21 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |


[Clique aqui para ver as próximas entradas](README6.md)
