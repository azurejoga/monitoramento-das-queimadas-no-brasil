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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60854113-72fe-3a72-b79d-b029f5152f82 | -8.85703 | -49.88448 | 2025-11-05 05:33:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3af0585a-315c-3c74-9503-8547fb616470 | -12.43058 | -63.15226 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| feaa3a80-2603-3028-bc64-80eb826863a3 | -8.86455 | -49.87944 | 2025-11-05 05:33:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1224451-311f-3c3c-bca4-e8b9a3f462b2 | -8.0613 | -49.64294 | 2025-11-05 05:33:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87e43ba1-a545-3af0-af16-30aea1224594 | -12.24913 | -62.3401 | 2025-11-05 05:33:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4cd0efe-a793-3da3-9e9e-b8970ce236e0 | -12.44112 | -63.15034 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc90d213-cce3-36db-9827-3c7925071786 | -13.37861 | -61.29384 | 2025-11-05 05:35:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f24c7b9-ec5a-33e6-bbff-40a2301a98e3 | -16.19018 | -56.76663 | 2025-11-05 05:35:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 033023bc-609a-3b20-92f3-91f45721bf4d | -18.51432 | -53.50185 | 2025-11-05 05:35:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5e4946b-c68a-345e-ab24-d657dcaf138b | -15.67753 | -58.38588 | 2025-11-05 05:35:00 | NPP-375D | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b4e53e7-5022-33ed-8948-33cf1646dcfc | -13.3751 | -61.2933 | 2025-11-05 05:35:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7babe7f-a91b-3510-a034-f97ee4202672 | -13.37159 | -61.29275 | 2025-11-05 05:35:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 125ae69f-ded8-3605-b8f2-c3f096d1cafe | -18.51349 | -53.51046 | 2025-11-05 05:35:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c73fee9e-6391-3a9b-9959-2c95ff9c0853 | -18.11225 | -53.56659 | 2025-11-05 05:35:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3eaf83ef-7b36-3bf5-adc3-99a2ad926cd1 | -16.18953 | -56.77187 | 2025-11-05 05:35:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 772fd16c-b2de-34a0-aebe-40990b459d32 | -18.5139 | -53.5062 | 2025-11-05 05:35:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d99e4d8-a743-341a-9245-171e4ccafa51 | -13.37452 | -61.29727 | 2025-11-05 05:35:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00efd28c-ab56-379e-aed0-74f99517dc55 | -18.11784 | -53.57168 | 2025-11-05 05:35:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 917c20a3-1518-328d-8723-a07c428c2da7 | -18.11829 | -53.56721 | 2025-11-05 05:35:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 934992b4-fc74-3222-90a3-58e3491e3256 | -4.4633 | -43.2152 | 2025-11-05 05:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| c6f12aaf-ab15-3653-acb3-6d23dcad2e0a | -4.4259 | -48.9465 | 2025-11-05 05:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| d8ae6cb0-12d3-39e8-84bd-ef3fcba5ba0d | -4.4073 | -48.9474 | 2025-11-05 05:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 69342609-0170-3f86-b9fb-103def46dd13 | -4.4073 | -48.9474 | 2025-11-05 05:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 2abedf4f-701d-3ad6-8221-b498629c97fd | 4.8799 | -60.25635 | 2025-11-05 05:52:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fca7c35f-d8fb-35b8-bdae-ac59b1174dac | 4.87629 | -60.26042 | 2025-11-05 05:52:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 006b7e8a-1006-3283-8ed3-5a3798aab6c7 | 4.44671 | -60.49104 | 2025-11-05 05:52:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b84723c5-a6d9-3557-adb0-7671af06b9c6 | 4.44426 | -60.49018 | 2025-11-05 05:52:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e8630f4-84b5-3385-a73e-5057762c1942 | 4.44247 | -60.49114 | 2025-11-05 05:52:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d33aa6fa-7a38-3a28-8f7b-8f0b8fc1875d | 3.25019 | -60.68939 | 2025-11-05 05:52:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d86a3bd5-9ad3-3b62-a481-acd4606757e6 | 3.31849 | -60.07712 | 2025-11-05 05:52:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a996365-4edd-3e95-967d-b4faa591e8e5 | 3.24125 | -60.68704 | 2025-11-05 05:52:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1e7dcb3-5c84-3743-94b0-1b72ce414b15 | 3.14683 | -60.72129 | 2025-11-05 05:52:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84efae98-2630-3c80-845c-99396c9f7e8f | 3.31918 | -60.08125 | 2025-11-05 05:52:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0c514cd-9083-370a-a5ad-793489301332 | 0.84534 | -59.33505 | 2025-11-05 05:52:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6a53851-2e55-3870-8faf-414e223066ec | 4.86545 | -60.24699 | 2025-11-05 05:52:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77bc872a-1883-386e-8095-48ce8a344ee7 | 0.8445 | -59.3298 | 2025-11-05 05:52:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a920573b-d40c-39da-87fd-c8367c967f09 | 4.87572 | -60.25703 | 2025-11-05 05:52:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47fe8cca-4d1a-30fb-8b6e-57382f4c50c0 | 4.44092 | -59.93567 | 2025-11-05 05:52:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b81653f8-2c5e-3ec0-9795-66be211a95ea | 4.44484 | -60.4937 | 2025-11-05 05:52:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7e80324-f83b-3b0d-97d5-1a52b4e08697 | 3.14744 | -60.72507 | 2025-11-05 05:52:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6391f825-eb2e-3f83-be65-77264c1e57be | 3.29624 | -60.67477 | 2025-11-05 05:52:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb67319b-5fac-3c82-a747-22f57000845f | 3.24959 | -60.68569 | 2025-11-05 05:52:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abe0b73a-a6c8-3c24-98e9-9d0030256e49 | -12.5874 | -62.981 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ebf1440-3e1a-3f9c-9ac3-8e80601aa06c | -12.43688 | -63.15133 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c3603e9-ad45-31bf-9d49-1c9b66ee12bb | -10.82067 | -69.40501 | 2025-11-05 05:57:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e33b1f66-3210-362e-89c1-94f9a382f293 | -12.42648 | -63.14825 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c51da7df-b190-33a8-afaf-ee241547f357 | -12.42022 | -63.13985 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7bd85dbd-aece-3fb0-b798-3d2695aa113b | -12.25028 | -62.34197 | 2025-11-05 05:57:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e8bb171-7cc4-36f9-b8c6-3f5702de52b7 | -11.73098 | -59.32297 | 2025-11-05 05:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 06dbd909-e9da-3524-925a-d25bef64642b | -10.77329 | -69.42603 | 2025-11-05 05:57:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c9fffe8-bb2a-3678-ad54-4c4e6023450c | -12.42794 | -63.1501 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37bd327b-0015-35e5-b6b2-aed375d7a237 | -12.43989 | -63.15012 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ee380ee-9870-30e6-8f13-7af700e8986d | -12.42589 | -63.15277 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adde2758-f495-3113-92bd-b8b3ae8a248a | -10.78817 | -69.41768 | 2025-11-05 05:57:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d42576be-f488-3dd3-a477-13df1b822de0 | -12.588 | -62.97633 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67558e09-e4cc-39b9-8104-1eb4437e397c | -10.92336 | -69.20678 | 2025-11-05 05:57:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8e68d1e7-ed0a-375c-abe1-7abc904b5ab1 | -12.43241 | -63.15071 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cfc7f23e-f0cd-3abc-a2e9-424db18c3a8a | -12.41961 | -63.14436 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e700564-37c2-3709-9421-ecd99c219f77 | -12.44135 | -63.15194 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5921e50e-6513-3fe8-a102-64f2dc17dee6 | -10.92667 | -69.20731 | 2025-11-05 05:57:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d32243c6-51de-3010-a98f-8ebb544d18dd | -12.42469 | -63.14047 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a1bf7212-5fb5-3da6-91c7-a54da125cbfd | -12.41899 | -63.14888 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f63bb2a-03c1-3420-8c36-38e92b953dd9 | -12.43037 | -63.15339 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 845cd242-2f1f-3c0b-bed0-cee2775f2191 | -12.43095 | -63.14887 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4281346-5dce-3c15-9162-c91a50225de7 | -12.44943 | -63.14682 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e2106a2-ae37-3374-9a87-8d028668cc79 | -12.42346 | -63.14948 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c4b681c-2dae-3aa7-ac12-38e8d2515b8c | -12.44437 | -63.15074 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ede60a46-83a8-306d-9da8-afea5f53f64a | -12.44884 | -63.15135 | 2025-11-05 05:57:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 31cb7432-bd41-3b54-bba3-5fa78bdd940f | -4.4073 | -48.9474 | 2025-11-05 06:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| ff1ec02c-6bec-3d77-a398-409882d74ddb | -4.4073 | -48.9474 | 2025-11-05 06:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| a8369228-08e0-3eb6-b277-f96219214d79 | -4.4259 | -48.9465 | 2025-11-05 06:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| cdcc529d-4be4-319e-a794-693f5d77b883 | -4.4073 | -48.9474 | 2025-11-05 06:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 21129731-f900-3923-afec-fe20490260f2 | -3.49373 | -50.46678 | 2025-11-05 06:26:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f028aae3-057e-3dea-a63c-13ae480ee490 | -2.64918 | -48.5013 | 2025-11-05 06:26:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 42af5a37-cb1e-35ef-82f3-c7aa59e76fea | -2.41884 | -49.29914 | 2025-11-05 06:26:00 | AQUA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 52717120-2422-3351-b812-2a92351132c5 | -3.43682 | -50.2343 | 2025-11-05 06:26:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0e23df24-fa97-33ad-8bdf-675d429b3ad9 | -2.61448 | -49.22331 | 2025-11-05 06:26:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bdcdab64-9ccf-3149-a4c1-a690fbe9e928 | -2.64727 | -48.5142 | 2025-11-05 06:26:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 5ecd4d96-4301-3e3c-a97a-ecfd6a000d28 | -3.49522 | -50.45686 | 2025-11-05 06:26:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c4b8c0d3-176b-39f2-8c06-f626a7a92872 | -3.81394 | -51.29058 | 2025-11-05 06:26:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b30909ff-2059-3bb8-96cb-cbbada0aa31f | -3.54047 | -45.4497 | 2025-11-05 06:26:00 | AQUA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 2e076bf3-f30d-339e-b81d-5236811b0e56 | -2.78496 | -50.31035 | 2025-11-05 06:26:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| e43326fe-8fd4-3feb-93b3-010fa489f8cd | -2.84395 | -49.40319 | 2025-11-05 06:26:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 099a2534-fd88-3bbd-9921-5b6981bcb730 | -4.40641 | -48.94071 | 2025-11-05 06:26:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| c55af38c-ef14-3ce3-9a88-7b33313e63b3 | -2.8324 | -49.41311 | 2025-11-05 06:26:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 37346bd7-6648-3f64-8857-84a193ba13de | -1.28156 | -49.14685 | 2025-11-05 06:26:00 | AQUA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| cd60e9a1-2798-3c3b-b486-e224249c0e3b | -3.23844 | -52.91325 | 2025-11-05 06:26:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ac1f71f5-e9b8-3f53-82a0-c9fc762d7b87 | -2.97731 | -48.70349 | 2025-11-05 06:26:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1d83ea99-4138-3a14-a73c-28f8758c535d | -3.82045 | -52.35952 | 2025-11-05 06:26:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a1778f09-1945-3747-b549-d89b480b564d | -4.45513 | -43.19711 | 2025-11-05 06:26:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 928de477-1fb6-308d-ac3d-c016b24f4e9f | -2.65973 | -48.50281 | 2025-11-05 06:26:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f2649f1d-49c9-367c-8629-ce12dfd9d769 | -4.45954 | -43.20606 | 2025-11-05 06:26:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| c9a3438a-3d08-3ce4-b11f-45174d78671a | -2.65782 | -48.51563 | 2025-11-05 06:26:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4a17cdb6-1cbc-3141-a3c6-19e29109111b | -3.30941 | -53.84267 | 2025-11-05 06:26:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 34231875-3cf1-367c-ad14-f9c68daa26f0 | -2.7835 | -50.32035 | 2025-11-05 06:26:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 65b7d271-a0a6-373e-b7cd-70ed3d7c8770 | -3.81533 | -51.28133 | 2025-11-05 06:26:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7aabba5c-fd16-345f-8e62-3a526ec6010d | -3.4399 | -50.21381 | 2025-11-05 06:26:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4ab319eb-fd86-3ad4-a765-2bc122cc40f0 | -5.03381 | -43.60884 | 2025-11-05 06:26:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| e748ee06-ec33-3a75-8825-08c2be4f9aa8 | -3.44488 | -50.21084 | 2025-11-05 06:26:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| eb746131-c673-3f9a-b8c8-a7401c05aaa9 | -3.31079 | -53.8336 | 2025-11-05 06:26:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README39.md)
