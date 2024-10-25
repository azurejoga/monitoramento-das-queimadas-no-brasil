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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22bfb2be-68ae-30e8-8b65-f1e366f04d1e | -3.5778 | -54.63255 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ebe89843-5f74-3a92-9ac9-e4ecaf0f4865 | -3.51775 | -54.63236 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 59cc3bdf-d3f3-31fc-843d-48450223b16e | -3.49118 | -54.45403 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 62e0a5cb-09a7-34a3-9823-228bbb26040b | -3.48928 | -54.44126 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 9eed5a62-fafe-3342-b047-5ca4979ed981 | -3.48629 | -54.44609 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 3823286a-dc9f-3f44-a5e3-08e5e9c72feb | -3.44297 | -54.13106 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 1ca4678e-b056-3333-8115-6c2e73fb1a38 | -3.43825 | -54.14838 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2ed91588-8011-3208-bb41-04052c1164ba | -3.42751 | -54.14988 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f83b57fe-72fd-37c5-bca7-a3118d2c2f7f | -3.41195 | -54.28138 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 96fdf765-80aa-352f-9bc9-d044282ee5d2 | -3.41133 | -54.27731 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6181d55f-dd6e-3285-8a15-8eb105d732a8 | -3.41071 | -54.27325 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 28d53d54-7f24-32ec-baf9-ec80de119fec | -3.40835 | -54.28189 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| aa464955-02fe-3486-a7f3-d6812c6e7cbe | -3.40773 | -54.27782 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 11340467-998a-38d9-9660-4d738ed6d756 | -3.10915 | -54.1506 | 2024-10-25 16:52:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 62a5020c-48b6-3b3f-8595-14afa1a35983 | -3.10738 | -54.16311 | 2024-10-25 16:52:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ba720d29-1426-3077-bacc-5701d8deaf82 | -3.10679 | -54.15913 | 2024-10-25 16:52:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 692c5a46-29da-31ab-99f0-0262a53eac30 | -3.10619 | -54.15515 | 2024-10-25 16:52:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 32ba4e38-fe86-3239-abd9-221aa81d7911 | -3.1056 | -54.15114 | 2024-10-25 16:52:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c362559b-4b53-33bf-8fc0-487f54b966be | -3.10441 | -54.16762 | 2024-10-25 16:52:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f3b48dbc-0ceb-33cb-8279-69651091d3f8 | -3.10263 | -54.15567 | 2024-10-25 16:52:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 40dbb0c9-5ab1-3446-94a0-6c4d657bf12a | -3.10203 | -54.15166 | 2024-10-25 16:52:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 428cce5d-a6c2-36db-b90b-fd8573ea865b | -3.09966 | -54.16016 | 2024-10-25 16:52:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b8c31109-2f81-39ea-a660-bc8bf4a904f7 | -3.09847 | -54.15219 | 2024-10-25 16:52:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| deb38670-ba5e-32aa-bd40-bb7d5eda5b4f | -2.99538 | -54.54476 | 2024-10-25 16:52:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| accc5356-83fe-37c2-8ce2-57c66815408b | -2.93933 | -53.91436 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 847adfcb-77c6-3e84-a8f6-c94ef69b1984 | -2.92647 | -53.9243 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a5bfd5a8-f0c4-3c80-9756-ccf6c9a7f3ab | -2.84155 | -53.98484 | 2024-10-25 16:52:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 262a9550-8a18-31b9-8e23-35b0b93174c5 | -2.80519 | -54.00635 | 2024-10-25 16:52:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 1eb7fe86-2cfc-3de2-a3d1-a993b2bea3f5 | -2.79348 | -54.02425 | 2024-10-25 16:52:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0177f4e7-29df-3250-bf49-bd1cd4442778 | -2.79306 | -54.09328 | 2024-10-25 16:52:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b0afba6c-7049-32bf-bf6b-02e28ea57494 | -2.79288 | -54.0203 | 2024-10-25 16:52:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5ff68840-54cd-30a6-aead-187ada08a339 | -3.27126 | -53.71006 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3b1e610a-9155-3f44-9f36-8046b3be587b | -3.26776 | -53.71058 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 93b71041-32e6-3ee7-9d2b-b8d618dcb2c8 | -3.26135 | -53.7155 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 034c4923-70e7-30d3-9687-871a9d967401 | -3.12273 | -53.71636 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e21f02e5-0c27-345a-a3cb-6ee799cbc292 | -3.12154 | -53.70863 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 47ef4615-75f5-3f0a-a751-04b91cd883c5 | -3.11923 | -53.71688 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 44d189b1-0e06-3cea-be69-ffed3d67d741 | -3.11053 | -53.73005 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| c896f2d3-bf33-3a79-8dfa-fba8914cc3f0 | -3.10994 | -53.72618 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 6594c89d-566c-3095-abc1-875b96a8f9ab | -3.10935 | -53.72231 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| a62ccde5-1713-3cee-91b0-d3d8875a42aa | -3.10763 | -53.73443 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2ca7e803-b18a-3eef-b9fd-415bd853c437 | -3.10704 | -53.73056 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b0cd1e8f-9b81-3f97-9133-6d54a694d8c3 | -3.10586 | -53.72282 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| ed760654-4371-3303-b791-4b142f78c291 | -3.10414 | -53.73495 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 031e0386-e41e-37e2-a4d3-851aa08bcdde | -3.10355 | -53.73108 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| bb1f8922-198f-34bf-b73a-f70b4453ce63 | -3.10296 | -53.72721 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 83bd7300-ff61-3e52-8a24-b8c3acaa6722 | -3.10178 | -53.71948 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 711b5846-8b7f-3191-ba74-8b8f7ffc42a9 | -3.09888 | -53.72386 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6f28ba56-8768-3741-94c2-44b2df38de86 | -3.09829 | -53.71999 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 7661ee1a-b1c0-366b-b448-2fd930ccf165 | -2.94436 | -53.7029 | 2024-10-25 16:52:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5b9a301f-181c-3fdc-8b1f-bf0c02452262 | -2.94378 | -53.69905 | 2024-10-25 16:52:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 41ecae25-bd37-3de3-9f4c-7cf8bb3c571b | -4.49999 | -54.96239 | 2024-10-25 16:52:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 98374233-f66c-32c0-8701-ae06a42eae01 | -4.48708 | -55.08311 | 2024-10-25 16:52:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| be7d5d65-77e3-34e7-acae-e14d2be67ab3 | -4.48639 | -55.07846 | 2024-10-25 16:52:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| ef1512bf-7b84-3834-bb98-ced3b3271fae | -4.35825 | -55.02484 | 2024-10-25 16:52:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 4ae7fbd7-f3b1-3e95-8b5e-aaeb94d6f887 | -4.29474 | -55.11717 | 2024-10-25 16:52:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 105802d4-fa64-3546-9508-fb8b507d76b7 | -4.05407 | -54.51549 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5f9de53b-4235-3e44-a5e7-41c6aaba0ed7 | -4.03589 | -54.54471 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 9356b1cf-1945-3b53-a226-6b8d3b7ac44d | -4.0327 | -54.61927 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 5c7213f4-f2e4-3e15-b215-ae0291ccef03 | -4.03204 | -54.61497 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f162c9f7-5f5e-3daf-aaff-b7a849bec0dd | -4.03198 | -54.62038 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6985a8ff-4cb6-3594-b54d-15f7004b58c9 | -4.03135 | -54.61607 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 56f974e3-2aaa-34bd-aed9-7c72d5e71af3 | -4.03072 | -54.61176 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5e8ee672-2673-3b95-a28f-a83e6b26939e | -4.02836 | -54.61551 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 30e055f6-155d-35d0-a45e-10372e270e82 | -4.02703 | -54.61232 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e77e2466-1de6-36a8-8f05-229b2177db75 | -3.96046 | -54.66574 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 58c645ab-daef-3fbc-b035-bc51c0b3de5b | -3.9301 | -54.53714 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c88e60fa-1fcf-323d-a315-4ce09c2e4009 | -3.81298 | -54.80112 | 2024-10-25 16:52:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 642dca49-fe1d-3477-a3b2-20bc713e0ab8 | -3.78542 | -54.64413 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 4f76da48-d038-3f0c-a652-20b150fe4599 | -3.67987 | -54.21433 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3e98ea5c-b261-3a2e-aff2-4250dec68465 | -6.28507 | -55.77947 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5b806e67-d1a8-32eb-a640-05d1b6fe036e | -7.7973 | -55.36195 | 2024-10-25 16:52:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| e95ccc60-ef8e-3866-a577-c6f591d0e975 | -7.79678 | -55.35833 | 2024-10-25 16:52:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 298ed895-1476-3bc2-a237-029c79d50e15 | -7.79324 | -55.36251 | 2024-10-25 16:52:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 9b8786b5-b5e3-381e-b128-d61fabf5b688 | -6.87668 | -55.58274 | 2024-10-25 16:52:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| bf29bf72-57f5-309d-a364-157be3ab3ff5 | -6.87651 | -55.58353 | 2024-10-25 16:52:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 15be1b4f-99b9-3d6f-95c2-f1a534fda125 | -6.87597 | -55.57991 | 2024-10-25 16:52:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7c92f7c7-c63a-34d0-a6cb-8e131060cfde | -9.93271 | -55.48399 | 2024-10-25 16:52:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dd76e09c-42d2-3284-b141-e46cc3868b22 | -10.71826 | -56.24175 | 2024-10-25 16:52:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 710085d6-5301-3191-9a4a-ab9e4507ac90 | -10.68666 | -56.34918 | 2024-10-25 16:52:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8e5f9a77-cb4e-3bd7-82bb-ff2b1431453c | -10.68212 | -56.34978 | 2024-10-25 16:52:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7bef04fd-562d-3ef8-991b-15d2807ca635 | -10.62348 | -55.90714 | 2024-10-25 16:52:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 269d002d-71e0-364e-838d-59b479912a79 | -10.37963 | -55.46997 | 2024-10-25 16:52:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d4160119-a0a8-3134-8f77-0cbdb6b54758 | -10.34709 | -55.42153 | 2024-10-25 16:52:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 72bd8e7f-9855-3a32-8888-8568ffe75d3f | -10.1055 | -55.38898 | 2024-10-25 16:52:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 04f01ed2-3a02-338d-8c69-2e568779d615 | -10.09346 | -55.17455 | 2024-10-25 16:52:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 14b7106f-eece-3f91-9a39-3a70827174c1 | -2.60875 | -49.62764 | 2024-10-25 16:52:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| dac3f365-5363-3e41-9816-cfa0738588ba | -4.57322 | -38.65072 | 2024-10-25 16:52:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 46218d87-d481-3255-a891-146b736658a5 | -7.07398 | -38.07545 | 2024-10-25 16:52:00 | NOAA-21 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 49.0 |
| 9851f3eb-1cc1-342f-ad45-38d9865c9472 | -7.04246 | -40.37929 | 2024-10-25 16:52:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| bb86edd5-1384-3129-b57f-55e627769b27 | -7.01474 | -40.45038 | 2024-10-25 16:52:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| f2eed5d2-a8f6-3149-83e8-608c701e7796 | -4.52148 | -40.73249 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 104.9 |
| e67a6bcd-8976-3f0f-ac06-8c8f22ede3d0 | -4.52083 | -40.74086 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 186.0 |
| 96625038-8467-3284-9f27-84be14106dec | -4.52015 | -40.73682 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 186.0 |
| 022a9687-2eea-3e64-a4f8-fe25dd753c1d | -7.61356 | -36.93775 | 2024-10-25 16:52:00 | NOAA-21 | SUMÉ | PARAÍBA | Brasil | 2516300 | 25 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 9f784ce7-2620-3952-b7c1-2fcfb8ef2115 | -7.56278 | -37.3522 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 24.9 |
| 48b87fc6-eb13-3d40-b765-9ae8b23889e5 | -7.56008 | -37.35593 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 65.9 |
| 362db4c9-6215-36d6-9514-2dd48b5b50f6 | -7.55613 | -37.35363 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 24.9 |
| 4c862f1b-4f4a-3231-b4c6-79d776895225 | -7.2866 | -37.40782 | 2024-10-25 16:52:00 | NOAA-21 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 694b9800-0c52-3bfc-80fa-4d2f256e28a9 | -4.8901 | -38.4343 | 2024-10-25 16:52:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |


[Clique aqui para ver as próximas entradas](README159.md)
