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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 744b4f4b-092e-3c88-b769-4f64aa8659ff | -2.11563 | -48.28547 | 2024-11-02 03:47:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4938b70e-ae6d-3cba-a9a9-dd513e98b6f8 | -2.11464 | -48.29121 | 2024-11-02 03:47:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 38d78286-c174-340d-8c8f-e7e350a82f6c | -2.11246 | -48.28399 | 2024-11-02 03:47:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| eb3fa733-e6b8-33cf-968b-255ce3152829 | -2.11151 | -48.28973 | 2024-11-02 03:47:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6940255b-556a-3eb7-9edc-71dbf4faf577 | -1.8459 | -47.45313 | 2024-11-02 03:47:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42df2b74-ec51-3def-8df5-3cb2a90fbdc6 | -1.84503 | -47.45827 | 2024-11-02 03:47:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7d588de-e1ca-3e4e-a187-6af4ed7737de | -1.84434 | -47.45145 | 2024-11-02 03:47:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13698964-27b2-3b1c-ab47-e0fbfe22ec06 | -1.8435 | -47.45658 | 2024-11-02 03:47:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf6cc4c0-34e2-3b86-9114-a47ce8d5dda6 | -1.83953 | -47.45208 | 2024-11-02 03:47:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3b71a19-103f-394c-9092-0077720aba5c | -1.77367 | -47.95903 | 2024-11-02 03:47:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 99ea12b2-8782-37fd-9d8d-5dff077161a9 | -1.7727 | -47.96482 | 2024-11-02 03:47:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6113006f-f598-30e5-af05-3f903970f41f | -1.76896 | -47.95716 | 2024-11-02 03:47:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5086743b-48c6-36d7-bb3d-b4ed5d80500d | -1.76801 | -47.96305 | 2024-11-02 03:47:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 384d4882-d779-3b73-a88c-b0140be2498e | -1.76711 | -47.95784 | 2024-11-02 03:47:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c8ce7310-d9f3-3d6d-8653-4599b236da0a | -1.76613 | -47.96366 | 2024-11-02 03:47:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 25d63f8b-4b5b-3f6f-8024-385df90e9170 | -1.61136 | -47.21903 | 2024-11-02 03:47:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f49cf756-5813-3b09-a38a-b787cef05c47 | -1.60505 | -47.21806 | 2024-11-02 03:47:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a78fd8b-f936-3a7a-a44f-93856b2f81fa | -1.06417 | -48.25938 | 2024-11-02 03:47:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30845cc9-576d-3df1-8465-db5aaa123510 | -0.94502 | -47.55725 | 2024-11-02 03:47:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6afcec9b-6622-3dd3-9656-1d377407bcb5 | -0.93853 | -47.55615 | 2024-11-02 03:47:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0b158d5-620e-3ea3-846e-a31f41e7d36e | -3.45811 | -47.66639 | 2024-11-02 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a3cf9ebe-4776-3c0e-a182-ac82c714cc3e | -3.45723 | -47.6715 | 2024-11-02 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9cfcdd77-e94f-3092-b043-5cb55007b54c | -3.08661 | -47.78247 | 2024-11-02 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdcf7d26-11e1-3a3e-8fae-bbdcff967db1 | -3.08484 | -47.78326 | 2024-11-02 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 263da53f-f3c1-326d-8850-c841418e4559 | -2.91492 | -48.61432 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14e890d1-5a7e-30c6-9d98-a61a6e5dc149 | -2.91387 | -48.62032 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9d5a7b5-6c72-31b0-8e49-bef37de88bbc | -2.91204 | -48.61595 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be2eb600-be51-3e70-be75-9c73c3d75d95 | -2.91173 | -48.63255 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 73edf8ef-2479-37f6-acf1-51c97395a24f | -2.91102 | -48.62202 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5adfb9c-3c12-3e88-af37-faf73e2cd4ea | -2.90999 | -48.62814 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1c7df75-5f8b-3690-bfa2-7e9d1e592f11 | -2.90896 | -48.63428 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff6c5b0a-2ed6-32ee-a73c-71cec25dcee2 | -2.90715 | -48.61917 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f742a455-2a6c-3b55-b87a-f39c0e967c2e | -2.78533 | -48.57623 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 583cf23c-07c1-322c-86c0-f457f22b6534 | -2.78431 | -48.58226 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fa1f8bc3-9b3f-38bf-b305-30fa778974c5 | -2.77961 | -48.56919 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 302d0877-64e5-3277-b3be-f690593d0157 | -2.77862 | -48.57507 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b2833a8-a688-3f45-afc5-e6372241037a | -2.7776 | -48.58103 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef8eec54-dfda-3422-8dbd-3937d7bad3d3 | -2.77665 | -48.71612 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cac8a6e0-950e-3082-ac81-fc3260305d28 | -2.77559 | -48.72216 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 41854994-c8de-352c-9f30-6be27e31cf83 | -2.77545 | -48.71664 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66cb2872-1cc7-31ad-bde9-50b1638c232f | -2.77451 | -48.72831 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| feaa82b9-e825-3fd4-9672-c4c89596638f | -2.77442 | -48.72274 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2fa562e2-dad0-395f-8941-2ce87e2418a6 | -2.77319 | -48.6478 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc9c7b40-e7cf-3d0e-ad35-9437d4240360 | -2.77191 | -48.57384 | 2024-11-02 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92cbf423-3105-394b-8a41-7f6efe4776e4 | -2.62973 | -47.96436 | 2024-11-02 03:47:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b3c1357d-ad50-36a2-890d-936f3f147cf3 | -2.62945 | -47.96841 | 2024-11-02 03:47:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0bc8f941-795c-3bf8-b3c8-713bca3d5f6e | -2.6288 | -47.96981 | 2024-11-02 03:47:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4095cab9-b268-342a-b7a6-64f62eadfd4a | -2.6216 | -48.33051 | 2024-11-02 03:47:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f99f4d19-e8cf-351e-ac08-91d52b3931e0 | -2.62062 | -48.33635 | 2024-11-02 03:47:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad00afb0-16d9-3684-bd0a-340c46992833 | -2.45917 | -48.49945 | 2024-11-02 03:47:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26cb6ef1-cf20-3cd3-9c47-481b0d357fdd | -2.45712 | -48.846 | 2024-11-02 03:47:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e1a6e07-cac6-3e89-bc1c-12c05d4f546e | -2.45027 | -48.84479 | 2024-11-02 03:47:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4856864-8139-36d0-8b4b-95bdcc8e3e63 | -2.40443 | -48.57613 | 2024-11-02 03:47:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19ea75b9-1457-324b-919d-23a23aa1bdbe | -2.40252 | -48.57911 | 2024-11-02 03:47:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31234dc2-ed68-328a-a186-69368def6b29 | -2.4015 | -48.58523 | 2024-11-02 03:47:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b01cc38-56b3-36bc-ab9b-90659991e589 | -2.36762 | -47.62874 | 2024-11-02 03:47:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6e0add91-88ce-3a19-b6f5-d2ba34647abc | -2.36682 | -47.62815 | 2024-11-02 03:47:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b809fc2a-5879-3de1-a513-a9b97095b627 | -2.36675 | -47.63389 | 2024-11-02 03:47:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 887c138f-3f3c-3db6-904b-fa8e8f70fb93 | -2.36598 | -47.6333 | 2024-11-02 03:47:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8bf44337-0a43-3672-a9f8-7d7eee7796fc | -2.36122 | -47.62776 | 2024-11-02 03:47:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63645f5d-152c-3edb-9190-be797b82f63e | -2.36034 | -47.63292 | 2024-11-02 03:47:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd7e43f3-82a8-3c00-90f4-d30df30d4f29 | -2.35957 | -47.63231 | 2024-11-02 03:47:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c621c1ff-f39e-3b95-a44b-e94173c2a79e | -2.35247 | -48.42346 | 2024-11-02 03:47:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6df65a39-3c5a-3cdf-8738-3182a6f939ca | -2.17304 | -48.72886 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a77c8897-8663-3823-9879-f888b7ca58f9 | -2.16423 | -48.73935 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aef7007d-5d48-33e4-a47d-99518034e7e8 | -2.1481 | -49.12692 | 2024-11-02 03:47:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78c6a108-1352-38b0-aa40-ba70cbcc7d21 | -2.14801 | -49.53591 | 2024-11-02 03:47:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2445a1e-68d7-3f03-993b-54a4921d8091 | -2.14208 | -49.52747 | 2024-11-02 03:47:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7eebf31-1133-3518-bb43-c8b8771687f8 | -3.51012 | -49.94125 | 2024-11-02 03:47:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdc15c53-cc6f-37d6-8445-06f30fe0ba10 | -3.50292 | -49.94003 | 2024-11-02 03:47:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec5ae535-0aad-3f9f-b5bc-fd722dad6371 | -3.45003 | -50.15673 | 2024-11-02 03:47:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17befd70-3e0e-30fa-bead-041870d09ba9 | -3.04831 | -49.47322 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2744289c-957a-3519-8270-98a01bc52a41 | -3.04717 | -49.4798 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86021a1b-e122-3212-b308-67d957398ddd | -3.04013 | -49.47851 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 009d3c10-7a54-3505-b7ca-243e9375a14a | -2.93855 | -49.34438 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a34e892f-0c34-3e48-b0f7-3b7612ef791c | -2.93603 | -49.42542 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8141fdff-8aa9-323b-ae8f-ed3c8ef1f9f7 | -2.93487 | -49.43216 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1f6def76-7111-37ac-8eb1-e7434999ed15 | -2.92896 | -49.42433 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 250a5b9b-73f5-3f74-bf38-56d9bea479dc | -2.86634 | -49.38667 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a3c06a4c-958a-3b73-81f4-cb0bfbe094e9 | -2.85929 | -49.38551 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6868e38d-7702-303b-8191-91d0bcee44e9 | -2.84523 | -49.38297 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 81e5cef3-4a9b-31ba-9df5-8c09255bd94e | -2.81837 | -49.76291 | 2024-11-02 03:47:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d7e9138-e675-361a-96db-f190e7464414 | -2.81719 | -49.76959 | 2024-11-02 03:47:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70460bca-2691-3748-8884-56e5f6d00d36 | -2.81661 | -49.76435 | 2024-11-02 03:47:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b79c0863-147c-3014-91c4-efdd53257128 | -2.74618 | -49.49204 | 2024-11-02 03:47:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bcd7dbab-ed1f-34b2-aece-53afe7893577 | -2.74547 | -49.55941 | 2024-11-02 03:47:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cf1dd8e-a9c7-35c7-88cd-01b2c4cbec4a | -2.74235 | -49.55511 | 2024-11-02 03:47:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a77b23f-81f3-3e03-96d8-3d820510f4b2 | -2.74113 | -49.56203 | 2024-11-02 03:47:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 977b6ba0-4d45-31eb-b76e-048d5ff55b00 | -2.73835 | -49.55816 | 2024-11-02 03:47:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03166100-204b-3b1a-a04e-62eb61f8b060 | -2.71338 | -49.28061 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ae1ca64-311a-3c2b-83c9-50cdd2092413 | -2.71224 | -49.28719 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44384cd2-d61a-3223-b5c6-ca03bda23a60 | -2.70521 | -49.28609 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a829f9e-2350-3bc6-b345-6bbb76ee3717 | -2.60951 | -49.15527 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d419ffc5-70ab-37fd-85b5-dc6646b3171d | -2.60842 | -49.16175 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be121f9a-2ff0-3180-961d-11797006109d | -2.60803 | -49.15544 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbd23af3-0f8c-34b9-b416-05d015ec3e4a | -2.60689 | -49.16193 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34a80ee2-4ba0-3038-bb82-073f0b56a480 | -2.60448 | -49.81968 | 2024-11-02 03:47:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2eb4d82e-b630-3b74-9388-7d2535f55bb5 | -2.60314 | -49.822 | 2024-11-02 03:47:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0c8a5f47-7ae3-313d-9b65-02cdfa1fd9d6 | -2.59726 | -49.81836 | 2024-11-02 03:47:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dadd5b98-9b85-3da1-893d-228719ba0f12 | -2.59594 | -49.82582 | 2024-11-02 03:47:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README25.md)
