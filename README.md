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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f61bde4-6423-3159-9c86-82a3ad7a0e93 | -11.9867 | -61.0214 | 2025-08-24 00:00:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 9d5a7809-8757-3569-b36e-503997baa54e | -17.5982 | -44.2784 | 2025-08-24 00:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 90f387f2-e700-3028-8b46-ee6f32045a13 | -16.7965 | -51.3637 | 2025-08-24 00:00:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 4b5f268d-aff8-3ad8-a992-6a5a443580cd | -4.9421 | -55.8233 | 2025-08-24 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| bdf64423-d336-3c13-a01f-790a6b68f8f2 | -2.9279 | -53.7078 | 2025-08-24 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 0028c1c6-adee-37b1-867e-33cd8daab62f | -9.0246 | -65.3807 | 2025-08-24 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 009a3708-f7ee-3ccc-a16a-a78f1e68c509 | -8.6131 | -62.5929 | 2025-08-24 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| e8a286dc-bb94-3f23-b719-467f8959cebf | -8.6314 | -62.63 | 2025-08-24 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c88f1074-fdf1-3bd9-8667-77167f265c2e | -17.4045 | -42.6186 | 2025-08-24 00:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 4217a007-0202-3fc6-aac1-216bb2acc267 | -7.5534 | -63.8556 | 2025-08-24 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 0e16029a-d653-377a-8fe6-33f861f02421 | -17.6183 | -44.2738 | 2025-08-24 00:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 3c801bca-3659-321a-8692-e6b5b0bc0946 | -8.7769 | -49.9763 | 2025-08-24 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| e1395c87-bf2c-350c-b94b-bb4a070483f7 | -16.7772 | -51.3451 | 2025-08-24 00:00:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 55.7 |
| d685bbc8-cf05-3c34-a63a-c1e9c6a23822 | -17.3844 | -42.6235 | 2025-08-24 00:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 943577d1-a0cd-3314-8a4d-6fe01a997ee0 | -9.0045 | -65.7174 | 2025-08-24 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 156.2 |
| 930de70f-ddfd-3d96-9176-dafa9f2dd90b | -8.9107 | -62.41 | 2025-08-24 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 882fcabb-9248-3d23-8430-1d5194c82362 | -5.4181 | -60.1784 | 2025-08-24 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 260.0 |
| c08f585b-4e76-3f31-a6bf-a216b8eb5d59 | -9.0046 | -65.6988 | 2025-08-24 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 8c66ebb3-960e-3bf8-9870-30f4c12ea637 | -5.4026 | -44.9952 | 2025-08-24 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 92456d26-9eda-30f2-bb20-157ab23ebfad | -10.6131 | -44.3051 | 2025-08-24 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 7107e1ee-24d8-37ea-a125-cfbae44e63ba | -11.5245 | -51.8685 | 2025-08-24 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 218dea36-4ad6-3ed9-ab54-1da0159541c9 | -20.3396 | -51.6839 | 2025-08-24 00:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 5644183e-bc4c-30d4-b5c9-d8047c54daaa | -5.4548 | -60.1773 | 2025-08-24 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 46cdc164-05fa-32be-98e2-87a86ac7d7b8 | -20.3594 | -51.7023 | 2025-08-24 00:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 148.2 |
| add05fe4-fdf4-38f3-9655-2c2cd78776f2 | -9.1999 | -60.7738 | 2025-08-24 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| d96b4d80-40e8-3c92-a390-e719749cace7 | -3.5994 | -47.5359 | 2025-08-24 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 6d1c356d-21c9-3ec0-b912-2aa9844e6c41 | -5.4213 | -44.9939 | 2025-08-24 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 21aa3e9e-2c7a-3937-a84d-0297930621c0 | -9.0416 | -65.7163 | 2025-08-24 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 88f794b2-6095-38a0-b90b-84eb71b2e079 | -8.7767 | -49.9977 | 2025-08-24 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 41b97710-5c1c-3b5a-bef7-bea1e0f12c55 | -5.4364 | -60.1779 | 2025-08-24 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 1c3d62ed-5c37-31c1-8e33-4d1c3b8297b3 | -11.5429 | -51.9086 | 2025-08-24 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 692a6001-9b02-3f62-8263-9c2f02e4baa9 | -11.5055 | -51.8705 | 2025-08-24 00:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 222cdd3b-f9f2-3e41-ae31-592753fdf256 | -3.7847 | -47.5719 | 2025-08-24 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 44d2f91e-5042-3553-864d-bdd538e52eef | -8.7582 | -49.978 | 2025-08-24 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 5177c6b6-dd56-3dc6-aac1-8e0a0e7a5ba9 | -11.5236 | -51.9317 | 2025-08-24 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| b6d30c17-da22-3781-b52a-ac8bb42448bd | -9.2184 | -60.7921 | 2025-08-24 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 9993191e-f529-3905-b212-c697919404db | -8.6856 | -62.874 | 2025-08-24 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 06b92747-e882-375e-b2c4-0c94611a2cb3 | -3.5995 | -47.5142 | 2025-08-24 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 02776f70-f9c5-3b4b-89a9-bf0920503baf | -5.4365 | -60.1588 | 2025-08-24 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| b6bf6f0b-f07e-3ef7-907f-213ef940f13d | -6.6082 | -48.0412 | 2025-08-24 00:00:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 68.5 |
| be91c83b-1de5-35f9-b7fb-b74197b9cb58 | -12.0055 | -61.0201 | 2025-08-24 00:00:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 9b848d66-e9bd-35ad-badb-26735aec9f1a | -17.5975 | -44.3027 | 2025-08-24 00:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 654f2def-f0e2-30c4-ad1b-72ee631f3b5d | -17.4052 | -42.5937 | 2025-08-24 00:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 7af0e063-69ba-399c-8575-f4a78aed7c05 | -8.9105 | -62.4479 | 2025-08-24 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 61488c29-b94d-32ce-b8a8-72092f05bdda | -11.5239 | -51.9106 | 2025-08-24 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 5b38e40c-aa16-36bc-91fe-767a93101691 | -8.8921 | -62.4297 | 2025-08-24 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 2ad5edcd-aea5-379a-9b36-76e40722feb2 | -9.1998 | -60.793 | 2025-08-24 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 068db335-fb22-3875-8660-a82a73094b90 | -20.339 | -51.7062 | 2025-08-24 00:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 0a432463-65ea-36cf-a4a5-43f4a62e9315 | -9.023 | -65.7355 | 2025-08-24 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 18c7bf97-0816-3c2f-a4e6-6f0289753fc8 | -10.4239 | -64.4281 | 2025-08-24 00:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 94d645cc-340e-3268-873e-a83fb99a1949 | -5.4547 | -60.1964 | 2025-08-24 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| e9d4f967-a5ff-3813-af0e-84d9a708e5bb | -9.0232 | -65.6982 | 2025-08-24 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 184.8 |
| 711342c4-31a5-37f9-9e28-584f9b44fd02 | -4.9605 | -55.8226 | 2025-08-24 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 189.3 |
| 60c61f09-afa1-3001-a22f-ae881da6a38e | -17.6176 | -44.298 | 2025-08-24 00:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 4c5d3e05-480e-38ee-9430-d4749743ea4b | -16.797 | -51.3419 | 2025-08-24 00:00:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 97.5 |
| a557f6b0-8cc9-3aa7-ba7f-6a178d89dc1f | -9.0061 | -65.3813 | 2025-08-24 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 5a02018f-9846-3800-86f0-ef64a1b0fd88 | -8.9106 | -62.4289 | 2025-08-24 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 5d153aa2-d870-351c-a532-9fc5579f1478 | -5.4215 | -44.9712 | 2025-08-24 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| f51f8f8a-71fa-3822-9867-d6b9ba48862e | -13.5512 | -51.5484 | 2025-08-24 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 9a82043f-c6ff-38e6-a3fe-8a8fa0c2d965 | -2.9279 | -53.6877 | 2025-08-24 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| b40f1a52-b862-317b-b61a-49388aeeb6fd | -4.5568 | -43.2096 | 2025-08-24 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 8c382e69-e8d0-3b5a-a21e-bf2a76f5d4db | -5.4182 | -60.1593 | 2025-08-24 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 171.3 |
| 8feaf9b6-cf58-3d6b-84fc-ec4526cb4f72 | -20.3599 | -51.68 | 2025-08-24 00:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 258.0 |
| 908708be-ba13-31a7-8be2-3e78db519011 | -9.1441 | -60.7765 | 2025-08-24 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 0e6bdac1-d7cf-3edc-84ac-d3168e8a1c89 | -13.5516 | -51.527 | 2025-08-24 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 6e8a0693-66ea-3727-aad6-043dfca0da21 | -4.5567 | -43.2329 | 2025-08-24 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| c3f4906e-a9d6-3ce1-aece-b851e04b9506 | -9.0231 | -65.7169 | 2025-08-24 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 290.0 |
| 9fb65b7c-c16e-3c1c-b213-ded4209f88ad | -20.6929 | -42.3072 | 2025-08-24 00:00:00 | GOES-19 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 48.0 |
| 9f38d9a7-1d9e-3a09-a419-f75f5a9b436e | -8.7579 | -49.9993 | 2025-08-24 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 9faab2d6-897b-3ac7-887a-be43bff627bb | -4.9606 | -55.8028 | 2025-08-24 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 2233d35a-47b9-38f0-8a8f-fb7ae87d8aea | -10.6128 | -44.3284 | 2025-08-24 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 2f6c875c-887f-3420-b007-0fb59035e090 | -11.5055 | -51.8705 | 2025-08-24 00:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| d670b317-e6dc-36e2-ae71-b4dd1ccdb267 | -5.4026 | -44.9952 | 2025-08-24 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 0003aa16-eece-33ee-adfe-c7f3bf2a0fb6 | -14.8153 | -47.9343 | 2025-08-24 00:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 2a6f2211-80bc-324e-a47c-56b337d3da17 | -14.7958 | -47.9375 | 2025-08-24 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 105.8 |
| af5a27d9-a601-3dee-8825-c84fc8da2847 | -14.7981 | -59.6343 | 2025-08-24 00:10:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 892f8ee9-fde8-384c-820f-b5959dc627eb | -8.7769 | -49.9763 | 2025-08-24 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 158b1d17-5413-307c-8e81-8ed40e20e425 | -5.4182 | -60.1593 | 2025-08-24 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 163.6 |
| 3ce2070c-7de8-3287-a594-ed5ebc5915f7 | -9.0045 | -65.7174 | 2025-08-24 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.9 |
| e8bb6ad8-f66e-3410-ba99-ce611938b1ce | -6.6082 | -48.0412 | 2025-08-24 00:10:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 77.1 |
| b085b0ea-843b-35bc-baaf-3f47b3c66b42 | -22.0846 | -53.8425 | 2025-08-24 00:10:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 138.0 |
| 048da81b-b602-3608-8514-19806c6dcae8 | -7.5534 | -63.8556 | 2025-08-24 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 9eacbe56-be21-32fb-8960-079b38faf251 | -3.7847 | -47.5719 | 2025-08-24 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 21c2e66f-e6ff-3a91-a849-a5849c2e880f | -14.7953 | -47.96 | 2025-08-24 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 53.9 |
| f2121ef1-35a8-3e6d-9780-da977cb8ea05 | -20.3701 | -46.7433 | 2025-08-24 00:10:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 64.3 |
| c7cf61d6-3dfe-3be2-a7b6-05b54338ac28 | -17.5975 | -44.3027 | 2025-08-24 00:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 52.0 |
| a231d3f8-e356-3a4b-b5f8-5b2af4112d6f | -22.0644 | -53.8243 | 2025-08-24 00:10:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 90.5 |
| 20c3d9c2-7ebd-3f29-83c3-a0c826dd2298 | -4.9606 | -55.8028 | 2025-08-24 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 9bf353fb-ad65-35a1-aa6e-8afce6f6bfcf | -22.0851 | -53.8204 | 2025-08-24 00:10:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 282.6 |
| 51b2d655-9288-3bf2-980d-4ab21697e34e | -8.6131 | -62.5929 | 2025-08-24 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.3 |
| edc62047-d813-39d9-ba38-53a2ac53dab3 | -5.4181 | -60.1784 | 2025-08-24 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 276.5 |
| e76fccda-5239-3660-aabd-832856258578 | -22.0856 | -53.7984 | 2025-08-24 00:10:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 85.0 |
| 769945cb-23be-3b1f-94cc-b4145d0752c3 | -20.3396 | -51.6839 | 2025-08-24 00:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 1b6775bd-0bf2-3ca0-8bbc-e469aa1f90f2 | -8.5946 | -62.5936 | 2025-08-24 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 4c6ee535-7d29-3642-9d72-34560b9b6297 | -16.7772 | -51.3451 | 2025-08-24 00:10:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| eff7d05c-0950-3079-b718-6738193aee08 | -16.7965 | -51.3637 | 2025-08-24 00:10:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 2c3b8887-9597-33f9-9a7f-77c66b991957 | -8.9105 | -62.4479 | 2025-08-24 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 5108b3a4-4cf1-3514-bffb-0b827896d5d6 | -16.797 | -51.3419 | 2025-08-24 00:10:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 0d049658-d13f-3a68-b269-41867f924970 | -9.0061 | -65.3813 | 2025-08-24 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 49c9b6b2-9a12-39ac-8546-156d90e51cc1 | -20.3708 | -46.7195 | 2025-08-24 00:10:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 59.7 |


[Clique aqui para ver as próximas entradas](README2.md)
