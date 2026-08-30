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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c176596-6121-3c60-9038-2848253993fd | -11.57464 | -44.03216 | 2026-08-30 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7c31db5-c553-3cbb-95b2-c308a94c0894 | -10.81824 | -45.33327 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5774a874-cb6a-320c-b576-221f9bc35e88 | -11.35038 | -45.16257 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd41aab4-ecb8-3ca4-8acc-40f1dc632d67 | -7.94337 | -44.26328 | 2026-08-30 03:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 92428332-b788-3c2c-a9cc-f2e8606994cc | -10.76622 | -44.85776 | 2026-08-30 03:38:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ce350e6-3c38-39b7-81ed-ba520636bb97 | -10.13051 | -45.70361 | 2026-08-30 03:38:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 17b72747-dbc3-3108-8eb6-496832271700 | -11.36091 | -45.16874 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d6175a64-35cb-3e65-b6c4-6fc53aebeef1 | -11.37026 | -45.43033 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8476ca32-201b-3dec-a67a-51db41641505 | -8.25213 | -46.50414 | 2026-08-30 03:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ea0fd4b2-97a2-387b-b7e3-7234eb30f736 | -8.20568 | -44.81828 | 2026-08-30 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 857510ce-1dfb-3b87-8735-2010355daaa2 | -10.40182 | -38.21813 | 2026-08-30 03:38:00 | NOAA-21 | ANTAS | BAHIA | Brasil | 2901601 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2dd53050-2113-3d18-b1c7-5f4236846a46 | -7.61453 | -44.85018 | 2026-08-30 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47d40c2f-9a1f-34a4-9f58-31a1c1dac2e0 | -9.76038 | -48.16452 | 2026-08-30 03:38:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9f95b2a-9e7c-3f58-bc4a-096ea3e23606 | -9.31732 | -47.62993 | 2026-08-30 03:38:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a33f2615-027c-3562-8e1b-bac4f691d549 | -12.92486 | -45.89759 | 2026-08-30 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a4a55e0-bbcc-3ef0-9917-6722224e3afa | -11.56876 | -44.03445 | 2026-08-30 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d323e6a9-0e9e-371c-bd84-1e9f423735cf | -10.81329 | -45.3279 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 66959a8d-c6ad-3b84-b2c3-c8327eef72d1 | -13.94004 | -43.99663 | 2026-08-30 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74a53a9c-e6e7-3940-ab51-01a10184bd86 | -10.81411 | -45.32364 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9168616c-3769-3e98-ae44-eac6b0ea1003 | -7.61529 | -44.84595 | 2026-08-30 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b76f3c6b-6e81-3b10-aadf-14fe3a256e8c | -7.61377 | -44.8544 | 2026-08-30 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c4fe7085-6829-335e-a555-f3611a8573f5 | -11.3448 | -45.14833 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c977e262-b820-3d41-a81f-7e728ee1de2c | -11.34317 | -45.157 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8a25a0fc-87b3-33a3-bdba-39544bdc47f2 | -11.24987 | -47.04824 | 2026-08-30 03:38:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed0f060a-41b8-3357-9eaf-6c82e8c3ee24 | -11.33837 | -45.15139 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9a9a8933-8f60-384a-bf1f-b6d31b280d1b | -7.613 | -44.85867 | 2026-08-30 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f72c1569-0374-3dcc-97d9-0932bb7e0bc4 | -12.43041 | -40.07688 | 2026-08-30 03:38:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9cccec1f-a68b-3bba-9910-03349f940ba0 | -11.53196 | -45.55301 | 2026-08-30 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a72af38-a26a-36a0-b45a-54c4b2e88296 | -11.3408 | -45.15157 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4d2ef22c-6776-31c1-8f9f-6fbbcd9e1bd5 | -11.20974 | -45.07442 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 703ec1f5-dc4c-3979-9660-578fc3c245c5 | -10.78784 | -45.33567 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 53f30510-b88b-3177-a675-f53bab563286 | -10.95103 | -43.03655 | 2026-08-30 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 367af628-a4d5-310a-ab0a-18e287826bcb | -8.14059 | -45.4733 | 2026-08-30 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d69efeda-518a-3b2b-84fe-c5fcdc227323 | -8.25171 | -46.50624 | 2026-08-30 03:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9a0764b6-f6e9-3603-b08d-6bd93a265467 | -11.23494 | -45.09573 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e43edda-a26b-320c-ae78-25f26c51966c | -10.14647 | -45.69786 | 2026-08-30 03:38:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 839822cc-3720-3f68-a90a-b6db5dd647c3 | -10.78866 | -45.33145 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6c6681be-121d-3010-9706-8ddeaa8f435e | -12.90526 | -45.87621 | 2026-08-30 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2951dca4-9ca0-3295-80d5-8ec22fea57c5 | -13.93504 | -43.99563 | 2026-08-30 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19fd7300-395d-34fe-8a4a-bc0f7ad9d413 | -8.14065 | -45.47571 | 2026-08-30 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6b1b3b4-c6b1-3332-8de7-aaa63845c5be | -8.25109 | -46.50968 | 2026-08-30 03:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 53445431-b130-3fa5-91b1-715b634c60c2 | -10.95207 | -43.03082 | 2026-08-30 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 1625676d-5ce2-34b1-9194-569a2b569ad4 | -11.34241 | -45.16106 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| da0d47c8-55e4-3e87-ae49-bad94c00ca3c | -8.13969 | -45.47822 | 2026-08-30 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee1c9fae-e09f-3b98-9a20-e45c29316e04 | -9.76619 | -48.16645 | 2026-08-30 03:38:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a12b24fc-bc34-3882-bab0-d7079c7e4235 | -11.34166 | -45.14722 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4deec7fd-a9c2-365c-abf3-1aa761476b18 | -11.53115 | -45.55716 | 2026-08-30 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 929286ec-df4a-3375-9487-0cd75e11c930 | -7.617 | -44.85761 | 2026-08-30 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a01e4512-156e-30ae-af8f-c6e406b725c6 | -10.94711 | -43.02988 | 2026-08-30 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 6344b518-deb8-3e15-ab59-5f3ed2e3bc3c | -11.34557 | -45.15717 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 236f8578-4c72-311e-96eb-24cfec3aa7a3 | -11.36931 | -45.4313 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3ffc488-02a2-337d-8c12-5eccb577ed29 | -11.20895 | -45.07856 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fb67aef-0e78-30ea-8c1e-566db155b2d8 | -7.95401 | -44.26901 | 2026-08-30 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ab776db-c507-3255-827e-e8ef51384850 | -11.33998 | -45.14284 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 484c160f-2c4c-31b2-866e-bc1309affa37 | -11.34728 | -45.14847 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52927aac-018f-392a-ac8e-2376d3b062f3 | -13.93982 | -43.99495 | 2026-08-30 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27de879b-1270-3368-8899-63afd0611d9e | -12.42893 | -42.88365 | 2026-08-30 03:38:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fd19d7dc-fb6a-398f-b269-f681b4852ef2 | -12.92518 | -45.89434 | 2026-08-30 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d66ea31-1e19-3f9a-bb32-3cb710e83ecb | -10.95703 | -43.03176 | 2026-08-30 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| b8b86b84-6c5e-38e7-a1ac-a731a026424f | -10.95599 | -43.03749 | 2026-08-30 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 18fe8a42-72a3-3ceb-ad28-1297ed278838 | -9.21295 | -46.06833 | 2026-08-30 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0d1f3831-8adb-3558-8d91-4ef975364bb2 | -12.08268 | -47.19421 | 2026-08-30 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7de59885-21c7-3501-9d0c-207ae06f2bd1 | -7.61193 | -44.85207 | 2026-08-30 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f541e3b-ef2f-371f-9e5c-2fb544595961 | -12.92438 | -45.89842 | 2026-08-30 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8a41193-2b8e-3e99-ac55-4d097ac7d996 | -7.61271 | -44.84787 | 2026-08-30 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b75cb2e-304e-321d-a7be-5a53b67f444a | -11.22033 | -45.0802 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 375c6c8e-75b2-38fb-bf0a-3e96b0da5888 | -10.75989 | -44.86045 | 2026-08-30 03:38:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e333f946-1f58-374a-8d23-c7e1e4fae873 | -8.13971 | -45.48066 | 2026-08-30 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 10b8ccd9-6677-3c98-894d-6e6a5b20f3df | -12.90387 | -45.881 | 2026-08-30 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 550d4bef-34f7-3356-977e-576e91307cc0 | -11.33917 | -45.15987 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0033c7e1-52e5-361a-bc01-468a2b06152b | -15.6025 | -39.87596 | 2026-08-30 03:38:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 46bad950-a240-300e-a48e-f97f6e221042 | -11.34639 | -45.15302 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 471077ce-44e4-3123-afbf-4711e2a2671a | -11.36015 | -45.17267 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5edd4038-3f71-3e10-9d54-82072907ea32 | -10.80916 | -45.31831 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4d37731d-3ddb-3ec2-be27-1aee633850b0 | -11.33998 | -45.15577 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 894b7186-8578-3c2f-a33a-462f6f245111 | -9.21206 | -46.07306 | 2026-08-30 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| cdd9c304-ab01-365f-b503-d843780ef482 | -11.34478 | -45.1612 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c66d8da2-7b85-312a-8366-30def4168c86 | -11.26126 | -45.06548 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 701753c3-ad40-3060-84ca-811af62156b4 | -7.9464 | -44.26447 | 2026-08-30 03:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ce4bacd6-eae4-3816-8e6c-5b654a16964c | -9.21792 | -46.06682 | 2026-08-30 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 6e94d9b7-23bc-36a5-8b88-74f30af6930d | -10.78948 | -45.32727 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 532963d8-eb0c-3d9f-889b-67ed559ad659 | -11.37006 | -45.42739 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 154b3911-47d2-35c3-9a30-c6021b363344 | -11.21052 | -45.07035 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 43a2d00e-4ecb-3476-b9d9-fce52ff1f602 | -12.90443 | -45.88027 | 2026-08-30 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4952765f-a374-373a-8d19-89445b82c60c | -11.23988 | -45.10053 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f39a4540-1482-3287-ba17-ab0a43cd9212 | -7.61858 | -44.84915 | 2026-08-30 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bfb15c4a-6c03-3b71-904c-60876c740d5c | -13.35724 | -46.92131 | 2026-08-30 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33402b19-b611-3937-9ca7-a79d49fd810f | -10.95311 | -43.02511 | 2026-08-30 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 7cd3699d-a912-334c-ad60-408f3ec06b63 | -10.81906 | -45.32898 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f6dddcde-4d4d-3262-a0b5-ef23290dfc5a | -11.21463 | -45.07946 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afe43cea-583e-3823-8681-1f347beb1363 | -11.35118 | -45.15847 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90493e9a-d629-34cf-a1fe-01d3d18ec337 | -7.94569 | -44.26846 | 2026-08-30 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 55cbc283-a81d-3ea4-bd06-3920efea6724 | -9.21382 | -46.06369 | 2026-08-30 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5e204241-bb03-3247-b258-ee12d03881f5 | -11.34959 | -45.16662 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8369e9f8-ff5a-3a4d-9c80-530cba90e4e3 | -7.61778 | -44.85342 | 2026-08-30 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a96463e7-ba8f-3580-acac-90160b3efc38 | -12.78635 | -44.61306 | 2026-08-30 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebef090c-991e-3ad0-9692-d39d28b03caf | -14.19184 | -43.57271 | 2026-08-30 03:38:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5a84f3e7-d9bd-3ade-aa7a-31478123ee8a | -10.14551 | -45.70274 | 2026-08-30 03:38:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 216afe0f-c3ac-3c3f-8149-088363489a33 | -11.21126 | -45.06645 | 2026-08-30 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f9ca0d28-8994-3d68-9464-0d89b9d53e14 | -9.2117 | -46.06573 | 2026-08-30 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README24.md)
