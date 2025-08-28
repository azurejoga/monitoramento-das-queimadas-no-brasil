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
| 1ff0b837-20be-35d1-a6b3-0c4108fb07ca | -9.6794 | -47.0798 | 2025-08-28 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 70317641-ce34-3301-9403-d9f54d5e39ec | -11.3329 | -43.5452 | 2025-08-28 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 04dbc435-4f0f-35e6-9953-a3177515c144 | -9.4246 | -60.5701 | 2025-08-28 13:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 80957bea-1a62-38f3-85af-963b5cb0527b | -6.4543 | -44.5749 | 2025-08-28 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 6348d486-019a-3de2-806b-745cab5ffad0 | -13.4208 | -46.9864 | 2025-08-28 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 49ac2456-6986-3bb6-bf90-f23cc23c6036 | -11.3526 | -43.5187 | 2025-08-28 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 1bc04183-1928-3199-873f-12c221378032 | -10.8233 | -60.8019 | 2025-08-28 13:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 66b7f68e-e958-37b3-ba80-60f476baed8c | -6.3881 | -45.6018 | 2025-08-28 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 9c41df61-ba86-33c8-a463-9a6add71443f | -9.406 | -60.5711 | 2025-08-28 13:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 965a6c40-7263-34fa-811a-d4b1c4bfc0ef | -10.4736 | -57.9563 | 2025-08-28 13:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| bf5bd7f3-dd12-3e10-a013-66ed90b5b0bc | -11.1523 | -54.3104 | 2025-08-28 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 74505c0c-a10d-3e0a-b135-892f4c6f00cc | -6.8583 | -43.6169 | 2025-08-28 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| c6dac946-c62e-35b1-a282-e15c0888a42c | -13.0863 | -46.3352 | 2025-08-28 13:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 107.3 |
| f34bb0b4-3efb-34ec-8e9b-d34df6467ae9 | -10.8421 | -60.8009 | 2025-08-28 13:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 62501bac-44a8-3bca-9897-1e2f07ad34a7 | -11.3521 | -43.5423 | 2025-08-28 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 352.9 |
| 999b2fc6-f9b8-3dea-b9a8-157fe79e9cc5 | -16.3606 | -43.7858 | 2025-08-28 13:30:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 190.4 |
| cba3f94b-dd67-3c60-8547-2c958fe35e3a | -7.1917 | -44.0732 | 2025-08-28 13:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 5099fc1d-9de9-3b57-8830-b47b3a089246 | -7.3196 | -46.109 | 2025-08-28 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| ebc7b34e-9906-3caf-aa23-3cf093e3e877 | -6.1595 | -44.0472 | 2025-08-28 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 62337230-2e13-369b-9764-afccf29e594d | -10.4738 | -57.9366 | 2025-08-28 13:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 9227b363-4a5a-32ed-8803-fe2a1a8fffd3 | -10.8049 | -60.7644 | 2025-08-28 13:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 5489e793-47d1-315d-adf4-f22758bc0313 | -11.2378 | -55.0569 | 2025-08-28 13:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| e93fee05-b53d-3107-8e30-09ef2414a52f | -6.8772 | -43.6152 | 2025-08-28 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 3dd0ab11-bf52-39af-b7b9-78a588b17316 | -9.1339 | -65.788 | 2025-08-28 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 653.2 |
| 6580f34b-c265-3d3c-8ba3-3884c394b71c | -12.8032 | -48.1516 | 2025-08-28 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 6813ddf5-8098-3f08-b902-be314169233a | -13.5197 | -46.8578 | 2025-08-28 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| df115c46-975c-37e9-8e6a-0a19c896dbb6 | -9.1155 | -65.7699 | 2025-08-28 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 613.3 |
| 46272641-cb74-3c79-8239-7287d0c207e5 | -6.1562 | -44.3926 | 2025-08-28 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 7598751b-25f6-3ed6-be17-d872707c99c5 | -9.1363 | -65.2835 | 2025-08-28 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 7262e922-d874-3ed4-a760-03a2ddc4d035 | -6.178 | -44.0688 | 2025-08-28 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 0686eb02-ddac-3cc9-99a8-c1aa7f87cfed | -9.4058 | -60.5904 | 2025-08-28 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 114.6 |
| b3068ba9-e365-398f-b0d5-670075928dbc | -10.7862 | -60.7655 | 2025-08-28 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 43e6bae4-0009-395f-b18c-dee54672163f | -11.1523 | -54.3104 | 2025-08-28 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| c967949e-131f-3a27-a1bd-ef86d3021db2 | -16.3606 | -43.7858 | 2025-08-28 13:40:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 255.4 |
| 7596556e-77ca-3e61-ab45-7dede4a38c24 | -12.8032 | -48.1516 | 2025-08-28 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 7c14d315-2d6a-30ae-b6a0-745583f78f50 | -14.3343 | -51.8944 | 2025-08-28 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| eff97dea-6df5-3763-965c-a50e7e1b79c8 | -6.4388 | -42.4096 | 2025-08-28 13:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| 69d400e6-f605-35af-a9b3-2fb12d6d66a1 | -7.6414 | -42.6718 | 2025-08-28 13:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 118.7 |
| 2b96d8f5-ec3a-3051-b954-0f5dfdb6bb6c | -11.6539 | -44.8765 | 2025-08-28 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 93b42f4b-953f-3d04-ad21-129262b9377b | -10.4738 | -57.9366 | 2025-08-28 13:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 32691058-2947-35a3-a0e3-81c85dd18637 | -7.3357 | -59.6484 | 2025-08-28 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| e3c28d70-20a8-3aed-b86f-fcbb249f0dc7 | -6.4543 | -44.5749 | 2025-08-28 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 2f7d961a-551f-334b-9e8a-71dc8076607c | -9.4061 | -60.5518 | 2025-08-28 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 3cf8ba60-3292-3f97-aabd-f5636fa85c55 | -6.4355 | -44.5764 | 2025-08-28 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| a53a8bbb-84ce-3b1c-b0e6-dc2dc049ab9e | -9.676 | -64.9838 | 2025-08-28 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| d2a73b6e-cc9b-3cd6-a73d-dbfacdc3fa19 | -8.2705 | -45.1605 | 2025-08-28 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 48350150-1c6a-3c6f-991b-d4eee5124927 | -10.8049 | -60.7644 | 2025-08-28 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| a837f898-2f7b-3aa4-8590-fc9cfe31aa99 | -12.8224 | -48.1489 | 2025-08-28 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 5265727c-325b-30de-a575-094b1ab23ccd | -10.8421 | -60.8009 | 2025-08-28 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| ad98496d-106c-30d0-a855-f47fc25d8545 | -13.5386 | -46.8775 | 2025-08-28 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| e4343932-9734-3f02-9d6d-84d589983be0 | -9.406 | -60.5711 | 2025-08-28 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 246.8 |
| 5c589d68-b2fb-37bd-927b-9cfcd2c7c689 | -9.134 | -65.7694 | 2025-08-28 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 228.9 |
| 1e601cd5-6947-3988-b31f-4985a5027ed9 | -8.4407 | -43.6666 | 2025-08-28 13:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 58acec26-cf1b-3bca-8ad8-97aee086d115 | -11.5707 | -46.3751 | 2025-08-28 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| d2fdfca5-f318-36dd-9dd0-c5a6cbdaa6f8 | -13.5197 | -46.8578 | 2025-08-28 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 3f897354-44d3-32ea-b13e-60ffe844ff81 | -9.6816 | -48.3139 | 2025-08-28 13:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| e0dfa31a-c66e-3485-979f-53715e616911 | -11.3329 | -43.5452 | 2025-08-28 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 69e63dca-f106-3b4d-91fb-3a85f7aedb3b | -9.1153 | -65.8073 | 2025-08-28 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 701.8 |
| 46631b88-4a76-3743-aea1-9e9caf77f424 | -15.2101 | -53.8086 | 2025-08-28 13:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 92957deb-a9fd-3b89-8e37-935b543aca35 | -10.8419 | -60.8202 | 2025-08-28 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 192.3 |
| 94fdc53f-3b6b-3c06-ad8e-e683ee3ca90e | -12.8028 | -48.1739 | 2025-08-28 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a75a1cbf-0c23-3924-9889-e54859de508e | -14.3339 | -51.9157 | 2025-08-28 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 22e0fc56-e9a6-3f16-9e32-7fe7d00b4ff0 | -9.1155 | -65.7699 | 2025-08-28 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 413.7 |
| 5feabcd8-09c6-3a2b-b173-e8e61725e6b2 | -10.8233 | -60.8019 | 2025-08-28 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| adb3de69-e2d3-3407-a11a-91cddb97ec90 | -9.5423 | -62.4014 | 2025-08-28 13:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 719f6356-79f5-3c6a-adfb-41f7122e7220 | -13.5193 | -46.8805 | 2025-08-28 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 101.8 |
| ad3595b9-9fb1-3bad-9117-6fe0d2c63301 | -7.1917 | -44.0732 | 2025-08-28 13:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| d77b13d9-7e96-3c86-935c-93d00cb5a5cb | -10.4736 | -57.9563 | 2025-08-28 13:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 4dba3680-ed37-359c-842e-f18e6b60ef1b | -7.0569 | -44.3623 | 2025-08-28 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 8e11819f-1c3b-3a72-bf6a-f31c5e3f35e4 | -9.4246 | -60.5701 | 2025-08-28 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 166.1 |
| 52cc4bc8-3e00-3654-bf69-a36a3c7b0e62 | -11.2378 | -55.0569 | 2025-08-28 13:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 386f22d5-81c6-37a0-9603-4264204dac64 | -9.4366 | -48.2955 | 2025-08-28 13:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 4517bbc3-cea7-3ff2-bf5b-ef947b5b0be2 | -11.2189 | -55.0585 | 2025-08-28 13:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 80252628-d991-3703-8683-d86bc1b78511 | -7.6222 | -42.6975 | 2025-08-28 13:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 668ec851-08cd-31ee-82c3-4f4a1c6bc99f | -9.1339 | -65.788 | 2025-08-28 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 962.9 |
| 26aac221-f1b5-339a-b18e-16000f41b5c4 | -14.3309 | -53.2477 | 2025-08-28 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 2cc505f2-8939-3253-80b8-a459a701729d | -7.6225 | -42.6738 | 2025-08-28 13:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 176.9 |
| e2518f5b-4fad-3cc0-aba1-3626ed64ccce | -8.8842 | -60.7507 | 2025-08-28 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| cbce30b9-4d94-3fef-9827-9d2b3f223a77 | -6.8772 | -43.6152 | 2025-08-28 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 8f6fde25-ca90-35ef-8723-c5436b174906 | -13.4204 | -47.009 | 2025-08-28 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| e6868142-05ef-3eb0-9548-31bd8e7b0171 | -9.5424 | -62.3823 | 2025-08-28 13:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 14e7184e-8c3d-302e-b172-37ef2a5a9d29 | -14.3696 | -52.0813 | 2025-08-28 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 54ea6360-f614-3b5d-89ea-ed9511c43d79 | -13.4208 | -46.9864 | 2025-08-28 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 648b5b9f-3822-3849-84df-0327369e24b8 | -10.3709 | -45.1686 | 2025-08-28 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 0360e50b-58d1-388e-a274-a5d8ccc3cc4b | -13.0863 | -46.3352 | 2025-08-28 13:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 980632b7-9551-3b78-a63d-d3139e77cf55 | -6.2755 | -43.6907 | 2025-08-28 13:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 70867166-ec83-3fec-95d7-a7c57c8a3184 | -11.3526 | -43.5187 | 2025-08-28 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 937c1d9d-cf60-3465-8bfa-d8a68cf66e78 | -6.8583 | -43.6169 | 2025-08-28 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 64ab1083-8688-39ab-bbc1-aab02dc0fb1c | -6.1595 | -44.0472 | 2025-08-28 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 6a672069-7471-3af8-9946-46bae145244a | -9.2632 | -65.8959 | 2025-08-28 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 2b1dcf25-c3a8-35bd-90b9-f921a65919a7 | -12.6878 | -48.1677 | 2025-08-28 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 49534b03-fd61-3ec9-9dcb-da370d63d83b | -12.3989 | -45.0415 | 2025-08-28 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| a4477189-68df-3c99-ae13-9340c5cfa34b | -7.1917 | -44.0732 | 2025-08-28 13:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 113.7 |
| b4c4285c-2cbe-3ca5-8638-e81916048354 | -12.6878 | -48.1677 | 2025-08-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 507154cb-109f-3bc4-a04d-86fb5437c4ea | -13.0154 | -56.8982 | 2025-08-28 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 796534b3-1382-3a72-88a8-5b6ddd12d7da | -9.4061 | -60.5518 | 2025-08-28 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| edd9bf20-d341-340c-b993-b9d97d531c1c | -9.6816 | -48.3139 | 2025-08-28 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 837dc7eb-e1a3-3ecd-9261-de73ee2379c1 | -12.8228 | -48.1267 | 2025-08-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 4e262df2-b8d5-3030-8f47-9e10ede1d858 | -12.8032 | -48.1516 | 2025-08-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 8d21ae63-8ed5-318e-b18a-756c643399ba | -6.1783 | -44.0457 | 2025-08-28 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |


[Clique aqui para ver as próximas entradas](README97.md)
