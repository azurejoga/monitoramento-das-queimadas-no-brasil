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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31a9e9aa-a457-337c-9d35-4a521300ba3e | -6.558 | -61.407299 | 2026-10-10 01:47:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0a7e0e89-0f01-3265-8c54-a46cf7d36121 | -6.8044 | -59.311199 | 2026-10-10 01:47:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dca8a4ea-f56d-3ab1-88d6-5af35d241c0f | -7.927 | -54.7384 | 2026-10-10 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 082ddf7f-5e55-3bd3-9fe8-bf8776702fef | -4.9113 | -45.7927 | 2026-10-10 01:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 350.2 |
| cf38d6f4-b5af-3233-8b66-75cb70554f21 | -10.9093 | -44.8438 | 2026-10-10 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 6878f3d7-5f61-3023-8e39-f51f07e25297 | -6.441 | -55.0624 | 2026-10-10 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 05f63e5c-4bf1-3f9e-8160-b4550c793284 | -4.4507 | -47.9112 | 2026-10-10 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 93db4908-e40f-3853-bf6c-1e3e7adeef8b | -9.9384 | -44.8791 | 2026-10-10 01:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 228.8 |
| b89a212a-e795-390f-97d0-6dfdab44733b | -10.6201 | -60.4658 | 2026-10-10 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| e6f8d283-fd14-3a87-9a68-a6f5a9735b8f | -7.5162 | -45.3024 | 2026-10-10 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| a4315d01-e852-3303-a2b7-f1fa93e081d4 | -9.3805 | -64.6567 | 2026-10-10 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 543fccc5-6e81-3881-8337-f1465984d3cd | -5.7565 | -45.1293 | 2026-10-10 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 8aad8046-1b65-3003-899a-bc57877f6734 | -3.1284 | -54.1857 | 2026-10-10 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 61111ee2-27a7-34f7-b3cb-20cd0b3ae908 | -7.5347 | -45.3233 | 2026-10-10 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 409e709b-ef8e-34ec-b04a-b7a5ef7ab293 | -4.9301 | -45.7691 | 2026-10-10 01:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 172.3 |
| 68d71bfc-caee-3518-b7bb-9a413b5b7709 | -14.3415 | -55.0341 | 2026-10-10 01:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 119.3 |
| d10479fa-989a-39ff-a368-b24d7ebab907 | -3.2571 | -54.1824 | 2026-10-10 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| a53945da-c744-3890-ba81-bcee709eccef | -2.618 | -59.9747 | 2026-10-10 01:50:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 504e55b0-2ad2-32fd-8a87-5f007d2052e9 | -17.1414 | -41.3371 | 2026-10-10 01:50:00 | GOES-19 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.2 |
| 9a60185c-c4d6-35b4-9d2c-0604b2ad5aef | -4.5929 | -55.7168 | 2026-10-10 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| a1a73c41-b1d4-3124-b073-400e485cb62c | -10.6013 | -60.4669 | 2026-10-10 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 0ae04797-96b6-3cdf-bb73-845d84d47feb | -10.6199 | -60.4852 | 2026-10-10 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 6a598dc5-de02-3332-8180-fc52e8128e13 | -3.2203 | -49.4417 | 2026-10-10 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 3a5c8d04-e3b8-37c0-91ee-f4cd8ffd6c0b | -2.9451 | -54.0698 | 2026-10-10 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| e3f7d766-74dd-343e-a328-87c7b71a402f | -5.7378 | -45.1307 | 2026-10-10 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 0fcddb67-dfb2-34cc-afd0-d746974e7d1f | -6.8023 | -59.3237 | 2026-10-10 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 0dc5e0c1-b8e6-3011-8a87-7d32d57853a0 | -3.839 | -55.7997 | 2026-10-10 01:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 061e6bc8-3605-308f-a76a-0464430e0b0b | -7.535 | -45.3006 | 2026-10-10 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 7c4cde48-98dd-3953-adb6-2699245dfe19 | -7.5159 | -45.3251 | 2026-10-10 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 083148f9-913d-392c-baa5-685e74467423 | -14.3418 | -55.0135 | 2026-10-10 01:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| e5210888-726a-31cf-b9ed-2a7527b4ef8b | -7.9272 | -54.7182 | 2026-10-10 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| b0143958-7f59-3479-9ce1-ae7552a2e8eb | -3.1285 | -54.1657 | 2026-10-10 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 564c678d-28a2-32a8-9ad5-0f840c8025a7 | -10.9097 | -44.8206 | 2026-10-10 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 260.9 |
| 44684c28-aa59-39c0-87f5-0303a5e0ed5a | -10.6012 | -60.4863 | 2026-10-10 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 197.0 |
| 763e4f8b-6bc5-31e2-8224-c6b25a157b23 | -3.5491 | -54.7351 | 2026-10-10 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 577412d8-1562-36f4-bee2-1bb41ef47df7 | -10.8905 | -44.8232 | 2026-10-10 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| cc32f282-92fd-3002-b1e4-3bda83dbbae4 | -13.386 | -43.8945 | 2026-10-10 01:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| e27ce4a5-8c5d-385c-a8b4-e9fb2d8d5919 | -3.1114 | -53.7839 | 2026-10-10 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| d7c95746-7dea-345e-a335-3d1e0aedc9db | -3.9912 | -59.356 | 2026-10-10 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 18dae74d-585c-37c1-a20e-7b8086f8b55c | -4.4025 | -49.7774 | 2026-10-10 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 7752c441-72fd-3b52-ae38-c8eef9d4f6a6 | 2.727 | -60.2586 | 2026-10-10 01:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| d26fa676-d398-3010-99a9-5fe83202b277 | -3.8391 | -55.7799 | 2026-10-10 01:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| cd4faf83-3288-314c-ba1a-39901e825156 | -9.9388 | -44.8561 | 2026-10-10 01:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 057ca29a-f11d-32bf-9303-31da09b1c2ac | -7.9084 | -54.7396 | 2026-10-10 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| fd0e7ca6-82bb-3193-9cb1-58f085a12954 | -10.8902 | -44.8464 | 2026-10-10 01:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 24d39ed4-3884-34cc-9e73-fed29e319e81 | -7.4975 | -55.0055 | 2026-10-10 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 77b36d27-08fb-3cc7-9846-e42090d2d8b8 | -7.5687 | -64.585 | 2026-10-10 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| ed57e06a-d964-30ff-ac95-4af625282fb7 | -4.9115 | -45.7702 | 2026-10-10 01:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 171.0 |
| 078a2ff0-aab9-3e32-8dd9-13cc423a1acf | -7.0228 | -47.661 | 2026-10-10 01:50:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 7132bac5-e03c-3d59-ada7-316cddbe9f40 | -4.93 | -45.7915 | 2026-10-10 01:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 364.3 |
| 1f903d97-06b5-34f4-82a0-248f98753f97 | -7.9086 | -54.7194 | 2026-10-10 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 04182abd-8cfb-38c6-bbe9-bdd53340e27b | -6.4595 | -55.0615 | 2026-10-10 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| fbd12988-c044-314a-8dd3-3a336445045d | -3.9911 | -59.3752 | 2026-10-10 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| e3773331-ca16-3aae-a0f6-0f43ef6ba11b | -22.0909 | -48.9738 | 2026-10-10 01:50:00 | GOES-19 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 543b8581-5f3d-3efe-9bbb-23dad9b454d0 | -9.2976 | -47.3871 | 2026-10-10 01:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 20dac4ae-9e59-3380-a80a-e77e14f0d426 | -3.6048 | -54.5936 | 2026-10-10 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 769e97dc-f140-3cf2-a6d7-385969a0b16e | -13.3666 | -43.8979 | 2026-10-10 01:50:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 545b49ee-5cec-3a4d-b96d-cc2925ed7f64 | -6.4411 | -55.0424 | 2026-10-10 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 3382e3af-a402-3f14-8cb8-6189800590eb | -6.478 | -55.0606 | 2026-10-10 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 413cb175-63ce-3d98-bd12-8c97af32189c | -12.2877 | -63.3711 | 2026-10-10 01:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 798c3ce1-fdb5-3e0b-836a-715837171a47 | -3.5676 | -54.6946 | 2026-10-10 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 0aece949-a1ce-3284-b018-90fb1e3a18d9 | -3.5864 | -54.5942 | 2026-10-10 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| efe16006-e190-363a-8172-5c39d1e1d403 | -14.3223 | -55.0363 | 2026-10-10 01:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 3ac35af1-6d6a-3cf2-b721-60010ed21c0a | -4.5929 | -55.7366 | 2026-10-10 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 07c36b1d-19e0-376a-ad75-b14ad41b365b | -3.2204 | -49.4205 | 2026-10-10 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 2e87c117-2189-3dde-a74b-1531f1b6091d | -7.535 | -45.3006 | 2026-10-10 02:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 60a3620b-7d10-3621-bed5-f4ac72fab860 | -5.7565 | -45.1293 | 2026-10-10 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 0f85c963-1873-3a1c-ac25-758f04774ada | -3.9915 | -54.4619 | 2026-10-10 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 10471217-9ece-3eea-9e22-d914c298f9dc | -3.1285 | -54.1657 | 2026-10-10 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| f72f3347-f6e8-3f34-9996-5393709d0f4e | -7.5159 | -45.3251 | 2026-10-10 02:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| ee7e7d89-fdfe-3337-aee3-2a47534e5fcc | -10.8909 | -44.8001 | 2026-10-10 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 397b0ac6-f765-36b9-8e95-949f21fd85a3 | -7.5871 | -64.5845 | 2026-10-10 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 49186cf1-68f0-3317-be62-8871bdda656b | -9.6059 | -40.615 | 2026-10-10 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 2b86af51-c001-34b7-a549-fe2a7ea92b27 | -6.4595 | -55.0615 | 2026-10-10 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 5a8b63a9-84b5-38cb-a5ff-0bb883ce9cf4 | -6.9318 | -59.2605 | 2026-10-10 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.5 |
| de5beabd-11e1-3c5d-9480-aadcf59d51a0 | -10.6013 | -60.4669 | 2026-10-10 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 111.9 |
| f6d0d335-9719-3d10-ac6b-4a957c09f635 | -7.9272 | -54.7182 | 2026-10-10 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 404aba68-2c49-3d69-9841-b05554c2d8be | -13.386 | -43.8945 | 2026-10-10 02:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| ab7eb029-8955-3e50-91a6-4fc6974e8f28 | -10.91 | -44.7975 | 2026-10-10 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| f342ed94-2a1c-3449-b821-97c6d4cbf0bf | -4.5929 | -55.7168 | 2026-10-10 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 6a4a5b81-1a31-3f83-b576-bb2dcb2bba3f | -7.4975 | -55.0055 | 2026-10-10 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 0beb461b-c4ed-31c7-8e8a-996c8b928e24 | -3.6048 | -54.5936 | 2026-10-10 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| c16a11e7-58e3-388f-85b5-fecba5d5f534 | -3.2203 | -49.4417 | 2026-10-10 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| ea589841-a0c8-3e3c-8d98-d31b8ded4794 | -13.3666 | -43.8979 | 2026-10-10 02:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 4896ecd8-756f-34c4-9570-3ae2a989ba1a | 2.727 | -60.2586 | 2026-10-10 02:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 49f39c91-5177-3d0c-a725-d293cc98d340 | -10.8902 | -44.8464 | 2026-10-10 02:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 7fcaa7e0-665a-329f-97f6-d57f36c1561d | -2.945 | -54.0899 | 2026-10-10 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 1fe2c139-f342-35ed-9730-3cc064f687e4 | -3.2388 | -49.4411 | 2026-10-10 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 5eb7df24-f04a-396d-9154-9bc86352bd48 | -7.5347 | -45.3233 | 2026-10-10 02:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| e53b1000-bf48-3f5d-9d6e-8375cfbbe168 | -7.5687 | -64.585 | 2026-10-10 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| fbf7826d-96cf-3911-bdcc-9520e03b385e | -3.6397 | -60.6226 | 2026-10-10 02:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 4fd4e99c-d238-365c-95ed-be2992eb96d5 | -3.5676 | -54.6946 | 2026-10-10 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| b1357483-2a47-32eb-b919-404ecc16fc11 | -7.5162 | -45.3024 | 2026-10-10 02:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| aeb464d5-c7ee-3acb-b5b5-126bdb9fb96d | -3.839 | -55.7997 | 2026-10-10 02:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 5cde3872-915b-3b81-9fc8-da422b359fa9 | -10.8905 | -44.8232 | 2026-10-10 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 177.1 |
| def4e534-f2be-30a6-a51a-ee6f3b1864a3 | -6.4411 | -55.0424 | 2026-10-10 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| b8cdc8d9-2f95-3ff8-a9f1-aba334865b9e | -14.3415 | -55.0341 | 2026-10-10 02:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 4dc6ba5b-96f9-3289-bf8f-397e3e4ecc00 | -6.478 | -55.0606 | 2026-10-10 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 90deb878-f3e3-3885-bb8e-091a7cc0869b | -3.1284 | -54.1857 | 2026-10-10 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| d2fc72bd-69a6-3209-a716-1a64f05ce6de | -3.9911 | -59.3752 | 2026-10-10 02:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |


[Clique aqui para ver as próximas entradas](README22.md)
