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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b79ae21-cff5-3f96-9ba3-7e66485557bd | -3.09417 | -61.21384 | 2026-09-19 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3eb5732-5981-3244-be06-70b314e385af | -1.58608 | -54.42616 | 2026-09-19 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6e0b8201-3da6-3d4a-a126-b542a86ec535 | -5.91278 | -59.95041 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e0ce3bc-98e4-3140-bd62-aa501d6b8452 | -3.69295 | -60.60857 | 2026-09-19 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 825aa2fd-e4d9-3cc1-bb57-87d2d83dbdb9 | -4.42588 | -55.52544 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99c05f17-903c-39f2-928f-11d9155f3eb6 | -2.89644 | -57.79854 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 99fe06da-6fe1-3b73-a54e-86dd12b5e293 | -3.11583 | -61.41392 | 2026-09-19 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d94b4b46-6c5b-35b9-9935-846ec7cf72ba | -6.4452 | -59.97977 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a5d70e7-7476-352b-8b8b-96f50366b982 | -4.42858 | -55.5139 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5b9c568a-0adc-3173-8943-23cfe6b016de | -4.40766 | -55.49697 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac27e50a-2077-37ca-b817-e5035fe80249 | -6.94186 | -55.04475 | 2026-09-19 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b76b972-1d4a-3ef2-822b-d93882e38fad | -3.14799 | -53.93286 | 2026-09-19 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6226ebeb-3819-367b-bdba-11fb7c0f5d47 | -4.06727 | -56.24919 | 2026-09-19 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc3d2027-fa48-35c1-b0de-f4056e7c98d7 | -1.22649 | -55.72377 | 2026-09-19 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1bab9322-83f8-3609-9be2-c71fa6db46f4 | -1.11645 | -57.27402 | 2026-09-19 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6e3329f-74cf-3d8c-8834-1c379b72979e | -6.32913 | -55.28432 | 2026-09-19 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97496a29-d820-3a0d-83b5-879209d3e153 | -4.4934 | -54.98482 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c132bde4-1aac-33c5-b680-4eb84a2f2a4e | -3.6971 | -60.63348 | 2026-09-19 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80ff141d-d4f2-3637-9725-16ef471e7c48 | -3.11154 | -61.41761 | 2026-09-19 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cc49795-d6fd-3f72-9b0a-cce04b2d4cb4 | -3.33853 | -59.81296 | 2026-09-19 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c61d616e-ba51-34ea-9eee-54335d0cab50 | -1.49426 | -54.97315 | 2026-09-19 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24ebe3fe-bd53-3496-acec-4b4768e29679 | -3.7086 | -60.63522 | 2026-09-19 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0d50fd0-444d-3018-a452-be20b458557c | -5.89324 | -59.93966 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a385bc98-48ed-34b3-9a3f-ae24a80fdf4d | -6.70595 | -59.45943 | 2026-09-19 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 845d8924-9c7c-36b8-9270-7ec13df75967 | -1.57647 | -54.45228 | 2026-09-19 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd05a8f5-23d1-3460-aabd-05b3da01c861 | -6.32966 | -55.28041 | 2026-09-19 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a063fb8-8aa8-3ae0-b72d-acb9f353a53b | -6.32342 | -55.28345 | 2026-09-19 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4f8ef90-5761-3a01-b720-8c0fba7306da | -1.57705 | -54.44834 | 2026-09-19 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70383950-02dd-39b2-9f17-1dea6c59dcbb | -3.25288 | -60.88366 | 2026-09-19 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a4fe54b2-7ce5-3c3c-9d75-a0b2f7b7e9a7 | -3.55711 | -58.55155 | 2026-09-19 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf3f5e97-fb26-3db5-aee2-88912345e5e0 | -6.13848 | -59.94451 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 969670c6-f7af-3709-ae9c-1b2d77917fac | -3.34816 | -59.85728 | 2026-09-19 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d579ab11-6f95-3ccc-aebc-986f4303e8e8 | -4.49394 | -54.9811 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d98e9042-a624-3e51-8e0c-f6472ddbafff | -2.90105 | -57.80087 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ad76e5e0-0ecb-39a8-af43-24dc01b37b31 | -4.4933 | -55.49171 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd308db3-aa3f-394b-858b-11bbcb5109f0 | -4.42737 | -55.51531 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 566d8ed0-9618-3aa1-8d7c-0d18fe86206f | -5.76427 | -57.4515 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d27a54c7-36b3-387d-a907-60a4411000f3 | -4.50696 | -54.97136 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a52a9a64-8c5c-3689-9b1c-0d2fe8c1ada4 | -3.3527 | -59.85442 | 2026-09-19 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cd6601b-6dc3-33cf-a2e9-32d1adb8321b | -4.36095 | -55.43157 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2db58685-3e8d-399d-a4ea-98ab1873db75 | -3.33452 | -59.81233 | 2026-09-19 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8a9fd4ad-200f-3adf-8d7c-7169d9618b00 | -3.33293 | -59.82279 | 2026-09-19 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 608a78bb-b7e9-3005-823a-c5cd4005c713 | -1.22555 | -55.7299 | 2026-09-19 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1058969d-0ebc-3ed2-b489-6205ea0ad066 | -4.49278 | -55.49532 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26b30b09-c6ac-3f26-8fba-6f1ca8f4ca10 | -3.44967 | -58.21348 | 2026-09-19 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 84fed862-85fe-3b3e-bd4f-25643b26a93c | -2.894 | -57.78382 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 15ad30cd-12a2-3f3e-9c6c-32e7e1e61017 | -4.42639 | -55.522 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2df757e4-4cd4-3270-b59b-deb368deb79f | -2.96347 | -52.14459 | 2026-09-19 05:42:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 86271067-0cb0-370f-9051-a3d0b1d42922 | -4.4883 | -55.48745 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68277432-782b-311f-8f16-eacc9c82d919 | -2.89959 | -57.80858 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 62c9b70a-7061-3e2f-b9f5-10e3c53c7c39 | -3.69609 | -60.61391 | 2026-09-19 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ec21f50-3a07-3dfa-a3ec-a59983214047 | -1.65981 | -54.91805 | 2026-09-19 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12e2cd03-ee59-3167-be70-c54ff4256a97 | -1.597 | -55.54977 | 2026-09-19 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98524723-205c-3271-b787-c0523719332a | -5.91333 | -59.94667 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06c86123-226f-33b6-936a-ef6a059ac4d5 | -1.58551 | -54.43001 | 2026-09-19 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4b65e8f4-e32b-33b9-a3ee-74f7e77b8fe3 | -6.93767 | -55.03097 | 2026-09-19 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f540126b-2a57-384a-80cf-3012c3d13269 | -4.53808 | -54.93369 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a4caa90-b8bf-32fd-99fa-fb05c4cda34a | -8.61213 | -54.59533 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aeee7c74-a7f8-3361-bdf3-956306a7dee9 | -8.16262 | -54.82552 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ce000e4-e0c9-3b1f-867e-90422cae500a | -8.14686 | -54.80529 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5aacaba-d70f-397e-af19-7e63622c7919 | -10.92855 | -53.97193 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d201d76b-3379-322e-8b51-2ea5659febb5 | -10.70308 | -60.73393 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b6f13f6-0353-3b47-9edb-5122c4e717d5 | -8.71094 | -62.53907 | 2026-09-19 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 211120d9-592f-3088-91a6-27a2de4f4977 | -10.92994 | -53.9604 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26e839a1-1316-3798-a6fe-30c9d80f5e35 | -10.70834 | -60.72667 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a48a2b88-4029-3cfb-972e-b210ce494d6a | -7.87941 | -62.54757 | 2026-09-19 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6ddbecb-54c9-3325-8090-2c2df539104f | -6.76387 | -59.4255 | 2026-09-19 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc0fe246-c783-3d71-9419-aa44fb2f3a53 | -10.87388 | -54.09109 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ccad33f-b7b4-3da8-a74c-7216bb5e5e7f | -10.70413 | -60.72606 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 18004ee2-3a9a-37a5-87a7-0a4e62b46ba9 | -8.92314 | -62.41949 | 2026-09-19 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab47ffe5-de59-35c4-8d72-94714f5eded6 | -10.69804 | -60.73454 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1b218cf-9315-37e0-9b44-3ce2f66fa528 | -10.86552 | -54.1067 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8cf644d0-1c30-3b85-9308-e2c140da6618 | -10.9351 | -53.96098 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc4f48c1-a23b-394c-baf3-ac662ee08b58 | -9.55137 | -66.02375 | 2026-09-19 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c773c417-efef-3443-bf28-ba224aeda159 | -9.55467 | -66.02427 | 2026-09-19 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c3dc57e-edda-3e65-8c3e-0712ac32603e | -9.70075 | -54.82874 | 2026-09-19 05:44:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7b8ac25-f964-3d80-b6df-c609da3805c9 | -7.37503 | -68.01029 | 2026-09-19 05:44:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15f9be8f-1917-346f-b1d9-b96fab941033 | -10.69749 | -60.73845 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f9856bd-d28e-39d5-ab2a-aeaef23762e1 | -10.89222 | -54.05291 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 73916e82-91c0-30eb-b0f0-31b9350c5b47 | -8.61085 | -54.60515 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5ffd19c-5b42-31f9-b875-a75953de120d | -9.85225 | -63.69264 | 2026-09-19 05:44:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 291a4058-f65e-32cb-8ad8-a1db6fdd6c2e | -9.39164 | -60.35099 | 2026-09-19 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf26d542-ccc5-3c9a-aee6-684929b58a45 | -8.6101 | -54.60963 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2cc84921-e6fa-3649-8844-b4714d50fd99 | -11.14561 | -54.02398 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 94502f68-949f-35d3-b067-6daafc45e86e | -8.42007 | -54.73027 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fecc5cb7-0568-350c-b82e-5ab04f73024d | -12.01781 | -55.54555 | 2026-09-19 05:44:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02edb455-a1ad-33df-8e01-99754d3572ab | -10.70729 | -60.73455 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2087b60e-65b5-3876-b33f-e66b37079f7f | -9.33605 | -60.31605 | 2026-09-19 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d18ed6c5-1251-38af-9778-d20c7911c1b8 | -11.67254 | -54.44467 | 2026-09-19 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 885b3d7d-bf38-3af7-8a59-f38c3f8654fa | -7.55871 | -61.32896 | 2026-09-19 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fd2fbb7f-d86a-33a2-a8fc-63176e2dbc99 | -9.70131 | -54.82417 | 2026-09-19 05:44:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f98ed247-cc8f-3635-be57-3cf5fc6338d6 | -8.01079 | -61.37079 | 2026-09-19 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1577780-a756-33c0-a3e7-b53ab1f83c63 | -7.37095 | -68.01358 | 2026-09-19 05:44:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e1885e8-c163-3dc4-94aa-3ffdfda20e0a | -9.38005 | -60.34111 | 2026-09-19 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c2652fd-36cf-3fc7-a169-c2e6c6159ec0 | -10.71676 | -60.72786 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99da5993-7596-3c4e-ad3c-a1523e5d7769 | -10.89144 | -54.05268 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 715a7958-8ddf-3747-8ef1-25acd60c8001 | -9.3743 | -60.31998 | 2026-09-19 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5729ec01-01f4-34c1-bbf4-3f97e1ed8a6a | -10.6994 | -60.72938 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e536490e-163f-39ba-830b-d8213f98ae13 | -10.69439 | -60.72999 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3286e17d-1659-3561-9d16-89664c10b046 | -9.54297 | -63.7764 | 2026-09-19 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README97.md)
