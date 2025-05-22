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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 657b4f08-cf17-3a13-9700-b50dc9c399dd | -20.9398 | -56.5998 | 2025-05-22 03:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 922fefda-28de-373b-ab85-4fa90131a83e | -11.5719 | -47.4521 | 2025-05-22 03:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| a8989aa1-fb10-3396-aa9e-8ab3e84ca147 | -11.5723 | -47.4298 | 2025-05-22 03:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| ef6b6602-6eb7-37a8-8633-d886109df055 | -11.5528 | -47.4546 | 2025-05-22 03:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 290f9681-0542-3aee-b871-a634eb0bbb37 | -12.2943 | -52.4995 | 2025-05-22 03:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 6b4971c8-2395-335c-8836-a2863db6924c | -11.5719 | -47.4521 | 2025-05-22 03:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 800bf8a8-5774-3d30-bab4-3c7797e956a7 | -12.2943 | -52.4995 | 2025-05-22 03:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| c6cc0c42-4d08-33a3-a728-1ae7a334e8c2 | -20.9398 | -56.5998 | 2025-05-22 03:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 8b19a58d-7cfd-3aa0-bf97-34c532ac56a2 | -11.5528 | -47.4546 | 2025-05-22 03:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 11cb1e95-6d7c-3c58-9073-274d029d20df | -11.5719 | -47.4521 | 2025-05-22 03:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| fd83738f-123e-39f9-95e8-d677450c2a87 | -20.9398 | -56.5998 | 2025-05-22 03:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 62.1 |
| ce3ca718-db87-358f-a2a5-c499f114a092 | -11.5528 | -47.4546 | 2025-05-22 03:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 2c592a0a-ab7a-33ab-8266-e380887c623d | -13.5261 | -43.6797 | 2025-05-22 03:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| ad4d8382-bb20-33ba-93b4-270f3fbab80f | -11.5719 | -47.4521 | 2025-05-22 03:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 1d5817f4-f320-35ab-b475-53682c4cc872 | -11.5528 | -47.4546 | 2025-05-22 03:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| c595807c-281a-3dc8-84b7-c9d3470be450 | -5.40117 | -48.3938 | 2025-05-22 03:53:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8661fff6-e4b6-3a28-9861-3eb0dfa18b7f | -4.02125 | -38.50928 | 2025-05-22 03:53:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 04e34ad4-d82e-3c0f-981e-cec6233aa0fb | -3.13617 | -40.99435 | 2025-05-22 03:53:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 40cc604e-6546-38da-a274-f261ed6cad9c | -4.29214 | -48.27681 | 2025-05-22 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f9fafbe-2d43-3981-b997-717b16c87c61 | -5.07089 | -37.7158 | 2025-05-22 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3a0216bc-a6b1-395f-a17c-82a1de857cf6 | -4.29286 | -48.27263 | 2025-05-22 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e12e1309-d797-3abe-a70a-dee9353d08ad | -12.10903 | -49.2988 | 2025-05-22 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48640e0e-96f2-38ad-8a54-7357e77103c9 | -11.55276 | -47.4533 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 90eb6622-5342-33fe-b07d-86f57f4a6cc0 | -13.69425 | -45.27341 | 2025-05-22 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8147c80-553e-3e96-8103-43aa4d42a27e | -11.60707 | -47.62213 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 097e2ff7-2d86-31bf-af46-3bc3ad8c8410 | -11.55376 | -47.44795 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2291d05c-fab5-3dde-b524-861f2f9b19c7 | -12.28821 | -52.50119 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a9d376bb-1ff2-34d4-b08c-224843057075 | -10.36441 | -47.97408 | 2025-05-22 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cb9e3a2a-abbf-3fe3-8c6f-52b61fd6c7d4 | -12.08243 | -47.34422 | 2025-05-22 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3e5c6594-4503-355b-9328-858470c6d993 | -9.96726 | -49.81099 | 2025-05-22 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 449d56f7-ffb6-39c9-ad65-cdd2a7ca4484 | -12.28942 | -52.49545 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 65d7e052-6915-361f-b8c8-14a16cb02746 | -11.24496 | -49.49532 | 2025-05-22 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b980c178-1b2c-3dc7-b1b7-d827ff8961d6 | -13.53534 | -43.67451 | 2025-05-22 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 4c3989a2-40f8-3e4e-9b34-47877f8cd821 | -12.28701 | -52.50693 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 288b11d8-a921-3306-a7cc-e5a693d8f48f | -11.86262 | -52.2792 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 504a8700-960e-3297-83da-665eff3984ca | -12.34834 | -49.98292 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6430b38e-6706-39be-93ef-b361e5786923 | -7.95125 | -49.76646 | 2025-05-22 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1f5935d-9a40-3913-9a59-2e2fef049153 | -11.59967 | -47.62222 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d322f2c-c502-3f15-aa20-60fc1c98a220 | -11.24411 | -49.4947 | 2025-05-22 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fdc0ee9-7b1c-3783-a629-0bf02ce9ff5c | -11.70803 | -47.78498 | 2025-05-22 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60b06d05-3273-31f4-adff-593a4cb3c54c | -11.60221 | -47.62116 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b82b576d-8641-3cf7-bb67-4fd5a8301356 | -10.55187 | -42.42937 | 2025-05-22 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7e52bc1a-81ab-34b0-ad5c-752501cebca0 | -11.5654 | -47.43903 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 63f5fc92-692f-3b52-a02d-7f78c422c408 | -10.36556 | -47.9679 | 2025-05-22 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d91f3883-ef27-36d2-b63f-de57a707e5d8 | -13.69828 | -45.27418 | 2025-05-22 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 496ec0a0-bd7c-3e71-aeab-2f6f78859469 | -11.24965 | -49.49581 | 2025-05-22 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8dd3c79a-08a9-3d88-8882-688c480413a4 | -14.05751 | -45.51527 | 2025-05-22 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4deffb5-10f8-35a0-a985-5a7dbae01faf | -12.29225 | -52.48824 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c1ecee50-15ab-3800-b381-7cbf1c9df50f | -9.60261 | -49.02129 | 2025-05-22 03:55:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 579404fa-301b-3cb4-b7d7-e77925d1b5d9 | -12.2911 | -52.49394 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1ee8bf4a-bfc4-3448-abf7-7f71a2bd9ec2 | -14.13524 | -41.69111 | 2025-05-22 03:55:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5fe08e0b-0e87-31d9-8f40-764611792075 | -12.84264 | -47.39655 | 2025-05-22 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41a3fcf7-13bb-3f4d-8f7d-dab6924b0e6b | -10.37915 | -47.97995 | 2025-05-22 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d9f8f4b-7d52-30f3-90ad-a520bef00c04 | -11.79996 | -49.33257 | 2025-05-22 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3bde9fac-9082-33fc-8bca-0177f00fb784 | -12.29475 | -52.50255 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 778ea98b-da38-3d4d-9867-4566c885e946 | -11.86416 | -52.27495 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 31fb3483-8565-3458-a61e-e94f61438103 | -10.36952 | -47.97496 | 2025-05-22 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8d3ef5d2-e977-37d1-b166-b8a64a89e17f | -10.02868 | -48.69528 | 2025-05-22 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 84e011cf-9594-3085-b37e-05010e008379 | -13.51676 | -43.69418 | 2025-05-22 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a39608ce-4991-382a-ba6a-7c5ca125d2bf | -10.09672 | -47.1014 | 2025-05-22 03:55:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 921891f1-a7fd-3cbc-96c5-fee1264c444e | -12.30128 | -52.50392 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ce2ca48c-010b-3c73-838a-582c145de231 | -10.03402 | -48.69656 | 2025-05-22 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e8ac8c6e-c2cf-3897-95c4-691cd2cc0545 | -10.55311 | -42.43086 | 2025-05-22 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| d85b32a4-2b3f-3ab6-aae3-64874a1da0bf | -7.80371 | -46.21281 | 2025-05-22 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f1d1939-f0b4-388b-b605-f5dd255a0fdb | -10.36893 | -47.97813 | 2025-05-22 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f4eb17b-e609-3329-a019-8026657526b6 | -12.35278 | -49.97729 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9807c5e3-6fa3-3d21-b047-b32ed8e06d92 | -13.50494 | -43.69668 | 2025-05-22 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 471c34a0-6294-3933-ae67-ad97cb4b2f03 | -12.36318 | -49.98357 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5ef6fda-27c4-33f5-8597-58385db09f6d | -11.56724 | -47.45601 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 3db3eb1b-52c8-333e-8571-c8609bcef9fc | -9.019 | -47.74124 | 2025-05-22 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b242d3b2-e1d5-324f-ba25-08b6fbbdff72 | -7.95207 | -49.76196 | 2025-05-22 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee5d0c49-5eee-34b5-94d0-7af1d68ea043 | -7.5809 | -45.85984 | 2025-05-22 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad4e22d7-78d7-380d-ad9b-a054542e4b31 | -12.34151 | -49.9753 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e206f034-ac80-395a-83fc-96c7ae290ebd | -11.89396 | -49.20227 | 2025-05-22 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fcaeed55-e916-35d2-9801-86dce2c6491e | -13.89842 | -41.29812 | 2025-05-22 03:55:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2715fb39-b48f-3ca8-b224-1064eca31112 | -12.30008 | -52.50966 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e5418c5b-4220-38de-8f4e-99bb91daafa0 | -7.80281 | -46.21799 | 2025-05-22 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c321cdd-d23a-3bd7-bbc1-310f2fc4f286 | -10.03463 | -48.69329 | 2025-05-22 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 85f311fc-54df-3faf-b717-289f926e6aea | -9.96646 | -49.81519 | 2025-05-22 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 421f1cb9-f806-3a7d-bf0d-950f5a40d46f | -13.29629 | -39.86245 | 2025-05-22 03:55:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 59c0a237-eab6-3462-a2c9-b6d90c8f8569 | -11.59099 | -47.61476 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33ee0ed3-2009-34a0-a4f1-4f5253493315 | -12.33856 | -49.97317 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8961ce22-7098-3652-b97e-3fd4ac2d68fc | -10.365 | -47.97093 | 2025-05-22 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ce96bb3e-35ed-3025-b04c-37542dde8034 | -11.93159 | -45.76416 | 2025-05-22 03:55:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f02a1dea-8c7d-3241-8b27-2b19b60f7965 | -11.55659 | -47.45957 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 03d8ae0a-1341-3d95-8e9f-09de74d7178d | -8.90756 | -50.01973 | 2025-05-22 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2de972fb-37fe-397a-b072-587ba803e281 | -12.3576 | -49.98233 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9cad03d3-1919-397e-8c23-c87372bb77a1 | -12.34908 | -49.97906 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e5509163-9fdd-3918-92b5-71ec10c0af4f | -10.65898 | -44.49623 | 2025-05-22 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6578def1-cffe-30dc-b06f-bce561080b64 | -11.56242 | -47.45508 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| f7b33caf-b9c6-31d5-92ed-ce3cc97d4b56 | -13.53457 | -43.67896 | 2025-05-22 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 466df714-e5a8-3121-9884-e80bb5e2a056 | -14.86495 | -45.12061 | 2025-05-22 03:55:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e93af4c8-18b9-32fb-b3fc-400f45c449e9 | -7.46529 | -47.06183 | 2025-05-22 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ed4f24c-c0e0-3687-9c1a-20827cdeec89 | -12.34493 | -49.97034 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5fbf1280-0893-359a-a2c4-3a68a70db096 | -7.94838 | -49.76391 | 2025-05-22 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c3e858bd-4695-3ae7-96d3-cbc1a71618cb | -11.56342 | -47.44969 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| c43cdccc-e7ce-37e7-b17a-30d0ea02b877 | -8.48287 | -49.60525 | 2025-05-22 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edeb8c27-b4a8-378e-bd1b-b63cc576a10d | -11.60455 | -47.62315 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 08da01df-621e-3942-a0cd-048d299892d2 | -7.39318 | -45.93924 | 2025-05-22 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f4d1eed-177e-32a2-bd07-def64792814d | -13.89784 | -41.3017 | 2025-05-22 03:55:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README7.md)
