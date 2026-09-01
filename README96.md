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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6fa4e1f-47b5-3139-adff-fdced77fa239 | -10.7856 | -50.5066 | 2026-09-01 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 5775a5d0-9dce-311b-b047-b6235d773294 | -6.9552 | -55.635 | 2026-09-01 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 5a41cf7f-6307-3949-bc47-99403ca3528a | -11.0928 | -51.5767 | 2026-09-01 13:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 84ceecc9-ebf5-3066-8eb1-b36c33fe80fe | -8.2788 | -54.9376 | 2026-09-01 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 178.5 |
| a284ba91-0fb6-32d5-9756-6fc701d87d6e | -10.1542 | -45.6755 | 2026-09-01 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 4bfb2cb6-c0de-340b-91cb-a6884ace20f7 | -3.1083 | -61.238 | 2026-09-01 13:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| f4478420-6dbc-3dbb-96c5-7ab3bd02aa1a | -14.5214 | -52.2313 | 2026-09-01 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 12d7b658-b1ae-331b-97ce-82ee08b1f94a | -10.696 | -46.2646 | 2026-09-01 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 47b599c2-bbad-38e2-bfdc-59f9f2b7fb92 | -12.9589 | -45.944 | 2026-09-01 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| d6dad090-7d0c-3fb2-b7ce-9d292d0d24b6 | -7.571 | -60.4643 | 2026-09-01 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| db8041f3-7a93-390e-9aeb-0bc1441a4665 | -8.2602 | -54.9388 | 2026-09-01 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 0bd6d733-96ee-3692-9534-d1210767b43c | -12.9225 | -45.8352 | 2026-09-01 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 017032de-7615-3739-a015-dac029f14379 | -11.2673 | -45.1167 | 2026-09-01 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| c1f1920b-e882-30f6-ac59-5f36c4ecdcd8 | -14.6732 | -53.5408 | 2026-09-01 13:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 1555b03f-40bb-3f55-a4db-306c257a7a68 | -7.9048 | -44.2577 | 2026-09-01 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 1c6c8be1-fe68-3cb0-a084-bd92379553b1 | -8.5214 | -54.8814 | 2026-09-01 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c977dcfd-4a9c-3947-b241-633409b7f9d3 | -7.5709 | -60.4835 | 2026-09-01 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| d14678f5-2a8c-39b4-9998-41ac41abf6f4 | -7.3487 | -60.5883 | 2026-09-01 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 5a9a2b59-007f-31ff-b7f1-9c522e4d3aa2 | -13.0897 | -45.163 | 2026-09-01 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| ac7551e1-d259-383c-af93-64a77d3582cc | -6.6542 | -59.426 | 2026-09-01 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 63822c84-0885-3448-874c-5dca48ba4850 | -6.8193 | -59.5734 | 2026-09-01 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e6b76d4d-8846-3e09-a3b7-15669bc894b6 | -6.9552 | -55.635 | 2026-09-01 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 228.0 |
| e5816421-da87-3011-886a-4ebe641e6c90 | -8.7817 | -46.4623 | 2026-09-01 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 37d463dc-2700-3ed0-aa94-6fde7072e4a1 | -3.879 | -44.0576 | 2026-09-01 13:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 33af8cbe-bd5d-3f8d-9fa8-0f09a73c0dd1 | -6.9553 | -55.6151 | 2026-09-01 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| d5d08df6-1a4b-33db-ac31-2cadd5f187e6 | -11.1931 | -46.1319 | 2026-09-01 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| c4555950-66c4-3f7b-b0f4-4ee3b8c57154 | -7.1786 | -55.4837 | 2026-09-01 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 7ec8bb52-8554-3d5f-b006-64ca543c3b68 | -6.8009 | -59.5742 | 2026-09-01 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| fec49e68-959e-36cf-ac48-6f08565ad388 | -7.905 | -44.2346 | 2026-09-01 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 2f7de800-b2b8-3298-b052-7f29fecd0985 | -7.8628 | -61.1405 | 2026-09-01 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 7ccfd1a5-6539-3801-942d-591a06688869 | -8.7628 | -46.4642 | 2026-09-01 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 6d6cd7f5-1fad-3676-8fb6-6212587d8968 | -8.7819 | -46.4399 | 2026-09-01 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 860c7d76-d4a0-3eca-942f-1482bd6e3439 | -3.5161 | -59.0597 | 2026-09-01 13:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| a052697b-3f04-3ca5-b25a-9ca3ee345ce7 | -10.7856 | -50.5066 | 2026-09-01 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 5d3284d1-86bb-3f26-8f04-c0ef82550b8b | -13.3374 | -51.7241 | 2026-09-01 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 16d79720-a484-3bf3-a866-d34a9b70a6f8 | -10.3391 | -49.9762 | 2026-09-01 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| cdb685eb-6468-3b1d-a5e3-5499b58da95e | -12.9032 | -45.8382 | 2026-09-01 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 8535fb28-5388-3d9a-9af0-a4c60472e1a5 | -7.9988 | -44.2711 | 2026-09-01 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 973a8597-3d7c-3908-b051-16803f222a96 | -7.3488 | -60.5691 | 2026-09-01 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 8aee2681-1734-389c-af99-9cbffcfd13aa | -10.696 | -46.2646 | 2026-09-01 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 152.3 |
| f5d36fa7-bb81-358d-a07f-50cdbaeb0009 | -10.7407 | -54.0401 | 2026-09-01 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| bfaa7334-da4f-3d9f-b5e2-4b2304af3ce9 | -11.112 | -51.5536 | 2026-09-01 13:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 14cfbd79-7e83-32e2-87af-33bf8a397e51 | -7.5894 | -60.4827 | 2026-09-01 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| b6498396-0d1a-3803-a2d0-ecf443c84329 | -10.8624 | -45.3789 | 2026-09-01 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 46449899-6eb7-3526-86ed-dfb2037266c5 | -11.8056 | -46.0476 | 2026-09-01 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 1d144324-0231-3c58-8665-639849fee4b3 | -9.9931 | -46.3057 | 2026-09-01 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 227.9 |
| 29e30a1e-a379-32f3-b29b-2964b67f852c | -11.5479 | -45.4676 | 2026-09-01 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 5134182c-6bed-3ec2-b4a0-e8a65ae06de6 | -11.2439 | -45.3727 | 2026-09-01 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| b5dd8d83-0389-3a9d-819b-3b7e99d2b3ea | -10.8818 | -45.3534 | 2026-09-01 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 323.2 |
| b627ac73-b402-38b9-a7ba-47eca78e8056 | -10.036 | -44.7056 | 2026-09-01 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| fc755db9-6535-32e8-bbfa-b0d05b0728e6 | -14.6732 | -53.5408 | 2026-09-01 13:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 244.3 |
| eb03011d-6d76-354d-aa1d-a8e43e9b6e6a | -10.8627 | -45.356 | 2026-09-01 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 281.8 |
| 7ec2ecac-b916-3d34-bac8-3edb694cfeb3 | -10.6964 | -46.242 | 2026-09-01 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| c06714f8-de73-38c8-9ad3-dbadbafedbb5 | -10.0101 | -46.4386 | 2026-09-01 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 231.6 |
| bdf09740-1d29-3b3a-9f0f-84b626474c35 | -8.279 | -54.9174 | 2026-09-01 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 9b911a34-6544-342f-a56b-391ea144b3ac | -14.6538 | -53.5433 | 2026-09-01 13:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 208.8 |
| 35b63d28-1a5d-31b3-945f-afa0856dcceb | -8.4235 | -44.9849 | 2026-09-01 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 8fd0ab5e-1908-366d-bf5a-b840fe86265f | -10.3577 | -49.9957 | 2026-09-01 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 384.5 |
| 71bdfad7-1587-3e32-8915-ea405c9762f9 | -17.1146 | -46.8556 | 2026-09-01 13:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 15016d89-ceef-317c-ac51-bc71f40c0238 | -7.8716 | -47.0838 | 2026-09-01 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 2e200b2d-28bc-31b4-9aac-79403dc0ac3e | -10.3574 | -50.0171 | 2026-09-01 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 86031094-ffbc-3fd0-b811-a50ad4798128 | -14.7108 | -53.599 | 2026-09-01 13:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 42bc997a-5401-3faa-bc7f-86aeeb805f0d | -10.8631 | -45.333 | 2026-09-01 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 48efe8bf-7d26-3d5f-9c51-6e911ecd4643 | -3.1265 | -61.2377 | 2026-09-01 13:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 5b68d0d8-e87c-36b1-a37a-5c4374a641fd | -3.8789 | -44.0805 | 2026-09-01 13:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 751d717d-f533-3f89-af12-590c728b5f73 | -13.9477 | -54.3971 | 2026-09-01 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 86ffff1d-cc0c-32f6-88d7-b28b40ac3ef9 | -6.1659 | -57.7403 | 2026-09-01 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 55c40d87-e7ca-31df-b226-6d579c1872b5 | -13.0892 | -45.1862 | 2026-09-01 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| dd187c51-1722-361b-8e40-0f50300376ab | -3.1083 | -61.238 | 2026-09-01 13:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| c84cd859-5e86-3b3b-b36c-b6e2d0416c3b | -15.4429 | -52.681 | 2026-09-01 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 158.4 |
| d71a6e23-92fe-31d5-a1cc-21ad10dccda4 | -8.2602 | -54.9388 | 2026-09-01 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 1db78f25-f7a5-36b9-9dce-cba0d129d75f | -7.2005 | -60.6897 | 2026-09-01 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a8a4dc40-6872-3ed3-a829-36b4a490a08f | -3.6215 | -60.566 | 2026-09-01 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 0e2bf5b7-5329-3933-9afb-dc8ead784ad0 | -8.7631 | -46.4418 | 2026-09-01 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 249f4900-a87a-376f-9367-70850a6c65da | -9.9912 | -46.4409 | 2026-09-01 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 242.9 |
| b3ad8852-0c85-3f0f-a6f6-71c763ef3d14 | -3.8604 | -44.0585 | 2026-09-01 13:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 210.4 |
| a0b4c4b3-03f6-3b8e-a758-f51c9ebb54eb | -6.6036 | -58.5972 | 2026-09-01 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 0232fde6-0518-3fea-885c-85eaaa99dbe8 | -11.2295 | -51.2667 | 2026-09-01 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 190.0 |
| ee6796aa-4b26-357a-9f5c-424e941f2ed0 | -10.3388 | -49.9977 | 2026-09-01 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 426.6 |
| 92f10625-19ac-3bcc-a033-88b81c829bb6 | -10.3385 | -50.0191 | 2026-09-01 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| bab405f3-9ff7-3d58-bb7c-a2d8c67fec7b | -14.6535 | -53.5642 | 2026-09-01 13:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 42cce3dc-90cb-350e-85a1-7379d834549c | -7.2006 | -60.6706 | 2026-09-01 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| a44fa6e0-48c9-3d92-b057-34e79bad1763 | -3.8605 | -44.0355 | 2026-09-01 13:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 6186561d-17eb-3b24-800e-f4123fa6e00a | -8.6149 | -54.855 | 2026-09-01 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 3b36b364-8e99-3d87-9d14-6ad42e5d5460 | -10.358 | -49.9742 | 2026-09-01 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 811f07fc-9f4b-3b66-828b-5e99350d78f1 | -11.2292 | -51.2879 | 2026-09-01 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| f0651fa3-764e-3196-be55-e5a0312e1957 | -9.4606 | -67.4531 | 2026-09-01 13:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| ec6b4bc0-7303-3a34-ad7b-347625b03446 | -7.571 | -60.4643 | 2026-09-01 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| bd29b423-aa87-35c5-b8aa-f9218f6dd219 | -6.8036 | -59.0921 | 2026-09-01 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 8d6a2c11-edae-330b-aa8e-2642665698ca | -14.6728 | -53.5618 | 2026-09-01 13:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 123.0 |
| c5d01be3-8ea0-3147-ac25-bbf905b145d7 | -3.8789 | -44.0805 | 2026-09-01 13:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 2aee5b74-1e18-384a-ab96-ae12d08d4fe8 | -14.7108 | -53.599 | 2026-09-01 13:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| adad3609-c0ce-32b9-9589-43f5c6e385a5 | -10.358 | -49.9742 | 2026-09-01 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 6bab7726-8ed9-3846-8092-10b7c46db75b | -3.8605 | -44.0355 | 2026-09-01 13:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 85d19d17-9a44-3b50-b685-56d812b61498 | -4.181 | -63.1543 | 2026-09-01 13:50:00 | GOES-19 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| a4c08359-3840-3dbb-bebb-4c163fdb42c4 | -9.4345 | -45.6477 | 2026-09-01 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 37052924-e0e1-35e4-a39d-8a5f43d96741 | -10.3577 | -49.9957 | 2026-09-01 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 473.4 |
| 2cd459f3-0047-3665-91be-b88f589391c2 | -11.2474 | -45.1655 | 2026-09-01 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 14af35c1-9f03-33dd-bce7-34cc8b8822da | -6.8193 | -59.5734 | 2026-09-01 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 147.6 |
| dee5070e-71cd-38e8-8f84-88e513aec3fe | -7.2005 | -60.6897 | 2026-09-01 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |


[Clique aqui para ver as próximas entradas](README97.md)
