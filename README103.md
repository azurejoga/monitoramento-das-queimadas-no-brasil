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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 396e0419-692f-37da-a9f6-b4882cfa514c | -6.77 | -55.6445 | 2026-09-01 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c4bc2cc9-f424-3606-9f7a-016a7ede584a | -5.5833 | -60.1924 | 2026-09-01 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| fa5e3e1b-e3c9-3e6c-8c69-fe4226349710 | -7.5709 | -60.4835 | 2026-09-01 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 166.5 |
| a691b654-6696-3cd7-9977-1e0bd3ba3651 | -8.4046 | -44.9869 | 2026-09-01 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 91c52c1f-5438-3e34-93a5-121be59e5750 | -7.182 | -60.6904 | 2026-09-01 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 568f7ddb-f3db-3f33-a318-dd127a4bbd43 | -3.4979 | -59.0409 | 2026-09-01 14:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 83a43376-8d09-308e-93f4-88fa3be9af69 | -3.6216 | -60.547 | 2026-09-01 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 9657b740-13f9-395d-bd4c-f5c0e6ebb300 | -11.2295 | -51.2667 | 2026-09-01 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 158.7 |
| f7e95e88-1c6b-3e5f-9a2f-1deaf71095a4 | -7.2006 | -60.6706 | 2026-09-01 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 123.1 |
| d26532d0-d7dd-3e90-91da-01e0619ac1fb | -10.1538 | -45.6982 | 2026-09-01 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 2615a1f2-7515-32ec-8408-20389df22bad | -12.9032 | -45.8382 | 2026-09-01 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 485.0 |
| 6b9ffd7f-cda0-32fb-8795-b6776f7ccf8f | -3.5161 | -59.0597 | 2026-09-01 14:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 114.9 |
| a3cdef28-040e-3f39-838c-e962d2798c87 | -13.967 | -54.395 | 2026-09-01 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 305.5 |
| 90831bb0-fb8d-3f16-9557-528ef00f47a5 | -10.3577 | -49.9957 | 2026-09-01 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 312.2 |
| d84a9b8c-7e06-34e1-91b1-2f853e640a0d | -6.8217 | -43.5271 | 2026-09-01 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 0f5556fc-f03b-329e-9824-2d10e3b9c098 | -10.7409 | -54.0196 | 2026-09-01 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| d3b4cf21-cb24-36ef-8b65-217f0b00e0dc | -6.8009 | -59.5742 | 2026-09-01 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| c3cc330d-6dc4-3e87-81e4-0b2170d27b12 | -8.5739 | -66.9754 | 2026-09-01 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 9233fe24-ccd7-3e33-84f3-109b7b5c75ac | -5.9451 | -57.6906 | 2026-09-01 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| baffeab6-1aae-3b23-9acc-6353a32109f6 | -11.2314 | -54.0164 | 2026-09-01 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 8bfbf4d8-c1db-3c25-b667-601ccba70202 | -7.9422 | -44.277 | 2026-09-01 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 8888ea43-b5a8-306d-8ac4-2b574f4395b8 | -6.8036 | -59.0921 | 2026-09-01 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| d9883910-4c54-36c4-92e8-39cf613e5df4 | -9.4421 | -67.4535 | 2026-09-01 14:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 54eed008-eb94-3ec0-8bf1-adc6da657bb9 | -7.5658 | -61.3811 | 2026-09-01 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 54cdd599-f96c-3835-90e6-21ded42a5c18 | -7.2255 | -42.7616 | 2026-09-01 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 545830e6-f142-338a-8fdf-071546bf99b6 | -14.6535 | -53.5642 | 2026-09-01 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 6886f48c-0fe3-35fb-a369-f858ed391bae | -15.4429 | -52.681 | 2026-09-01 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 58a0701b-ccb6-314f-a3f6-90392d27b62d | -3.5162 | -59.0405 | 2026-09-01 14:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| fecbffab-1f06-36bd-88df-8dd1d4701bae | -14.5634 | -52.0344 | 2026-09-01 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 73f373e2-f579-3e4c-8526-5dfdc51216e1 | -3.1083 | -61.2191 | 2026-09-01 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e4a004ba-58f8-3707-b38a-b05dfeb34f43 | -6.6727 | -59.4252 | 2026-09-01 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| cbd019f6-6869-3bd7-b22b-08d97f1ef700 | -10.1528 | -45.7665 | 2026-09-01 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 53d46406-d1d7-3ab3-9ee8-6ea291d4e2e4 | -7.9048 | -44.2577 | 2026-09-01 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 77b92271-a4c3-3609-b925-d44fba949c0d | -11.2638 | -45.3241 | 2026-09-01 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 1895a040-d374-38aa-aaac-7ddc6be27c8b | -3.879 | -44.0576 | 2026-09-01 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 08da76e4-2f51-3e1e-8894-e26f9ef71522 | -6.9367 | -55.636 | 2026-09-01 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e6ac024d-4db9-35b8-ae43-19b5f7dcca57 | -14.2599 | -52.8782 | 2026-09-01 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e48c70e7-c2c0-3f66-b926-2679051871a9 | -10.8046 | -50.5046 | 2026-09-01 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| def7e45e-7897-3803-871a-8f5bc387c3f2 | -7.9988 | -44.2711 | 2026-09-01 14:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 520e1387-d4c6-3fad-9358-1724afeb6ae3 | -11.2292 | -51.2879 | 2026-09-01 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 7c498205-3e6e-3ea4-a32a-92f1579f5c89 | -9.4606 | -67.4531 | 2026-09-01 14:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| d6004667-e216-30d7-80d9-b5a0b5197cb9 | -11.269 | -54.0334 | 2026-09-01 14:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 80c50b74-dbed-3eec-a689-7f69e1d69b7e | -3.1266 | -61.2188 | 2026-09-01 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| f8d87447-8a34-33f6-8572-346b80b392ea | -5.5649 | -60.193 | 2026-09-01 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 2c776385-dabf-3e4d-8539-d7974da723dd | -16.1523 | -46.6749 | 2026-09-01 14:50:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 115.7 |
| f7dd3040-c224-3914-b95d-58e2a43ed8ad | -3.9707 | -60.0258 | 2026-09-01 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 9f254bce-8024-3b77-be21-54182e75049a | -8.9242 | -63.2804 | 2026-09-01 14:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 2c9fdb27-1ac4-3e97-b87f-086eb41ca06a | -17.1351 | -46.8284 | 2026-09-01 14:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 5cb124ae-ce88-3a7f-9802-f7bf95b355d7 | -4.181 | -63.1543 | 2026-09-01 14:50:00 | GOES-19 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 284.5 |
| ab403722-c20d-31fe-81ae-cf16c0958d84 | -11.2125 | -54.0181 | 2026-09-01 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| c378ff5f-b1c2-3039-b283-51188cffbfd7 | -3.6215 | -60.566 | 2026-09-01 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 119.0 |
| d785c71c-0e90-38e3-9f65-86d2f877243b | -3.4979 | -59.0409 | 2026-09-01 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 178b15c8-04d2-3584-95de-c65e964e6159 | -11.2295 | -51.2667 | 2026-09-01 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 153.1 |
| b433dd59-fa82-3457-93bf-d4646d791409 | -7.2191 | -60.6699 | 2026-09-01 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2ab3513e-ba16-3148-b342-7b79af6254b9 | -7.2934 | -60.5713 | 2026-09-01 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 60a5ea84-cfba-3a69-ab69-6d5227d41373 | -9.6685 | -50.8299 | 2026-09-01 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| a7e8b95f-d3f9-3a9a-bae3-0dd103cf91cc | -11.2298 | -51.2456 | 2026-09-01 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 1bf1acc3-70ac-3955-8abe-0b85d63bb080 | -10.8627 | -45.356 | 2026-09-01 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 492f3ee4-9817-3b91-9da4-edb66451b12a | -11.2482 | -45.1194 | 2026-09-01 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 4f7bbd3e-ba03-3151-afef-92b7e3d96836 | -13.3374 | -51.7241 | 2026-09-01 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| a5d49e4a-bd14-3da0-bffe-17a289a66a38 | -10.8624 | -45.3789 | 2026-09-01 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 688c9a63-cf7a-3cda-9e5c-c0795c596a9c | -6.7514 | -55.6654 | 2026-09-01 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 270a358b-4d09-3431-8ad8-fe1e0f0ff43b | -11.2488 | -51.2435 | 2026-09-01 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| e3fa1288-b882-35e6-9daa-0557c546ecf3 | -10.7409 | -54.0196 | 2026-09-01 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| c94a7d73-515c-3ed9-b871-9673b62395cf | -13.0897 | -45.163 | 2026-09-01 14:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 431.4 |
| 3c8a4db0-0edb-3457-8e67-58f6e92299a0 | -12.0929 | -47.1362 | 2026-09-01 14:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 9f14b7bd-23de-3677-b714-0e90b41eda2f | -7.8862 | -44.2365 | 2026-09-01 14:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 22409de3-bb25-3004-938c-226802007cf0 | -10.7856 | -50.5066 | 2026-09-01 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| a8dbac97-f02c-3835-9226-2059f2cde97e | -11.0623 | -49.6829 | 2026-09-01 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 0c2a7e76-ed11-34d6-8461-6b9d9748cfaf | -7.4548 | -61.4234 | 2026-09-01 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| c3dcde43-699c-3d09-bd6a-683884594adf | -17.1146 | -46.8556 | 2026-09-01 14:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 565ac3c8-7aee-36a3-b3e7-bc26d411ea42 | -7.5259 | -44.4565 | 2026-09-01 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 9aec412e-04cb-3eb6-abea-8c46dcc27e19 | -7.3117 | -60.6089 | 2026-09-01 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 87d9484b-a5bd-358f-815a-cb72d220ecf3 | -10.7271 | -50.6405 | 2026-09-01 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 208.9 |
| 962fbc7b-cd1e-3cc8-9670-4c4517a13b15 | -6.6542 | -59.426 | 2026-09-01 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 07719f00-4777-3630-8522-f317c874026d | -6.8009 | -59.5742 | 2026-09-01 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.9 |
| fce49643-a7f8-3f1a-a4c7-65ca2c04a9ea | -7.1822 | -60.6713 | 2026-09-01 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ffc93ad7-417e-3be1-a471-4bcdbb3c1566 | -11.7219 | -47.6104 | 2026-09-01 14:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 5982adfa-25d7-39d9-ba81-0a38a2796da4 | -7.4262 | -44.9468 | 2026-09-01 14:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 85d9ee9c-7ede-31b3-bee1-17ec4ed82b5e | -6.7699 | -55.6644 | 2026-09-01 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| e62d2d28-b36c-3219-aa27-478091f4ef0f | -7.4153 | -44.2599 | 2026-09-01 14:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 41.7 |
| ba418abd-1216-3083-93f3-f065c3371871 | -10.1525 | -45.7892 | 2026-09-01 14:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 85679530-1167-3c4d-87d5-bfa8a2d5cf61 | -10.1528 | -45.7665 | 2026-09-01 14:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 45accd51-f720-33f1-95b0-ee9330ab7e20 | -7.3488 | -60.5691 | 2026-09-01 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 537cef4b-cc24-390c-81eb-9fc4e58a8c59 | -3.2623 | -58.2367 | 2026-09-01 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 6d7f88b5-fdf5-3efb-a57e-98f4f4748ba5 | -11.5479 | -45.4676 | 2026-09-01 14:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 421.6 |
| 0919b485-f9bf-3001-810c-e6bd10b1636b | -6.7692 | -58.6679 | 2026-09-01 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| cbb83209-6c46-3db1-b472-90c8274837d7 | -9.9912 | -46.4409 | 2026-09-01 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 5b181f64-9d01-3cc8-87bf-f0490cf7230b | -3.4185 | -61.3461 | 2026-09-01 14:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 68ea211c-a31e-3255-bf40-50dddb75eb6c | -3.8605 | -44.0355 | 2026-09-01 14:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| b1050d04-9de6-3402-a624-573e46b82aab | -6.8008 | -59.5934 | 2026-09-01 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| fab64862-0062-33a7-b771-be90818e01b0 | -11.7216 | -47.6327 | 2026-09-01 14:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| d763bdd6-9f75-3010-86b1-4c9a1e93808b | -7.5526 | -60.4651 | 2026-09-01 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 8fe165ed-18a5-36b5-87f2-5c44b9115bd0 | -11.5287 | -45.4703 | 2026-09-01 14:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 846c098e-85c4-3efc-b073-9e42474fe07f | -11.2673 | -45.1167 | 2026-09-01 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 231.4 |
| e5cd8369-9fea-3ca1-8966-5c833522f208 | -3.5161 | -59.0597 | 2026-09-01 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 128.6 |
| f1b4ef26-bf53-330b-bfbf-d9b32d408db5 | -3.5162 | -59.0405 | 2026-09-01 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| f957b70e-bc2b-3d10-bb02-30fe5057611a | -10.1538 | -45.6982 | 2026-09-01 14:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 48b11158-98ff-3b2c-adcb-32dd0deb8290 | -7.4986 | -63.7448 | 2026-09-01 14:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 283d707d-56f8-335f-bf5f-a5eb59137291 | -13.9862 | -54.3928 | 2026-09-01 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |


[Clique aqui para ver as próximas entradas](README104.md)
