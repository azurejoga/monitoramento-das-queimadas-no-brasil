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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 408aab42-afb5-337e-aa3e-9fad9ae5e303 | -6.622 | -58.5965 | 2026-08-31 12:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 5f016dfc-47ad-324f-b786-33b93de9f501 | -6.9176 | -55.7166 | 2026-08-31 12:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| cc290727-66e4-3370-b1fd-6f2b87fd123e | -7.9236 | -44.2558 | 2026-08-31 12:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| baedfb1a-5886-32c6-8ebe-377095520539 | -18.2904 | -52.6818 | 2026-08-31 12:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 4f0b0fb7-d7c3-33f3-b45a-a81af2c85c94 | -6.6036 | -58.5972 | 2026-08-31 12:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 268.4 |
| e1847ffc-7036-3109-b5dc-6a288049ea3b | -14.4394 | -52.5176 | 2026-08-31 12:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| a1469bf0-cf24-3c11-b1fc-9b67c6f8738a | -11.3423 | -45.1982 | 2026-08-31 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 70ba1adc-9e91-319a-b513-5bf921dbb0a6 | -8.7439 | -46.4661 | 2026-08-31 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| b0a9a385-7cbb-3d8a-a00f-40e329256fc4 | -7.9608 | -44.2981 | 2026-08-31 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 594e07ad-d913-381f-bac2-cb9834ee4b1d | -6.1109 | -57.684 | 2026-08-31 12:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 7e6a3172-180b-3fd4-b969-115e582819ea | -6.1294 | -57.6833 | 2026-08-31 12:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 310bc04d-65b6-395a-9b34-197fd7bea8c9 | -19.1344 | -57.3797 | 2026-08-31 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 167.4 |
| 1bf795e3-b7af-3666-9daf-5c7cac668c6d | -18.2904 | -52.6818 | 2026-08-31 12:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 3d383c0d-9665-34ce-b488-48b146dde51f | -8.7439 | -46.4661 | 2026-08-31 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 3107fc3c-f95e-3abe-92ec-5166dc93ffea | -19.134 | -57.4005 | 2026-08-31 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 202.9 |
| 171c3c31-cbdd-3b89-87fc-f9eb8dcbc16b | -3.5345 | -49.4733 | 2026-08-31 12:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| e804c77d-4f4c-3e16-a24c-930e9f1625b5 | -19.154 | -57.3978 | 2026-08-31 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 193.1 |
| db33acef-5a5b-30ae-b7f8-765a70db5561 | -8.7442 | -46.4437 | 2026-08-31 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 8950c2a0-dcfe-317c-9bd8-9c48d9a81c95 | -6.9177 | -55.6967 | 2026-08-31 12:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| c29102bd-34ef-3234-a5e8-56a4540efdf6 | -18.2704 | -52.6851 | 2026-08-31 12:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 6eb4ffa4-b509-3751-b977-eb61867935a8 | -14.4201 | -52.5201 | 2026-08-31 12:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 98377909-3a6e-3872-b420-79aafbb45623 | -7.9239 | -44.2327 | 2026-08-31 12:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 4d8b5e99-b9a7-38f7-a158-d970bd245c8d | -6.9176 | -55.7166 | 2026-08-31 12:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 7208fc7d-b80e-3188-b712-72db4829591e | -11.5475 | -45.4906 | 2026-08-31 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| d3a97446-61d7-34e5-8321-47859aac36fb | -18.2899 | -52.7035 | 2026-08-31 12:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 70d3cacc-1b3d-31e1-8316-d0bf215fa3c4 | -5.2547 | -55.9105 | 2026-08-31 12:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| dd5e123a-8597-3f37-9478-d830b66a11a1 | -11.2482 | -45.1194 | 2026-08-31 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 46423a9d-16e5-3e45-8b27-07f16c02558c | -6.6035 | -58.6166 | 2026-08-31 12:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d6b33322-fee5-39e6-bdf1-460be5c167ce | -6.1109 | -57.684 | 2026-08-31 12:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 1b57f4b3-a7ef-3400-8099-c51a7d2b8f41 | -11.3423 | -45.1982 | 2026-08-31 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| e36cb9f8-b339-384d-a954-f46543978065 | -14.4394 | -52.5176 | 2026-08-31 12:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| e540acce-184b-365e-8081-6e53e89eb11a | -6.6036 | -58.5972 | 2026-08-31 12:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 301.6 |
| d8a10aa1-57f6-32b6-9b53-81c0dfefd92c | -6.622 | -58.5965 | 2026-08-31 12:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 166.8 |
| e7b1ded1-9f78-39d0-a3e0-e5fa13c32f16 | -18.27 | -52.7068 | 2026-08-31 12:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 127.4 |
| af898adf-036d-3d95-be8a-717fd92b2994 | -14.4007 | -52.5226 | 2026-08-31 12:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 3778f0d2-d90c-3b0c-8e9a-9956ec1041d2 | -6.1295 | -57.6637 | 2026-08-31 12:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 24206436-f7f2-3653-9346-73145064a269 | -11.3423 | -45.1982 | 2026-08-31 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 205.0 |
| b944c726-7f4d-3350-94c9-9dcdb3120d86 | -7.9236 | -44.2558 | 2026-08-31 12:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 86c4b381-a22a-378e-aaac-a94e36a70502 | -6.9176 | -55.7166 | 2026-08-31 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 3a6b6101-89fd-3bc9-91ff-0c685c184519 | -5.2547 | -55.9105 | 2026-08-31 12:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 8b792479-994a-32f3-ad0a-700677699925 | -11.5279 | -45.5162 | 2026-08-31 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 317864f3-b29c-3bf8-9877-d6aef0560890 | -11.3419 | -45.2212 | 2026-08-31 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| fba08c4e-e136-360b-8104-f6f38b60b3dd | -5.5831 | -60.2307 | 2026-08-31 12:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| c54e1553-1de7-38ec-a523-7c9d7a094a7a | -6.6036 | -58.5972 | 2026-08-31 12:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 394.8 |
| 74c3c403-5446-3803-b656-0549894df5af | -11.9378 | -45.0656 | 2026-08-31 12:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 8fec7229-de86-3450-870f-173de2e7ee3b | -3.5345 | -49.4733 | 2026-08-31 12:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 6a49347d-c5de-39e1-8f92-f2b8a334aa12 | -14.4201 | -52.5201 | 2026-08-31 12:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 20ef0697-0c8f-3aff-be95-7f8af37e03db | -11.2482 | -45.1194 | 2026-08-31 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| c8b494fb-bc3b-3d85-af9c-e06b9abc8cc2 | -19.154 | -57.3978 | 2026-08-31 12:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 209.6 |
| edb23788-7e28-3804-9a3a-3d84b20dabb2 | -7.3118 | -60.5897 | 2026-08-31 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| a6a65fc9-cd59-36da-970e-557b56db3931 | -9.5775 | -47.6224 | 2026-08-31 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 31c58c39-8806-3f45-8ccb-a00533e36763 | -11.3427 | -45.1751 | 2026-08-31 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 44b17941-1707-31bb-a4c6-2a2f283700b1 | -6.1294 | -57.6833 | 2026-08-31 12:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| bd260cfc-7637-35f4-957c-6b312f2d66ae | -9.8015 | -46.4629 | 2026-08-31 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 97f7924a-8a22-3658-ac7c-f733b051190f | -18.2704 | -52.6851 | 2026-08-31 12:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 26f0db10-ce7a-3f26-9136-7932a12400f5 | -7.9239 | -44.2327 | 2026-08-31 12:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| ddb248b9-c1ce-3512-8d74-f30305bc194c | -11.3767 | -45.423 | 2026-08-31 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 23bfd086-5c4b-3a00-b3cc-e159c8c2d3be | -8.7442 | -46.4437 | 2026-08-31 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| d9cc6649-2b45-31aa-8f19-b2285c3bc165 | -14.4007 | -52.5226 | 2026-08-31 12:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 17aeda57-d6ae-3457-bd70-a7009666773d | -11.5283 | -45.4933 | 2026-08-31 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 359f0a51-91cf-3884-a174-f660ad6f5a0c | -10.1531 | -45.7438 | 2026-08-31 12:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 7f2e776d-bbe0-3f98-8424-d5c59117d32e | -18.2899 | -52.7035 | 2026-08-31 12:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| af74f616-0f99-30cb-a84b-6b04a324274a | -6.9177 | -55.6967 | 2026-08-31 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 6531566f-eed5-3d35-aa7c-bdd29e543d10 | -14.4394 | -52.5176 | 2026-08-31 12:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 7b114bfe-1bd3-3a3f-9607-a77f10a0c6a3 | -18.2904 | -52.6818 | 2026-08-31 12:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 129.8 |
| c9c78868-cc4f-34b6-ab67-51e7256139ca | -19.1344 | -57.3797 | 2026-08-31 12:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 452.5 |
| 1cd3e810-c735-3146-bc0a-3fbb2e157613 | -10.7407 | -54.0401 | 2026-08-31 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 45f7ec86-8460-3198-b260-d6f55f23060d | -11.5475 | -45.4906 | 2026-08-31 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 8847714d-842d-3da4-80b3-08d7df532131 | -10.1535 | -45.721 | 2026-08-31 12:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 201.4 |
| 0f919fda-c7a4-3ab0-9a62-3d7e17c95332 | -11.3232 | -45.2009 | 2026-08-31 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 116dfa52-36b3-3203-ab4d-211e700a911b | -19.134 | -57.4005 | 2026-08-31 12:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 410.8 |
| baa58cbc-c690-369c-bbd0-ccfedde82062 | -9.8018 | -46.4405 | 2026-08-31 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| eb107423-29a3-3c59-bcfe-ea7dffd0f0b9 | -11.229 | -45.1221 | 2026-08-31 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| bff1682c-c7bb-31d3-87b1-b61b1c40ebf9 | -11.3615 | -45.1955 | 2026-08-31 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 6d5c40db-eacd-3397-8012-17be29123607 | -6.6035 | -58.6166 | 2026-08-31 12:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| ac037d03-14f5-370c-9ade-4660568feeab | -18.27 | -52.7068 | 2026-08-31 12:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 152.6 |
| cb964acf-1409-31a2-9220-e9d508e0326e | -10.7459 | -47.9757 | 2026-08-31 12:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 7f1809c5-77c2-330c-8929-66690440191d | -8.7439 | -46.4661 | 2026-08-31 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 997252f3-4066-3832-8edd-e3e868e79712 | -6.9176 | -55.7166 | 2026-08-31 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| bd1639fd-1330-3bbd-962d-86e8dfc60448 | -9.4156 | -45.6499 | 2026-08-31 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| fc3e533b-5978-37b0-a4e9-aa82d129ccc8 | -6.622 | -58.5965 | 2026-08-31 12:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 4a24fc8f-3792-321b-ac00-887a3ca5110e | -18.2904 | -52.6818 | 2026-08-31 12:50:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 55f912b9-a0ad-3b66-b20d-0d14d088cfcc | -7.3118 | -60.5897 | 2026-08-31 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| bb2cdb31-92ed-375c-8116-b67d3dd5dd75 | -6.9177 | -55.6967 | 2026-08-31 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 9eddcdb0-5b50-3dfd-9ec9-692d160e3a70 | -5.5647 | -60.2312 | 2026-08-31 12:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 5ca4b64f-699f-3a41-85df-472f486e6be8 | -11.5475 | -45.4906 | 2026-08-31 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 19e57f33-1b22-334f-a160-cc96a3187c90 | -18.2899 | -52.7035 | 2026-08-31 12:50:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 82.2 |
| cf53717c-d47a-314a-847e-58bbafe148a8 | -18.2704 | -52.6851 | 2026-08-31 12:50:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 4e6ee68c-5c60-389f-b929-65e61a958a16 | -14.4201 | -52.5201 | 2026-08-31 12:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 87b229b1-d1b1-36df-ada0-9f59b8833e62 | -11.1634 | -50.5727 | 2026-08-31 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 7e303952-a294-3af2-9ad3-ab738426c08a | -11.9378 | -45.0656 | 2026-08-31 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 31a88b41-08dd-3c4b-8239-f3adcbae73ef | -8.7442 | -46.4437 | 2026-08-31 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 96e5d189-d982-3457-a25c-9050341b8493 | -19.1344 | -57.3797 | 2026-08-31 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.5 |
| 428ec0e7-1488-37d4-927f-bbdf9e7ce3ad | -6.1294 | -57.6833 | 2026-08-31 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 1b9441ef-a601-3596-b629-b3935e50a82c | -11.3575 | -45.4257 | 2026-08-31 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 24a79526-984a-32c3-904b-7db9e672d148 | -10.1535 | -45.721 | 2026-08-31 12:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 1f27ae74-ade7-36f6-8d7d-f617c7a4f77b | -10.7596 | -54.0384 | 2026-08-31 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 4f923aad-f0d8-36dc-a1bd-9b5e10eecabc | -11.3419 | -45.2212 | 2026-08-31 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 12db9746-ff5e-3c55-99c4-8818b12a34c4 | -9.5775 | -47.6224 | 2026-08-31 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 2dcb58a9-515e-30c4-bb8e-014c98b27624 | -19.134 | -57.4005 | 2026-08-31 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.0 |


[Clique aqui para ver as próximas entradas](README85.md)
