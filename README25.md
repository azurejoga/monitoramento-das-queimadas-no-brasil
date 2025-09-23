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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4a6f61e-f5ac-36a0-b47d-5f3830eb20ad | -6.34608 | -56.20322 | 2025-09-23 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85001470-135b-3513-9531-892c5cd3440d | -7.39333 | -70.10526 | 2025-09-23 05:59:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b2c3d6b-1a31-3c09-b6f1-1c548ca71eab | -7.91343 | -70.14497 | 2025-09-23 05:59:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cebfe5e6-fc9f-3b14-a57c-a4f8b9db7647 | -2.3654 | -67.21264 | 2025-09-23 05:59:00 | NOAA-20 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 241a1eb3-092c-3594-9ba1-9df553bc0956 | -2.36483 | -67.21634 | 2025-09-23 05:59:00 | NOAA-20 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a142c20-8a7d-329d-b1c5-0dcdc1eaf317 | -10.23457 | -68.7672 | 2025-09-23 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fbadbb1-ac97-336f-a05d-d3258c4c69bd | -8.783 | -71.80805 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37fd7407-9dfe-3d73-93a9-24620de4513c | -8.20442 | -69.87032 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17dc06f6-55b1-33f8-9317-fcef19eeb3b0 | -8.88649 | -71.27191 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e40fa956-bfc4-31ae-b4ac-d88fae61fcad | -8.391 | -71.03388 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 60078711-e496-3898-8282-fcfae08d8111 | -8.30601 | -70.56312 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ba3c842-d36c-3c25-936f-423de85f01f3 | -8.8872 | -69.2293 | 2025-09-23 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aeeb104c-09ba-32e1-8602-5e9f00349489 | -9.98192 | -68.4478 | 2025-09-23 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89080791-68be-325d-83aa-334280527a60 | -10.87817 | -69.18741 | 2025-09-23 06:01:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3320406-e32c-32d1-b1a7-2f923ca12801 | -9.37655 | -68.82073 | 2025-09-23 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56da0655-c0b3-379c-9702-a15019672262 | -9.5026 | -68.24291 | 2025-09-23 06:01:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e1ead699-9547-3756-8919-e8848000d7d9 | -9.28646 | -68.11918 | 2025-09-23 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0272b157-7f09-3d26-befa-c40345cd18b5 | -7.99303 | -71.31242 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8f71d22-7345-31b7-a42a-3364578197ba | -8.86294 | -71.37632 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46bf402f-468f-3f2b-a693-3969345e8f68 | -9.22215 | -67.57773 | 2025-09-23 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c51bfef-89df-3548-aa33-3478feefa6db | -9.11642 | -68.31715 | 2025-09-23 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 181e9aa2-6187-369d-99f1-059d5369f6a5 | -15.95834 | -59.48903 | 2025-09-23 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f652285f-f7b1-3347-8f5d-d25913d54ec5 | -9.29012 | -67.29063 | 2025-09-23 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d0218fa-6dfd-3cad-bf11-87a239df645e | -8.37356 | -70.75945 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c41f9dbc-414a-30c5-95ee-107bfb101c10 | -8.72461 | -70.75114 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d857314-4df7-305a-b2c2-b09e57b9c02e | -8.80364 | -70.78906 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aafbf919-caf9-315b-80bf-12faa954c60c | -9.60771 | -68.54658 | 2025-09-23 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| facf5005-fdae-36b2-aa82-3088ee8488c0 | -9.45779 | -67.1411 | 2025-09-23 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2484905f-503c-377f-950a-73546aaca3e9 | -8.20496 | -69.86682 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33f833ca-5c04-3de6-bf55-722cdc328bf9 | -8.42866 | -70.19485 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3889367f-5f70-3a61-9417-3e1e90446dc0 | -15.95881 | -59.48421 | 2025-09-23 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9694dc76-8cce-312f-83ec-d7a7eb2e19f9 | -9.13375 | -68.17695 | 2025-09-23 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5222f8e1-2942-3810-aa3a-79023b261886 | -10.24318 | -68.7568 | 2025-09-23 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c159490-e815-369e-b926-ee2f19544f2b | -8.87814 | -71.49467 | 2025-09-23 06:01:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86f3c4fe-ce48-38c9-a61f-e241f8a6b8e2 | -8.97231 | -68.02218 | 2025-09-23 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d2094c6-dfbe-3292-9d07-12b4adfc6169 | -9.43971 | -68.93307 | 2025-09-23 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a75b3f13-291c-3e97-839b-c294087b92e5 | -8.24435 | -70.90982 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a49efc3-f673-39f1-a5a2-427d82fecad6 | -8.85463 | -71.30257 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9da18979-763d-38f5-8f2f-b01d05147866 | -8.69363 | -67.05755 | 2025-09-23 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b32fe809-c0c2-323d-b463-01c526a32aa6 | -9.14437 | -67.81389 | 2025-09-23 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 122895df-8c9e-3c44-a98f-2628b63140e7 | -9.11584 | -68.321 | 2025-09-23 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fcf55a6-8dbf-3709-9664-a80ed86b8fb9 | -9.45346 | -67.14493 | 2025-09-23 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75888bb8-8d22-3cad-8d0b-8191cf210042 | -8.81081 | -67.07263 | 2025-09-23 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76c70db0-f50b-3e42-8d2f-5082b349aa47 | -8.42811 | -70.19833 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf0fa078-578f-3249-981a-7c60fe9c9ea0 | -9.65207 | -68.7121 | 2025-09-23 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6020f2f2-1f7e-37d5-9935-82eb49085f17 | -9.46147 | -67.14168 | 2025-09-23 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75601d66-a213-366c-a048-7efda07d50f6 | -9.29075 | -67.28633 | 2025-09-23 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b08fe553-9eb1-3b32-9d42-16a65c7294c4 | -8.89958 | -71.82314 | 2025-09-23 06:01:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f013c0f0-06e8-37a7-8aee-6ce48799a978 | -10.23571 | -68.75956 | 2025-09-23 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1edfda43-201b-3c81-9e86-6683c043c537 | -8.31889 | -70.91136 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 652d2e7b-631a-3c87-b06f-67ec0f17badc | -9.47384 | -67.13456 | 2025-09-23 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cdfee6c-adf9-3994-8952-d02f9df42b43 | -8.85851 | -69.15925 | 2025-09-23 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6700813-81e1-33e7-a243-20507cac951b | -9.16812 | -67.68024 | 2025-09-23 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4543ac31-394f-34ff-93ad-52d6026137fa | -9.4708 | -67.12962 | 2025-09-23 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e905ed84-05d5-3787-ad54-30c2d30acac1 | -8.31944 | -70.92932 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9029b709-ad08-39a1-8b52-c2088450a0ec | -9.94129 | -67.22662 | 2025-09-23 06:01:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b3a802e-5a1f-3eed-adbe-c50ec1511de2 | -15.94515 | -59.48768 | 2025-09-23 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87187fba-5b51-3320-bcf4-14ceae1795a5 | -10.06016 | -68.45818 | 2025-09-23 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84974675-685d-3d23-9e14-587cac17f925 | -15.91848 | -59.37419 | 2025-09-23 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 336a941e-2aa9-3ff2-bd7c-d63e6dda2672 | -8.341 | -70.72927 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92db902f-c1a8-3ed8-9da3-b56d691d5775 | -15.94563 | -59.48281 | 2025-09-23 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d738a518-2c5d-3e47-a1b7-d0f35fb79d5a | -9.47015 | -67.13401 | 2025-09-23 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a3fc904-50d5-306f-8c6f-b9a26408167a | -9.79802 | -68.87987 | 2025-09-23 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd02c7d1-220d-3704-90a8-99e865db5b60 | -8.18154 | -70.08093 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0207da62-047c-3f72-a984-fae437bd87ba | -9.45054 | -68.88543 | 2025-09-23 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8fa3558-402d-30c9-9169-014ef34b753e | -10.14577 | -68.70741 | 2025-09-23 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9d9449e-5d86-3adf-9895-4cec49108d60 | -7.98912 | -71.31542 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebc4410a-e774-345b-9d9c-9eb8f6e7d81e | -8.56605 | -69.68647 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 61ea740a-3e3e-3e4c-bf94-c5db086b2325 | -9.47753 | -67.13509 | 2025-09-23 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 084b1b8c-04d1-39e4-b5c4-91017c79eb95 | -10.05853 | -68.45947 | 2025-09-23 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63aed0a5-6407-3fbe-a503-1bb27b3ff278 | -9.17239 | -67.94058 | 2025-09-23 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7fe0826f-d7ed-3e3a-824c-9602ca26ba57 | -9.55987 | -68.55888 | 2025-09-23 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| faa21461-faa2-3139-8702-ae42aea9c61d | -10.23628 | -68.75575 | 2025-09-23 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 513d4e95-7478-300e-bca4-92c2e3096e93 | -9.45714 | -67.14548 | 2025-09-23 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88974dd8-ad2a-3ffd-9fa5-f9e5ae2ef4ee | -9.1906 | -71.83672 | 2025-09-23 06:01:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1e4b579-d886-3918-ae86-ae1868b212cf | -9.92382 | -67.42394 | 2025-09-23 06:01:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 447568ef-8c90-375b-be76-e210b775bb64 | -9.00537 | -69.41326 | 2025-09-23 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 966eb861-c379-325c-bcca-99babea6edc7 | -8.89089 | -71.28703 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4bb1ccd-7f0a-32af-882c-d811fd10a743 | -8.88757 | -71.28648 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9f02d5e-074f-3080-820f-eb3dcb3a7e2b | -9.94498 | -67.22718 | 2025-09-23 06:01:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97d03f59-808c-3520-bc60-b8ac13cf58f7 | -8.56066 | -71.46104 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bad261a5-c945-3361-ac74-ceb48d8b2ba1 | -8.31737 | -70.36205 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b67303f5-e8cc-3632-afe5-3ef30a3c09ed | -15.95123 | -59.49352 | 2025-09-23 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b27ef011-2999-34e0-9b42-933e72ff4c21 | -9.44978 | -67.14436 | 2025-09-23 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50e7acd5-4ccc-3da2-a8d5-fc09ea3d5f4d | -9.44225 | -67.4208 | 2025-09-23 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6f877c7-b171-3ebe-a05e-a553b7dd06b3 | -8.3029 | -70.8409 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72364b72-4dc6-3f12-9a3d-9f8e6d9d632e | -9.19563 | -67.57049 | 2025-09-23 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39059e44-03d0-3b01-b388-71d20aa761a7 | -9.45111 | -68.88172 | 2025-09-23 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c624c63d-016a-30c4-a811-6749e9d7e1fc | -8.04753 | -71.01497 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d782be48-66c8-381d-a903-36008eb35b49 | -9.46777 | -67.12466 | 2025-09-23 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b4e6307-d772-3d6e-bc86-3cef8016d60b | -9.45042 | -67.13998 | 2025-09-23 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 190f4a35-9d8e-373b-9aa7-eb3e9cfb4eef | -15.95173 | -59.48851 | 2025-09-23 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 082cf7ba-752d-3189-bd91-0284f004e6f3 | -8.24159 | -70.82006 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bb7dbde-1c85-38ac-bf1e-35f944cf0a5d | -15.91608 | -59.37416 | 2025-09-23 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc45bc5a-f70f-3a49-8ec1-b03376b783ba | -8.82783 | -70.63607 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a739df89-a9c2-3dae-a261-bf9e0bbf5578 | -15.92264 | -59.37561 | 2025-09-23 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ababb79-8e4f-3063-9850-c4133457e2d5 | -9.19204 | -67.56993 | 2025-09-23 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b89758ed-b4ad-3199-9036-93a80eaf089b | -9.80201 | -68.87663 | 2025-09-23 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87e4745b-af59-3899-8883-b6788f8d0a44 | -8.23815 | -70.19698 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71e661b3-94f4-3714-b0b1-cc3ef68bc9e8 | -10.14922 | -68.70794 | 2025-09-23 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README26.md)
