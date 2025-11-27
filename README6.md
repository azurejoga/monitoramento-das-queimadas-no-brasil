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
| 40953348-da5c-3e63-9e3d-3f0d24eb7bbf | -6.10416 | -44.70359 | 2025-11-27 05:50:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3d28dcd9-9d72-3757-9b2e-6a1299145459 | -7.5004 | -45.71325 | 2025-11-27 05:50:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 18606cb9-f65f-3119-b01c-804ff554b768 | -4.57075 | -43.29062 | 2025-11-27 05:50:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ae3f692e-f5ec-3666-a482-63f158dddbcd | -4.67256 | -47.1679 | 2025-11-27 05:50:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 928fe90f-767f-3486-b94a-0da1df93da7a | -8.03204 | -43.14452 | 2025-11-27 05:50:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| aecd9460-e1bb-34e4-8136-39c810400c9e | -6.89554 | -42.84785 | 2025-11-27 05:50:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c98f09c7-84f5-3ca8-a2c6-cfea68133735 | -4.71506 | -46.4516 | 2025-11-27 05:50:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ec5c40bc-747c-3b69-a8e4-56d1e4e65724 | -4.71314 | -46.46399 | 2025-11-27 05:50:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5c725cb1-04e7-3cfc-a85d-5cc92bbf8dc2 | -4.83184 | -44.0685 | 2025-11-27 05:50:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a9cfd5e4-f500-3052-b987-261c4d7d940e | -5.7078 | -47.05312 | 2025-11-27 05:50:00 | AQUA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7e05bba2-77cb-3e10-a337-277258ec450f | -5.69929 | -47.03871 | 2025-11-27 05:50:00 | AQUA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 94b79bf5-bd93-3b87-8aa1-d7f6a58907d0 | -4.05058 | -46.56245 | 2025-11-27 05:50:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2078d34a-30be-393e-a633-0825108400f8 | -4.00661 | -46.98778 | 2025-11-27 05:50:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 60124912-d242-396d-be49-6ed9ccd7f3ce | -5.69718 | -47.05194 | 2025-11-27 05:50:00 | AQUA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| e59e315f-e448-399e-83db-20d55a7e4a64 | -5.98029 | -44.60215 | 2025-11-27 05:50:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b1c0c94c-f553-37d5-b536-2d8824feb03d | -4.83322 | -44.05935 | 2025-11-27 05:50:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c679f46f-0b89-384a-b126-16e14240e61f | -3.81331 | -47.04505 | 2025-11-27 05:50:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b180a434-9110-3483-a4f2-2c8049b1300c | -7.50979 | -45.71468 | 2025-11-27 05:50:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 925254b4-2251-34d2-a048-2ed938dd8b36 | -8.04453 | -43.1349 | 2025-11-27 05:50:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 6561dbba-e428-3991-b352-3dfab840afa7 | -8.03337 | -43.1357 | 2025-11-27 05:50:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| d7a871dd-57b6-3fde-b88e-aba282498bab | -6.89686 | -42.83904 | 2025-11-27 05:50:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6298677f-400f-3254-8c6e-800be1387058 | -13.47973 | -46.69466 | 2025-11-27 05:52:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8201fb3f-69bd-3fcc-bc35-b0dca028e114 | -13.47816 | -46.70464 | 2025-11-27 05:52:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| c6adffcf-945b-3727-bc28-03d1d7b87141 | -8.38441 | -44.00896 | 2025-11-27 05:52:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fb6fb6d1-35df-3eb5-848a-428b1e2bd84a | -13.40266 | -51.15387 | 2025-11-27 05:52:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 80a1939a-7684-3a58-9223-5b631a573ff6 | -13.40024 | -51.16632 | 2025-11-27 05:52:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 6130dd2a-295c-3f04-aed4-898db6a86508 | -13.40366 | -51.14655 | 2025-11-27 05:52:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 70ef8ce9-7ef5-3bc8-a373-8bf5bdfd0ee4 | -21.70836 | -49.98234 | 2025-11-27 05:54:00 | AQUA_M-M | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.6 |
| 03b8938b-bc41-3352-956d-7e76e0c769bc | -3.5269 | -43.6828 | 2025-11-27 06:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 60795259-2aec-3c97-903e-0d77e768b801 | -3.5269 | -43.6828 | 2025-11-27 07:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 8f8470e2-3efd-30d5-acf0-4866ab94fa2a | -3.0726 | -45.1405 | 2025-11-27 07:40:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 2eaab749-7e72-3e4a-a3fe-35f56148d333 | -3.0726 | -45.1405 | 2025-11-27 07:50:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 72185d72-4863-3303-8e21-aab68aaa706a | -3.054 | -45.1412 | 2025-11-27 07:50:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 94b65360-b56a-36ba-84ec-170c37fae381 | -3.0726 | -45.1405 | 2025-11-27 08:00:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 642f9900-5be7-3dee-b896-c703cd336512 | -3.3883 | -45.2406 | 2025-11-27 09:00:00 | GOES-19 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 127.3 |
| b489ce2f-9778-3388-a75a-ca95ff6caf5d | -3.3883 | -45.2406 | 2025-11-27 09:10:00 | GOES-19 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 6fc24612-e858-3440-9f10-e27d1ec51a7e | -3.3883 | -45.2406 | 2025-11-27 09:20:00 | GOES-19 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 7533ad9b-5e47-376a-83af-2543491bea65 | -4.0199 | -42.4431 | 2025-11-27 10:40:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| c29701f0-99f9-3ffb-9ef2-cda29662d896 | -4.0198 | -42.4667 | 2025-11-27 10:40:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 4393be86-49fc-366a-a593-a5daece254b3 | -3.5269 | -43.6828 | 2025-11-27 10:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 155.4 |
| e9f09b00-9f16-3c38-9cd7-e603a63c5b97 | -4.0199 | -42.4431 | 2025-11-27 10:50:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 9af5cc2b-8aac-3f04-a530-31233378a19b | -4.0199 | -42.4431 | 2025-11-27 11:00:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| e5dfb6ce-5f2d-35d6-8147-d5dd78aa6cc5 | -4.0198 | -42.4667 | 2025-11-27 11:00:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| ffcb4124-d700-30c0-8690-f9286b027f8a | -4.0199 | -42.4431 | 2025-11-27 11:10:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 102.7 |
| 77021625-8718-3198-a8af-08897ba925f2 | -4.0198 | -42.4667 | 2025-11-27 11:10:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 77.4 |
| f4125e75-2e99-3b3d-9ec9-6ee764d7331c | -4.0198 | -42.4667 | 2025-11-27 11:20:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 8cc402c7-c26f-3480-9aac-76fc6c9f40bf | -3.5083 | -43.6837 | 2025-11-27 11:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 0f5d329d-b43c-357a-8bcd-9e822917a1b0 | -4.0199 | -42.4431 | 2025-11-27 11:20:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| efbbd91b-e254-35cc-aef4-815a4789af49 | -4.0198 | -42.4667 | 2025-11-27 11:40:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 438aa9f8-674b-3ffe-9038-5c362b2954d0 | -4.0199 | -42.4431 | 2025-11-27 11:40:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 4cd18836-a3de-333a-b7cb-6fe5b513019e | -3.5083 | -43.6837 | 2025-11-27 11:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 4927a521-d9a0-347e-bc5f-69863f45f51a | -3.5269 | -43.6828 | 2025-11-27 11:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 4ca2c208-417b-3a90-8b34-0c03e5a3fe37 | -3.5269 | -43.6828 | 2025-11-27 11:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 1dc583da-8858-39a2-ae8d-3deda433322f | -4.0199 | -42.4431 | 2025-11-27 11:50:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| be55c058-6f1d-3ffe-9c49-f0dae2d98941 | -3.5083 | -43.6837 | 2025-11-27 11:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 97ec16b3-d506-3876-bc2b-d15a2c0ea4b0 | -3.5083 | -43.6837 | 2025-11-27 12:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 128.1 |
| fabcd69d-adac-3c80-9987-d08a5f959614 | -4.0198 | -42.4667 | 2025-11-27 12:00:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| 594669be-4e08-3583-aea9-8ed1047abc35 | -3.5269 | -43.6828 | 2025-11-27 12:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 191.4 |
| f4f1534a-3f1d-35e3-8ad6-d0ae8fe3620e | -6.4968 | -38.8522 | 2025-11-27 12:10:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 38d7f0b7-4ffb-343b-862d-d5415788b250 | -3.5269 | -43.6828 | 2025-11-27 12:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 207.5 |
| b6f5ef71-ce4b-3e27-953d-545617ff89a8 | -3.5269 | -43.6828 | 2025-11-27 12:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 195.6 |
| dc71bb98-3651-3356-a583-fcba296f9018 | -3.5083 | -43.6837 | 2025-11-27 12:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 5f8bf06b-672b-3e47-91ec-431a548ed78d | -3.5083 | -43.6837 | 2025-11-27 12:30:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 61e1c6f6-c351-3fb7-9ed1-68ce01d97a3b | -3.5269 | -43.6828 | 2025-11-27 12:30:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 7c94e42d-187c-32b2-8515-6fb763d44907 | -3.5269 | -43.6828 | 2025-11-27 12:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 172.4 |
| ac97aebf-f961-37c2-9d47-545eecf987d7 | -8.0703 | -43.0981 | 2025-11-27 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.1 |
| e68e130f-276e-36ab-a220-f39d20997a6e | -3.5083 | -43.6837 | 2025-11-27 12:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 6a489249-b481-3872-96d8-d1f00b64fcd3 | -6.9037 | -38.0928 | 2025-11-27 12:40:00 | GOES-19 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 92.1 |
| d9b7a766-a826-3d17-9b1a-7d4f7b011fdb | -3.0125 | -42.1375 | 2025-11-27 12:50:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| daa18dc7-905d-3401-aaa5-7d418f2c0264 | -3.5083 | -43.6837 | 2025-11-27 12:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e69f04e7-e8a8-35c2-afb7-2d306de0a22c | -8.0513 | -43.1001 | 2025-11-27 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 167.3 |
| 21684a6b-4ac5-3d2d-9e98-b28aa285e57a | -3.5269 | -43.6828 | 2025-11-27 12:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 244.1 |
| 1b4c61d9-3bee-396b-9a99-a9d0f6873e53 | -8.0321 | -43.1257 | 2025-11-27 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| 593be20e-ed1d-3303-8da2-4042d64cc1e6 | -8.0703 | -43.0981 | 2025-11-27 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.0 |
| efd3a031-d7ee-3c8a-ad81-91bdeb70a244 | -6.4968 | -38.8522 | 2025-11-27 12:50:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 01b2a810-f8d9-3508-bebd-604d24323a77 | -3.0125 | -42.1375 | 2025-11-27 13:00:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 70d47a59-b1a4-3e58-a1ba-204ebc243603 | -6.9037 | -38.0928 | 2025-11-27 13:00:00 | GOES-19 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 125.7 |
| e939f6c6-0aed-3d8a-a5f7-fc58f429f47e | -3.5083 | -43.6837 | 2025-11-27 13:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 1b730acd-658b-32e2-83db-09d782650da2 | -6.4968 | -38.8522 | 2025-11-27 13:00:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 98.5 |
| 49b56e03-eeb7-3bac-9522-0c16c40d35a1 | -3.5269 | -43.6828 | 2025-11-27 13:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 163.8 |
| d909eb53-c449-37b9-9b14-202c4fcf67dc | -6.4968 | -38.8522 | 2025-11-27 13:10:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 121.0 |
| b3b75087-c220-3abc-9f73-8a6d038edcfe | -3.5269 | -43.6828 | 2025-11-27 13:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 499.8 |
| 90f7b3be-2329-3d12-9c2d-30bc409a9328 | -3.5083 | -43.6837 | 2025-11-27 13:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 180.8 |
| d9854b17-c7fc-3e75-960e-0e503984908b | -8.3982 | -44.0204 | 2025-11-27 13:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 4a9a4f44-8a83-3875-9382-e3dce8877043 | -7.4894 | -42.7586 | 2025-11-27 13:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 87dfa621-880c-3b18-ae46-087969972bea | -3.0695 | -41.9451 | 2025-11-27 13:10:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 7123120c-09c2-3a53-87fa-d5760fd65524 | -4.4246 | -43.4038 | 2025-11-27 13:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| e2e23ef9-5891-3747-8d0c-3ca002db43ac | -7.4894 | -42.7586 | 2025-11-27 13:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 0fccfdb7-30d9-3365-ae92-b92a0656be79 | -3.8768 | -44.4242 | 2025-11-27 13:20:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 12fb796c-00d0-312b-84de-377ebf001faf | -6.4968 | -38.8522 | 2025-11-27 13:20:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 114.0 |
| f29685ca-c669-3ef5-b012-5c5faf48d8e9 | -3.5083 | -43.6837 | 2025-11-27 13:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 184.2 |
| 8a4a6767-ccf3-3e9c-9da9-40fe601c22c9 | -3.0695 | -41.9451 | 2025-11-27 13:20:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 19aed63f-fe2f-35a1-8028-a56877d51580 | -3.0608 | -43.703 | 2025-11-27 13:30:00 | GOES-19 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 698a5ca0-2c12-3731-afa5-80439b82bcd5 | -3.4799 | -42.0925 | 2025-11-27 13:30:00 | GOES-19 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 3fed4700-4940-32a7-90e8-e99dd0992c85 | -4.4246 | -43.4038 | 2025-11-27 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| e8c8d612-79c0-3d43-848b-14db7be1ebb6 | -6.4971 | -38.8268 | 2025-11-27 13:30:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 123.3 |
| 276ad9f2-782d-3c39-b7a3-b5846c62b2f3 | -4.9474 | -41.1653 | 2025-11-27 13:30:00 | GOES-19 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 3d35af77-bad6-388f-805e-608bdc90d68b | -6.4968 | -38.8522 | 2025-11-27 13:30:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 194.6 |
| 431d4d0f-2567-3457-ab43-d13d917aa48d | -8.0507 | -43.1472 | 2025-11-27 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 93281067-2eb4-36d3-9f0f-201d50898d55 | -4.4246 | -43.4038 | 2025-11-27 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |


[Clique aqui para ver as próximas entradas](README7.md)
