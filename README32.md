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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cd41b12-f85c-30e2-a774-bfb7d58a4136 | -7.56059 | -42.67549 | 2025-10-14 04:25:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d1adbad8-520d-3c3a-9815-9f25ee0031c6 | -11.50012 | -43.48112 | 2025-10-14 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75cbbde5-8bb4-3776-8f0d-7302d090b9c6 | -11.51779 | -43.51595 | 2025-10-14 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73efd684-4ac5-34f2-8676-df2f6f9460b4 | -12.65842 | -43.43009 | 2025-10-14 04:25:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2055b467-3ddf-31ef-a7f9-1fab975dd746 | -12.85265 | -50.64423 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 727377e6-ec86-3754-b320-6a669fc24c65 | -7.75137 | -45.71041 | 2025-10-14 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b259716-acd2-351a-8ceb-893cdcce0e77 | -8.44106 | -46.18689 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b3867601-deff-38ab-9433-ed5c26252dd8 | -12.84193 | -50.66392 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8d65dab-e23c-3ab0-aaa3-78cfd557dfd4 | -8.42736 | -46.23104 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9cc43326-ecad-37a8-84df-666756ebaa6d | -12.82041 | -50.63852 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| dd5fc6c4-ba12-33b1-880d-3d379bda25fd | -8.4439 | -46.23363 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c76cbc2-5546-35e0-aa39-22427fd9edd1 | -11.74508 | -43.28422 | 2025-10-14 04:25:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 310e2196-f5ee-3b74-99a7-c06b008bd7c9 | -6.69384 | -45.97768 | 2025-10-14 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40458a53-009a-393c-8547-914eb4790b63 | -8.87803 | -47.97217 | 2025-10-14 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc1f057b-1105-3951-bb72-1a73422304a7 | -7.76179 | -44.73083 | 2025-10-14 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b14b036-22d4-3dc8-95e9-b81286445e87 | -12.62681 | -44.12355 | 2025-10-14 04:25:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14c8674f-c7fc-367d-a983-adba40a2921f | -7.03419 | -46.25471 | 2025-10-14 04:25:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11dcf2f9-75cb-3bd8-95c9-2dd4e01af149 | -7.90362 | -44.99395 | 2025-10-14 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4eccd03-e204-3590-bddd-b36d22fa3a45 | -12.73924 | -48.36441 | 2025-10-14 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2df734b1-2b94-3a18-ab9b-f626b73eba06 | -7.92757 | -44.13289 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3b0e43a9-1829-3097-b476-6c3583ca73c5 | -7.94726 | -44.12018 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 5fdf0ce4-c17b-3d2b-9789-6a3f6c4c7ac5 | -10.15619 | -44.91926 | 2025-10-14 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 91c1090f-4203-3a3d-bef0-a6bae7e8e957 | -12.8032 | -50.65274 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f55a49ff-c5c9-3cd9-ad04-f1fe5401bab0 | -12.17014 | -46.56893 | 2025-10-14 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e771f356-b91a-3e21-b887-7307513dc5bd | -7.64112 | -42.56885 | 2025-10-14 04:25:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 359a4e41-2cdb-3c16-8062-ac4f74ba1ed5 | -10.14565 | -44.55061 | 2025-10-14 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea742d59-f6e5-3cb3-bd8d-1ce4bc265628 | -5.73772 | -51.30779 | 2025-10-14 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 912c8e4b-5070-3863-8f8f-562b51e7914c | -7.02737 | -46.98358 | 2025-10-14 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 204ff0a6-3d21-3e96-a51d-2e8b2dfd492c | -7.76122 | -44.73449 | 2025-10-14 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c748c2e1-86d9-3a80-940e-84d83f9f4357 | -12.77485 | -50.6579 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b6c6101-ef9b-34de-8d16-69091aa9b353 | -8.44484 | -46.14114 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f1b327e-7a41-3b13-834e-adb5383c7550 | -8.44005 | -46.23658 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64cb7526-14b2-36a4-8d29-051bd1203bbe | -6.66315 | -47.74707 | 2025-10-14 04:25:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2386316d-bb8d-3cf5-a01c-fac4d0b2e50f | -8.45372 | -46.17105 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7117c560-cb51-3bc7-89c8-5c076dcc6572 | -7.75897 | -44.72664 | 2025-10-14 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b1f2839-905b-3b0e-ab2e-30570ad61a17 | -7.53383 | -42.70309 | 2025-10-14 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 082d956d-81fe-38b2-9136-42cd39dc4c0e | -13.38534 | -42.71397 | 2025-10-14 04:25:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 95e3c327-3217-3987-b6c5-3dee08a1bbf7 | -10.8231 | -44.00266 | 2025-10-14 04:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8eb14652-de8f-3e9b-9f6a-a3f2a1ee5e5e | -8.45313 | -46.15313 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63924c71-1f7a-3e90-a3a4-eafe5b27563d | -12.63044 | -44.12105 | 2025-10-14 04:25:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3a897d7-d46b-3ed7-92d2-c099a4cfa2f2 | -12.80464 | -50.64436 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a7901ded-c528-398b-a5d9-6a4024fbff72 | -12.68873 | -38.55416 | 2025-10-14 04:25:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f2484f27-d145-38d6-b352-a67112a46e9a | -12.82113 | -50.63433 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2ec5f13-c0e0-3b1a-9ef3-8db74e5affd9 | -7.91877 | -45.00744 | 2025-10-14 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bcce40f-7948-3fe7-8626-b4c406fd235a | -6.70882 | -46.529 | 2025-10-14 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eec6a158-85e9-3860-9def-76b6ba5322eb | -5.73834 | -51.3041 | 2025-10-14 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f01348f2-eef7-313e-9b4c-609fe968c9d1 | -7.38601 | -44.00961 | 2025-10-14 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5883f4c2-903c-37e2-98d7-5d7fb22e0119 | -8.43725 | -46.21122 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be47066e-f361-3a2e-bdae-280633c73d03 | -7.94438 | -44.11581 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f930f65f-c68d-3f59-86e2-4c79a26ea0f3 | -12.85694 | -50.64067 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d212b54-839e-34e2-b92c-cd4dde4c363e | -8.24045 | -47.8583 | 2025-10-14 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc2c9d5e-85ea-38b3-bc4f-7ecab8573b02 | -12.04909 | -54.24656 | 2025-10-14 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c60479c-ea05-3d91-8148-0099a850463b | -12.04373 | -54.25029 | 2025-10-14 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6349f8ef-7fdc-343a-a27d-efcfa06feccd | -7.31644 | -45.75573 | 2025-10-14 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e626565e-f066-3857-a0e8-909950083151 | -12.82901 | -50.65299 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f9fe2f2-0105-3ed5-be65-588cd3a8b76d | -7.94667 | -44.12402 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 7f601b2a-1637-3caa-9368-d1b90e8d352a | -6.37885 | -47.25982 | 2025-10-14 04:25:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d684e78-281f-33cb-b3c1-b81062c91d68 | -11.52297 | -43.51918 | 2025-10-14 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0398350-edf6-3b90-9f2b-6992049239ee | -8.08711 | -55.18114 | 2025-10-14 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78055d73-ada8-3c3e-88e6-04dfdd095427 | -12.81754 | -50.6337 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2914b271-9cc1-30db-b1e3-162f44d4708c | -12.80822 | -50.645 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a419cd3e-dbf9-3c2c-b874-435dd76bc5dd | -7.75615 | -44.72245 | 2025-10-14 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a083ce7c-a00f-3e10-9a1c-f716fe12329d | -7.76065 | -44.73814 | 2025-10-14 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f71b7bfe-c982-3ff1-aaf7-fe7602d12cc1 | -11.51977 | -43.50249 | 2025-10-14 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 920044dc-328f-3e1c-957e-7320417d0a2c | -8.43394 | -46.2107 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f341c384-497b-3bb9-b3be-98095206e061 | -12.61567 | -48.31149 | 2025-10-14 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b15f565e-7077-30d2-aecf-3db49dfdb8ee | -7.95014 | -44.12453 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e18d7b5b-cef4-3b58-9c5c-056c285deba6 | -12.8419 | -50.64232 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fe6d3e55-61cd-3dec-ab52-f248f95dfe8e | -12.81109 | -50.64982 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f263a34a-ed13-33bd-8129-516491bb2287 | -7.13488 | -42.49693 | 2025-10-14 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f7fe2bf5-11a1-37e4-8e1b-75906af2c7a1 | -7.91834 | -44.12362 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c90c3a16-1aa4-3f03-961a-bd31c840413d | -7.31199 | -47.8132 | 2025-10-14 04:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0a2c1bc-ca27-3950-847c-93eecd35a18a | -8.55091 | -44.58796 | 2025-10-14 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca730781-f085-3987-985a-85c9a34908e9 | -8.45041 | -46.17054 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ed3955e8-faf5-31b5-bec8-23cfdf3140de | -8.43277 | -46.1749 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5cc28a6-bc25-3c51-9385-a091fbde37ba | -8.45037 | -46.14913 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1965ce43-a60f-3b86-8382-42e01752322e | -7.92122 | -44.12799 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2fedb7bd-a022-394b-92cf-87f227a45472 | -12.61957 | -48.30846 | 2025-10-14 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8beaac74-e331-379c-b95b-1da96571e1c1 | -11.29282 | -44.02871 | 2025-10-14 04:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 74ecd247-c34d-314d-a3f3-40871eeef1ec | -7.75501 | -44.72978 | 2025-10-14 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc416a9d-2f65-360e-9ddc-8ee3e493dbcd | -12.84691 | -50.63458 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 85eff60d-8b76-3db8-90c6-241a1347a043 | -12.79747 | -50.6431 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8c4c1980-8549-3d9d-b9ff-c99d8f15c1e8 | -14.13404 | -42.69554 | 2025-10-14 04:25:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c012b386-14ae-3912-806a-7cdaf06a9de3 | -10.82072 | -43.99379 | 2025-10-14 04:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e03ff1af-b573-308f-a8a3-6cdaf1b75e89 | -7.94955 | -44.12838 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1e37d910-15c7-309d-ae16-3a8d1d9452a9 | -11.51911 | -43.50699 | 2025-10-14 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16fce78d-061a-3951-a930-37464b4b64aa | -7.9224 | -44.12031 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cba24c70-ab97-313e-b569-ee8187cc0d62 | -12.6268 | -44.12051 | 2025-10-14 04:25:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2a81189-b477-3c2d-a185-fff17e6bbc45 | -12.81539 | -50.64626 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dc84cff6-f5c3-3fc5-9cd3-3a8ec78c5b52 | -12.8326 | -50.65363 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffdd1f43-86e5-347e-8235-5e1e2a019dba | -6.66882 | -46.13659 | 2025-10-14 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5080683-aaf3-3179-bae6-21ee3b05b84d | -7.1674 | -42.19495 | 2025-10-14 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6dda2963-85b6-3e61-8b35-c14c16bb41bd | -11.54828 | -43.15006 | 2025-10-14 04:25:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cdbcf3e8-dda8-3282-a0c6-b3f9e16ac1f4 | -12.85552 | -50.64905 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46533239-d258-3c83-b0eb-0cc3f6ea06ab | -7.53753 | -42.70361 | 2025-10-14 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5a129096-e031-32f0-b811-9017ae5cff0c | -11.5217 | -43.52818 | 2025-10-14 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bef4b8ef-ec2f-3730-aeb9-4fbbba75f331 | -7.50008 | -43.05914 | 2025-10-14 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e9d0bbc6-7259-3d5d-abb1-2ba40696c1a0 | -13.53698 | -43.01068 | 2025-10-14 04:25:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 7942aee6-3b8f-3b63-973e-113b0ec54ff7 | -12.99887 | -43.99796 | 2025-10-14 04:25:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 243b8c65-51f8-354f-b920-ef9d8b6414a9 | -12.81826 | -50.65109 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |


[Clique aqui para ver as próximas entradas](README33.md)
