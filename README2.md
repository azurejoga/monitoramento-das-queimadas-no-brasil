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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02b4729d-d0bf-37ac-831c-f05acba98c09 | -20.2978 | -50.02634 | 2025-03-26 01:20:00 | TERRA_M-M | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| 310600bc-2e9b-3cae-9165-6ced130cbf4a | -20.28429 | -50.01352 | 2025-03-26 01:20:00 | TERRA_M-M | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 6af3e185-a3c3-3565-b6b8-3f58891aebf5 | -20.29527 | -50.01148 | 2025-03-26 01:20:00 | TERRA_M-M | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.5 |
| 3e1c2080-66e1-369c-83dd-c9517ac84962 | 2.23502 | -60.7153 | 2025-03-26 01:24:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 913862eb-a7c6-381d-88e8-e6526b8403b8 | 1.82297 | -60.89385 | 2025-03-26 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b1cdd5ac-fbb5-3ac9-99d5-9034c3563e02 | 2.20206 | -61.80661 | 2025-03-26 01:24:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d3a395a3-4020-3e58-a748-e6419dcae4a5 | 2.55968 | -60.69625 | 2025-03-26 01:24:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.2 |
| a112e9cf-7c62-394e-9827-038ffec6911d | 2.19269 | -61.80524 | 2025-03-26 01:24:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 86e3d3ee-fec5-33b7-8d89-ce25d6267ae0 | 1.7317 | -60.29601 | 2025-03-26 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 36f96a1b-3e98-3ced-9b00-2eaaa7cf8c20 | 2.20066 | -61.81657 | 2025-03-26 01:24:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5878e18b-2dd1-306b-9186-2bd509b3dd1c | 1.6892 | -60.99523 | 2025-03-26 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 29f6ecd4-684d-3a09-9967-cbee9cd48abb | 2.04579 | -60.75051 | 2025-03-26 01:24:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 02e0bdfa-f90c-37f8-8a7b-21f8d7690709 | 1.82427 | -60.88463 | 2025-03-26 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 9ff6d008-e55f-3e57-82f0-d3d075154dac | 1.81524 | -60.88336 | 2025-03-26 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 045ea3b3-72f2-3fa1-814c-ee54f62c3b9e | 2.23629 | -60.70625 | 2025-03-26 01:24:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6a19dc54-ee7f-3c11-88b6-9c9d4726ce05 | 2.56737 | -60.70655 | 2025-03-26 01:24:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e208c049-7b7c-3519-8d28-bc12677fc3a4 | 1.82557 | -60.87541 | 2025-03-26 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 92d7ba25-cc46-3aa7-9233-e5917d922f32 | 2.37565 | -60.23875 | 2025-03-26 01:24:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6c84cce1-4af5-36de-b6c8-838d025c4fd8 | 2.16888 | -61.25259 | 2025-03-26 01:24:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe87ff20-9c46-39bd-987d-77b888892ced | 2.17112 | -61.82247 | 2025-03-26 01:24:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4517b1f2-ed61-3bf9-bfa0-33ca7d0a0268 | 1.52544 | -60.71497 | 2025-03-26 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b414ea2b-1783-3ba1-a476-495a9e11f717 | 1.90569 | -60.16315 | 2025-03-26 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 515fd560-d08f-3fb1-be6b-3dc495baf64d | 2.56862 | -60.69752 | 2025-03-26 01:24:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 6658e6f3-3d82-3c93-b5c3-332195ca58ad | 2.04709 | -60.74125 | 2025-03-26 01:24:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0f836d05-9209-3775-b371-48f9084a81ae | 2.10709 | -61.82802 | 2025-03-26 01:24:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f15e9143-e6b0-30f1-af27-f55f87c983a4 | 1.81654 | -60.87414 | 2025-03-26 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c48a7dd1-f4a6-3ff0-87e4-6fdc8facaf77 | 2.61327 | -61.50098 | 2025-03-26 01:24:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c175d034-5c6d-3429-8943-6437b0f4280e | 1.83461 | -60.87669 | 2025-03-26 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.4 |
| ab3499d8-9789-3bb2-8041-e65cab6a9e66 | 1.95746 | -60.65757 | 2025-03-26 01:24:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f68c8eb2-9282-3c29-baa5-810c749162ff | 1.37015 | -60.3759 | 2025-03-26 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0c0e896f-e90e-3d10-a0dc-d94e232d97a9 | 2.19129 | -61.8152 | 2025-03-26 01:24:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ab898a9e-0c93-3a2f-81c4-fcff207dbd08 | 2.39231 | -59.9114 | 2025-03-26 01:24:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5ead7c93-d991-3ec1-91a8-42043393d40f | 1.95618 | -60.66665 | 2025-03-26 01:24:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d47a52d4-6ea3-30a2-b03a-b359449f7c79 | 1.94603 | -61.20256 | 2025-03-26 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7eaa8767-608e-35d2-ab84-71f1b4110a79 | 1.83331 | -60.88591 | 2025-03-26 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.8 |
| b247f954-0784-33bc-baa6-73aceb9f913a | 2.56093 | -60.68723 | 2025-03-26 01:24:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.7 |
| c30f2614-7f03-352f-8a67-200fcfb3dc42 | 2.31498 | -60.14317 | 2025-03-26 01:24:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 32abfb40-9d0d-3527-8373-1d04fbcc5309 | 3.98508 | -61.50786 | 2025-03-26 01:26:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 5c9d0463-4d20-3244-b8d7-cffe4b88857d | 4.67861 | -60.90411 | 2025-03-26 01:26:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e5be823a-df58-38a7-bfd0-bfd9212c79fe | 4.07059 | -61.5546 | 2025-03-26 01:26:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 837c413f-f793-37e2-afe2-e13661504e05 | 4.6685 | -60.91167 | 2025-03-26 01:26:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6d3aea83-85f4-3529-8c0e-dade14862bba | 3.97599 | -61.50658 | 2025-03-26 01:26:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 71632679-f7c1-361f-891e-1d201576d87c | 4.06149 | -61.55334 | 2025-03-26 01:26:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 20.1 |
| c1e070e2-0452-352c-9deb-187f1a65f0f8 | 4.65641 | -60.92241 | 2025-03-26 01:26:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ab8194e2-adbe-3af0-9332-27c5ae8516b0 | 4.07191 | -61.54524 | 2025-03-26 01:26:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 013f5f89-4871-359a-9162-98be292b6e6a | 3.98758 | -61.55603 | 2025-03-26 01:26:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bfcab084-d0f9-38d2-9d93-513a9fb77504 | 4.65764 | -60.91354 | 2025-03-26 01:26:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 39c3e277-58b7-3441-9180-c549b486bf0c | 4.08747 | -61.56659 | 2025-03-26 01:26:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 83e70f87-81c7-3633-80bb-095ffaea220b | 3.99416 | -61.50916 | 2025-03-26 01:26:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 4917f7f9-67d4-31c5-9bfc-25a3bb53eb32 | 1.8317 | -60.8954 | 2025-03-26 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.1 |
| c62c6889-bb63-3f30-ac23-d6b57367d9cf | 3.9845 | -61.5054 | 2025-03-26 01:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 13b8c82e-ff70-3567-9abc-5b4b6bdf2a36 | 1.8135 | -60.8956 | 2025-03-26 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 962112d0-930b-3607-8fd8-d96ba7c3ff83 | 1.8317 | -60.8765 | 2025-03-26 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 128.5 |
| f7acf396-d361-357d-8536-739547be9157 | 1.8135 | -60.8767 | 2025-03-26 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 117.4 |
| c470df71-58fb-33fa-820e-211cb2820bb0 | 2.5618 | -60.6975 | 2025-03-26 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 6f3550a2-8dc9-3763-9709-a82c5abfcb32 | 1.8317 | -60.8765 | 2025-03-26 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 133.1 |
| d1646037-d4d8-3e14-84b8-1ba610407e89 | 1.8135 | -60.8956 | 2025-03-26 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 7a25dd37-3374-3fd0-8072-e9e7d835431a | 2.5618 | -60.6975 | 2025-03-26 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.5 |
| c012d2e2-a52f-3428-9b5e-f042bf4e5757 | 1.8135 | -60.8767 | 2025-03-26 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.6 |
| f2dfb669-9e8e-31d7-a30c-d245db2d4d04 | -20.3005 | -50.0138 | 2025-03-26 01:40:00 | GOES-16 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.1 |
| 21f0543c-00cf-3d23-b755-f6274d751d77 | 1.8317 | -60.8954 | 2025-03-26 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.6 |
| ae7dfe4a-cb86-368d-b073-8c717871aaed | -20.3005 | -50.0138 | 2025-03-26 01:50:00 | GOES-16 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.4 |
| 730e4d3a-960b-32fd-872e-5343ddd56d09 | 1.8317 | -60.8954 | 2025-03-26 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.8 |
| c60a79d0-87e6-3c75-a7d6-cfa470b0c4cf | 1.8317 | -60.8765 | 2025-03-26 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 136.8 |
| b481751b-3eb0-34cd-bd7e-20ed50c65551 | 1.8135 | -60.8767 | 2025-03-26 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.2 |
| e90a7382-bccc-3076-876a-1d882463250e | 2.5618 | -60.6975 | 2025-03-26 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 91907679-589e-3bc8-9ca7-64dde8387d85 | 1.8135 | -60.8767 | 2025-03-26 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 89df9d05-1f0a-324d-b5b7-3e61568944a4 | 1.8317 | -60.8954 | 2025-03-26 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| ad982fcb-c7a8-31cc-b22d-4f3006f2daa6 | 2.5618 | -60.6975 | 2025-03-26 02:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 86.0 |
| bb37fabc-fd86-3a3e-9356-a24e9fad09bf | 1.8135 | -60.8956 | 2025-03-26 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 537e9d15-294e-3257-b3fe-6c77a6901e15 | 1.8317 | -60.8765 | 2025-03-26 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 257e5aa7-e0f1-36c1-9ff1-bed46901e7b8 | 1.8317 | -60.8765 | 2025-03-26 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 111.1 |
| b677fbe2-ed3a-32ff-b113-23e86270f3fc | 1.8317 | -60.8954 | 2025-03-26 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.4 |
| a09c6b43-bc32-3932-8b32-b582f5b21e46 | 2.5618 | -60.6975 | 2025-03-26 02:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 75ef46a5-cd39-3e62-b660-668d3156eeac | 1.8135 | -60.8767 | 2025-03-26 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 9cc9951f-1207-3218-9201-2bb7f6b0dbef | -17.8658 | -39.8648 | 2025-03-26 02:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 64.3 |
| 72e08bf0-e6db-3c09-af4f-670f9252039a | 2.5618 | -60.6975 | 2025-03-26 02:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 79e66953-8036-3311-acac-58fb4e2b6116 | 3.9845 | -61.5054 | 2025-03-26 02:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 71358ac1-6e7a-3071-8023-555a68029ed2 | 1.8317 | -60.8765 | 2025-03-26 02:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.0 |
| c8025887-75d0-3d47-b0e3-7dde19db13e3 | 1.8135 | -60.8767 | 2025-03-26 02:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 50f683e1-a0fa-3f99-9a45-39599d3406e2 | 1.8317 | -60.8954 | 2025-03-26 02:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| b7ad296e-ad15-33fc-986b-bb10723bf751 | 1.8317 | -60.8954 | 2025-03-26 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 7d208a98-4997-3b29-bb51-bac588fa3b52 | 3.9845 | -61.5054 | 2025-03-26 02:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 54.4 |
| a163a0cc-3b9f-37f4-a1cc-59cee8cd9174 | 1.8135 | -60.8767 | 2025-03-26 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 98353b80-c64f-31c1-80f1-a3d01715f428 | 1.8317 | -60.8765 | 2025-03-26 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 98999057-6b0a-36a5-8fb7-fb54c0ac9754 | 2.5618 | -60.6975 | 2025-03-26 02:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 74011209-e481-3973-a96d-ee01cc86c540 | 1.8135 | -60.8767 | 2025-03-26 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 327f7e0c-fd8d-316f-97f8-43536c7b7cd5 | 1.8317 | -60.8954 | 2025-03-26 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 677de6f0-33f4-3eaa-a216-06f78688cf3b | 1.8135 | -60.8956 | 2025-03-26 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.3 |
| fa220285-9c69-3929-80c8-21a74a5f2b57 | 1.8317 | -60.8765 | 2025-03-26 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 42dbbea0-5f54-35a1-aac3-5a6c98e9cbe3 | 2.5618 | -60.6975 | 2025-03-26 02:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 6864e2b3-27be-39f9-88d6-4d000140c89b | 1.8317 | -60.8954 | 2025-03-26 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 2c3967d4-1159-346d-84e5-f0ad1b4ec6d8 | 2.5618 | -60.6975 | 2025-03-26 02:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 46c834f8-38fb-38d6-94bb-2e8c8ee76153 | 1.8317 | -60.8765 | 2025-03-26 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 8e994e3d-5f71-3964-bb55-7de637e05c07 | 1.8135 | -60.8767 | 2025-03-26 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.2 |
| aa8127b1-1bb4-31d5-8fb7-293c1575a32d | 1.8135 | -60.8956 | 2025-03-26 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 5f613e45-3acc-3395-bde3-004e4b0fe714 | 1.8135 | -60.8767 | 2025-03-26 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.2 |
| f617237f-75e5-3aca-8743-60a331c20c13 | 1.8317 | -60.8765 | 2025-03-26 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 81289ec2-fc40-3914-9aa5-009726bbaa1a | 2.5618 | -60.6975 | 2025-03-26 03:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 4e08db81-014d-36b5-8f71-876588bc969f | 1.8317 | -60.8954 | 2025-03-26 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |


[Clique aqui para ver as próximas entradas](README3.md)
