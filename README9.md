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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a410464-ad21-3938-81f3-f112cb0a3d79 | -2.90539 | -48.30285 | 2025-08-19 00:50:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7a77a984-8fb5-383e-8111-b6f88fe1f160 | -4.0007 | -42.5149 | 2025-08-19 01:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 109.5 |
| abc6b304-8ba8-3da0-84f8-9b5570b86464 | -5.5785 | -44.0914 | 2025-08-19 01:00:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 1b151c76-b21a-3199-a2e7-bfbd80405392 | -9.1895 | -59.6364 | 2025-08-19 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 666d4b25-cb08-3586-ace2-7fe24589c4c8 | -14.9809 | -54.8158 | 2025-08-19 01:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| dd67db05-9b08-3611-9a50-09b6b05cfb79 | -13.0162 | -56.8378 | 2025-08-19 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 49db78d5-db17-3572-920f-0f76da62d84e | -5.557 | -49.0801 | 2025-08-19 01:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 2027791a-2f10-3cf1-b163-9f5110c2580b | -6.9524 | -43.6083 | 2025-08-19 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 01bc8be1-7111-3941-9d7c-4ce440f2ec06 | -5.5571 | -49.0587 | 2025-08-19 01:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 11b372ab-f7f4-34ff-8307-477b7cd891e5 | -21.8869 | -48.1841 | 2025-08-19 01:00:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 60fed646-0340-3507-8ba6-a477c6ab93d7 | -6.9715 | -43.5833 | 2025-08-19 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 9351ef02-b5f6-361b-a4c9-12bca8203116 | -6.9336 | -43.6101 | 2025-08-19 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| e29e031b-8fac-38ce-b76c-50cecaeb75bf | -16.4659 | -45.098 | 2025-08-19 01:00:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 259.3 |
| 0d018991-20f8-3abe-9b63-d5786c569587 | -16.4857 | -45.0939 | 2025-08-19 01:00:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 623.6 |
| 2bf3b918-2f68-3129-a490-071edd27c136 | -17.3451 | -47.1551 | 2025-08-19 01:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 14d0f75c-14da-34ad-88ba-690855355e70 | -3.982 | -42.516 | 2025-08-19 01:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 275.5 |
| 57cde589-4ae8-3fa2-885c-06d68d499085 | -9.1894 | -59.6558 | 2025-08-19 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a7e8315b-0604-327f-b44d-38394dda052b | -8.9788 | -60.4964 | 2025-08-19 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| b846dfdc-1931-3dc6-a062-09ac44f0bdce | -16.4665 | -45.0743 | 2025-08-19 01:00:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 1ea2388b-47fc-38d8-9304-f1d0220e613f | -15.0389 | -54.8089 | 2025-08-19 01:00:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 42fb6d44-8c67-3db9-9c0b-ae232ed4d295 | -16.4851 | -45.1176 | 2025-08-19 01:00:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 128.7 |
| f495b24a-d053-304a-ac2c-da5820de43bf | -6.9527 | -43.585 | 2025-08-19 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 36c7ab58-c010-37c2-b59e-2c993deca625 | -5.7887 | -43.6134 | 2025-08-19 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| f076de21-86cb-35ed-9e88-a880761313b5 | -12.9971 | -56.8395 | 2025-08-19 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 8b1f07d0-6586-3253-8391-2007a664eaab | -16.4863 | -45.0702 | 2025-08-19 01:00:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 203.7 |
| 3d66f47d-ba09-3458-9c50-9b973ffd7db0 | -6.9712 | -43.6066 | 2025-08-19 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 7e3523fa-9a59-3188-ab68-a215562f3bc2 | -11.8702 | -51.578 | 2025-08-19 01:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 8c3147dc-73b9-31b6-82ec-5a91f02181dc | -6.9339 | -43.5868 | 2025-08-19 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 3b64742f-ef90-3324-9215-71aa5d0623a3 | -15.0196 | -54.8112 | 2025-08-19 01:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 9b9f6ef1-9153-3e5d-aec1-30b9b04eae2e | -3.9819 | -42.5396 | 2025-08-19 01:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 115.4 |
| 923f23b0-cb5c-38bf-bf0d-f70c6a51b6ac | -16.4653 | -45.1218 | 2025-08-19 01:00:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 62.3 |
| ee90e50a-c793-3343-a1aa-6f23dc638d0a | -14.9812 | -54.7951 | 2025-08-19 01:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| b392c18f-d547-302e-8800-d1ac4958d5df | -5.7887 | -43.6134 | 2025-08-19 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| d0ddadd8-ea71-3f5b-a069-70c22cc5e932 | -8.9788 | -60.4964 | 2025-08-19 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 5abca112-8ca0-3480-be69-1d93411bbc14 | -21.8869 | -48.1841 | 2025-08-19 01:10:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 301e989b-8f66-3575-b290-e0ac4465e661 | -13.0162 | -56.8378 | 2025-08-19 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| f109cf80-fc04-36b9-9ad4-b518bd8d9d1e | -6.9527 | -43.585 | 2025-08-19 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| ad21d69f-475f-3cf2-9de1-03ef110e79fe | -16.4851 | -45.1176 | 2025-08-19 01:10:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 91.7 |
| e0846945-6477-364d-897e-80bbdb43b0ba | -6.9336 | -43.6101 | 2025-08-19 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 6d5516fd-4020-35cd-a6f5-57b0fa0fcc71 | -7.2602 | -50.1613 | 2025-08-19 01:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 8ce9079e-cd8d-356e-97cb-31e0070faef0 | -9.1895 | -59.6364 | 2025-08-19 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 10428541-e60e-367a-9c0b-1eaf72040d2a | -6.9339 | -43.5868 | 2025-08-19 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 32414f79-5eeb-34a8-81f6-d144b8aacdba | -17.5729 | -44.4764 | 2025-08-19 01:10:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 82.0 |
| baeece18-0760-3d81-bccc-c78cacee53df | -16.4659 | -45.098 | 2025-08-19 01:10:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 234.8 |
| 32e57bb1-5dba-3817-8263-25faa5f23bf4 | -16.4857 | -45.0939 | 2025-08-19 01:10:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 325.3 |
| e26ea444-53e2-36ae-94ab-38a63a145db2 | -16.4863 | -45.0702 | 2025-08-19 01:10:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 5503940e-266b-3da8-8d34-96e2208fcf07 | -3.982 | -42.516 | 2025-08-19 01:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 203.3 |
| 10835efc-35ac-30bd-af2e-283e39edd86f | -19.9433 | -48.1957 | 2025-08-19 01:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 75.9 |
| dc2192b5-fc35-3092-95da-12d507e96fc6 | -6.9712 | -43.6066 | 2025-08-19 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 1606a9c1-2a36-379b-ae59-803ff2a42ed5 | -6.9524 | -43.6083 | 2025-08-19 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 4350d203-ee9c-3b26-81b1-979565dd47f9 | -14.9812 | -54.7951 | 2025-08-19 01:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| a7099696-c468-3c5b-9a53-ebb2de445939 | -16.4665 | -45.0743 | 2025-08-19 01:10:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 86.0 |
| fe4bd749-240a-3de3-ad5d-f240c4022d5f | -15.0196 | -54.8112 | 2025-08-19 01:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| ff82cfac-15a2-318a-a30c-b87a11c36c8f | -5.5785 | -44.0914 | 2025-08-19 01:10:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 8f80e3b9-6e84-34ca-b398-26548192fc84 | -13.1555 | -54.9357 | 2025-08-19 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| c7d6a4fa-f7fc-3b96-b44f-582acbaf15df | -16.4653 | -45.1218 | 2025-08-19 01:10:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 76394269-fd89-32da-bb63-b4706fecad64 | -4.0007 | -42.5149 | 2025-08-19 01:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 89462eba-a092-31eb-b7a1-4a6cd34c92fb | -6.9715 | -43.5833 | 2025-08-19 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 326c50a4-63f2-3ab4-9d34-a1985fbc9ddd | -14.9809 | -54.8158 | 2025-08-19 01:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 8845b50c-f1f5-3726-8bd8-7a5632f2e414 | -3.9819 | -42.5396 | 2025-08-19 01:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 9e810ff5-195a-347b-a655-e1d16938a0ce | -15.0196 | -54.8112 | 2025-08-19 01:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| ef5ad235-7b84-330b-a023-f3093d5ee119 | -6.9339 | -43.5868 | 2025-08-19 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 106.4 |
| bac8821a-80a9-3c97-9263-a4137bafdc74 | -6.9715 | -43.5833 | 2025-08-19 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 74a414a6-56cb-37d4-8bdb-70c0acc35ea7 | -14.9812 | -54.7951 | 2025-08-19 01:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 0bff4483-ba7c-3350-8728-f30aea73811c | -15.0389 | -54.8089 | 2025-08-19 01:20:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 43cba5fb-5c6c-3a6f-88d0-88c13fdeb756 | -6.9524 | -43.6083 | 2025-08-19 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 187c342f-825b-33e4-bc78-481dc031eb7b | -3.982 | -42.516 | 2025-08-19 01:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 153.8 |
| c2787b37-e278-3224-b7d4-28b51caef162 | -6.9336 | -43.6101 | 2025-08-19 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 7deb0894-aaaf-3df9-bd73-7332d3eb4964 | -8.9788 | -60.4964 | 2025-08-19 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 5be988aa-8fff-3302-ba71-7d6d145bf31d | -5.5785 | -44.0914 | 2025-08-19 01:20:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| d7bbbdf0-4ad7-3033-90b5-83fcd8e2dfe3 | -6.9527 | -43.585 | 2025-08-19 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 21757a49-ce38-3eb5-9892-60a51d174b25 | -3.9819 | -42.5396 | 2025-08-19 01:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 9e7ea7bc-8343-322f-bed0-de559f94049f | -13.0162 | -56.8378 | 2025-08-19 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| f78d393f-b857-3040-8b2b-6c3688341db9 | -19.9426 | -48.2189 | 2025-08-19 01:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 1de99a7c-fd7d-3bc8-828c-636d6b63b547 | -19.9433 | -48.1957 | 2025-08-19 01:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 655ca3f8-5ad8-3772-83f4-8f075e7cc132 | -4.0007 | -42.5149 | 2025-08-19 01:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 60.9 |
| 084998fb-e684-36e4-8884-6f07be62ce21 | -5.7887 | -43.6134 | 2025-08-19 01:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 15096036-4156-3c29-915d-505d0b59b377 | -6.9712 | -43.6066 | 2025-08-19 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 803f496f-57ce-3d4e-9671-5ae84816fbf5 | -9.1895 | -59.6364 | 2025-08-19 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| f1378300-732a-37b7-91bb-37e77819603e | -11.8702 | -51.578 | 2025-08-19 01:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 8df00d3d-cbe3-3c1d-afa4-ce3084a0f7b1 | -5.8807 | -48.1125 | 2025-08-19 01:20:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 720c91cf-8507-3f16-a8d0-ca584b9ce1f9 | -7.7932 | -66.949501 | 2025-08-19 01:27:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b996f373-6ed1-3179-9c21-effc97473de8 | -9.1876 | -59.661701 | 2025-08-19 01:27:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6164b008-0983-3fb8-b7d0-5e3ea86cb1d1 | -12.9815 | -56.8489 | 2025-08-19 01:27:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 344c8020-834d-37b7-8ce7-71273543256f | -7.5988 | -67.368896 | 2025-08-19 01:27:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f821770a-d0d0-36e3-9221-f28d7acff8f0 | -14.9838 | -54.794498 | 2025-08-19 01:27:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 961366b6-07d9-3d13-8566-1fd164bdeb91 | -13.1699 | -54.957802 | 2025-08-19 01:27:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80e5be2e-32ee-32b5-a64a-0ea0e354585b | -9.1996 | -59.627201 | 2025-08-19 01:27:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de1e0c93-b329-345f-b909-565784155092 | -7.4491 | -63.025299 | 2025-08-19 01:27:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 709f6806-911b-3b87-92d7-a567ea3c7734 | -9.1779 | -59.664101 | 2025-08-19 01:27:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 603351d3-f270-32c9-bcb1-44446d96c74d | -9.1803 | -59.632 | 2025-08-19 01:27:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5b71206-57a2-3031-b8ad-f630046e286c | -12.9866 | -56.868698 | 2025-08-19 01:27:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8af5374e-81b2-36c2-8223-89940143b1d1 | -7.7963 | -66.963303 | 2025-08-19 01:27:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f2148e54-be16-370c-abf1-f0ee890977d0 | -7.6 | -63.449799 | 2025-08-19 01:27:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c48a78ca-33da-3c24-ad60-3944a40471e7 | -13.0008 | -56.843601 | 2025-08-19 01:27:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bbc051fc-32f9-3dd7-8ff3-723247c31b7c | -9.1839 | -59.646801 | 2025-08-19 01:27:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c7b1184f-4ce5-33fa-906e-28aca5b1bbf2 | -9.1766 | -59.6171 | 2025-08-19 01:27:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4c65579-b0c8-3ca5-ba84-ad14818cbb0a | -7.7848 | -66.958603 | 2025-08-19 01:27:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 846b943d-83a0-352b-9daf-d63e0cec0d2e | -12.2288 | -64.237396 | 2025-08-19 01:27:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8f3178a6-3275-3552-8a42-18afc9644517 | -7.9349 | -63.2948 | 2025-08-19 01:27:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
