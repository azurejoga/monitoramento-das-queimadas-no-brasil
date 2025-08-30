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
| 9ea08754-e8a8-32c7-a023-339939dcaf60 | -9.4433 | -60.5499 | 2025-08-30 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 167.0 |
| 5a02cab2-575e-3154-babe-0b1304e03a9b | -9.4435 | -60.5307 | 2025-08-30 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 909f2c37-9eb0-3e4d-9d5c-8c4d7d40d0e3 | -8.9126 | -62.1058 | 2025-08-30 03:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 2f9fb195-837b-3dd8-a508-175ea0a5b977 | -6.7814 | -43.7865 | 2025-08-30 03:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| d623d93e-9820-38ea-b19e-0c53aad6684f | -6.1663 | -43.3506 | 2025-08-30 03:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 3a180850-53f7-3c35-bbb5-f50229bec136 | -9.0614 | -65.4355 | 2025-08-30 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9c0c5ff8-ab14-3614-abb2-06f31552c7a3 | -6.185 | -43.3491 | 2025-08-30 03:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 4337db2e-e633-3512-81ba-7750d36305d4 | -9.1155 | -65.7699 | 2025-08-30 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 9a415c2a-1e69-37b5-a512-05c68feb2dd8 | -6.1853 | -43.3257 | 2025-08-30 04:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 296.8 |
| b8470e74-cb81-366d-9811-595148caa82b | -9.4432 | -60.5692 | 2025-08-30 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 40eb6c15-4441-3194-8795-c571c445cd6c | -9.0614 | -65.4355 | 2025-08-30 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 95d3fdca-9c5a-36ad-a3ef-723bee7c10c3 | -6.1663 | -43.3506 | 2025-08-30 04:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| b18724c6-275a-3c9a-8b3e-fb3692844cb2 | -9.462 | -60.549 | 2025-08-30 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 5ff45c70-a750-3950-bc93-dfe5adbfdbed | -9.1155 | -65.7699 | 2025-08-30 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| aa9ec85c-2bf0-34f6-83f2-16bc124bde53 | -8.9126 | -62.1058 | 2025-08-30 04:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| d5faa138-a290-35b6-a18d-49bc132dc846 | -9.4433 | -60.5499 | 2025-08-30 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 151.2 |
| cc3c6a0f-b2da-3ea7-98db-70796146a6f0 | -6.1855 | -43.3023 | 2025-08-30 04:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 29ff093f-50a1-35fb-99a5-024ad7eb2e09 | -6.1665 | -43.3273 | 2025-08-30 04:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 186.0 |
| 96aa129d-6531-30cc-9d72-0957dcb50b6c | -9.4435 | -60.5307 | 2025-08-30 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| b9b31e2b-ed40-37b5-b0cf-b2f393eb4ed7 | -6.185 | -43.3491 | 2025-08-30 04:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 142.6 |
| c841733f-3d34-3cb9-82c4-3837694b0cbd | -9.1155 | -65.7699 | 2025-08-30 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| ded784c1-7f56-3ab4-a0a2-e981623f5a8d | -6.1853 | -43.3257 | 2025-08-30 04:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| e01fda7b-c46d-3992-b782-c61494e93a4e | -9.0614 | -65.4355 | 2025-08-30 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| addeba78-dbe0-3660-a0bf-ae5a733edbca | -6.1665 | -43.3273 | 2025-08-30 04:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| af31a225-fa91-3b3e-9213-767930617d5d | -9.0613 | -65.4542 | 2025-08-30 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| d9f8bf2c-26e4-327a-bb96-910f67e6d021 | -7.42114 | -46.02371 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7548b3aa-dea7-3df5-9203-94b821f81b0d | -6.16961 | -44.17634 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 444f04bb-261c-3dfa-b943-980f73fa33ae | -5.67499 | -43.4379 | 2025-08-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f704c366-434e-3538-ae2a-a069c8ce1356 | -5.82573 | -43.23063 | 2025-08-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d6076c44-f6b0-3c66-a556-a06b161c076b | -4.87468 | -46.84894 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 698409e7-5c45-33bf-becd-8091030e05b6 | -4.63059 | -41.39266 | 2025-08-30 04:19:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d44f9d50-0fee-3983-85f8-74e8b8dd0ebe | -6.17727 | -43.31359 | 2025-08-30 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f1edf39-fd13-340e-899a-de46123ea394 | -5.72626 | -45.53091 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e75dd5f-c571-325d-bf93-b6fc91cf50d8 | -7.60567 | -42.71088 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e8fa9949-23b4-3d14-90cc-8335e9c1275f | -3.42087 | -49.04759 | 2025-08-30 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa0e8a50-7972-3438-b05d-a9d4be04aa8b | -5.82434 | -43.81519 | 2025-08-30 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ab651bd3-24d6-3458-ac67-de03fc3a91d0 | -7.43474 | -44.81199 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90189a84-b151-3fab-98de-a860180f3fd0 | -6.45154 | -43.98099 | 2025-08-30 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e88420a2-36dd-3045-bce9-c3ce4b36ca92 | -6.01023 | -43.42382 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f612828-f5dd-315e-9aef-af2e6e993f5f | -9.31915 | -40.21684 | 2025-08-30 04:19:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 346544c8-5540-3f33-a83f-2dd52417176c | -6.17569 | -44.18085 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0e15248-086a-3e26-ba0e-7a90ca5c9439 | -6.18234 | -43.32547 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ab430cf-9059-348b-b107-d77575c93fc8 | -5.67001 | -43.44807 | 2025-08-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e07bda2d-a1e9-3758-beba-aa1d86875ace | -6.04945 | -44.46968 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e23e688-a4ac-3632-baee-2056faf8d836 | -6.68678 | -49.77501 | 2025-08-30 04:19:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f17ca91-ca33-3742-b31b-9d5c84b45e92 | -6.44981 | -44.56091 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d21bab41-fcc3-301a-bb36-6c72c1add00d | -5.62248 | -45.24016 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c1257c2-4578-306c-98c0-c8df81516d16 | -6.52063 | -44.86894 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 239ad219-2f93-3e20-a4a8-3e20ef9b1627 | -3.28484 | -43.41663 | 2025-08-30 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80797739-3e58-371c-8f3b-8a48e006d845 | -6.27822 | -44.46344 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5d74362-1fd2-3a2d-a9c7-efd453a934fa | -6.17292 | -44.17686 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 932cb880-6e6f-31a9-9b89-6875a360ba84 | -6.17897 | -43.32496 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb6c34d7-dec2-30e6-98f0-c7bc97a20dad | -6.56329 | -43.67679 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 486e20f8-fb07-3007-9591-b6fdf385c4d9 | -3.06645 | -39.9295 | 2025-08-30 04:19:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 96e717b5-ab65-3524-bfb3-c6294344ce04 | -5.99869 | -44.72655 | 2025-08-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84372ea7-666d-37cf-a742-a95cd67a3d0a | -5.61768 | -45.00901 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3345908b-8f9e-3198-93e1-b8b5c9d08f3b | -8.46476 | -43.63447 | 2025-08-30 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28a10b46-7823-3141-8564-6a64d780054e | -7.08369 | -44.29074 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7f11e7c-7100-3a2b-970f-4af08900ff12 | -5.42819 | -45.52303 | 2025-08-30 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c6db2097-af34-38e4-b8ae-64d5c6814ee1 | -6.13656 | -44.19244 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7dc6acbb-b4d9-397d-b484-5c29de5ced89 | -7.65148 | -42.65385 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 97f60990-b290-321c-97fe-f67cc22f098e | -7.30287 | -44.3246 | 2025-08-30 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a582ea7f-a4dd-3ff6-9876-024993b16609 | -7.6106 | -44.95002 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 025eddc0-caeb-3d25-8823-b1e5be32607e | -7.05739 | -43.82138 | 2025-08-30 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d0dbb08-702b-3a15-821b-d20c641ca1c0 | -5.04639 | -37.99536 | 2025-08-30 04:19:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 04434712-5a1f-31af-b762-cab0759b0163 | -8.46421 | -43.6381 | 2025-08-30 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9470947b-b4ea-3dad-a3fe-683ecade1803 | -5.69632 | -45.95966 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 38a30e07-2da5-3022-b85f-051bb027805d | -2.44376 | -47.32808 | 2025-08-30 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f18345f-3cc2-32ee-a261-6c11c67502ab | -7.40601 | -44.29471 | 2025-08-30 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a5bec5e-29fb-3b2f-b2d4-14aebe096e24 | -6.41452 | -45.6114 | 2025-08-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5026a358-3fc5-3f0c-9e9f-628a2d4994b9 | -6.18123 | -43.3327 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 190.6 |
| a313e998-926a-32bb-a11e-1f8dcf92d300 | -6.23935 | -42.40619 | 2025-08-30 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 2d128d72-e7dd-3433-a9bb-a17190353f76 | -7.08037 | -44.29023 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccd253c8-50d2-3863-9ab4-033be21123ea | -7.09318 | -44.31727 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e7547b89-a9f7-3607-97cb-b9171b22b84a | -6.2783 | -44.4847 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bcc422b-b1d8-3d30-a317-3a8f7e242067 | -6.26829 | -46.01759 | 2025-08-30 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7470c39d-27f8-3d77-9d04-33b9855fb01f | -6.32008 | -43.79835 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3b3ea92-e61d-3342-a255-285deb063a52 | -5.74765 | -45.37355 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 926fff47-68f6-3c5b-90d1-87ae17f8d205 | -8.4672 | -43.68719 | 2025-08-30 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c9a813f-7e95-3d14-b3d8-4cfb77114a88 | -6.78276 | -43.77533 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9ddf92ad-9c22-3c42-ae26-5046eb23c231 | -7.406 | -49.52139 | 2025-08-30 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb3d56f6-5e28-3a0b-b227-10473d344869 | -6.94504 | -46.17242 | 2025-08-30 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e06d7552-35c9-393e-a6c8-35defc0430d6 | -7.15814 | -45.23204 | 2025-08-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e07b9ed8-4b0e-3dc6-baca-bb9cc907cb9c | -6.17002 | -43.33834 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11739fce-c5d1-364e-8a9e-8b8d3184256b | -7.42169 | -46.02019 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76b4f0d6-459c-3f79-a105-d4c56eeb99e7 | -6.18405 | -43.33683 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1b22eaa-f8ab-3bcd-abef-7d9297eae414 | -5.48284 | -43.51752 | 2025-08-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19401af6-d9c5-3f31-814d-5182894d5c4e | -6.29545 | -42.79459 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 89b3e080-4928-3f9c-89b5-d892c6efd578 | -6.89015 | -44.44199 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c0d275a-3273-3955-8bab-d48e15652b78 | -7.55632 | -45.23212 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eaa65372-db47-3ffe-bd9c-3c77f2146f76 | -6.52619 | -44.85916 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f7c4e31-d0ac-3e09-be50-0d080d189081 | -7.61613 | -44.95797 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c865d19-f2af-316a-9407-d29bbb341b38 | -2.98542 | -48.60556 | 2025-08-30 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4830e5a7-a696-3366-8511-3a9247c2e767 | -4.42379 | -40.71259 | 2025-08-30 04:19:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c440a50d-bb87-35ce-b12f-d0a5e0ec0f12 | -6.12025 | -44.88688 | 2025-08-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b5b2aa59-3d99-3b3a-9dd2-f851d4bf827a | -6.41562 | -45.60444 | 2025-08-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db67497c-0617-31f9-8337-c899065bae49 | -5.22097 | -44.80446 | 2025-08-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0771fc2-ca7f-3f6d-b0e0-1d4b6f75efa8 | -4.63418 | -41.39317 | 2025-08-30 04:19:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 946693bf-61f9-3ff5-b364-d77a5d74dc63 | -6.09163 | -44.0002 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 997e500e-cf5c-3f09-b16a-97da36285aa3 | -6.50524 | -43.54781 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README18.md)
