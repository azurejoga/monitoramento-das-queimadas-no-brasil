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
| 51f0c4c3-811f-3080-901f-4d1b60cce8de | -20.1686 | -46.6738 | 2026-03-24 00:00:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 102.4 |
| ab68dbd5-98c5-3353-8e01-923c9b6b6bfa | -20.1481 | -46.6787 | 2026-03-24 00:00:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 5f14a833-9f94-33b5-9aa4-065a08a10328 | 2.032 | -61.1013 | 2026-03-24 00:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 415eaa71-85e5-3bee-a682-5d5e25d34cc8 | 1.8867 | -60.6677 | 2026-03-24 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 84.3 |
| b3026afb-386f-3b7b-a2d4-ce1ccacc77bc | -20.1693 | -46.6501 | 2026-03-24 00:00:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 6b82c1a8-b917-32ef-ba0b-4c9ef12d701b | 1.8867 | -60.6677 | 2026-03-24 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 4feb4d23-4336-343d-8a2c-5db1b59b4155 | -20.1693 | -46.6501 | 2026-03-24 00:10:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 600922b8-681d-31bf-939e-241f8bcaea07 | 2.032 | -61.1013 | 2026-03-24 00:10:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 62.2 |
| ab52be38-5b2e-3f94-8134-f6c33757503c | 3.3485 | -60.1339 | 2026-03-24 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 57.7 |
| ba22906c-3cd4-3523-9351-edb5cf4fe1eb | -20.1686 | -46.6738 | 2026-03-24 00:10:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 464d6f94-29cb-3e2e-a218-afd9e7ae3c26 | -20.6793 | -48.784401 | 2026-03-24 00:13:00 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eaa03f51-1fa1-3958-9cf0-c02e9a218260 | -20.1556 | -46.680199 | 2026-03-24 00:13:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ece33820-1654-3594-9fba-321fc3627c1f | -20.1705 | -46.6535 | 2026-03-24 00:13:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f48c2a43-ce1b-3e34-bfad-3fc8ea350d7e | -20.1572 | -46.6875 | 2026-03-24 00:13:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6dfe7e50-cceb-3e4b-90f9-49fd1828b84f | -20.8827 | -48.576698 | 2026-03-24 00:13:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| dd34e959-d0b3-33b4-ae34-c83be7c7ef55 | -20.1607 | -46.655899 | 2026-03-24 00:13:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 45e578b9-750b-3cdc-a7a4-6340af9fc429 | 1.0946 | -60.629398 | 2026-03-24 00:13:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5747bf67-c088-3cd0-9778-4ec48736ac87 | -20.1541 | -46.672901 | 2026-03-24 00:13:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 82bea3b4-442e-3b03-943b-523ee2d49568 | -20.1525 | -46.6656 | 2026-03-24 00:13:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| af03d498-7eee-3bb5-9824-7cea46a78234 | 1.0994 | -60.6087 | 2026-03-24 00:13:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 33e56bdd-c792-34ee-82ac-4afb81d68621 | -22.255501 | -46.936798 | 2026-03-24 00:13:00 | METOP-B | ESTIVA GERBI | SÃO PAULO | Brasil | 3557303 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8fdaa3f2-ac5c-3b15-9242-1562816ba711 | -20.681 | -48.7925 | 2026-03-24 00:13:00 | METOP-B | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f22ab92c-056b-3c47-b952-4f347fec79c0 | 1.9028 | -60.620899 | 2026-03-24 00:13:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fc1a0a5d-94c7-3253-b8b3-77e85cadd917 | -20.1591 | -46.648602 | 2026-03-24 00:13:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 49e7a911-8929-33da-ab98-756e3a02ed70 | 2.0426 | -61.068501 | 2026-03-24 00:13:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a633a55c-1a37-3588-b96b-0ca6e1c75726 | -21.1667 | -48.665001 | 2026-03-24 00:13:00 | METOP-B | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 76e80375-6b3e-38c3-abe3-20fcffa0d540 | 1.0897 | -60.606499 | 2026-03-24 00:13:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1ed4f93a-d810-3680-97c4-270a185c2a47 | -20.1654 | -46.677799 | 2026-03-24 00:13:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 84887162-3940-36bc-89d8-9011b212a1e9 | 2.0523 | -61.070702 | 2026-03-24 00:13:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 529a5623-8beb-3ef5-80f6-d027d6a1ef44 | 1.8884 | -60.638802 | 2026-03-24 00:13:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7fcc4b26-83be-3283-819c-6369510c131b | 1.8981 | -60.640999 | 2026-03-24 00:13:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3ba383fd-06bb-36a9-86a1-a1b1dd60c9c8 | -20.1693 | -46.6501 | 2026-03-24 00:20:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 23c339c2-0468-35bd-a2a5-de8f2ea23310 | -23.5881 | -54.3242 | 2026-03-24 00:20:00 | GOES-19 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 79.2 |
| af135980-a8fc-3e98-90e6-cd10ad2fe74a | -20.1686 | -46.6738 | 2026-03-24 00:20:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 82.1 |
| e416629f-085f-3699-af1d-716a42d36ee5 | 3.3485 | -60.1339 | 2026-03-24 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 2e53c889-de67-3a59-99f8-1a6b857c2fc5 | 1.8867 | -60.6677 | 2026-03-24 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.6 |
| f86c9de7-5aa4-347a-9f0b-37fc18431d10 | 1.0845 | -60.6552 | 2026-03-24 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 78ce5de1-b81c-3699-b607-af6f3a4794a0 | -20.15762 | -46.6899 | 2026-03-24 00:20:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 02cb2219-ebda-3954-a58d-b6ca1d2abf50 | -21.16515 | -48.68252 | 2026-03-24 00:20:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 75de0d96-32e5-3b39-baf8-60e02ccbde78 | -20.72975 | -49.43624 | 2026-03-24 00:20:00 | TERRA_M-M | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 17e38dba-151b-37a9-874d-4bf63d665fe4 | -21.16386 | -48.67254 | 2026-03-24 00:20:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 5a066a71-ebc0-391f-8187-9d219143ae7b | -22.25623 | -46.94971 | 2026-03-24 00:20:00 | TERRA_M-M | ESTIVA GERBI | SÃO PAULO | Brasil | 3557303 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d6383640-7da8-3643-917f-5f1b6dc78cbd | -20.15898 | -46.69941 | 2026-03-24 00:20:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d430f174-889a-37bc-8c87-e538f1350c72 | -20.88699 | -48.59147 | 2026-03-24 00:20:00 | TERRA_M-M | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| dc78108d-f0fc-37d3-8cb1-fe0acd0dea0f | -19.65165 | -49.05153 | 2026-03-24 00:20:00 | TERRA_M-M | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f94254a9-6de3-35e3-b891-51ec5373286f | -20.67461 | -48.7926 | 2026-03-24 00:20:00 | TERRA_M-M | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 63790c2c-ef6e-3015-9b8d-5f85ee07c4d9 | -21.04233 | -48.79428 | 2026-03-24 00:20:00 | TERRA_M-M | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.8 |
| 4d53591c-cc78-31f4-9149-ff0e925fa459 | -21.32744 | -49.1581 | 2026-03-24 00:20:00 | TERRA_M-M | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| ddfd9ed6-648c-3bfc-82d8-2f3b055ffaae | -20.67591 | -48.80251 | 2026-03-24 00:20:00 | TERRA_M-M | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 8f5dbe8e-815d-38ed-b14e-59090ceec86f | -21.11294 | -47.46537 | 2026-03-24 00:20:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 19b19695-9df1-3431-b3a2-8b62ad323c6e | -20.16244 | -46.65981 | 2026-03-24 00:20:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 705a7929-edb5-375d-b958-e555bf78a7ce | -20.72842 | -49.4258 | 2026-03-24 00:20:00 | TERRA_M-M | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d8d63dfd-a49d-3d50-b672-e26f01da0065 | -20.15625 | -46.68034 | 2026-03-24 00:20:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 3c113c4d-fd1e-3ba6-bb59-7132e70b9788 | -20.16381 | -46.66937 | 2026-03-24 00:20:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 14095460-dd13-3019-91e2-ee1be8b2ff93 | -20.14734 | -46.68177 | 2026-03-24 00:20:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 533275d6-a25e-31e9-a23e-61b10c2fe7ae | 1.88888 | -60.6656 | 2026-03-24 00:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 1abb4b11-922e-39e1-ae82-abc2f696752f | 0.67901 | -60.50285 | 2026-03-24 00:24:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 2a702856-0344-3555-8b00-16f646686127 | 2.03686 | -61.10443 | 2026-03-24 00:24:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 71.8 |
| f45cfb8b-290d-3892-88aa-2942c72c7911 | 1.88479 | -60.69474 | 2026-03-24 00:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 93fd17cf-72cf-3a77-a4be-f7dc471c21be | 1.84648 | -60.42707 | 2026-03-24 00:24:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 18.2 |
| dbf343ca-d007-3511-84b6-5334631c17ae | 1.88673 | -60.67011 | 2026-03-24 00:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 35c3ed81-64cd-30b2-b569-9f54fcb1e897 | 1.08295 | -60.65148 | 2026-03-24 00:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.3 |
| e6a7e8d5-2d09-387c-b9c2-54c2f100df0f | 1.8867 | -60.6677 | 2026-03-24 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 8e9b7372-ac85-37a1-9f1b-4101b04a2d68 | -20.1693 | -46.6501 | 2026-03-24 00:30:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 49eaaf7f-b691-3b75-b2e8-62fb1ad1b0df | -20.1686 | -46.6738 | 2026-03-24 00:30:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 9184326d-914d-3ca1-9534-bb6944cfdd1f | 3.3667 | -60.1526 | 2026-03-24 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 711e25b2-3e9e-34e3-a4a0-d3a2f81c1078 | 3.3485 | -60.1339 | 2026-03-24 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 45248ea3-3d75-39f4-92d8-5c1e1459bdad | 3.3668 | -60.1335 | 2026-03-24 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 64.0 |
| d6993d0c-ea8c-3cc9-b748-7013b417babd | 3.3484 | -60.1529 | 2026-03-24 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.3 |
| b2f16fe0-a461-30d1-bfc3-1aaeefd3089e | 1.8867 | -60.6677 | 2026-03-24 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 655b42e3-ee5e-3944-8ec0-00f59e92a903 | 2.032 | -61.1013 | 2026-03-24 00:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 35.1 |
| b32edc06-0829-30d9-9aff-c4e365ff276c | 3.3667 | -60.1526 | 2026-03-24 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| cbb8fbe9-f124-3e2e-91db-90d6dfc22ae5 | 3.3484 | -60.1529 | 2026-03-24 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 9a553690-bd81-3ae7-b6c5-341724fa4a71 | 3.3668 | -60.1335 | 2026-03-24 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 02dc3bc8-6f20-3eb5-90cb-7a2df206845c | -20.1686 | -46.6738 | 2026-03-24 00:40:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 79.2 |
| dd0b22d2-46b4-3590-a5bc-9260f1a24aa8 | 3.3485 | -60.1339 | 2026-03-24 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 93470ed0-bf75-3793-a4bf-7741f8a40b44 | -20.1693 | -46.6501 | 2026-03-24 00:40:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 04926aa9-13b3-3c45-a9f6-e833c8e8916b | -19.6514 | -49.045898 | 2026-03-24 00:47:00 | METOP-C | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e9260c2d-981e-34eb-a564-69035a60e6ab | 3.3729 | -60.1231 | 2026-03-24 00:47:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d8bc3350-46ec-3e19-9d1c-d30a52782941 | -20.162399 | -46.653599 | 2026-03-24 00:47:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dd460443-6a4b-30dd-aad8-a6b4394db055 | -21.162701 | -48.672401 | 2026-03-24 00:47:00 | METOP-C | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f1b732aa-4eb2-3831-b774-bec784dcfa8d | -21.042101 | -48.782398 | 2026-03-24 00:47:00 | METOP-C | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9b00c86a-fc3a-350e-9b14-41c2f19c9f39 | -20.1462 | -46.673 | 2026-03-24 00:47:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 87b7687f-7e6d-3410-a28c-4325a015499f | -20.165701 | -46.668201 | 2026-03-24 00:47:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 88e3099d-e689-3032-b5fd-7df440acb91e | 3.3691 | -60.139 | 2026-03-24 00:47:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3ab364d3-2ae9-382f-ba98-22556c432ee3 | -20.1576 | -46.677898 | 2026-03-24 00:47:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3cccf759-d918-3e0c-b142-55d5cd1a01f2 | 1.8964 | -60.6432 | 2026-03-24 00:47:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dee318f1-c06b-3241-a7c0-37c1034fa032 | -20.159201 | -46.6852 | 2026-03-24 00:47:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e2a01c8d-2aee-31e4-b3fb-c35766a033c4 | -20.156 | -46.670601 | 2026-03-24 00:47:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6bb1c23e-1f29-3bb8-a246-771725f572c8 | -20.160801 | -46.6464 | 2026-03-24 00:47:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 53f638b5-20f6-34fe-9eef-e12755e756d6 | 3.3594 | -60.1367 | 2026-03-24 00:47:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 17093347-5c7d-36d3-854e-11c0ece5015c | -20.1478 | -46.680302 | 2026-03-24 00:47:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 38dfa264-1cb2-3d11-a53f-00e964450fea | -21.043699 | -48.790199 | 2026-03-24 00:47:00 | METOP-C | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fc9ca0af-605a-3c9a-a93f-c0f55be31006 | -20.164101 | -46.6609 | 2026-03-24 00:47:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c5dbe6c0-7940-3a14-9e8d-37bc6e125ec8 | 2.0501 | -61.075199 | 2026-03-24 00:47:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8d3e7bdf-5a73-30f1-9b37-75f8341033bd | 1.9018 | -60.6637 | 2026-03-24 00:47:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5cc30839-5400-392f-b42f-8f9ff3b95245 | 2.0455 | -61.094601 | 2026-03-24 00:47:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4476b72f-7373-3caa-9773-89a35fe3eef2 | -20.675301 | -48.793598 | 2026-03-24 00:47:00 | METOP-C | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e1402cb4-d757-38e7-83bb-2e3065243999 | 1.8921 | -60.661499 | 2026-03-24 00:47:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| eed7e9f1-5ea1-3ed2-bcf8-ae98d4080243 | -16.43 | -54.9235 | 2026-03-24 00:47:00 | METOP-C | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
