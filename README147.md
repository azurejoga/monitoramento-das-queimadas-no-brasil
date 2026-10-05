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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a4126be-66e6-3d9c-a72e-cb53c45b05cc | -9.34017 | -64.71497 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7cdd6124-b99c-37b1-9a64-17df6d5a9526 | -1.6669 | -55.0619 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f3a0e3a9-c10f-3234-acd2-faf63cc96608 | -7.23172 | -55.19675 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 24d6ca16-7bed-3e8d-9543-d2180d7662a6 | -8.82049 | -68.6553 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 84ad9da2-0d14-3fb7-9074-b2e555256058 | -8.63225 | -69.5032 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 742f867a-cf46-3e7c-8167-92579ab2b4eb | -1.28255 | -56.97824 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| edd7be5c-fb90-30a9-b43a-90f2861b014e | -9.14987 | -68.23546 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| da860190-3148-36d9-a95b-ef49c6ca5286 | 3.5723 | -61.34956 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3a96dd78-ac85-315a-8d46-be72c48091a4 | -9.42703 | -68.06329 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 98c98879-c29b-3523-b18b-d780a7b524b0 | -10.67309 | -69.09917 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 16.6 |
| f3e00e5f-9dae-3cc2-afd1-c0426647bbe0 | 0.92358 | -60.40395 | 2026-10-05 17:37:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5c9a5a4c-5cf2-3edc-bea8-e61ab7e2e713 | -10.37987 | -68.95561 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 6e261e73-63ca-3955-a95c-16f8cae2a81e | -2.0111 | -66.31789 | 2026-10-05 17:37:00 | NOAA-20 | JAPURÁ | AMAZONAS | Brasil | 1302108 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3679d7c1-3978-3008-af1b-ad2eb43fcbb8 | -9.34424 | -64.71445 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.0 |
| ab19d91c-595b-37d1-ba32-570a4a22a26b | -1.56267 | -55.17188 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0fd191ef-f8d6-393a-b5b3-93fa6b8de680 | -8.99724 | -65.39741 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e26a822b-091d-3d2b-86bc-de44e60a2d9b | -10.14685 | -69.02016 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 5cbb05d4-761b-3faa-9c4a-7c19fd214dbb | -8.42485 | -55.00302 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 450584aa-215d-30bc-bcb9-6e3d036c76bd | -2.54303 | -66.0341 | 2026-10-05 17:37:00 | NOAA-20 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 2bc7c362-3338-394f-a469-ec3e4d48edad | -8.45955 | -67.24358 | 2026-10-05 17:37:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c8ff74a4-2c23-3863-a878-237e512538a0 | -9.0851 | -66.08447 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| eb41cdc5-43d1-3457-ac61-fee0f8c2bae5 | -1.60032 | -55.97112 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| dde512ad-e116-3c66-a04f-03204d9797b0 | -0.37885 | -52.06363 | 2026-10-05 17:37:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b5483854-eb11-3da3-8109-228370dbc2fd | -2.04157 | -54.30427 | 2026-10-05 17:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 8dc45ec9-4ffd-3b50-9fab-01ef0420f247 | -1.23838 | -55.94841 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 757a4edc-9628-36c5-bc20-2e5a91017cc7 | -8.77938 | -69.64113 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 25.1 |
| ed36bcac-c930-3d17-abb6-9fbe5e4216d1 | -9.4493 | -68.23254 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 10.3 |
| cf1616ec-5500-3604-9a53-4fbd97eea65d | 2.26272 | -50.82598 | 2026-10-05 17:37:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 884df0dd-3178-3d02-8603-3766483f33dc | -1.69664 | -55.0196 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 928f0d3a-ac0c-3655-a390-e7505e706b16 | -9.26965 | -67.5324 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 915182d2-7cdd-3d99-9fd4-2bdf69f5c58b | -10.39617 | -68.03209 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 13.5 |
| f16adc8c-21b0-38e6-bf3b-055a35018136 | -8.97386 | -71.41173 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 92ee1ae3-420d-30ba-bb19-461bbfe724fa | -7.07032 | -59.23542 | 2026-10-05 17:37:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fde5e162-f02c-3197-a325-e42849d9c998 | 4.21382 | -60.69523 | 2026-10-05 17:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3c89f0d8-e16c-3a64-a2e5-22cc9cb0ef78 | -8.64458 | -66.95565 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 49c4559b-c504-3dd4-9cfa-768ff290efcd | 1.61064 | -55.78863 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| bd0853a5-7853-3c59-acc0-9a521abe6d83 | -2.76924 | -57.65956 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a4dc07ac-2e14-312d-93e3-b5f7b7435804 | -9.46053 | -64.33065 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 31.6 |
| fa9745e2-732b-3ca1-81e7-707edff6bb37 | 3.14648 | -61.40543 | 2026-10-05 17:37:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd41b602-669c-3ca5-bc5a-1e1b290272c2 | -1.3756 | -55.99932 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e3a63138-db43-328f-be6d-934beea539f6 | -9.12591 | -68.29243 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fbfd347-6999-390c-8456-d5746de349a3 | -9.29237 | -67.5387 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 0fbbbeb3-eea6-3289-abbc-b74b52929f6e | -1.30608 | -56.92494 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e41712d1-148c-37fb-8477-57d8a5b1399e | -1.7494 | -56.02327 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d7f271a-1827-34e3-b475-6be721846a66 | -8.66095 | -54.57143 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| c5fbcc16-8c5c-3d1d-9359-d73075034782 | -8.66758 | -54.53711 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 7daa88af-7ffd-39e5-991c-3192f9541890 | -6.51577 | -55.38881 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d0142c77-b252-3d0d-8cb9-c60ae89a87f7 | -8.74206 | -66.57747 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 858ef546-3f95-3df1-9019-760f9dd9c1b5 | -3.17443 | -60.05671 | 2026-10-05 17:37:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d0c15e52-bcf2-3ec2-aafb-89bd4937d0c0 | -10.6916 | -68.75754 | 2026-10-05 17:37:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ce966d3-017e-3e61-8d68-b546907ccf37 | -9.48175 | -66.79305 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a93f6a05-9704-3471-b69a-073e19544961 | -8.85204 | -66.79786 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 9d6dd54d-0b3d-3300-8ac5-e497f878e4af | -10.4231 | -69.53688 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7bf0441c-07e1-3b00-b4aa-658ad154e4b6 | -8.59615 | -67.13844 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 662fccba-15b3-3451-827d-ae4a755fae52 | 3.84808 | -60.2874 | 2026-10-05 17:37:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 688ea980-de98-34f4-b0f1-6418221bf3d7 | -8.86892 | -66.82832 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d4340e4a-82c9-373d-b129-5cd59dcdce92 | 1.29589 | -51.12692 | 2026-10-05 17:37:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 555e1ed4-0f2a-391c-8e9b-2b232b6e2636 | -1.28664 | -56.92788 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 62c7b0c6-d906-3891-a353-270528f24aea | -9.88472 | -64.27673 | 2026-10-05 17:37:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ef3fcde5-c8ca-363f-88b0-8b2713f4226a | -9.09962 | -67.74844 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 1757b622-630c-3612-99fc-4e0d97cbff43 | -6.51407 | -55.38671 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d5ca6c5c-e8d0-3ea8-91f9-ed9fa4976a85 | -9.35318 | -68.92175 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 3d663d04-7a2f-3a00-be84-59fac30289d7 | -0.73909 | -57.97787 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 32918f7a-ae16-30dc-ae2b-1f4bbce32b00 | -1.77532 | -53.77842 | 2026-10-05 17:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 04c351f2-b431-36b1-8655-ff37ac12f64d | 2.08826 | -50.90134 | 2026-10-05 17:37:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c5555d32-5555-39fa-a8be-e1988658bdc2 | -9.54256 | -68.66749 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7977e4d9-6463-3834-8c04-dc0f7fab2159 | -9.07962 | -70.03949 | 2026-10-05 17:37:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 4dd9907c-11fd-31c1-a474-dafc033bd21a | -8.85998 | -66.7868 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 30ff0478-f99f-38ca-8c45-d65b7c53b16e | -2.52046 | -57.48346 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 25731c73-9073-3c63-b39b-3166313401fe | -8.82007 | -68.65202 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| bee311ef-183e-334f-b489-c92117b0bf90 | -3.24246 | -64.83674 | 2026-10-05 17:37:00 | NOAA-20 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| bb59511b-8b2e-3909-95de-7da0e966e755 | -2.09368 | -56.62072 | 2026-10-05 17:37:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 75981709-4ccc-3f86-b166-20a95deece4f | -2.02359 | -56.88921 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cbddb409-4f1b-3b3d-b21b-bd611e824b24 | 2.48489 | -51.26882 | 2026-10-05 17:37:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fc034cd5-1194-3bba-9f82-00c8604cfd48 | -7.11317 | -55.72332 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 1f94a4a0-722d-33cd-b70b-73ca15e350c5 | -2.54372 | -65.87505 | 2026-10-05 17:37:00 | NOAA-20 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 31.8 |
| d89f21b0-697d-3422-a24b-5fe0585e8d26 | -2.15299 | -56.66391 | 2026-10-05 17:37:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efbf0138-2f24-3a75-b136-07b014d24c16 | -9.43533 | -68.8586 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 8941bb3b-84a9-3533-90e6-324aefc9d92c | -1.19613 | -53.38667 | 2026-10-05 17:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 27571742-6c18-3771-87d9-3dec4b2deb81 | -2.60488 | -57.56414 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| a1b353da-9492-32d4-9ed5-b93b0929b501 | -8.72078 | -68.90417 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f8228b39-469d-366e-b12c-71abb9ce2f32 | -0.71028 | -57.98658 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4c75b91a-f8bf-320b-8708-534109d08fa3 | -9.1408 | -65.90542 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 9e399c3c-8403-3f40-81b6-99ab5612316f | -9.26 | -67.64796 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 302a5dc0-3e08-3746-81e3-1ba753fdde4d | -1.38356 | -55.40955 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 212a6fb6-e6d5-33a1-97c6-099714da7ec0 | -8.82547 | -67.38492 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 66e7763b-0ee8-3247-bdcd-4809db7520e4 | -10.01818 | -68.97508 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 93a2e441-145a-3101-9d89-6bbf7c4f2e82 | -2.53045 | -57.23165 | 2026-10-05 17:37:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 7a382322-8dd5-3172-a7c3-683e0fe13e49 | -9.41997 | -68.95239 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 175b9b84-d089-3805-9353-5635975c29c7 | 1.07733 | -59.69398 | 2026-10-05 17:37:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3ff60b2-40d1-352d-885d-4181487d7726 | -8.7967 | -66.9153 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e78728ff-18e9-3cb4-801b-d6d74f05a74d | -9.12177 | -67.83739 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fe5a3f8a-ea26-3594-be84-744827c8512b | -9.22447 | -66.12699 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c5ffb9f3-ccd2-3c58-b6f1-2276c189be03 | -8.62621 | -69.50027 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 342b4693-1e26-3103-9477-79a78e30149c | -8.72582 | -70.56535 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9dc2201-7a05-303c-affd-9223f776466f | -1.81654 | -57.10122 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b15f70d3-b163-3598-930b-0d5f57e72694 | -2.8742 | -58.27887 | 2026-10-05 17:37:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d0f1fff4-d72b-30f7-a04f-4e2c34817ca0 | -8.97647 | -69.30132 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4e544580-2483-3472-ade6-d03b55eb96b6 | -2.53524 | -66.09251 | 2026-10-05 17:37:00 | NOAA-20 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 26b68ed9-21e9-3a51-a5db-bb299ad43dc1 | 4.22297 | -60.70417 | 2026-10-05 17:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README148.md)
