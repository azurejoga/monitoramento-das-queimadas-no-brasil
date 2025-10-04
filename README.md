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
| 92fd1780-ee32-3b87-b60c-3a6591dffc7d | -3.8384 | -41.5729 | 2025-10-04 00:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 102.8 |
| d34e579d-cff8-3b8c-b25c-1cbf37797f41 | -15.71 | -46.2745 | 2025-10-04 00:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 71.4 |
| cf8c0f64-836e-32c6-a014-732de97410d0 | -4.4446 | -43.2164 | 2025-10-04 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 4b969070-198b-3b8b-90fa-2bc20d39b11f | -9.9584 | -50.2286 | 2025-10-04 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 0438470e-ca52-30ce-8ad6-b6f7d55c4bdb | -17.0903 | -46.2347 | 2025-10-04 00:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 44f9b876-9ad2-3d15-b30a-a8fabd3f722d | -4.4445 | -43.2397 | 2025-10-04 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 4d8926f6-b218-3c19-b5bc-acc4480f13fb | -13.996 | -48.1987 | 2025-10-04 00:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 143.0 |
| e305168e-9256-3300-a740-a64ebd2bde28 | -14.2321 | -46.0794 | 2025-10-04 00:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| db3f2f10-c0e5-3674-925e-2b27839cf881 | -4.954 | -45.0694 | 2025-10-04 00:00:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 15acb492-188f-3a10-9df6-0ed31c7a6986 | -17.0855 | -43.3564 | 2025-10-04 00:00:00 | GOES-19 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 39abf5c1-fe02-33f0-b101-72ce6103c17a | -9.9582 | -50.2499 | 2025-10-04 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| a17a9b3b-428e-3ba1-a43e-6bb852b3752b | -13.3414 | -48.1411 | 2025-10-04 00:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 338284b9-ac78-3363-8378-f1a2a05c3668 | -4.9726 | -45.0683 | 2025-10-04 00:00:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 4b8816c9-5c7c-3e91-ba5c-148a006df154 | -5.6496 | -49.1175 | 2025-10-04 00:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| b92d1b60-a8a1-3ca5-acdf-33b46b065569 | -16.0212 | -50.9425 | 2025-10-04 00:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 9afdc3a1-cc2e-3a41-873e-878298b798b4 | -9.3464 | -54.5201 | 2025-10-04 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 168.6 |
| f69ee8b2-d444-377e-b389-7beab2270d34 | -9.3274 | -54.5418 | 2025-10-04 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| fe014c85-b068-3bdc-9239-dc089deb3f24 | -4.4258 | -43.2408 | 2025-10-04 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 83ed430d-6d4b-3bf0-abf9-31205967c6b4 | -13.3221 | -48.1439 | 2025-10-04 00:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 249.0 |
| a203f4c8-c694-3e2b-998b-8266e47cb1ff | -13.3225 | -48.1216 | 2025-10-04 00:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 216.2 |
| 4c0fc207-5efb-3029-aba5-7fa4432634a5 | -7.4616 | -46.8542 | 2025-10-04 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| b7890452-9254-3234-926f-639e6e876ecb | -6.8774 | -47.2334 | 2025-10-04 00:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| cd6bf23e-c1f9-363f-a315-22bb1486f1bb | -5.3665 | -47.2063 | 2025-10-04 00:00:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 10fca027-9f3c-333b-a21d-5a698aff2356 | -6.8865 | -44.4923 | 2025-10-04 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| a0b2dd3b-91d4-3f75-9ca3-a578d0750183 | -19.6205 | -46.6856 | 2025-10-04 00:00:00 | GOES-19 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 4ff669e0-5607-3c76-9b22-badc670a7fc8 | -8.961 | -48.6908 | 2025-10-04 00:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 422bde25-606f-3278-a4ce-ef13b4148a70 | -17.0704 | -46.2388 | 2025-10-04 00:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 78.1 |
| eb073c41-99de-3c58-8fab-5a8a41e5488c | -4.4845 | -42.8631 | 2025-10-04 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| c8b4a971-b349-37bd-be2b-0b39949033ec | -17.0897 | -46.2581 | 2025-10-04 00:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 817ca7e9-9114-3e50-b491-66f78eb47df3 | -15.7297 | -46.2707 | 2025-10-04 00:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 119.6 |
| ffabfa44-7572-330b-8cd5-6e5d3d9df03e | -16.0217 | -50.9207 | 2025-10-04 00:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 68f35a97-fbc2-3eab-94d3-8b8919193eb8 | -9.3276 | -54.5215 | 2025-10-04 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 214.0 |
| 6f0d5e0b-aaa8-3573-8bc2-b7cf9d51eca2 | -6.8678 | -44.494 | 2025-10-04 00:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| c4fdfbde-c57f-3598-902c-0a536c3ed94e | -4.3197 | -48.0908 | 2025-10-04 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 2b008a3c-c960-3d18-b003-8677f8af7060 | -8.2316 | -46.8066 | 2025-10-04 00:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 9edb464e-2bc3-38b7-9b8b-67c2e484d516 | -9.9393 | -50.2518 | 2025-10-04 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| bfcb8608-8b47-32ae-9108-d3798b9f3a3d | -4.4632 | -43.2386 | 2025-10-04 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| d78e5d44-9159-3462-a27f-60a982a6fcec | -13.3229 | -48.0993 | 2025-10-04 00:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 876b3023-e384-3309-8fb3-4c6496c7ffdc | -5.1967 | -45.0541 | 2025-10-04 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| e3d6da89-6bff-3d20-9600-290acb75eb70 | -13.9965 | -48.1763 | 2025-10-04 00:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 5ce796b0-4825-359a-8445-c11adb0dfad5 | -2.6883 | -48.3899 | 2025-10-04 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 7347b703-a47f-346c-83af-2d2d6c0d1774 | -14.2325 | -46.0563 | 2025-10-04 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| cb083f10-eb19-3fb0-94b0-1b2c6f865e82 | -4.4443 | -43.263 | 2025-10-04 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 44.9 |
| eac445e7-af24-3579-bcc5-032833ab465e | -8.2319 | -46.7844 | 2025-10-04 00:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 380a6a82-f5e6-396b-9b27-6a3dabb48196 | -9.9396 | -50.2304 | 2025-10-04 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 75998ec1-063b-31ad-99ac-c727dcabd9c5 | -5.3851 | -47.2052 | 2025-10-04 00:00:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 8f668332-897f-3504-a9ea-1cf1b0c04477 | -15.7292 | -46.2939 | 2025-10-04 00:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 1db01b19-e475-3281-a545-59ca3cfbef50 | -5.1965 | -45.0768 | 2025-10-04 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 89de58e8-7d26-354b-b92d-44e7aab914eb | -14.9347 | -46.8736 | 2025-10-04 00:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 91b4742d-a84a-34d7-a816-5576103df79e | -12.9659 | -51.0029 | 2025-10-04 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 96dcaa04-09db-3806-a025-a5d44af407f2 | -5.3663 | -47.2283 | 2025-10-04 00:00:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 252f7c18-60d4-343d-92e7-d1c49b256d02 | -12.3813 | -54.4603 | 2025-10-04 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| e19de897-fcc9-3bcd-b4e7-e97e1aa1431b | -12.9663 | -50.9815 | 2025-10-04 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 5ae31552-2694-3ace-a3d9-3f17466812cf | -13.3418 | -48.1188 | 2025-10-04 00:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 54ba377b-92e2-35cb-8624-20e961fa6f99 | -8.6322 | -54.9949 | 2025-10-04 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| c565fdfd-69a1-3f7e-bc1d-bb1a092ea69b | -2.9013 | -50.7351 | 2025-10-04 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 64326e55-b975-3313-8e8d-81c7eb8d1967 | -14.9347 | -46.8736 | 2025-10-04 00:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 3f7aa617-0bc1-310e-a08c-f066f17b9a18 | -17.0855 | -43.3564 | 2025-10-04 00:10:00 | GOES-19 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 4ea30584-b0f6-3cf0-8ae9-5e46b4a7af9c | -8.6138 | -54.976 | 2025-10-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| e68850f4-d38b-3665-b340-aba850312660 | -17.0704 | -46.2388 | 2025-10-04 00:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 38f5762e-5acf-3d6d-af79-998930965488 | -4.4443 | -43.263 | 2025-10-04 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 855c4dff-5a41-3623-ae2b-b183f2c519a9 | -6.8774 | -47.2334 | 2025-10-04 00:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 486817e0-dbbf-3c30-9b80-e8981c94bc58 | -4.954 | -45.0694 | 2025-10-04 00:10:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 5457c2ad-d293-3132-866b-32fbd55e1c1a | -16.0212 | -50.9425 | 2025-10-04 00:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 85dfdef8-a766-3f0e-98dd-d176192f150b | -17.0903 | -46.2347 | 2025-10-04 00:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 4bda7099-c4aa-39b0-a778-d26f1a0684b9 | -3.8572 | -41.5719 | 2025-10-04 00:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 63.8 |
| 076b4cfb-4fea-3ba4-a0dc-899b62d2ffde | -4.3197 | -48.0908 | 2025-10-04 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 778574d2-c315-3c75-8b96-36e98aaffe70 | -9.3274 | -54.5418 | 2025-10-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| c1873b0d-34f1-3bd0-9150-276c08aebe41 | -4.9353 | -45.0706 | 2025-10-04 00:10:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 8c80aab0-d60f-3045-8e54-0501f7b8654d | -13.3414 | -48.1411 | 2025-10-04 00:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 86b5a747-f644-3caa-9304-4f36a8a13d1f | -12.3813 | -54.4603 | 2025-10-04 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 1fe0eb54-3b62-3464-be83-ba077566c449 | -2.9013 | -50.7351 | 2025-10-04 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 6d511982-ed9b-3d40-8561-6f0514f059ad | -17.0016 | -49.1478 | 2025-10-04 00:10:00 | GOES-19 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 40100355-b3db-3d4b-bf95-fb915bab87da | -13.3229 | -48.0993 | 2025-10-04 00:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| a51cb57f-a614-3386-b130-287e463b0108 | -6.8678 | -44.494 | 2025-10-04 00:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 1c94a78e-e7a4-35e9-9bc1-64e78d7a42cb | -16.0217 | -50.9207 | 2025-10-04 00:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 496f04fd-0898-33ac-b657-de0cd180fb52 | -5.9085 | -49.2944 | 2025-10-04 00:10:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| e3107c5a-cfd7-31fe-827f-556fbd4177fd | -8.6136 | -54.9961 | 2025-10-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| a35872d1-5421-3d1e-a167-5b83b5d24959 | -13.996 | -48.1987 | 2025-10-04 00:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 224.2 |
| 9bf2b561-b626-3de4-af60-1fe0135380c9 | -4.9726 | -45.0683 | 2025-10-04 00:10:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 425c4a42-72ab-348d-b6ea-ff66b9624473 | -8.6324 | -54.9747 | 2025-10-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 5291ced7-e072-3798-9c19-9ee3c2efcb85 | -5.1967 | -45.0541 | 2025-10-04 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| d9b7740a-5997-39e7-9c97-cf049017ca67 | -13.3225 | -48.1216 | 2025-10-04 00:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 0da446c6-1173-34a2-a219-043b0217af23 | -13.9766 | -48.2016 | 2025-10-04 00:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 8ffd1ee0-44b6-390c-89f9-ba2f1dff9890 | -4.4445 | -43.2397 | 2025-10-04 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| a1af3a91-c5c2-3743-809b-47b27e231fff | -8.6322 | -54.9949 | 2025-10-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 01e06395-1869-3b9c-b081-ec5cdaca0937 | -3.8384 | -41.5729 | 2025-10-04 00:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| d8c968f1-c4a1-3fa5-afea-7464f5ed547d | -13.3221 | -48.1439 | 2025-10-04 00:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 251.8 |
| a2cf8751-2278-335a-b62e-cf3a54e6e9b4 | -17.0897 | -46.2581 | 2025-10-04 00:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 69.8 |
| ee1e1f66-6e49-3ca5-90a8-a09bc7b9e2f7 | -14.2321 | -46.0794 | 2025-10-04 00:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 6ecb354e-1dfe-3c8f-956d-691073a3dc22 | -15.7292 | -46.2939 | 2025-10-04 00:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 8ae9cc40-e36c-37c3-abf4-104b55c95a59 | -13.9965 | -48.1763 | 2025-10-04 00:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 7f2e84c5-7a2f-3b5a-afae-e8e7af8a9e0f | -9.3464 | -54.5201 | 2025-10-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 7f008e58-e3bc-3257-8685-65dd18fa3910 | -8.2316 | -46.8066 | 2025-10-04 00:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| f17ecef6-2fd2-3345-b18d-bb1c6845fd78 | -5.3665 | -47.2063 | 2025-10-04 00:10:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 34.4 |
| fe7c881a-40be-3d1b-a0d4-f6dd156038ca | -6.8865 | -44.4923 | 2025-10-04 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 51c2237b-9681-3463-8102-fc20b32ad7fd | -9.3276 | -54.5215 | 2025-10-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 186.1 |
| be95483e-ba97-3145-883d-bcdc0a9bb9f6 | -15.7297 | -46.2707 | 2025-10-04 00:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 90.2 |
| daf986b6-377c-3cbb-bc7d-d105aadc6f9e | -2.9014 | -50.7142 | 2025-10-04 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 990e709c-b9dd-3d27-a9ff-e381f89a397d | -9.9393 | -50.2518 | 2025-10-04 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |


[Clique aqui para ver as próximas entradas](README2.md)
