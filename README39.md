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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b89b391-3772-3155-b3da-77174e7e0e42 | -19.77122 | -42.0053 | 2024-10-08 03:45:00 | NOAA-20 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| adfc8242-d7d3-3769-9df2-c47912fe9d70 | -20.21619 | -42.89743 | 2024-10-08 03:45:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 33aed0ea-d593-3d41-8c3a-03a8e5567c5c | -20.21529 | -42.90233 | 2024-10-08 03:45:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ea9d67a1-5885-3011-8255-7668eacc6ced | -19.9819 | -42.45102 | 2024-10-08 03:45:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0463996c-065f-36b9-ba0d-3b7434379b12 | -19.97728 | -42.45506 | 2024-10-08 03:45:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e251aafd-744d-3181-8c9a-88692df170a2 | -22.19226 | -42.98125 | 2024-10-08 03:45:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 728a8285-e155-3774-bdd3-edf25ef63d79 | -22.1792 | -42.4684 | 2024-10-08 03:45:00 | NOAA-20 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 92d4cb3a-3b67-3250-a451-37029a256d01 | -21.97768 | -42.41739 | 2024-10-08 03:45:00 | NOAA-20 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7cf23a7b-6981-32e2-ba12-f94ee38b9d01 | -21.97606 | -42.42651 | 2024-10-08 03:45:00 | NOAA-20 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| ee0b7f75-92a9-35c9-be92-5f862d849c77 | -21.97045 | -42.41558 | 2024-10-08 03:45:00 | NOAA-20 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9826f763-1a3b-3489-bc5d-f13bfaa784f8 | -21.86121 | -43.38118 | 2024-10-08 03:45:00 | NOAA-20 | MATIAS BARBOSA | MINAS GERAIS | Brasil | 3140803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ca5ad2b7-546b-33e3-8b1f-951492b2f2a0 | -21.79831 | -42.51307 | 2024-10-08 03:45:00 | NOAA-20 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7bc42996-7f09-3e48-97d1-3ce9befa8d27 | -21.71049 | -43.49644 | 2024-10-08 03:45:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f5e752e2-c1c6-3ebf-97d2-da08de578e86 | -21.55604 | -42.3355 | 2024-10-08 03:45:00 | NOAA-20 | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c686a9ea-9bac-3de8-ba64-abc605029588 | -21.55291 | -42.3531 | 2024-10-08 03:45:00 | NOAA-20 | RECREIO | MINAS GERAIS | Brasil | 3154101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4a2ea36b-e7ca-3ff8-b789-d1ea12523b5d | -21.5524 | -42.33472 | 2024-10-08 03:45:00 | NOAA-20 | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c957a9a6-db14-3a6b-94db-b2cdb0434db9 | -21.54798 | -42.33832 | 2024-10-08 03:45:00 | NOAA-20 | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| af57765c-5280-38e3-905c-05d121f98076 | -21.54721 | -42.34261 | 2024-10-08 03:45:00 | NOAA-20 | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6305e0cd-9c3a-3dfc-9649-fc4ef16afb53 | -21.54431 | -42.33768 | 2024-10-08 03:45:00 | NOAA-20 | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 05c0ff30-cc68-3adc-8064-94330664369f | -21.54353 | -42.34203 | 2024-10-08 03:45:00 | NOAA-20 | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 58fdca21-50f3-3443-b71c-22de3ac5d3f2 | -21.16233 | -42.20257 | 2024-10-08 03:45:00 | NOAA-20 | PATROCÍNIO DO MURIAÉ | MINAS GERAIS | Brasil | 3148202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0475412e-098c-31d3-b9da-31ce3c61d395 | -21.06549 | -42.70564 | 2024-10-08 03:45:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0e42c345-5f7f-3efa-aa13-2aae0740cf3d | -21.06541 | -42.70786 | 2024-10-08 03:45:00 | NOAA-20 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ad34528e-5682-3a7f-80b7-fbd1a3333bd9 | -21.00573 | -43.05989 | 2024-10-08 03:45:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 74efdaac-39e3-305a-93db-fb0bd1ef4c9c | -21.00452 | -43.05618 | 2024-10-08 03:45:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 6d151320-253f-3470-bc6f-2b12aa4c90f4 | -21.00193 | -43.05902 | 2024-10-08 03:45:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f3c08ebe-8520-3846-b167-4693eeea87dc | -21.00072 | -43.05532 | 2024-10-08 03:45:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 02735cf8-7d14-3eb5-90d3-75edf9b32fe5 | -20.99998 | -43.04788 | 2024-10-08 03:45:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d482e251-389d-39e5-a3ed-182b9708f752 | -20.99976 | -43.06046 | 2024-10-08 03:45:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d806a175-50b0-3fa6-9b1c-b3a495a99741 | -20.99905 | -43.053 | 2024-10-08 03:45:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 529df02f-f95c-3140-9467-8688c70f7bb6 | -20.99812 | -43.05815 | 2024-10-08 03:45:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 7fae95b6-279f-37b5-825e-5fb00704c9b4 | -20.99788 | -43.04934 | 2024-10-08 03:45:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 37b28f76-9c46-3347-a0cf-93a3ce04f690 | -20.99692 | -43.05447 | 2024-10-08 03:45:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 35149175-3997-3491-8298-012c9361321c | -20.99525 | -43.05216 | 2024-10-08 03:45:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 26340842-2072-3329-b1bc-4fa40b19d02e | -22.89979 | -43.7534 | 2024-10-08 03:45:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f0f9bd8e-e578-3c38-877e-cd957297e4f4 | -22.87615 | -43.60326 | 2024-10-08 03:45:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 63afa3da-d04c-3539-a4be-c3351246eefb | -22.85493 | -42.97967 | 2024-10-08 03:45:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 05fd266e-5e92-39f8-9053-cfedfca198ad | -16.48813 | -43.81737 | 2024-10-08 03:45:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df026c9c-95cd-365b-9f52-c0a5fb1404ad | -16.34769 | -43.69901 | 2024-10-08 03:45:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb255156-f996-33af-9879-fbb0e65b7962 | -16.37585 | -43.19619 | 2024-10-08 03:45:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30da0521-9c04-3af3-8419-ed2b4e0d63e3 | -17.65377 | -43.89373 | 2024-10-08 03:45:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 628fa679-cbb4-3ca6-86ad-e4234560f937 | -17.58335 | -43.73463 | 2024-10-08 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c842222-8714-3fc9-86b8-1fceed726f61 | -16.67965 | -43.88591 | 2024-10-08 03:45:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df2a0f63-c0fd-3f1c-82ac-137524cffbd2 | -17.57585 | -43.7047 | 2024-10-08 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5ab9cd7-6e6b-3a09-93f5-3f92eb59a67f | -17.09459 | -43.80638 | 2024-10-08 03:45:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0331eeb-6cb9-32d6-85bb-14cb9ef1fc05 | -19.4514 | -44.11831 | 2024-10-08 03:45:00 | NOAA-20 | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e1e19de-4287-3e18-bcfa-249caca5fbe9 | -19.45064 | -44.12229 | 2024-10-08 03:45:00 | NOAA-20 | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58051a57-d949-3608-aa71-b145abfaa231 | -19.25138 | -44.36345 | 2024-10-08 03:45:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d24cdaa0-50f3-3adc-ab6f-f150b5cb4afc | -19.25051 | -44.36789 | 2024-10-08 03:45:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6fb25ab-ca15-368f-8457-433debafebe1 | -19.17433 | -43.31358 | 2024-10-08 03:45:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5134cdd9-126d-32ee-a6b1-98a86f40c77a | -20.40699 | -43.94495 | 2024-10-08 03:45:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 89458a6a-eb3b-315a-b0de-e0b0db4b0781 | -20.40619 | -43.9491 | 2024-10-08 03:45:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 73c11ef7-37d8-3643-ac44-4d309feedd2b | -20.40416 | -43.94076 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| 54a14441-c196-345b-b749-36410dd5fdef | -20.40378 | -43.93972 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.4 |
| e128c22a-2846-388d-b962-d7436a7513b7 | -20.40338 | -43.94503 | 2024-10-08 03:45:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| 38a6af6f-6d23-3202-86cb-57550aa533e0 | -20.40296 | -43.944 | 2024-10-08 03:45:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.4 |
| 47eb2c24-d21d-31ff-967c-27b928204eb0 | -20.4026 | -43.94921 | 2024-10-08 03:45:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.6 |
| 6049e62a-a6ba-3d7d-9dbf-03f2fb80bf61 | -20.40214 | -43.9482 | 2024-10-08 03:45:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| be1e9adc-dafe-3c01-a3d1-c386cf813644 | -20.40185 | -43.95327 | 2024-10-08 03:45:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.6 |
| 97e79876-248a-3f29-8d8b-134d3ba010b9 | -20.40136 | -43.95226 | 2024-10-08 03:45:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| f603a23f-93db-3fa7-8a6a-d9154425716e | -20.40096 | -43.93527 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e3fa4a3c-36a8-354f-bb68-3980c290680a | -20.4001 | -43.93992 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| 35e3d76e-2472-3dc0-b619-90b05294cb57 | -20.39973 | -43.93886 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.4 |
| 0bb41047-a95b-38e7-b2bc-5d71956e3364 | -20.3993 | -43.94427 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| a1cd909d-33f4-3c94-bc74-084c2ad05dfc | -20.39888 | -43.94325 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.4 |
| 6fb0b828-3c58-3b6c-9669-fddec617c813 | -20.39853 | -43.94842 | 2024-10-08 03:45:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.6 |
| 9939b805-53e2-32df-b75d-9f924647ac79 | -20.39807 | -43.94744 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| f13fc2f1-ac90-35ca-a7b0-8d8480da4004 | -20.3978 | -43.95236 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.6 |
| 950050ac-9edd-382c-9818-5f720fa440cf | -20.39731 | -43.95139 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| 8e56e4e8-f8ff-381a-a568-dcc1842233df | -20.39605 | -43.93905 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 1e60ea6c-7334-3439-8f4d-4fae0ad72fc5 | -20.39525 | -43.94339 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| e7f2d915-94af-3c4d-b481-055c12f9eaf0 | -20.39448 | -43.94754 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 45e748ee-8f5b-3b06-a0d7-c85b46813944 | -20.39208 | -43.93772 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| b3585415-3279-34dc-8e06-e380ff4d5896 | -20.39127 | -43.9421 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 2da3f2c6-438d-3bc5-9fbd-a70a45f2ea2e | -20.91452 | -43.7496 | 2024-10-08 03:45:00 | NOAA-20 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7d866382-1958-3bcb-9291-cbe7bfb9d109 | -20.90084 | -43.82182 | 2024-10-08 03:45:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 44885eeb-8266-3861-a678-3539e8f39171 | -20.8032 | -44.51241 | 2024-10-08 03:45:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 45815b46-a449-3c51-8a3b-a9d272d049a3 | -20.79904 | -44.51151 | 2024-10-08 03:45:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ce049223-a24a-3dc0-ae56-004a643ab320 | -20.45074 | -43.80431 | 2024-10-08 03:45:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8708b5cb-b02e-332e-9449-aed6a1eaf4b4 | -19.78388 | -44.29659 | 2024-10-08 03:45:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69d6801e-ab20-3f34-a474-1a3e8fd1ca69 | -20.37119 | -43.95924 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 96a92dfe-96e3-3a20-94a2-0de238c7135a | -20.36473 | -43.94866 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 194a0c2b-8e33-312b-b6d5-ff4307c86a26 | -20.23202 | -44.44141 | 2024-10-08 03:45:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b70061f2-5d14-3181-a737-752f54036092 | -20.23127 | -44.44525 | 2024-10-08 03:45:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8af0ba31-537b-390c-b26c-68c7f5db9330 | -20.22779 | -44.44069 | 2024-10-08 03:45:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e1973074-6d15-3182-bb99-9e1cdec5197b | -20.39047 | -43.9464 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 7c1b3157-f546-3bb6-a197-34ff7f4b7fa7 | -20.3897 | -43.95055 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 3c2376bf-bf22-356c-b6f8-d4ac7236648e | -20.38894 | -43.95461 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| adb9bc98-9d7c-388d-97a9-70034dd2a22b | -20.38822 | -43.95847 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 83663488-78d4-3e52-b0ab-d8f13c0352a0 | -20.38729 | -43.94079 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 80d4105f-5fb9-3b1e-bcb9-c1c2347669a4 | -20.38648 | -43.87764 | 2024-10-08 03:45:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8f64e7f1-282c-3f2c-a7a8-23ed82d6ebb6 | -20.38647 | -43.94525 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a436f6c5-4523-3312-88fc-121f7b4fecfc | -20.38567 | -43.94952 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ed06eae8-e577-3b88-a653-7bae40042bdf | -20.3849 | -43.95366 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2ceae108-d1ac-36b7-a1ea-c7eff917bbd8 | -20.38416 | -43.95763 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 33886eae-315f-3621-ae9d-d86509e5a7d4 | -20.38244 | -43.94424 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 66983e2e-1992-3f47-a6e8-6cc791d24192 | -20.38164 | -43.94852 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6689fea5-f45d-3ca2-909e-3ea3a5d995c9 | -20.38088 | -43.95258 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 18958634-d249-3fa7-87e3-9acdbce380cd | -20.38012 | -43.95668 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3ac711f2-2e46-3b5d-bf94-e8dc86452da0 | -20.37934 | -43.96083 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |


[Clique aqui para ver as próximas entradas](README40.md)
