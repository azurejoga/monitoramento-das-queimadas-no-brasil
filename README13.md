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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5b88593-3609-3abb-82fe-d3b696d6916f | -5.1624 | -55.9338 | 2026-09-16 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| f7f04f25-88fc-3d1d-a907-ec4f9ae3ea41 | -17.0431 | -41.2862 | 2026-09-16 03:20:00 | GOES-19 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.4 |
| 4055e137-0ae1-3a8c-9e6e-5beffa2d1453 | -12.7713 | -51.2189 | 2026-09-16 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| f34a5873-e206-3425-aef2-f1b8703c4047 | -12.7518 | -51.2426 | 2026-09-16 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 48d1e275-74c0-3b8a-9d48-52cf1e87cbc6 | -6.344 | -62.6904 | 2026-09-16 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 2ed90ddf-ffb7-3d50-96af-291ffb9df2c0 | -5.144 | -55.9345 | 2026-09-16 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 231e9c84-e6d6-3792-9955-aaca91739e19 | -7.6511 | -67.164 | 2026-09-16 03:20:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| f4e7a11e-5ea3-3c35-aaa4-bdc64e4bbbdd | -13.287 | -51.2832 | 2026-09-16 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 19336521-25ba-3125-8ae9-a6583c97c6f4 | -9.0931 | -45.7314 | 2026-09-16 03:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.8 |
| f12c220c-48bf-3ce6-a972-cb6817b2cbd0 | -12.6443 | -50.7858 | 2026-09-16 03:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| af71c2f3-f3a7-39e5-93f3-da91292feb01 | -9.3893 | -60.3022 | 2026-09-16 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| bf7f2694-916f-351c-accc-88a1256c700f | -6.344 | -62.6904 | 2026-09-16 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| f20cc343-bef6-3f3d-a455-dc594f1c0dd4 | -13.2874 | -51.2618 | 2026-09-16 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| aebef695-8ba9-3718-b871-21b250ea6586 | -12.644 | -50.8073 | 2026-09-16 03:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 41.2 |
| e41ebb8c-df93-3bf1-a8b4-bd27027d690f | -5.1624 | -55.9338 | 2026-09-16 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 25662b5e-7fe7-30b1-a2c2-f7072976c2cb | -7.6511 | -67.164 | 2026-09-16 03:30:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| b51ba85d-6128-30e2-afa9-a91b5cbb6120 | -9.112 | -45.7294 | 2026-09-16 03:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 69e5d9ee-a1cc-39d7-b126-7d8bece46688 | -11.1401 | -40.4748 | 2026-09-16 03:30:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 73.0 |
| 415bfdf2-d379-30cc-bd0b-2781d3a4e7bc | -12.6249 | -50.8096 | 2026-09-16 03:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 3342276c-e6ec-3401-9522-c896d99b49af | -12.6252 | -50.7882 | 2026-09-16 03:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| caa47126-fc9a-31cf-91cd-b5fd7d643479 | -5.144 | -55.9345 | 2026-09-16 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 6098532b-357a-375a-89c1-0ffd1c38b035 | -17.0431 | -41.2862 | 2026-09-16 03:30:00 | GOES-19 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.3 |
| 19784b8e-556c-3f78-9521-03a47f0db662 | -12.6447 | -50.7644 | 2026-09-16 03:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 46.2 |
| d1413c83-6e08-33aa-96a8-74c85b78b030 | -6.3256 | -62.6909 | 2026-09-16 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 470be477-7744-3ba0-829c-e1d78a448f4b | -5.1624 | -55.9338 | 2026-09-16 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 39adfdf8-3253-3f6f-afd6-9095eba30f7b | -6.344 | -62.6904 | 2026-09-16 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 22020ba9-e1c8-3cd5-9f87-dc5d8e7cd396 | -7.6511 | -67.164 | 2026-09-16 03:40:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| f1aad236-ad4e-377e-b029-9ce0a3b2b64b | -9.112 | -45.7294 | 2026-09-16 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| f439bda3-83e8-371a-9a83-0ec4692154f3 | -5.144 | -55.9345 | 2026-09-16 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| a8a484a0-4128-36ff-b516-e410f8625987 | -6.3439 | -62.7092 | 2026-09-16 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 02ff0b16-e49c-33f8-bd67-23fbc3c75b82 | -6.3257 | -62.6721 | 2026-09-16 03:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| c781effb-6136-35c1-92fe-0fa4a393e5a8 | -6.3439 | -62.7092 | 2026-09-16 03:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 08166f98-cfff-3fba-a3c4-7d8d03d20953 | -6.344 | -62.6904 | 2026-09-16 03:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 95173b26-68e8-3a14-b8d9-8c945ec452bc | -7.6511 | -67.164 | 2026-09-16 03:50:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 65c5fce7-7a95-3871-b27e-bd9c21fc1fb8 | -6.3256 | -62.6909 | 2026-09-16 03:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| f9bf9188-f0b2-33e8-bce8-b234cc20e83f | -6.344 | -62.6715 | 2026-09-16 03:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 700b212b-f835-3b6b-839a-150f529c4a8c | -2.90243 | -40.39145 | 2026-09-16 03:51:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5722448e-3e76-3853-a3be-6e6df8c72032 | -1.21562 | -47.89471 | 2026-09-16 03:51:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 942c4242-85ac-38a0-aa93-f62c568584a3 | -1.21121 | -47.88971 | 2026-09-16 03:51:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2275531-88f2-3f85-8c35-bb5442c344b7 | -1.21717 | -47.89809 | 2026-09-16 03:51:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1122652a-02e2-3348-a761-6f568954e0b2 | -2.9041 | -40.39164 | 2026-09-16 03:51:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9eb7f948-04f5-3b55-a8c7-8834b880c095 | -1.2184 | -47.8909 | 2026-09-16 03:51:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1c7e03b-4f58-3bf4-b484-cad5c70e0ce1 | -7.18369 | -41.80914 | 2026-09-16 03:53:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7930916d-3179-318e-b9a3-4423f303cfd0 | -7.0922 | -42.10125 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 92b0d796-b374-35c4-a24f-1a58994b216d | -7.14108 | -42.09348 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fcb3138a-72e0-3041-961a-2aa48aa39570 | -5.10404 | -47.61394 | 2026-09-16 03:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b50f55e-f6c4-360d-ac16-c7e31f2bb87f | -8.38633 | -42.21411 | 2026-09-16 03:53:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 96ee29a9-9a41-3963-aeb9-598ab7a72bc6 | -8.03024 | -45.54554 | 2026-09-16 03:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e254398-93bf-3c7c-b01b-4677cb2c18b1 | -5.99975 | -44.31443 | 2026-09-16 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 004d9c8f-8d44-31bd-a417-4157ae81a475 | -7.04106 | -42.04375 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b20a62c1-4b1e-3bd7-9a38-86b3936f2059 | -5.14721 | -47.6044 | 2026-09-16 03:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac680a0f-2222-3644-af24-91fd338c0d3e | -5.75241 | -37.88563 | 2026-09-16 03:53:00 | NPP-375D | ITAÚ | RIO GRANDE DO NORTE | Brasil | 2404903 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1606daae-cb3d-30d8-bc3b-828251c5b49b | -7.22848 | -46.13856 | 2026-09-16 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e172574e-3954-3b71-88a3-1b6a60f70cf1 | -5.62935 | -40.85122 | 2026-09-16 03:53:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c1bc2c9b-e073-3eb4-aa03-1ec8b01521e9 | -7.09732 | -41.76463 | 2026-09-16 03:53:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d0d0b6e5-6890-3d31-a59a-054c54e5c63c | -7.34935 | -44.50077 | 2026-09-16 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b057cdf1-2a80-350c-8522-da41af3f0562 | -4.98369 | -45.15741 | 2026-09-16 03:53:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90163bce-142f-31ed-860d-741aacb356ae | -5.62625 | -40.85199 | 2026-09-16 03:53:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6acbc2ee-c876-3ab5-ab04-82250ff64c75 | -7.18259 | -41.80714 | 2026-09-16 03:53:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4a4bf5e8-ff4b-3c3f-9375-42138c21cc26 | -4.36377 | -47.78547 | 2026-09-16 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ac0504e2-f115-379a-83a5-b2578b569e90 | -4.90823 | -45.67858 | 2026-09-16 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79a6be0f-09f5-3d31-b246-b262f880d8bc | -5.63234 | -40.85933 | 2026-09-16 03:53:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 65a6803e-de7e-3a63-846a-79768bfa8566 | -7.17406 | -41.81208 | 2026-09-16 03:53:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1dda27e2-718b-3b1c-b5e9-339b949c38f9 | -6.81523 | -35.14623 | 2026-09-16 03:53:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 580adc9e-a562-3b8e-acb8-387c918c6569 | -6.6631 | -43.64761 | 2026-09-16 03:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5b46f10-52ac-3653-94af-a6dbd2da7cf6 | -3.88374 | -40.93271 | 2026-09-16 03:53:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 82c3880d-8c0e-3196-8fdd-2c22c790632f | -7.11043 | -41.80993 | 2026-09-16 03:53:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1c9782e3-987a-3cf6-ad71-1cf8627e8415 | -7.33453 | -44.49173 | 2026-09-16 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2d27212-9b0d-3d72-93f5-d082a0ca0986 | -7.10966 | -41.81432 | 2026-09-16 03:53:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3c2cc4f9-8523-35cf-b48c-1eb42bd2cfa3 | -7.11719 | -42.09151 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 61fbd8a2-97af-366a-8c89-9ef03f18c058 | -4.40981 | -42.31715 | 2026-09-16 03:53:00 | NPP-375D | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 36bc23f9-a930-3ddd-b12e-c867aad5fdfc | -7.17189 | -42.10385 | 2026-09-16 03:53:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6a4c01b0-df9c-3ebd-ae59-0420ac1915d4 | -5.1059 | -47.62597 | 2026-09-16 03:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 35a914cf-185f-32e5-9be5-0f3c1aa8113d | -5.99736 | -47.39024 | 2026-09-16 03:53:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45d03d22-0934-3762-9876-5f4287a5c5b2 | -6.95653 | -42.57749 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 313b4641-a90a-3290-93c8-d44c240b5b2b | -7.51567 | -47.33255 | 2026-09-16 03:53:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f8acead-5ea3-3b3a-a8c8-2a7dfff2e7eb | -5.98784 | -46.63365 | 2026-09-16 03:53:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a2275f55-95e1-3548-9f7f-a4f5cdb29288 | -6.32914 | -41.76066 | 2026-09-16 03:53:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 97116894-27fb-3697-85d0-18752266f730 | -5.62931 | -40.86005 | 2026-09-16 03:53:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8940e833-cfc8-3061-be78-12093c79bafa | -5.78142 | -45.09195 | 2026-09-16 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4f9f2146-66b6-3b0e-a28f-3f2025a3c08b | -5.7143 | -46.19554 | 2026-09-16 03:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b64b76f-43fe-3ef1-b8c7-09b35c9c5bd9 | -7.0903 | -40.65268 | 2026-09-16 03:53:00 | NPP-375D | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a4a6ac20-eebf-39c3-a7a4-8c72f3a72fc4 | -6.9506 | -42.55649 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7d32c7be-e499-3691-b8ae-9d461634f56d | -5.29777 | -42.71347 | 2026-09-16 03:53:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 57e7fd16-cb11-324d-ac7c-79b956545644 | -6.39454 | -44.06419 | 2026-09-16 03:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c141764f-67b1-3b1b-b9dd-44636e60c968 | -6.99071 | -38.1458 | 2026-09-16 03:53:00 | NPP-375D | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e7fe84b7-b562-314c-8457-52a3da7001f6 | -7.17952 | -43.51437 | 2026-09-16 03:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 134c2316-55a5-3eab-8fda-82c3b4f09c70 | -4.98384 | -45.15718 | 2026-09-16 03:53:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33cf62e6-94d8-3173-b6a4-d724c9c1e0e7 | -5.62871 | -40.85493 | 2026-09-16 03:53:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b40575bc-97d1-30db-acbe-b0f14df0a7aa | -7.18441 | -41.80489 | 2026-09-16 03:53:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 15768461-cc15-3c28-bce2-b19b48aad4ec | -5.10032 | -47.61844 | 2026-09-16 03:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 353c962c-38be-325f-a380-10f4d531c9c9 | -6.94712 | -42.57604 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2a23399e-687c-38d4-9d46-824b8dcb7bec | -7.08844 | -43.56288 | 2026-09-16 03:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 305f2897-853e-3beb-b169-8fb76ad52412 | -5.71515 | -46.19083 | 2026-09-16 03:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d38821eb-7299-3ddf-8e9f-be160454972a | -5.11844 | -47.61075 | 2026-09-16 03:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5bf6df18-576a-3497-8685-04d0e6e649a9 | -5.24793 | -36.7518 | 2026-09-16 03:53:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1c6ac41a-eb15-392e-bbb3-21f8e2c4a744 | -6.95184 | -42.57672 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 03afe327-7f73-30d2-8df2-21ab04282a38 | -6.3963 | -44.05433 | 2026-09-16 03:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e1f5064-7b6c-33a3-82df-dc93e49c9ba9 | -5.10695 | -47.62 | 2026-09-16 03:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 85c29992-dd5c-35ad-a4fc-ef33aada7f28 | -5.62994 | -40.8562 | 2026-09-16 03:53:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README14.md)
