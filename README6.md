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
| b1f11766-796b-369d-8c26-e332b83bf28d | 1.10635 | -60.53753 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d9007726-1306-3c68-8b25-32b37c7c74d9 | 1.09294 | -60.49266 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d7fff5c1-8ef6-3496-91aa-3954d94d3b1f | 1.1078 | -60.54658 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 909a1a31-84c9-31b7-b52e-a296298b8f35 | 1.11102 | -60.52043 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 39d376ca-2e4a-37e5-a749-791439f5d882 | 1.11167 | -60.53202 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5eedc0c4-1c71-3b4e-9a0d-777c6ef42207 | 2.08017 | -60.53123 | 2026-04-13 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00f82a7d-09b1-3d4c-ba55-e5a28f105d93 | 1.10877 | -60.54411 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ab97c0eb-e8f3-3cc5-986d-b7694092b90f | 1.10346 | -60.51237 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c1582854-5423-3cfd-8e19-66862e06a806 | 1.10707 | -60.54206 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cfd18c69-4f73-30a8-bf54-50dc1f2f16c6 | 1.1065 | -60.53056 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7c79d9ca-535f-3cee-bd17-8168915eb904 | 1.10197 | -60.51019 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe7491d0-6c11-3d50-a4ba-bb0b8fc21cd5 | 2.08608 | -60.52997 | 2026-04-13 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 300eb3e5-b7bf-3517-af05-649c5b8050fd | 3.2342 | -61.2056 | 2026-04-13 06:14:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6eb9c4f1-46fb-3a2f-9beb-db260012afb9 | 1.10875 | -60.51375 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4d1ea11d-d53f-3015-8dc1-718f1d7fa5e6 | 1.11239 | -60.53653 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5c362999-f17a-3a20-9db6-697271910bf7 | 3.23357 | -61.20185 | 2026-04-13 06:14:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5be21088-ad48-3ffe-962a-a326dee40361 | -10.95408 | -45.26399 | 2026-04-13 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 405fe4c6-0a11-36e6-a15c-bc257295d63e | -9.82503 | -37.22836 | 2026-04-13 11:04:00 | TERRA_M-M | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4a3e1867-0659-354f-a2c3-3545b7f2edd4 | -7.8191 | -42.0573 | 2026-04-13 12:20:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 108.5 |
| 67d23031-87eb-32a3-8791-86e245ef5846 | -7.8191 | -42.0573 | 2026-04-13 12:30:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| 36cd2660-1466-3fc1-97b6-7a88fb7a8610 | 1.10207 | -60.52048 | 2026-04-13 12:40:00 | TERRA_M-T | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 61e05f90-57d5-30f6-9a2c-aa828912750b | 2.3782 | -60.95063 | 2026-04-13 12:40:00 | TERRA_M-T | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 17.4 |
| fbe545ac-d1cb-3788-b8ff-60a9f4325e5f | 2.38032 | -60.96618 | 2026-04-13 12:40:00 | TERRA_M-T | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 4f0c5aae-4cf6-3cf1-867f-92c67532b7f8 | 1.10586 | -60.54811 | 2026-04-13 12:40:00 | TERRA_M-T | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 7bc79603-5f43-336a-817e-3efe4121e863 | 1.11292 | -60.53983 | 2026-04-13 12:40:00 | TERRA_M-T | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 2549f1f6-9aea-3046-8e59-2ce85af440a1 | 1.10396 | -60.53428 | 2026-04-13 12:40:00 | TERRA_M-T | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 160.6 |
| e59a33b6-e64e-304b-bcfb-e45c99ce278b | 1.10002 | -60.52753 | 2026-04-13 12:40:00 | TERRA_M-T | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 142.7 |
| b8b73ead-8ed1-34e3-977d-9c452c0344f7 | 1.10202 | -60.54131 | 2026-04-13 12:40:00 | TERRA_M-T | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 19ce3bd9-2b19-3503-81c3-ad612441c474 | 1.11091 | -60.52604 | 2026-04-13 12:40:00 | TERRA_M-T | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.7 |
| f2a5c0c6-8d1f-3cea-b5f5-d2a57c24a469 | 1.2671 | -60.3127 | 2026-04-13 14:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 8dab130f-7669-3562-a4b3-dee7da35189e | -7.8381 | -42.0552 | 2026-04-13 14:40:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 217.3 |


