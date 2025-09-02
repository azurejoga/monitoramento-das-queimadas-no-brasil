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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3da6c05b-2f38-3841-90fb-37ceb0e47e17 | -11.6527 | -52.191 | 2025-09-02 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 6d19ce08-df38-3d84-a932-208c4b2ae1f8 | -8.6882 | -62.4192 | 2025-09-02 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 67909a54-655b-3a38-bd50-214bb7e01875 | -11.6717 | -52.189 | 2025-09-02 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 63ead01f-4141-3626-adcc-16bdded6719b | -7.484 | -44.8272 | 2025-09-02 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| ce8904ec-f359-311e-9b8b-9bd11be4da5f | -6.2771 | -43.5279 | 2025-09-02 14:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 4fdd8d57-c7b6-303c-89b4-d1e65f368dc0 | -6.3504 | -45.6273 | 2025-09-02 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 142.2 |
| ef87fe62-6396-3efa-a2d1-38712bd5d523 | -6.666 | -45.8946 | 2025-09-02 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| bf575627-5580-3366-bf64-f909abe0859a | -12.9197 | -56.9471 | 2025-09-02 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| cf0abae7-d3d9-3cd0-84f2-f6ea0b2c68a4 | -6.982 | -44.346 | 2025-09-02 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 004ef471-31ed-3f60-a032-e833bb545ada | -8.1995 | -44.8023 | 2025-09-02 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 7c9ba804-55b6-3cbe-96c2-52d6e149fc58 | -8.6132 | -62.5739 | 2025-09-02 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 23d8f329-2927-3fe7-bded-217f4107e730 | -7.1091 | -44.7474 | 2025-09-02 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| dc587b73-526f-36c6-a931-4086620c5623 | -10.8947 | -50.8356 | 2025-09-02 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 5489a6ae-b5a5-371a-8fe7-e1f4a30a405a | -11.9224 | -50.6153 | 2025-09-02 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 8d592747-b34a-3c91-b381-0f246fe2be11 | -12.9192 | -56.9873 | 2025-09-02 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 158.4 |
| 0b93dc5c-f9a0-36de-ae7c-d7f1928dc5dc | -12.0066 | -51.351 | 2025-09-02 14:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| cd735656-f05c-31b0-9d51-7a159789471f | -7.5477 | -61.3247 | 2025-09-02 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 312.9 |
| 88509dcd-1812-3ded-b265-b9011464e575 | -7.9351 | -46.4559 | 2025-09-02 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| cf823429-8c02-32c3-a0a7-514dc6624bf3 | -12.7734 | -47.6666 | 2025-09-02 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| b33c3d75-ffa5-36f4-86e5-98e8d0e6c4b7 | -6.2794 | -43.2945 | 2025-09-02 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 88461aea-3bae-3916-9c75-e434e863921f | -8.5758 | -62.6323 | 2025-09-02 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 7686b35d-ab67-3358-bcc1-1ccdbf1ac3a5 | -6.2038 | -43.3475 | 2025-09-02 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 131.4 |
| fe79de51-be24-3bb2-b2ca-03dd04d9ff7e | -4.8936 | -43.1882 | 2025-09-02 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 72e23c23-3b7a-3e9b-8179-6b153f8c3c4b | -8.4024 | -48.2646 | 2025-09-02 14:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 127d6389-67fd-3de9-85e9-1cfa9c447a60 | -9.7294 | -48.9834 | 2025-09-02 14:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 5e6d5e1e-260f-38ec-be74-b5017228e73b | -11.1037 | -44.6315 | 2025-09-02 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 183.8 |
| db51e397-c008-3c6c-acd1-fc5d58a0c5ec | -18.0723 | -45.9553 | 2025-09-02 14:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 858cbcbf-9df3-319b-a902-175e4e08a4ad | -5.6571 | -43.6697 | 2025-09-02 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| eff703f4-f327-3c0b-88bb-2c8c3f1f3f83 | -10.0623 | -48.0978 | 2025-09-02 14:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 4c116a71-765b-3e09-a685-cb7f661cff1f | -6.3319 | -45.6062 | 2025-09-02 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 199.1 |
| fe025650-2a67-3eda-b8ca-618bb34fecd0 | -6.9754 | -43.2326 | 2025-09-02 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 205.7 |
| d0936a06-100a-3d6a-865f-c99668ac3f4f | -7.1089 | -44.7703 | 2025-09-02 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 73f077e9-15d5-33a6-99d5-42e75279986f | -11.3901 | -43.5602 | 2025-09-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 5c14f3f5-a468-351f-a693-37fedc80200c | -5.7168 | -45.4035 | 2025-09-02 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 262.8 |
| 874cd99c-5f5f-3ce8-bb2d-71977b337296 | -6.0514 | -45.6048 | 2025-09-02 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 2ae525d2-8f52-3904-8b38-3cf5d18fa8b0 | -5.8882 | -42.9988 | 2025-09-02 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 144.2 |
| 38fb8e7a-d2bf-315d-ab16-1086cd7af5ab | -9.4498 | -62.3294 | 2025-09-02 14:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| e49edbd8-2547-31b8-bcd1-88a2117665a6 | -14.5662 | -53.0081 | 2025-09-02 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 8028a3b5-b64b-35fc-a1cb-9ccfdb7a49da | -11.1252 | -50.5982 | 2025-09-02 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 9fdc0e59-4c99-339e-994f-9854443d416a | -8.6169 | -61.9473 | 2025-09-02 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a5675755-274a-3244-a630-9b78ea87fb30 | -5.8642 | -45.6408 | 2025-09-02 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 9296f616-dd97-3c92-bb9c-494928f6a334 | -6.8911 | -45.8538 | 2025-09-02 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 95f18238-145c-3602-9362-95371fb697d5 | -6.9629 | -44.3707 | 2025-09-02 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| ba2bf195-37c1-3d79-a45d-bd039049943b | -5.9037 | -43.3485 | 2025-09-02 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 0f898114-41e2-3009-bebf-caaa4465561f | -9.1909 | -59.4619 | 2025-09-02 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 9d2fb44b-dc3d-3183-b49f-6f606a2d5b9b | -6.4443 | -43.6998 | 2025-09-02 14:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 22a21fdd-cd60-3da4-9093-2bc8893da9c2 | -4.8936 | -43.1882 | 2025-09-02 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 218.2 |
| 6a72de5e-903c-397e-8baf-97060fb419c8 | -7.4966 | -45.3722 | 2025-09-02 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| f4adc468-9bf4-3b55-ad37-928878b460c1 | -8.2198 | -49.5115 | 2025-09-02 14:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 1213e153-51c2-34c0-9643-da9771384fa7 | -8.3291 | -44.9948 | 2025-09-02 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| d67b086a-cc81-36e9-864e-abf6e4e1a641 | -12.0069 | -51.3298 | 2025-09-02 14:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| f6866ed6-4a8a-319c-a18b-a596445fd3c8 | -11.8527 | -51.4742 | 2025-09-02 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 01e4c584-8c97-3f6b-a202-0331e4e9a3e9 | -9.5025 | -57.8032 | 2025-09-02 14:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 125.8 |
| f60e0d0a-842c-388e-bfda-e26989a00c91 | -8.5947 | -62.5747 | 2025-09-02 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 1b327066-eac5-3620-bdca-743abf1b6b01 | -5.8694 | -43.0003 | 2025-09-02 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 170.2 |
| 16fd925f-36fd-33b6-ace9-9110baf08f6b | -5.3974 | -43.3867 | 2025-09-02 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| a8477726-24ea-3feb-9950-80bf25970002 | -11.3713 | -43.5394 | 2025-09-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 1bd84710-f969-3eeb-b5ac-ea0ad969bb44 | -8.1995 | -44.8023 | 2025-09-02 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 7561b193-215f-36ec-91ae-7f02682c06d0 | -11.8583 | -52.4208 | 2025-09-02 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| df48266f-fa40-3a0d-ab91-3b382e160ec2 | -4.9122 | -43.2103 | 2025-09-02 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 149.9 |
| b6150c84-a9ac-3e98-bd0c-30d0282abe6b | -10.0623 | -48.0978 | 2025-09-02 14:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| dc6cccb0-f77e-3db3-b0ae-89c48ac5fd10 | -11.9879 | -51.332 | 2025-09-02 14:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 77a4338c-1c47-3e67-813c-ba87c7b5d28c | -5.6571 | -43.6697 | 2025-09-02 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 379521de-0e23-3df9-a828-5021a95b5405 | -11.853 | -51.453 | 2025-09-02 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 5ecf5173-0177-3608-b5cd-fd575481df62 | -12.2156 | -50.1295 | 2025-09-02 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 800bfa5f-91ee-3049-962c-a9d6f137a033 | -6.0699 | -45.6259 | 2025-09-02 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 5d8ff1eb-ec34-37b1-b70d-11a22223b09e | -11.6527 | -52.191 | 2025-09-02 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| dc9913cc-a6a1-34f7-a832-b7437f45b003 | -7.9163 | -46.4577 | 2025-09-02 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 1125e738-1dbd-395b-b0ee-5e94cecd4477 | -15.7366 | -53.6561 | 2025-09-02 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 1d8fcc64-4cb9-3f6e-8888-41578dcea703 | -8.4024 | -48.2646 | 2025-09-02 14:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 16dff11c-b8ec-3b5c-bcb6-472a8d296f30 | -7.4652 | -44.829 | 2025-09-02 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 2439b451-122b-3572-8eec-0253d5440123 | -7.4969 | -45.3495 | 2025-09-02 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 212.8 |
| 89a64a6e-b870-34fc-a830-8833aeffa466 | -6.9942 | -43.2308 | 2025-09-02 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 191.6 |
| a9da5724-6da9-3524-883d-b4bb58a01659 | -7.5476 | -61.3437 | 2025-09-02 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 282.0 |
| ee9b9b73-b217-3997-8fec-a0b81ab523b0 | -6.2221 | -43.3927 | 2025-09-02 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| c04c3ef9-7dd3-391a-9a5b-9d2d37b136f7 | -9.9411 | -51.6261 | 2025-09-02 14:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 49125cb4-c48a-321d-9631-778ee2c706b7 | -5.8644 | -45.6183 | 2025-09-02 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 26b12fd3-9633-365a-97d4-5e24fc1b1631 | -5.8111 | -43.2156 | 2025-09-02 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 88a1f4f0-3c75-3894-9976-0d0d296b6991 | -6.2583 | -43.5294 | 2025-09-02 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 69b51abb-4d86-35de-990f-2940cea20c1a | -7.6783 | -61.0908 | 2025-09-02 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 4985657b-9e4f-31ef-a277-96e4f0e0ac96 | -11.9224 | -50.6153 | 2025-09-02 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| cf3ad12f-13e8-3325-9406-964a9db413b6 | -5.8109 | -43.239 | 2025-09-02 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 48a7d690-219c-36e1-9d73-093b24054028 | -9.7483 | -48.9814 | 2025-09-02 14:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 216.6 |
| 8946a634-f0f7-333f-8729-e5127d6cdbee | -10.062 | -48.1197 | 2025-09-02 14:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 5e4c146a-e894-38e5-8607-e2d367ba4ee6 | -11.4488 | -46.8198 | 2025-09-02 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 7953ba28-b183-3773-88fc-c4c68e037673 | -12.216 | -50.1079 | 2025-09-02 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 638d3db5-7811-3dc6-b311-38246ca6f26c | -6.1848 | -43.3724 | 2025-09-02 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| eb7dd680-cf51-3608-a739-356ded1e8d58 | -11.1033 | -44.6548 | 2025-09-02 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 535.9 |
| 16f8e1af-b6dd-3c90-b43d-3b35d35f627f | -11.3893 | -43.6075 | 2025-09-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| a1a40fa8-f1ce-3de4-9725-965bd990d37e | -5.7004 | -45.1333 | 2025-09-02 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 68a07242-5cf6-3fa0-9649-89c8d39bdcb9 | -15.7363 | -53.6772 | 2025-09-02 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 3c62c711-1e14-3402-b89b-6a8a32276bce | -7.484 | -44.8272 | 2025-09-02 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 5cc9481b-0779-3c52-87fd-8501945e2ace | -9.7294 | -48.9834 | 2025-09-02 14:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 2371256c-b922-37d1-8f72-ef47d836bb46 | -8.4022 | -48.2864 | 2025-09-02 14:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 188.9 |
| ea554ca6-8337-3e09-8844-ed2f6f636bbb | -6.2771 | -43.5279 | 2025-09-02 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 719ca63a-8641-3b39-9720-bc0f22cd0363 | -11.3709 | -43.5631 | 2025-09-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 028426ff-cf5a-309f-8371-6a2422c2972e | -11.6715 | -52.21 | 2025-09-02 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 102.5 |
| a2c8099c-6dc4-3e9d-a2b7-356028bcd947 | -9.4981 | -46.5197 | 2025-09-02 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 228.1 |
| 40d9cbd0-c78a-3e25-9717-c656fb8a50cf | -6.2794 | -43.2945 | 2025-09-02 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 82d9d7e1-a0f6-3637-b761-c05c864e0add | -6.9129 | -45.5593 | 2025-09-02 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |


[Clique aqui para ver as próximas entradas](README102.md)
