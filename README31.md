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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10c688f4-53dd-396c-a52b-9402356ffe5c | -8.60463 | -67.17168 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 08ccc493-74ad-3be4-8d6f-bfdcedcc92fc | -3.21982 | -61.15133 | 2026-09-04 05:25:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab5d161e-718a-3626-ac21-b99c67ae52d7 | -18.14093 | -51.79926 | 2026-09-04 05:25:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d09526d7-36fa-31a3-b8d4-6cb50d47bbf8 | -4.48485 | -55.086 | 2026-09-04 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86c650b0-9871-3880-bebd-e3885e1c1bea | -4.48594 | -55.07877 | 2026-09-04 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc988127-b34d-30f2-a820-f5af2fb3f304 | -3.21984 | -61.17307 | 2026-09-04 05:25:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e10d3c1a-e3e1-31c8-88d2-84e465a472db | -4.67425 | -55.63857 | 2026-09-04 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8c2f4e16-d52f-358e-8d4e-ad99945757e4 | -4.24248 | -62.23845 | 2026-09-04 05:25:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5cb2b04-4e6d-3f73-9232-b657792dc8ce | -17.09745 | -56.84803 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 57832588-9d83-3365-b558-5bdb9190af61 | -10.65064 | -61.76262 | 2026-09-04 05:25:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5055876a-342b-3bc8-87e6-f0a87ab84cd0 | -4.28213 | -59.96893 | 2026-09-04 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59a961f4-3083-3e3e-b8ef-e5c945e929ea | -4.12773 | -56.34723 | 2026-09-04 05:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4172577c-5318-3983-8842-55a36bbb4b70 | -3.61405 | -60.56638 | 2026-09-04 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 101dd2c3-e9e3-356b-905b-750e7e5a6924 | -4.14496 | -60.69542 | 2026-09-04 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22b0fb91-084c-3d58-8bca-5a326b1212c7 | -3.66984 | -58.91969 | 2026-09-04 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65e2c7a0-111c-3bbd-b311-6f475d27eb70 | -5.55912 | -60.17624 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db412dde-2ae1-338f-9fcf-beb0177b7c1a | -10.28704 | -68.8502 | 2026-09-04 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2225959-223d-323c-8c24-e66060705c2a | -4.15382 | -60.70388 | 2026-09-04 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5ab5894-e96c-35b5-84a5-41b53a3a62a4 | -3.7774 | -61.75922 | 2026-09-04 05:25:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8382db0a-e52e-3c76-8a8a-e74c97d70576 | -17.10023 | -56.86153 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8695d2c0-55b4-3e63-8c40-0d3c38474106 | -5.56627 | -60.17381 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f37031b2-0c3d-35d4-9fbf-5f41a2e26c62 | -10.28879 | -68.8404 | 2026-09-04 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 449a888b-d04b-3116-8c12-7b727eb7e8e2 | -8.60036 | -67.17095 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bd998941-fb24-3aca-9b53-7a14919269b8 | -3.65043 | -58.77886 | 2026-09-04 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65670bd3-22af-3906-9c1e-3b6411fc0d63 | -5.17492 | -60.28561 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b77c2f1-679f-3eff-829d-2a8295fb2d9e | -5.33401 | -60.13721 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db37951d-c1ee-3b77-b9df-8089f7590498 | -5.77246 | -59.16838 | 2026-09-04 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abda955a-8c19-3699-a7af-195f19d5d28a | -10.0822 | -67.75733 | 2026-09-04 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c60816df-6437-3905-b606-2113d546eb66 | -4.48539 | -55.08239 | 2026-09-04 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a7181e4-46b4-3579-81bd-d5b6490272e3 | -8.66847 | -66.95334 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae300473-38b1-3e88-8e2b-6d0866381193 | -3.21591 | -61.15436 | 2026-09-04 05:25:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b3b4a00-810f-381f-bbc9-bdd1fa4a98b0 | -5.56297 | -60.1733 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a8306f48-59f8-34e8-8c27-54a2ac5ad9ac | -9.03316 | -65.73513 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1d7520c-db90-3ff6-bd7e-927a11a85f64 | -9.02423 | -65.44939 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90b9053c-dbf7-3715-a2b1-036b9e4d1333 | -8.71337 | -69.99751 | 2026-09-04 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2848b7f3-2214-3288-bea8-edd57342319e | -5.16331 | -60.27322 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d798d936-c1b7-34db-952c-6c096fa0e6f0 | -8.87238 | -66.66932 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb0c901c-104a-3535-87c8-bf0b87efb58f | -12.16392 | -60.76368 | 2026-09-04 05:25:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9e8e215-2b93-387f-aab7-fd3f56e348de | -8.6068 | -67.18453 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 172d233f-b506-3b7d-bdd1-1dde418d9ae2 | -5.3307 | -60.1367 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a53ff855-5f02-3540-8b27-f12162d6e467 | -6.31147 | -56.04182 | 2026-09-04 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a26832cc-3a1f-34e0-b77f-4bcbcf908a80 | -6.1343 | -57.68774 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eeb14b7d-e412-3cbc-a576-bb60647f24ea | -3.39331 | -61.32339 | 2026-09-04 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35769398-bdfb-390b-b6bd-0cc8de1850ae | -3.39443 | -61.31628 | 2026-09-04 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e2ba84c-fbec-3d8c-b09d-191244986dcf | -4.81639 | -62.78222 | 2026-09-04 05:25:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 784b0432-dac1-3833-99a8-5bc3ee4f846f | -9.0431 | -65.7468 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ac5a583-e0ef-3270-bfac-b67687df4fe9 | -6.16009 | -57.75797 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20316e11-7527-36c2-b317-0f463cfdc464 | -5.59316 | -60.19926 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4d43992-e810-3226-9189-e105604b063b | -15.68034 | -51.84509 | 2026-09-04 05:25:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1d428d9-3e24-347e-9ad6-ff56fb7eb471 | -7.87516 | -71.75766 | 2026-09-04 05:25:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5915abdf-6e99-368c-8415-9094118ff34c | -3.39387 | -61.31983 | 2026-09-04 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6992dbf-ba0d-3703-bcb0-87e209731a6b | -17.09797 | -56.84373 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b6d243ef-8bb2-34cf-a363-98417776043d | -12.54292 | -57.34887 | 2026-09-04 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5ce0207-7482-34de-ae58-a980d94f2b54 | -22.32086 | -54.87466 | 2026-09-04 05:27:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aad324fb-b631-3c2c-81c2-caf6bc979014 | -19.08937 | -57.36388 | 2026-09-04 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ac8910ff-6ea4-34d5-9fdb-cd7353de4850 | -22.31558 | -54.87393 | 2026-09-04 05:27:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11d2b63f-9320-37df-8313-ecbdcc41050f | -19.08455 | -57.36757 | 2026-09-04 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fa8faa90-fdc6-3dec-988d-0d294e7a806f | -10.5103 | -51.3194 | 2026-09-04 05:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 56ed1a2a-6a72-3831-b554-16a6425e1f65 | -10.51 | -51.3405 | 2026-09-04 05:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 0ea0bd39-19c7-3a3c-b132-3df69c79b1c1 | -8.5916 | -67.1973 | 2026-09-04 05:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 4cb9ab20-a8bb-3ade-a669-7872aaddda23 | -8.6101 | -67.1783 | 2026-09-04 05:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 26ed6623-b355-34ee-94ab-f45c6279405a | -6.6882 | -59.9628 | 2026-09-04 05:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 4e19cbbc-9362-304b-bbb6-e2ebf29cd34d | -6.6881 | -59.982 | 2026-09-04 05:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 161.1 |
| 90131fd4-bb1c-3533-83aa-9355971de84b | -8.5048 | -54.6606 | 2026-09-04 05:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| b0dfd467-59a2-3e5a-b26a-8e1105e6dc71 | -7.5476 | -61.3437 | 2026-09-04 05:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 2485a457-d0d9-3ff2-b902-d8340130d4d8 | -7.566 | -61.343 | 2026-09-04 05:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 37.4 |
| bf5ba34e-7a0e-3a1c-a37e-b0a28f2431a3 | -8.5916 | -67.1788 | 2026-09-04 05:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 106.3 |
| bd9b8137-4414-305c-8965-fcc5ecc27e0f | -6.688 | -60.0012 | 2026-09-04 05:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 08b106fd-f3e7-3f19-99a9-297c1388135d | -6.7065 | -59.9813 | 2026-09-04 05:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| da6bd51a-0fb7-3579-8f58-79dd78120475 | -6.6696 | -59.9827 | 2026-09-04 05:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 8cc4eae6-dcc9-3292-b3d5-0c8c550a1888 | -6.6697 | -59.9635 | 2026-09-04 05:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| d60326d7-361d-36df-96ee-045bd2a5d372 | -10.5103 | -51.3194 | 2026-09-04 05:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 15801c1d-486d-39c5-a447-d3f3e98b9d07 | -6.6881 | -59.982 | 2026-09-04 05:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 26e9eb66-6375-3e10-af54-62a72995938e | -10.6548 | -50.3923 | 2026-09-04 05:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 3b0efa98-114a-36c8-b420-ceb1fec10ad5 | -8.5048 | -54.6606 | 2026-09-04 05:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 7e15d25a-b27d-3737-86e4-075bb071f842 | -8.6101 | -67.1783 | 2026-09-04 05:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 0556bdb9-555a-3d6d-8f77-d711588ae9a5 | -6.6882 | -59.9628 | 2026-09-04 05:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 356f7168-7758-3f63-87e4-d6049034b411 | -8.5916 | -67.1788 | 2026-09-04 05:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| b3761b4c-cc3b-3819-8942-cb9e7bf042b6 | -6.6696 | -59.9827 | 2026-09-04 05:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 2e73a584-c9d4-3ae7-8802-aa6bb46ad53f | -10.51 | -51.3405 | 2026-09-04 05:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 0b33a1b1-a82d-314c-9f0d-06cad8f63143 | -6.6697 | -59.9635 | 2026-09-04 05:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 921ba93d-44f5-3a41-87a2-d9803473aae9 | -7.566 | -61.343 | 2026-09-04 05:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 5adfab38-6e7e-387f-b8ee-22d7ed6eeabc | -6.7065 | -59.9813 | 2026-09-04 05:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 1338d896-2166-3153-a6ac-3e38821a25f1 | -6.6881 | -59.982 | 2026-09-04 05:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 7d76e23f-ac7d-3025-8b17-eddd0326e1c0 | -6.6696 | -59.9827 | 2026-09-04 05:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 8ab93f39-9ac9-382f-b96d-68ebe5fb88fd | -6.6697 | -59.9635 | 2026-09-04 05:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 5bf05ecf-5848-32c8-828e-288b285f1b92 | -6.6882 | -59.9628 | 2026-09-04 05:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 9d4bb275-078b-3256-acf7-b5b32010b00c | -7.5476 | -61.3437 | 2026-09-04 05:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 51aded16-0e3e-364c-aa94-c27338f0fd5c | -8.5916 | -67.1788 | 2026-09-04 05:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| a38be27a-d10a-3cc5-98a2-6e8441700069 | -8.6101 | -67.1783 | 2026-09-04 05:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 7d18ff50-b646-358c-be28-5246590c2309 | -6.7065 | -59.9813 | 2026-09-04 05:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 89372519-7df5-3d2f-9cb6-156ec0c2c529 | -10.5103 | -51.3194 | 2026-09-04 05:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 75982bbd-2bf4-3983-86c9-ab2e84075585 | -10.51 | -51.3405 | 2026-09-04 05:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 389cb95b-86fd-3409-9604-d10f48fa7ada | -1.50699 | -55.68801 | 2026-09-04 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c005fd4a-ae69-3358-85f6-86c4e6072edd | -1.5076 | -55.68415 | 2026-09-04 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea6b28b3-9f1d-324b-bddd-f76a7c83fa75 | -1.50841 | -55.68503 | 2026-09-04 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8e0a177-7814-3ee4-90a2-4dd7be971282 | -1.24593 | -54.53386 | 2026-09-04 05:57:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59920b9c-8a68-3a5d-b472-47ed51936e0c | 2.44529 | -60.76585 | 2026-09-04 05:57:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8af1979f-b643-343c-8c46-3d5aa3bfa1e3 | -1.50782 | -55.68891 | 2026-09-04 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6220daf7-8602-3003-b702-0da9d488184a | -1.24757 | -54.52775 | 2026-09-04 05:57:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README32.md)
