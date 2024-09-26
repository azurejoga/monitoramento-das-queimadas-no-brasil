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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 138f4b45-f9f4-365e-88d8-6d012f2c668d | -11.2171 | -51.15722 | 2024-09-26 04:06:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 80faa0f2-ba58-35ea-b6d3-3633e02abb6c | -11.21653 | -51.1603 | 2024-09-26 04:06:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 0b8119ba-53e7-3904-b60e-b0f96f895104 | -11.21313 | -51.15009 | 2024-09-26 04:06:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d30a4a38-1563-324d-b380-a39a456c0360 | -11.21256 | -51.15316 | 2024-09-26 04:06:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 81dd418e-29be-397d-8b92-b4568fd58666 | -11.212 | -51.15623 | 2024-09-26 04:06:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cf99c73c-9fa8-3e91-a71f-823ff14bd5da | -11.21143 | -51.1593 | 2024-09-26 04:06:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 812ec38c-1b32-31aa-b544-32ac92f4f24a | -11.20804 | -51.14908 | 2024-09-26 04:06:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7278a651-271c-33a0-bcd7-a31085861a80 | -11.20747 | -51.15215 | 2024-09-26 04:06:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5c7ded4-d4e1-370c-8c0e-354a57da5a75 | -11.2069 | -51.15522 | 2024-09-26 04:06:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 239524ab-923e-3508-bf77-44c4c27f1f30 | -11.05758 | -51.43425 | 2024-09-26 04:06:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99dcd437-d3b2-3e5c-aa29-6761252afa4e | -11.05698 | -51.43747 | 2024-09-26 04:06:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1de11f9-c71e-32e4-84da-cf21f1805c55 | -9.11108 | -53.30274 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 041316fc-fa8b-3d43-963c-39121c2d69fc | -9.11093 | -53.3008 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a99ed44-2a05-3a1b-9cbc-fd9c69ea9155 | -9.11006 | -53.30552 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0991fce3-9229-3db3-8648-4bb7a53e1003 | -8.89105 | -53.02644 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f22687f1-c146-3b1b-aa48-dfc46f06cd75 | -8.89017 | -53.03111 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 09dbb6d1-e91a-3180-a118-d5ac303e122a | -8.65216 | -53.11969 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c92f26c6-4c33-3a54-a8d1-382db865f571 | -8.65143 | -53.19027 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23dfd8c2-2e2e-3557-b788-db692144d4f2 | -8.65039 | -53.19585 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32c4838f-2f1b-3c8c-b7db-b2fd0042667b | -10.45209 | -53.30945 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2569e3e4-21e0-38f9-bec4-6e0102391393 | -10.45124 | -53.31385 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e213c73-b81f-3c49-ba70-2d87a6205365 | -10.45037 | -53.31837 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e33e3419-99b0-3e9c-a89e-8b8feef245b4 | -10.02358 | -53.45949 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1913474a-1a2f-3f5b-a2bd-69961eddbc9c | -10.02348 | -53.4929 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 3fc75bb7-eae8-34fb-be43-fcac14da363a | -10.02334 | -53.4676 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 4534d9eb-964b-3d21-9d2a-81e69a3dc3f5 | -10.02272 | -53.46395 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c576f4bf-fa24-3321-b6c1-013d61b1ebb2 | -10.02244 | -53.47216 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 53b288e7-3448-3434-80db-765e7c91d6ea | -10.02185 | -53.46852 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cba1128e-7a3c-326f-863d-f69d26bce884 | -10.02062 | -53.48136 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 508beb28-ecc7-307f-809e-76ed4b6c84bc | -10.01921 | -53.48236 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3f82f69-ddf8-3136-8d5f-5868209782ae | -10.01755 | -53.45829 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 140ddc15-4f25-326d-a8df-3c31b84ec70e | -10.01668 | -53.46284 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88747fb8-c852-307f-bd15-0f587f2bf98b | -10.04222 | -53.4672 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 174d49ea-79ff-3607-83c0-4fc234a55a2e | -10.04156 | -53.46365 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01b49911-9d33-3d24-aa27-1d1644011696 | -10.04133 | -53.47174 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 6903a3cf-70e9-3bcd-bdbf-8e96ba0d9d3a | -10.0407 | -53.46822 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 542586ac-a389-30c4-8634-8a5e8bf743f1 | -10.03983 | -53.47279 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7002b1c2-b2a2-302b-b5cb-46941881c572 | -10.03801 | -53.45676 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 34df0bd2-01d6-325f-9d66-5bbe7403e795 | -10.0371 | -53.46137 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 4386dd9b-2782-3f2b-936b-cd8c3feea8d8 | -10.03643 | -53.45772 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| ff39c94c-7af0-3f7f-91c5-4898a97c1eeb | -10.03555 | -53.46232 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 664a7f85-4dc3-3c0f-9a1c-3c59eb897fc0 | -10.03552 | -53.49554 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b6ecd0c-42fc-39d9-be9b-7080672c8bcd | -10.03531 | -53.47049 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 1152690b-7f70-32ae-bfa6-9021d75ff9cd | -10.03441 | -53.47505 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| b490b192-4c83-33ea-9dca-b6f4f03fc006 | -10.03382 | -53.47145 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 5d1117b1-9b9f-3a74-bb79-6c1a14dcea66 | -10.03351 | -53.47961 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ba4baa9-ce33-349c-848f-7263bcc37cec | -10.03295 | -53.47604 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| ae0ea6a5-c5c4-362b-8f75-796a55c9c1da | -10.03262 | -53.48414 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8dcb5b67-f262-32a2-b9be-c0244152eb1b | -10.03208 | -53.48061 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95d53ee8-b09e-3f29-be92-00de5b3346d3 | -10.032 | -53.45549 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| e97c4dce-0925-39a9-a230-30632d3e11b5 | -10.03172 | -53.48867 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| b4a291c4-15fa-3515-9786-7b2cbe6ca1d3 | -10.03122 | -53.48516 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c813a57-28e4-35d3-88ba-4c6391ce9aae | -10.03111 | -53.46001 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 17b48587-70a2-3a94-8573-3c1433c94d9c | -10.03084 | -53.49317 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 5096cf15-f8b9-3879-995a-6a7a5ad9e4da | -10.03042 | -53.45643 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| bddcac5e-b49c-329f-bd62-d4afa74d190d | -10.03036 | -53.4897 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 6aa45dba-8f49-3774-9d18-47f36af61ce6 | -10.03022 | -53.46452 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| b6a40177-5127-3b04-aafe-961815a1c7d1 | -10.02992 | -53.49782 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 5f4306e5-9aa0-31e0-97c9-5b2170158b9d | -10.02956 | -53.46093 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 121.0 |
| ed422b6b-1ab3-3ec3-a045-53095f062dc5 | -10.0295 | -53.49421 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 2f0e4572-8027-36ea-be8c-adf23e48764f | -10.02933 | -53.46904 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 3d613889-8c9e-397b-830b-ee7cda270f8d | -10.0287 | -53.46544 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 0f27b2a2-3d0c-329b-9328-7e45adc98674 | -10.0286 | -53.49896 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 96848ae9-b69b-3efd-b057-61c647d5b54b | -10.02842 | -53.47361 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 89c86971-1a4c-3d1a-b9f1-f0c7c5c41c8b | -10.02784 | -53.46998 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1ff26792-6c8d-34d7-a00a-d0399a6192ea | -10.02751 | -53.47821 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00e8e07c-e809-3e3e-a210-823d5c23b719 | -10.02697 | -53.47457 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| d6af8c73-2455-3296-a573-141c08d113dc | -10.02661 | -53.4828 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55398fe3-c9a0-3fbe-8ca5-e1c284646933 | -10.02609 | -53.47918 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9d04289-b806-3196-a122-61a279b78707 | -10.02599 | -53.4542 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| d00297be-1027-3290-b782-ac6d9e07d62a | -10.0257 | -53.48738 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2fe153a-004d-339a-9e21-331bbb442a93 | -10.02521 | -53.48379 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40c0e09a-1fd1-346f-90a6-34955c33a2aa | -10.02512 | -53.45863 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 826e8f6e-0261-3217-9a37-ff1dac036c93 | -10.02481 | -53.49189 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 786c541d-ba6a-365a-a483-a20d57bfcf16 | -10.02442 | -53.45507 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8df426b4-6ac2-373a-8355-ec71ab58e545 | -10.02424 | -53.46306 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 4979b9d0-23ca-311f-b10d-8923de145c05 | -9.17316 | -54.67849 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7ad2feca-7748-3cc9-9842-a35c2608289a | -9.1731 | -54.66876 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4916161e-4bf5-385c-971d-0dcfa07866ca | -9.17196 | -54.67455 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40503800-13f6-3583-b51b-167b657ae807 | -9.17076 | -54.68062 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b58e1a7c-4317-38ad-ac42-5b4eb2110b99 | -9.16777 | -54.67097 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aefe4f46-383c-398b-8c61-5dfa3a5a24a0 | -8.71179 | -54.79806 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d7845149-6065-3481-9d68-982a60d3bb09 | -8.71064 | -54.80392 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be2018ec-b7ce-3fb1-96a9-c3a3a7e30d01 | -8.70927 | -54.81086 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4e3963bf-a2a0-3a97-9a6f-f3f7a9fcc2eb | -8.70787 | -54.8015 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 043cbfcd-f847-395c-acbe-95d4ce430cd6 | -8.7065 | -54.80869 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fcfd6158-71f6-38f3-8a5a-41ac0fbe6659 | -8.70513 | -54.79671 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7702b32b-a949-3e87-9037-0bb4d5cac49f | -8.70387 | -54.80307 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a9829c0-ac83-356e-aad2-a6d28e4a612b | -8.70226 | -54.79462 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 85469b10-9f88-3efe-898a-75af999be850 | -8.70104 | -54.801 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| faf5a4b6-956b-3f30-ae7b-b4388d1652a6 | -8.69939 | -54.79068 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5000ad36-cd7e-32ff-bde1-92a8ac929e8b | -8.6982 | -54.79669 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 487b9005-f9a3-3a4a-80f5-a48cfa71d91d | -8.69647 | -54.78867 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e505861-bbeb-3185-9e0b-edbaecd0e3c2 | -8.69531 | -54.79475 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 92355b90-bb6d-30ed-987d-22c1a8a8a1a5 | -8.69359 | -54.78499 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ead108e3-1b85-38b3-a04d-e5c54dd91e7f | -8.69244 | -54.79082 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f8d1601-6e06-39fc-a307-666a3659054d | -8.52984 | -54.59842 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c3b9961-8c82-30c3-8a45-aa0053c3d404 | -8.529 | -54.58057 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b1f52de1-9639-3470-a6b9-47c5074daaac | -8.5279 | -54.58636 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9134a9b2-e782-39f8-b259-1926656010c0 | -8.52779 | -54.57394 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README66.md)
