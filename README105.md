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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77f542ae-655d-3ebb-945d-2780b5672288 | -1.1671 | -53.68105 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4de8631-220a-3dd8-8c9c-ab932a6808eb | -1.692 | -52.44341 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc4bf345-43c3-38cd-94a6-11572c455d61 | -1.71964 | -52.77261 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b8096c6-54c5-3bcd-a584-51a53537fc40 | -1.68982 | -52.46128 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b5a94a3e-7b3a-3acf-b11e-8e5e4a39b4ed | -1.63032 | -53.87219 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c99a60b5-5bfb-32a1-b8a5-d22cbe9f666c | -1.70451 | -52.64237 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a69d08b0-8910-3f8d-8126-a3869a06ca10 | -1.35837 | -54.66086 | 2024-11-29 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a18dc785-0b73-3477-a284-418cf279b3c3 | -1.69677 | -52.4623 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| adec1de7-762f-3347-b478-efa51ca46c7e | -1.5991 | -55.43795 | 2024-11-29 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a077793-9014-3b4d-b320-f07e95cfdc12 | -1.44544 | -55.16119 | 2024-11-29 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58905da7-de8b-3689-9cc9-1d70ff228857 | -1.68908 | -52.46297 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b697d175-2faf-3121-8402-6ac5793d5c42 | 1.24867 | -55.99209 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5833029f-d33e-3afa-b89c-0749a91465ec | -1.71377 | -52.76538 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ea864c75-cf48-3f89-b9ac-a1dffcf4cef3 | -0.29508 | -51.74934 | 2024-11-29 05:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b3cd3509-1850-35f7-a459-b6b40f66e23d | -1.06665 | -53.64142 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da61dc7b-fa36-328d-910d-9052cc923e79 | -1.34961 | -55.01196 | 2024-11-29 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65c978ca-8a09-3662-a4d3-4dc4da75f91f | -2.25429 | -53.74548 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e949ed73-786c-3e93-b261-aba8df64725f | -2.05446 | -56.07825 | 2024-11-29 05:44:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7f971098-50d5-32f7-827f-4dc8a0b6b9c8 | -2.0539 | -56.08194 | 2024-11-29 05:44:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa6339a5-dc42-3a9a-8071-493ab6b7fcf7 | -2.25345 | -53.75089 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a170e02-2f54-3c98-b4e5-71b772bce586 | -1.1615 | -53.67493 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6dee6d08-f6f1-3f67-89b5-53de57552dd4 | -1.95081 | -52.96375 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc528d79-b0ce-37cd-a167-0efeec879c26 | -1.59716 | -52.28589 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 429b3d21-3ed5-392d-b72d-c1b62d1e206d | -1.68699 | -52.42928 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c386e3a3-f892-3549-a6e0-f4d5ba47b43c | -1.70492 | -52.45205 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| eef34f80-7a40-3056-b9ae-7f28fd11d509 | -1.62433 | -52.37782 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b047692-9ab5-3e53-bf25-fafbb0ee75ee | -2.05947 | -56.08277 | 2024-11-29 05:44:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2af3769-6984-3ae7-b813-ae5b08a35254 | -1.49537 | -52.43847 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5b004b92-3c5f-3a6c-b067-c1d0f4d3fa43 | 1.20669 | -55.99307 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75d053bb-6886-3abb-a17e-ef040192f8df | -1.58245 | -53.84345 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| d059d1a7-f761-3c72-a5ee-25fc62962bd2 | -1.06813 | -53.64168 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d99ae1a0-f2ef-3dc8-b45a-e48c7b2edd2e | -2.26241 | -53.4752 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 33628fce-d5ad-3b3f-89a9-e725e8b4c25a | -1.5953 | -52.28531 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 680b4092-10e0-358b-b86b-75484f87e6c4 | -1.7133 | -52.63076 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94c42087-b96c-3cc3-9994-7fde99011338 | 1.29728 | -60.42082 | 2024-11-29 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b2548bf-40cb-3823-bdf6-ca1d7125f0c6 | 1.21009 | -55.95679 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6395d74f-16eb-39c3-91ac-ae80a134a309 | -2.58393 | -54.24273 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60755bd0-25d3-36ab-a525-6f13c971bebf | -1.52506 | -55.37851 | 2024-11-29 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f5f4e37-77b7-35fc-84af-65d8850ba7d5 | -1.94988 | -52.96971 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f4d05b65-d923-331d-baf5-ff2fe0df0cd8 | -3.22679 | -54.17968 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 052f6614-ad18-3005-8911-d309aff8ae97 | -3.18996 | -54.32942 | 2024-11-29 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0657a49b-6787-3aa2-9994-a1c3686de99b | -3.33354 | -53.22041 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94cfa9d8-66a5-3c2c-8630-b2daf0b95260 | -3.22552 | -54.17822 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8fcf4b24-b786-3b74-a200-b50819fff2bf | -2.96148 | -53.72223 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a984da04-b15d-31f8-9e80-44a7e84cf73e | -4.51337 | -59.81707 | 2024-11-29 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e45c516-ddf0-36df-bb5c-a500892752cc | -3.02938 | -54.02412 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d105d42-36ce-32a5-9202-9daf9cfae6c4 | -2.98392 | -53.29538 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 690462f2-6095-3e11-9003-e5873e90dea3 | -2.62292 | -54.30407 | 2024-11-29 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff7e8e39-c1e0-3d1d-be5e-9394cbcef578 | -2.75614 | -54.12368 | 2024-11-29 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ca38678d-5031-3f80-a7b5-302a19db4d5d | -2.7569 | -54.11852 | 2024-11-29 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73fabc90-02d0-3af0-83fe-7826633ccc9f | -2.97815 | -53.28789 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 0acb8245-4cef-3e2f-b4fc-6a4fc9577915 | -3.21965 | -54.18398 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4e468b48-d73c-3903-8c4d-763cd4851984 | -3.57311 | -53.02879 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16edd4c8-d41e-30c7-b24c-4a79bfb96765 | -3.3353 | -53.20841 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98b59915-7afd-3bfa-8256-a48761ae32d9 | -8.63122 | -63.49617 | 2024-11-29 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76df0435-713b-3e8d-8e23-4b0c2c0b1f30 | -3.02214 | -54.0285 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f677316-b352-34a4-8610-5bcd8ef7461e | -2.62218 | -54.30904 | 2024-11-29 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25ec7322-76f8-36bd-9b44-5f5ef4c0a465 | -2.98575 | -53.28289 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d53af554-da6a-39b9-adef-c37d3b93711f | -3.50457 | -53.81139 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87bf0ca4-5f5d-3675-907d-ae1dc3e72528 | -3.49876 | -53.80511 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a645d4a0-5fb5-3de5-9092-b04115550d7a | -3.47036 | -54.54617 | 2024-11-29 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b4147e8-95ba-3553-93a2-458b88fd09c7 | -2.97148 | -53.28645 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 13b4d17f-41b1-3b45-adfe-e6c5a5995162 | -3.57398 | -53.02282 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66a4cff2-9641-371a-93a4-48f0eca18525 | -2.36414 | -56.11591 | 2024-11-29 05:46:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d82c542-91a5-37ae-9c4e-9cb26717946f | -2.97907 | -53.28156 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e5500b33-ed50-3ba6-9d03-55f5664ca268 | -3.49955 | -53.79953 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 116ac343-d5b3-3418-a5b8-32307d9e94f9 | -2.90532 | -54.18446 | 2024-11-29 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| caefcc04-da1c-3b58-8744-705886ee6424 | -3.21911 | -54.17736 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f4d3291-59a8-3079-b13c-0bc949620886 | -3.11657 | -54.47789 | 2024-11-29 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1f761f9-d6c0-33c9-a2b4-1f12efe8da83 | -3.09327 | -54.13143 | 2024-11-29 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a58be474-c9d3-3dd5-9926-00b41e0e0185 | -3.10206 | -53.26032 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 213577be-59d6-313c-9ecb-4beb8282a298 | -2.73394 | -54.14175 | 2024-11-29 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8951b990-6dc2-3578-86c8-1ac2df3d3d96 | -2.36918 | -56.1203 | 2024-11-29 05:46:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8a7a556-fa3f-3841-a4ec-447d2e8a172f | -2.83423 | -54.12485 | 2024-11-29 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d88504a-e330-3035-8e87-7a9fbc1620e1 | -3.49463 | -53.79766 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06950582-c401-39b8-8ab1-807fe117b4c7 | -2.97725 | -53.29401 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 4e1624a3-3d98-3208-a16d-e89d6b762f2d | -3.11268 | -54.47656 | 2024-11-29 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aea0b0a6-4d7a-3c6b-bdf3-80e329bfbba4 | -3.09309 | -53.82119 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 805080c6-e9b7-3c82-987a-a92818679f09 | -2.9672 | -53.72873 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 051e2b5c-d3a0-3a69-bdf4-81c741634b49 | -3.49956 | -53.80963 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4cddd47c-dd62-3bdb-9378-9ef4466e4888 | -4.51403 | -59.81266 | 2024-11-29 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37efe9be-8dbc-3842-a14a-82d67a0336a8 | -3.6713 | -54.4501 | 2024-11-29 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d788d70d-897f-3b35-b8a5-0d555133e20b | -4.08119 | -62.94484 | 2024-11-29 05:46:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e48d56f-20d2-3a6a-bf97-49a74135224e | -3.25224 | -53.63672 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d9a13dc3-cb7d-36df-9a58-241a80010d8e | -2.98483 | -53.28918 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 48f095b5-a44b-3a52-af94-545c6ba84924 | -3.22039 | -54.1788 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 13d40d97-9d11-3945-b3f8-5efa2d8ffc11 | -3.49301 | -53.80857 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8f0979d-c359-3539-b9fa-004f2feeb547 | -3.2514 | -53.64245 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 69bcc37e-22fa-39f4-b8e5-e1f739446b9f | -2.96684 | -53.72549 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d13f7892-71c9-3ea4-973b-f5a1ce89c49f | -3.33264 | -53.22655 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4c622978-3071-33b8-a4f3-7b06b3dd77c2 | -3.09532 | -53.25924 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 501da731-06ef-38aa-ae12-50818647639e | -3.1012 | -53.81172 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c8cd0ea0-4af3-3c8e-8ea3-45daff73b43d | -2.97059 | -53.29253 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ffd6f2b4-4e61-320c-bf9e-6b5e6d22be5a | -3.22227 | -54.06779 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 467bf9a3-458b-3bec-93c0-abf716c3dd5f | -3.3887 | -54.29183 | 2024-11-29 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44ba2ba6-5add-3050-86e5-b798d8190fe0 | -2.97478 | -53.29256 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 12f04c08-b710-3a11-ad5c-2fd4934db2e4 | -3.09297 | -53.81702 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e97188b-71c7-3c90-a91d-a56e2e33a8e3 | -2.97386 | -53.2986 | 2024-11-29 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| a3193b90-563d-35f5-a5ee-0ae8750a43bc | -3.22152 | -54.07287 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3dfb79a-c271-30a4-a43f-f39bc8e886ae | -3.49802 | -53.81033 | 2024-11-29 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README106.md)
