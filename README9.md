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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c31922c8-2586-3d5e-a69d-6995f713e94a | -3.7152 | -46.039101 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9829c428-b360-333a-b351-33f4b7fc54e6 | -4.2957 | -48.095501 | 2024-11-17 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05f49d13-349a-3b4f-83ec-7266736d61e4 | -2.6692 | -46.200699 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c1091482-cce2-3e61-8a81-fa0f007f407d | -3.6307 | -43.164902 | 2024-11-17 00:28:00 | METOP-C | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2857976-0865-35b1-8979-1eb268edc51d | -1.8369 | -46.529701 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1f5aea5-81ac-37f1-9fe8-389c870a5769 | -2.9148 | -45.1576 | 2024-11-17 00:28:00 | METOP-C | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 27a09b92-f8b3-3702-9505-5b6ae8790da5 | -2.5863 | -47.552898 | 2024-11-17 00:28:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ea40fd4-082a-3d5a-9a43-dfbc81d5de96 | -2.6043 | -47.541302 | 2024-11-17 00:28:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd00275f-fa33-387b-9f8e-0debec5a5579 | -2.8591 | -46.6702 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ad2407f-da36-356a-a85e-c8be9d58f907 | -4.1379 | -44.196602 | 2024-11-17 00:28:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 590ca89c-4937-3ce7-9e5b-81f8a4786838 | -2.2117 | -46.410301 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a3a0107-2c0e-370c-95e5-6ca07fbc6806 | -3.2424 | -53.5131 | 2024-11-17 00:28:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 770bfc9c-aba2-3a9e-8067-a1858d8e5a32 | -6.9503 | -46.396999 | 2024-11-17 00:28:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1078e69-7da6-3ec1-85bf-03064a1a422d | -11.1621 | -45.112301 | 2024-11-17 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 347684bb-a5b6-33af-9f81-d41d09fcf246 | -2.7843 | -45.802898 | 2024-11-17 00:28:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c61ed342-38ad-3b66-9724-212be90e0f7c | -1.8001 | -48.443802 | 2024-11-17 00:28:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e0986d8-6be0-310d-b719-7801bf800414 | -3.1244 | -45.891499 | 2024-11-17 00:28:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b702bf7e-2bc4-3af2-85fe-7509f010c6ad | -4.5534 | -48.0061 | 2024-11-17 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da613ceb-dec1-3c3d-83fc-37348d9ccc28 | -3.1162 | -45.900501 | 2024-11-17 00:28:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2432d48b-fa26-36a0-9b6a-a71dd3fe142e | -2.14 | -46.4119 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0efe013-8857-37ae-a184-4ea2209bbd69 | -3.1039 | -45.981998 | 2024-11-17 00:28:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b0271fcc-4305-31fc-b8b0-d8bb8f1b041c | -4.21 | -47.216 | 2024-11-17 00:28:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c2cce166-f8a5-3e45-80fa-8dd38e0ab7bd | -2.6653 | -46.8153 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 062958a2-9bb5-3eb5-99a1-0ba7ba503715 | -2.8281 | -46.669899 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efedf202-62a3-3dcb-a127-3a65d90c2b9b | -3.3001 | -48.836498 | 2024-11-17 00:28:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e08f417-6a06-3af2-827c-ac176d060f39 | -4.5783 | -48.0252 | 2024-11-17 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6fad606-6f11-346f-b515-cc8d65b864fc | -3.4968 | -53.995 | 2024-11-17 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 2b3e104d-b78b-340c-8dc2-bbc947c3c6d4 | -1.9166 | -46.5804 | 2024-11-17 00:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 83382844-e13b-3383-94fc-d064d06dc073 | -1.2674 | -47.0976 | 2024-11-17 00:30:00 | GOES-16 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 56e7b9d9-11c0-33ed-b65c-b787764b4ad6 | -2.9238 | -45.1685 | 2024-11-17 00:30:00 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 405e8ae3-c289-34c9-825c-5f3a9c7f8aa3 | -2.678 | -46.2059 | 2024-11-17 00:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 876cb144-a654-350d-9c9c-1b4ec2c66944 | -2.9581 | -45.8181 | 2024-11-17 00:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 100.8 |
| ed1c5f10-e030-3eec-8382-4945f1cc4a0b | -12.4004 | -57.5127 | 2024-11-17 00:30:00 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 9d4fad86-4f38-33f1-9de6-67ce31ec60ca | -1.8007 | -48.4543 | 2024-11-17 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 1c1a728d-6659-3dec-bdf1-efbd3b9d022d | -5.2725 | -44.913 | 2024-11-17 00:30:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| eb54673a-fee9-3cfc-a364-eee6bff0c9e0 | -3.5494 | -50.254 | 2024-11-17 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| d2c71851-296e-3ebd-bd45-22d5cfb58692 | -2.88 | -46.73 | 2024-11-17 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 90171e1d-db71-3f4d-a4d1-85d2b84ad40d | -8.4339 | -44.1788 | 2024-11-17 00:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| b81f12c1-0b69-3aee-bd6e-7c6bbf40b2c4 | -2.678 | -46.2281 | 2024-11-17 00:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 33712fcd-c155-3aaa-9608-1aef18b69c9e | -3.5309 | -50.2547 | 2024-11-17 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 307.2 |
| 4610b36e-e801-3b26-ae82-a9355a24a35f | -3.5124 | -50.2553 | 2024-11-17 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 49ed0193-d62e-3862-afe9-edb10f720b83 | -3.5308 | -50.2757 | 2024-11-17 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 7cf35f65-8b58-3bcb-b9dc-15c911633ba3 | -2.6231 | -46.0299 | 2024-11-17 00:30:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 7d8d928e-150f-31e1-8e22-71723a978c7d | -1.9167 | -46.5584 | 2024-11-17 00:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 1855ee78-68de-344a-bf26-8fa32db3a29c | -2.5987 | -47.5705 | 2024-11-17 00:30:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| a9fc42a1-418a-3ffc-9478-8f99b8531c0f | -2.8481 | -45.4862 | 2024-11-17 00:30:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 8124e048-e3ad-3b88-85f5-629320377506 | -3.793 | -46.052 | 2024-11-17 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 8ac5e53a-4084-3882-8e6e-50c1376750dc | -4.4866 | -48.1045 | 2024-11-17 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 8fa03323-7577-3ba5-88cd-51affc24b390 | -2.6595 | -46.2065 | 2024-11-17 00:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| fc96f343-457f-3547-8e51-750a173c98be | -4.58 | -48.0132 | 2024-11-17 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 2b643deb-673a-322a-a24c-e325ed70ed65 | -2.8295 | -45.4868 | 2024-11-17 00:30:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 1f508620-8ea6-38d8-80ed-17ec1c5b1fd1 | -8.4336 | -44.2019 | 2024-11-17 00:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 160.8 |
| ce2ed814-bc40-3834-b311-4d9c288cf9bb | -2.9582 | -45.7957 | 2024-11-17 00:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 108.7 |
| b70b5344-9ddd-3250-82c4-7c9b54beedd5 | 0.6159 | -51.7881 | 2024-11-17 00:30:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 117c2955-49d1-38a7-9d1b-45902274d355 | -3.531 | -50.2337 | 2024-11-17 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 5516f687-6b61-3347-8312-a7baa73ce529 | -1.8008 | -48.4328 | 2024-11-17 00:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 295a9431-c146-390c-a0ab-eb478de14d95 | -3.7745 | -46.0305 | 2024-11-17 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 415c8f35-c50e-3de7-a0ec-ea7297e46140 | -3.7931 | -46.0297 | 2024-11-17 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 97.6 |
| deed8211-0f85-3ebc-832d-fc701399e3d3 | -2.8801 | -46.7079 | 2024-11-17 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| d2c9fd28-076f-32b6-a67a-0d9dfc6691c5 | -4.5616 | -47.9925 | 2024-11-17 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 2f0d2638-e452-3e1f-a208-d0847f03fa43 | -4.4681 | -48.1054 | 2024-11-17 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 868e346d-5865-3f25-84e1-dc224d76dc6c | -3.5678 | -50.2534 | 2024-11-17 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 3e0c4c1a-8588-395f-bc24-55f914f87171 | -4.5614 | -48.0141 | 2024-11-17 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 97d2cbb2-17d4-32a5-bded-930d88a81d40 | 0.6159 | -51.7676 | 2024-11-17 00:30:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 9efc94ae-009e-3112-826d-0f5b5a5e0798 | -8.4525 | -44.1999 | 2024-11-17 00:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 399.7 |
| a3d96aea-3853-3771-9d89-d28424b79bf3 | -2.8614 | -46.7306 | 2024-11-17 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 150.5 |
| bc4ce3d2-e9c7-39ac-ae2b-14f5c0e655dd | -8.4522 | -44.223 | 2024-11-17 00:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 125.5 |
| c5fccc44-2172-335f-a52d-878b6278f9b4 | -8.4528 | -44.1767 | 2024-11-17 00:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 176.2 |
| f1504465-c4da-3592-bc0d-7ddea2b9e2ec | -3.7744 | -46.0528 | 2024-11-17 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9b37ef19-a2b9-3b04-a878-cff748e212b0 | -3.1454 | -45.4753 | 2024-11-17 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 7aa08546-5106-37a1-90b9-cc6be16392a2 | -2.5988 | -47.5488 | 2024-11-17 00:30:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 38013787-1dfc-39ad-8113-492e28aff47f | -1.2488 | -47.0979 | 2024-11-17 00:30:00 | GOES-16 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 22286a65-edf5-3b4c-8493-4de8489a705b | -2.8615 | -46.7086 | 2024-11-17 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| cd2ee4c3-45c1-34d2-b46e-9d452131a26f | -3.5851 | -50.5255 | 2024-11-17 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 9995ea66-066f-317d-9dfe-4d1cba37e156 | -4.58 | -48.0132 | 2024-11-17 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| e52ce96e-b742-3929-84c5-c5e4370847eb | -3.7931 | -46.0297 | 2024-11-17 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| eac44706-1fc9-3d63-ba30-5ce5c94714ac | -4.5616 | -47.9925 | 2024-11-17 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 7faadc80-63aa-3483-8aad-399d6b3359df | -4.543 | -47.9934 | 2024-11-17 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 2dfcd1e9-6f65-3533-98ba-9046adf3c514 | -1.8008 | -48.4328 | 2024-11-17 00:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ccb79130-b639-3143-9c5e-f38ca13a496f | -2.9581 | -45.8181 | 2024-11-17 00:40:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 163.8 |
| f22f27d4-c28c-3322-8982-7e1c2292a8a1 | -3.5124 | -50.2553 | 2024-11-17 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 407316b8-1842-3d93-b476-f9d617eda217 | -2.5988 | -47.5488 | 2024-11-17 00:40:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 75006b22-5c49-3ba0-b8f0-007dd779470a | -4.5614 | -48.0141 | 2024-11-17 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 12d6bd1e-88ca-3723-b3d8-811805f15df1 | 0.6159 | -51.7676 | 2024-11-17 00:40:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 254ec76c-8e19-31b0-af84-c36bc5c9e95b | -1.9167 | -46.5584 | 2024-11-17 00:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 5616a2f0-260c-3e3c-9bc0-f39e5a047553 | -8.4336 | -44.2019 | 2024-11-17 00:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 8c196cd4-f825-3354-8a16-5dd646a9f6a8 | -2.678 | -46.2059 | 2024-11-17 00:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 29d61c78-2e3e-3b2c-b417-0c4466135a50 | -2.88 | -46.73 | 2024-11-17 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| c92d1500-dc55-3311-a984-d2b79d2782a0 | -3.793 | -46.052 | 2024-11-17 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 1b2a5e79-9367-3101-887b-18104f0d12b3 | -12.4004 | -57.5127 | 2024-11-17 00:40:00 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| e6dee3ef-12aa-3ea1-ae06-004a61ff4295 | -2.8615 | -46.7086 | 2024-11-17 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| a801c86d-9760-3e8c-9505-addbb0cd084b | -1.8982 | -46.5588 | 2024-11-17 00:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 3a96ded7-3d06-3e07-ab3a-386b7d785bb0 | -3.5309 | -50.2547 | 2024-11-17 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 297.9 |
| da57ab1f-b9ac-3c6e-bf2c-eeeb563f6f7e | -2.5987 | -47.5705 | 2024-11-17 00:40:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 0764b674-a79b-36e0-a63e-869ffc136bd5 | -4.4866 | -48.1045 | 2024-11-17 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 0bc3dd43-71f4-3677-8cdd-da0757402e63 | -2.5802 | -47.571 | 2024-11-17 00:40:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 7dd4ef50-0711-3da9-837d-8a56b9300b77 | -8.4525 | -44.1999 | 2024-11-17 00:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 180.6 |
| d9fb4a60-9d84-3be3-82e5-61fdaaa4833f | -3.7745 | -46.0305 | 2024-11-17 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 6229d388-a219-3964-89d8-c7fcef3566ad | -4.5799 | -48.0349 | 2024-11-17 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| e732c20d-538b-309c-9396-d535e19be54c | -3.4621 | -49.1143 | 2024-11-17 00:40:00 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |


[Clique aqui para ver as próximas entradas](README10.md)
