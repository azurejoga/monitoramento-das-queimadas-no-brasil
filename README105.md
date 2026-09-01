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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6606fc04-c94d-3c9d-ae5e-6043d3c1c954 | -8.163 | -55.4266 | 2026-09-01 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| c5cdab33-d749-353f-82d0-6e500ecf9d46 | -6.6542 | -59.426 | 2026-09-01 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.3 |
| a41c7a3b-726e-388e-ab9e-98f3c346e75c | -11.7216 | -47.6327 | 2026-09-01 15:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| cb4b43ce-e3a2-3acf-971e-6b65a6f06290 | -8.7628 | -46.4642 | 2026-09-01 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| d98b718c-65ff-372f-b9fe-7d25097da973 | -11.5475 | -45.4906 | 2026-09-01 15:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| c570fccf-b15a-325c-b055-f2741717a735 | -7.3488 | -60.5691 | 2026-09-01 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| c2823678-6cab-3e64-94eb-66892f32a6fd | -10.7856 | -50.5066 | 2026-09-01 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 44d6e112-e395-316d-b582-d47e37775713 | -6.8008 | -59.5934 | 2026-09-01 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| b8cc290d-ad29-371b-944e-d6d343503ed3 | -5.5648 | -60.2121 | 2026-09-01 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| e600cfa5-814c-325a-aedb-f3afc40cc06e | -6.8192 | -59.5927 | 2026-09-01 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| b17b523a-9b37-3e18-867e-74fcd0e3e705 | -5.5833 | -60.1924 | 2026-09-01 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 693fa4fb-98e8-313f-a32d-a704f1c5e77c | -3.4185 | -61.3461 | 2026-09-01 15:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 96cfdde4-ab4c-3a72-86a0-225a8d3502e7 | -8.499 | -55.3051 | 2026-09-01 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 05947077-470c-32ff-bebe-305acfd55f81 | -6.6541 | -59.4452 | 2026-09-01 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 6413a08c-cb7d-343a-b317-e070fd82f3ce | -7.1167 | -45.7898 | 2026-09-01 15:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 277cbcfa-c001-3903-91b1-f31fe00c5d70 | -7.571 | -60.4643 | 2026-09-01 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 02fa220b-cc30-3d27-ab98-bc4f10165f37 | -14.9386 | -56.3216 | 2026-09-01 15:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| a33beb56-6f2e-37ce-88a8-f4eb215bb993 | -14.4831 | -52.2151 | 2026-09-01 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 135.3 |
| fbfedd0d-1668-3599-bfc6-1d720ed49c0a | -12.3814 | -48.1655 | 2026-09-01 15:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 3bc788ec-60e8-3740-973c-1252bee5a892 | -8.2229 | -54.9412 | 2026-09-01 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 8348b767-08c8-3f25-8fc3-072d36c011a2 | -11.2673 | -45.1167 | 2026-09-01 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 684b1266-e814-3fa2-bfcb-e7d8c7c7f8af | -7.5289 | -61.3825 | 2026-09-01 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b2e52ff2-83d8-346a-a481-7b0799996b0c | -8.5792 | -54.6758 | 2026-09-01 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 19f0b9d8-c757-3a00-9cb2-fde5ae030420 | -10.8627 | -45.356 | 2026-09-01 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 0fe45705-5a2a-3b46-8e4b-87a290faddf6 | -3.2623 | -58.2367 | 2026-09-01 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 217.3 |
| 51b52b59-b0a4-3beb-9f8f-c8f9024994bc | -7.2934 | -60.5713 | 2026-09-01 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| af10a300-cf49-338e-836a-51675855fc63 | -8.4046 | -44.9869 | 2026-09-01 15:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| a6a2f7e2-3bc1-3448-8eb9-49d25e071eb3 | -6.8009 | -59.5742 | 2026-09-01 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 1d4db303-b7ed-3ed0-9af7-67b6c0251613 | -10.3764 | -50.0152 | 2026-09-01 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 3e8c89ad-724c-30a4-8358-00ededbedcb2 | -10.3577 | -49.9957 | 2026-09-01 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 450.6 |
| 0fbbc3a0-1b63-3e65-8ac5-a5400f5963c7 | -13.0897 | -45.163 | 2026-09-01 15:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 3186e55e-0db5-329d-a32a-c7fdb131a77d | -7.4549 | -61.4044 | 2026-09-01 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 8959b13f-9df5-3014-9622-4c3d89533536 | -3.6215 | -60.566 | 2026-09-01 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 121.8 |
| d5ffc262-f65c-3c62-8cbc-d7e27561b5a6 | -16.1523 | -46.6749 | 2026-09-01 15:00:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 733cc107-2b42-3fd5-8e89-4891c96712e3 | -12.1457 | -44.196 | 2026-09-01 15:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 4a53d4b7-587e-3dcb-b2d5-65fc1b1b1008 | -3.5162 | -59.0405 | 2026-09-01 15:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 5a6f5358-e806-3bba-ab3f-b8183c3220b7 | -13.4691 | -51.8776 | 2026-09-01 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 3092daff-8e49-33de-a720-9ecae2509143 | -13.3943 | -51.7595 | 2026-09-01 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 87c6f7f6-0e08-3820-a033-c506bdf2596d | -6.6727 | -59.4252 | 2026-09-01 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 6d105c19-8cd8-35a7-85bb-e28c9cbaa4c3 | -5.5649 | -60.193 | 2026-09-01 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d9f72bb9-c54d-32b0-a748-6c61c264e8e0 | -3.6398 | -60.5656 | 2026-09-01 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 1180e37e-0248-35c5-9fc6-d6a46dfe536b | -12.9032 | -45.8382 | 2026-09-01 15:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 347.3 |
| d2b25ab0-03f0-3ef9-9895-898004c41ed0 | -10.7409 | -54.0196 | 2026-09-01 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 40279315-edad-3465-9952-f06a0939f70c | -11.0623 | -49.6829 | 2026-09-01 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| b3f7f748-03d7-3830-9e7b-aea2f0a83f1d | -14.6535 | -53.5642 | 2026-09-01 15:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| e647bed1-7878-3b9c-ab10-b88c6be67771 | -11.3044 | -45.1805 | 2026-09-01 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 63a3bc91-22be-3106-97f2-832d922ee221 | -6.7692 | -58.6679 | 2026-09-01 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 8da1a30c-a0dc-3814-9e39-ba9b570383fe | -10.7274 | -50.6192 | 2026-09-01 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 2a295bad-a7b9-3c20-9b3a-badb5f3b0641 | -7.5259 | -44.4565 | 2026-09-01 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 665d0929-df65-3c90-bf1d-76e1152a9e83 | -4.1515 | -60.7068 | 2026-09-01 15:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| b7b54652-05a0-3521-b4f2-8a072b8cabab | -4.181 | -63.1543 | 2026-09-01 15:00:00 | GOES-19 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 269.8 |
| 03255701-7914-39c8-9c0a-ad31f056a22b | -13.3374 | -51.7241 | 2026-09-01 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 00829835-09d2-33b6-8449-4d633ca80e0f | -11.0623 | -49.6829 | 2026-09-01 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 5386e1d9-9d73-341d-a325-f5a803c8334e | -13.4707 | -57.0574 | 2026-09-01 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| a1891e82-9ccf-3a00-8545-9aaae9c05bf5 | -10.7409 | -54.0196 | 2026-09-01 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| d810afa2-b1d9-3f08-a795-0909a7e0f9c7 | -14.4587 | -52.5151 | 2026-09-01 15:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 028017a7-b7be-3b1d-8b51-cca1a712b98e | -10.3764 | -50.0152 | 2026-09-01 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 90b3ab94-8685-31f5-bd7f-c98a7ee8e121 | -13.4516 | -57.0592 | 2026-09-01 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 116.6 |
| aa6a357c-b66f-3271-80ac-9b0d365c7da8 | -8.499 | -55.3051 | 2026-09-01 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 3a50d6cb-8425-3155-9c0d-436613bc4fbb | -11.6649 | -47.5957 | 2026-09-01 15:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 2e0bea70-be8d-31c1-8a18-49440e5abf11 | -11.6972 | -54.5672 | 2026-09-01 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 60492405-fafe-3cea-b992-cf21ee538e6e | -6.7514 | -55.6654 | 2026-09-01 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 28f9273c-09fb-3e96-997d-8fa321b5c7aa | -10.7271 | -50.6405 | 2026-09-01 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 902072b0-9741-39cd-925c-655376bde8cc | -11.2954 | -50.6222 | 2026-09-01 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 778ae7e1-34de-3a2d-be70-c5421afed032 | -7.3488 | -60.5691 | 2026-09-01 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| bbad3574-fe5a-3507-b28b-ddad232fae3e | -8.5971 | -54.7553 | 2026-09-01 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 6898c0dd-5c92-3c28-85bf-3373bbddc568 | -9.1719 | -51.5476 | 2026-09-01 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| eeac74f7-1f59-33f2-94a4-b2f89274f54c | -9.9516 | -53.9844 | 2026-09-01 15:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| f1fd00c9-4eb8-3bfe-ace4-5bd40e9bfec3 | -17.1351 | -46.8284 | 2026-09-01 15:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 86443552-7a4d-3f52-bee7-26cd75fafdff | -11.2482 | -45.1194 | 2026-09-01 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 76473fc1-e78c-329a-bd76-edb06749ed28 | -12.0912 | -45.0656 | 2026-09-01 15:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| d901bd7e-7f6c-3ffa-812f-4b8ae51d66da | -7.5289 | -61.3825 | 2026-09-01 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| bb9a412e-600e-3a05-bf2e-533fe9fe2c05 | -8.4046 | -44.9869 | 2026-09-01 15:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 7d93680c-05a5-3f13-849f-bd62e38a5aeb | -3.79 | -59.3031 | 2026-09-01 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| bf7adfde-98e2-3a76-a761-8ace8fbc707f | -5.5649 | -60.193 | 2026-09-01 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 7c78d6f1-38bc-3603-96d9-b615f50268aa | -17.1146 | -46.8556 | 2026-09-01 15:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 6fbfe013-6f80-3d3e-be4f-0fccfc0f4098 | -11.2478 | -45.1425 | 2026-09-01 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 638ceac1-eac8-33f6-94e8-cf1e83ba4c32 | -8.7628 | -46.4642 | 2026-09-01 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 5eff217a-e775-34a8-ac50-85c709003fe4 | -7.2006 | -60.6706 | 2026-09-01 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 247.3 |
| f6fa2902-c704-3338-bbc2-5b6e0073b65b | -5.5648 | -60.2121 | 2026-09-01 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 7ade40f1-16d7-3ee8-8187-f9b779323bed | -3.5162 | -59.0405 | 2026-09-01 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 54cb77ec-0dce-319d-8c6f-ca0a6953baaf | -11.2764 | -50.6243 | 2026-09-01 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 2b51c6ab-4892-3410-998f-64acb9974408 | -3.4185 | -61.3461 | 2026-09-01 15:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 22891bfa-89ea-3760-81c8-35e98863ec66 | -14.9193 | -56.3237 | 2026-09-01 15:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 4cc5b241-c7b5-3b9b-9248-2eb3bb68111b | -1.4394 | -54.2369 | 2026-09-01 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 7f143ea1-2903-3a58-a9e8-ce86c0078e6c | -10.7274 | -50.6192 | 2026-09-01 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 22e66680-3179-3b7f-8fd5-23dca10d0f1b | -11.2957 | -50.6008 | 2026-09-01 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 5d07a2c3-bbc4-3967-b93b-1f99db9fa284 | -13.9474 | -54.4179 | 2026-09-01 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 8026b56a-5f68-39ba-ab39-a94d990a31e3 | -15.4429 | -52.681 | 2026-09-01 15:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 136.6 |
| c08e3521-6279-3a46-be3a-05174a0d9abb | -8.7768 | -45.3803 | 2026-09-01 15:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| c691d670-0132-32bd-b79e-2cfce39bb87b | -11.2439 | -45.3727 | 2026-09-01 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| e865261f-6adf-39ce-8e88-69e831fa7eec | -13.967 | -54.395 | 2026-09-01 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 448.5 |
| 176244cc-bcc0-385a-bdaa-50cde0bf8fb2 | -12.1457 | -44.196 | 2026-09-01 15:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 83d55a5f-5e2f-3d48-b2c0-48b1fff7a280 | -16.1523 | -46.6749 | 2026-09-01 15:10:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 192.3 |
| b0a5f599-9733-3cd1-87fb-ced4351d0c09 | -7.5526 | -60.4651 | 2026-09-01 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 8a7af3fb-f5a2-359f-bf4d-19da3bda60e6 | -11.7973 | -47.6672 | 2026-09-01 15:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 29c8ff91-38be-3f6a-aeca-ebd1cc5fe7b6 | -6.7123 | -58.9412 | 2026-09-01 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| eb35db30-4608-3b4c-aac1-9b9da24926cf | -13.9477 | -54.3971 | 2026-09-01 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 223.6 |
| 9b372344-8ce4-305f-8ca3-6be06c8ffb80 | -11.2298 | -51.2456 | 2026-09-01 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 802f79e4-1bf8-332f-be42-c4db1723a1ec | -13.9667 | -54.4157 | 2026-09-01 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |


[Clique aqui para ver as próximas entradas](README106.md)
