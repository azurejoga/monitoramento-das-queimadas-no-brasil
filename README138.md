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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17baf90c-3cb2-3cc4-9520-ddf1274210d0 | -11.73968 | -40.2375 | 2024-10-25 16:50:00 | NOAA-21 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 20.1 |
| b98d90b5-e447-3c3d-8698-2cfa2ae950d2 | -11.73133 | -40.19323 | 2024-10-25 16:50:00 | NOAA-21 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 7f66123e-d165-3d1d-9ff0-4aa851133375 | -13.2791 | -40.72881 | 2024-10-25 16:50:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 069c23ed-595e-3be8-be21-72c14ff3e372 | -14.71269 | -41.9215 | 2024-10-25 16:50:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 230d2640-563d-3251-82eb-017ff04606da | -14.7122 | -41.92248 | 2024-10-25 16:50:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 19.7 |
| bbdd97ba-332a-389b-9b42-9c0c3f02335e | -8.68914 | -36.00467 | 2024-10-25 16:50:00 | NOAA-21 | PANELAS | PERNAMBUCO | Brasil | 2610202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| a3c7ab67-cffd-38f1-9bb1-b12877b74ed3 | -8.68498 | -36.00105 | 2024-10-25 16:50:00 | NOAA-21 | PANELAS | PERNAMBUCO | Brasil | 2610202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 1e7c5f74-b387-3978-b48e-44d3993e5625 | -8.62693 | -36.15975 | 2024-10-25 16:50:00 | NOAA-21 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 7444b0a0-2e36-326e-85c6-4ced464b5ec7 | -7.61453 | -36.93939 | 2024-10-25 16:50:00 | NOAA-21 | SUMÉ | PARAÍBA | Brasil | 2516300 | 25 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c393a8d7-895d-30a3-adcf-e837fa3ea565 | -9.29267 | -36.71582 | 2024-10-25 16:50:00 | NOAA-21 | ESTRELA DE ALAGOAS | ALAGOAS | Brasil | 2702553 | 27 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 335a7d3b-87e5-3b5d-81bd-f7046f008b1d | -9.2909 | -36.71762 | 2024-10-25 16:50:00 | NOAA-21 | ESTRELA DE ALAGOAS | ALAGOAS | Brasil | 2702553 | 27 | 33 | nan | nan | nan | Caatinga | 5.3 |
| e84de5ab-742f-33f4-9ef1-154c85271152 | -8.92724 | -36.96779 | 2024-10-25 16:50:00 | NOAA-21 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 8.6 |
| e2d5790d-573d-3e94-8391-64f773c7734b | -8.24882 | -36.6406 | 2024-10-25 16:50:00 | NOAA-21 | POÇÃO | PERNAMBUCO | Brasil | 2611200 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e6f988cc-5c07-3ee6-aa6e-73a0f1584a08 | -8.90345 | -36.48428 | 2024-10-25 16:50:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 0c4e4701-2a7a-3986-96e4-ac4731471f3d | -9.60991 | -36.89828 | 2024-10-25 16:50:00 | NOAA-21 | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | 5.8 |
| cb250b37-f918-34f8-a1ab-f7c58f2d8883 | -10.55323 | -37.99693 | 2024-10-25 16:50:00 | NOAA-21 | ADUSTINA | BAHIA | Brasil | 2900355 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 07f2bdbc-fd9b-3516-8249-31187a35a279 | -10.64465 | -37.12604 | 2024-10-25 16:50:00 | NOAA-21 | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| 208e6599-6cc9-3d5e-a2f3-1ba1ab9fa5c0 | -10.6436 | -37.12298 | 2024-10-25 16:50:00 | NOAA-21 | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 34.9 |
| 3ef3f02a-fc24-32d3-947e-fd64b2c69b7a | -10.64352 | -37.12045 | 2024-10-25 16:50:00 | NOAA-21 | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 32.3 |
| fd7385b0-4041-3d6c-8dc9-dc9b20460fb8 | -11.46229 | -38.26226 | 2024-10-25 16:50:00 | NOAA-21 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 14a3c6a9-d336-36bf-aa1d-b6470fbf42c8 | -11.88158 | -38.16535 | 2024-10-25 16:50:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| ec8be261-551b-3917-a364-9dda4e97dc79 | -11.69596 | -37.54815 | 2024-10-25 16:50:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| a5b63ad4-c16d-3f93-bed0-c9a2c008b80e | -11.69532 | -37.55001 | 2024-10-25 16:50:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c0c816ec-cce7-35f9-a558-c98bb28eec78 | -11.69078 | -37.55437 | 2024-10-25 16:50:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 7ce227d0-4e98-3b74-be1e-313c16f4083b | -11.69018 | -37.55624 | 2024-10-25 16:50:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 3fe47d93-af54-3095-951c-c4938c3ecaf4 | -11.25043 | -37.67176 | 2024-10-25 16:50:00 | NOAA-21 | ITABAIANINHA | SERGIPE | Brasil | 2803005 | 28 | 33 | nan | nan | nan | Mata Atlântica | 35.0 |
| a2062fa1-7ec0-369e-955f-24cf4db689e1 | -11.13638 | -37.4248 | 2024-10-25 16:50:00 | NOAA-21 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 70d251d0-f878-3f4d-9d99-989b399271f7 | -11.13275 | -37.42365 | 2024-10-25 16:50:00 | NOAA-21 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 0e745be2-b9d3-3595-90a8-84dc0b3cbcc4 | -11.10512 | -37.36749 | 2024-10-25 16:50:00 | NOAA-21 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 19602d28-7cc0-3aee-881c-598236617565 | -15.57163 | -39.00246 | 2024-10-25 16:50:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 167350eb-d2b4-3766-9ae0-08074dbc2dfc | -15.57104 | -39.00327 | 2024-10-25 16:50:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 78f831a0-efc2-3717-8a65-6707c32477ce | -7.98433 | -38.06682 | 2024-10-25 16:50:00 | NOAA-21 | CALUMBI | PERNAMBUCO | Brasil | 2603405 | 26 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 303e2316-0572-3e6b-b912-9fa6c790785a | -8.81908 | -38.36834 | 2024-10-25 16:50:00 | NOAA-21 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8365a51d-a94f-3bf8-81c9-1e92b3b258b1 | -8.81818 | -38.36359 | 2024-10-25 16:50:00 | NOAA-21 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| dcb3a43b-306b-3a4b-985b-55b59f4a08ed | -8.65344 | -39.24817 | 2024-10-25 16:50:00 | NOAA-21 | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 36b53794-b563-3364-8bb1-34b1013cd874 | -8.17694 | -38.19107 | 2024-10-25 16:50:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 7d80ec4e-c4d5-35e6-824e-d47af02e9664 | -8.17599 | -38.18609 | 2024-10-25 16:50:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 58e9ccee-b873-31ec-8ffb-fb44a6179f1b | -8.1739 | -38.19212 | 2024-10-25 16:50:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 38db82c3-a5c0-388f-963c-bbf7a5673ef4 | -8.17298 | -38.18715 | 2024-10-25 16:50:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 9.9 |
| e990470c-3795-3dc6-b86c-1f730081e42d | -9.97622 | -38.56539 | 2024-10-25 16:50:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 662b7ca7-2166-337a-8a8f-596950cb1dae | -9.97315 | -38.56733 | 2024-10-25 16:50:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 885d55cc-ae0a-313d-b89d-926253d811c5 | -10.31064 | -38.51133 | 2024-10-25 16:50:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 6314d0c1-421c-382a-a832-c3850e1c6afb | -10.30573 | -39.32215 | 2024-10-25 16:50:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 54939cee-11c5-328e-bf17-937e1fbf888f | -10.30296 | -39.32121 | 2024-10-25 16:50:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ea1d18a1-d653-3f7f-8dba-3f876c307216 | -10.08797 | -39.42069 | 2024-10-25 16:50:00 | NOAA-21 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| bec00cd9-c0c1-3fc2-aa3c-73b54ff78872 | -10.07974 | -39.21128 | 2024-10-25 16:50:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 66ee5942-3821-3912-b7f3-4a063b2f1aea | -10.07838 | -39.21146 | 2024-10-25 16:50:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| c65cb314-99ef-36f8-a023-9dfaf2e85302 | -11.89152 | -38.91854 | 2024-10-25 16:50:00 | NOAA-21 | LAMARÃO | BAHIA | Brasil | 2919108 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 41c1f108-d024-362c-8daf-347bd27cf794 | -11.32098 | -39.80057 | 2024-10-25 16:50:00 | NOAA-21 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 20.6 |
| be162e61-61a3-338a-8fe6-476954b64357 | -11.3203 | -39.79701 | 2024-10-25 16:50:00 | NOAA-21 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 20.6 |
| cb6fca87-4ded-3f86-af90-fd5f6c094e3e | -10.96364 | -39.68967 | 2024-10-25 16:50:00 | NOAA-21 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| bba323fe-9c14-3331-98f5-fe56f4bbf75d | -13.61514 | -40.45003 | 2024-10-25 16:50:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 26.2 |
| ac211323-0598-3d03-865c-09a9b144abee | -13.03726 | -40.15816 | 2024-10-25 16:50:00 | NOAA-21 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 77316974-d6a3-3157-94cd-6a22aba14f62 | -13.5913 | -39.31893 | 2024-10-25 16:50:00 | NOAA-21 | TAPEROÁ | BAHIA | Brasil | 2931202 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| d9cc73cc-8460-3015-9766-690930c096cc | -13.51188 | -40.17694 | 2024-10-25 16:50:00 | NOAA-21 | ITIRUÇU | BAHIA | Brasil | 2916906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0c7cb198-671e-3dd5-8220-5d0a7dccb85a | -13.51033 | -40.17672 | 2024-10-25 16:50:00 | NOAA-21 | ITIRUÇU | BAHIA | Brasil | 2916906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8e77bee1-887c-3b18-bd22-3ae7e5239c36 | -13.44349 | -40.2847 | 2024-10-25 16:50:00 | NOAA-21 | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| bdf1425d-b528-3e14-9af2-9c6455910c15 | -13.44289 | -40.28159 | 2024-10-25 16:50:00 | NOAA-21 | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| b4dbf948-27c8-3bb2-8d3c-689060dfea16 | -13.28004 | -40.11157 | 2024-10-25 16:50:00 | NOAA-21 | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 34b98a64-e018-34eb-8ab2-3c6c89e92d11 | -12.85241 | -38.92827 | 2024-10-25 16:50:00 | NOAA-21 | MARAGOGIPE | BAHIA | Brasil | 2920601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| cef1ce1e-66ef-3a84-9e9d-adf2f567529d | -12.85159 | -38.92961 | 2024-10-25 16:50:00 | NOAA-21 | MARAGOGIPE | BAHIA | Brasil | 2920601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| f53b8d7c-15a1-32f8-b789-80e409c0ae47 | -14.9814 | -40.48201 | 2024-10-25 16:50:00 | NOAA-21 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| e28aa1ce-6315-31fd-a0c2-460f1392597e | -14.9805 | -40.47725 | 2024-10-25 16:50:00 | NOAA-21 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| aed8250a-b4d0-3f8c-b812-898b50463017 | -14.97959 | -40.4805 | 2024-10-25 16:50:00 | NOAA-21 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.9 |
| 9ae80fde-75bd-3401-a5d1-91cd0dfbac95 | -14.93498 | -40.36973 | 2024-10-25 16:50:00 | NOAA-21 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| ec954cff-ff84-35cb-bc3d-b72d445d2c5c | -14.38402 | -39.618 | 2024-10-25 16:50:00 | NOAA-21 | AURELINO LEAL | BAHIA | Brasil | 2902401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| dcc6ee50-3486-3b90-ab84-a66f31b9ab97 | -14.38274 | -39.61787 | 2024-10-25 16:50:00 | NOAA-21 | AURELINO LEAL | BAHIA | Brasil | 2902401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| c70e2cde-1b20-3f61-9ec3-ed5dbda2c334 | -14.26694 | -39.60281 | 2024-10-25 16:50:00 | NOAA-21 | GONGOGI | BAHIA | Brasil | 2911501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 62a4161b-e12c-3a69-8a5e-160cbdaa4c87 | -14.26564 | -39.60165 | 2024-10-25 16:50:00 | NOAA-21 | GONGOGI | BAHIA | Brasil | 2911501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1893c326-c636-3a7d-99eb-238d9c2e3792 | -13.76475 | -39.87594 | 2024-10-25 16:50:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 34cb4b64-1fc3-3912-97ed-6656c34930c3 | -15.97356 | -40.7579 | 2024-10-25 16:50:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| db4cc71b-60d8-3f24-90da-c086aafa9605 | -15.96114 | -40.79391 | 2024-10-25 16:50:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| aa32b8df-d012-3c83-83d4-6de2582be5a9 | -15.90319 | -40.85915 | 2024-10-25 16:50:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ae9ff448-12b5-3cd5-bde2-a8665711c225 | -15.87503 | -40.96291 | 2024-10-25 16:50:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 589208a8-65db-33df-9b39-d10658c60b22 | -15.74178 | -40.71022 | 2024-10-25 16:50:00 | NOAA-21 | MATA VERDE | MINAS GERAIS | Brasil | 3140555 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 81a890c8-ab05-349e-8542-633d49eb423a | -15.70609 | -39.69443 | 2024-10-25 16:50:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| c28c5a94-eddb-3b93-bec1-b39d13ef0401 | -15.70534 | -39.69431 | 2024-10-25 16:50:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| b8488049-5dc8-3de6-86f8-d26cb27dab6e | -15.70377 | -40.61401 | 2024-10-25 16:50:00 | NOAA-21 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| fc0a043f-fb4b-382f-91d1-2c2a387c5b3a | -15.70319 | -40.53442 | 2024-10-25 16:50:00 | NOAA-21 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 95d0808d-151e-31ad-86e1-abffc77d0e19 | -15.61492 | -40.79336 | 2024-10-25 16:50:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 43.4 |
| 4dbaacd4-131c-3bf4-a5ee-170ba587b60b | -15.53489 | -40.63881 | 2024-10-25 16:50:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 885fd66d-ba65-36c3-b5f5-9548f8e12779 | -15.30814 | -40.64231 | 2024-10-25 16:50:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8f97af7d-9b70-34d5-b0c4-1949e37135d9 | -15.26638 | -40.65585 | 2024-10-25 16:50:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 9a7fb30f-16ca-37e4-9428-9b50a654f0bc | -8.48761 | -40.46121 | 2024-10-25 16:50:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7385ac9a-98f2-389c-bb21-d86101141273 | -8.47044 | -40.48147 | 2024-10-25 16:50:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| cf33ee11-439f-3195-821a-dca8a2f5de2a | -8.46904 | -40.4828 | 2024-10-25 16:50:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 99ba81d0-0035-3e45-8b4b-5e13235c8f52 | -8.91722 | -40.4368 | 2024-10-25 16:50:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c09592fe-1db0-3d46-9b8a-c0828dae9b2f | -8.91183 | -40.43784 | 2024-10-25 16:50:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 9d9d5bee-f7f4-354e-b6f9-9367d0613fbe | -8.69097 | -39.41951 | 2024-10-25 16:50:00 | NOAA-21 | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 9bf9654c-a8ea-3703-97a7-de0572607c45 | -8.68519 | -39.42061 | 2024-10-25 16:50:00 | NOAA-21 | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| cd8abcfa-811e-3f0d-9a71-aa3b617e4298 | -8.579 | -40.49385 | 2024-10-25 16:50:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e01ae8b3-d1e8-37e5-90b7-b943ea1b1744 | -8.51986 | -40.47602 | 2024-10-25 16:50:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9468a991-3537-3edf-9cab-b44a0c901eab | -8.51848 | -39.72032 | 2024-10-25 16:50:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 8.7 |
| e294582a-f1e7-39f0-91ab-b7b9d0511715 | -8.48346 | -40.46095 | 2024-10-25 16:50:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| cffedc4d-1798-3078-8e3e-caaee4440aa5 | -8.20975 | -39.8347 | 2024-10-25 16:50:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 40.1 |
| b50c71d6-c3c8-3401-ae95-4f41083254f9 | -8.20903 | -39.83073 | 2024-10-25 16:50:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 38.7 |
| c0989692-8932-38f6-817f-2766c51ec9ec | -8.20409 | -39.83581 | 2024-10-25 16:50:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 40.1 |
| 256f9f06-95bc-3fd1-b2cf-a1160332dcab | -8.20335 | -39.83181 | 2024-10-25 16:50:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 38.7 |
| 2e90fce0-b982-32f6-8402-045acde7c938 | -9.19736 | -40.99022 | 2024-10-25 16:50:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9c66a4da-9caa-3628-b1c9-69d3e60579be | -9.17328 | -40.94571 | 2024-10-25 16:50:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |


[Clique aqui para ver as próximas entradas](README139.md)
