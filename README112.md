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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 230771f7-cedb-355b-8c05-61b8de92b39b | -3.46132 | -60.59144 | 2024-09-27 05:25:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 50fcf4c4-8c1f-383f-9c5f-abce486e2598 | -3.38764 | -60.65112 | 2024-09-27 05:25:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8f86d12-f27a-3bea-bb6a-e8b4e288ffc7 | -3.08765 | -60.46238 | 2024-09-27 05:25:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a06563c-2aac-3d07-b9ae-0a8ce1da84b0 | -3.08486 | -60.45838 | 2024-09-27 05:25:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4f5c18d-0aeb-3683-a9f6-99acb1de895f | -3.08432 | -60.46186 | 2024-09-27 05:25:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e7b684e-1b41-38e4-8440-62cf8c7a3bb3 | -3.08175 | -60.71706 | 2024-09-27 05:25:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac27d687-b7f8-3159-8bf8-4813562ff660 | -3.05544 | -60.77663 | 2024-09-27 05:25:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1ea1b5a-8055-35ad-8c85-56e69688a8d4 | -2.97896 | -60.98351 | 2024-09-27 05:25:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 130251a6-5afe-34e8-84a8-2484482d59e2 | -3.64646 | -60.53838 | 2024-09-27 05:25:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 603f79ef-7c31-31f1-a901-026fa87f6472 | -3.64592 | -60.54187 | 2024-09-27 05:25:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6051377d-bb05-36b2-8e77-5428c8e10ea4 | -3.64368 | -60.53438 | 2024-09-27 05:25:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f437dcf3-8b53-3d38-ba9b-9a1e846d0cfe | -1.50077 | -61.59198 | 2024-09-27 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8e417b9-b69c-3a19-a3f2-539e2ca7482e | -1.50022 | -61.59544 | 2024-09-27 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a264a0fe-f006-30a7-adac-95768fad24ba | -1.49968 | -61.59892 | 2024-09-27 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f701035-58b0-3b87-b7fe-6a6a8c9320d6 | -1.49745 | -61.59146 | 2024-09-27 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ebef4aa-c288-3b5c-9ed8-6207eef4fc6a | -1.4969 | -61.59492 | 2024-09-27 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 46965992-d29a-3212-862b-65f7f1a9295f | -1.49636 | -61.5984 | 2024-09-27 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ec606204-2cfd-3443-b645-9a4f35c9975e | -1.49358 | -61.59441 | 2024-09-27 05:25:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f753260f-5eb4-3f5c-8fce-d1f500332024 | -3.20243 | -61.50801 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ebc6faf1-40de-3a56-91d6-faa4155b9851 | -3.18348 | -61.56161 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 27f9461c-804e-3292-86bb-09f442811401 | -3.16742 | -61.53444 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ead0e67e-5893-37b0-8164-6e6e2128e7a8 | -3.02602 | -61.67826 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c93dfaec-120a-3925-83ab-1328f375645a | -3.02548 | -61.68172 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5085a8b9-f2a7-3137-b8b0-e760ba3ba2fb | -3.02494 | -61.68517 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2442f075-7a48-3c2b-bf14-d0d406657444 | -3.02439 | -61.68861 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7f23649-e148-3beb-a8a9-7b20865ede52 | -3.02385 | -61.69207 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 369f2123-644a-3a93-9a68-5b957146c53f | -3.02217 | -61.6812 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01806fe6-0c43-3efd-af68-14d9f1762227 | -3.02162 | -61.68465 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 431cd6ff-d437-323f-b2c1-008444c4b527 | -3.02108 | -61.6881 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 988c1bfd-cf8a-3afd-b1fd-fa1b9678182d | -3.02054 | -61.69155 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ee5cdb93-53e1-3da8-ae65-96412dc283db | -3.0194 | -61.67723 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46046c3f-ea9d-321b-beee-6f41b49b1285 | -3.01777 | -61.68758 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abbe1175-55af-3c21-a70d-b92fa69e674f | -3.01723 | -61.69103 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c39400a4-1df3-39fb-96c7-d645e8c06940 | -3.01668 | -61.69448 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95484d68-fdac-3536-b313-ae499b2b53f4 | -3.01554 | -61.68017 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c8230e9-0f8e-3d65-baf1-5dd93fa2a27e | -3.015 | -61.68362 | 2024-09-27 05:25:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd625f5b-dd74-365c-9202-f5b87121015e | -11.21096 | -54.7597 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2cd5906-ca48-3f6b-80bc-27089388189b | -3.86408 | -65.15774 | 2024-09-27 05:27:00 | NOAA-20 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 022e3ef1-4d94-3d09-92c6-e80f43235064 | -9.39535 | -66.58276 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c736a08c-2761-3ab5-ba4a-90dc0a0d9350 | -9.33815 | -66.6012 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5c0d0ec-f162-3f45-b65a-0f7cceb08aff | -9.33794 | -66.59914 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2054f102-110c-3be9-abb2-841551d87b36 | -9.33439 | -66.60056 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09d13718-3355-3b5c-bcaf-9c264aae8fcd | -8.82075 | -66.74462 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a18ee760-3bd0-3c42-b276-2b3390cd4d94 | -8.80303 | -66.664 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1c718ed2-4802-3e3a-bb1a-3bf01c3f95b7 | -8.80224 | -66.66866 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8a45cd88-754c-386b-84f4-d243aa6fa9fd | -8.75975 | -66.87195 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0446e37d-fa92-300f-8a7e-bfdaed81f83c | -8.75508 | -66.87614 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4f53d62-935f-3168-a2a5-ed135387ee31 | -8.71526 | -66.96311 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea79e3f2-99ad-3b74-9f54-14ef8459a07b | -8.71445 | -66.96801 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c56733b-3adc-3d18-8e42-b1676819fbd2 | -8.71139 | -66.96244 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7a0246ea-9190-3fe1-9c82-603d7b390dab | -8.71058 | -66.96733 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c2b8dd1d-f425-3b21-a353-c04af30da266 | -8.70752 | -66.96177 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7fba4123-6147-3263-bac4-8b4a7fb5999a | -8.69956 | -66.98563 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d09b7d4f-83fc-395b-98a5-40d3ceb75632 | -8.69568 | -66.98496 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86eb5773-5b94-3f48-8e90-c7b9a76332d4 | -8.69486 | -66.98988 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0cc1636e-7c2e-3cbe-a30f-e263e9162149 | -8.66966 | -67.021 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fb119bc5-56ed-311d-888d-898d0c1cc52e | -8.66577 | -67.02032 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6ea6be2-d109-34d9-b066-d8b42ef58737 | -8.66188 | -67.01965 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42f4a3ae-d236-3759-8de9-090b002961da | -9.17153 | -65.81202 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5480043d-a94e-3790-8d6a-0ab2b6701411 | -9.17136 | -65.92474 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96fe0e5e-3ed1-3f4d-87bd-c8014ddcb9b5 | -9.17083 | -65.81622 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d028d75c-7cd0-3ff8-9361-0643aeecd970 | -9.98302 | -66.851 | 2024-09-27 05:27:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac79ad43-6924-3a18-a5a5-79204d9c5d4b | -9.97924 | -66.85035 | 2024-09-27 05:27:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7406250-6d4f-38a6-a0ec-02eb7aa7f012 | -9.84881 | -66.42621 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 012dde56-12e7-3976-b347-2e871260b2c4 | -9.69946 | -66.85229 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8705efb6-62de-3017-b2b6-74ccc79177e1 | -9.69566 | -66.85165 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 258adb60-80f0-375c-904c-d57a311532e1 | -9.57494 | -66.64693 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45a1b190-9321-3aec-9cd7-b8e1590175e2 | -9.57416 | -66.65153 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10982305-bfd2-3071-a9cb-a3d23e132659 | -9.4566 | -66.54409 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 956099ed-3241-3292-870f-e26e2f02c6cb | -9.45535 | -66.54619 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a80b200-921d-3f70-9dac-08069a73ea14 | -9.45286 | -66.54346 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16a39005-0345-3673-a39d-1dd3bd6cee1d | -9.45161 | -66.54554 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d414971f-592d-33c3-8c6c-5624108c6619 | -9.44912 | -66.5428 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05dd1064-d82f-3944-8a77-0573f4af6ccb | -9.44835 | -66.54736 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4aae309a-de77-3365-9e00-7712c5668b36 | -9.44787 | -66.5449 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44af9c19-cf99-3d7c-a7a3-8e78295bad02 | -10.01716 | -66.97253 | 2024-09-27 05:27:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76b2237c-7b3f-35a3-8121-060682fe89f9 | -9.55781 | -66.03651 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59e96964-fc7d-3bbf-8c02-885052755dbc | -9.55562 | -66.02735 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 71a6143c-d02c-3b49-b97f-38d1030a01e8 | -7.65044 | -67.19538 | 2024-09-27 05:27:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 975ea17f-ccba-3105-8ad9-aab39128b04a | -7.64704 | -67.19119 | 2024-09-27 05:27:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 823fd9fc-21d5-3a71-baf6-beca8c8e47fc | -7.64645 | -67.19469 | 2024-09-27 05:27:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da768311-9e31-37d8-be3a-381bcdcfd6d9 | -7.64586 | -67.19817 | 2024-09-27 05:27:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7c05da3b-8145-3422-8b64-8f18e47b1f8f | -9.19112 | -68.29616 | 2024-09-27 05:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2fe8a59-726f-3838-95d2-547212f7f12e | -9.19044 | -68.30006 | 2024-09-27 05:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 532b979b-b543-3ab6-83b0-2ca48511d0bb | -9.18693 | -68.29545 | 2024-09-27 05:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b36753fa-6539-3f81-84d2-d8d42ab7ecf3 | -9.1474 | -68.37302 | 2024-09-27 05:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f5f4b75-bc82-3b3d-bce0-5bbc5d1231e8 | -9.14671 | -68.37695 | 2024-09-27 05:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4baad9e8-f368-31e6-8e7d-c8526eeee063 | -9.14362 | -68.36945 | 2024-09-27 05:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7df85d71-41eb-3e38-9a6a-f27361a39b24 | -9.14319 | -68.37228 | 2024-09-27 05:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 128ed5a1-c2d8-3fdd-8c60-354acacb999e | -9.14296 | -68.37338 | 2024-09-27 05:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c43e8aaf-9262-3818-af63-2f33cf108b7d | -9.1425 | -68.37621 | 2024-09-27 05:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 677c7a31-55bc-3a62-9e82-39600d4f4311 | -9.14229 | -68.37733 | 2024-09-27 05:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 817543bf-2a0c-3609-b6c1-516748a54a46 | -9.12987 | -68.39944 | 2024-09-27 05:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62189d76-79e4-3148-af2f-0de2d46b4941 | -9.12565 | -68.39873 | 2024-09-27 05:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1cc6bc2-7902-30d1-9114-8e8f74974773 | -8.99946 | -67.37605 | 2024-09-27 05:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9307cad4-f137-320d-a338-c576c9370779 | -8.99858 | -67.38117 | 2024-09-27 05:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 04e404e7-40ef-31a1-b65e-01ece8ecdc1b | -8.99551 | -67.37536 | 2024-09-27 05:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 85908bc3-c183-3422-a4b5-dbd4b989ec3d | -9.43268 | -68.80396 | 2024-09-27 05:27:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ee7285f-23c2-3df0-ad2f-3dd5cdda57e9 | -9.36666 | -68.73765 | 2024-09-27 05:27:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f149aa81-3ea1-31f9-be00-892c6c9fa7c2 | -10.47015 | -67.76665 | 2024-09-27 05:27:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README113.md)
