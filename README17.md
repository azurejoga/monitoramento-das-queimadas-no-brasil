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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9253b00-46eb-375b-8c44-4874e3a558dd | -5.6242 | -45.7308 | 2025-08-27 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0dc9db4f-5481-35d1-a21d-8ff9ac8822e9 | -6.80057 | -44.3506 | 2025-08-27 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74df9a65-d379-3e4e-bd8b-ed4c981cc8e8 | -6.12686 | -42.94719 | 2025-08-27 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 96d51391-85a4-3159-8329-518017462233 | -5.66441 | -47.49317 | 2025-08-27 03:36:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e024a0b2-40de-39bf-bb5f-9fbf23076143 | -6.18662 | -43.01484 | 2025-08-27 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1790ffaf-0eff-382a-81d0-c6be1a6cda04 | -6.18778 | -43.00819 | 2025-08-27 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 295e76ad-be41-366c-86c5-e21a385cd1e7 | -6.12857 | -42.94892 | 2025-08-27 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |
| d7fc5919-cde2-31af-a3a5-f6422e948641 | -7.0799 | -43.64942 | 2025-08-27 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b584dc45-d093-395c-803e-675efbf96065 | -5.53457 | -36.84731 | 2025-08-27 03:36:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f73b5b61-91f7-339a-b90d-87f005692815 | -7.59857 | -43.95276 | 2025-08-27 03:36:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ce37dfd-c096-33c5-8990-1c99687f0db2 | -7.17445 | -43.8472 | 2025-08-27 03:36:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36ed80cd-239a-3459-8fe9-c77175bd6cbc | -7.65998 | -42.65527 | 2025-08-27 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e3b2034c-a972-3fa5-9091-05dffa90c10b | -7.12296 | -43.69432 | 2025-08-27 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e0c6c568-1e04-3b26-8585-bd71b2e67dd9 | -7.43806 | -42.04174 | 2025-08-27 03:36:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ffe56e2c-b118-3002-ac5b-191aa2b0e1b4 | -7.64395 | -42.6862 | 2025-08-27 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 19ba88b2-fe9e-375d-882b-499fdcc798f1 | -6.12626 | -42.95055 | 2025-08-27 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 9951863b-653e-3e71-85eb-6a770e787e2c | -6.1863 | -44.17297 | 2025-08-27 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ae5172df-d8f6-3af0-ae45-41cef5f79735 | -6.90445 | -43.13631 | 2025-08-27 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68c69ced-3a9a-3d23-956b-d05fc95f3ce4 | -7.65962 | -40.15692 | 2025-08-27 03:36:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b1f86163-a0b6-309c-99c3-7dc5e3da4092 | -5.69069 | -40.98138 | 2025-08-27 03:36:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d3160c57-8494-3cae-bf77-588c9ec6b73d | -4.84644 | -42.89022 | 2025-08-27 03:36:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d167d48-4428-303a-adbd-bd1b881237cf | -5.09856 | -43.79365 | 2025-08-27 03:36:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9358f964-1e46-3fc8-9934-73c09d0c2a05 | -5.86157 | -42.92611 | 2025-08-27 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8a818030-a553-3d7a-b859-ec2751b7c755 | -7.70481 | -45.76705 | 2025-08-27 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 088692ef-b2a4-3814-9ac6-b73bafa5908c | -7.70294 | -45.77695 | 2025-08-27 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c7a05e49-af5a-3b24-91a2-99bb57a985e6 | -6.8985 | -43.13878 | 2025-08-27 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3520439-2908-3c7b-83fa-64df8a9f838c | -4.85188 | -42.89114 | 2025-08-27 03:36:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae0fd3a8-b678-338f-9441-9c47aa82a1b7 | -6.80966 | -44.99642 | 2025-08-27 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d92f30c-9732-35a5-8469-f44e45dda933 | -4.88199 | -37.4826 | 2025-08-27 03:36:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f0f61dc5-5f49-399d-82a7-2d22b86f6add | -5.66134 | -47.48897 | 2025-08-27 03:36:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 071d673e-9368-319f-9e34-7e4d07e3e83d | -6.75701 | -35.14043 | 2025-08-27 03:36:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| cc5fcd50-bbfd-32be-a573-93290ea9b404 | -6.13332 | -42.95333 | 2025-08-27 03:36:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| fe4a4051-8aa0-3a0c-928b-5baa561b69f3 | -7.26283 | -45.3566 | 2025-08-27 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6887857f-ca69-3e87-9a57-ed82c47fd0c1 | -6.46154 | -44.57402 | 2025-08-27 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f9b722a2-83ff-3c7f-9331-823ec0f6fb30 | -6.96014 | -44.09499 | 2025-08-27 03:36:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26cb341c-ae11-3194-957f-903a41b5f369 | -7.59295 | -43.95206 | 2025-08-27 03:36:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bc656a1-2435-31aa-9a49-6ca89c90f902 | -7.64713 | -42.6683 | 2025-08-27 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8ba3f547-b695-303b-bf40-0c2bd63ead9b | -5.50949 | -36.68019 | 2025-08-27 03:36:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 616e7c8b-f795-3b88-bcc2-dcaf73478b22 | -6.83855 | -39.40855 | 2025-08-27 03:36:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3bacab91-dfb2-3acf-8756-a05eb07cc276 | -6.16369 | -42.61845 | 2025-08-27 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 122c86c0-008b-37cb-abbe-a10b8e716bf4 | -7.70388 | -45.77197 | 2025-08-27 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6be9a25c-2fd4-3627-b294-9fda72d8c996 | -5.69155 | -40.97629 | 2025-08-27 03:36:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 263a3901-eac5-3937-884d-1370d31b2884 | -7.6466 | -42.67128 | 2025-08-27 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 38e6e7f0-86f9-3c60-9a1d-0910fff4a37d | -7.17583 | -43.84755 | 2025-08-27 03:36:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10b8c103-d4ef-33e9-9163-a4015d1e0051 | -4.85063 | -42.88932 | 2025-08-27 03:36:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67ecf741-e40f-303f-8e84-22f41c101203 | -4.4992 | -46.37796 | 2025-08-27 03:36:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 48e1b96c-5d46-3407-b651-2f4f8611b63c | -7.65384 | -42.66022 | 2025-08-27 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 56e774e9-08fe-3901-b816-e37bce4f63db | -6.13099 | -42.95489 | 2025-08-27 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| b79cd2d7-e587-3a37-97e3-45f6f11741c7 | -5.95325 | -42.49307 | 2025-08-27 03:36:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b88ad624-d340-3dad-b590-382f9d083d58 | -7.16837 | -43.85729 | 2025-08-27 03:36:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a94c1a1-68e3-31fe-8fd4-eb9dd765d93d | -4.88122 | -37.48722 | 2025-08-27 03:36:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b1936486-370b-3d18-956d-1e995de138a6 | -7.71015 | -45.7729 | 2025-08-27 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b5c5301b-1045-3900-bc76-228d97a0f3aa | -7.65278 | -42.66618 | 2025-08-27 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cd59c057-b3dc-3e1f-9ebc-7ada86386220 | -7.16263 | -43.50526 | 2025-08-27 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 77f0ddd1-c1e1-3438-bb3c-dee965adf906 | -6.80882 | -45.00105 | 2025-08-27 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9f997aa-f0e1-3118-8701-39a02d33910c | -7.14891 | -44.14671 | 2025-08-27 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9670e5a1-40f0-3ba3-926e-8c3d5fc25cff | -5.94748 | -42.49546 | 2025-08-27 03:36:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3137ede5-55e3-34b1-86d9-2ad641e0965b | -7.65946 | -42.65819 | 2025-08-27 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f92d870b-024e-3240-a605-858b2bcaad51 | -7.65894 | -42.66113 | 2025-08-27 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6e1388f0-1585-3ae0-9f81-337fdcd4d3f4 | -6.76037 | -35.14097 | 2025-08-27 03:36:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 3fe4990b-5e63-3888-9c22-2d851e2a696d | -7.64608 | -42.67425 | 2025-08-27 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| aeceb137-f4f5-339a-97c0-cd47f5dbc952 | -5.50723 | -36.6713 | 2025-08-27 03:36:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c7e02ac1-b39c-3dce-8798-758f224fed6d | -7.1709 | -43.84286 | 2025-08-27 03:36:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f431cc2-8dda-323a-99be-f7b1e8ccce3f | -6.37985 | -44.96094 | 2025-08-27 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cce1611f-21c8-35da-8925-1045d2a2f301 | -5.62657 | -45.72475 | 2025-08-27 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7093786-f4cc-31a9-a695-1fe49b3aa9fb | -7.383 | -47.04555 | 2025-08-27 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58b72907-373c-325e-8f7b-a7d6c3dc19f3 | -7.12361 | -43.69067 | 2025-08-27 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b16c0f7e-5291-312a-a0e5-feb5a4790552 | -6.96516 | -44.09971 | 2025-08-27 03:36:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75589a2d-b3f7-3660-a0c8-b5cd0ee1b05b | -7.16954 | -43.84262 | 2025-08-27 03:36:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5610431f-49b2-3fe3-adb3-8f27656fc7f8 | -7.63883 | -42.68535 | 2025-08-27 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b6850bdb-847e-33b3-9e1f-c0a8fe5d36fc | -6.49445 | -44.68363 | 2025-08-27 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c3b01733-05c3-3b2b-89ce-41ad95193c6a | -4.87796 | -37.4841 | 2025-08-27 03:36:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9224b994-c49a-3c49-ba7b-b07cc794e124 | -7.16327 | -43.50166 | 2025-08-27 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 195fce7a-e82d-38b9-a894-a52c171d8d79 | -3.97947 | -43.24662 | 2025-08-27 03:36:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b012f24b-afb1-3e45-8943-b5cddc5a9d67 | -5.86521 | -42.90533 | 2025-08-27 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 55084f05-90f6-3b62-ac02-077ac19ac441 | -7.08542 | -43.65034 | 2025-08-27 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb30c675-2836-3625-bc3a-61f82fd0e580 | -6.84039 | -42.82768 | 2025-08-27 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 03a0b02f-fb05-3190-aabb-9ea41721e8ef | -6.87594 | -44.39636 | 2025-08-27 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1a9e9c5-cb20-370e-9237-fe334e1400b1 | -5.63397 | -45.72055 | 2025-08-27 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90f9394f-0977-3c1d-8ce5-f4a5201e649e | -6.57755 | -47.38641 | 2025-08-27 03:36:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 10b908d0-1ec4-302b-a689-15021effecc9 | -5.7844 | -42.59523 | 2025-08-27 03:36:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| cca7ec43-c15f-39ef-a189-f9c126306756 | -5.62514 | -45.72554 | 2025-08-27 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a49a5ff5-a1bc-3cfd-af03-9e78b9566986 | -6.96447 | -44.10357 | 2025-08-27 03:36:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f05c2a5-68a3-33eb-a0b1-c13afbdf9a43 | -6.79482 | -44.34933 | 2025-08-27 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8ee0a10-f75a-3433-a7b8-b7de685786b4 | -6.57059 | -47.38503 | 2025-08-27 03:36:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d964e033-4fa9-357e-b81f-ae63ac24ca42 | -4.50028 | -46.37194 | 2025-08-27 03:36:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b51d9bd4-4580-3d7e-a705-799a8d445b9b | -6.12799 | -42.95228 | 2025-08-27 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 1d97022e-1f9b-38a1-9cba-ab1568bdbee1 | -5.87597 | -42.93859 | 2025-08-27 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 15fcfe82-e261-3acc-ac88-e34d7de15920 | -6.19286 | -44.16964 | 2025-08-27 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 153b8b35-3574-3b7c-b7e7-6e1ef5fca699 | -5.78497 | -42.59196 | 2025-08-27 03:36:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e5e99fda-5048-3667-8866-db36368d70e0 | -5.95269 | -42.4963 | 2025-08-27 03:36:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1027e4c3-760d-3e7f-b031-44277081d326 | -7.64555 | -42.67722 | 2025-08-27 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fac4fd54-109d-371f-9b5f-b877aac0d06d | -7.64676 | -39.01957 | 2025-08-27 03:36:00 | NOAA-21 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e9fe0920-b1eb-314c-a7fc-2ddc21ae518a | -7.17025 | -43.84661 | 2025-08-27 03:36:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 331d3170-df85-3f7f-b640-2c5514ae3574 | -7.4779 | -46.00477 | 2025-08-27 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0a4f8cd-b56b-30bd-838e-bbfbe2210194 | -6.43813 | -44.60251 | 2025-08-27 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ef1f627-7f1e-3fa1-b733-ec6c8e2a45ea | -7.70921 | -45.7779 | 2025-08-27 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7ec25015-05be-321f-b6e0-5587e5860a35 | -5.78555 | -42.58868 | 2025-08-27 03:36:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5b10669d-07c5-3dbb-9071-406dc0936d2d | -6.7803 | -44.29782 | 2025-08-27 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85b7d082-3e1a-31e5-b7a7-95f49ac3c59c | -6.18702 | -44.16894 | 2025-08-27 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README18.md)
