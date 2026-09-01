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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0a11e04-351d-3e92-a7ef-080459109635 | -6.37548 | -51.76202 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 40ab67a7-cf9d-327a-b3da-4c493fa8b0a1 | -7.1783 | -55.42152 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 699131aa-26ec-3656-905e-3231e8a8c160 | -7.01839 | -59.65037 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c019b73-662d-3fdc-be85-1072c2fe5202 | -8.93474 | -62.36712 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c76707a3-abbf-3e83-b5fb-d72a2627dc21 | -7.62307 | -55.30043 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a31dc0f8-37d8-38a9-9428-63cc12b366c7 | -11.66657 | -47.59171 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad300e03-a67a-3218-a1ae-ebf223b7708a | -6.26085 | -55.42377 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b42e20a3-ad03-3d20-a783-d62d23401a16 | -7.79454 | -49.26567 | 2026-09-01 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa0c3fcb-4da4-3249-8c0a-094c5f2002c9 | -10.78557 | -50.51854 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cba9c4f1-70e7-306c-a39c-a223d5c177e7 | -11.21518 | -46.13738 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d65885ee-671d-3539-bffe-1281935b91ad | -8.61817 | -54.85435 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8662f568-9270-37ae-b249-b7d10dea34f8 | -7.36218 | -60.59864 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 56c6cd03-4f3f-3657-8d66-cdf0e7aba5c8 | -6.15616 | -57.77781 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9bfc4a11-ec0f-39ce-8072-b4c15a2a0d30 | -9.13603 | -60.52515 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86784b4d-bc88-3026-af37-740c236011c9 | -5.24336 | -55.89152 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eed57bba-872e-3082-ad72-9158ae9aaf3b | -10.78503 | -50.52203 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 890dd718-6565-3806-83ee-853c0a1d98f6 | -8.80344 | -46.36717 | 2026-09-01 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9724e693-53f2-3ea9-af53-2dbda43a5dbc | -5.24866 | -55.90429 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d08122f5-b5d6-3353-b1df-58fa795d0472 | -8.24302 | -54.94823 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5146759-a7d7-3be0-81ce-d41fa16daf7d | -11.71757 | -47.63236 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff6476e5-da8f-31f2-9231-d0cb2151835f | -9.16742 | -59.36572 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e098517-d00b-386f-bc15-e762cbe832dc | -11.5108 | -50.2932 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 395e7ef9-f252-33b0-823a-22bb7298f02a | -6.92555 | -55.62638 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05f952bd-510a-3d54-9566-4e9a3aa07b1c | -9.67411 | -50.84124 | 2026-09-01 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5cb922f-5c4f-3893-a8c9-bdf83f55d458 | -5.95116 | -57.68303 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 244bd226-680b-38b7-98b7-b15cf3d800b2 | -11.79376 | -47.67651 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70bc34b0-6d35-3064-8973-c96b288e496d | -7.42147 | -49.74053 | 2026-09-01 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f04bc665-a805-36ab-a282-5816e86bf06c | -9.14799 | -61.09909 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ab89929-fd4e-3f7f-9982-a28981acf1ca | -6.75989 | -44.57485 | 2026-09-01 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 026ba6cb-7544-3b98-a02b-f03f81001620 | -4.09033 | -54.10014 | 2026-09-01 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90dfa94e-c534-3bb5-8578-d5a1d28173d7 | -6.78474 | -55.64181 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e67f17a5-0a85-3a28-938e-97cb56ba8218 | -10.85779 | -45.31047 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8bceaf9a-fb5d-3191-afb7-81babe65bb00 | -6.94192 | -55.63316 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6e89756-5687-3a32-b80d-57637c4a34f3 | -10.15276 | -45.74836 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d0d947ef-325b-3871-b73d-a392529cc8ae | -7.33958 | -60.5794 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9c5e1bcd-13c1-3093-914a-75cba158125a | -10.20791 | -50.36495 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 393d6eb1-d84f-336c-af27-9c0387f35b22 | -7.1182 | -42.75471 | 2026-09-01 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 59dcb788-b7e5-3a0c-8a83-d39a51ee1143 | -10.83907 | -50.63447 | 2026-09-01 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 344d91ba-81fa-3e07-bb80-a852f78498ec | -3.62523 | -60.55911 | 2026-09-01 04:40:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0f4593f6-028b-3589-bb2c-68add68f0188 | -8.13473 | -54.96952 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| aae049d1-c89c-31e9-a8b0-06af73df9e10 | -11.27824 | -50.58716 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 366ee8c9-a2c2-3e71-a2b7-05ee7a5b6116 | -7.1772 | -55.42196 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a70eb25-b791-39d2-8718-f9fe0f6fc92b | -11.66892 | -47.60084 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| acca68d9-abe0-3032-a887-03929208fd17 | -6.77346 | -59.43401 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 704da717-ad52-3d5c-b698-d31ba737a8f5 | -9.67134 | -50.85875 | 2026-09-01 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8ad77c7-da9f-3173-9ffd-ba2fd55a3dc6 | -7.25872 | -61.11043 | 2026-09-01 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9bfbe078-68ae-38ff-8198-0e27a2acaaaf | -10.03478 | -44.70454 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2817dab8-894b-3a20-a0bc-8e3a725c4949 | -4.80071 | -55.97743 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 721a2df6-a5ae-3b1f-a5a8-05d8d1ba277b | -6.8177 | -59.44151 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c29fa760-c67b-3947-8eb5-3dec8e20ac3c | -11.24492 | -45.15686 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb05750d-9ca0-3628-9498-63481720cb5f | -9.46759 | -57.01524 | 2026-09-01 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bbcd10e-62e1-3d88-b4cf-d77340247240 | -10.35307 | -49.97646 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf472dae-c393-365b-bec4-6c9a76469071 | -7.35563 | -60.59121 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 54f33349-c66a-32ed-9ab7-05196424c321 | -10.99502 | -48.39116 | 2026-09-01 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccb6575b-96d3-3704-aa0c-982042ee5b9b | -6.77409 | -59.43042 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ba62729-1acc-3097-9431-870bd3e10cf2 | -7.45696 | -59.93281 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 25b43ef5-3f77-314e-856f-d8172d52e965 | -7.884 | -47.07669 | 2026-09-01 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cdb8f27-cb65-3854-ac64-ba3b965443d2 | -10.32213 | -49.95672 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7b0ba59-aa13-3a55-8890-26ef763514c0 | -7.90792 | -44.25614 | 2026-09-01 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76e73277-85de-331a-89f6-4be5fc0ed560 | -8.50085 | -55.34603 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ff6613c-e787-359c-adc2-901c14e3c0fb | -6.36315 | -55.99961 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 172fd7ad-c858-3579-ad26-667badfce8bc | -7.09926 | -45.77274 | 2026-09-01 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9bd8543c-602b-3ccf-80dd-f6c48338d140 | -10.39381 | -48.23571 | 2026-09-01 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3683ea0f-f8b8-35d2-bcd7-d44d7a9bd96f | -10.35206 | -50.00505 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| fa135630-4bea-32db-95df-c9427f6d8b8e | -10.94833 | -49.77364 | 2026-09-01 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c616f893-7d33-3b67-984e-8b75f33fb59c | -11.10376 | -51.54353 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 927d6445-d843-39d8-967b-dd5d9a0d76f5 | -3.6195 | -60.56834 | 2026-09-01 04:40:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b517bd5e-7430-3d24-be44-f18279ca1725 | -11.93944 | -45.09974 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb52ee26-d72d-3c68-a2f0-182bed2cd13d | -9.15614 | -59.53693 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebd4aa84-f8ed-3da8-ab2b-2f065f6363b3 | -7.29315 | -56.68616 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c2f4338-c9df-368e-b245-03f34c92ebaf | -10.15857 | -45.76403 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d31ca56e-20e4-3187-b3fd-3a31653485bc | -4.80246 | -55.97592 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7c852759-fa5c-3f2e-8539-8ef3d262bade | -4.96351 | -55.85674 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5819584b-9e07-3972-ad3a-aaf74b9f50d0 | -6.59743 | -58.58986 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9344f892-eeab-3750-bc94-18acdd5e7165 | -7.35708 | -60.59311 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a6c43211-7818-37a2-a1ce-191dd1b04914 | -8.59419 | -54.7586 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83184f9a-0763-3e2f-9507-7cf6108e41ee | -7.62966 | -55.2862 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 023b7c04-c2f8-3793-a7f0-e28d2201c466 | -10.36478 | -50.01064 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd6090f0-c554-3959-9468-9aa17da23cd3 | -7.2961 | -56.69252 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1b8ac2e-57ae-3c8f-bc5a-50fd5ef1e8b6 | -5.25163 | -55.91381 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4d85f83-e172-3871-b549-8c2be1cac5f9 | -11.25804 | -45.35788 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6597f39f-a44f-3d4d-bb75-5097bfcf8185 | -3.12136 | -61.23282 | 2026-09-01 04:40:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4a817176-f87e-3dcc-b1f0-b624a4c233ab | -9.1764 | -59.63606 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf277435-b924-3f4b-9b26-5af83c755dbd | -5.95066 | -57.68589 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70d5e08a-d700-3038-8523-98151f84f340 | -10.75047 | -47.99069 | 2026-09-01 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea3b997b-518a-3593-b53a-21020a365293 | -5.25313 | -55.90501 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 987c0c4e-9e2d-3b81-84fa-0efd84344706 | -9.4668 | -57.01974 | 2026-09-01 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b85bc091-413f-3b46-a8fe-472736b78b1b | -11.23995 | -51.24273 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ea4de70-8480-354c-b523-273b8d63b939 | -6.80981 | -52.68351 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6c33db1-538d-3cbe-9f3d-d8f5890568a0 | -10.03559 | -44.69413 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7637138-4347-3070-ba6f-f784f05b6477 | -9.01518 | -44.85336 | 2026-09-01 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3288993-04ea-3759-bca1-9e8766044f1b | -9.15359 | -60.94073 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b06a491f-7979-3667-99e7-a6a1cef15030 | -8.50303 | -55.30923 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11709a6b-1329-3cc0-9097-b1e67da2d3c9 | -4.97169 | -55.8354 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53b5bf7c-d96a-3690-892a-b9024199b2cd | -9.18368 | -59.45765 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6cf98aaf-4a7d-3285-b1d2-000b8af83b1d | -8.76272 | -50.47289 | 2026-09-01 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec391d3d-f6ab-34c7-9274-b34becfc4b3d | -6.12051 | -57.68387 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 41d6b6fd-cb02-3472-80f3-44b0424e03d9 | -7.19809 | -60.67586 | 2026-09-01 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e5dd1293-23f7-3fd7-af56-f64f72010082 | -6.81151 | -59.5688 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d09195e6-f60f-366c-b79a-95802a797680 | -10.32558 | -49.113 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README38.md)
