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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f47dc2c3-c667-37db-b0e3-952f5d1fe829 | -13.49484 | -61.44742 | 2025-11-02 05:12:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8c54cb2-244e-3f2e-b566-3597cdd357f2 | -15.30589 | -59.23738 | 2025-11-02 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea58b3a3-7f32-3c4a-9374-d1f4ae289134 | -13.49551 | -61.44345 | 2025-11-02 05:12:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a0cceff-009a-3ae6-beed-12146f820593 | -15.30258 | -59.23684 | 2025-11-02 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a6570d9-75da-322f-8734-251f34d5b9be | -12.46349 | -54.32001 | 2025-11-02 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e734bb07-5743-3ddc-ad53-e6d6a85dbf8a | -14.6601 | -46.61894 | 2025-11-02 05:12:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70d342e2-ec81-3e78-b7f7-6c33745dbeda | -10.78294 | -56.81841 | 2025-11-02 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f68aad8d-0f36-330a-b142-2ee07b98066b | -12.31859 | -57.7293 | 2025-11-02 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b79e4d3-7ae6-3b17-bf78-957f6f1dc46f | -12.46508 | -54.32148 | 2025-11-02 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 139fcb72-02d7-3ad1-a01d-4a75189749fa | -12.43154 | -63.14163 | 2025-11-02 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac616e0b-eee4-3ffb-9c52-e469066975e9 | -11.88283 | -63.4488 | 2025-11-02 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| caf772b6-a8bb-32d5-a450-422c3316eb86 | -12.37325 | -63.87833 | 2025-11-02 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbc2c5df-4ce6-3ada-9567-c0ee366e12f9 | -12.3713 | -63.88919 | 2025-11-02 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d52a6418-3152-3db6-b2d4-78838a139428 | -12.37534 | -63.88995 | 2025-11-02 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 116c685e-d717-3d21-8592-483a13e0743e | -11.3638 | -54.3124 | 2025-11-02 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86b7de5d-227c-3804-9e84-cf6945f6754e | -11.36311 | -54.31715 | 2025-11-02 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a64fed84-83a0-3df8-8b9e-ed4c7cc036c8 | -12.37195 | -63.88557 | 2025-11-02 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fea6a84d-b192-309c-bad2-a3ca06e7926e | -13.98149 | -51.50764 | 2025-11-02 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 62d14de3-b754-3711-b3c2-f211a8c8bb2b | -13.4978 | -56.56977 | 2025-11-02 05:12:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 689c9096-7ad8-3886-b853-4da49aa3e132 | -13.49269 | -61.43886 | 2025-11-02 05:12:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0338db83-eb5d-3646-9c58-9647f8ce6f8b | -14.66116 | -46.60886 | 2025-11-02 05:12:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d38c57f-7f30-3417-b81a-0b4fbb9b0397 | -13.76923 | -48.86979 | 2025-11-02 05:12:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0829931-49a2-39c5-b8d7-3101175f7e5b | -12.42321 | -54.49113 | 2025-11-02 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5913264-41aa-31fb-8d11-49c0fe850215 | -12.46663 | -54.32549 | 2025-11-02 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e7210df-1c56-335a-bc22-ee94c92e7891 | -12.63978 | -62.10903 | 2025-11-02 05:12:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5b1c778-dfbb-31b1-81fa-77885a2e8671 | -15.66785 | -56.15164 | 2025-11-02 05:12:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 81920f51-62c7-3b94-b4bb-ff10d44bf448 | -12.86781 | -50.8836 | 2025-11-02 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4d9b65db-4fb9-3fae-9a35-950b9aa1660b | -12.87685 | -50.89037 | 2025-11-02 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2fe54bc9-0731-3bca-a26d-a99c7e133896 | -11.35869 | -55.13663 | 2025-11-02 05:12:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad7fde17-1469-34c4-bf6a-035a630f66c5 | -13.9761 | -51.51218 | 2025-11-02 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b866d859-384a-3025-8562-7e0e0b0457bc | -12.46279 | -54.3249 | 2025-11-02 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67fa42b7-8d84-37bd-a4ea-98e5a768569b | -4.1361 | -51.152 | 2025-11-02 05:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 320aeede-46d0-30de-96fe-4c3e9548f649 | 3.28299 | -61.14902 | 2025-11-02 05:59:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0985395a-c14d-3ad8-965b-11872b572c65 | 3.28195 | -61.15167 | 2025-11-02 05:59:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21959041-41e6-3cf2-95aa-7bd430380d46 | 3.28369 | -61.15343 | 2025-11-02 05:59:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98f6d0d1-e673-3a10-940a-d152c59d1ff8 | -12.43043 | -63.14451 | 2025-11-02 06:01:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c5a5daf5-a9bf-3f69-aede-8f0de3307f22 | -12.44103 | -63.14018 | 2025-11-02 06:01:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1e1302a-dd05-317b-9040-969514d3dabb | -12.37511 | -63.8828 | 2025-11-02 06:01:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9a84f50-56c8-35d2-b7d9-0701105d9c4a | -11.88499 | -63.44983 | 2025-11-02 06:01:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbe63bb4-d24a-338e-b80d-44010f909ec2 | -12.37981 | -63.88345 | 2025-11-02 06:01:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1066ed82-31b8-3684-bee7-02c93781c69d | -11.73705 | -59.30724 | 2025-11-02 06:01:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66a43905-8982-3374-9a2a-bbac73cbe1d3 | -12.3124 | -64.03685 | 2025-11-02 06:01:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db922485-44ff-3244-9c14-091c41305e02 | -12.38047 | -63.8784 | 2025-11-02 06:01:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25d23413-0ed4-30d2-98ea-cbdb1eaef234 | -12.23725 | -60.32035 | 2025-11-02 06:01:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05fe35ac-cd5f-3458-a358-73d45dca1b0b | -12.37108 | -63.87711 | 2025-11-02 06:01:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7298fb9b-c9e8-320c-8284-406425fe98b7 | -9.4127 | -68.07103 | 2025-11-02 06:01:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43e9b5d5-f4ec-375b-9a09-793b4dba22e6 | -12.37577 | -63.87775 | 2025-11-02 06:01:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7727cd0-35bc-3b73-99d8-9dc9e9ce82a8 | -12.43114 | -63.13884 | 2025-11-02 06:01:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c5ebac1-148c-32aa-9b4e-7a07e4872ce9 | -11.73645 | -59.3124 | 2025-11-02 06:01:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 128b5018-e235-3022-bc7d-b319cdbb59eb | -11.73078 | -59.30626 | 2025-11-02 06:01:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 464be6e6-ba09-352e-b0f2-6c1836eb8869 | -12.37042 | -63.88215 | 2025-11-02 06:01:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5756c80d-5276-3ca6-b843-53e9756eb4a1 | -12.43608 | -63.13951 | 2025-11-02 06:01:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d3f3d6ff-98a3-34eb-acdd-d242bee6b775 | -12.37445 | -63.88786 | 2025-11-02 06:01:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b6e6661-3cf7-3abf-8b43-b62de9c3e63b | -12.43537 | -63.1452 | 2025-11-02 06:01:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 24163a5f-678a-33c7-b447-4a500a2cec85 | -8.75893 | -66.98674 | 2025-11-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e59c41d8-0e1a-3a38-b2f2-abd45511d492 | -9.6835 | -65.61487 | 2025-11-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcfa1c58-2e66-3c41-8d11-df0be55fc106 | -15.62706 | -58.22856 | 2025-11-02 06:01:00 | NOAA-21 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1fb84f55-7b8d-3093-80b1-5132772ff821 | -9.68213 | -65.6144 | 2025-11-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c09ea1d0-270b-3655-9ba0-72959bff914d | -12.23673 | -60.32484 | 2025-11-02 06:01:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b9247fd-f1c4-33e1-8986-333e2b47d218 | -9.91683 | -66.71169 | 2025-11-02 06:01:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08daa7f4-7308-3da5-ba77-fa65ac68150e | -9.40938 | -65.608 | 2025-11-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f1b9934-33db-3969-ab3a-60b39a67c65a | -3.23636 | -58.8871 | 2025-11-02 06:01:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0164443f-aa29-329c-ba5a-4bc1b5f8ea97 | -12.44812 | -63.12379 | 2025-11-02 06:01:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8a53dd9e-3e10-35a2-88bc-71e0a9556463 | -3.65543 | -50.70463 | 2025-11-02 06:09:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 211a76de-b71b-3616-bc6e-b974083debd4 | -3.62069 | -51.47614 | 2025-11-02 06:09:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 485157b9-7e94-3136-b8ad-f7676cf7876a | -4.67728 | -44.61648 | 2025-11-02 06:09:00 | AQUA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ee041a25-46db-33c8-81e2-ffaf4cf2eb3f | -3.45889 | -50.22475 | 2025-11-02 06:09:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fadb0b53-f0a3-37fc-b722-5e2e5ca32ee3 | -3.50633 | -50.46828 | 2025-11-02 06:09:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d9cfbc8e-50ed-3b6c-943e-3cde6145af50 | -3.21837 | -50.58384 | 2025-11-02 06:09:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 620d3707-0ee7-3b5b-96b3-52fa072872df | -3.01438 | -49.43506 | 2025-11-02 06:09:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6e2f2f32-c43c-3c44-8e38-688c62651acc | -3.83074 | -51.30931 | 2025-11-02 06:09:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 25d13d61-3ed2-3b69-adfa-fbb1d3a80eee | -5.42176 | -44.63567 | 2025-11-02 06:09:00 | AQUA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7c897c74-70eb-36c3-80a2-2bc444dc2b95 | -4.14277 | -51.14773 | 2025-11-02 06:09:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 71dde09a-ee84-3069-906d-e4935ef174d8 | -2.83399 | -49.40522 | 2025-11-02 06:09:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2e48239c-afa1-39b5-a6bf-93a6dbbb7c29 | -3.02434 | -49.44228 | 2025-11-02 06:09:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5df0a359-3ff7-3c1f-94e8-609370cdb1f7 | -3.56127 | -54.56201 | 2025-11-02 06:09:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ae3e202c-81a7-35a5-95b0-969e0f09cd66 | -0.84615 | -48.62054 | 2025-11-02 06:09:00 | AQUA_M-M | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 947f4502-18fe-35e1-a7ff-06fa32678766 | -4.13326 | -51.14622 | 2025-11-02 06:09:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 51f2142f-594a-3ceb-b242-8da23acc4b4a | -3.01302 | -49.44408 | 2025-11-02 06:09:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 71042d2f-3bc4-3978-86d1-5a996c3d1bc6 | -3.51903 | -50.32168 | 2025-11-02 06:09:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d3801bab-695d-39e5-93f5-423d8a2798e7 | -3.24375 | -50.79319 | 2025-11-02 06:09:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 91d0ac21-f5a9-35a1-baa0-2e761006363a | -2.44817 | -49.03086 | 2025-11-02 06:09:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 66d882c6-bf45-307f-83cb-9bcd95717b69 | -3.46036 | -50.21526 | 2025-11-02 06:09:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 28040ce6-921c-3c94-80e5-f0b68d95ded9 | -4.13485 | -51.13577 | 2025-11-02 06:09:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6e5f3aa6-1934-3b8a-8c92-b66a2b1b9feb | -0.85499 | -48.62183 | 2025-11-02 06:09:00 | AQUA_M-M | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f3206f29-3fb7-3c67-93c3-e78f7cff407b | -3.06203 | -49.37424 | 2025-11-02 06:09:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 08796d34-8ab5-3480-b1bd-ac37b4e7f8d4 | -0.84749 | -48.61169 | 2025-11-02 06:09:00 | AQUA_M-M | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9761f747-3478-311d-9d95-0924b908fa58 | -3.23432 | -50.79178 | 2025-11-02 06:09:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5b56fd32-0148-33a1-9812-aab6127b1d5d | -3.45101 | -50.2178 | 2025-11-02 06:09:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c30af4d4-6480-3b15-8dfb-234f168db4f7 | -4.1361 | -51.152 | 2025-11-02 06:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 6ecd2ab2-575d-314b-91eb-abf7ca72a993 | -8.15499 | -44.47876 | 2025-11-02 06:12:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0c6403f5-6409-3785-adc6-6f83da93c8c6 | -9.05862 | -48.83214 | 2025-11-02 06:12:00 | AQUA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 38880ccd-2cb2-35b2-8760-10b536a8420e | -10.61836 | -52.18035 | 2025-11-02 06:12:00 | AQUA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2fd2460c-9fa7-3026-a99a-3cec0a81c3d1 | -6.73844 | -45.95337 | 2025-11-02 06:12:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| da14790c-f70b-3ade-8bee-0ea55ac46586 | -5.48285 | -48.64455 | 2025-11-02 06:12:00 | AQUA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 774f6429-febf-3399-9210-eb2bd28dd684 | -10.73796 | -46.24835 | 2025-11-02 06:12:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0dc9de31-e2e8-39e7-8054-ee9f1e3e2413 | -10.62766 | -52.18185 | 2025-11-02 06:12:00 | AQUA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1bdf1d5e-1432-3f58-92a5-126db7e128b6 | -9.06748 | -48.83345 | 2025-11-02 06:12:00 | AQUA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9de828c9-fa82-3a7a-a14f-7f87e5175947 | -10.9941 | -54.00146 | 2025-11-02 06:12:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4c17beb0-6476-3582-b693-0d19d35d2de8 | -12.86979 | -50.88685 | 2025-11-02 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |


[Clique aqui para ver as próximas entradas](README28.md)
