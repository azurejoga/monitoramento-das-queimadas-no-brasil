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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff02e0f9-699b-39a7-a44e-099f95540386 | 0.0638 | -60.9799 | 2026-03-04 05:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 71.2 |
| f3b142ac-4d0e-3441-92f8-09f73a33bd16 | 2.67018 | -60.4106 | 2026-03-04 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d8b73f0-c8a9-353d-8588-cf302db97208 | 3.87911 | -61.68564 | 2026-03-04 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0038881-6af1-31c8-a425-dd2f324af318 | 1.51309 | -59.92732 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a9fe9b8-af9f-30a2-bbb2-4049df28c996 | 2.52291 | -60.98938 | 2026-03-04 05:22:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0373379e-ad97-317e-8112-cc2bfce3fe08 | 3.01462 | -60.66099 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82a82820-e38a-36e9-8fd8-b12f0a3fbec5 | 3.03691 | -60.64603 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed41961d-dc48-3afd-993f-50a0394cda83 | 3.05675 | -60.63995 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53c26339-de1b-3026-b1b9-4f4137d1aa55 | 1.48978 | -59.90945 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 418e23cf-901b-3416-99ed-7b1434f05494 | 2.95143 | -61.08741 | 2026-03-04 05:22:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d012855c-11bd-3b71-9973-72832f0b822f | 2.91323 | -60.43748 | 2026-03-04 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c4cb4ed6-2416-3031-a8c0-d6539e0309dc | 3.04644 | -60.64155 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf5668a3-2445-3159-9ec3-e673084ec065 | 2.92745 | -60.46165 | 2026-03-04 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 42a2d3e8-868c-38ad-b1ab-7fe721b20650 | 1.94891 | -60.81771 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fa514d6-82d6-372f-b95e-15ade2a6e3c8 | 4.50843 | -60.97421 | 2026-03-04 05:22:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc01538d-8400-3020-a9e4-3a9fc6ca8840 | 2.65425 | -60.10235 | 2026-03-04 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbacb182-a1ae-33db-a359-60ac3a764ad0 | 2.64419 | -60.44459 | 2026-03-04 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67c67adf-48fc-3906-b0a4-ae6a037cf1c5 | 1.50642 | -59.90681 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 682bd769-4e2a-3d8f-8167-7a4cd6d345b3 | 4.64302 | -60.6976 | 2026-03-04 05:22:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 365ae945-153a-38f9-b75d-5b7bfdc7b743 | -2.74513 | -58.1846 | 2026-03-04 05:22:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d07946c5-3bec-317e-9e2a-b104ec984f19 | 4.17713 | -60.38293 | 2026-03-04 05:22:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3143007e-6dfc-3cc4-a83c-1cca57f04266 | 1.50088 | -59.91488 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c687723-9e7b-3019-b60a-b3e8bb4286f2 | 2.68152 | -60.41632 | 2026-03-04 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ede1de5d-d307-3ce2-aa23-40b7ca5fb6a8 | 2.65873 | -60.10899 | 2026-03-04 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a082b993-c839-3cb4-9544-36a2667d7159 | 1.51642 | -59.9268 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95d243db-9e7a-3aa1-acf5-f4c7de8fb42e | 4.50961 | -60.98182 | 2026-03-04 05:22:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2e63f29-2bda-3683-98d1-2dee89d0b488 | 1.48645 | -59.90998 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f373bfcf-6d2e-3bd0-a272-52a6b405f32f | 1.50365 | -59.91085 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cfc9065f-ae09-3174-9067-c32bffb38dd9 | 3.02032 | -60.65244 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3725ac35-fcac-3071-ac1c-24b3c3542fe3 | 1.95123 | -60.51684 | 2026-03-04 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfc3167b-5b27-38ba-967b-c0990cd23546 | 4.08781 | -60.14648 | 2026-03-04 05:22:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08209d8b-acb4-33eb-8305-43b9a27d18e6 | 1.86238 | -60.40034 | 2026-03-04 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e6969b2-8daa-3ad8-a01d-bccc6725237a | -1.84327 | -60.00398 | 2026-03-04 05:22:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ab2c4b4-de69-365f-ab61-739ec03a7f6a | 1.5031 | -59.90735 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 354017a0-5134-39eb-9cad-d72f6e3c0424 | 2.25172 | -61.66381 | 2026-03-04 05:22:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e21b83d8-d68d-3e3d-add6-1662bd1d1b52 | -1.42743 | -58.93518 | 2026-03-04 05:22:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 811b24f7-69aa-3059-9cbe-1714ee9a18d5 | 3.05331 | -60.64048 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba14f1b9-5af0-3385-b903-ca677fe27b17 | 2.22571 | -60.74949 | 2026-03-04 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86a3907f-e7bd-3398-b111-3f863b72ab3e | -0.50255 | -64.60851 | 2026-03-04 05:22:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22ccfaa1-bd81-358b-a0c1-d295adb667de | 1.51421 | -59.93434 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29225efd-f9c4-36a5-84ac-3def826170c0 | 1.51365 | -59.93084 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56de34dc-148e-3a24-a232-15a004eef4c6 | 2.69239 | -60.08175 | 2026-03-04 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39e67bca-7196-3be9-a227-31929eadb332 | 1.482 | -59.92498 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af293196-b801-36c1-ae30-38ccaece45ce | 1.50476 | -59.91785 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 16e79029-a9d1-3c2d-a5da-9805576ec115 | 2.91949 | -60.45534 | 2026-03-04 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e764e869-ed84-3e35-9327-2b2700ad2bfa | 3.87548 | -61.68617 | 2026-03-04 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d8b7b0a-334c-3e35-ad88-310f659066e7 | 1.47534 | -59.92603 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92a89845-aae9-3ed1-914c-9f33024176a5 | 1.75975 | -61.15461 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05df4ca6-a4e6-36da-8ff0-9ff70c7306ef | 2.91571 | -60.6108 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03b02717-0305-38c8-82ed-3e11ada48475 | 4.50925 | -60.97902 | 2026-03-04 05:22:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc0f3453-b19f-3004-9b37-1e3b4f437075 | 1.45739 | -60.07259 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bac8d78f-debd-365f-a98a-7cca3e959c1f | 1.50642 | -59.92834 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ca23ed9-6078-38a6-b12c-90db09761864 | 3.06431 | -60.71179 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbad8931-b01d-3b24-971f-8b366c9de679 | 2.95083 | -61.08353 | 2026-03-04 05:22:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5731eb0-b525-3108-beeb-5831f1b8df97 | 4.04377 | -59.86279 | 2026-03-04 05:22:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfbd2b0d-19ee-3fe2-87e7-8ad362eca407 | 2.67813 | -60.41685 | 2026-03-04 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d2c47bb-37ec-32ab-aa7e-fab044c30e4a | 1.50865 | -59.92083 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e69a039-f068-3eec-9150-56ce0f3e6ea3 | 4.04434 | -59.86647 | 2026-03-04 05:22:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4512fd5b-9d6d-3f52-bb41-9324498ac85f | 1.67276 | -60.51106 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 148d0a2c-00fa-3296-be6d-209586c3cc56 | 4.04713 | -59.86219 | 2026-03-04 05:22:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f9ed469-8bd1-3641-92ad-2fe8b4bd5a6b | 2.77919 | -60.81598 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1727b25-eb71-3890-b442-e2091e8e6fd3 | 2.78264 | -60.81545 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e9d397b-9402-35d8-a4d1-642caaa0a67d | 2.89682 | -60.60231 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| baff701e-3998-30a1-a897-df884933a35e | 1.51142 | -59.91678 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 1a548b56-51d2-38d5-9667-09dd956bb908 | 3.04034 | -60.6455 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e06cbade-e85c-3d08-bab5-e3581a2e3104 | 3.06144 | -60.71609 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a602b5b5-7776-31d5-92e5-aae2dfafe7a5 | 1.49755 | -59.91541 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 226b5cf3-536e-36e3-a910-163652508cfb | 4.17951 | -60.39813 | 2026-03-04 05:22:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dc12a6a-93bc-3aee-91dd-74353087164c | 2.65817 | -60.1054 | 2026-03-04 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46ba6599-74da-345a-9fe1-13ecc6ee5c84 | 1.55289 | -60.28664 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 918c331d-e27d-3d23-84cf-641b1059b78f | 3.06489 | -60.71555 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 059beb25-9230-3b3e-b6e3-fd66aec8c60b | 1.50698 | -59.91031 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 339dbd4d-ec91-37f3-be0a-0b90a5a2dd71 | 1.9648 | -60.51474 | 2026-03-04 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ff67a5f-2c35-3694-9b18-454cf9342a79 | 2.67075 | -60.41425 | 2026-03-04 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39a597ef-e0cd-3d3e-bd14-667164043152 | 2.22076 | -60.08861 | 2026-03-04 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b365eb7f-69b8-3a8d-bd3d-c3a6784e4f09 | 1.4535 | -60.06959 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54eb1781-3271-3367-8254-5cc1bc1aed99 | 1.50754 | -59.93536 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc823aea-8953-351e-bd3b-16cab3d0af38 | 4.0477 | -59.86585 | 2026-03-04 05:22:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6bfbfe1-c37a-395c-a335-c8cc30b9fb19 | 2.87142 | -60.26408 | 2026-03-04 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b101a9a-46c2-301a-8909-854cfaad0a80 | 3.05732 | -60.64369 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49756019-55ff-318f-a9fb-e16739e61461 | 1.49032 | -59.93444 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5934f92-3b86-3508-8f28-0dd6f132d8ac | 3.01747 | -60.65671 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8780691-c36c-3957-b803-9e7960a8e61d | 3.04988 | -60.64101 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a627a6a1-3ff7-34ba-86c8-e0917309c441 | 1.93881 | -60.37047 | 2026-03-04 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3fdb1f0-4542-3b87-97ba-184eff0b831a | 2.92404 | -60.46219 | 2026-03-04 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ee1d9c37-5fd4-329d-aab2-f7d4e0d23933 | 4.08836 | -60.15003 | 2026-03-04 05:22:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c992c89d-d48c-314d-b31d-4050fa5186ac | 2.65088 | -60.10287 | 2026-03-04 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15886403-4d8f-3204-a141-af7215aa126e | 1.82804 | -60.85131 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b97ffc3c-dda7-395f-b438-f668ad072e6e | 1.59009 | -60.22627 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f916137d-cb10-32cb-b404-0d933e1e1495 | 1.55358 | -60.40015 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 481f47c6-1f70-3947-ab6b-236f85075763 | 4.50902 | -60.97802 | 2026-03-04 05:22:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83610b4a-75a2-3b73-a8c2-6b357e22f279 | 3.03004 | -60.6471 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2880499b-8650-3885-a676-676386cd9537 | -3.78153 | -56.46569 | 2026-03-04 05:22:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.1 |
| d6b781a9-376d-37aa-92a9-5ad9fea90938 | 1.50144 | -59.91839 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efc3453f-1295-3124-9c89-53f8c3c282d8 | 1.52486 | -60.70895 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b29ca274-45be-34e4-8fc5-ff9498e3baf7 | 1.50532 | -59.92136 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0d35e54-06e3-3d3b-b71e-3fc44f61136e | 1.48533 | -59.92447 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2d6392a-8d08-3a16-8a92-3ffa6a9f9ccb | 2.67415 | -60.41372 | 2026-03-04 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbc668ac-0b6a-3825-975b-18645358197b | 1.50753 | -59.91381 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d291fa24-1be5-3b84-882c-73deb03ef1ca | 2.22914 | -60.74895 | 2026-03-04 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README8.md)
