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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07ee7281-60d0-30e0-9fc8-7a68d3d71837 | -7.4257 | -63.5595 | 2026-10-05 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 31013429-5cfe-3178-a348-7bd4a5d5cdca | -10.2199 | -61.4321 | 2026-10-05 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 61b85828-22a4-3675-81ad-2fd443f14d73 | -8.6736 | -54.5481 | 2026-10-05 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 1b1f0d9e-b6c8-3652-9706-5ebdacd01b7a | -3.8447 | -50.3273 | 2026-10-05 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 147.2 |
| 35e0ccdf-7ab6-373d-851e-7dc07e133011 | -2.9817 | -54.1091 | 2026-10-05 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 665edd0c-d6a1-330a-b143-092291a7d149 | -2.9632 | -54.1497 | 2026-10-05 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 195ce41e-eaae-3bb0-aace-c52e448d51f4 | -3.9217 | -49.713 | 2026-10-05 00:00:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| ecfc39cc-865f-3af3-a7a9-8c085002d04f | 1.7487 | -55.6256 | 2026-10-05 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 7f13f7b4-1971-3cf0-92ee-79ef52a40ec5 | -3.2755 | -54.1819 | 2026-10-05 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 120289fe-3285-3757-a817-b12765c7c292 | -0.3952 | -52.0357 | 2026-10-05 00:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 48.0 |
| e6557c60-996b-30af-bc68-6b028ec5e0a2 | -5.5893 | -49.7388 | 2026-10-05 00:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 3e9a8d87-f9f1-385c-8441-dd6d757f97ae | -6.0075 | -53.5122 | 2026-10-05 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 7bc0ed8d-d9e4-37b0-bca8-744eb667faf5 | -3.9032 | -49.7137 | 2026-10-05 00:00:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| bc17d50b-f615-3f6f-8228-c17f97f61a76 | -2.9082 | -54.1108 | 2026-10-05 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 77c16597-732f-310a-b267-71aaf121b851 | -6.9143 | -43.6583 | 2026-10-05 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 87dc3663-f196-3bc0-928e-23144e3d5a78 | -8.655 | -54.5494 | 2026-10-05 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| a71e2eb3-1291-32ac-829b-3228f30a9cff | -2.6859 | -49.0325 | 2026-10-05 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 3f3fbbf2-5552-3963-9526-ef541f83dd77 | -6.1781 | -52.9328 | 2026-10-05 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| a78730be-de1a-36ae-bdf0-b3ebca014759 | -6.914 | -43.6816 | 2026-10-05 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| e5016149-aa09-3645-972b-4f509331a581 | -8.3526 | -62.8302 | 2026-10-05 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| f100e6e9-4eb8-3ac1-a35a-b3100551e873 | -0.3768 | -52.0358 | 2026-10-05 00:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 49.2 |
| afb556dc-c653-37f5-ba2d-f61d0c4cbca5 | -6.8952 | -43.6833 | 2026-10-05 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 031073c6-7a69-3365-ad05-8ea6c24c1ea4 | -7.4626 | -63.5583 | 2026-10-05 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |
| e41046b3-2520-3de5-a111-24ebb74e958f | -3.5128 | -54.6162 | 2026-10-05 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 36f09aa4-2d1f-38e0-9f1f-f7876647188e | -2.9082 | -54.0907 | 2026-10-05 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| ec6abe9b-750e-33b5-8456-2b76466a5400 | -5.5705 | -49.7611 | 2026-10-05 00:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 5b4ae6f5-1ab1-3b4f-8273-564057b3ebd2 | -6.8955 | -43.6601 | 2026-10-05 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| c7a75290-075c-3891-91e6-5e8dc42839f1 | -3.9218 | -49.6918 | 2026-10-05 00:00:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 9f4337f3-14fc-3c3e-89b7-d32d72e22408 | 3.0916 | -60.5757 | 2026-10-05 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| baa5583e-7288-31b1-a75e-e7e8fe66f40b | -9.1613 | -68.2568 | 2026-10-05 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 90ff081f-25ab-3ef3-8db5-5a174d95b9e7 | -8.6548 | -54.5696 | 2026-10-05 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 7b872f4e-7cca-31c9-a5e5-ea5d943ddef6 | 1.7303 | -55.6456 | 2026-10-05 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| aca0b96c-bdc9-34db-a12d-390de561e157 | -8.6734 | -54.5683 | 2026-10-05 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 652656b4-0ac6-33cc-830f-7ee0520db2b1 | -5.9882 | -53.635 | 2026-10-05 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 8faf178c-2a67-34d5-9bad-a8d16861d3b4 | -10.2197 | -61.4513 | 2026-10-05 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| dac7843a-f0e1-3be4-a979-9229fcb4a0a0 | -2.9448 | -54.1501 | 2026-10-05 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 471b1295-1dc5-30db-9f37-aed1f8cffcd8 | -2.9817 | -54.089 | 2026-10-05 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| d07d773a-28ad-3a16-9a1e-3124e21d1139 | -7.4442 | -63.5589 | 2026-10-05 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 231.1 |
| 2663be50-7a1f-3e2e-9d98-ed7c4224e240 | -2.7796 | -54.1138 | 2026-10-05 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 2373e99e-4861-382f-875d-ac837702574b | -2.4432 | -56.383 | 2026-10-05 00:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 780f3c94-de6b-3fbc-bb1c-b01c162df7cc | -2.7044 | -49.032 | 2026-10-05 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 35a10ab5-4ace-3250-81d9-ed55cf9fcbbe | -7.4441 | -63.5777 | 2026-10-05 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 100.1 |
| b4e13720-7dce-3802-b1df-1f77b9e699f5 | -3.9033 | -49.6925 | 2026-10-05 00:00:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 65a3586e-7739-3629-a31a-7e20db006b7a | -5.5707 | -49.7399 | 2026-10-05 00:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 1d7c0948-3e41-3b49-9a19-7f6f6274f980 | -2.9449 | -54.13 | 2026-10-05 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| f5c454be-c77d-3c3f-94ea-c846a8393dd1 | -3.8448 | -50.3063 | 2026-10-05 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 167.1 |
| 5d14910c-d1f4-35bc-a7f9-cf6cf024eed6 | -5.5891 | -49.76 | 2026-10-05 00:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| c948321d-dcd9-3c77-aca6-c661f3dc19db | -6.0074 | -53.5325 | 2026-10-05 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 9a45d652-efa5-37a9-abc7-dd5f0b86a3ed | -2.6675 | -49.0331 | 2026-10-05 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| a0d819e3-f55b-33e0-8f0b-0b81737bf0ab | -2.9265 | -54.1305 | 2026-10-05 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 2deac552-c713-3c00-ac6f-788e904170d8 | -2.7796 | -54.0937 | 2026-10-05 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 42f966d5-7b49-3436-a850-91e179083bab | 1.7304 | -55.6259 | 2026-10-05 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 4439c483-ba44-3237-950b-3cd09e7aed9b | -5.5893 | -49.7388 | 2026-10-05 00:10:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| b56888a0-c2a5-338e-9988-0cfbf8b35666 | -10.2199 | -61.4321 | 2026-10-05 00:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| cc95a7ea-271a-34be-9a42-14777940a415 | -6.9143 | -43.6583 | 2026-10-05 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 09d37b91-36b1-3711-96f8-b5c78e5bbea6 | -6.2343 | -52.848 | 2026-10-05 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 137fea17-1627-37f1-b7b9-ba878898da28 | -3.2938 | -54.1814 | 2026-10-05 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| e31ee73b-4a9d-35f2-b7cb-b481c5f972a5 | -6.2161 | -52.808 | 2026-10-05 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 23729a32-ce09-3822-8412-f3a0167ec5bf | -5.5891 | -49.76 | 2026-10-05 00:10:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 8ac39d73-483c-37c7-bf6e-75a6d65e95e7 | -2.9448 | -54.1501 | 2026-10-05 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 8869d361-79a4-3dfc-b65d-27051706ad18 | -6.914 | -43.6816 | 2026-10-05 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 9498059e-66bd-3227-ad03-dbe0e7e62d75 | -2.7044 | -49.032 | 2026-10-05 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| fc6e17c6-7ef2-34a5-bf13-d4929f39a2d0 | -0.3768 | -52.0358 | 2026-10-05 00:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 87d0a704-8bda-33f9-912b-d1ceb1e8c0fb | -2.9082 | -54.1108 | 2026-10-05 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 577816a4-b986-3d51-995e-8f6a736c92b9 | 1.7487 | -55.6256 | 2026-10-05 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 31fae88e-04b3-3913-9fdb-370717e738a0 | -8.3526 | -62.8302 | 2026-10-05 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 923966b3-7bd5-37d8-aaf9-164bbf8aaa92 | -3.5128 | -54.6162 | 2026-10-05 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 0ddffb9a-f46b-3258-8d54-45d6628866bc | -3.2755 | -54.1819 | 2026-10-05 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| d7dba065-b23b-38d4-9aa6-06dc376aa2e9 | -6.8952 | -43.6833 | 2026-10-05 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 05260aeb-6907-3989-983f-e9ae2ed1b477 | -6.1974 | -52.8295 | 2026-10-05 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 279e3a4e-f9e0-3e1d-ad4d-e2d5fa9bf66b | -2.9082 | -54.0907 | 2026-10-05 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| f57ac000-b05c-305b-8afa-10785e505d1b | -3.9218 | -49.6918 | 2026-10-05 00:10:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 50791ac3-bc98-38b6-a334-09e84ffd237f | -7.4442 | -63.5589 | 2026-10-05 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 233.2 |
| 4df31d88-ca04-3570-9060-e869c0e25f04 | -2.9449 | -54.13 | 2026-10-05 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 03822196-8546-3d87-8b78-f3befe00dec3 | -3.8447 | -50.3273 | 2026-10-05 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 970ee8a3-37cc-364f-8ff4-1209346ea549 | -6.8955 | -43.6601 | 2026-10-05 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 4540e409-9427-3d16-be0c-3f0d6c67bbd7 | -2.9817 | -54.1091 | 2026-10-05 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 425fa338-7927-3dfd-bb43-085bca139e94 | -8.6736 | -54.5481 | 2026-10-05 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 065f72da-c4de-3e9c-ac39-9593c3804366 | -6.1781 | -52.9328 | 2026-10-05 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| d81501da-ca02-3360-9a9f-7cfceb4fc94c | -7.4257 | -63.5595 | 2026-10-05 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 35e0aafb-10b4-3122-9f6a-6e0edc5c5cc3 | -2.9817 | -54.089 | 2026-10-05 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 715769ce-83a1-3362-b7d5-237c2e091439 | -8.655 | -54.5494 | 2026-10-05 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 7254a8bb-99ba-3b6e-b526-9df2543e18bd | -6.2529 | -52.847 | 2026-10-05 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 3c9fe66c-1b08-3cdc-8fb9-fa8c64d295cc | -6.0075 | -53.5122 | 2026-10-05 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 55cf26d9-0e54-32ee-b8ad-ed2a2f8d7d33 | -8.6734 | -54.5683 | 2026-10-05 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4b97c0a7-3311-338b-84f5-80bffc8dbff0 | -3.9217 | -49.713 | 2026-10-05 00:10:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 1b6edef0-ce8c-3614-b737-0ef4744c53da | 3.1098 | -60.5753 | 2026-10-05 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| acc35ca5-33cc-3c35-af62-117bfca7fb00 | 1.7304 | -55.6259 | 2026-10-05 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 084c2a4d-22a9-339e-8204-fac15e87d262 | -2.6859 | -49.0325 | 2026-10-05 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 8230d10c-dbd2-3e2b-8efb-a70ea4674079 | -7.4626 | -63.5583 | 2026-10-05 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 6c2e0c4d-73e1-31d9-8479-aae4abccae97 | -10.2197 | -61.4513 | 2026-10-05 00:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 0f92ba79-a46a-3e4a-8bf1-2b128ce4c53c | -9.1613 | -68.2568 | 2026-10-05 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| a197011b-d5cd-3c05-b1f8-6df4cf4b0edd | -3.9032 | -49.7137 | 2026-10-05 00:10:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 87ef511c-93d2-3456-8d3f-0de9726a5c1e | 3.1098 | -60.5943 | 2026-10-05 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b4a083ef-cac0-3e0a-80e1-7a4dba5bcc14 | -3.8448 | -50.3063 | 2026-10-05 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 23401069-273a-3214-8bb6-2dde3e281083 | -7.4441 | -63.5777 | 2026-10-05 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 722114c7-4e2f-3309-af42-482c4f33eec0 | -5.9882 | -53.635 | 2026-10-05 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 97fb468d-556f-32f0-beda-85611536c816 | -3.3134 | -53.8592 | 2026-10-05 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d5fde355-5f8b-31bb-bc48-8bfe753ad3bc | -6.2159 | -52.8285 | 2026-10-05 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 12817c3b-41a2-3607-aa5a-87a402dd00bb | -6.9244 | -43.676399 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
