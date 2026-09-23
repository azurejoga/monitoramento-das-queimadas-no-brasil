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
| 0610b4e4-1c1f-3816-ade7-1d1ad39c50c7 | -9.15324 | -61.19653 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1311bba2-cdf2-3837-9026-b79004557f0e | -11.3999 | -44.05345 | 2026-09-23 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbe5a433-bdce-33e8-aa5a-831584be08fb | -6.67351 | -55.05285 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a65324be-0243-33c0-947e-3f6f9d539784 | -11.12657 | -49.45295 | 2026-09-23 05:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 36c2be76-db75-3d99-969d-31e646107249 | -12.1235 | -45.62703 | 2026-09-23 05:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2e091dc1-c774-322d-b95c-3cefba009d72 | -10.91438 | -53.94875 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d2267a4-b8a3-33a3-8e38-e6fefbeeb55e | -6.53065 | -55.35838 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa8eb0d1-eeb1-39a3-8520-ac606207efa7 | -5.88056 | -51.57861 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0a63eb9-13fa-32f1-a89d-1c406e2f3f31 | -7.78259 | -50.2273 | 2026-09-23 05:04:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08cc4e77-ac1f-38f8-af79-8e813a146e32 | -8.91586 | -50.9216 | 2026-09-23 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6693262d-3688-3be5-bbfb-b3cfeb5a6d9c | -6.62225 | -59.99088 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4019c07f-2187-3635-b82e-377d93660c21 | -10.00151 | -45.21008 | 2026-09-23 05:04:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b87e5cb9-5b8c-33bd-a15c-1fa99b87dd20 | -7.55745 | -48.68732 | 2026-09-23 05:04:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8e5b85f-d1a9-3148-94f1-174e4f632018 | -6.7879 | -48.68054 | 2026-09-23 05:04:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c8f75bf5-d68d-336f-b2d8-ff6b8d9cd02d | -3.87285 | -52.25698 | 2026-09-23 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 140e2cb2-7127-3c90-ba3c-2bf890b05700 | -3.68504 | -60.59628 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de825a74-2bd3-301c-b9c7-1f109c617b65 | -11.65934 | -50.97875 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e335050-364b-3d79-92ce-4b458fba0bed | -10.0411 | -50.22283 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c659a5b-f996-36e5-862e-c2a546ce25e1 | -7.04452 | -62.93649 | 2026-09-23 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37aaa293-5ad8-3c99-b60c-48e5094790be | -6.43221 | -48.45289 | 2026-09-23 05:04:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f5cc563-8745-3ac7-8ede-b1294c18f730 | -6.03685 | -44.03485 | 2026-09-23 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5edd00b2-0a25-3450-82aa-3986e0bb68aa | -4.45211 | -55.0223 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 045656f6-f9b6-3fe2-8510-2615a7d536f7 | -6.8916 | -55.33218 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c2faf5ec-a426-3cc3-b5a2-1a069f568291 | -6.31202 | -57.74614 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0017895-926e-3edf-84de-b63d04e1dace | -9.93362 | -48.47419 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83af8f3e-7410-3ee8-b7dc-9d1c88010b78 | -10.9133 | -53.93412 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52dca79c-57b0-3978-9c5a-4abaac3b1889 | -3.69958 | -57.29318 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea59e142-1f76-32fc-b42e-ce8550bde852 | -11.6328 | -50.94606 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f366903e-868c-3995-9f7b-0a125361b7c8 | -4.21997 | -50.66188 | 2026-09-23 05:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cd371c5-49ed-3a6c-871f-f6f087ecacb6 | -6.72336 | -44.1543 | 2026-09-23 05:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 46430a51-4347-3e5b-bcaf-7aee58877558 | -11.30251 | -51.34878 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2235e6fb-d8d1-30a6-a934-6f06faf07388 | -7.15153 | -48.44213 | 2026-09-23 05:04:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d23bad4-c6a2-35d5-a4e4-77b76c3696a8 | -3.81876 | -58.88689 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48d67b28-2ab6-30fd-9520-4249541757f8 | -5.45389 | -60.15306 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 726000fc-be6e-36fc-a0ba-4d01af1d7978 | -8.28265 | -54.77671 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e44d563c-5290-32b9-9b25-af87e2704c17 | -5.18367 | -49.33809 | 2026-09-23 05:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e26cbec7-f437-39a8-93be-6d20aae30007 | -8.82677 | -45.92889 | 2026-09-23 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad59f193-0a64-37f8-8f64-2bf3b4b02e37 | -5.21304 | -56.07668 | 2026-09-23 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 690954c4-aad2-305b-8a28-ad18c14c3d2f | -4.15011 | -60.79415 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0046e64-306f-3c4f-96ae-1b88de9edcf6 | -6.23511 | -51.00645 | 2026-09-23 05:04:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 26f8d08d-6167-3076-b248-e53a589c4092 | -9.52796 | -45.39941 | 2026-09-23 05:04:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2537ef9c-02c6-3112-a7ef-8c35262a43a5 | -11.64279 | -50.97691 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13b3fea5-fe9c-3870-963f-ecb73fd9e58a | -11.40872 | -44.02852 | 2026-09-23 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4a0284d0-7f51-303d-820c-63717c25c904 | -2.66807 | -59.91162 | 2026-09-23 05:04:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af1f3465-81ed-370c-aa94-3fda9e992277 | -7.30874 | -44.16996 | 2026-09-23 05:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67dc7e4d-37af-346d-95a9-91f0619e043f | -3.81665 | -59.01245 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 783098c3-7a34-3faa-b1fc-824ccd201fb6 | -7.42018 | -49.86194 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdf2cd65-f7be-3f9d-9fce-51943d19f482 | -5.57072 | -42.72805 | 2026-09-23 05:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 032a0252-3f6c-365e-a75b-59260ee36ac0 | -6.32531 | -51.85359 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2dbc118-a48d-37cd-975e-4be1996a40dc | -10.16347 | -47.67648 | 2026-09-23 05:04:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f61eb267-5583-3c57-85f3-dba3c4aff0d3 | -7.03276 | -44.65261 | 2026-09-23 05:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 12e7fb9e-044d-3e96-ac86-a9631943a68b | -6.9251 | -62.90794 | 2026-09-23 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d29e8b5-1ccc-3c59-9a1a-c9f524c4120d | -6.609 | -59.959 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 845636e3-4f2c-3d50-a4a0-e74decc2ed33 | -6.37562 | -42.78519 | 2026-09-23 05:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ba1767de-aba3-3224-adbf-a29dbb04745e | -5.61798 | -45.24898 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| e1e3d898-614d-357a-9fcf-3aaf0f1213b9 | -5.1843 | -49.33398 | 2026-09-23 05:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac53d094-9fdd-3390-abb2-ceddaa6a1846 | -6.64836 | -50.93042 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92403943-7d72-3f9d-a954-fad1a11d35e0 | -6.92565 | -59.63156 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45e62fc4-47b8-3a7b-9e07-4f0340fafd41 | -10.45536 | -44.94467 | 2026-09-23 05:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f85c5521-eab9-3f85-9964-0f8cfb4ae6bd | -7.49469 | -44.33064 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d49d6fe0-fef3-37b3-97ea-951b2fc370d3 | -10.4601 | -44.94857 | 2026-09-23 05:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ba4121f-b46c-38e8-bf17-4a7c4cbfdc6d | -6.1473 | -59.93581 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 450de2d8-b397-32d3-879b-4581296080a1 | -6.62373 | -59.93074 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 19a04f22-c1a7-39a8-a2b6-77edfb8f28c1 | -4.05531 | -56.31163 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1fe09ad-721a-3a19-895d-caee6a0d5487 | -6.34375 | -43.36993 | 2026-09-23 05:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 846ab5d1-cc3c-369e-9935-d2b11a5824c4 | -6.45337 | -54.98706 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2db0fd61-3ed0-387e-8a39-8797327549a3 | -6.13335 | -43.84143 | 2026-09-23 05:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9e1feb97-9c05-3dde-9713-7d92a22d85dd | -6.61021 | -43.74762 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 23646bdf-1142-373f-905f-a295c5f41489 | -10.049 | -50.21969 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f251f9a7-77b3-32be-8eed-b720658fdb8b | -8.18087 | -54.8215 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a6b8fa2-b773-3228-8330-312de131011d | -11.07342 | -49.73376 | 2026-09-23 05:04:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04939a07-c7bb-3596-ab59-27b532963eba | -10.25008 | -49.96574 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7db72eb-95c5-30b7-a854-283771907aba | -6.30099 | -57.73686 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 606fd9b9-6bd6-3803-a081-cd09334408a6 | -6.61323 | -59.95815 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ccd3533-8bd0-3cb3-a694-71bcc0e795cc | -10.71322 | -48.72188 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 712fdab0-f3da-39eb-a99c-ae1c4ba63d55 | -6.67102 | -55.06822 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2556b966-f41a-38c3-80c6-429b7782edc3 | -6.63313 | -59.93235 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a2dc0148-6604-3e1b-9618-a7cb983d6414 | -6.30733 | -57.74907 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40b6eeee-e6d6-3d0d-b34f-0e0515aaf131 | -4.08874 | -62.08087 | 2026-09-23 05:04:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9300ed9-c30a-32ca-9ac6-1f1bd59b39b4 | -5.83418 | -52.17645 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a337df9-1aa7-39c4-b831-40998ebb84ca | -8.45263 | -48.70819 | 2026-09-23 05:04:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1490471d-7779-32f6-bfa0-f84da2d33365 | -5.8181 | -57.73735 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 498cea90-1600-3e25-9f6e-13f6927dc4d7 | -9.10945 | -61.43813 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bd2e5845-2bdd-371d-8fae-c9c4a89a13ee | -9.16023 | -51.53276 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f80d1f76-d272-3571-a615-548c734aa283 | -7.23276 | -56.41895 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b96860a-5c4c-3cb6-b2ec-dc546c31262a | -10.2976 | -50.54514 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e42bb020-6a98-3b2f-967f-f8842974929d | -10.91381 | -53.95227 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b292b565-a6d0-317e-bdd6-ba8d96e1fe9c | -6.70183 | -59.95503 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1ab54d8-192b-3803-af33-2a41ee1e11a0 | -6.10746 | -57.67748 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7c3963e5-5505-38ce-9a25-303718232a2f | -11.6615 | -43.47482 | 2026-09-23 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45dc9d95-8506-3776-b492-b654ff8d1e61 | -3.29735 | -57.86023 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0495a35-fb95-375b-bb15-06dbdb6d658c | -11.77484 | -50.99902 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4478eff8-2c7d-37b0-8f74-c60c1e7246a0 | -6.00537 | -44.10972 | 2026-09-23 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0690ab91-e300-3ad2-a854-ed84194cba73 | -6.12951 | -51.70016 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8a8525a-54f1-3f9c-ba88-a2b41646515f | -5.87445 | -52.06886 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ea183e5-d897-3c4d-8475-37a6ed088e9c | -11.63922 | -50.97636 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d908d4b6-cca6-3158-afd3-0ace9af973ed | -3.83766 | -59.3858 | 2026-09-23 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a9847f7-3766-326a-89bc-54376bd023c0 | -6.74106 | -55.30525 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fba02f93-d623-3393-8bde-ed3546d39013 | -6.67452 | -55.0688 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d50fc932-a1e0-3bd1-911f-842a9eabd6c0 | -8.81434 | -44.26818 | 2026-09-23 05:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README81.md)
