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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6599091-8745-3cca-91de-939cc1954896 | -10.46406 | -44.37737 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ddbae8d7-8ff7-3c04-9a81-262ecdfea009 | -8.26211 | -45.06697 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36a9986f-f4bf-331e-b7cf-55182b19b18d | -7.53209 | -44.87159 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5744184c-063b-3797-a8f4-801121e4f4e5 | -11.50051 | -44.26817 | 2025-08-05 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e67bcc3-8539-334e-a7ff-1361fec80fe2 | -10.92625 | -48.36795 | 2025-08-05 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fae2aa6a-01f6-3ec8-aa22-2b8697094755 | -8.22931 | -45.05409 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e7f6e35-0781-3883-92af-8214ebc414e7 | -11.50439 | -44.26519 | 2025-08-05 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8edf978e-d730-3667-8970-1dcf81822ef7 | -17.35911 | -46.0876 | 2025-08-05 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ddfeda3-694e-303e-b783-8288be50d3c6 | -11.04396 | -47.61533 | 2025-08-05 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e659463-2d11-3b34-a968-9b727ef82e59 | -7.57342 | -44.89647 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63fd27ad-8662-3c89-891a-7404d8e111bc | -8.85509 | -47.60428 | 2025-08-05 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ddb0861a-1b66-3338-8b8b-831f1c805cb3 | -8.22871 | -45.05776 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bbae4cd-480b-3d34-bc39-c1f65ec5506a | -7.94782 | -43.8971 | 2025-08-05 04:17:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb34c226-0f35-3f10-b24d-8dc06177dffd | -9.39277 | -45.51014 | 2025-08-05 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d90f3b34-5cd2-33a5-8f2d-271f6320155c | -12.35135 | -46.05744 | 2025-08-05 04:17:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9470a31c-cc6f-32c4-b89f-e4853d7cc8e4 | -8.22531 | -45.05721 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4e30c70-7cbd-3483-8d42-da65b82ad04b | -17.87927 | -44.49284 | 2025-08-05 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c88f489c-dda5-3db4-8bfa-9c7816eecebb | -14.30374 | -52.01978 | 2025-08-05 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0969da60-d7e1-354a-8102-511245dc3370 | -7.94394 | -43.90007 | 2025-08-05 04:17:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96047da6-63f4-36fe-9d51-6cad46374278 | -8.2361 | -45.05519 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cf28771-835d-3c46-982e-ea970ceca61c | -12.58788 | -45.06934 | 2025-08-05 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7341a1b3-69a9-34ec-bf57-02d19001b3d2 | -17.21094 | -44.83627 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c4fe6e8-2bb7-3b82-9003-1f95536e59fb | -11.15573 | -49.70394 | 2025-08-05 04:17:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85d5d47f-fb46-39f3-b85f-655d6871cfd2 | -8.95285 | -46.74336 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2cd4c1db-c955-30cf-ae7f-55c698329b4a | -10.33392 | -47.82749 | 2025-08-05 04:17:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e79f7566-1ab5-3e56-8327-fe935e8328a1 | -17.37634 | -46.08684 | 2025-08-05 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 671b7b5c-c02a-383f-993e-19cb76f2026c | -17.35637 | -46.08335 | 2025-08-05 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81ce7deb-f24d-3646-a735-3ded26ad495c | -10.48753 | -51.86454 | 2025-08-05 04:17:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc1b85fd-bc01-3e62-8278-1ed4c8556262 | -11.92995 | -44.928 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dba6c8e8-756d-33fd-a00e-e265437e7b3c | -7.86242 | -43.86173 | 2025-08-05 04:17:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6c2c79d-7067-3230-ae83-df0651bafe4c | -8.22191 | -45.05666 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ed2f722-60e6-343c-9c47-211466cda6d8 | -17.21427 | -44.83683 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f08dbb4-88da-3be0-9d0b-3296ef25a294 | -11.9221 | -44.95566 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4fbd3ec-8309-37e7-93fe-567f95e2e879 | -10.45006 | -44.38624 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54c3457a-134c-3a0f-8ebf-befae96087f2 | -8.95938 | -46.74881 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 919e5194-1615-310c-9b45-36633abaf16a | -8.95354 | -46.7392 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3e6f77c3-a1bd-3262-88eb-281176ace7ca | -17.68489 | -46.64374 | 2025-08-05 04:17:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0c56823-c7a7-3078-95da-85425f9d5eac | -6.69249 | -44.35934 | 2025-08-05 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 349c41b9-bc21-371d-b98c-f2e29ab7bf90 | -10.77781 | -46.64549 | 2025-08-05 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 597248f0-3795-302a-afb9-ac1c48ccb715 | -12.54459 | -44.72705 | 2025-08-05 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04897414-4d2a-3fd2-add6-c4d65cbd43eb | -7.56549 | -44.88071 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad11067c-196a-34e3-8154-f0b91e6ca825 | -5.99003 | -49.91135 | 2025-08-05 04:17:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8224b573-c93a-3a91-800e-7538f1ca4268 | -10.45062 | -44.38271 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb3ef3f8-6858-3ee4-880a-3605d90897e8 | -11.75781 | -45.01313 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4969a029-5c17-300f-b955-5d47e98c9834 | -17.99398 | -44.3359 | 2025-08-05 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a35d2756-53eb-3a38-b333-42228009a921 | -10.46795 | -44.37438 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51ecaa15-cbeb-3090-b81f-792c806b67ee | -7.53268 | -44.86792 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36d7d486-1c52-3514-ac52-25b21b9aeb82 | -8.00809 | -43.2212 | 2025-08-05 04:17:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 4a2599f0-b1fc-313a-ba7b-29aec4e69c5a | -8.93978 | -46.73259 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| dcf733e7-b522-365a-90c4-6b1141d6f267 | -6.91442 | -44.20826 | 2025-08-05 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a3fcf0c-07e5-31dc-b344-d5fe60e76f50 | -7.48539 | -45.05273 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58b1710c-81e1-38f4-aeb3-5ef5f9174df4 | -10.47516 | -44.37193 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 690c5c63-3fa3-3d0f-b82e-2ebfe380b2a6 | -7.39085 | -44.64399 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c01b0f81-ef01-3aef-93d5-966058ee5fcb | -9.05324 | -45.06235 | 2025-08-05 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8aa323fa-6d90-3572-a447-e67d27d62a44 | -18.85414 | -40.45666 | 2025-08-05 04:17:00 | NPP-375D | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| abc9503c-a3d8-342a-a536-9f2647f34c45 | -8.25251 | -45.06165 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f03d0ce-5a98-3400-a205-4613c5082677 | -7.20109 | -44.49915 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7469e433-a5a0-33c9-af74-1ef7ef75a058 | -7.11367 | -47.84199 | 2025-08-05 04:17:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a24d34e9-9043-3994-a5ec-c7f42fddb05b | -8.21451 | -45.05923 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08cfb1e2-8b3f-31be-968d-68af1333fa4d | -8.94201 | -46.7415 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c438072-bd64-313d-be87-94573b2a34b5 | -11.78583 | -45.00277 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2df70ddf-a76f-3370-9860-fd8d9ee6ea36 | -9.16467 | -40.60029 | 2025-08-05 04:17:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 60645527-6284-3649-907c-e41659440852 | -11.27802 | -40.97755 | 2025-08-05 04:17:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5e480232-32de-38de-b4f2-98fc7c96c391 | -11.75557 | -47.54218 | 2025-08-05 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cfc7618-06f2-371a-87a9-af5dde18af63 | -10.91001 | -48.37009 | 2025-08-05 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8695dae5-167f-3867-af6e-d88826acf03c | -5.8889 | -43.73761 | 2025-08-05 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b47737a1-f255-3064-b92e-b5044617573b | -8.01459 | -43.13668 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6812f83f-097d-3dad-a6de-d7762869ea8e | -17.68824 | -46.64433 | 2025-08-05 04:17:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d97f05c7-091a-35d8-8c99-677c9f373606 | -12.48514 | -41.06359 | 2025-08-05 04:17:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9f9b6cb7-5bfd-3b2e-86fa-03083312582d | -7.0888 | -44.69635 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d6b831b-5f15-3a93-bd44-bb8941855f3d | -7.36855 | -43.7541 | 2025-08-05 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee661072-b372-3d30-8bef-57dadd56f3ff | -7.60558 | -45.30545 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9290eda7-a38d-385b-baf8-b5ec306f1aa3 | -7.39201 | -44.63684 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03391113-7d66-3ea2-b586-649331b0d7c8 | -6.73549 | -45.30783 | 2025-08-05 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e69dcb0-0fab-3510-bc02-2e4c31ff87c0 | -7.37432 | -44.16202 | 2025-08-05 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b9d5dc3-776b-35d6-9129-6825f81b8f1a | -9.39338 | -45.50641 | 2025-08-05 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92fcef55-563d-339b-ba6d-1f7cec6b3659 | -10.44673 | -44.38569 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e03e74c-9071-39ed-93e5-45833dfb2a29 | -7.47909 | -46.57711 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbfda445-42ac-3c81-91a7-28e2237801e2 | -7.56502 | -44.88386 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d4edf87-49e8-392d-b915-1643031c4e11 | -6.69452 | -43.07403 | 2025-08-05 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7ad2ba3-12ab-3bb0-bd49-c1d8b5bc0be8 | -8.35898 | -46.56109 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09b9c356-143d-3a98-ae6c-631cfd6117e9 | -7.38806 | -44.63982 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 889e8b4a-e374-3d58-8237-d59d4893e2f5 | -7.13759 | -44.08051 | 2025-08-05 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ded816e-b7f1-37db-b4bb-cd2352b1f37e | -6.01284 | -52.1545 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1772f72-17b6-36e0-b0d0-86da35123b5f | -12.22548 | -44.1942 | 2025-08-05 04:17:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f3e88ffd-66e6-3206-8270-af9303449ad0 | -9.64516 | -43.84704 | 2025-08-05 04:17:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| af75bfd9-1c86-3056-9a15-2bfeb6a3fcbb | -11.74503 | -45.00736 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a236e884-eedf-3cc9-a7a3-bcc82d635276 | -8.73989 | -46.43345 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a58b119a-3933-3537-966b-8f55e851f112 | -7.83416 | -45.23042 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e55c2476-3b0d-3288-9e90-7ffd7c24be75 | -8.95422 | -46.73504 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 35a4f425-a9df-3757-b674-62ca69629e6b | -8.11307 | -45.51777 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d9c4849-e8f8-3cff-b3fe-161ce6ddcad9 | -6.67722 | -49.79045 | 2025-08-05 04:17:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c7beb01-e43c-3eab-8878-0dee49a149d8 | -12.34455 | -46.05629 | 2025-08-05 04:17:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9df63ce-242f-331e-a77d-9f1dc46fa71c | -5.65646 | -42.57602 | 2025-08-05 04:17:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7db85ab0-ea43-37b6-950d-a90593a7c090 | -14.26335 | -51.98154 | 2025-08-05 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a4643e1f-f967-30b2-9573-cd414f070b41 | -7.52869 | -44.87106 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21e62f29-35fb-3093-b126-dd38cc2f0c9d | -7.99967 | -43.14502 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 3df38757-a7ff-3564-9f19-bebe39e14af3 | -7.57122 | -44.88859 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd59871b-aa34-3616-9f99-809fca85727e | -11.93542 | -44.95788 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae5bd24e-4d02-3f2e-ab34-64b9b04b6d5f | -12.64529 | -44.49403 | 2025-08-05 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README19.md)
