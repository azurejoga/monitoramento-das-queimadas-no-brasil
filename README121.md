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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4371d9a1-9bb0-3b17-a6cf-4a5c71141d05 | -9.1405 | -65.41495 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43e27183-03e1-3644-bc15-938c4ac6bea7 | -8.33595 | -70.79975 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 710d8c21-7db8-350e-afe5-d84e6a541382 | -9.05971 | -65.48814 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7d427fff-d6e5-33ce-90c1-e31eb88af793 | -8.04268 | -71.58144 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5be65c8-9436-37a7-9f5d-3c9f9d7fb9bd | -8.62937 | -69.50121 | 2026-10-07 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da49e832-5112-31cc-8474-d4f1478a5d7c | -7.6734 | -70.0814 | 2026-10-07 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79fae058-2d02-3846-ad4a-b975a8770d26 | -8.84109 | -66.79047 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08f499d4-8221-3e83-914f-fe47aa70100e | -10.24427 | -68.30079 | 2026-10-07 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4dd56bd4-f5ce-38a8-a989-d45869e8a067 | -8.30443 | -72.79755 | 2026-10-07 06:01:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4942abd4-0b7e-3823-bf83-85520f2c73db | -7.95125 | -71.33644 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c143c7d7-236d-30a3-be2e-dd30f6736d70 | -8.62495 | -69.50763 | 2026-10-07 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b17ec55-d67f-3d22-a6d4-aac9bfb21221 | -9.13913 | -65.29302 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1003102a-7c13-34cf-8f6d-5a54e62f49cb | -9.34721 | -64.71273 | 2026-10-07 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e41b754d-f42c-3616-8441-235e20a90c1e | -7.8871 | -72.35463 | 2026-10-07 06:01:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 18.5 |
| e8c34f8c-527c-3ddb-9116-97ed1ed454ae | -9.11848 | -67.85718 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa671420-409c-32e3-a251-c1dac43e9a57 | -10.4512 | -69.30167 | 2026-10-07 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b963496-46e9-314c-90f1-f05fd5e88174 | -9.15533 | -65.94681 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2065bec9-5731-3a7b-8eb2-83b3b30331ec | -8.83301 | -62.41887 | 2026-10-07 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d06f220-9a0f-3530-be44-6b238ab8f7ed | -8.87128 | -69.17612 | 2026-10-07 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 191b0a54-07d7-3aad-8b50-61e4157fe185 | -7.94903 | -71.33861 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a1b9b46-d366-3e49-a72a-1b0845d437b3 | -7.85412 | -72.46423 | 2026-10-07 06:01:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bcc2b239-6183-38ef-ab63-e3aaf8352944 | -8.01727 | -70.92639 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14db2001-ae50-3e85-9311-9dc4c69145b1 | -9.49986 | -66.73737 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70248eb1-f863-351b-84ca-ea98310d18da | -9.26832 | -67.9359 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee9b1724-6237-3710-b238-b80305a56ae3 | -9.24467 | -67.96536 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ad7d80d-95da-3b54-9b5b-8a63b3ff5862 | -9.60728 | -67.48067 | 2026-10-07 06:01:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a40ae109-ce2a-30ca-a284-34b5c3778173 | -8.86797 | -69.17558 | 2026-10-07 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c80d9365-6aec-3d31-ba62-212ab3acb786 | -8.74142 | -69.41575 | 2026-10-07 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb727bb9-827c-3901-ab87-744edda90af1 | -8.28457 | -71.07336 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 844d9b45-11dc-3ccf-999f-c0a3f885a382 | -8.39769 | -70.26771 | 2026-10-07 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43167237-ba3d-33ed-b1aa-8861c3d887c6 | -9.10259 | -65.35555 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 726761bd-615e-359a-90cb-cb901fdbb5ab | -9.13469 | -65.29705 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44238838-61e1-3403-9f4f-64101cbc816e | -7.26897 | -72.99837 | 2026-10-07 06:01:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c6c70a9a-81de-3345-acc1-4f578fa64580 | -8.91131 | -68.87936 | 2026-10-07 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 080236fd-0062-321c-b423-9d8ec09ac647 | -10.61776 | -60.48999 | 2026-10-07 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 669ecd1b-6c65-311e-95fe-957803198929 | -8.25031 | -72.77921 | 2026-10-07 06:01:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1b32fa1-97b2-3f42-8950-f13b2524eb31 | -8.26752 | -70.8983 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49fc9895-4e98-3cd9-b8cd-e3c2f0b03f87 | -9.10704 | -65.35154 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 726ab8ea-816a-34c7-8e18-5e42246a6bc8 | -8.61482 | -67.19316 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 736f18b0-7b65-349f-8c2a-9414236a6c2e | -9.05598 | -65.48757 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 680c85c2-721b-3268-a455-b3faccaabec9 | -9.54429 | -64.81702 | 2026-10-07 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8b5b80d-0922-3da8-9908-f285f13299dd | -8.0172 | -70.92752 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8126b7b0-b155-3691-8048-60a9ff095623 | -8.62881 | -69.50468 | 2026-10-07 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db08c14a-9928-34f0-ae02-d7dbda76cd8b | -7.88276 | -72.3583 | 2026-10-07 06:01:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 2dc7c691-97ab-33da-9aeb-7378a7a59c1c | -9.17044 | -65.76796 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46072b48-160e-30e9-8c4d-b267b4af2e90 | -9.97297 | -68.82263 | 2026-10-07 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17ad973c-a685-3999-815e-3dec03f7b15b | -9.24411 | -67.96897 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a16719b-d4cc-39a0-9f95-9fb09473587b | -7.81658 | -72.71534 | 2026-10-07 06:01:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98d614f3-7c98-3310-915f-efe983fd826c | -7.82177 | -72.70702 | 2026-10-07 06:01:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e88bc5a-a41e-3331-9457-c781c434177d | -8.69348 | -68.70898 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ae82c7a-47df-3b80-b711-794ec8f66c1a | -9.47033 | -67.07255 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c7cb60f-02a4-34f0-a58b-96a8b30dbd3a | -8.9112 | -68.79356 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4408ae85-3dbe-3987-b472-110b690e87bb | -8.21055 | -71.01164 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 045c6a2f-54aa-3a2b-ac68-bf2357027b36 | -7.57278 | -70.22308 | 2026-10-07 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66630061-7e83-3ab3-83cf-e12fd02a8605 | -8.86301 | -68.77547 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8d1bdc1a-4300-31ed-8afc-3e73b644a435 | -9.35388 | -68.76408 | 2026-10-07 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e43e684-e52b-311a-a0f4-351ce2090cca | -8.24611 | -70.83459 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08b5ffca-2932-3b5c-87eb-98f4dedd46fb | -7.69304 | -72.4173 | 2026-10-07 06:01:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d920fd3-bcb7-33df-9763-0b86f3fbfcdf | -9.39648 | -68.79598 | 2026-10-07 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15f8754d-1477-3d01-97be-24604b78fb34 | -8.15114 | -64.07608 | 2026-10-07 06:01:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3778a221-d702-38aa-9ee6-afa0711a27bf | -9.14358 | -65.42005 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2dd5ddc-fe35-326b-bfbf-7eac882f9b56 | -8.98057 | -65.44576 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de1cf5c7-2817-30b4-b61b-5214f77f33f8 | -9.33729 | -67.75695 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2ad0e4b-3acd-3202-b478-7ba5097ecc95 | -8.97684 | -65.4452 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 896deca0-5c59-35c2-9c88-64736b731c78 | -9.52228 | -67.41796 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23b99852-b217-33d4-bc62-ad631ff7fc42 | -9.13535 | -65.29245 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 021218e6-94d1-344d-a9cd-c5556f664331 | -8.54586 | -66.97909 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f479ad2-b78d-3bfa-88e1-2f0164500e69 | -8.54241 | -66.97855 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbf0ce15-3f8b-36ad-a130-ee43af535141 | -8.15063 | -64.0796 | 2026-10-07 06:01:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6beddfad-2c22-3a9f-b382-4937b95ae0c2 | -9.42539 | -67.41112 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be2991ae-5e8a-36bd-b0ca-1e813e50af4c | -8.77667 | -69.53561 | 2026-10-07 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6960fbfb-363a-352b-808a-f78e832d2f30 | -7.26517 | -72.99773 | 2026-10-07 06:01:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ca949f8-dbd3-38e4-8aed-fe046899b837 | -8.71657 | -69.46526 | 2026-10-07 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df924eaa-d850-3067-b90e-c789a397b43e | -9.43381 | -68.07965 | 2026-10-07 06:01:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49f8cc99-5f27-38bd-beab-0789a9af564d | -8.82781 | -62.42296 | 2026-10-07 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91610663-09b1-3bbd-bfd4-35ce2d4025ea | -9.42183 | -67.75482 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99e4cdf4-d620-38ed-bc3d-7b291f6b82fc | -9.6107 | -67.4812 | 2026-10-07 06:01:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 882d7587-633c-3c60-bf79-5137054ef4b9 | -7.70396 | -72.81013 | 2026-10-07 06:01:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c827c5e1-fdd5-3f1a-8817-c6f5390c6205 | -8.83975 | -71.80141 | 2026-10-07 06:01:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf7e02b3-c237-3a43-8a3b-b60bc82e534d | -8.15515 | -64.07668 | 2026-10-07 06:01:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7ce7f56-d53f-3822-8bc3-f12b71352a5c | -8.54126 | -67.00948 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 169c8635-4015-3c6f-a445-8e9559def49f | -7.02812 | -71.75101 | 2026-10-07 06:01:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| baa7ee85-5c86-3886-9db4-220a020187e7 | -9.11096 | -65.35454 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56e68c79-2bf2-36d7-b8ba-5cb58bb6ac36 | -8.51669 | -67.01373 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 994a608c-e392-3346-a816-6f76695843db | -8.59523 | -67.04882 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e7d10d7-9588-3fac-a237-81c0ceecca46 | -8.59693 | -67.0607 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e426f527-b700-3945-aa4c-f319638ce41f | -9.17332 | -67.3192 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a2407cb-ae8c-336e-9cda-d5c3ee7c6bd8 | -7.7053 | -72.80733 | 2026-10-07 06:01:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 159d9021-8522-3f72-8dbf-3f03aa6e228f | -8.18466 | -70.45393 | 2026-10-07 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca336d62-4724-34ff-bdf6-e915a60a0e37 | -9.1429 | -65.29358 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 678e7091-d31b-3e25-a20d-4acd366e0c04 | -8.5981 | -67.05313 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26e684ed-14fe-3b25-9933-a55603490cd8 | -8.96937 | -65.44408 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e083fb24-8f92-3799-9c92-f8fc9f7ae4f9 | -8.33534 | -72.61295 | 2026-10-07 06:01:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 803aca64-5f87-306f-9103-d16497b16df8 | -8.91506 | -68.7906 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e697934-b23a-3147-8532-a88856bbf85e | -10.6182 | -60.48667 | 2026-10-07 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87fe4e68-da09-3433-b0c7-5fa96a0c69fd | -9.95506 | -67.19456 | 2026-10-07 06:01:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 471e8a03-bc8f-3488-bd4c-f74174ff279f | -8.63244 | -67.05326 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a8fb8c9c-aa94-3a13-b344-389d066d9fe3 | -7.88346 | -72.35402 | 2026-10-07 06:01:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 18.5 |
| d53566c3-251d-33f9-8560-505ed72d025f | -8.26812 | -70.8946 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ac6b4d0-cc51-3e4b-a81d-063228ef4546 | -9.5041 | -67.1673 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README122.md)
