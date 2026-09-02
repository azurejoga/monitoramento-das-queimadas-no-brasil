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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 496f7d56-1ea6-3c16-b3b5-0bd925ae010d | -6.93 | -45.7157 | 2026-09-02 14:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| f3db126e-c7c9-3f1c-9bb8-8f1bf8018b8d | -7.0057 | -59.2575 | 2026-09-02 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b5bf551c-80dc-3d29-a4c8-3125fc86b192 | -10.8624 | -45.3789 | 2026-09-02 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 3a8ad5b0-8bec-3dce-a8c8-47ab71e4f129 | -8.7115 | -47.5567 | 2026-09-02 14:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 42.6 |
| ff4e0bda-dfa4-3167-adf7-d28956e7c292 | -12.0741 | -47.1164 | 2026-09-02 14:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 152.6 |
| f5422ceb-1e4a-309f-9e36-ee07bd7ef2d3 | -3.2361 | -61.2359 | 2026-09-02 14:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f9593128-a047-38c0-a29c-b605c71825eb | -7.5139 | -60.7537 | 2026-09-02 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e5f5fde4-cf73-329c-8253-137a0f5edcad | -10.7268 | -50.6618 | 2026-09-02 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| b9b030ff-1e4b-350d-982e-35d03b08dcc9 | -7.2005 | -60.6897 | 2026-09-02 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 5a534b3e-7ae7-362f-81ed-6d782d97a9bd | -14.2989 | -51.7072 | 2026-09-02 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 0c530c24-64e7-35a9-a850-9d36407f1872 | -5.5833 | -60.1924 | 2026-09-02 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 7b6d7bfc-3b4e-30d1-b753-6f92f49b6657 | -11.0247 | -49.6656 | 2026-09-02 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| abe417ee-cade-3378-8e31-85fa4875ae9d | -11.1496 | -51.5708 | 2026-09-02 14:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 141.4 |
| c3135c75-f05e-3a32-8c4f-87b94363b471 | -6.8756 | -59.4171 | 2026-09-02 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 1dd42b5c-9391-3ff4-a222-19b29a58f25d | -9.1721 | -59.4823 | 2026-09-02 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 8ac6461a-a0ad-3104-b027-53afd8ee2e63 | -3.7533 | -59.3231 | 2026-09-02 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| ddd46a07-061c-3bef-8a38-10d7f37cde0e | -7.2006 | -60.6706 | 2026-09-02 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 5be0e064-eafb-30ea-8a2c-0477b1046e4e | -3.3452 | -42.8067 | 2026-09-02 14:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 9353d149-160f-39e8-a507-ada2be5ef381 | -7.2191 | -60.6699 | 2026-09-02 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 79a8807f-e3d0-347f-b0ba-af9564fae0f0 | -9.4349 | -45.625 | 2026-09-02 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 1d7c0837-881a-3b6a-b5a4-cd4a833290b8 | -11.0434 | -49.6851 | 2026-09-02 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| e8a08aee-81f9-3977-9b69-f36769e231fa | -10.7199 | -47.1812 | 2026-09-02 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 9306cf01-b50c-33ec-8b5b-261fdffc7c1f | -6.9113 | -45.7172 | 2026-09-02 14:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 0bff963b-8fa4-36b9-8d74-1cbe1ef1e178 | -5.5648 | -60.2121 | 2026-09-02 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| bccb4ee8-f310-3a23-b9ce-59b2bf57bd8b | -9.6633 | -48.2721 | 2026-09-02 14:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| ef58a362-cd37-3016-94e6-b56110ed6545 | -11.0244 | -49.6872 | 2026-09-02 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 732c3984-810d-3058-b030-08b0a6704910 | -8.9111 | -62.353 | 2026-09-02 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 48a7f286-0265-39de-9eee-e198e28eba11 | -8.7615 | -62.5679 | 2026-09-02 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 95c0e832-1877-36e7-9753-4a4b9182710f | -13.9855 | -58.672 | 2026-09-02 14:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 140d7ce0-b781-3b4f-a0b9-7b53ab6275fa | -9.0243 | -65.4554 | 2026-09-02 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 857aaad1-9af6-3f12-89f5-49054110abca | -13.5724 | -59.7362 | 2026-09-02 14:50:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| b0cba352-379c-349c-ab81-42bb6a6734b4 | -13.5533 | -59.7377 | 2026-09-02 14:50:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 65032573-fd13-30fc-9075-2f8924b6273d | -13.9853 | -58.6919 | 2026-09-02 14:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 2370c5a3-8441-36cb-a5b9-617261a2d9ad | -7.3302 | -60.589 | 2026-09-02 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 5ba46f82-5de6-3393-81ae-78d83b10a4d5 | -7.0242 | -59.2374 | 2026-09-02 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 87eeb1f4-ee2e-3a8c-baf6-6a2b28ff57c9 | -6.3894 | -45.4664 | 2026-09-02 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| e9d385c7-0991-34b5-9af9-90f57d7b46ff | -6.3892 | -45.489 | 2026-09-02 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| db526391-9c00-3f52-bc21-810aadad36c1 | -7.3118 | -60.5897 | 2026-09-02 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 99ed1718-ca77-3e93-8e16-7a69c7859baf | -9.0244 | -65.4367 | 2026-09-02 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 73a775cc-f7cc-312c-84d0-21c4b9bdb63b | -12.1704 | -47.0806 | 2026-09-02 14:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 2e01b194-55ac-3ef9-b9d4-4cee6bcfcbfe | -12.3626 | -48.1459 | 2026-09-02 14:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 37dd855b-a50e-3c07-bfe1-c7bb944e21a5 | -9.1719 | -59.5017 | 2026-09-02 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| e6f00586-4816-3d55-838b-6929ea9d92fa | -9.8806 | -64.9764 | 2026-09-02 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 5f61cccd-74b7-34af-9ff3-746f7a8d2d94 | -11.3579 | -45.4027 | 2026-09-02 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 1da4f56a-3a98-3f56-80e4-e2864107d08f | -7.2536 | -61.1074 | 2026-09-02 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 2a740850-c3be-3db0-8852-b4526a327a62 | -3.6216 | -60.547 | 2026-09-02 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 92e5b191-e6f5-39ed-a5bf-9c3cd16a6c3a | -5.9635 | -57.6899 | 2026-09-02 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| ec211bc6-3057-3701-8247-338e860299b5 | -13.5531 | -59.7574 | 2026-09-02 14:50:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 80a24153-a688-3c4a-ac76-8b169e5f638f | -10.5788 | -47.7306 | 2026-09-02 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 230.1 |
| 1c54dbce-bd2c-3aa8-b69c-1d75c6066300 | -3.2361 | -61.217 | 2026-09-02 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 8aafbb72-59c1-31f1-b5d6-db03cb8c4047 | -12.1504 | -47.1283 | 2026-09-02 14:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 065d49e4-055b-3df6-858a-a772053c3cca | -7.3487 | -60.5883 | 2026-09-02 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 3abb82d8-712e-3efb-aa59-2cffa1fc4c09 | -7.566 | -61.343 | 2026-09-02 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 171b368d-d01c-33c0-b400-0a978e165663 | -3.6215 | -60.566 | 2026-09-02 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 6e18bb36-2f39-33d2-90ff-cf18833bbf4d | -3.3688 | -59.3887 | 2026-09-02 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 25f5cbea-4bd4-38bc-aee5-d22c92199d73 | -8.7613 | -62.5869 | 2026-09-02 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 0da752d2-4faf-3d8b-8d01-837a9d3d95d1 | -13.9664 | -58.6736 | 2026-09-02 14:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 199.0 |
| f9911883-2803-3116-80ea-a1be0bcc2b67 | -17.0878 | -56.8534 | 2026-09-02 14:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 135.3 |
| 25613acc-83af-337a-89ca-3d0d50f15432 | -1.0182 | -53.7189 | 2026-09-02 14:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 6d05decd-9505-374b-99a2-2ce1e1a8e15c | -10.696 | -46.2646 | 2026-09-02 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| db2a3ca1-67f8-31dc-940e-fb55355a0ff2 | -7.856 | -45.1792 | 2026-09-02 14:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 44.4 |
| f5cd8672-3826-3120-859d-4c81f123a5f0 | -5.5832 | -60.2116 | 2026-09-02 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 149.9 |
| cb8e32b8-983b-31fd-98dd-8fa8b37fc0b4 | -7.3117 | -60.6089 | 2026-09-02 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 5a593ed6-887a-3092-ba60-2f340577d187 | -11.1117 | -51.5748 | 2026-09-02 14:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| adfb72fa-7b90-369c-a405-a3b2d9490105 | -7.5659 | -61.362 | 2026-09-02 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 04cd38e0-df70-33ce-9204-10127adcbfdd | -9.8805 | -64.9951 | 2026-09-02 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| ed2d392f-eaea-33bd-a5b3-a4c57c085d39 | -6.7123 | -58.9412 | 2026-09-02 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 8b7d0c31-e371-357b-ae85-2f80da0f9787 | -8.7628 | -46.4642 | 2026-09-02 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 7e0c82de-3524-349c-af8a-9406e2e7b37f | -12.3622 | -48.1681 | 2026-09-02 14:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 5f55ea2b-1608-329b-9265-63ac6d8179a3 | -6.6883 | -59.9436 | 2026-09-02 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 7b19425e-c4d3-3e61-878d-ac42263c3b6d | -10.7839 | -50.6346 | 2026-09-02 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 7a321840-317f-3c41-84e3-e4677d5cf4c4 | -11.0247 | -49.6656 | 2026-09-02 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 57055b2d-aeed-3e3a-b0b1-cc06549c6f96 | -6.3892 | -45.489 | 2026-09-02 15:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 5135008e-6913-31a9-a36d-dc3e495fa549 | -7.2192 | -60.6507 | 2026-09-02 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 80801906-c644-3255-9720-239895dc4a40 | -5.5648 | -60.2121 | 2026-09-02 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 754b2de0-e844-3df9-a104-a4ab339f0975 | -6.931 | -56.4496 | 2026-09-02 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 6a36fa14-e2cf-350f-979b-6904e757425f | -13.9855 | -58.672 | 2026-09-02 15:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 2bce7e3f-573d-35af-930e-cdc1558e8cda | -6.8756 | -59.4171 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 1678cae5-68c1-33c9-a1ac-2ecd77764865 | -13.5533 | -59.7377 | 2026-09-02 15:00:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a67e3ec9-f094-3651-908a-4a34a5b65d27 | -17.0878 | -56.8534 | 2026-09-02 15:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.8 |
| f0ca3061-cc2a-3eb2-a72c-516b7ad9f7c6 | -7.0428 | -59.2173 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 1d3a7dd2-6e31-3fd1-b9d0-9dde7f7d23bc | -6.8613 | -41.6532 | 2026-09-02 15:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 0a5af025-1836-350a-b3e7-d93de92b0caa | -7.0057 | -59.2575 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| d4f058c4-4cb0-3997-a76d-131eef94f97d | -7.3672 | -60.5875 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 62be5f92-7c0f-3355-835b-3c1d5fd974df | -8.7814 | -46.4847 | 2026-09-02 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 34f26aee-3ee1-3913-bfa0-a6f619c1914b | -3.3871 | -59.3883 | 2026-09-02 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 08bccf38-192e-30f8-9d53-9c457e3b1d3d | -12.1457 | -44.196 | 2026-09-02 15:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 778e55b4-7fd8-3ed9-8e8f-7e9f2d00e435 | -3.6215 | -60.566 | 2026-09-02 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 130.7 |
| b9dcfe71-c03e-36a5-b078-ec1a6335b1ee | -3.8446 | -59.3977 | 2026-09-02 15:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 09d10db0-8402-31d5-8636-eb82adcd99c2 | -7.3302 | -60.589 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 34b55668-bbd4-3b04-ab4e-93f43ff0bef6 | -10.7268 | -50.6618 | 2026-09-02 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 1233ff28-d0c2-30cf-8c34-2a68b6d7b9ae | -6.8019 | -59.4008 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| fa988c43-8a0f-3731-b22e-6464ec398e4c | -6.9872 | -59.2582 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 856a2293-37fd-3eac-9ab0-17bfd94b6463 | -12.0737 | -47.1389 | 2026-09-02 15:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 0005de06-dc94-3d56-a96e-ed0bcfe3732e | -8.7115 | -47.5567 | 2026-09-02 15:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| af68e995-1ab0-3a04-96d4-0c702edadad0 | -10.7454 | -50.6812 | 2026-09-02 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| abd87c48-c1cd-35ff-8f23-2313a5d3a8d0 | -9.862 | -64.9771 | 2026-09-02 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| e99826c7-e94c-332f-a60a-23beb8bc0ee7 | -10.4145 | -49.9898 | 2026-09-02 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 204.4 |
| e9603571-8c6a-3cac-ade4-170e8c08a4dd | -13.9664 | -58.6736 | 2026-09-02 15:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 163.3 |
| f6e44df1-df34-31f2-aa38-09cf98df2520 | -6.6883 | -59.9436 | 2026-09-02 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |


[Clique aqui para ver as próximas entradas](README82.md)
