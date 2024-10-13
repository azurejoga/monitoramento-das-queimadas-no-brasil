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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6688e9a8-bc18-3268-b22f-a533563f685d | -12.8874 | -62.79776 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 835a5383-8d91-3e93-8459-dad921511803 | -12.82625 | -62.99566 | 2024-10-13 02:15:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6f74c080-bce6-367c-a655-a2ffd9292572 | -12.77819 | -62.10813 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 24.2 |
| f0966fa2-1e8a-37ae-b893-0fe7b732f074 | -12.7714 | -62.28279 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 01883f9d-b182-3e73-b82d-ff45828942ec | -12.76895 | -62.26765 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 40c624df-ab3b-3ddf-837a-b52f7030e4cf | -12.76129 | -62.29017 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 12773c24-a5b2-3cae-861d-106dcd842587 | -12.76016 | -62.28472 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 33.8 |
| a1cdf90e-2feb-3215-816c-a375dad260ee | -12.75893 | -62.27498 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 5aabacf9-154c-3db7-8912-3896c9758e9b | -12.72038 | -62.25042 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| abc0cad3-c2d8-3dcd-86e7-5c03905525e9 | -12.71795 | -62.2351 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c337a711-7a7f-38b0-bb62-3c5a5f4fea0b | -12.70741 | -63.03571 | 2024-10-13 02:15:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 19.9 |
| c32586cd-736b-3fb4-8d17-9b589eef36e7 | -12.50957 | -63.26273 | 2024-10-13 02:15:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 2079764b-7d8e-3467-a2b4-b9bb17549758 | -12.48332 | -63.02199 | 2024-10-13 02:15:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 465a81ee-b546-3c2c-bf30-a1273bff27a9 | -12.48123 | -63.00846 | 2024-10-13 02:15:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 90624841-ce6b-38c0-8d49-e20a145d1c54 | -12.39883 | -63.74399 | 2024-10-13 02:15:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 29905f65-493c-327b-9e18-edb027a5388f | -12.39698 | -63.73182 | 2024-10-13 02:15:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 9c3024e3-5240-3b02-a561-c946d32cc119 | -12.38868 | -63.74571 | 2024-10-13 02:15:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 061f8017-a22b-3527-83cb-b6d456d39a79 | -12.38682 | -63.73353 | 2024-10-13 02:15:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 96876595-3514-3c4a-967c-34072e45c4a2 | -12.38496 | -63.72139 | 2024-10-13 02:15:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8d3fcc1e-6cb9-3693-a672-8876ea9abb3f | -12.31501 | -62.31287 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 206f2b8f-65d7-31d6-a91a-f3fa4342d18b | -12.31259 | -62.29785 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ac0d85c4-e33a-3e08-a8d9-ff955a4979c4 | -11.8783 | -64.99998 | 2024-10-13 02:15:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8f102fb0-d79e-3614-b8bf-bd427f08b47b | -11.86882 | -65.00146 | 2024-10-13 02:15:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 97286462-cd00-3c15-8714-5810b8d5ddcd | -11.73547 | -63.83326 | 2024-10-13 02:15:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 21bc6374-9aa8-307d-ac1b-eac83b7c34bb | -11.7262 | -64.03735 | 2024-10-13 02:15:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fa7cd5cb-9914-3f64-9a0d-e3187118947b | -11.72595 | -64.9874 | 2024-10-13 02:15:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5fcad8cd-bf8d-3616-8b87-185d59014c4a | -11.72484 | -64.29995 | 2024-10-13 02:15:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4fd6e83d-9326-3125-9a32-93f50058d740 | -11.7244 | -64.97697 | 2024-10-13 02:15:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| fef07faf-e40d-364b-acb7-c710502360f2 | -11.72378 | -64.1581 | 2024-10-13 02:15:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2341ecd3-a79c-3fea-a1a0-1c634d925b02 | -11.72283 | -64.96648 | 2024-10-13 02:15:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 23.9 |
| f8e3051e-65eb-3122-afde-c57a5b9f9266 | -11.68205 | -64.15283 | 2024-10-13 02:15:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0673da58-1aa2-35e7-903c-4f8b58a176ad | -11.6659 | -64.04771 | 2024-10-13 02:15:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3edb9fad-a9ae-37c5-a7cf-cfa1a2fd8916 | -11.66413 | -64.03614 | 2024-10-13 02:15:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e069e809-3b89-3435-84a1-9a3b11792ce3 | -11.62275 | -63.9624 | 2024-10-13 02:15:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 51373c30-ab30-3159-9373-34d9c01581c8 | -1.733 | -54.173 | 2024-10-13 02:15:16 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| fbe67d37-9b52-3c5d-8112-71e29296a4b6 | -2.1693 | -48.8108 | 2024-10-13 02:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 28fdf298-f016-3d6c-8244-85a3a55ab849 | -3.0731 | -54.2473 | 2024-10-13 02:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 9de0ebfb-378b-3933-91be-f9b9784a5746 | -3.0956 | -53.0559 | 2024-10-13 02:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 145.7 |
| 03ea27ce-e670-345b-858b-5bcabc2adb57 | -3.0957 | -53.0355 | 2024-10-13 02:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 201.5 |
| 5f505f0b-b17c-3e39-8e36-acbee29a2465 | -3.1141 | -53.0351 | 2024-10-13 02:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| e812135f-83e9-3068-bdb9-dea0d0251a50 | -3.1606 | -50.4766 | 2024-10-13 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| cd16c1b8-5f42-3e4a-bfbb-409e70284d55 | -3.1607 | -50.4556 | 2024-10-13 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 13125b31-db3b-36fa-a984-4898b54d4f15 | -3.1791 | -50.476 | 2024-10-13 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 4afda313-3e0f-39d9-ba3c-e1738561061e | -3.1792 | -50.4551 | 2024-10-13 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| a815b8b4-61c8-33f7-aaea-4f83da15ae5a | -3.1976 | -50.4545 | 2024-10-13 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 071ddc6a-c8fe-3fa8-a551-76a4dba5e7a1 | -3.3409 | -47.3278 | 2024-10-13 02:15:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| ccdc8a93-8370-3a7f-926d-47e92f78264b | -3.341 | -47.306 | 2024-10-13 02:15:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 6703512a-dc38-3345-ab2d-0b714e133532 | -3.3595 | -47.3053 | 2024-10-13 02:15:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 144fb5ca-fab2-3059-b1c3-f1289295b730 | -4.1148 | -48.2515 | 2024-10-13 02:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 527d6c4d-ba85-375e-9ef1-1f2f47916241 | -4.1149 | -48.2299 | 2024-10-13 02:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 5d93ff7a-2ca4-39af-9256-bd421dce6fde | -4.3985 | -44.4881 | 2024-10-13 02:15:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 5ed4ca28-8804-3c0c-a3f1-134ccd59502f | -4.3986 | -44.4652 | 2024-10-13 02:15:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| fb2299ed-80be-3532-8385-6964b0cdf536 | -4.7004 | -60.8077 | 2024-10-13 02:15:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 56be63d4-e103-3964-a94a-f58e96bbf2e0 | -4.7005 | -60.7887 | 2024-10-13 02:15:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 43c9a2f0-7e7a-3577-9bb6-82a3101530bd | -4.7188 | -60.7882 | 2024-10-13 02:15:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 063d3353-8e6c-3574-961f-b88458d2b37f | -5.1381 | -45.3969 | 2024-10-13 02:15:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 356581a4-215b-36ee-af61-7a045ef23a18 | -6.1301 | -47.2664 | 2024-10-13 02:15:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| de2bfa8e-69b5-39c5-82ab-05d20c103d86 | -7.6627 | -47.3229 | 2024-10-13 02:15:50 | GOES-16 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 304ef3e5-eb58-38e9-9984-80b2e514210a | -7.6815 | -47.3213 | 2024-10-13 02:15:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 5080a907-099f-31a9-ad35-583da6f6d9cf | -7.6817 | -47.2992 | 2024-10-13 02:15:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 0107b340-f94e-3657-9233-b2ee65b048c4 | -9.7359 | -64.2295 | 2024-10-13 02:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.9 |
| c7135056-2929-3549-ac68-55955b88f202 | -10.5097 | -42.5023 | 2024-10-13 02:16:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 63.3 |
| 1b8a8deb-7144-3bc3-9f02-2d7b149c8d22 | -10.5091 | -49.9798 | 2024-10-13 02:16:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 269.8 |
| 15fbdbea-a588-3788-bfd7-4d8c7ea161f8 | -10.5094 | -49.9584 | 2024-10-13 02:16:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 236.1 |
| 3c6926c1-bc2a-34d8-98d8-4916b60054ca | -10.5281 | -49.9778 | 2024-10-13 02:16:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 330.1 |
| 12145a4e-4819-3179-8dfa-65bfeea7e2b3 | -10.5283 | -49.9564 | 2024-10-13 02:16:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 297.0 |
| 0fb1a5be-0239-3fda-a4a0-3be0a24dbd71 | -10.9311 | -44.6789 | 2024-10-13 02:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 5e0e2882-d1c9-3d8b-8a2d-e119cb8ab844 | -10.9315 | -44.6557 | 2024-10-13 02:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| b858846a-4011-38a0-9d55-3e3b09ad1d34 | -10.9502 | -44.6762 | 2024-10-13 02:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| da1df6b7-e851-3b1c-b64d-2e55875a01fe | -10.9506 | -44.653 | 2024-10-13 02:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 3cc7513a-116f-36e6-af18-2953802e44e4 | -10.6913 | -63.47 | 2024-10-13 02:16:08 | GOES-16 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| ffc1d27d-f66b-3b91-bf76-b49ac8c3d6a4 | -11.1068 | -43.3428 | 2024-10-13 02:16:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 69.5 |
| faf32b0d-d5be-33d7-8aa1-f6cc59bc7550 | -11.6334 | -48.3736 | 2024-10-13 02:16:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 68495052-0a87-3ce1-ab2f-f253d1989d37 | -11.7308 | -64.9769 | 2024-10-13 02:16:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 1b7c6e10-949d-3840-9e5c-5c545bd94013 | -12.2754 | -47.6473 | 2024-10-13 02:16:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 03865365-7a08-3f97-bf9e-1b7ff80356ec | -12.3982 | -63.7284 | 2024-10-13 02:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 88.1 |
| dae17c79-7e7a-34e3-ad49-a7ab9d124e24 | -13.1363 | -41.9683 | 2024-10-13 02:16:20 | GOES-16 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 52a29bcc-2b04-3f75-a18d-1e33aefd640d | -13.1557 | -41.9646 | 2024-10-13 02:16:20 | GOES-16 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 6088c1ca-b4db-3864-af26-59b583f3fb7e | -13.1475 | -62.3215 | 2024-10-13 02:16:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 37705176-1e29-3204-9cdb-135dcbe0c91f | -15.6419 | -59.9767 | 2024-10-13 02:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 56a6b28b-7612-32ff-b70a-04e081b1f2b4 | -17.0001 | -57.4381 | 2024-10-13 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| d998b167-ba07-35cf-8c5c-1840d6caf179 | -16.9998 | -57.4586 | 2024-10-13 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 79d88249-f0cd-3d3d-a541-87ebe949f39f | -16.9995 | -57.4791 | 2024-10-13 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 273eaf62-9d9f-3698-85a0-06e77df2a72a | -17.284 | -42.6479 | 2024-10-13 02:16:42 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 37dc9cbc-a018-31fb-87f6-12f2522a72b7 | -17.1957 | -57.4562 | 2024-10-13 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 155.5 |
| 99232545-ffad-39fa-b48f-69c29d7a3ca6 | -17.1954 | -57.4767 | 2024-10-13 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 130.1 |
| 41caf40a-f210-34ef-9c7e-6950d1a169d0 | -17.1764 | -57.438 | 2024-10-13 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.4 |
| e3d0d40d-6451-344e-ad79-eff5bddebdb5 | -17.1761 | -57.4585 | 2024-10-13 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 212.7 |
| 60d75f53-8186-3586-a483-efcc933ca6ef | -17.1758 | -57.479 | 2024-10-13 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 145.0 |
| 0c0cd1a9-08ae-3aa9-9aea-0beac7922775 | -17.6474 | -56.2876 | 2024-10-13 02:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 35335f2d-cc0b-3a09-b0d5-9e731d2d2350 | -17.6478 | -56.2668 | 2024-10-13 02:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 80ceb211-17fd-3a8f-8c3d-c618fa5fd445 | -17.9837 | -57.3819 | 2024-10-13 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.0 |
| 6d9a8aec-4632-360d-9e35-7a40b8141910 | -17.964 | -57.3843 | 2024-10-13 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.2 |
| dbfabe1e-2d12-31bd-84dc-e8eca6a95d98 | -17.9643 | -57.3637 | 2024-10-13 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.4 |
| a1a78eca-7151-3d54-812f-7516632dcd89 | -17.9841 | -57.3612 | 2024-10-13 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.2 |
| 04dccc79-e189-315f-845d-7a8df9fec519 | -18.2147 | -56.5873 | 2024-10-13 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 3bb70b2b-2632-3108-8022-8cb2f2ac1536 | -18.2151 | -56.5665 | 2024-10-13 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.6 |
| 807e923b-ceb1-30a4-bb90-a493cf5e13e3 | -18.2162 | -56.504 | 2024-10-13 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.0 |
| 438c3ddb-6cbd-3f3e-89f0-b7015254f5be | -18.2166 | -56.4832 | 2024-10-13 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.7 |
| ff8cc78f-77d6-3141-b9c2-c2d1b9b1821c | -18.236 | -56.5014 | 2024-10-13 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.6 |


[Clique aqui para ver as próximas entradas](README30.md)
