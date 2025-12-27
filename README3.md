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
| cff365b6-2c50-369d-bb2d-e911ee79c9be | -17.55787 | -57.11057 | 2025-12-27 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 5eddec80-74ae-37ed-869b-805e5bba0854 | -15.52641 | -51.87074 | 2025-12-27 00:49:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c14e355a-8035-3b47-baad-2c8548dad55a | -12.67398 | -46.77288 | 2025-12-27 00:49:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 63b52c79-20c3-35f6-91b6-5336a5d57435 | -12.66841 | -46.77947 | 2025-12-27 00:49:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 9f626d5f-7fe8-3feb-80eb-a18edb8a9d21 | -18.84283 | -53.63013 | 2025-12-27 00:49:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ae788acc-1acf-3032-8c90-94636d55c42f | -10.48614 | -44.93962 | 2025-12-27 00:49:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 46e898c0-2b6e-37f7-a3d2-2f6d92076af5 | -10.94091 | -49.4174 | 2025-12-27 00:49:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 04338c0d-efc7-3039-b4d2-7e8fc4b9ffb7 | -11.63391 | -49.42144 | 2025-12-27 00:49:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 21c7ea18-49ed-3716-9638-8127b59f741b | -10.4889 | -44.9235 | 2025-12-27 00:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 13c3cdfe-c5f3-3b0a-bf60-57080fccef17 | -9.497 | -35.7942 | 2025-12-27 00:50:00 | GOES-19 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.4 |
| b2c0f371-ed97-397c-9276-24e11a070d61 | 1.8317 | -60.8765 | 2025-12-27 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.1 |
| f41ad479-b489-317f-b825-0eafe0723f3d | -3.09971 | -49.45123 | 2025-12-27 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 2b905a1e-935e-37f0-b94a-54b74963a814 | -3.74468 | -49.72321 | 2025-12-27 00:52:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| ef5a5f4f-91fd-333c-b88b-2e5cc4a66bea | -6.2247 | -55.65234 | 2025-12-27 00:52:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 79cfd5d0-9993-3984-b391-1dc96f32e398 | -6.22592 | -55.66115 | 2025-12-27 00:52:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 09ce2caf-fbd9-30e4-ace3-cd0de2e8277d | -1.48455 | -54.20595 | 2025-12-27 00:52:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4e017cfa-53ac-3eef-ba11-05ebab039de0 | -2.89279 | -52.58988 | 2025-12-27 00:52:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| f7076e09-ca2c-3fb6-bfb4-243bec032ed1 | -1.61353 | -54.71643 | 2025-12-27 00:52:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c555e5df-3f4f-3f2d-8372-10b7b4c13dec | -2.98045 | -52.63448 | 2025-12-27 00:52:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fe4dfe69-2102-31da-9690-23539a9f704b | -1.47918 | -54.2021 | 2025-12-27 00:52:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| d6d5b4d9-17d0-366f-a1a4-188cb5a36bee | -2.3739 | -51.91616 | 2025-12-27 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 111608d7-f148-33ba-8329-90804b5fa200 | -3.00446 | -52.87786 | 2025-12-27 00:52:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b793bb03-7a47-3115-bf87-65742eb9212c | -3.13255 | -52.84735 | 2025-12-27 00:52:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1bb87617-577b-3f2f-adae-394c90d76f87 | 1.82982 | -60.87821 | 2025-12-27 00:54:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.6 |
| f6ed85aa-dd20-30c6-92e2-36bd328a573e | 1.83015 | -60.88468 | 2025-12-27 00:54:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c48ea006-c77a-3acd-aba2-f0b7f36fad3b | 3.22918 | -61.19353 | 2025-12-27 00:54:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 637cd89a-6534-35e0-a742-a4b6ffeb903f | -0.10935 | -60.78402 | 2025-12-27 00:54:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5d20bf37-a396-38f2-882f-1240a60d883a | 1.8318 | -60.87274 | 2025-12-27 00:54:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| a8b2abd5-bb5c-36b9-8f89-45357a9feb0c | 2.40026 | -60.39649 | 2025-12-27 00:54:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ceaa68ab-3031-30eb-a0ae-825924712f60 | 1.83155 | -60.86632 | 2025-12-27 00:54:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 8fc47f5c-bd2d-30bd-a868-421804599426 | -10.4889 | -44.9235 | 2025-12-27 01:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| b722145a-5cc1-38bb-adab-05129ba7998f | -2.4685 | -47.7697 | 2025-12-27 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b132ed35-5d62-3382-9568-86a168901de1 | 1.8317 | -60.8765 | 2025-12-27 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 09d13f4e-8b54-30f0-a49b-bec72db0bcb8 | -2.4499 | -47.7702 | 2025-12-27 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| e3c08c41-f5f3-35ab-8b61-d8d4a9be16a5 | -2.4499 | -47.7702 | 2025-12-27 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 48e6cec8-1601-3735-8d76-f3e6fb455b5b | -2.4685 | -47.7697 | 2025-12-27 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 2b1c9be6-44ac-3c8f-a9bf-d69f2faedb47 | -2.4684 | -47.7914 | 2025-12-27 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 5b0af4f7-fd34-3849-8fc6-b515c23f9f22 | -10.4889 | -44.9235 | 2025-12-27 01:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 46817f40-9efd-39f2-97f6-427f37e13eb3 | -2.4685 | -47.7697 | 2025-12-27 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 0b9fe8ba-0b77-3ade-bfc1-156e08ac00e3 | -10.4889 | -44.9235 | 2025-12-27 01:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| d5b7a375-704b-3991-b896-fbb0c9fdb374 | -2.4499 | -47.7702 | 2025-12-27 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 1a31c579-e110-33a7-b578-ff4182fe3a06 | -2.4499 | -47.7919 | 2025-12-27 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| dd61016e-3b41-3cc6-a959-4f4ba949207c | 2.5065 | -60.9822 | 2025-12-27 01:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 52405860-3ff9-301a-9e7d-284556b2fb3c | -10.4889 | -44.9235 | 2025-12-27 01:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 48.7 |
| fb01cde4-2163-30ee-8893-486c4ceef4b8 | 2.5247 | -60.982 | 2025-12-27 01:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 50.3 |
| d1d6aa43-11f7-390d-9c32-d4defe927cb4 | -10.4889 | -44.9235 | 2025-12-27 01:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 5b8b0f49-3967-3266-88b2-f873d686a3fa | 2.5247 | -60.982 | 2025-12-27 01:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 59986680-0159-39b2-a385-f45e99b6c73f | 2.5065 | -60.9822 | 2025-12-27 01:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 85.0 |
| fab4ecd1-eb22-30a1-b8ae-9efca2da9cac | -10.4889 | -44.9235 | 2025-12-27 02:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 0e3a5081-1563-3a08-81fd-121e13e31c02 | 2.5065 | -60.9822 | 2025-12-27 02:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 94.8 |
| f07dc226-f5aa-38a2-8fe0-deb9e6337f74 | 2.5247 | -60.982 | 2025-12-27 02:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 71.6 |
| afd5622f-67ba-3089-90e4-fd656a54e364 | 2.5247 | -60.982 | 2025-12-27 02:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3c544571-a50b-3aaf-9111-3a750639b33a | 2.5065 | -60.9822 | 2025-12-27 02:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| d100e310-cabf-3a31-9a12-eb5fe2aa04ea | -10.4889 | -44.9235 | 2025-12-27 02:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 54.5 |
| ea945b34-1da7-3b6b-a73b-ca72456bbf18 | -10.4889 | -44.9235 | 2025-12-27 02:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 91212d97-0f04-3c7d-8353-21f81c918eda | -10.4889 | -44.9235 | 2025-12-27 02:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 3791b839-6e58-3550-bb50-3627c84fc253 | -10.4889 | -44.9235 | 2025-12-27 02:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| c9f4eb71-2e57-3dcb-8a9c-166d2dcda6b8 | -10.4889 | -44.9235 | 2025-12-27 02:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 9aa2f899-869f-3ba1-a800-b46ce7898177 | -10.4889 | -44.9235 | 2025-12-27 03:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 1f22bb79-6d69-3fed-b2f5-2d542361013c | -7.50309 | -35.23668 | 2025-12-27 03:00:00 | NOAA-20 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 0faf6a6d-9981-3373-b6d6-7614ee82b9dd | -9.74025 | -36.09776 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aab2a136-4b7a-371a-874b-9899ebe7b561 | -9.73941 | -36.10228 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2986746a-aafb-3ff4-9b61-87176a5c4735 | -9.72748 | -36.09975 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6b8e2d76-2891-3c20-a1f2-86aea8d6a7fc | -9.73513 | -36.09204 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 29.3 |
| 5f821a37-b9b9-36db-bc86-bb7db5070927 | -9.73587 | -36.09912 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 59d19487-d8b1-3286-934f-061be493796d | -9.73086 | -36.08184 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| c99227c7-3d65-3d08-b2a9-87b41b1dc921 | -9.7411 | -36.09327 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 84a02287-c45a-31da-baf4-a38308e9e854 | -9.73001 | -36.08633 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 29.3 |
| fd179428-6711-344f-ac3b-ccb820433929 | -7.78779 | -35.1463 | 2025-12-27 03:00:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| bc34da38-3327-3b57-a519-5f97189a7440 | -9.7299 | -36.0979 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 32dbb8c6-bfc8-3284-993a-01968c94be35 | -9.73681 | -36.08311 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 5a2ab5a4-a497-3ddf-a366-ebc9386371cf | -9.72917 | -36.0908 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 29.3 |
| 62ba49a2-e975-3c3b-bb8a-f5a6ec00d3c2 | -9.73077 | -36.09344 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1b08823f-6ae9-3a13-9eac-e9b18b7bee4e | -9.73674 | -36.09465 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| fde20ad9-2527-3ae7-8af1-a69f8c34e8f2 | -7.78859 | -35.142 | 2025-12-27 03:00:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| c893bcb0-cbfa-3733-80bd-84d97c13ed8c | -9.73429 | -36.09651 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f2a4a7cd-c37f-3bb9-9e65-4ab85e7e1394 | -9.73164 | -36.08899 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| 8e36b91d-e4ac-39ca-a354-1ebb5b7a633f | -9.73597 | -36.08758 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 29.3 |
| 9c56eadf-ed86-3aad-8a01-2c47b14dec33 | -9.74093 | -36.10501 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fc83623c-b50c-3d8c-9e1c-722655da0896 | -9.73499 | -36.1036 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a6c3ada1-900f-3624-af00-553a2b87f2a5 | -7.50387 | -35.23239 | 2025-12-27 03:00:00 | NOAA-20 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0cc53586-d074-3ee3-8276-0d1d0135cc97 | -9.72902 | -36.10236 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 045c3b8e-f5da-3325-a3cb-30e87fc7f950 | -9.73345 | -36.10099 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| de5f98b7-cfa3-3799-8613-881eefe29802 | -9.73761 | -36.09021 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 31.2 |
| e74b1fa1-6f44-3b01-b7f2-3b2323cede87 | -9.7326 | -36.10549 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3095493e-2268-3527-9bd1-038914874a92 | -9.73339 | -36.08006 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 1e4ac243-6465-38fe-b247-088b57704b89 | -9.74194 | -36.0888 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8bc7b2e2-c3ca-3681-a6bc-2deb99175962 | -9.73252 | -36.08453 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| 609f49b7-8520-3c6c-b1ad-ca007cb1cc09 | -9.73848 | -36.08577 | 2025-12-27 03:00:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 31.2 |
| 6a4b9640-1afd-3f42-a540-bf5e57b71f7b | -15.87328 | -40.93299 | 2025-12-27 03:02:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 44cc4e42-d86f-3fc9-bc23-dcd958bd0595 | -15.87152 | -40.94065 | 2025-12-27 03:02:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| fc5266c5-62ab-3985-aa2b-653d03d933b9 | 2.5247 | -60.982 | 2025-12-27 03:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 97b84bb8-7aa7-31f0-aca0-f06cc0332a81 | 2.5065 | -60.9822 | 2025-12-27 03:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 331b9f07-b755-37cd-906d-b510dcabe1bf | 2.5247 | -61.0009 | 2025-12-27 03:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 8152675b-e6fd-3b4e-94f1-5a93aea1f7fd | -0.0828 | -51.2738 | 2025-12-27 03:10:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 46.9 |
| d29ee6fd-770f-32d8-8d39-131fc972d8fb | -10.4889 | -44.9235 | 2025-12-27 03:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 1b4474b7-b733-3c76-9fd9-5ed1d437c752 | -0.0828 | -51.2738 | 2025-12-27 03:20:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 61fbd27b-7c30-3b0d-bb1d-755ecadd958b | -0.0828 | -51.2946 | 2025-12-27 03:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 15df1319-65e3-3403-9660-f33095766fac | -10.4889 | -44.9235 | 2025-12-27 03:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 451c376f-1008-379e-9555-2cebca741d86 | -0.0828 | -51.2738 | 2025-12-27 03:30:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 46.8 |


[Clique aqui para ver as próximas entradas](README4.md)
