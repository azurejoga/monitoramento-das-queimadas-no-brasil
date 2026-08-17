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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cb088da-4adc-33b0-a85f-3a286a14e31a | -9.47578 | -60.54582 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b522d6e7-4b71-3556-bcaf-16f140944862 | -15.78473 | -55.56865 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c650beaf-b4d4-3db3-a4f5-b6fca2e519b1 | -11.72125 | -54.6195 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05c89af9-fa34-34d6-b448-ecdf6a4375d5 | -11.22851 | -54.01728 | 2026-08-17 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f6b43a6-dfee-3058-8ab1-29278adfcef9 | -14.18842 | -53.06069 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 374292a2-016d-3e26-bfd4-17d62cebb2e7 | -12.20738 | -52.87132 | 2026-08-17 05:18:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4d71ca9-5c56-34ba-a8d7-7f2ad2470f38 | -9.58659 | -61.01804 | 2026-08-17 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b733c48-8337-3375-9817-b81addfdae76 | -11.71363 | -54.61837 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4528909e-4330-3bd1-a1df-110b65860699 | -13.50348 | -46.23622 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| faf30f6d-86eb-32e9-a041-dcd4fd170115 | -11.71226 | -54.62777 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98664948-881a-3d36-abbf-da78640af3ad | -14.32428 | -53.04743 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c55279b-4628-3c64-8666-a15201e3b298 | -13.50443 | -46.2537 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67c50368-582c-3600-b72a-ff06bca7e2d9 | -10.92842 | -57.13223 | 2026-08-17 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 980609b8-071c-37d1-8638-47240da0f8a4 | -11.48232 | -46.57572 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e5d9f39e-b36b-3445-969a-2cb6ffa6d288 | -15.8994 | -55.5334 | 2026-08-17 05:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| e294ac06-f7ba-381f-adb5-2594c948b9d8 | -15.9189 | -55.531 | 2026-08-17 05:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 135.1 |
| ec7d01c8-25c8-3281-b519-151d5348f2c4 | -6.6568 | -58.9628 | 2026-08-17 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 6f0dadc1-e16d-356d-8daf-d8428675e867 | -15.9185 | -55.5518 | 2026-08-17 05:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 5758d284-be59-3d20-acbf-c616f2a93fea | -6.6384 | -58.9636 | 2026-08-17 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 7b0b7ce0-11f9-3441-a47e-b590a4f5346a | -16.21479 | -57.6373 | 2026-08-17 05:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c1c7a5f7-9518-3222-ad42-5e1da9daa0fa | -16.21767 | -57.64175 | 2026-08-17 05:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0a02a404-76bb-3b21-8580-31f62a1ccd7c | -18.44375 | -49.73729 | 2026-08-17 05:21:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1a322b9-e542-354d-8fbc-10b50f936fc2 | -18.80543 | -46.74141 | 2026-08-17 05:21:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6d73504-6d23-3627-bbfa-8357e351755c | -16.19754 | -57.63443 | 2026-08-17 05:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a6be7622-34f4-3af6-86fd-9871bbcf7f2f | -18.80603 | -46.7346 | 2026-08-17 05:21:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de56e00e-54cb-3bdf-99ae-b3698b9fca1d | -20.73315 | -47.82866 | 2026-08-17 05:21:00 | NOAA-20 | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e5649587-4cca-3a99-95a9-5494bebefed7 | -18.44415 | -49.73326 | 2026-08-17 05:21:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7004b814-c043-3826-900e-0f4c5cfbc699 | -17.53298 | -49.20951 | 2026-08-17 05:21:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbe27a27-6742-30ab-ad81-0f058b7e0f9e | -20.73172 | -47.81981 | 2026-08-17 05:21:00 | NOAA-20 | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| daa4d634-ddc8-3904-9cf1-d75b50e4ebb4 | -22.0858 | -55.96717 | 2026-08-17 05:21:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9634c77c-8e5e-36da-86c1-0e7c73916ee8 | -16.23089 | -57.64795 | 2026-08-17 05:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 91a893f1-4a1c-3f64-ad5b-1145850d8e85 | -17.32806 | -54.93734 | 2026-08-17 05:21:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 16c3179a-b2de-3d3c-8255-c5b0763168d5 | -17.32403 | -54.93679 | 2026-08-17 05:21:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74cffe21-01ea-3f1c-85b2-1e55652d99ae | -16.22053 | -57.64627 | 2026-08-17 05:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a58304c2-aa35-3bd4-8946-7b8b69b25f56 | -18.44858 | -49.73734 | 2026-08-17 05:21:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95c42b86-09d6-3f66-9641-5c097d0103f5 | -17.32851 | -54.93393 | 2026-08-17 05:21:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb68d337-2416-38b0-8b6d-3171b7897d7d | -16.21652 | -57.64951 | 2026-08-17 05:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a57b7e3d-c230-395c-8381-e3fe36a66ec7 | -17.534 | -49.21075 | 2026-08-17 05:21:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95a0da86-c48e-364d-9a54-9c64c6807431 | -17.32448 | -54.93337 | 2026-08-17 05:21:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d4cb49c-b51a-307f-9508-422a33111853 | -16.22686 | -57.65126 | 2026-08-17 05:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e43898f1-dec9-3481-9016-2b3798b55df8 | -16.23031 | -57.65184 | 2026-08-17 05:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| e4e933a3-1915-3961-8201-316a9b63108e | -16.21307 | -57.64892 | 2026-08-17 05:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d90e864d-d022-3fd0-82f7-87aa65cfc19d | -20.7337 | -47.82231 | 2026-08-17 05:21:00 | NOAA-20 | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5f7bb5c3-986c-317e-a64b-bf6210d783a9 | -16.20099 | -57.63501 | 2026-08-17 05:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 32010951-4a71-3e4d-95fa-0eab0e0a9c01 | -17.53352 | -49.21527 | 2026-08-17 05:21:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa6779a2-d1c1-3c10-9226-020468957eea | -17.3294 | -54.9271 | 2026-08-17 05:21:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9933a9b2-77c6-3a98-82b1-86510ef50ba9 | -18.8061 | -46.73582 | 2026-08-17 05:21:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 06968a12-bb31-32c6-b3a1-f97ffac656e4 | -16.22341 | -57.65068 | 2026-08-17 05:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 02bad38e-9316-3d0d-bea5-be416a7396e7 | -16.22743 | -57.64741 | 2026-08-17 05:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1b1905d5-328b-336e-b826-d8552c587de2 | -18.44282 | -49.73685 | 2026-08-17 05:21:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fbdd070-179a-3603-8929-632466b297b6 | -16.22398 | -57.64685 | 2026-08-17 05:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d80d6ebb-8e24-3999-b4f3-85eba456b59c | -20.73122 | -47.82605 | 2026-08-17 05:21:00 | NOAA-20 | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e273ad71-5c17-306b-b571-39a47208b322 | -17.53253 | -49.21399 | 2026-08-17 05:21:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e980a90-7d05-3adf-8466-1a4b975b57bd | -16.21997 | -57.65011 | 2026-08-17 05:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5c3ae57c-c005-38f0-8921-d08f3075b42d | -15.9189 | -55.531 | 2026-08-17 05:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 8f16e578-3842-3bee-b525-93bb8c5b164d | -15.9185 | -55.5518 | 2026-08-17 05:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 86f10b85-4b26-3c41-bd17-bceb157e4982 | -6.6199 | -58.9643 | 2026-08-17 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 63ba9690-1a04-3751-9f2b-e63c7ec097b1 | -6.6384 | -58.9636 | 2026-08-17 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 4d950d15-250c-359a-9bea-80fc6af67a3e | -6.6568 | -58.9628 | 2026-08-17 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 2c7468ce-33b6-353d-8023-573222e2e3e6 | -15.8994 | -55.5334 | 2026-08-17 05:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| d59bc726-ceec-3487-a794-5e25b737559c | -15.9185 | -55.5518 | 2026-08-17 05:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 76621c82-a67b-3c34-a0ca-8bd95c69ff40 | -15.8991 | -55.5541 | 2026-08-17 05:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| f68ef056-4cb5-313d-aacf-7ffd2fb8ca79 | -6.1106 | -57.7425 | 2026-08-17 05:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 38982ebc-1948-3a8e-9745-400f0a6ff2e4 | -6.6568 | -58.9628 | 2026-08-17 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d20dbbc7-4b20-3bf2-a84a-ad3e48a67195 | -6.6384 | -58.9636 | 2026-08-17 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 1ed3417e-e5ec-327a-96d1-0f6b67c426e5 | -15.9189 | -55.531 | 2026-08-17 05:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 91dd4770-49dd-372d-bdaa-3f68ed60359d | -15.8994 | -55.5334 | 2026-08-17 05:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| e4780566-b98d-390c-ba9d-c2268f698178 | -6.6384 | -58.9636 | 2026-08-17 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 078b01a8-7356-3b06-9a3d-aab681fccb4b | -15.9189 | -55.531 | 2026-08-17 05:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 121.3 |
| d5bd07ac-c4c6-3a5c-a6d8-cfa65bd5b3fd | -6.6568 | -58.9628 | 2026-08-17 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e34c2d52-9174-31e0-a27d-979ee0fd90de | -15.9185 | -55.5518 | 2026-08-17 05:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 59c52786-71b9-38d2-85aa-5f8440802c61 | -15.8991 | -55.5541 | 2026-08-17 05:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| b8a39a1c-a109-3949-9587-0307114ead5f | -15.8994 | -55.5334 | 2026-08-17 05:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 223b29f5-496d-3868-8c37-98d47e9bde3c | -3.89341 | -59.35251 | 2026-08-17 05:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc76fae6-b950-3e3a-bf4e-e22b573cea35 | -3.80692 | -59.33353 | 2026-08-17 05:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e607d53-108f-3612-9067-4139c6bf587e | -3.15016 | -60.26222 | 2026-08-17 05:59:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a7ddc33-a402-3475-bb18-f1e5dd9c4640 | -3.89397 | -59.34852 | 2026-08-17 05:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8addbbc6-01cd-3ff2-8c36-291bf973f2a5 | -3.80542 | -59.3341 | 2026-08-17 05:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75807ad4-7f5e-3bab-95ef-7de6786eecd6 | -3.14967 | -60.26555 | 2026-08-17 05:59:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9145e68f-39ca-3ec7-ac28-43842c29805c | -3.80635 | -59.33753 | 2026-08-17 05:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0f71ab9-28e7-3994-8285-7656d47ec028 | 0.49084 | -60.59617 | 2026-08-17 05:59:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed95ce18-fc32-3bae-b43c-839367f25fe4 | -3.79968 | -59.33321 | 2026-08-17 05:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c602b628-0d08-3ac9-ad4b-5ee27ec9d4b3 | -3.80118 | -59.33263 | 2026-08-17 05:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 172c3009-606c-3f9b-a7d1-64cd62e0ab8b | 0.48928 | -60.59682 | 2026-08-17 05:59:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f070f20f-8169-31d2-8af4-32974e87869a | -3.80062 | -59.33661 | 2026-08-17 05:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e219d25d-4d78-38c5-910e-14bfb5b28b2e | 0.49487 | -60.58971 | 2026-08-17 05:59:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 326ba2e5-cec8-39f3-aeb6-162e3e0bd435 | -15.9189 | -55.531 | 2026-08-17 06:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| ed7ee1fa-0971-3d73-b64c-85f21da11c3a | -11.1299 | -46.5019 | 2026-08-17 06:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 1a3ebe0d-0301-3d46-a092-01532ec92b0d | -15.8994 | -55.5334 | 2026-08-17 06:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 45a883a3-dc72-38ec-adca-00320a50277e | -6.6384 | -58.9636 | 2026-08-17 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 0dc873fb-3eb2-36aa-bf0b-4c5227fb6b18 | -11.1487 | -46.5219 | 2026-08-17 06:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| beb9a5e4-f26e-3e24-a9dd-5a3bb8dd5df2 | -15.8991 | -55.5541 | 2026-08-17 06:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| e2173084-6cea-3c89-a597-70d0714934d7 | -15.9185 | -55.5518 | 2026-08-17 06:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 116.2 |
| ebc0736a-d79e-3bfc-9ea8-2f17c6dc9abb | -11.1296 | -46.5244 | 2026-08-17 06:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 33b28897-698b-35fd-83aa-2000ba99e4ed | -8.96552 | -60.5223 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9262351-3501-3fc1-a8a2-92d481401754 | -6.62545 | -59.07726 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8256760c-7457-3ca6-a83b-16a69fb925ea | -9.37497 | -62.36392 | 2026-08-17 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdba9a72-5e88-331f-821f-f55de6db59b4 | -7.42923 | -60.02885 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 294a4777-7c7f-31cc-98c1-47bf3fa18bf0 | -8.97172 | -60.51915 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d6ee11d-ccbe-3280-b944-908c22603869 | -9.17948 | -59.6782 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README60.md)
