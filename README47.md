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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26cfb046-2a70-369f-a6e2-309b57f3f41c | -10.09308 | -68.38454 | 2024-10-31 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3187fbdf-fd8b-3d64-815d-089cb76e965a | -10.05453 | -68.53339 | 2024-10-31 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3bf719a-580a-385f-9c42-0339848f201a | -10.63586 | -69.01734 | 2024-10-31 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0497e21b-cbee-352d-97fd-ef349389118a | -10.6352 | -69.02135 | 2024-10-31 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45ce8b5e-e32c-3dd4-90c7-0e4d2b86f2b9 | -11.10814 | -68.68702 | 2024-10-31 05:44:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fd73eb6-cfcf-36c5-bfbf-821e5356c6ec | -10.9389 | -68.3685 | 2024-10-31 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ca92bc2-55fa-3048-b2e5-fd42ddbe2e63 | -10.90022 | -68.32683 | 2024-10-31 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25f97978-b537-3c98-8389-bb7fb7dc1b93 | -10.95041 | -69.18024 | 2024-10-31 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83ba82c6-9d28-3f71-a96c-3ceaa7874f88 | -10.94822 | -69.17142 | 2024-10-31 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afca85b0-1479-3442-872e-29b5f69571f9 | -10.91881 | -69.21683 | 2024-10-31 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f4f7791-9113-3955-b758-fe6e2ecf2d2f | -10.79798 | -69.04725 | 2024-10-31 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfba1669-8353-3270-a545-7d0bea2d39bb | -9.30894 | -62.40646 | 2024-10-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d415cef5-33f2-3e7f-b754-a3617820fb14 | -9.1459 | -61.3849 | 2024-10-31 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d46aa5fb-265b-3e1a-b5ee-b91e3981fefa | -9.14351 | -61.38127 | 2024-10-31 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76bf3415-4eec-3652-a399-e29474aa390c | -9.14282 | -61.38622 | 2024-10-31 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a82ffcd-88b5-3f97-90e1-fad1a5b63c2b | -9.14202 | -61.38434 | 2024-10-31 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac94fa45-4464-32e1-adcc-adf5fdd33b62 | -11.84277 | -62.09362 | 2024-10-31 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e95b86d-8d26-3794-9d78-43a513a706b2 | -12.53518 | -63.30568 | 2024-10-31 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0af48e58-22ab-3af7-aa20-6fd897348b12 | -12.53456 | -63.30999 | 2024-10-31 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29b2c9fd-6936-3c5f-9efc-203164e78333 | -12.43422 | -63.27941 | 2024-10-31 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| c08edfdb-0a2c-39b8-a245-d4439912d59c | -12.4336 | -63.28371 | 2024-10-31 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| be938b79-e72a-3bf3-a137-c229216dab9c | -12.43059 | -63.27886 | 2024-10-31 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| bd23c967-19e1-3a18-b694-77f92c2dec29 | -12.42997 | -63.28316 | 2024-10-31 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 76df76d0-3bbc-30a5-9744-93a2d877d153 | -12.42696 | -63.27832 | 2024-10-31 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b323e161-ce12-39cc-b8ad-1dcbf566e7db | -12.42633 | -63.28262 | 2024-10-31 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 570e5faf-1507-3aa5-8c8a-a8228123f24f | -12.42395 | -63.27346 | 2024-10-31 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8c7b469a-e6b9-3466-b4d6-371789d425a5 | -12.42332 | -63.27777 | 2024-10-31 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1cb84a8c-0675-3f0b-bffa-150d9b5460ef | -12.4227 | -63.28207 | 2024-10-31 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 45698938-b8ef-353f-bde0-469ec741a5d1 | -12.41969 | -63.27722 | 2024-10-31 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65704626-ef08-3eb7-8df0-ca25985b9c8a | -12.41606 | -63.27668 | 2024-10-31 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a41c7e3-49d1-36cf-ba51-56176283c3ec | -7.65944 | -63.45098 | 2024-10-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29107ff0-dce4-3967-8447-db4e0446b6cd | -7.65888 | -63.45475 | 2024-10-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 651153f5-0c8d-3ba0-b2f6-6aba623af475 | -7.4778 | -63.49397 | 2024-10-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adf091d1-ab2f-32e8-91af-1bf5c58738b8 | -7.47666 | -63.50145 | 2024-10-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d9fe8a6-a1d1-3c8b-99f8-7cafcc43b30b | -7.47494 | -63.4897 | 2024-10-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b5e6a85-ac20-3d6d-9bf7-aa39f507a8ee | -7.47437 | -63.49345 | 2024-10-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6021b00-0f70-3c77-85d2-bdb790db30c4 | -7.4738 | -63.4972 | 2024-10-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94159865-680d-3dda-9350-d55d2b625964 | -7.47324 | -63.50092 | 2024-10-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cde8d2b-02a3-346c-8517-fa152bd45608 | -7.47038 | -63.49667 | 2024-10-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42c9ae0c-6726-36bf-a2fa-142f3f259727 | -7.46982 | -63.5004 | 2024-10-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebefb152-5fcc-3711-8976-61236f98668b | -8.86861 | -63.54324 | 2024-10-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f022619-6639-39f8-a45e-9ab196784647 | -8.84962 | -64.16368 | 2024-10-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44c27f9c-a0d3-36ee-bde9-4957d59de836 | -7.93277 | -63.66068 | 2024-10-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d8537f5-77d9-3d39-9b3c-d06f30107a66 | -7.92992 | -63.65643 | 2024-10-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5aa681cc-a17a-3973-8b6c-349e2e7bf2e7 | -7.90139 | -63.61389 | 2024-10-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a39f2366-e076-3701-b3d0-a175cca4ce57 | -7.88845 | -63.72235 | 2024-10-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7258ce7-3f7c-3089-a4c5-cd11cd76ac21 | -7.88673 | -63.71069 | 2024-10-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8923c546-1fd0-3f0a-b5a0-344674dd96ed | -10.14699 | -63.70921 | 2024-10-31 05:44:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38c0d6af-3db0-30cd-95b2-e607bceb5fbb | -9.62732 | -63.25963 | 2024-10-31 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab330d36-393d-395a-b26c-a2e4ce6f99dc | -9.62731 | -63.25691 | 2024-10-31 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4f2229d-78ac-3c15-8490-753bfb28c744 | -9.56206 | -63.13591 | 2024-10-31 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26836ce1-8a71-3709-89c4-922f559885e1 | -9.5591 | -63.13129 | 2024-10-31 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61b3941c-327a-3ae0-b14f-52e24ee489dd | -9.55851 | -63.13536 | 2024-10-31 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed58750f-9fce-3d5a-b52e-c532af862013 | -9.55558 | -63.25425 | 2024-10-31 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55b6dd97-a0f0-3f2d-80ae-15cbcd09521d | -9.55556 | -63.13075 | 2024-10-31 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efd57fca-c132-3a64-8cd2-732d0f375dcb | -9.55497 | -63.13481 | 2024-10-31 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f5af9fd-17f6-3967-b5b0-2e2f441d67b2 | -9.8683 | -63.98143 | 2024-10-31 05:44:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 778e2eda-cbd2-33f6-bc0d-69743840234f | -9.86487 | -63.9809 | 2024-10-31 05:44:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9438b03-2d5d-3268-a566-31c766f1d057 | -9.52294 | -63.45177 | 2024-10-31 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 330bd040-5f15-3bd1-995c-f5128012044c | -9.51945 | -63.45126 | 2024-10-31 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4985b4c2-6e41-35d8-9a3d-b7c008195298 | -9.31981 | -64.25014 | 2024-10-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6149eb93-7bb6-31a9-9279-c6e63fd116c0 | -9.31926 | -64.2538 | 2024-10-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 324b20fa-1213-30cf-a6fe-0fb52cc5bcbf | -9.30176 | -64.25487 | 2024-10-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d8ebc30-2e9d-3a3e-bcf9-3c61692950e1 | -12.22654 | -64.20898 | 2024-10-31 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a6651249-e6e6-3d5f-91a8-bfdd4049395e | -12.22307 | -64.20846 | 2024-10-31 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c9c45b9a-9354-3d59-b562-1fda6ba41b44 | -11.97896 | -64.04162 | 2024-10-31 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df67a678-7d25-3a01-b753-b240be0b1b59 | -11.97313 | -63.98419 | 2024-10-31 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 615c4277-8be5-3f13-9bed-ab6472c798ed | -11.97254 | -63.98816 | 2024-10-31 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b77659a6-d91d-3892-abd1-ebf8b7f048af | -11.96963 | -63.98366 | 2024-10-31 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e23811d3-785f-305f-b2de-d22ca3b9f0a4 | -11.96905 | -63.98763 | 2024-10-31 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3450c40-56af-3ec3-9b89-e6b9aad7b142 | -12.35666 | -64.32826 | 2024-10-31 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ae7a9d4-3199-3e3c-b1ac-53f815195b14 | -12.26088 | -64.43186 | 2024-10-31 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| caa7fd11-7711-3120-9461-90965402fcdd | -7.28023 | -64.6544 | 2024-10-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b84eb4d-0905-3fb1-8419-9edcb24e4e9b | -9.30861 | -64.27843 | 2024-10-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a92fed0-6754-3b56-b46a-f804d6747ec3 | -8.11043 | -64.11185 | 2024-10-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df65416e-d98d-3f5b-af07-fdccfbec8758 | -8.10706 | -64.11134 | 2024-10-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a9b5cd9-e443-3afb-9630-295080041afd | -10.69017 | -65.00103 | 2024-10-31 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c47f61cd-03be-3b94-a789-aae7b271a9e6 | -10.6879 | -64.99333 | 2024-10-31 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5d9071f0-7357-3f04-97af-09584145e85a | -10.68736 | -64.99692 | 2024-10-31 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 37fec0a1-7f28-3f9b-8567-622630be3922 | -10.68682 | -65.0005 | 2024-10-31 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 338f6d1c-f101-325e-8346-5cb826f8b3bf | -10.68455 | -64.9928 | 2024-10-31 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c3f3b4f3-5385-3418-a30b-86adbe5eabfa | -10.68401 | -64.99639 | 2024-10-31 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5b536178-c962-307d-be71-1b2806d8ac2f | -10.6812 | -64.99227 | 2024-10-31 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 694f5b0f-7aea-30d0-b559-b9d89395facd | -10.06725 | -65.18908 | 2024-10-31 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5351d24c-8d98-3d47-9232-cad823e91b45 | -9.87702 | -64.69588 | 2024-10-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2d53e630-3dcc-3778-b06d-684948e90c1e | -9.87366 | -64.69536 | 2024-10-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 900be99c-9668-30cd-a7d7-4a6dd4c2ba22 | -9.70358 | -64.60999 | 2024-10-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b44cf9bd-69d9-3093-958b-4b4255fa3718 | -9.70303 | -64.6136 | 2024-10-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f11c17fb-b33c-3b36-a0bc-aface040b0e0 | -9.70076 | -64.60583 | 2024-10-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a79a577-1dab-30a5-b188-d6e041b0a634 | -9.64878 | -65.74084 | 2024-10-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6c25ab2-1232-3fcb-b66e-879a4499e84a | -9.54576 | -64.44475 | 2024-10-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4635cfb6-a894-3ba0-a3d1-8372664b3b67 | -9.54405 | -64.4333 | 2024-10-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60560535-fce0-33c0-9269-01603df1d5f4 | -9.54349 | -64.43695 | 2024-10-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb200485-0339-3330-bcc5-3eda79157e67 | -9.54238 | -64.44423 | 2024-10-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9948faaf-88bd-3640-8b88-d4c79ce647df | -9.45964 | -64.69393 | 2024-10-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bed4ace6-e331-3592-8618-c0965325fb79 | -9.33081 | -65.68662 | 2024-10-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79a8df50-0ac0-3b05-9c09-b4e73a01996d | -9.14274 | -68.86855 | 2024-10-31 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4512471c-3919-3410-9616-03dab2a0a6c1 | -9.00498 | -69.09019 | 2024-10-31 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fda118f-ccbc-3a02-a27f-6fec857e21d0 | -8.68188 | -70.12353 | 2024-10-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84cccb63-4b51-35e1-b4d9-bfb2f389f1db | -8.64344 | -70.12853 | 2024-10-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README48.md)
