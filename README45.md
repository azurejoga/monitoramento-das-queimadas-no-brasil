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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 440230a7-e8d9-38db-9506-75ae16bd15e2 | -2.6937 | -51.79201 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 831a890e-e1c3-399d-b30d-e3899dbc1613 | -2.59456 | -51.36364 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dcb951ab-7c0b-312e-ae4f-54d0c8a58504 | -2.57684 | -51.84707 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f43a8d4-871f-383d-882d-80508bdba728 | -2.5759 | -51.85271 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 010ce444-6507-364b-820b-914a86333b90 | -2.56222 | -50.6937 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 354593d1-3d41-31c8-adb4-9f15a662115c | -2.5576 | -50.69293 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f17c8935-f0ef-3c6c-aa4a-3ace9e7911c8 | -2.44912 | -50.99385 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aaf48744-4e29-3f6c-886d-e78818fdb558 | -2.41488 | -50.47809 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b95e8e89-4c20-3d46-9360-dbdbcb3c3015 | -2.4098 | -50.56792 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d370bc8-7ebf-33b6-ab62-8b5816f9ad95 | -2.24554 | -50.74348 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b82fa76-f565-3a63-a660-636102c1620b | -3.13016 | -50.60217 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0cfe466-f29f-3616-bb88-40bb3bef5375 | -3.12938 | -50.6069 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 709f071d-a56f-3e7e-8f68-1db21dadc517 | -3.1286 | -50.61168 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06194b17-cea2-39e3-946f-0ddb07ee9e64 | -3.1256 | -50.60147 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d863d898-cdc1-3521-add3-16c8bd5247b7 | -3.12483 | -50.60617 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb420a19-b109-3aa5-a04e-cfe7e83c214a | -3.12105 | -50.60075 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ff151cf8-b300-34fa-b25f-f9e51f53e980 | -3.12027 | -50.60547 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7132da59-cc9d-30c5-a6b1-b09b06c9328c | -3.11571 | -50.60481 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0057b54-03f6-3e99-97b8-b4502ff81098 | -3.09994 | -51.34836 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 90965af9-beda-3c3f-bb63-fe9c1ccf35fd | -3.09603 | -51.34228 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d351c85f-54b9-3b67-8ab2-61cd85998d15 | -3.09515 | -51.34753 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d576fd8b-bbe5-3e28-84cc-219d53fa4981 | -3.08503 | -51.26137 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4299f1c1-f4fd-3632-8c9c-f9ee39e3584c | -2.91761 | -51.00423 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97e29931-b231-3cab-8bbc-8af615faa814 | -2.91653 | -51.00266 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23866112-b248-308f-be4f-b34f00a81a13 | -4.66741 | -50.96473 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b93d2a53-25f4-3466-9e20-87dbee43ca90 | -4.66662 | -50.96941 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d72a528d-6359-3168-9832-136aefd4b1ee | -4.61944 | -50.97251 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 658276ec-687b-330b-b1f0-b1cb834fa5c2 | -4.54041 | -50.96904 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24796df5-f591-3d14-9338-941b7c675a58 | -4.53984 | -50.97131 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ed712f6-e4f4-37ab-9262-542b31ddf307 | -4.53963 | -50.97359 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 059830bc-4304-3990-917a-b0b6e4d87a35 | -4.53585 | -50.96831 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12745439-c6c0-381b-a734-4c04d1f13fb2 | -4.53527 | -50.97059 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5461407-8136-3712-b7a2-3f7e9398bacf | -3.94725 | -52.25396 | 2024-10-26 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e12f25f-7e99-38ab-9a55-5d1ccd33f552 | -3.94676 | -52.25693 | 2024-10-26 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79756f1d-7d02-3ed3-b727-896dcb82c7f6 | -3.94626 | -52.25991 | 2024-10-26 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 835ecf24-cd38-3dbd-8d2f-2cf77c2b3dbb | -3.94172 | -52.25613 | 2024-10-26 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bc82e7f-176f-3fae-9c1c-0d90803994f0 | -3.78529 | -51.3736 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46938753-0203-394e-93b2-c0b25783afbc | -3.71181 | -51.3452 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5dc99a2-e332-3300-9869-878637b13e9b | -3.70893 | -52.11834 | 2024-10-26 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 96d80197-7441-3892-99ee-6237475e64d7 | -3.70849 | -52.11936 | 2024-10-26 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 492a1220-1fa0-3733-adb2-2bb2980f17bd | -3.69265 | -51.63466 | 2024-10-26 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2af6422-21c1-37df-8f62-d53705c74409 | -3.68753 | -51.99849 | 2024-10-26 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9fe61abd-97fa-391d-bc51-586dc4708a6e | 3.64142 | -51.28949 | 2024-10-26 04:17:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a0c3581-1d28-3bc7-8fcb-d466069489d8 | 3.64094 | -51.28622 | 2024-10-26 04:17:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 665553f0-96cc-3139-914c-62659042dad4 | 3.61489 | -51.29346 | 2024-10-26 04:17:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e869968b-2cd0-32e7-9371-223f62d36754 | 3.60958 | -51.29426 | 2024-10-26 04:17:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d201494c-5405-39d8-b8b2-926dcce79f84 | 3.38464 | -51.28972 | 2024-10-26 04:17:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b17adf4-a5fc-38a9-a0a1-eb1b366d570a | 3.38417 | -51.28647 | 2024-10-26 04:17:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7d49d05-4c0a-3d97-8cd2-a6f608749bc8 | 2.80258 | -50.93093 | 2024-10-26 04:17:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 938771c6-7edf-3543-90f9-7639814c3cbf | 2.80214 | -50.92794 | 2024-10-26 04:17:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ef89742-241c-3e28-ba78-7ef77d7e52fe | 2.79702 | -50.92873 | 2024-10-26 04:17:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3111e1ba-6a64-3430-9d4b-e6cc0e8c8a1e | 2.79236 | -50.93252 | 2024-10-26 04:17:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0d6db75-0f2a-3da2-a231-509a5e269a41 | 2.78902 | -50.94529 | 2024-10-26 04:17:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56ea0630-48ef-341c-8bea-9c602d48dc0f | 2.78857 | -50.94229 | 2024-10-26 04:17:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64003607-1a17-332c-b038-960a8e08f005 | 2.78813 | -50.93929 | 2024-10-26 04:17:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a82c1590-dd6b-3b1e-a6a7-ab318fb52055 | 2.78769 | -50.93629 | 2024-10-26 04:17:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be39b211-132c-3799-9c89-85c68a3d1b63 | 2.78725 | -50.93331 | 2024-10-26 04:17:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f484fcee-1afa-3e89-a953-4479029d94c4 | -1.65199 | -53.24265 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8824af3-7b24-312d-a5bd-f28edeb907f6 | -1.65141 | -53.24627 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df9dee5c-4faa-3fa2-ad15-43652b0414d5 | -1.60084 | -53.30999 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cae077cc-adde-39de-97f1-20356f321e2e | -1.59524 | -53.309 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8305b37-3d26-3d81-8adc-27df6cc37163 | -1.58964 | -53.30807 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 549b2423-f838-3b2a-8952-03279a56ecb4 | -1.58901 | -53.31187 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4709c8aa-27b5-3d7b-bd86-87342853177c | -1.5778 | -53.30997 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb2bf23a-1167-3c65-a08a-1e41800ecb11 | -1.57717 | -53.31381 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 352e26a9-baa9-3f95-9329-cfef7c9f5806 | -1.5577 | -52.0612 | 2024-10-26 04:17:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6eb6bfeb-9b02-3cd1-a94c-7c7540c18123 | -1.55254 | -52.06039 | 2024-10-26 04:17:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2c2bfef-9888-3ec3-8146-f1dcca207ce7 | -1.41749 | -52.10452 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d45e665-4d1f-3550-ac06-780da7acb4d0 | -1.4128 | -52.10055 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03b86679-53e6-32cf-83e9-58aeab09f470 | -2.97733 | -53.26396 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab3e6c33-dc53-3b85-8faf-2884b4befaed | -2.97689 | -53.26653 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c22b600-bc60-3a0c-88db-f9c3b54ed3d2 | -2.97674 | -53.2676 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 33e73fbc-f2c8-3cfd-b1d3-de26b6c2eafc | -2.97145 | -53.26544 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 28058b86-67b3-351c-85dc-92559aa65270 | -2.9713 | -53.26649 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10a284ea-02e6-3425-9932-d494776fb018 | -2.97083 | -53.26906 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b337947a-182d-3ec2-ab3c-22db27067ebe | -2.97071 | -53.27013 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0d7f1d83-202f-3d97-987e-ea3254b89135 | -2.96586 | -53.26539 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44924c4e-4f41-314b-a486-bd5fc5b10114 | -2.94561 | -52.98281 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41441608-f9a3-3cfc-9fcb-c4f14e162fac | -2.94554 | -52.56424 | 2024-10-26 04:17:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b4d79d76-7fe7-3131-83f7-b7714fb21d46 | -2.94504 | -52.56729 | 2024-10-26 04:17:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f1154cfe-378d-3a24-9eb9-b81d9211253b | -2.94454 | -52.57035 | 2024-10-26 04:17:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| c7f08c6c-9f61-3314-a37c-e7fb7e01398a | -2.94349 | -52.57671 | 2024-10-26 04:17:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 94b0cb7c-38eb-31b3-8e0f-f03194d77d96 | -2.94021 | -52.98212 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2312de31-e3b9-380b-94d2-6ee68bae8f67 | -2.93968 | -52.98524 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5e0566a-ef28-3ba5-b372-f68cccb9a65a | -2.89435 | -53.32307 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a45d0dd5-d325-302e-8206-dbea34256615 | -2.89373 | -53.32681 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0fa430b-9830-3407-914d-d6e85eda7bbb | -2.89312 | -53.33044 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45024d3d-28e2-311b-9d63-208b6ec23161 | -2.88471 | -53.31317 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f2bb5ca-27bd-3e04-ad10-abb4586f1e56 | -2.8841 | -53.31683 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91e4c86e-f19d-3316-87f7-d0307fd5cf37 | -2.88348 | -53.32049 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1338efd3-3c49-32d8-a8c2-e2bcb584c7b1 | -2.88285 | -53.32428 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51afad4c-1b15-312e-b5b9-c2c91119f05d | -2.8822 | -53.32812 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd31b7e5-53e3-3b51-8165-eea3fca0626d | -2.87982 | -53.30868 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a1d30a6-1854-3845-b9db-8890818f6756 | -2.87922 | -53.31223 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e2eb5c2-0ecc-3675-a7d1-f9814e429136 | -2.87862 | -53.3158 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c2832f79-cb5f-30bb-a989-20dc2f803e87 | -2.87801 | -53.3194 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7f19b3f7-3ef6-3908-9588-c9d61e8c7707 | -2.87372 | -53.31132 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cc2b561-745c-35e5-8681-0f51389e5b09 | -2.83018 | -52.14892 | 2024-10-26 04:17:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91b491b9-0639-3f4b-a0ae-232a8f67f22e | -2.82802 | -52.14954 | 2024-10-26 04:17:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38c59530-1854-3cfa-8e3d-c0d533272d38 | -2.8251 | -52.14805 | 2024-10-26 04:17:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README46.md)
