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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b7bf794-9eba-3428-838a-b486d6458680 | -9.14151 | -67.84225 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9b5bbb3-8265-3b7d-9145-da6dda634781 | -9.24747 | -67.96949 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad822a25-5d8e-38c1-9eef-0e4f0eb449c3 | -8.62843 | -67.05652 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8fcf163e-5fc4-33ab-86c5-0d109abab017 | -9.23795 | -67.87553 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fac95de7-bad6-3542-adee-d67dbf14ab33 | -8.83236 | -62.4235 | 2026-10-07 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f68c8038-0d33-398c-a442-69e1b96a4b7f | -9.10635 | -65.35612 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2050d17-daa1-35fb-98e5-5f7c68aefc8f | -8.59868 | -67.04935 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e580bb48-5d69-3333-98f2-30e389c50d25 | -9.06771 | -67.73776 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6c48eae-c74a-3e69-8554-247e3fc880d6 | -9.44423 | -68.40304 | 2026-10-07 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cfedefde-9c43-3037-82f6-24232768106d | -7.95314 | -71.33532 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c57d760-4911-3666-932c-ea8f2440715d | -10.73067 | -68.86308 | 2026-10-07 06:01:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42ce5f9b-e154-3e90-b4fd-9929ed88df51 | -9.23121 | -67.89671 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b3da111-b954-3825-bef5-b7eab5608ac5 | -7.67437 | -67.02589 | 2026-10-07 06:01:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f6f1fd8-70a5-3e8a-8a4b-cc4bbee65966 | -9.01858 | -69.21034 | 2026-10-07 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1dce013-08b8-34f8-82fd-db25242d06d4 | -9.44197 | -67.09568 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4a2dc8d-874d-378b-975c-edf086140ebf | -9.24988 | -67.96629 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0da22cb1-c17c-3253-aa4d-bd80ba3e2e06 | -9.1105 | -67.70709 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ba10bd8-550d-3270-a84b-d88bc8c4edcf | -9.09016 | -67.68149 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f13b8dd-cc74-395b-adef-f8a0d6daaa1e | -8.77998 | -69.53615 | 2026-10-07 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd456196-b38b-3984-be06-8a7849b63367 | -8.36855 | -70.57654 | 2026-10-07 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73039ad3-7fe9-3b85-a2a0-82bf9dd0bd70 | -7.94967 | -71.33475 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b960cbc4-a497-3b9d-b6f1-4806c543482d | -8.93748 | -71.3914 | 2026-10-07 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f02509e0-2b79-3cb0-afc4-c23c099456a6 | -9.42221 | -67.61562 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecf81a50-1708-3b99-8c77-872ca60a7ad2 | -7.95947 | -70.93719 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20d50a21-01c2-307b-9e96-bd5015c6260e | -7.7047 | -72.80561 | 2026-10-07 06:01:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ffad72c9-fd1c-3ce2-ba74-6ed57606cd75 | -6.84164 | -58.59431 | 2026-10-07 06:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a59a8f3b-7d68-3e5d-bc74-2f4e3257d38d | -9.75577 | -65.06779 | 2026-10-07 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 794cadb6-b517-3ce1-bf5f-fff81de5052a | -9.51969 | -67.11091 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b99ca78-547b-3665-89bb-69fea0db0ad8 | -9.14156 | -65.3028 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf493d81-e742-33a1-9699-5a5e997a561b | -9.42197 | -67.41058 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8449fa2-916d-3c5b-970b-9bc38a89af80 | -9.10994 | -67.71075 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63fb7df3-cbd2-3bc4-a934-0b2ee535cbf0 | -7.70768 | -73.0677 | 2026-10-07 06:01:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7425aee4-dc2d-3ae5-a5df-841b131f8491 | -7.8864 | -72.35892 | 2026-10-07 06:01:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 18.5 |
| da98df64-bb47-35f3-81cd-c349c4b684fc | -8.91175 | -68.79007 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19689369-23be-317c-b395-2cf3f7a2191d | -9.13846 | -65.29762 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37684d59-b5ba-3c4f-97da-94db8fe1a3a7 | -8.73159 | -69.98735 | 2026-10-07 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 73dca9c8-091f-3cc5-9a09-6b3a1718af50 | -9.06411 | -65.48421 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d15bf5cc-d96d-3101-8b0b-0f7555ac9ee5 | -7.75828 | -70.72963 | 2026-10-07 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e455e185-992d-39c3-a34d-6046fdd58e9e | -9.28903 | -65.64461 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90c6e4f9-0d39-3d0b-a4df-648afbb7d483 | -9.0763 | -65.48849 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 014fbac1-c033-36c9-9c06-56a140b68c90 | -8.14763 | -64.07198 | 2026-10-07 06:01:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f410180-0b74-3baf-b96f-ee6a728267b5 | -9.43851 | -67.09515 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3eb99e7e-32f1-3989-8bcb-8a9665bcf42d | -9.24804 | -67.9659 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21211dd4-e299-38c0-bbfb-04e80d5608ee | -8.71326 | -69.46473 | 2026-10-07 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5d9af28-e660-37c5-84e7-764574e4574a | -7.89074 | -72.35526 | 2026-10-07 06:01:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db3a3848-f295-3b31-aedb-3051d2c5b614 | -7.74949 | -70.15565 | 2026-10-07 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51af1100-81d3-329a-9ee1-fe335f91cf21 | -7.52834 | -70.02915 | 2026-10-07 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4725473-234b-37ee-8b47-f90b86d359fb | -7.43984 | -73.20309 | 2026-10-07 06:01:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84cf385a-ced3-343e-a537-b93340915515 | -9.11108 | -67.72586 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 040da968-ae81-3e8b-b578-6734fcf7e9b4 | -9.27868 | -67.54472 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5ecafb4-98cb-300b-9d5b-d8941eebf78e | -9.21039 | -67.83038 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| abf933fb-e201-3f20-be3a-ebb48a0967b1 | -9.59478 | -65.24123 | 2026-10-07 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b4ac18b-657b-3573-8f92-58288ddbf9a0 | -9.46163 | -67.083 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd230cee-8430-37cd-ae01-e6dc44b1540e | -9.11332 | -67.71128 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 352ff0bb-cf9b-3c89-a492-04423d3f7b9c | -9.44479 | -68.3995 | 2026-10-07 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2633eca8-e9f8-3bea-bffa-a4fd2e5d7ce6 | -9.23065 | -67.90032 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e1455d7-cb23-3e7d-b1f3-cc1f2b81f24d | -9.61013 | -67.48494 | 2026-10-07 06:01:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80b1ccd5-48c9-339f-aeb9-f7f1d690111a | -8.57551 | -67.22271 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae4c2a2d-e823-34ba-82d0-25847248a7e5 | -9.33453 | -63.6805 | 2026-10-07 06:01:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c52b9ed7-e419-31b1-b2b6-8bcef47b72f0 | -8.6531 | -66.93959 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a936dfe-8173-36fb-9f6b-89007f133a6b | -9.3998 | -68.79651 | 2026-10-07 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf12ea6f-8982-379f-8d2a-1c13831f8e55 | -9.12221 | -68.89889 | 2026-10-07 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f717a3d1-eb05-3a9f-8c98-9251c17c1733 | -7.01755 | -71.62144 | 2026-10-07 06:01:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23ab9468-8860-3016-90bc-ab6bcc264738 | -9.12072 | -67.84271 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f9b5f3f-f311-3001-922f-11df9208b93a | -10.58928 | -69.24448 | 2026-10-07 06:01:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4b6928b-72a9-3d33-998b-e928664d2d86 | -6.92096 | -71.47932 | 2026-10-07 06:01:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9d6d44d-9828-30c2-a983-01e3a2f5ee53 | -9.41855 | -67.41006 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f197101a-5345-39ff-b5fd-dc9377c48357 | -8.20773 | -71.00735 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a15439b-9ab7-38c0-a22e-a7ceb6543c61 | -9.46686 | -67.07201 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc6cf6b0-3c4e-36a2-96b4-d7a2da74bb79 | -10.5581 | -68.85712 | 2026-10-07 06:01:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac883868-386b-3c10-954c-e05fd36f211d | -9.07109 | -67.73828 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78d52daf-7174-397a-b58e-189e4925c092 | -10.04221 | -67.75127 | 2026-10-07 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ad95a8ce-ff92-3e8f-acc0-6ce039dfcfd1 | -9.2312 | -67.87449 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc0b0264-2418-32d1-a037-ffbb6bbc8bab | -8.87736 | -66.86662 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f418a04c-3d7f-3f44-bb75-4c7db8d60e94 | -9.60969 | -63.809 | 2026-10-07 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89b0b96b-ac00-35fe-bf02-f84421317c85 | -8.01784 | -71.07253 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82024a0e-3783-3b82-8789-1f3bcc2eef7d | -9.33827 | -65.46371 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02fad953-3d19-33b0-87b5-597d8e9a5e5f | -9.50698 | -67.17163 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ea847f6-3e36-3bd0-941c-2953d49377f6 | -10.46175 | -69.2776 | 2026-10-07 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38eee07f-af06-3d87-a73d-e8c1772a6308 | -6.84343 | -58.59346 | 2026-10-07 06:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23222927-0111-3fb8-b18c-bb2247aeb7a0 | -9.17275 | -67.32294 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9161367b-8d3d-34e1-ae11-4cb130bb650c | -7.88416 | -72.34976 | 2026-10-07 06:01:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 88c3374c-3569-3e87-81b6-ccb6339b4a04 | -9.33034 | -63.67987 | 2026-10-07 06:01:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28fae6c2-242e-300f-ba78-67bac7c7e593 | -9.20701 | -67.82985 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 151bad8e-dee4-3560-99a5-7bbd7251cedf | -9.11455 | -67.86028 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17be28d3-89b8-3ea7-9094-d88964e70b06 | -7.76168 | -70.73017 | 2026-10-07 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f08e4ce-7ce7-30f6-ab9c-1f4218458d98 | -9.11172 | -67.83389 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1caacd59-2ff9-3ca2-b30c-a267daf18ce6 | -9.45411 | -67.08577 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9b2df56-d182-3ecb-84e6-e77b2fa6560f | -9.48401 | -67.57603 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38b355bb-da71-3dbc-b550-b23a445ab6d1 | -8.7706 | -69.53107 | 2026-10-07 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 261aef02-d5df-35b4-a455-a1befb5d052b | -7.44368 | -73.20374 | 2026-10-07 06:01:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f4d3f44-b000-30f6-83ac-a09e3a44c9de | -9.07503 | -67.73517 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aece54a-a3cf-3856-8995-db6c7f861e99 | -9.23458 | -67.87501 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38118df3-af91-3f70-9195-31136f72a93f | -9.45758 | -67.0863 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a34bb45-2a8f-3fac-b632-a725d2109186 | -8.25167 | -72.78183 | 2026-10-07 06:01:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 901a606c-3948-33a8-a2c8-24fa1814d6c9 | -9.11959 | -67.82769 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c97a999b-49be-3572-95f4-571e21167205 | -9.1072 | -65.35396 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43828cc2-d1af-3121-aa18-fdefe6ade03f | -8.60407 | -72.7298 | 2026-10-07 06:01:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6d748d6-81b1-38ac-97ae-4fa308b5d144 | -9.10277 | -65.35797 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73521a89-07fb-39e4-ab1b-3c319b35bb45 | -7.53226 | -70.02614 | 2026-10-07 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README121.md)
