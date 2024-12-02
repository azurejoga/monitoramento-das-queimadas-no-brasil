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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 291ed836-cc86-360f-9101-5759030cf3a5 | -4.06382 | -49.07783 | 2024-12-02 04:48:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 27d6f461-9bbb-3b98-aee5-0c61332989b8 | -3.46511 | -50.2663 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc0f56b1-9ce2-3fcf-845b-12f7218cbc1c | -2.9006 | -51.57675 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c794f0bb-c732-3bd6-bd23-dd96362dcc3f | -2.70252 | -47.73772 | 2024-12-02 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08a72e04-683a-3efb-b868-2ccb7d45fbf9 | -3.76566 | -50.17765 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb5a6bfc-0c05-3b59-b9c2-51cc5dfaaa47 | -3.09751 | -54.13259 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fab2fcc-9c9b-3e62-996c-8188c0e2a681 | -3.06597 | -50.32733 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f358ffed-7e7b-34d7-b9b8-5a74453321f0 | -3.25998 | -48.89822 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1dbecdb-1155-3fc3-81a1-ae59d4c916a8 | -2.59372 | -54.25055 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cea51d6-30b7-342b-982f-43cf8079b0ee | -2.02249 | -54.31204 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d3eefa76-f21b-3730-ace1-c05d48b2bb7c | -2.54808 | -46.55754 | 2024-12-02 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5b0dc5a-7fcb-398c-96f9-42e3ab08aa17 | -2.16657 | -50.60502 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a44263d-2986-3e01-9213-09b497856f40 | -4.53317 | -45.69996 | 2024-12-02 04:48:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb1581b9-e066-3147-b46c-c42a151dc85e | -3.1597 | -51.11575 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f859ae0-6b15-3461-aced-e88a1433f1a3 | -2.28307 | -53.7869 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0fb6cac2-1dff-3e9a-aff7-30354eb76cf6 | -3.31268 | -50.50348 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06e74b5e-dd51-3937-80cf-76ce12d2a4a7 | -3.09343 | -54.13585 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ce93691-c6e8-315d-825c-e9312d3bc316 | -3.28615 | -50.44118 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bcde0bf-2ac4-3511-b7a9-23a5d2d8320d | -1.64715 | -53.86634 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ccfc9f1-e67f-37f4-a765-6cc4bb147bbd | -1.23471 | -51.62553 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc65afa4-3bc1-3456-8603-631b66e59956 | -2.47905 | -48.84726 | 2024-12-02 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e520b46d-7317-3c1c-8cff-dfbc398da25a | -3.98766 | -49.87777 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b08f7037-a6bd-33fd-bd37-84fda7f76d8c | -3.77939 | -52.03543 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 6bd465b9-a640-3003-bc5c-f2a501557df9 | -3.74861 | -52.27389 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 356005fe-4bfa-357e-a14a-10c5eb9f58f1 | -2.8748 | -54.03222 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2828cc72-8709-3698-8b6d-77b9ae2feec3 | -3.30375 | -50.04068 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9da2284a-8134-3ecf-9db8-384ae2b3a374 | -3.10293 | -54.0316 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a87a655b-a4a9-30bb-9613-a1d20d4bf227 | -2.45712 | -53.68243 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc92ac9b-1b03-38cf-b3b3-a03839bcba3f | -3.70786 | -50.25829 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02f5df15-8cac-3b8b-808a-68328bd92b0a | -1.49477 | -52.32516 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc8e8716-424d-364c-a6c4-f988196fe51d | -1.27817 | -54.5519 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9016969-d0f5-3f1c-ad88-4ea134279ba4 | -2.00165 | -51.17918 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7018f4df-b278-3f04-957c-32a3338299b0 | -2.71033 | -54.15655 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a831ebf0-703c-3afa-92dd-036166b0e205 | -1.49646 | -54.45247 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccf2c4c2-9c4d-33ee-9ece-650f9ff5ccb1 | -3.33695 | -53.37465 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f466ca80-271b-34df-bf57-f1a0e658036c | -1.90647 | -52.86237 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 58607c50-a502-3d59-b9cd-420d6d2c0431 | -3.25398 | -53.63369 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea00b794-1d8f-3da8-985e-dd0bf518410b | 1.1072 | -56.0267 | 2024-12-02 04:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 0158bc05-0eda-3961-88ab-3773fb39af40 | 1.1072 | -56.007 | 2024-12-02 04:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 06926382-d9e8-3142-95e1-bd3d3c4dfa2f | -3.259 | -53.6388 | 2024-12-02 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 193f3965-2a0a-341a-aeee-2fe1cb334c01 | -3.2591 | -53.6186 | 2024-12-02 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 64c0a055-c9ff-372a-bf29-361ffb403659 | -5.1181 | -43.1964 | 2024-12-02 04:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 245249d0-1399-317a-b01f-35b997151de6 | -5.5882 | -45.1412 | 2024-12-02 04:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| c8650fb0-ed09-327a-a90e-94fc8be54575 | 1.0889 | -56.0072 | 2024-12-02 04:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 921caee6-f4aa-3bc3-83ab-094587d0ad37 | -2.5612 | -53.3931 | 2024-12-02 04:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 911f78ae-b2a1-3c2e-affb-cd156a491c91 | -5.118 | -43.2198 | 2024-12-02 04:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 400c4bf9-ce59-3407-a295-1e59e72c74a8 | -12.4358 | -63.7455 | 2024-12-02 04:50:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 845dc97d-9ca3-344c-a383-dad395f67455 | -3.2708 | -46.4511 | 2024-12-02 04:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| efb42df5-828d-3033-8c12-fb78d8040704 | -12.4169 | -63.7465 | 2024-12-02 04:50:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 3006f939-d97d-33f5-823d-97acb902e9ce | -6.0777 | -48.05108 | 2024-12-02 04:50:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 01945cff-e50b-3d59-945d-f86f809ba933 | -11.06081 | -45.37384 | 2024-12-02 04:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2b39375-c427-31ad-b9c6-ca0c4e371683 | -9.34987 | -58.22238 | 2024-12-02 04:50:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf563b49-d30a-325a-9fef-67ce43e6db75 | -9.76957 | -56.92886 | 2024-12-02 04:50:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 107b1516-af52-318b-8fd7-503e50171a71 | -9.34525 | -58.22519 | 2024-12-02 04:50:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a975d3f5-f73c-306c-8415-f4cdfe59b542 | -6.37105 | -47.35416 | 2024-12-02 04:50:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fad9b12c-5076-3732-8e24-e80dfc8325a5 | -4.84518 | -50.49357 | 2024-12-02 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a876e685-65aa-30fc-be9c-4a1993b6e508 | -11.06052 | -45.38143 | 2024-12-02 04:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0e8d04e-62ae-3117-9772-81b5f9953403 | -8.83559 | -44.77791 | 2024-12-02 04:50:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24be0ded-0e47-30da-8111-8f968f4bf3c2 | -10.65431 | -44.49299 | 2024-12-02 04:50:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4140dbaf-4540-3233-90b6-b4822aa13aa0 | -10.65473 | -44.48969 | 2024-12-02 04:50:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13307a95-7835-34d1-b48b-3b2a6c30bdcb | -5.65108 | -51.4706 | 2024-12-02 04:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b568b600-a02c-30a2-85c7-acc10c271b16 | -9.36287 | -58.24295 | 2024-12-02 04:50:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93505c8f-936b-34df-94f6-90968d6bb615 | -9.91175 | -44.33084 | 2024-12-02 04:50:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20d3cd20-b553-397b-bf71-3216cbd5c560 | -6.81667 | -46.77377 | 2024-12-02 04:50:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4520241e-5fd7-37dd-96d2-6ec700a589ef | -5.21758 | -50.12159 | 2024-12-02 04:50:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2c2f119-cf51-3fbd-9476-758871ad48fe | -5.64015 | -51.32484 | 2024-12-02 04:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35474dad-0563-3bae-bfca-3a1b1ee6a71a | -5.93173 | -47.20641 | 2024-12-02 04:50:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a5cca25-9ad2-36d4-8e4e-e09e79736fcc | -10.49884 | -44.91637 | 2024-12-02 04:50:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 940753ce-3afc-31a7-a196-9e9a0685e409 | -4.84858 | -50.49408 | 2024-12-02 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cc14d18e-3d3d-32ba-999c-079235241510 | -5.90805 | -46.25257 | 2024-12-02 04:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00be625b-1d48-351e-9845-dae23af4e9e4 | -4.15421 | -55.02151 | 2024-12-02 04:50:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14bb14a2-7908-3cba-aa08-53d157b02a15 | -3.52113 | -62.76911 | 2024-12-02 04:50:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21cbf6f6-91e0-31d4-afce-92c90a98d20b | -10.65957 | -44.49369 | 2024-12-02 04:50:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34049bc0-149b-3e7a-ba2c-be8c4f368bf2 | -5.99918 | -45.41983 | 2024-12-02 04:50:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 032ad225-8507-347c-89a5-034b1b58426b | -9.33925 | -57.60533 | 2024-12-02 04:50:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90bc88ac-ab6c-37c5-bd59-42f7028f713e | -3.79428 | -58.9763 | 2024-12-02 04:50:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84d609f4-9cf0-398e-a5d9-5ad17ff336dc | -9.34804 | -58.23297 | 2024-12-02 04:50:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 220116a7-400e-3500-aab4-61168c604c7a | -9.77327 | -56.92948 | 2024-12-02 04:50:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8731eafd-7672-3bf5-b849-07cafafaca8b | -9.36689 | -58.24367 | 2024-12-02 04:50:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 251b5571-5632-36eb-930e-98e7a81b809c | -6.36698 | -47.35393 | 2024-12-02 04:50:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb4b0ae2-316f-3d36-83f3-490fd722335d | -11.07664 | -44.31101 | 2024-12-02 04:50:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26c19321-b346-32cd-adf4-85800d40b463 | -6.08859 | -48.05767 | 2024-12-02 04:50:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a408fba6-8e3f-394b-9d35-55fe5d8c28c1 | -5.16626 | -56.15327 | 2024-12-02 04:50:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 701b2124-3f72-3539-aa76-7db843b46fa2 | -10.7001 | -44.97395 | 2024-12-02 04:50:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc06167a-36da-3bd1-b0d7-a55ec06e2e44 | -4.84536 | -50.69359 | 2024-12-02 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe13ee81-5600-35ee-9b64-ac0d46f56218 | -6.08157 | -48.05167 | 2024-12-02 04:50:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a2dd7969-204f-341d-b8fd-92b4cab4d104 | -9.34926 | -58.22591 | 2024-12-02 04:50:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddd8e6e5-ebb5-3850-99e7-f549325c041d | -9.91131 | -44.33412 | 2024-12-02 04:50:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e88f979a-417d-3585-bed2-29486502ab39 | -10.84007 | -55.18435 | 2024-12-02 04:50:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 911e330f-a38d-3979-a7ce-835582907e82 | -5.217 | -50.12534 | 2024-12-02 04:50:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2a54208-5a78-3967-965d-40823ce6e0df | -5.64071 | -51.32132 | 2024-12-02 04:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ae82f2b-6e81-3b1d-99a7-ee3f4c4eb1a7 | -4.26486 | -54.67194 | 2024-12-02 04:50:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3014adc3-ac71-3fb5-8d5a-2af5540f6cc4 | -5.9124 | -46.25319 | 2024-12-02 04:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba524574-2ddf-3a72-8ef8-f0e4ce4adeca | -5.23615 | -56.06053 | 2024-12-02 04:50:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64c78bc5-3af6-3e36-b2a5-755af8409dd8 | -6.57173 | -59.09182 | 2024-12-02 04:50:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42ffa34b-870a-3372-8de4-8cbffd4afadd | -11.07325 | -44.31417 | 2024-12-02 04:50:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adeea10d-a88b-3ad3-9fb8-3e9e8bab073f | -4.18764 | -54.45554 | 2024-12-02 04:50:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 180f0b92-073e-341f-9334-7e2c9893ba09 | -9.91146 | -44.33182 | 2024-12-02 04:50:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7004b6b-21fb-3136-abbd-3db3c0e88b61 | -11.07903 | -44.31158 | 2024-12-02 04:50:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc9e3d03-0756-3e32-b0c3-9de6607998e5 | -9.34865 | -58.22943 | 2024-12-02 04:50:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README71.md)
