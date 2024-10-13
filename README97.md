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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebbe9e6d-edb0-30ca-b4ee-6b174531a7d9 | -1.88141 | -54.43758 | 2024-10-13 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c6f9eed-bd2b-3c99-8756-c151bf59f96a | -1.7316 | -54.0168 | 2024-10-13 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fee434b6-fe38-3652-a93f-3854d35d90bd | -1.72989 | -54.17921 | 2024-10-13 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1596c50e-0238-31b1-8459-5c04f5bdb0f2 | -1.72919 | -54.18388 | 2024-10-13 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5f8e8ee4-7a91-30d6-9891-7e098ed8b426 | -1.72532 | -54.1785 | 2024-10-13 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| eb6d99af-2163-37c0-91c5-b44d4d21549b | -1.59614 | -53.34997 | 2024-10-13 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96652bc7-e395-369e-a1b6-74a110c345e9 | -1.2671 | -54.67873 | 2024-10-13 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49ed4875-ca8a-3d6b-8e88-b8767e6e0e02 | -1.26206 | -54.68229 | 2024-10-13 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae38c530-dea8-3b8f-a4fc-e13f8cfabf01 | -1.26143 | -54.68634 | 2024-10-13 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 813ad2e0-c138-37c6-a526-7a9d7f695152 | -1.23299 | -54.11343 | 2024-10-13 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a797bff-c5fd-3cb1-a386-360ad53601e7 | -1.23226 | -54.11814 | 2024-10-13 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77cd9874-680c-37fe-af13-2316d85a4320 | -1.19304 | -53.3891 | 2024-10-13 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2bf2a6f-ded8-3be1-8931-022fcb8d7b52 | -1.16756 | -54.19827 | 2024-10-13 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db71ac16-0319-36bb-bdc7-83461057ea4c | -1.14569 | -54.10114 | 2024-10-13 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9af52b1-3b46-351f-a669-ae7c2edd9af9 | -1.14496 | -54.10581 | 2024-10-13 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 967c0b13-aa55-3a8f-b2e2-da7510eed5c7 | -1.14114 | -54.10048 | 2024-10-13 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0726ee25-761b-3e76-ba27-8a48cf857ba1 | -1.11318 | -53.61781 | 2024-10-13 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8c522a2-cc40-36eb-85f3-7ab512a1de8b | -1.09272 | -54.17313 | 2024-10-13 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61eac1c8-347a-308a-94ec-b0b7dcdb4d07 | -1.01895 | -53.7319 | 2024-10-13 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec30eb6e-d44d-39fc-b3a6-003e0def0f03 | -1.94857 | -56.45712 | 2024-10-13 05:25:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f7b0db7-3ab6-343a-bde8-8742add3798c | -1.94464 | -56.45652 | 2024-10-13 05:25:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4d644dd-14b4-33d3-a16d-839ed84fa85e | -1.71739 | -55.14632 | 2024-10-13 05:25:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05b8721d-5d79-36c9-bb9d-d80bb4c0ae27 | -1.67593 | -55.18909 | 2024-10-13 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4345a478-42fc-3b0a-88db-7c8d50213299 | -1.66722 | -55.13997 | 2024-10-13 05:25:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34f534bc-fddf-3a64-8793-d71b52453b6a | -1.65292 | -55.20289 | 2024-10-13 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8d2ba0f-a52c-3be7-b18e-7bf34e11f6f2 | -1.65225 | -55.20177 | 2024-10-13 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5846b528-8d79-3dcd-8fa4-a8bd8003d84c | -1.23871 | -55.90478 | 2024-10-13 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eec279b7-c808-3a20-89da-5ae6e4caf1d7 | -1.80268 | -57.12761 | 2024-10-13 05:25:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| faa98675-8562-3fa9-9b81-85ab04fcd7fb | -2.7446 | -58.1837 | 2024-10-13 05:25:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 119c81d4-2657-30e8-8fde-0db7751fa615 | -2.45337 | -58.03343 | 2024-10-13 05:25:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 7743e8f6-ff6b-37e3-94bc-14f4eb525d0f | -2.4504 | -58.02874 | 2024-10-13 05:25:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1fbac867-bb98-3d47-95cd-62a9963ebb97 | -2.59156 | -59.40435 | 2024-10-13 05:25:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e22ad5e-d340-3934-bbcb-d3b0c0e6de8b | -2.1079 | -59.31649 | 2024-10-13 05:25:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4b04263-fc03-3360-9ec6-ff5ad1c60bbd | 1.13048 | -59.52726 | 2024-10-13 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dbabf3f5-aaeb-3d50-b5dd-be100f4cd2ce | 1.12993 | -59.52377 | 2024-10-13 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bfd3aaa8-cb6e-3a9b-9d2c-4cc76038f52f | 1.12661 | -59.52429 | 2024-10-13 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70c29a8a-bbe8-39aa-8b3f-edfd9d583d67 | 1.12273 | -59.52132 | 2024-10-13 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d2bfaf7-3ae0-3572-b2b8-6d859158c3fc | 1.05972 | -59.5528 | 2024-10-13 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 706e0095-8800-3aa8-bc71-902fedc407b0 | 1.03886 | -59.74435 | 2024-10-13 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b191e75a-c1e5-3c7f-9a87-4878df869e6c | 1.01035 | -59.60672 | 2024-10-13 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 872d557d-93eb-384b-89a7-2b9565a0bb4c | 0.7052 | -60.21614 | 2024-10-13 05:25:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9ce0fc8-a11f-3b34-a45f-b188757fe232 | 0.70189 | -60.21661 | 2024-10-13 05:25:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67f70873-2c10-37a1-963e-8aa875355ea7 | -3.0936 | -60.29909 | 2024-10-13 05:25:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb6209fe-4998-3eda-98db-07f2f985ec3c | -3.09026 | -60.29857 | 2024-10-13 05:25:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85609b0e-236a-3ea4-a416-8ef21ac9f90f | -3.08971 | -60.30209 | 2024-10-13 05:25:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf4d18a8-77c1-3681-9aa1-ef9abff6e837 | -3.08916 | -60.30559 | 2024-10-13 05:25:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 959d50e0-17f4-3db5-9113-1f2a28b51edd | -2.98203 | -60.92568 | 2024-10-13 05:25:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34991b3b-4732-3beb-8b88-2d23a1d6ae67 | -2.98149 | -60.92912 | 2024-10-13 05:25:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d18575f3-b1df-3598-8211-02a0cb2044aa | -2.97872 | -60.92516 | 2024-10-13 05:25:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fb98547-474d-375b-9918-11219036bbfb | -2.97818 | -60.92861 | 2024-10-13 05:25:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edbbace9-a9a4-342e-b614-96674493b8e7 | -2.97764 | -60.93206 | 2024-10-13 05:25:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2eddd008-f016-3580-aa81-d9267d4b2851 | -1.92267 | -61.74294 | 2024-10-13 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45eecce5-c888-33b5-bca7-98db65e9e6a8 | 2.60246 | -61.28654 | 2024-10-13 05:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9794567-e4fb-329a-9778-630f5cdc8c34 | 2.58118 | -60.69265 | 2024-10-13 05:25:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82797dd7-90a8-3df6-8b17-79fc53339493 | 0.86662 | -60.61545 | 2024-10-13 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b7ba18b-336b-3ed7-94cf-348d3b23662c | 0.83322 | -60.57499 | 2024-10-13 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 957444e1-9383-389d-bca9-9f66e8cd50fd | -1.93533 | -61.72719 | 2024-10-13 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9b56477-199c-372c-8607-1e5703b039fa | -1.93479 | -61.73066 | 2024-10-13 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0340278-5802-3fc0-87de-87336f15adf4 | -1.9337 | -61.73757 | 2024-10-13 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8bda7021-e203-37e6-92f5-ff2cf0a678db | -1.93316 | -61.74103 | 2024-10-13 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 93c0b812-cd12-3073-a0d9-35eb5d8f4af4 | -1.92984 | -61.74051 | 2024-10-13 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 31a914ab-aa10-33ee-8124-4d711c9dba68 | -1.9293 | -61.74397 | 2024-10-13 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 57f5a83e-c31f-3c41-8bbd-55578a25d530 | -1.92653 | -61.74 | 2024-10-13 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4231673d-4ffd-3f25-9745-87489a7c85f7 | -1.92599 | -61.74345 | 2024-10-13 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba02cb76-3e28-3dba-b9d3-c7c4d373706a | -1.92593 | -61.72219 | 2024-10-13 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf69a34d-c89b-3efd-9878-a07da6cd0014 | -1.92321 | -61.73948 | 2024-10-13 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 186a7bb5-6193-3e49-865b-43fc19e7fc20 | -1.92207 | -61.72513 | 2024-10-13 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3a4acde-530a-348d-89a2-9f5c60ccd340 | -1.92153 | -61.72858 | 2024-10-13 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7c3486e-8364-33b9-992e-65af6570f15c | -1.92098 | -61.73205 | 2024-10-13 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67498289-0254-3bf5-861e-bf98dbcadbc0 | -1.92044 | -61.7355 | 2024-10-13 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3bebf45-d140-3a0c-aeed-ddf4bdef5bd5 | -1.9199 | -61.73896 | 2024-10-13 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e06a468a-857f-3b7c-ac96-93025433b3ec | -1.5218 | -61.59119 | 2024-10-13 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8cc11bbc-7810-3949-b441-2d899ff60538 | -1.51903 | -61.58722 | 2024-10-13 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e318efd6-2d66-3526-abdb-c1577017bb5e | -1.51849 | -61.59068 | 2024-10-13 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0fcd2f4c-0523-3d25-83b8-9e3a58f94f00 | -1.51518 | -61.59016 | 2024-10-13 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| de286b01-981c-3440-b8aa-00c0e47291c2 | -1.51187 | -61.58965 | 2024-10-13 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 86278e8a-2ca2-3f31-85a7-efee2b367501 | -1.49145 | -61.59001 | 2024-10-13 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96ec3300-1aeb-3810-869e-bbfc37d82309 | -1.48759 | -61.59295 | 2024-10-13 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2224f0dd-3a35-3d96-ac14-beb092c9aa5e | -1.48705 | -61.5964 | 2024-10-13 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35df9c79-27ae-316b-9fed-bcd5fbab2e59 | -1.3987 | -61.27247 | 2024-10-13 05:25:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c6279d8-d840-358d-a780-e06e17336210 | -3.00388 | -61.4152 | 2024-10-13 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 038bb112-a258-3036-aac5-e8718206982a | -3.00334 | -61.41864 | 2024-10-13 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6dc2ff40-d2f0-35c1-a199-3c52b3dae632 | -3.00111 | -61.41126 | 2024-10-13 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 954afb32-22ef-38f4-915a-0fa41898524c | -3.00057 | -61.41469 | 2024-10-13 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 316a6691-d8e3-34ed-9cf2-39e82ba6e105 | -2.99127 | -61.43083 | 2024-10-13 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 612b013e-bdad-3d07-aa45-ebd74350ccf2 | -2.99019 | -61.4377 | 2024-10-13 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ad3ef41-4b54-3e21-92ab-a83875b7dc68 | -2.98689 | -61.43718 | 2024-10-13 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 30b468e7-3017-3068-9904-70a454815d3e | -2.89742 | -61.87412 | 2024-10-13 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5762a22-1ffd-30fd-9ec6-db91610c7e07 | -2.89411 | -61.8736 | 2024-10-13 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2634fedd-26e0-3555-92b2-56ce208df5c2 | -2.88526 | -61.86515 | 2024-10-13 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06df6329-08d4-382f-9770-270c560071cf | -2.87815 | -61.88882 | 2024-10-13 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ed87fab-9c6a-3f80-a051-87b127d42614 | -2.87538 | -61.88485 | 2024-10-13 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e9b8464-cf52-39d2-aa1d-b1e5c2b652df | -2.87483 | -61.8883 | 2024-10-13 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8db608d-70c2-34f7-a1ff-fd3c05d7b6e7 | -3.26477 | -64.83377 | 2024-10-13 05:27:00 | NOAA-20 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d24ba70-07ef-3a6c-ae82-03eab6bc809f | -3.26408 | -64.83806 | 2024-10-13 05:27:00 | NOAA-20 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d47cad09-d9a6-3500-a9c1-1dd4fe9dcf8e | -8.5666 | -67.12671 | 2024-10-13 05:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1dc75fde-d289-30a8-bb8c-f3b0f625e189 | -8.46461 | -66.99105 | 2024-10-13 05:27:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f1bd856-35b1-3d16-820b-36790fbee7dd | -8.4638 | -66.99588 | 2024-10-13 05:27:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09fb236e-a63f-30f8-b1b2-22768091347f | -8.4593 | -66.97517 | 2024-10-13 05:27:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8629cfec-29f9-35fe-905a-b4b36215a10e | -8.45625 | -66.96964 | 2024-10-13 05:27:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README98.md)
