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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 637aac88-56fa-38e4-bc87-eef681e19daf | -6.70355 | -58.94923 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c0c11b5f-8455-3c22-8051-1aaa9d97464a | -6.61916 | -59.04916 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1397bbea-c128-39c4-9970-53e3b9c96226 | -6.72197 | -58.93878 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| db29f619-a251-3955-a108-261a027541e1 | -6.83412 | -58.97824 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 263844a9-c7ce-31ed-9954-791fc35db0e8 | -12.03946 | -46.44311 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e9ad190-40f9-305a-bc30-31ba3462f6d0 | -8.89731 | -60.59132 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 67e82cd5-aab9-3d75-b2cf-5d80c83ccf52 | -8.64847 | -54.70133 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1dff52c-1d09-3b74-b038-0116f01f0969 | -6.83373 | -56.41018 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4489f57-abb8-3140-82a2-b259c448bad5 | -8.90176 | -60.56383 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ea17abd6-f528-3e90-8cfc-aa90096afef3 | -10.46101 | -46.29566 | 2026-08-16 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac2233c4-34f8-3e54-a55f-66c38148615f | -6.84946 | -56.42669 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f08e86a8-757d-3bdb-a207-2560755ac871 | -11.10201 | -47.2393 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df00364d-dab6-318b-80cf-a6c830bc2a55 | -6.59413 | -58.99057 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43f3553a-bf8e-3618-a085-6be9fc8f7121 | -8.34595 | -46.53219 | 2026-08-16 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12a09fd9-d044-3087-859a-ff6df6a9a121 | -6.70051 | -58.9667 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5dfbb946-03e4-3240-96e7-221049304a26 | -5.25971 | -47.70302 | 2026-08-16 04:40:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b40a228a-53e5-38eb-9add-d84c1039783c | -9.49063 | -51.61222 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e32446f-455c-33bf-980d-d6daa742f6a4 | -8.99107 | -60.5996 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8786e3f-7b90-3f8f-908c-2c434b90e731 | -10.53844 | -44.85558 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d2f81c5-2888-3239-9bde-39599d9ffcf7 | -11.23038 | -54.82404 | 2026-08-16 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18d49e1c-0def-3d18-9df9-e60aa3f395a2 | -7.36848 | -46.81332 | 2026-08-16 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f42b6b4-9959-3223-af57-70c0784d531a | -6.63102 | -59.07676 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f077cf00-824d-3082-8fc9-5e46d464e6bd | -9.29858 | -56.80893 | 2026-08-16 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a543086-abd1-3a99-8180-6919f09d2af7 | -8.97231 | -60.50872 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 17e2b709-9b81-3088-9419-2f376420b86d | -8.65383 | -54.71775 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88a41f76-3fae-3462-9cbb-2c8af37a69b7 | -7.02756 | -45.91215 | 2026-08-16 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26aedccf-fb68-3e67-9e09-ff003b08dc4c | -8.95634 | -60.53073 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bf7095d8-ef25-36f6-ba87-b18e017660a4 | -11.35983 | -46.28357 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b83b189-3786-3c38-9473-818c7530c434 | -12.56913 | -47.85072 | 2026-08-16 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 421dd6f8-3a80-3109-aca2-084968152a35 | -8.64206 | -54.71571 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73d98b72-33d2-3a37-bb16-2150274e742d | -8.9008 | -60.60434 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6bebe39f-2d41-397e-bd52-7f25b8d0b009 | -6.85703 | -58.95787 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe6c3292-ba64-35f9-983b-b0ac07d52472 | -6.95847 | -44.23455 | 2026-08-16 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b45cad5d-3d13-3ad9-8dac-c6db52d551fd | -8.97355 | -60.53386 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b19b02e6-2508-36b9-ba53-1b17a14382dd | -7.22916 | -43.24994 | 2026-08-16 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c6be6a5a-b0da-3c18-854f-bb6efae17574 | -10.62629 | -53.89634 | 2026-08-16 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 344b43fd-55f2-3b55-a31d-b36aea2e6cfc | -6.98361 | -45.90009 | 2026-08-16 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af240813-7bce-3e85-83e3-89382cf71104 | -10.93827 | -57.11557 | 2026-08-16 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2acfbaae-e24e-31bc-912f-4ea817a31183 | -12.64473 | -43.90401 | 2026-08-16 04:40:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4b059039-bb3c-3ee5-ba31-1d0e70208b53 | -8.9601 | -60.51067 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bca48c20-c873-3b5a-8436-edba930d2d10 | -8.42997 | -62.66912 | 2026-08-16 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ab4f6e61-09b4-350d-a2f8-ac8f20e33b11 | -8.42738 | -62.67276 | 2026-08-16 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7c62199b-c815-394d-b0ca-e754befb1802 | -11.48768 | -46.60437 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 77196a09-1a08-393a-9e0e-5182b3005bf3 | -6.87977 | -44.97316 | 2026-08-16 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b72cf014-1054-3f29-a89a-7a31ef20a5b7 | -9.25867 | -56.9039 | 2026-08-16 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29813725-ec60-37ab-b313-6d30c1f98ed2 | -7.27465 | -44.67005 | 2026-08-16 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26ccb921-13ba-393e-ba68-9951a03ea0d0 | -9.48257 | -51.64071 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46cf0576-6af9-3fdc-b188-94c767b29d44 | -7.82379 | -44.10562 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a48f4874-31fe-3f3c-aafd-6da5ad683199 | -8.9571 | -60.52668 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 05c277da-b7b1-3707-8d6d-12137a2c007f | -11.89176 | -50.23116 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0fbb60fc-c72c-31c0-8efa-c96c9995bf66 | -7.22492 | -41.53422 | 2026-08-16 04:40:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 806971fc-b3d3-33f5-bacc-b12b96a9a795 | -6.82763 | -56.43792 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c0e589fb-a628-34fd-88ae-486999acc519 | -8.41123 | -62.65997 | 2026-08-16 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1b2f1b07-fcfd-3fc1-917f-0d69f691fe15 | -6.85321 | -56.43191 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6c835efd-0517-3b42-b2b7-741512271958 | -12.2788 | -45.90276 | 2026-08-16 04:40:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6bb862d-3e07-38c7-90c5-4d3e545ae1ab | -6.81926 | -56.46016 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e813f0b3-8d50-3b8e-8813-22ca771921f2 | -7.81959 | -44.10481 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2f45e18-92a8-3a94-bd42-4c6ede72eccb | -6.83145 | -56.41507 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d2b2b00-5990-3f62-a31f-d749a518f889 | -7.25722 | -44.6973 | 2026-08-16 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 03bee011-342b-3309-bc60-f902246e6bdb | -6.62621 | -59.07231 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 88a20ac8-3929-33d1-a2eb-bc5f9b23b9d1 | -6.62266 | -59.06086 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 553189a7-e13b-32af-8e7f-542d508fc118 | -9.37367 | -62.36398 | 2026-08-16 04:40:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 686e32e3-9bf7-36fb-9a63-73e3cd83c9bc | -9.35358 | -62.36534 | 2026-08-16 04:40:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 06d8e105-cd70-34db-8cf7-e1dae8bc3b12 | -11.30779 | -47.00282 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76f7ff37-c489-3542-a06c-37bb527495a2 | -6.62369 | -59.08645 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2fcc1684-5d5c-3d6d-8820-1574c058f50a | -6.7065 | -58.96416 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0990e72c-88cc-39bc-8fd3-3943172e22ff | -6.42852 | -60.07551 | 2026-08-16 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a4d62289-290f-3f7c-a228-5d08966d4612 | -6.83348 | -56.43824 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7686bad0-edf0-38c0-9cd1-076e24ec56ad | -7.40401 | -60.01434 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec9de5f8-1068-3da3-af0f-b6856cac431f | -6.8311 | -56.45188 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 37b4b5bd-16ab-3afd-84f7-b3640fd67dbf | -11.65127 | -46.54315 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 378a075d-2ec8-34eb-9e55-4e81ad599770 | -8.26586 | -57.34177 | 2026-08-16 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d9899149-b666-30a7-8820-87ee1831ab0a | -9.47347 | -51.62089 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bd84c7a3-f815-3c6d-87ac-6b9090628c3d | -6.84428 | -56.42176 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b99f788e-742a-391e-8368-29b3e2b94c23 | -8.95212 | -60.52166 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 555c0493-8e65-3849-bcbb-d0c18a43e538 | -6.86084 | -56.41469 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3322ead7-5ff0-3b47-b459-f8fe53bb7cb9 | -7.39476 | -60.00079 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 324a7393-59dd-3d93-a1de-f4c321216acc | -9.47489 | -60.50728 | 2026-08-16 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95e5634b-4bc5-3385-b172-21d303ae757e | -6.63829 | -56.39315 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cd699bd-14fc-3bc7-a9ab-69c994dd81f0 | -7.5865 | -45.01701 | 2026-08-16 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bdbbea79-18d6-3510-95a8-166143751c8c | -6.72317 | -58.93185 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8ef992c3-bd81-3540-be30-461302186022 | -6.36991 | -58.32004 | 2026-08-16 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d71fdad-ddaf-3664-b4c7-0ed8f5e25079 | -6.8284 | -56.43337 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b7de0c4-b676-3478-b2af-94d56b3c2705 | -6.59473 | -58.98708 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9304d625-f08b-3064-83db-ccf8df478932 | -6.72257 | -58.93533 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e7b04d08-4acb-3510-96de-68d8fc85345d | -11.45537 | -46.61429 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 215b5bfc-7d32-3934-8c63-f2b957a3c827 | -9.06006 | -45.78689 | 2026-08-16 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d03b7ee-009c-3c4b-8d44-6947b1dbe8f6 | -6.6335 | -59.06277 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a8930739-50c2-3fa0-9773-468098a4ba69 | -6.7166 | -58.93784 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2aa1dae6-44c3-3741-ac27-065a996915db | -6.85873 | -58.97937 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 77fc38cb-da6e-3d5a-9ce4-5254245919b5 | -9.26765 | -56.90539 | 2026-08-16 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8d4b645-89cf-3406-85da-9998853a2a45 | -9.47348 | -60.51502 | 2026-08-16 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eaff4eda-668a-39e4-861b-bb07954edf6b | -9.10588 | -46.39098 | 2026-08-16 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4979cf8b-ae14-3c7f-8bd7-e7bb60ce1e59 | -8.60168 | -54.66784 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29290138-d6d7-36f6-979d-60a13f835a8d | -12.4684 | -46.66487 | 2026-08-16 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d237c89b-f74d-3b27-87ef-5ee42a800bbf | -9.47062 | -60.51145 | 2026-08-16 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9256f6e-6ce1-38f7-b2f7-4d834093353a | -10.45721 | -46.29505 | 2026-08-16 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8948ee9f-e893-3bf5-94a5-89a72d3f17e8 | -7.02824 | -45.9075 | 2026-08-16 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bee4c12-9679-3a90-a1dd-6cb1a694284e | -8.65299 | -54.72284 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9448d30-96be-31a7-acfc-49f47ae77069 | -8.54523 | -54.59473 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README19.md)
