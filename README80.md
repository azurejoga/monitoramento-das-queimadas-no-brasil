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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2ff892c-ce70-31ee-a02f-7199a5f3163f | -1.79765 | -52.75844 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 550f9aed-a574-3ac6-ab87-191f7c0b2fe6 | -1.89092 | -48.65146 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aad98d19-671b-32a0-9490-86261fff68bf | -1.2694 | -54.56123 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c250d062-47fb-3f43-836a-abd59e3f4d30 | -4.88491 | -41.30254 | 2024-11-30 05:01:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 381f190f-f847-3368-a3d7-088668a8374e | -4.00891 | -49.94427 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c3046ea8-3df2-3cb5-9c5f-c4d55b14890a | -2.60732 | -54.35978 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a645dfb4-e626-3e36-9441-44385d157baf | -2.62885 | -54.07111 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3cd2fbbb-7f11-3455-8820-93b6f4f6227a | -2.83838 | -54.1148 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7499e535-32da-3559-8feb-994d0d4584c3 | -3.27939 | -50.59211 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aec38354-a3f9-3c51-815f-4eed65e0fcb2 | -3.27969 | -50.19155 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a3c182c3-70c9-3e30-bfd7-1943458553b9 | -1.05062 | -51.74065 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60c1860f-8726-38ff-a118-5edc1c3512a9 | -1.87246 | -53.95422 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39293a79-47c5-31da-a4be-c9354ea96f23 | 1.19777 | -55.94948 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e84041af-b442-31d7-ab37-ec5387451367 | -1.97551 | -52.8957 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3937c80b-52c7-39a9-bc83-640ae9b3651d | -1.1946 | -53.8738 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0967f5ef-5f28-30ab-9d33-08f30846f75c | -2.98962 | -53.88652 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ab117f1-e667-3c78-a9af-50b5411d9a1f | -3.2797 | -53.01126 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2057dbe-7544-3973-a4af-375e25cf780c | -1.34648 | -52.13017 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c064647e-7377-3554-8f09-3c86bac547d4 | -1.0649 | -53.22066 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62609fab-4cc3-3fc0-b6c7-f3eeac8b0f07 | -2.80257 | -54.03762 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 71991ab3-65e9-3182-b9a4-c2863ee7efe6 | -2.36222 | -55.87297 | 2024-11-30 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22ef4294-823a-3300-acb3-65f307617976 | -3.05127 | -54.0507 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf09276a-acc2-3358-80f2-25bc3442c2bd | -3.32049 | -51.62526 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e755b624-47da-38f2-b933-6f8ccc75533d | -2.60805 | -54.20347 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88330911-517b-36a7-bc11-15575333c7a0 | -1.85769 | -50.80743 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3d48fe2e-e6f2-3483-be06-c7fbbd943e31 | -2.64826 | -54.03469 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e60e703-6a6f-3589-aaef-1c0c0ea78736 | -1.40729 | -51.58532 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d64b326-01bb-3618-a507-11560831af21 | -3.12404 | -53.76198 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d479f275-ef4b-3a54-bd5c-3e89a274b72b | -2.20166 | -53.74995 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bae2b05b-9a31-31bd-8230-18df2fed6dfd | -1.44606 | -55.20029 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f0956fe-58bf-3df7-9cd1-954cef522d47 | 1.87871 | -55.72976 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ada136e-e319-388e-b83f-447bd0c08024 | -3.53296 | -52.15753 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 577e70b5-f3b4-33f7-91d4-adb070f22f95 | -2.44455 | -53.62479 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c91ad81c-bf82-3145-9e8c-63ea4faa8816 | -2.57345 | -54.33679 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e215c3e-bf89-34d8-bace-25325983af18 | -3.11314 | -54.47831 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46cb5fea-0ce3-3d37-83f5-281b1d82528e | -3.14141 | -53.7173 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4603203-0587-3961-809c-243e3c547fed | -3.09973 | -54.02584 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a455f7a-5941-3899-bdde-6d02f761424d | -0.81718 | -51.61675 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 689d7a01-6297-3033-9d0c-c50da6716d80 | -3.09432 | -53.28588 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79bf7806-dd2e-3259-93ab-f81d3ca3786a | -2.7605 | -47.90102 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29402dd3-5be1-3842-8a8f-f078a6ca504a | -1.76134 | -53.64299 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 649c44c0-e7b8-3c86-bcf7-6c3c53ec42b0 | -0.25255 | -51.6085 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 675dd853-93a2-3a06-83b3-511d0c2e0476 | -2.58643 | -51.91896 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec10a188-34c0-3db6-b3a2-e09e435eb58b | -1.57875 | -52.00791 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 803cb5a0-925f-3327-903a-c4506b292e0c | -3.83933 | -52.17934 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f9337f2-65eb-32a2-87b7-bd5f5028c462 | -3.2422 | -53.92897 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06729055-d114-34b8-920b-14fe92af9d7d | -2.81977 | -51.2955 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67946cab-cc3c-3f07-ad32-577371d488c0 | -3.15268 | -53.83202 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 949ca9db-99bc-3272-af7f-2f3ac4c01195 | -2.72593 | -52.98096 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1ae19a5-a099-3d0e-be37-e5eb893caebd | -3.30396 | -51.10464 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f95904fd-0cf9-30d1-9ec3-e94eba80d8cc | -3.21599 | -53.37892 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cc333b3-5962-3da2-aab4-c5a4435d427c | -3.05949 | -50.33102 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b2c6eed5-8933-3fdb-8721-7dafdb4c7205 | -3.06739 | -50.33225 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 19e5902b-5e3e-3610-8649-6c2b85404349 | -3.24665 | -53.92245 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2acca2c3-7e93-3eb7-b037-30e7b83c9e4c | -3.35647 | -49.7623 | 2024-11-30 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 522c1f31-64f5-3346-96ea-f79b08755e87 | -2.82268 | -54.06224 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8ed0894-33dc-39c5-8459-6fd831773f59 | -1.09243 | -53.38453 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff60b9b6-658d-3ef5-af47-cc2fc8bc2131 | -1.13807 | -54.10624 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9a15adc-2c40-3504-90f2-e5e55efc6d96 | -3.78717 | -52.40289 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e058a6a-1092-3fc1-8daf-6f1170b3a67c | -1.07991 | -53.63851 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 91ca2456-4feb-3b02-84c6-5435becb40a5 | -1.76018 | -53.6284 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0706c06d-ead8-35f7-bdaa-f31fae7c1968 | -3.01207 | -51.85781 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5ea616c-43eb-32f1-9f8b-95f4cced06ce | -2.75915 | -54.12766 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1af854f1-82b3-380e-943d-06794ad4277d | -3.95987 | -50.18621 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f270f6e3-95c3-31e1-a8fb-51fff369e680 | -2.88273 | -54.00697 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ac668dc-4bec-322c-9e75-62686ddf82ff | -2.59941 | -54.08437 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd97fc51-8e7c-3a2a-a69e-373520095296 | -1.20538 | -51.73805 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d39f0d03-849a-3b80-a9fa-1c5aa876f2ca | -2.02157 | -48.06327 | 2024-11-30 05:01:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 60a90fb4-d16f-3845-ab23-bfc2ff631d9d | -1.16285 | -53.77616 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ae7cd3d-7014-36c3-aa3d-7e6cf01e3bee | -0.25088 | -53.76236 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a51be67e-c2e8-3dbe-b209-f810b570d50f | -1.32396 | -51.74286 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4d7c6a6-47b7-3fe0-bebb-55ab58788856 | -3.27593 | -45.57005 | 2024-11-30 05:01:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e3b36c6-95e4-30cc-80e7-711e6427ae43 | -1.13067 | -53.807 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d42a5687-bbbb-3cc8-8a75-7eea70a7b7cc | -3.98767 | -41.51802 | 2024-11-30 05:01:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e69859fc-50d1-3e5e-9dd0-3f69e41f1b29 | -2.56805 | -47.35789 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbbe8eea-5e6f-394e-a80e-59ae656af080 | -3.09024 | -54.02076 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2b0d4da-237b-381d-bc41-a7c1e5c25984 | -1.10271 | -53.60255 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bdbf47d-ee34-3591-b26d-5b129dc14756 | -2.72651 | -52.97722 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80d21170-89d5-3b33-a093-72bb51421f12 | -1.945 | -48.70832 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 683948d4-cbb4-33bc-a4af-d33a19719512 | -2.26672 | -53.46592 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44b3ac13-4616-392b-9ee3-5303137480c7 | -2.9508 | -49.44723 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6e70371-aad9-3580-a8fa-8600e39a2cd9 | -3.19793 | -53.42426 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0521417-d121-30d8-9e38-930514333d03 | -1.05424 | -55.24191 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| affb7ecc-0b40-3f75-9e59-cad07ecc34b8 | -1.36297 | -55.19085 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8452122b-d4da-3609-abc4-9a65fb6529d5 | -0.87684 | -53.68246 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ca79dea-de17-3f1d-942d-224cad5e8966 | -1.71805 | -52.77696 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79cbed96-d1a6-33b2-877d-42957783125a | -1.0902 | -53.39874 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9509aa72-5ce1-3194-97be-da5349e34ed6 | -3.37295 | -50.17632 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e0e8a41e-def6-363d-88c2-89076ffa9ed6 | -2.84666 | -54.08387 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc1e6523-4fdd-3dee-adeb-a40c22dae6be | -3.29786 | -50.7598 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 239249d0-04ac-3092-8cbd-0eb125a5a71e | -2.78774 | -51.72047 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17d6ae7d-27a9-3c0b-beaf-43609d0a8979 | -3.93691 | -47.98574 | 2024-11-30 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5432793-976d-338c-b4dd-c03adb742363 | -3.25517 | -54.21881 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f24ba426-8838-3f2e-9df7-6edcf84efac7 | -1.42401 | -55.27509 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b3b679f-0604-3fd1-b7e4-35675b7ff8e2 | -2.36758 | -54.4855 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 455df37e-fb63-3b7e-aa27-88e34a20cf9d | -1.10104 | -54.12529 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7abaa34-a004-3631-a8df-27b9e6679029 | -2.14224 | -54.88481 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cdac0680-a9d6-313b-81d9-6b1ff85d982b | -4.42177 | -46.14674 | 2024-11-30 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| caad0914-a11d-3b28-8760-e5caca90ea39 | -2.54841 | -55.22787 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11d3efc2-ccdf-3469-8920-8bb3a8d319f1 | -1.51581 | -45.89924 | 2024-11-30 05:01:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README81.md)
