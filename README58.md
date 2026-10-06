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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98291497-a5fb-381b-9955-72c6d7c4748e | -7.05702 | -59.2344 | 2026-10-06 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7640f871-24f6-3ba3-bf67-9e1c5953eb17 | -3.96615 | -56.12499 | 2026-10-06 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dce84063-b1f8-3ffd-ba80-8f27496eb6e5 | -3.23272 | -53.8649 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7eacb65-05e7-375a-9b68-b137bf5adeed | -8.34822 | -62.83826 | 2026-10-06 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 512123bc-631e-3e56-8f9d-eae85f6db5de | -3.1162 | -53.76424 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 86b335ff-9936-345c-9653-ae9b4fdc82bf | -2.92008 | -54.10905 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 52d1a3d7-02e3-337f-9ad5-307f929c2011 | -3.15548 | -59.14917 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d8fd344-3a77-3ca6-b44b-e591e2f1f9e7 | -2.03135 | -56.93642 | 2026-10-06 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8c61208b-8ce4-3666-800b-b2c2600b08b7 | -3.58298 | -55.40328 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 95962e32-1350-3e0f-8b7f-393ecbdc02fc | -3.25261 | -60.73053 | 2026-10-06 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa8bf8a4-1f26-36d5-b296-21a0806e86f5 | -3.99533 | -56.2655 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20126b4b-6b71-3418-91f1-c97882e39ff0 | -1.75598 | -54.94814 | 2026-10-06 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 446a8105-d3a8-3d91-910b-5071d867782f | -1.24965 | -55.88092 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b058bb4d-9691-3d13-a574-a25ad3eb68d4 | -3.02964 | -53.89597 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6eb825ce-17be-3ed9-9fd6-c16299e17ffa | -3.95824 | -56.04982 | 2026-10-06 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 425aaaa3-6072-3a3c-aeb3-293f4fdb8948 | -3.10375 | -53.758 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f1453c94-eaf0-30ec-b829-0fca52bbc7aa | -3.05052 | -54.22031 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| afeaeada-d548-3dad-b3e4-be9c5037b9ba | -3.08856 | -54.16802 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 46b9928d-6859-3a49-bbe4-34a81f20abe9 | -3.68525 | -55.95612 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 223756ec-8d0f-38aa-890a-7e15b07b6471 | -2.79671 | -54.09459 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3848e399-34fb-3bdb-99b9-6b9cf320e174 | -3.47828 | -55.4323 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4f0edf3-692a-3a40-96da-b1a01444ab76 | -3.37527 | -58.19013 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 25cb3918-46b6-3c8e-b619-45a940254de9 | -8.35219 | -62.83515 | 2026-10-06 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9853cfef-2d6e-36d4-bb5a-c7a0155302aa | -3.05246 | -54.20709 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd02c4e5-ac7a-3d09-ab8f-c0ee1e6b2b12 | -2.8771 | -54.13491 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4b9ec93-1822-3f0b-a98e-00e9eb6de952 | -3.96124 | -56.05287 | 2026-10-06 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4519aa79-b607-39b2-9c92-03e29cdec5a8 | -3.06284 | -54.22483 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 629f9908-eefc-3db8-a6a4-478c00d2584a | -3.06209 | -54.1452 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54a7ee62-144c-30b5-8d31-c49fe8ae1a71 | -1.75619 | -54.95119 | 2026-10-06 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad72bcbc-ded4-3fe5-9fff-6ef25787cf07 | -3.61219 | -55.47659 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90621e75-6162-3acf-8abe-1d96dc8fb887 | -3.62931 | -55.28466 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 13aefef4-ff0e-3bc1-8d48-c9dbaa4fafa3 | -3.54563 | -59.48359 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 188ede79-cbe6-3e30-9028-b20e523f28e2 | -2.94014 | -54.1486 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1e3de405-76b2-3eae-8352-38c03a54a7a7 | -8.7679 | -63.68685 | 2026-10-06 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04b9b315-8ca5-39bd-9639-9f284dab1a2d | -3.04708 | -54.21433 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f09ad55-de89-3cec-9ad6-64d4f0348e87 | -3.15657 | -50.44534 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26bc861e-0270-3a59-9a3d-310c5c194c55 | -7.43904 | -63.55772 | 2026-10-06 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6f9776c-bd11-3a2a-885b-9baaea736600 | -3.49736 | -54.61656 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fab8f7cc-ddfc-36c0-9a35-98bcca4ff796 | -3.07829 | -54.17876 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ad8bea54-c863-3fbd-b5ee-ea2c6f2bb70e | -3.2756 | -54.18987 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d482ebb-4216-3512-bca6-c27a37e76fcb | -3.60759 | -55.47958 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1688b0cb-1eac-3e83-97f5-bcc789038a38 | 1.73193 | -55.61997 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bcface7d-f303-3cc1-83a9-ca05dc404ba9 | -3.10376 | -54.18258 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ad080e2-79f1-3060-8414-f9039f5a4e29 | -3.08195 | -54.18341 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90d7398e-a400-3a82-9d9b-7cb10151b845 | 3.07507 | -60.57647 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cd9e38e-b286-3ea1-86d2-d4f1eb68cb52 | -3.09149 | -59.18919 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3797585a-14a9-3fa3-a3b9-b77cb79ae13a | -2.99161 | -54.12219 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2df608e9-4f14-3604-a408-179cdc72c2c5 | -2.87243 | -54.16626 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 112e9897-4d29-3671-92dc-71df2dea0809 | -8.32523 | -62.91724 | 2026-10-06 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f57489d-39f0-3054-8415-6d0fc2942ae7 | -3.23211 | -53.86909 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed1f794c-1c1f-3f40-b7b6-7860f07ffd44 | -3.12558 | -53.76136 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07cffe4d-e2c0-35a7-b634-91b411bdaeba | -3.27061 | -50.39886 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24940724-99eb-3b58-ade7-2740718bbcab | -3.05475 | -54.22095 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2ade9c51-026a-3a14-984e-03507698d3c4 | -8.34379 | -62.82256 | 2026-10-06 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 527dbc42-933b-38e1-8d68-7892e234c279 | -3.28044 | -54.18649 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc2f65d4-4468-3020-a690-e2bb6c9ec9b9 | -1.61284 | -55.12179 | 2026-10-06 05:23:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2200931b-4567-3696-9a68-caec64af959a | -2.78584 | -54.10907 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01b42357-c107-3f70-b5c4-1e47788428f4 | -3.68837 | -55.9613 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 574992fc-e09a-3079-856e-0a52dfeef92b | -2.94316 | -54.15716 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27293f0b-c2ae-3a45-9d85-a01a92b782c1 | -3.12156 | -53.69997 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a62841b-85ce-3611-9c36-6efc30dfcd01 | -2.98736 | -54.1215 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bcf57455-c77b-3f3f-bad8-3ab7f686e461 | -6.69258 | -55.20597 | 2026-10-06 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 450c5616-c0f5-3b35-a841-0710029f3372 | -3.07701 | -54.15803 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfa9a112-8f79-33a4-989f-e6e86a357fb1 | -3.47043 | -50.10751 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81b24098-3615-3ef2-a891-3df211bc6b41 | -2.98572 | -57.5708 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c54ad94-dadc-3196-b175-1d4f4acb919e | -3.27678 | -54.18178 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d083cec4-009a-397e-8c87-ffd050927ca4 | -2.13259 | -56.69806 | 2026-10-06 05:23:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f56a5fdb-8d1e-3c1d-bbb6-0630b7d2ade4 | -3.85005 | -55.84254 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4097acfb-eb8b-3e54-987b-e9cadc179e3c | -3.06092 | -54.20842 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d7020677-c6a7-3d61-b826-4f57527c85e6 | -3.22159 | -53.88026 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01d31410-9074-3823-911a-c92f5200fce6 | -1.61463 | -55.11375 | 2026-10-06 05:23:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49ebb42e-0efe-3b92-bf49-0ee7df9dd435 | -3.06511 | -54.15378 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cda83db5-da24-3e61-8667-ac0e9102ee71 | -2.98795 | -54.11754 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aad5687a-5e50-3a66-9ff7-44604c868d63 | -2.9371 | -54.14005 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59e717cd-1d95-3e9c-83bf-a8e1d32d580c | -3.49955 | -49.90443 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 695eef21-4703-35c7-95a0-6177d56fab39 | -3.6338 | -55.28186 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5fa3ca4c-2aa2-387c-93e5-d5913f5704a2 | -3.53667 | -55.52467 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e240765f-b482-36c3-8fa2-1a4fecacdd28 | -2.86745 | -54.14143 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f35d4f7e-d5e4-3428-a1a2-73f770dab0d0 | -8.97283 | -65.4458 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c354e2a0-5122-3e27-b77c-1dc0629f9a3a | -2.95651 | -54.15502 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0771aea-86ce-3729-b447-389ed3bb6c8f | -3.48964 | -57.78562 | 2026-10-06 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d6cb19f-7399-3ace-9f64-6fcc15655293 | -2.29951 | -56.7725 | 2026-10-06 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a74667bf-25b7-32ac-9a8f-bf6477723092 | -3.22822 | -54.30515 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2bce38f2-b00c-3e3f-9997-b478f45fee50 | 0.70164 | -51.43129 | 2026-10-06 05:23:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db58a0bd-2a69-32d1-b957-bb9012e70229 | -3.69288 | -55.95721 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 623b81f6-4ca2-3bce-b6ba-9d0c6a4b0ba2 | -3.24018 | -53.87461 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11ea0ad0-7698-33e3-ba74-d52741d9065e | -2.26862 | -57.08907 | 2026-10-06 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 387938f4-39f8-3075-9d7e-c0749668612f | -3.06327 | -54.16571 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51b9b371-9c55-3ea2-8149-d5bcd3aeb33c | -2.91704 | -54.10041 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9cd4363-54be-3c79-9fb3-e4d78e4c3479 | 1.79385 | -55.54107 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1bf4b2e6-eb58-3503-bd63-257e3751ac3c | -3.24929 | -60.73002 | 2026-10-06 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 364aa13d-3ab5-39b7-8a97-fd39d88ff539 | -2.54773 | -57.39321 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 889c6266-c0ed-3fb8-a6e3-3e46455c8858 | -3.06981 | -54.17743 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 43ab4599-dd78-3501-95bc-a0fb1c5d1e67 | -2.78497 | -57.67054 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6559568d-9304-3a75-9309-e5626c141358 | 3.0574 | -60.59808 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a97177a2-a367-32de-9cdb-6acea8089ce1 | -3.52877 | -59.39599 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f16667a4-d9fd-3386-8cb6-f6995b68364d | -2.94377 | -54.1532 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 271cc1e4-0bd1-3ef4-b7bc-1999c4795d0c | -2.78386 | -51.66681 | 2026-10-06 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ecbe11da-6f61-307a-a3f5-4f33adcf95e2 | -2.49054 | -56.82468 | 2026-10-06 05:23:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eeb3cf68-a492-3521-ac66-2dd57102116b | -4.77427 | -50.80899 | 2026-10-06 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README59.md)
