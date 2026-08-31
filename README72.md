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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69302bc6-8881-35ef-96c5-924fb8ea104b | -5.48827 | -57.14632 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 693aace1-a11f-3a35-8df3-23cfdcab480d | -7.6086 | -61.37357 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| a5d43980-ab5b-3f8c-b83e-f24223bea07b | -1.62217 | -55.16792 | 2026-08-31 05:53:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 659abe1e-bce4-3402-88e4-98ca19b32a9a | -6.12251 | -57.67602 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| d176f685-0395-3516-9b1b-e7ebc7e914b8 | -5.87747 | -57.77887 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e273d441-841c-34ef-93ef-bbd5283b21bd | -5.95736 | -57.68169 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4bdc01e8-dc30-3c84-ab5b-8a0248c3dc94 | -6.93274 | -55.63025 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a239ccac-6a4f-393b-afce-8174c6562bc4 | -7.81006 | -63.25953 | 2026-08-31 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d85b6d2-7f60-3438-806a-b6e627b648f7 | -7.33856 | -60.59972 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 39cf0f2d-9dc0-3bb3-8260-90b5d8433a18 | -1.39746 | -60.33459 | 2026-08-31 05:53:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 91f5e5f7-09e6-368f-b8e7-642dc9892f9f | -1.61938 | -55.16957 | 2026-08-31 05:53:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 710e3c6f-06d1-3322-a0dd-456d64c3006f | -5.96324 | -57.67921 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb53e5e7-8675-36b9-87fe-54312f6783fb | -7.29405 | -60.58884 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b891d264-1401-306c-9fb9-bda407d701ff | -7.58196 | -61.34467 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be53db4c-f044-32fb-abb9-d1dd879f3fc9 | -5.48379 | -57.14367 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a66d2f3f-26f7-3291-a64c-9e1ed7ac2bad | -6.12101 | -57.6866 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 44204c63-9ae4-3362-bf5e-4dd6cedf5f14 | -6.93832 | -55.63608 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 381aab35-dc1e-3c88-8492-1d369f453e80 | -5.24065 | -55.89391 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad8ee253-7344-3e3d-8ea6-bcc61f47a785 | -7.52959 | -55.33559 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1882970a-b90d-319b-a6f7-93579b38b943 | -5.96275 | -57.68259 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63d156e1-1676-3005-bf1f-eb9088aa4cab | -5.95636 | -57.68856 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7ceac227-bb43-3ba3-9331-794f804b4708 | -6.7761 | -55.64176 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| adb89391-d478-35b6-9c61-a91718dda133 | -5.25688 | -55.89288 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 548bd3ae-7a92-3470-8bd8-a36e8251a7b1 | -6.79183 | -58.99929 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3512993-267d-3a0a-9c82-0295f5ae7bd7 | -5.95786 | -57.67828 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0ab435f-2f31-376f-b276-2c9964da13b1 | -1.59363 | -54.41089 | 2026-08-31 05:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3eb81e5c-b593-381e-bae2-6c8e7fc47af8 | -6.86068 | -59.47686 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d23a877-03e1-3597-b141-950aa5004151 | -7.57708 | -61.34813 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95cb1a5f-453d-3aed-ac75-e9bf324795ea | -6.91246 | -59.48677 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ad9e68d-4478-35ed-86e7-c71c6a6d048b | -1.41245 | -60.32112 | 2026-08-31 05:53:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad3d3d55-f29c-34fb-8e1b-59f309cf78ca | -7.57961 | -61.34562 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aef0cb28-64b1-3cbe-859b-06b8ac8ac00e | -5.88615 | -57.75631 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2eeafb57-6905-3b3f-ab6e-73f5b51dc2a1 | -5.94643 | -57.69613 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1453b3e-d42b-3c27-977a-d01fc3460573 | -6.92002 | -55.72424 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6e4a3097-7a42-39b8-86f0-e457127d1a31 | -5.85872 | -57.55808 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b37063d3-b545-30b3-85d0-7e9cc42d9a58 | -6.77433 | -55.64206 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 06f134a7-a469-3b79-8f2e-7968f5f4d84c | -5.25266 | -55.89578 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f90ab1dc-d9a4-30ca-a9f8-280123254ebe | -6.41813 | -58.2315 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fbf8703-2e88-3668-82a0-7c405c2e2c8e | -5.25683 | -55.90989 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| bf7f59f3-6f2a-3802-84dd-0329da32787b | -6.77657 | -55.67304 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f3c67ac-16ac-31a4-8b56-bc2959bbd739 | -5.48927 | -57.13908 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7fa9708c-f774-35f8-b66f-988a639fc5d0 | -6.86475 | -59.4829 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc3787a8-2e95-3301-8de2-f33f47af8a43 | -6.15674 | -57.78298 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e6aee83d-18b5-31cc-8094-7cc125bcc0b5 | -6.15624 | -57.78637 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ef4fbf01-fe4b-3949-88ef-88fbb879f2f9 | -5.93964 | -57.68985 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2f1bbff-35d3-33ab-a6db-f17cd490f8bc | -6.08859 | -57.7209 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da30fbcc-61f6-3c0e-b88d-3c9436f38c0f | -5.87699 | -57.7823 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2be19736-b42d-300d-89f7-762cb783b787 | -7.5611 | -61.32203 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 938150c7-250b-3d40-8c28-57baa2f7643b | -6.93764 | -55.64108 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c9fea0cc-27dd-33da-ba0e-b4757c63ffcb | -5.85922 | -57.55443 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e8508d7c-b373-3e9b-9d9a-53370ce1ae3b | -1.59438 | -54.40604 | 2026-08-31 05:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7e5176f-231b-331d-9cec-6c53952cb3ae | -7.52892 | -55.34086 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe5158a4-6756-361f-9c30-a1005dc4b911 | 0.01035 | -60.6037 | 2026-08-31 05:53:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71f662eb-b9f6-3304-8631-d59694ed7d35 | -7.58139 | -61.34876 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddae9f90-07f0-329d-9146-20cb31b21d07 | -7.5735 | -61.35722 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64c0b53d-1260-3467-ba67-373d52c6d8b9 | -5.94404 | -57.69751 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 59b44da1-25fd-369d-8462-16f61856ea35 | -6.15333 | -57.786 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c548930a-ca05-383c-8d9f-f35088ce8b62 | -7.91973 | -61.33577 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69d5135f-37c0-3bc0-b24a-ac2f65d377e8 | 1.66149 | -60.13852 | 2026-08-31 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a1dbaa8-d42f-3272-8b30-2940f162a4a2 | -5.88477 | -57.76603 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92361fee-946f-3b4b-95fc-fdf164885fe6 | -6.901 | -63.06005 | 2026-08-31 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02499db9-d0f4-3e97-bf6a-c519e632e902 | -5.25085 | -55.89209 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8cdf3510-78bb-3a50-8891-9966316c31fe | 0.14461 | -60.40044 | 2026-08-31 05:53:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5aa21eea-bc94-3f6f-a2c2-357aed554098 | -5.24957 | -55.91812 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 228b2fb1-4792-3a1d-bfc8-972738ed87be | 0.19427 | -60.5024 | 2026-08-31 05:53:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caf1a2a3-5c98-3159-9f92-5d4f90c5887e | -7.57901 | -61.3497 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f3c2d15-696b-30b5-a77c-d0b4a79f70c1 | -5.94104 | -57.69526 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6dec8ec6-c427-3d9c-b033-3fc3c73313ce | -7.31326 | -64.72695 | 2026-08-31 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 895305cf-b57d-32a5-8f5b-94d86a86985f | -6.8655 | -59.46899 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4bdf005-abe4-3779-a289-b4ab14e66d0c | 0.00979 | -60.60019 | 2026-08-31 05:53:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c9ca428-fdd1-33fb-b73d-e06dea630e22 | -7.30948 | -60.57757 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 83743681-4216-3b14-9372-f739f18b548c | -7.52726 | -55.34483 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd204eb8-5889-328b-bb3d-d2cb043829c5 | -7.30372 | -60.58565 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 131d4be3-51b2-3384-ba4d-34bcfed82008 | -7.31147 | -60.59588 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8e02abd3-f9a9-3242-a87c-dfe898e447cf | -6.6788 | -58.74681 | 2026-08-31 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a242ad1b-8f41-3999-83a9-362dafdc3c8f | -5.2533 | -55.89119 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cc45f9f2-da96-308f-8b39-d9fb5c9c1123 | -5.87895 | -57.76841 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 471fe136-ed21-3a90-84f1-8cb1eb804bed | -6.86485 | -58.95072 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a36dd16f-6d98-3965-852e-c7b09b985909 | -5.25204 | -55.90027 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 9242f4b7-4d53-3956-a1e1-8089879681cb | -7.3979 | -60.58376 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26403cb6-699b-386a-85ce-c4af9da5d34e | 1.76892 | -60.23402 | 2026-08-31 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1800f92f-f3d0-39da-8435-82c7c9751bf6 | -7.58391 | -61.34626 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5c0baf1-190d-34cc-8959-91e89ce0c9ce | -7.62656 | -55.2948 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18241452-efed-3f3f-97bd-4a63b1afd590 | -7.31274 | -60.58703 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ceef7794-0d68-39e5-a02b-fb8da88a4d30 | -6.41805 | -58.23434 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18e36dbf-2cab-3f11-87b6-2f84d938c079 | -6.60864 | -58.59455 | 2026-08-31 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d2c4b3aa-f04d-3160-b9a7-016920833288 | -5.24354 | -55.90022 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ca086ae8-cea8-3795-a67a-d219a565dce5 | -6.90029 | -63.0647 | 2026-08-31 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6dd1306-cb22-364c-96ad-2150c03cf0e4 | -7.78996 | -61.58292 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 59969463-a172-337a-b93a-dd68827c9f45 | -7.60489 | -61.36885 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 3e161d3e-e702-3d3a-941a-808b48a3da8b | -6.41767 | -58.23466 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2760178a-90b7-30af-9b5f-3f113846da04 | -1.39806 | -60.33075 | 2026-08-31 05:53:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| db736f85-f5ca-3e20-9c17-a788e45d0ba7 | -7.55678 | -61.32142 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a41c52f-4d9f-390f-95fa-48fdcdaa64be | -5.95687 | -57.68508 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a62e46fd-3afe-3717-ae40-57130305b50e | -1.6215 | -55.17238 | 2026-08-31 05:53:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f889ec66-c527-345a-aa1c-1440d5f8cd56 | -5.87263 | -57.7744 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9bb645d9-fc5f-3dfb-840c-b2be966d47cd | -7.52796 | -55.33958 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c046297d-ee0a-301e-8525-4a446d029bcc | -7.58627 | -61.34531 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4ca0aa6-cc57-3e8d-992e-ab9aae8edeec | -5.48166 | -57.15305 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86f3f771-12b6-38c2-8846-7b0b843b6c63 | 1.76795 | -60.23407 | 2026-08-31 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README73.md)
