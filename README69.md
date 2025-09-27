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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f835fd8c-853e-3661-b635-aefb644bc31e | -14.8253 | -45.6282 | 2025-09-27 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 58637f0c-a308-32eb-9b3f-6d637d1ba65e | -20.7545 | -57.7845 | 2025-09-27 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.0 |
| 32a9a8b5-d97d-3745-ab3f-87b67106b098 | -11.385 | -44.9386 | 2025-09-27 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 8721f2a1-6674-3c31-b445-c1bae8856f56 | -7.798 | -46.9576 | 2025-09-27 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 235f1904-dddf-3056-ad84-6089009d6804 | -9.6159 | -47.5741 | 2025-09-27 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 178.5 |
| fe6570e2-1188-3639-8d71-791df0de67d2 | -10.2037 | -50.2254 | 2025-09-27 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 00bed401-020d-3a8a-8cb4-2678a22defb2 | -12.9722 | -46.2617 | 2025-09-27 14:20:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 35719f24-a6aa-3e4f-a969-eb960868ace8 | -9.9772 | -43.5962 | 2025-09-27 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 414.2 |
| 1c4c50a8-d2b1-3a59-bb8c-1b8556e2f0c5 | -20.5842 | -57.1587 | 2025-09-27 14:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 66.3 |
| eb94cb99-e7b3-3681-b1bd-f20c87f9949f | -9.9581 | -43.5987 | 2025-09-27 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 04f8afed-736f-346f-b31a-2d543459f32c | -5.407 | -42.2812 | 2025-09-27 14:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 9f3a51c8-faf9-37ed-a5ad-08756008ec84 | -12.9918 | -49.4448 | 2025-09-27 14:20:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 17c0dcd1-9605-35d4-a5d0-6ccf2725aea9 | -8.6328 | -44.848 | 2025-09-27 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| bf81be31-9d9e-3f47-8908-48b237ecbf42 | -11.4221 | -45.0025 | 2025-09-27 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 1cb7da86-908a-3141-a0f0-4f9b5fd24dac | -8.6631 | -43.991 | 2025-09-27 14:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| a222f6ed-4b9c-39fe-aac1-a65fd917f372 | -20.7131 | -57.8321 | 2025-09-27 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 5eb36a50-7d99-3098-8ba4-7b4e362cd92b | -14.85 | -45.3911 | 2025-09-27 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 9b3421d0-9f8f-3652-a49e-5d4cc775a853 | -11.3846 | -44.9618 | 2025-09-27 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| ad2a24b6-c8be-3e5b-aeed-bcf517544ed1 | -18.3247 | -57.0913 | 2025-09-27 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.1 |
| e5731957-63a1-3997-a2bd-71fe0ec1890b | -11.681 | -44.4312 | 2025-09-27 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 0f47331c-bb0d-37e9-8593-0395ccf58114 | -5.7588 | -42.7976 | 2025-09-27 14:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 72d6a85e-5abc-3198-baad-2dde631c3e25 | -9.3517 | -47.5801 | 2025-09-27 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 2b91fc30-e4af-3012-996d-b1248d677ef8 | -8.8415 | -46.2095 | 2025-09-27 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 457806e7-16ec-3854-91bf-e965f5f855b1 | -5.7227 | -42.6354 | 2025-09-27 14:20:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 128.9 |
| 8d95c611-60ad-368d-b9f7-af59f1964126 | -5.7585 | -42.8211 | 2025-09-27 14:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| 47bd35ac-a4d2-300c-a23c-9cb33a3b0559 | -10.4215 | -48.1234 | 2025-09-27 14:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d0578f64-192d-36d2-97dd-235aba7778e1 | -11.3642 | -45.0339 | 2025-09-27 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 191.0 |
| ee00c19a-2566-311a-8c59-ff8b2b0186b4 | -7.8637 | -44.5382 | 2025-09-27 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 5f14c576-5429-341a-96c5-cc61941b9f03 | -7.1383 | -45.5174 | 2025-09-27 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| a8adba0f-7d73-3b8f-a805-103d93ebaf15 | -4.7619 | -43.29 | 2025-09-27 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| b4223435-e0b1-396a-9fa0-d9713598a2c2 | -15.4328 | -48.2126 | 2025-09-27 14:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 27eaf78d-6f51-30e5-bde2-65983c4e1924 | -5.7413 | -42.6576 | 2025-09-27 14:20:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 185.3 |
| 5fe23ce7-8ad9-3b53-afd1-00c33ab07b46 | -6.7174 | -42.7393 | 2025-09-27 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| c8882627-af91-3817-89bd-cd6984a36b49 | -6.0593 | -44.7432 | 2025-09-27 14:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 767c28f7-c21a-38a3-b218-c9315fc64010 | -20.7342 | -57.7873 | 2025-09-27 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.9 |
| 71c91957-a17d-3164-93c1-c4e419a48214 | -3.0658 | -42.6781 | 2025-09-27 14:20:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| a667e975-5226-32e7-a1c7-959ca35c6eb6 | -3.8277 | -40.3373 | 2025-09-27 14:20:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 112.6 |
| 77ffab8d-2cbe-31eb-a559-ffb9fa9357ff | -9.3511 | -47.6243 | 2025-09-27 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| bb156b9c-1339-3b05-979f-e7873272913d | -5.7959 | -42.8417 | 2025-09-27 14:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 4520ff6e-14e9-3b99-a56e-668877a125ad | -5.7415 | -42.634 | 2025-09-27 14:20:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| d37f008a-a9a4-38a2-880d-d9f14dea1832 | -9.1753 | -46.6444 | 2025-09-27 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 0156edd0-ed03-36cb-97ab-9fc3fe3ed1ff | -12.0369 | -47.0543 | 2025-09-27 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7aa737a8-fa9d-3fc1-b82a-047753fd06c2 | -12.6498 | -48.1509 | 2025-09-27 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 36dbae35-e30d-3d1e-abcd-4c84c77e133e | -18.3049 | -57.0938 | 2025-09-27 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 245.9 |
| 53e85b6c-d9d8-313c-8be8-c213773d7a2e | -7.7558 | -47.3809 | 2025-09-27 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 4c228cae-b1f3-353f-aee4-8abd2bd6b4a1 | -7.6252 | -47.3261 | 2025-09-27 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| bf4f1dfd-32aa-3514-887f-5f127cbeb663 | -6.6983 | -42.7646 | 2025-09-27 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 136.8 |
| 1f10dcaa-2cd6-3886-bbc6-9987d3ece95f | -5.6813 | -43.0619 | 2025-09-27 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 300.7 |
| 426e354e-ee6b-3271-b947-b537e56ff93a | -10.2034 | -50.2468 | 2025-09-27 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 956ddb42-f485-36dc-b868-cfa34015f2d9 | -17.1739 | -56.3892 | 2025-09-27 14:20:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 5a7207be-2a1c-35c5-8837-d79a9adead8d | -10.4025 | -48.1256 | 2025-09-27 14:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| b007e21c-3a33-3d81-a026-359bf1feb4d6 | -6.2501 | -42.4736 | 2025-09-27 14:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 97.9 |
| c23c8976-c37b-3176-879e-dcc059eca976 | -17.1736 | -56.4099 | 2025-09-27 14:20:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 082f54eb-015d-3099-bee7-d5301474e85c | -11.6451 | -44.2966 | 2025-09-27 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| faea2bc8-0a7d-3bfe-a1f4-d253b167de0e | -12.8839 | -62.1256 | 2025-09-27 14:20:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| cfdea4c4-aa2c-3c08-82fc-683c887f4739 | -5.5335 | -42.8149 | 2025-09-27 14:20:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| faa2bbb4-af9e-3ec8-bb71-c08522f43d1a | -4.1759 | -44.2945 | 2025-09-27 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 2995fc4a-f36a-34b5-83b3-e0ed321eb8ce | -5.3693 | -42.3077 | 2025-09-27 14:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 135.5 |
| 2b2adf9e-d25b-3066-843b-906073e3acd4 | -7.3661 | -47.0173 | 2025-09-27 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| e6282156-6b1f-3974-9677-fad9a2f5b1bf | -15.8884 | -46.1944 | 2025-09-27 14:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 770eb479-8ff8-3dd0-846a-735eab287c9d | -5.8151 | -42.7931 | 2025-09-27 14:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 81d1dbde-5593-3654-92ca-fd2cd614eb06 | -8.822 | -46.2564 | 2025-09-27 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| b0986e4a-edb9-3f4f-959f-c0cd65834de4 | -9.3702 | -47.6002 | 2025-09-27 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 9fb1be41-6ba4-3149-8348-6aa01bbb6976 | -8.6442 | -43.9931 | 2025-09-27 14:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| f3612ab0-2ebe-3dd1-b0d6-26cdd01758e5 | -9.334 | -48.958 | 2025-09-27 14:20:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| e1de479b-814a-38c4-996a-73b20094fdf6 | -8.5221 | -44.6535 | 2025-09-27 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| e6b80ec5-bfac-30c4-a595-9c2d0965d265 | -12.6495 | -51.6797 | 2025-09-27 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 314.7 |
| 04f7ae04-fc17-38a5-862d-72af83481474 | -8.4827 | -47.8202 | 2025-09-27 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 184.4 |
| d48f162d-360a-374e-9c5e-91759966ab18 | -9.2871 | -48.2015 | 2025-09-27 14:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 552b38ff-ad52-35b8-9bc6-d5af3f204af7 | -11.4225 | -44.9794 | 2025-09-27 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 45b09409-c926-3fb2-b3ed-1dea91ebcadd | -14.0613 | -48.8321 | 2025-09-27 14:20:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 38.8 |
| cb5e6746-ab00-3689-8641-cd45574a655f | -9.3514 | -47.6022 | 2025-09-27 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 169.7 |
| a446e241-93f9-3bb4-bdcb-c4528260c02a | -7.7797 | -46.9149 | 2025-09-27 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| accd3c51-35de-3457-81c0-fd3c776c2a18 | -15.2136 | -56.0047 | 2025-09-27 14:20:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 9550c7bb-363f-3f57-8898-68ab73086ed7 | -9.4269 | -47.5943 | 2025-09-27 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 921d4b9a-252b-3a8c-9a25-4682dd92fbfa | -11.7006 | -44.4049 | 2025-09-27 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 8a865960-3891-3a9c-86a5-3de4c37c66af | -9.8781 | -47.7441 | 2025-09-27 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 801a9a2a-8578-380c-9aa6-eb47297da2f4 | -7.7609 | -46.9166 | 2025-09-27 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 44d1f9ec-a871-397f-a6bc-0d75270541cf | -7.7794 | -46.9371 | 2025-09-27 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 440.5 |
| 4d1882a6-0da1-39b8-a1a8-48ee5f0f8b2a | -11.3846 | -44.9618 | 2025-09-27 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| d7296953-dee5-36b2-ac6a-47d4dc6e9e56 | -8.6328 | -44.848 | 2025-09-27 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 5cee3f06-5188-3255-a68b-f9c76079b6d4 | -7.798 | -46.9576 | 2025-09-27 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 912eab07-8157-3e97-800a-e26f0c278cf6 | -20.5453 | -57.0802 | 2025-09-27 14:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 2f97eba5-fef7-3dde-80ca-dfff2c348d89 | -10.4215 | -48.1234 | 2025-09-27 14:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 343f62fc-c2e8-35fa-8685-62843c60064a | -9.0422 | -46.7255 | 2025-09-27 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| a10818e4-363d-3640-a8d6-a1b3b4c8b2e1 | -8.4827 | -47.8202 | 2025-09-27 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 273.8 |
| c0a9a481-ea8b-3851-85b2-b769e6a3e44e | -7.1383 | -45.5174 | 2025-09-27 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 43356635-d8b4-356d-915b-51abfe1a6327 | -3.8234 | -40.9955 | 2025-09-27 14:30:00 | GOES-19 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 99.8 |
| 6a8d72fe-d014-3e00-9b0f-df6a88ef3f3e | -7.7609 | -46.9166 | 2025-09-27 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 582c85cd-dbc5-3086-a181-a2c7f06713b4 | -8.8415 | -46.2095 | 2025-09-27 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 82174e6f-b4a7-3d42-9e08-fbd5836f49a3 | -10.222 | -50.2662 | 2025-09-27 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 379862c4-5cbf-33ad-b453-8d8f3c705507 | -5.7579 | -42.8917 | 2025-09-27 14:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| 38356320-c19a-3800-b5ac-57359bde93db | -6.6009 | -44.9053 | 2025-09-27 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 1622cd5f-1b51-36fd-b60a-f345a94d514d | -18.3049 | -57.0938 | 2025-09-27 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 251.5 |
| a5c14bc0-ee6a-393d-a0b3-dbce90caa237 | -12.3583 | -44.1386 | 2025-09-27 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 63153a0b-7de8-32d3-bc85-10a88a469a27 | -15.2136 | -56.0047 | 2025-09-27 14:30:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 77bef7b8-c589-3ef3-94ab-7331bd7c6c48 | -13.3375 | -47.3147 | 2025-09-27 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 63afa506-43ad-362a-8e9f-5051d804af18 | -20.5656 | -57.0773 | 2025-09-27 14:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 2a69412d-c03f-3fbf-870b-bb60e9304f7c | -11.4413 | -44.9998 | 2025-09-27 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 604.8 |
| f80877e8-7390-33f5-84b1-b82f59d7c49a | -9.334 | -48.958 | 2025-09-27 14:30:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |


[Clique aqui para ver as próximas entradas](README70.md)
