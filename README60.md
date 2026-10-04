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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78f8a09b-e25f-3b49-810e-e0b737835d0b | -3.51176 | -54.61102 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fce6a60e-cdc2-3843-8e4c-4a8e38ae13ff | -2.94107 | -54.18757 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed992ca2-1857-350d-a644-c3e442f2b059 | -3.22912 | -54.31392 | 2026-10-04 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b06a68cd-4c77-39bd-9d30-6f4deeb58d29 | -5.85085 | -53.46949 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fead3c4f-a389-37f9-8efd-8c650b0d5449 | -2.90303 | -54.08525 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4050a718-ce6b-30a5-9704-c54aca900432 | -3.86148 | -55.82053 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2197c596-75d7-3574-90dc-58d35f5b2f78 | -3.01703 | -54.16671 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4ff9941-0e35-3a3f-bda0-b09874f2b232 | -2.32573 | -60.06585 | 2026-10-04 05:16:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fe3e1e7-6716-3d3e-bbf0-462959c84ca9 | -2.82348 | -54.13094 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 52c03f1f-1693-3c7c-bf22-4c1491f4fb97 | -3.20678 | -50.74689 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2e92b2fc-f0e6-35e9-b95c-301f3c1e228f | -3.58995 | -54.53262 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6294f76d-0a29-3928-9e8b-f78b39406f8e | -4.50397 | -55.52773 | 2026-10-04 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3573a06e-b37d-3ead-aacc-331341821e0a | -3.04996 | -54.23197 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 841c034d-1111-33cb-8cb4-83de3d9647ab | -6.00185 | -53.52083 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2c6a1c32-85b5-377f-b83b-54f395cdaab0 | -3.47386 | -50.09538 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 559654ff-0b46-366b-a39e-52099dc9e005 | -3.00054 | -54.18013 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac8416a0-20e6-33b8-af96-c5157df684b1 | -2.77944 | -51.36836 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4eca209-9bcc-38f6-8545-e885722c140b | -3.76188 | -49.56485 | 2026-10-04 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| df8f9504-7ce4-36d2-8335-5150e9dd168b | -2.73471 | -58.04301 | 2026-10-04 05:16:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85164aa8-c50a-3559-aa75-5b73f5bc3b29 | -6.00087 | -53.55326 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b147e3ba-53a0-3f46-9bec-3eec0a19334c | -6.07886 | -53.47114 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e4e08a9b-7ea0-3b4b-ab80-fda9880c2f4a | -3.12707 | -53.74405 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd881e18-b531-303b-8eeb-9b9048c2c3b9 | -2.58936 | -51.84946 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| bc5b813d-2150-3a7e-9952-1890a1940cad | -3.06975 | -49.54745 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc74774d-438d-3981-af50-b774a3c74a2b | -4.46446 | -54.96602 | 2026-10-04 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d58cb1a-1008-3c5f-a780-8980a7430133 | -3.17801 | -54.08541 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f59cedc4-1864-3bad-84ce-430483e9338c | -3.58392 | -55.55583 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d7be74f-9659-33ba-9b50-c7dc4dbb1ddc | -2.8189 | -54.11418 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7f191d27-82ee-3f5e-9ce3-40385c80c2fd | -2.79549 | -54.10252 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6812d70-52ba-34a7-965c-a386bb9be066 | -2.10987 | -49.0034 | 2026-10-04 05:16:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03786704-91a5-3c15-b64d-8673ba137b80 | -3.02067 | -54.23542 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ff86025-ca0b-339d-bb45-eb24fb3fc786 | -4.26134 | -46.37088 | 2026-10-04 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6826587d-3565-3383-8140-9df23bb6c819 | -2.82286 | -54.13485 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f326f4ab-8952-3f84-bacd-b34c3769df20 | -4.26202 | -50.78845 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa8a48e4-e383-313d-a1d9-a45b02528e1a | -4.25484 | -46.37398 | 2026-10-04 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72960d2d-87fe-340d-979f-84c095b6ccb3 | -4.81371 | -54.73245 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27e68fb2-a454-3988-b3fb-4e166bdb9c96 | -3.6604 | -54.51574 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69886c4f-8b37-32db-b080-087e99d83c44 | -3.17612 | -54.09739 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d477466-757a-3102-b069-0b379031b575 | -2.83226 | -54.2121 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa2aa813-d2d2-3cb7-acf3-85b6f14bca5f | -3.85206 | -55.96708 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efb849ee-cff6-3a30-955c-4fa7739856c8 | -5.99927 | -53.64098 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c4d1e7b-0aa0-3abe-ae59-55cb4e66271a | -2.97129 | -54.08767 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffb9f8c3-1d03-36f0-8c09-4b65f5193340 | -6.00117 | -53.52537 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cebb412a-341e-36a6-9833-81207613e440 | -2.82242 | -54.11472 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2ac621a2-e2ed-3758-ba81-1fe23a69766f | -4.13297 | -54.15768 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71dbe7c3-b13c-3d7c-9370-53cc9cc2e6a8 | -2.92879 | -53.94265 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f04b04ee-4f43-3298-b240-c72930c94b80 | -2.80314 | -54.09968 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c427a292-eb78-3b5c-b1d6-e47def3fdfe8 | -2.82013 | -54.10633 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d583591-c59e-342c-97cf-f75b18795dfc | -4.26019 | -46.37886 | 2026-10-04 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7c942c9d-26dc-3ad8-ab07-f29a0e6b73a2 | -3.5835 | -55.31627 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 48631607-04c0-3f44-9b85-5d41fb24d20d | -4.12647 | -54.15262 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a420cb88-fa6f-3935-9969-c9210848f30a | -3.23811 | -58.75639 | 2026-10-04 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d689d373-402f-304d-8a33-f2d90ee0dda3 | -3.18932 | -54.08232 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 980181ce-3dca-3470-87fe-2bf73193dbd9 | -3.51871 | -54.61205 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| addec457-ad54-3000-9cc6-51d8b9730030 | -2.84706 | -51.28708 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecd33812-1a84-31a2-bae2-90b0e33ee0eb | -2.80253 | -54.10361 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11d52955-d77f-3224-9162-95641adebc75 | -3.01642 | -54.17065 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f245c9a-c7a8-34f7-80fd-fc9471c35c98 | -4.46792 | -50.97504 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3fd7907-2dad-3fcb-99bd-54c44cd56072 | -3.51991 | -54.60441 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55557d61-3c94-3bd0-9a8f-e63b2285af8a | 1.76344 | -55.63901 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03a3473b-e67c-315d-bf00-7850e768fd65 | -3.60014 | -54.23168 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54270f15-7211-3bcb-a4b4-a7ba0552b3c9 | -4.52093 | -55.75135 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33630b7a-9af2-3716-8af5-2fea8dd8df6c | -3.07445 | -49.54816 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cf2cc199-47a0-39ef-bbdd-701e94b2588a | 1.75738 | -55.64347 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57076102-31c3-3965-a5a6-da463e81c55e | -3.42584 | -59.56816 | 2026-10-04 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eaac6c89-ac31-3e0c-817d-4b4896b1ad56 | -6.07743 | -53.48043 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 340c55fd-d68e-38b1-93f3-b74f72782601 | -3.67181 | -60.61666 | 2026-10-04 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 836c4102-8583-3099-bce8-f7f81612676c | -3.99093 | -55.81881 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6435f8e-6d19-3289-8bf8-6f07b19fe326 | -2.81935 | -54.1343 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 04bcb2ef-06db-3c07-bba7-f822aba6182e | -4.2832 | -50.26345 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 84810bb5-80da-3b76-ae4f-d48d3afd058f | -3.18257 | -54.10237 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cea87cac-6b68-3fc5-ae1b-36231989b9c5 | -3.17864 | -54.0814 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e7bc3d68-4302-354e-8f32-0f37b8d269c4 | -2.48301 | -56.09587 | 2026-10-04 05:16:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcf44361-59e5-3522-8c70-8c8bd6218b86 | -2.85062 | -51.29149 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0822717-5cff-3549-b060-c6a88a3f32b4 | -1.2122 | -55.86077 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84a03d6f-d770-33c3-90aa-0fd4d6cf7edd | -3.29399 | -49.1268 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fdf079e8-760d-34ea-91de-79ac02d74a02 | -3.53271 | -59.39642 | 2026-10-04 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a4017c9b-cbe6-3ca1-8db9-76199c79a4b1 | -3.61481 | -55.51307 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0df13f57-dafb-3def-ac7e-dca0f573f0d6 | -3.13673 | -53.74003 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2c7c788-8b78-3ce9-a03d-6d953dc3ffc9 | -4.11183 | -54.41025 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60642b31-72dc-3138-95d9-288c545f1192 | -3.84484 | -55.96954 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca076e99-e0ce-3a88-8154-eff53ae6ad30 | -3.11169 | -53.72484 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| d47710e0-5b8a-333f-8ff7-0ecf9db71bf7 | -1.65728 | -55.21489 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 377cf940-82c1-36d5-b349-ad426a50cbd8 | -2.58066 | -51.87975 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6a3425d4-6608-3e46-9dd9-5c9b0b83a965 | -2.2514 | -51.93658 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 95b8f515-2b81-35eb-9149-5449fd7f10dc | -3.66102 | -54.51186 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 112c17b4-a4c7-3ab6-8573-5a7af900caa7 | -2.913 | -54.09081 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8f03d8e-cffa-3efd-8bb9-2c6d7f3bdcf4 | -3.18516 | -54.08583 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 942ff8b8-eb0d-3d88-b1ad-1acf03fdcf17 | -3.4655 | -50.08924 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| caf21cdb-a466-31ce-b821-4b46e62e0952 | -4.28705 | -50.26878 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| c1fe1adf-239d-3162-980b-0192c1b7caba | -5.96359 | -55.35092 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 24dd26a6-941e-31e6-a5c6-aed77924003a | -3.12089 | -53.75993 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4d18f6c7-baa2-3ffe-a1db-74f13891ee9f | -3.60047 | -54.23113 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdd8b3d6-59f5-3409-af7f-df2591559436 | -2.94392 | -54.1238 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 07f45766-2c64-3c71-afef-7309a74deddc | -3.98741 | -56.2711 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5844aaa9-6cbc-3b36-9e53-b6ee25625562 | -3.12542 | -53.73117 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 03c8256f-7154-39c0-b2d5-5fda7b87faa0 | -2.36445 | -50.60408 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a75e36f-bb23-36bc-a708-ff4cea80df0c | -4.26886 | -49.98131 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e80a5bef-8814-3156-a44f-2c2320c2bc67 | -2.58223 | -51.86949 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1b6fe10f-6e0f-37d6-a921-4d56f27d4eef | -4.41926 | -55.75011 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README61.md)
