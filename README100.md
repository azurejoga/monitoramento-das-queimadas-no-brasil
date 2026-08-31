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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 053b6043-0632-38f4-b1d3-ee604ff59239 | -14.5674 | -54.1176 | 2026-08-31 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 131.7 |
| a9ee3b33-6b81-3caf-ac09-c589f5a6a2fd | -10.1087 | -50.2776 | 2026-08-31 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| ffad8a59-0c9c-3052-b578-4cab1250ccc9 | -6.2469 | -53.6826 | 2026-08-31 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 4aad7525-51db-3230-a130-5cf02e5a95ea | -7.6253 | -55.2787 | 2026-08-31 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 815fcc58-5573-3e65-b8c7-2420573e77f6 | -9.5964 | -47.6204 | 2026-08-31 15:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 240.8 |
| 86705ed3-82f8-3b52-9ba3-4cbcfc108173 | -10.1084 | -50.299 | 2026-08-31 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 301.3 |
| c137d834-4deb-3619-aac8-2c516097ac38 | -11.1913 | -51.292 | 2026-08-31 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| ce78f77d-1801-31f5-93e2-1c42c1564496 | -13.8384 | -54.0158 | 2026-08-31 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| bec5a83e-b922-322e-9663-43a4825fb9fe | -5.5647 | -60.2312 | 2026-08-31 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 32ee4a93-1373-36b0-b4cf-4b597ed6bc2c | -2.6741 | -59.382 | 2026-08-31 15:20:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| f3c8f170-43ef-37f4-8ee6-f0bfdd1ec99a | -15.2669 | -53.8851 | 2026-08-31 15:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 16c7e3bb-699e-3b0e-b181-d5857c68a756 | -11.3611 | -45.2185 | 2026-08-31 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| f5440bae-0997-34e5-9e0e-cc9cfac6fb5e | -9.6942 | -65.0582 | 2026-08-31 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 49be44d4-3ffc-3e20-beb2-618bc5c33bb7 | -3.4185 | -61.3273 | 2026-08-31 15:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b8c16c55-1d75-39c3-ac69-a13e5377fe0c | -12.9032 | -45.8382 | 2026-08-31 15:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 2889dabb-45c2-3491-a7d5-b186cc1638a1 | -9.8927 | -60.2752 | 2026-08-31 15:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 40d8fa6a-59ad-3d5d-8a55-ae01915cc315 | -7.0057 | -59.2575 | 2026-08-31 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 96b8a1b1-516a-3c52-8368-6fe27a60cc5f | -9.4758 | -48.1822 | 2026-08-31 15:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 5d133c5f-0247-3854-b6a0-fb990c89228b | -10.5607 | -50.3595 | 2026-08-31 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| cb3e4afd-5e5f-3c24-9c42-ad50a199a46e | -7.9239 | -44.2327 | 2026-08-31 15:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 584.6 |
| 834a8bb0-3be3-38ee-b8ec-faa4cf64bf1d | -13.4707 | -57.0574 | 2026-08-31 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 6fb3eda8-429c-3c30-9d1c-083befafeaa3 | -2.6741 | -59.3628 | 2026-08-31 15:20:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 1614e147-d2a1-32c5-86dd-fea321fbb4b2 | -13.8563 | -54.0967 | 2026-08-31 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 147.5 |
| b8c6d00c-7756-3201-b755-b530ae22cd84 | -10.7598 | -54.0179 | 2026-08-31 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 327e3f54-92dc-3cf8-a4d4-9c598f4cbe82 | -10.5601 | -50.4022 | 2026-08-31 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 149a6315-cc23-3eea-86b9-2b6ff6578c72 | -5.5831 | -60.2307 | 2026-08-31 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 56e999cf-0f5e-3344-a64a-bd49d3a59f1d | -11.3802 | -45.2158 | 2026-08-31 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 8c6e64a6-2c75-37ac-b400-4be1062cfb62 | -8.7439 | -46.4661 | 2026-08-31 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| fbb20c1f-3a83-3a6f-a1db-e919ae031f44 | -11.1821 | -50.592 | 2026-08-31 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 062c7faf-d246-3d02-bee6-f299fad354c1 | -5.4876 | -57.1416 | 2026-08-31 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| f9322668-cf8c-3186-8696-207dc29f8c37 | -6.1295 | -57.6637 | 2026-08-31 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 57d2adf1-5fc3-34c4-bf9d-9400959bb57e | -8.6154 | -54.7945 | 2026-08-31 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a67bc1f0-bb18-37de-b343-0eb2928dd7b1 | -11.2503 | -54.0146 | 2026-08-31 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 4bcb0dc6-da3e-3962-b6db-58bb9a2b69a3 | -5.9451 | -57.6906 | 2026-08-31 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 3386bb1e-4cff-3d3d-93eb-b8286266aa20 | -11.1732 | -45.0378 | 2026-08-31 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 31361118-ff8e-3457-b23f-d4ea43fc9f5c | -6.9368 | -55.6161 | 2026-08-31 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 30c503f1-29bb-341c-a80c-2dda59be9a1e | -10.3205 | -49.9567 | 2026-08-31 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| c8d2928b-fa41-39c3-8ba7-7201cd6dae1e | -5.8873 | -52.1477 | 2026-08-31 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| cf1f40b7-92e8-383b-a788-fa5de4f06373 | -3.6076 | -59.0769 | 2026-08-31 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 104.1 |
| b3fc2388-fe8b-375d-bce1-4345e8b5ee44 | -18.2695 | -52.7284 | 2026-08-31 15:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 9bb28268-6852-37f0-b4fe-974d8102ece5 | -10.5793 | -50.3789 | 2026-08-31 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 30b53bec-16c9-3176-a5b4-d38590014bf1 | -7.9425 | -44.2538 | 2026-08-31 15:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 195.3 |
| 721da126-1479-32c0-bcb8-23da08c0a922 | -10.7593 | -54.0589 | 2026-08-31 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 23db8ba7-4eb8-3eb7-80d2-95b1855aa2d6 | -10.8218 | -50.6306 | 2026-08-31 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 26171363-00ab-32fa-bb11-16f7748e8c9a | -11.2125 | -54.0181 | 2026-08-31 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| dc264720-2f73-3d48-818d-a0c56576e825 | -6.1109 | -57.684 | 2026-08-31 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 241.5 |
| 87851663-91a6-3644-988a-d64fbc25f1fb | -14.5868 | -54.1153 | 2026-08-31 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 154.1 |
| a7905baf-d377-3370-a1fc-902b1c094c96 | -10.8804 | -50.4965 | 2026-08-31 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 64d1f2af-15cf-3583-855b-e23bd8193a60 | -14.5871 | -54.0944 | 2026-08-31 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 8a5c824e-1111-3f24-a867-3cb2ff68ceaa | -11.2294 | -45.099 | 2026-08-31 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 4f3de5d2-405a-3b92-b082-db01639d367b | -10.8046 | -50.5046 | 2026-08-31 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 2a2af5f2-99da-39ab-a44e-72fa03ff406f | -10.8043 | -50.5259 | 2026-08-31 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| f0cdddce-66b9-3ff1-a1d3-321976deac8f | -3.6215 | -60.566 | 2026-08-31 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 185.6 |
| 026d0ae5-1e12-3f98-90b0-d4269e7f2f6a | -8.7989 | -62.5095 | 2026-08-31 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 110.2 |
| b0baf51a-8876-3d6f-bee7-4f64a87d48d4 | -7.9608 | -44.2981 | 2026-08-31 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 8942539c-935c-3f20-a92c-2ce66ed2389f | -10.1531 | -45.7438 | 2026-08-31 15:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 114.8 |
| b7426945-cc45-3c5a-969a-7d26ad170b6e | -7.9605 | -44.3212 | 2026-08-31 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 7885c442-f61f-3a4c-ac97-220dfc648bfb | -11.3431 | -45.1521 | 2026-08-31 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 9f58f12e-774c-3b34-a8f0-e49194095b79 | -7.5659 | -61.362 | 2026-08-31 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| fd75b115-78ea-3670-a91a-2a5a99e9abd7 | -12.0925 | -47.1587 | 2026-08-31 15:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 0de5366d-8b38-302d-a736-d5ce93aa245a | -14.5678 | -54.0968 | 2026-08-31 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| f8d0361a-d1cd-305e-9ef1-067b42f825a7 | -18.2904 | -52.6818 | 2026-08-31 15:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 101.3 |
| f4d652d5-72f0-3c0e-b7d0-820999264a4c | -10.8444 | -45.3126 | 2026-08-31 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| ba265707-6b04-3852-b0b6-2c1b80d0d9ca | -2.6559 | -59.3631 | 2026-08-31 15:20:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 3ed2f513-4da2-3b7b-8000-5bcb79b92fac | -11.1818 | -50.6133 | 2026-08-31 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 64827b68-903e-3029-bf1b-dd4a7887f881 | -7.9236 | -44.2558 | 2026-08-31 15:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 294.7 |
| b658690f-0ff8-31ba-afe9-5ea88da2b518 | -10.8614 | -50.4985 | 2026-08-31 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 4c12c4b5-6875-39b0-bfd7-2059894fdc7b | -5.2362 | -55.9112 | 2026-08-31 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 55424e03-e35e-3f37-8b6e-cc98ad609d33 | -10.7405 | -54.0606 | 2026-08-31 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| b367ecc4-536d-3bb4-a404-3e74c2a79733 | -11.6786 | -54.5484 | 2026-08-31 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 36b3fc8c-da3d-306e-9a1d-c03aa0b712dd | -10.7428 | -50.8727 | 2026-08-31 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| aff1cd85-741c-33c6-826f-86eb0f3e7f7b | -13.4899 | -57.0556 | 2026-08-31 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 7b85ba10-87a9-3cfe-88c5-2021395fae52 | -11.3615 | -45.1955 | 2026-08-31 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 206.7 |
| b8377b5f-7903-3da9-801c-b87f36ea75d6 | -8.7442 | -46.4437 | 2026-08-31 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| ecb93b6a-daed-3946-b0a9-9ce0db454ab8 | -5.2548 | -55.8907 | 2026-08-31 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 6927fb03-996f-30e5-837f-86334dad9f60 | -6.912 | -59.4927 | 2026-08-31 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f75e5a63-ac2f-3d9d-8535-c3466cbc4f52 | -8.7631 | -46.4418 | 2026-08-31 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 170.5 |
| f554693e-99ee-3047-a68d-2edd53f55379 | -11.8408 | -50.9874 | 2026-08-31 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 5a22ddbd-f9be-3d18-a2fb-43261c857c0b | -11.3427 | -45.1751 | 2026-08-31 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 3ceccf6b-f3e0-3c96-b9df-cdd85488ce88 | -7.9907 | -46.5177 | 2026-08-31 15:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 268.2 |
| 86001a81-e922-3984-b26a-ed0db21d6192 | -15.2475 | -53.8876 | 2026-08-31 15:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| cc62d06b-ea60-3f0c-8c80-304a6d9f5a89 | -15.2275 | -56.3716 | 2026-08-31 15:20:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| a18e6476-c29c-3281-aaf9-ddb6d5a36e38 | -6.7514 | -55.6654 | 2026-08-31 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 50c9daac-b65a-381f-a24e-1261c23163ee | -7.2933 | -60.5905 | 2026-08-31 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 228d26de-64e1-31fd-850e-57c906faff08 | -3.4185 | -61.3273 | 2026-08-31 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 8f3b9b5f-542c-3ba4-b6db-6664a52b8ec0 | -8.631 | -66.5473 | 2026-08-31 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| a7f9fbc9-9557-3939-a77b-e1684b8c3fcf | -3.9707 | -60.0258 | 2026-08-31 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 5b65a8e9-7caf-3a67-92eb-c3439388ed51 | -13.8384 | -54.0158 | 2026-08-31 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 66739aeb-e702-3b39-9bfc-8ff1c7b617e4 | -7.3476 | -55.1945 | 2026-08-31 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| fedad58a-adfa-3711-8ce4-7ca223464f7c | -13.8563 | -54.0967 | 2026-08-31 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 5a539189-9b3b-37d6-a067-24ead2bea713 | -10.8212 | -50.6732 | 2026-08-31 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| b7a8fa0c-2cfd-3064-b746-99d75d3d94fd | -10.5601 | -50.4022 | 2026-08-31 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| aa37affc-24b8-3e8a-8b21-d33d4adedba2 | -10.8614 | -50.4985 | 2026-08-31 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 340bdbcf-2379-373f-9166-3145cb7002d7 | -6.2469 | -53.6826 | 2026-08-31 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| cfc0deb8-a6a1-3798-83e7-087dfafb566d | -15.4231 | -52.7049 | 2026-08-31 15:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 540324db-27eb-3c19-b612-beee93f3e379 | -6.8751 | -56.5116 | 2026-08-31 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 42775a80-0d55-38aa-8f36-9d57608c1c73 | -13.9282 | -54.42 | 2026-08-31 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 14e64936-30ed-3596-8412-ad853be83793 | -6.1295 | -57.6637 | 2026-08-31 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 0c84e330-ff24-323b-adac-8925536013a1 | -11.1922 | -51.2284 | 2026-08-31 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 57b56238-0325-312e-91f7-bceb5844f01c | -10.7856 | -50.5066 | 2026-08-31 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |


[Clique aqui para ver as próximas entradas](README101.md)
