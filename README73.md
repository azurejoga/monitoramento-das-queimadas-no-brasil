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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f59543c-7a24-3515-9012-7e8869142a44 | -17.9117 | -57.61327 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 1fc357d8-67e7-3946-a346-c8aca1eb54a6 | -23.22266 | -49.41389 | 2025-09-29 05:01:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| a25973fd-ffc2-3bb7-9664-5964b6d7cfea | -17.89731 | -57.61812 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d89dd1a6-c4c7-370e-9b3d-5cb5e1aed180 | -18.97845 | -48.39919 | 2025-09-29 05:01:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e513798-9d6e-3f7c-893c-1629ec5f6c58 | -23.22857 | -49.40557 | 2025-09-29 05:01:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| b083569d-d9d6-3f74-8421-e2acf6207a70 | -21.86536 | -54.02121 | 2025-09-29 05:01:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c46a31b2-1ae4-36cd-8f50-dd36731159e6 | -17.74246 | -46.69491 | 2025-09-29 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 253ad949-45f6-319c-bcbf-91968f57b31f | -17.90899 | -57.60899 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| b885c2f3-9900-3d74-a619-b2f7b9fd6bc8 | -17.73162 | -46.69014 | 2025-09-29 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7eddd0af-11d3-3ec6-877c-7a4a2aa7d46d | -23.22421 | -49.39826 | 2025-09-29 05:01:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8a3c9f6c-bba7-3993-af93-cf4ab8695805 | -18.17083 | -53.32386 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc543047-3aa9-3afe-85b3-881daa25d610 | -16.02411 | -59.49814 | 2025-09-29 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3f6f245-3938-343b-9418-d03f91805e76 | -17.90957 | -57.60533 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 11511486-f715-3a11-ab17-b90baa9c6a89 | -16.84444 | -53.19856 | 2025-09-29 05:01:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87a32ae9-1877-3feb-9b74-bb83c2db0179 | -17.90569 | -57.60837 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6f6d71ad-2ed4-36c2-b87e-6085c93c5236 | -17.72644 | -46.68534 | 2025-09-29 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 346c4d5f-9d24-301c-8e8b-ca8757477917 | -18.1993 | -53.32973 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5be6202d-57ba-37e4-a813-3c34df36e4ec | -17.72603 | -46.68943 | 2025-09-29 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d2405f8-7a67-3eb4-84a6-a18b1c99717e | -17.89791 | -57.61446 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ae97a829-dec3-30b3-a747-ff563a489dbc | -18.19501 | -53.33376 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d7a58a73-3a6b-3cf7-9d79-911c92932c1a | -18.21392 | -53.30487 | 2025-09-29 05:01:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 04e68cf9-15c8-36bb-affa-477fe33d22d0 | -17.90722 | -57.61997 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 07bc73cb-830f-3b28-8ab8-d89c850f3d32 | -22.37105 | -49.96886 | 2025-09-29 05:01:00 | NOAA-21 | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7cbc38c4-c822-3372-b82f-82897462be8e | -16.01205 | -59.50455 | 2025-09-29 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46ce20a7-e0c6-30a7-abe4-ec30c36c5c1a | -17.90662 | -57.62366 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e5595dea-d640-3e97-b17d-ef4821059b7d | -17.71666 | -46.68633 | 2025-09-29 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dff360a7-b5a7-36c9-9f1f-799f46cb05d9 | -16.01913 | -59.50595 | 2025-09-29 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d93744f4-6cd1-348e-b244-7b3e93a81826 | -19.3086 | -48.91628 | 2025-09-29 05:01:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aebbeb3c-492b-37ed-a484-804953a8d52c | -17.71623 | -46.69029 | 2025-09-29 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fdd8441-56ad-32bb-9206-4702dfec0a49 | -20.54462 | -45.10423 | 2025-09-29 05:01:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| beaf836c-c53d-3b8e-8616-b4eea0394243 | -18.18129 | -53.32971 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4a6ae5fa-1efc-3e12-aea1-4bc4bdeaa829 | -19.86068 | -43.80939 | 2025-09-29 05:01:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6df09a49-600a-38f1-8dd3-cace78683077 | -17.90781 | -57.6163 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| ba46b418-0d57-3ac3-b874-0268407a3965 | -17.89849 | -57.6108 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f4a1fc6d-876b-3cf7-a48d-176935d66990 | -17.89908 | -57.60716 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 1950ba48-7d89-3f28-82d8-a34278f2c2a5 | -17.9018 | -57.6114 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7db8c7ad-df92-3201-b256-068a5bd16fbe | -23.22296 | -49.41088 | 2025-09-29 05:01:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| cb85ec2d-9572-3204-b25e-b51968029e44 | -18.19561 | -53.32931 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4fa424ca-cb84-36b4-9094-a6f998249f2a | -17.90121 | -57.61505 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 98d971ef-d098-3a0c-a96e-5328443e0c91 | -18.20848 | -53.31736 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35601252-a85d-32b3-83a1-4aee57111f2d | -18.17634 | -53.31125 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8cbfd53-4b49-337e-9804-181134c9061b | -18.17393 | -53.32861 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ecac126e-5b7e-3972-9581-1dfbfaff677b | -19.8596 | -43.80461 | 2025-09-29 05:01:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ced32d64-71ac-3f06-900a-21606f09afea | -17.72045 | -46.68864 | 2025-09-29 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91ef0b19-f601-3070-ac0d-4ea4ffa548f9 | -17.9084 | -57.61264 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 2dfff1e6-03a0-34e9-b6b2-80e16fede274 | -17.71065 | -46.68954 | 2025-09-29 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 149e460b-d611-3ec6-92bd-6db79d0d3e8b | -22.37115 | -49.96731 | 2025-09-29 05:01:00 | NOAA-21 | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3c1fc2c7-5529-3aa4-926c-425b0e4a3cde | -17.75227 | -48.76444 | 2025-09-29 05:01:00 | NOAA-21 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6e43cadd-0789-3f8c-bfa1-9ef3e05dd796 | -18.79708 | -47.43616 | 2025-09-29 05:01:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67797293-38e1-338f-bedb-90ef9bb1d874 | -17.90297 | -57.60411 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0e762962-8c91-32a0-9b65-f1599574a6fe | -23.53722 | -54.53714 | 2025-09-29 05:01:00 | NOAA-21 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b67ed7b2-4ab2-3c43-b664-8ab15516995f | -16.01559 | -59.50524 | 2025-09-29 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6f285654-4a7a-370c-bfd9-ef69e6b4f38a | -22.97783 | -48.36101 | 2025-09-29 05:01:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 482479f3-3bb5-359a-a3e0-965cabe04142 | -19.73081 | -43.22532 | 2025-09-29 05:01:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9aad8180-cf54-3807-b160-27485adfb009 | -18.1987 | -53.33422 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e8cdf80-c67c-3cec-b317-79db12ff3b11 | -20.63302 | -46.17247 | 2025-09-29 05:01:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81c25f3c-b4e1-3593-9dc0-e69752a9db4c | -17.7474 | -48.76365 | 2025-09-29 05:01:00 | NOAA-21 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 29c7937d-0704-34f3-8fa6-22f93664dcf3 | -20.63376 | -46.16405 | 2025-09-29 05:01:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f9b4a6d-9f6c-30b1-a13d-f3d3115492fa | -18.79435 | -47.43776 | 2025-09-29 05:01:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9cc8421a-00e9-3536-8eb9-e35dad6abef0 | -18.17695 | -53.3068 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 59f17506-8c42-3930-bc68-e5c3c013d6e0 | -18.17025 | -53.32807 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e7af2d5-28b3-3d45-994a-d7af6e8d0cb1 | -23.42075 | -49.46179 | 2025-09-29 05:01:00 | NOAA-21 | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1a2059e2-883e-300b-84fa-8d28d871fb9a | -19.32837 | -43.8112 | 2025-09-29 05:01:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 69f143d2-b228-3d79-9cf1-178a39b867c5 | -17.91111 | -57.61695 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| afbf2141-72de-3643-aae2-e67dd6a74df2 | -17.91229 | -57.60961 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| f75aecdb-1a2d-3c30-b5cd-f1f962534e0f | -17.90451 | -57.61566 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bd1ec928-609c-360e-b3dd-34226974fede | -18.21025 | -53.30423 | 2025-09-29 05:01:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 25.0 |
| c3cc2a9c-b474-320d-b8c5-021734065fee | -16.02339 | -59.50242 | 2025-09-29 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1c90b99b-6cf3-366d-a2b3-ec3ab2271eac | -16.84505 | -53.1941 | 2025-09-29 05:01:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfbb5f0a-b69b-36dc-85df-ef5c1166cd91 | -18.19249 | -53.32457 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5842b7bf-9650-346c-b32a-f2d06474fa78 | -18.17758 | -53.30229 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bba679de-ac61-377d-b0f8-c99747e38393 | -19.65469 | -45.98113 | 2025-09-29 05:01:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66d9652a-2a1a-349b-b662-82c092d39506 | -18.20787 | -53.32183 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a601f30d-c5d8-385d-bf30-6bf6707bf04e | -18.19601 | -53.33188 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76a04c04-e738-313b-8923-7763458789c7 | -17.91287 | -57.60596 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 522e2b9a-955f-3039-a69d-09678c4ead6c | -19.65515 | -45.97632 | 2025-09-29 05:01:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f71acef-b4ba-32e7-87da-e410809e69ba | -18.20477 | -53.31697 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f11ba2d9-80e4-39aa-8031-e72780b96203 | -23.22888 | -49.40244 | 2025-09-29 05:01:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| e016cf97-6ccd-3d2e-a6c9-6c78b0edb8dd | -17.73724 | -46.69064 | 2025-09-29 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09e8ad25-6109-3af0-a74b-23dc87ab32bc | -18.97778 | -48.40528 | 2025-09-29 05:01:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfb430ec-ba4e-3950-95d5-7c9147d7e0a7 | -17.75162 | -48.77007 | 2025-09-29 05:01:00 | NOAA-21 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| fb79f1b9-b283-3ce8-8751-6292be910c66 | -18.19293 | -53.32702 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a0fc2e3-9871-358d-befa-1c0afda1d21b | -25.06249 | -49.35852 | 2025-09-29 05:04:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ad048341-3617-3310-a835-075483d27a3d | -25.00815 | -49.38356 | 2025-09-29 05:04:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f23de18a-67d8-3595-bf5e-d16159d0ed21 | -0.10112 | -51.27877 | 2025-09-29 05:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ecbc50bc-4c1c-34b2-91b2-e8baa8bb9198 | -0.99549 | -47.06152 | 2025-09-29 05:23:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba017e1f-05a8-3018-b41c-1fb57300b4e4 | -0.10184 | -51.27982 | 2025-09-29 05:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 35c513b9-6e81-3859-9a34-29c3e6717592 | -3.1053 | -47.00993 | 2025-09-29 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b3560a72-0691-3c7c-8048-d9fce2e1bff4 | -3.10346 | -47.02203 | 2025-09-29 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 17a2ef91-f6bb-3739-8b5f-b90056a131d3 | -0.99316 | -47.06149 | 2025-09-29 05:23:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bb57d1af-714f-3fe8-89e8-c3c5e3cdec75 | -3.0976 | -47.01493 | 2025-09-29 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 5392c48b-e9fb-3004-b130-68207bded075 | -2.58664 | -48.40553 | 2025-09-29 05:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f9ff4f7-cb12-3df2-b312-825bbc217ff9 | -2.57917 | -48.40567 | 2025-09-29 05:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e5fcf53a-96f9-32a9-81aa-2563bae22307 | -2.57848 | -48.41038 | 2025-09-29 05:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 4e74e482-d484-3c60-888a-30c1a5ee6c84 | -0.09776 | -51.27353 | 2025-09-29 05:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2391829f-e445-3ae5-b8c2-10f47a8ea9b6 | -3.09852 | -47.00885 | 2025-09-29 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 499022ce-cbcf-33a5-979b-093eb38a02e5 | -3.09945 | -47.00266 | 2025-09-29 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0c61ea23-50ae-3ab5-9ea9-6c7de76c1b8a | -0.9946 | -47.06707 | 2025-09-29 05:23:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 215b3bda-d538-3464-8d3c-404cb93b4c62 | -0.102 | -51.27328 | 2025-09-29 05:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 49cc0a6e-44ba-3bed-9837-5b5067100f5c | -0.10269 | -51.27433 | 2025-09-29 05:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.0 |


[Clique aqui para ver as próximas entradas](README74.md)
