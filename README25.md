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
| 018b4556-f732-3175-8090-89d7c4ceefa1 | -6.6128 | -44.59853 | 2025-09-22 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 18288394-e7c4-33dd-8230-7c78816ab0d1 | -4.87241 | -45.80603 | 2025-09-22 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3582966-42e7-368d-b0bf-bd027d15805f | -5.5741 | -42.12378 | 2025-09-22 04:38:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bee2732b-8805-3949-b703-e38d1be2af64 | -10.34826 | -46.07415 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b0b3a60-1f74-38e6-8207-d17cea543554 | -8.17313 | -46.26529 | 2025-09-22 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a7d1ef8-58ec-35a7-bf82-dd3c552a4655 | -3.33472 | -50.08644 | 2025-09-22 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a22bea5-5998-3407-86a1-033c28b2bdad | -7.38053 | -44.57644 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02ad7b70-bb89-30cc-8451-b7b91766ec16 | -8.03983 | -54.89412 | 2025-09-22 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e4fd76f-adb0-3296-99b8-adfc2820bf73 | -7.8063 | -46.19917 | 2025-09-22 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1348f8cc-6d0c-30d5-bef7-e22cde4c80ab | -4.31445 | -48.09253 | 2025-09-22 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 662b9079-9337-3e0e-adde-e90e934af2e2 | -5.83225 | -49.02689 | 2025-09-22 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b1e41ed-ccf1-3578-a260-0cfcf5e48397 | -7.71007 | -55.45142 | 2025-09-22 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4f062a6f-5f91-3b6a-9c24-d55e88ee1156 | -5.10895 | -46.16663 | 2025-09-22 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3e94706-74f2-3651-b87d-f5994a8be8db | -10.35036 | -46.05982 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b8b74de-7993-3216-a21d-b7ec70d510e7 | -9.98819 | -46.23802 | 2025-09-22 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8030119f-ea88-3c60-a469-6d415cbcf3cb | -7.93989 | -44.10651 | 2025-09-22 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04b2d60e-ae17-30f7-a74b-a05c68fafa2e | -7.34811 | -44.45522 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f0d649b-739b-3b5b-9c66-bd1e6d11adfd | -7.44076 | -40.10461 | 2025-09-22 04:38:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 34464ceb-c0f5-35fc-94ee-5bff379b5ae3 | -7.94161 | -44.09482 | 2025-09-22 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 430bcfd2-ea92-3ec7-bcc0-6599b6c60ac4 | -7.61373 | -44.48623 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 519a686f-cd55-39f3-8165-ee94691670a9 | -7.28829 | -46.11641 | 2025-09-22 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 163d701e-e1cc-3981-9150-f940019fd11c | -3.48497 | -52.81121 | 2025-09-22 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1d42a80-0467-3764-93dc-946b093d31d2 | -10.37001 | -46.05002 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63e0bcca-52fd-3fd8-9bbe-1fd0bceb8fa7 | -8.29951 | -43.67799 | 2025-09-22 04:38:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a110427-3609-301f-9454-2a8d88ce3e24 | -8.85106 | -43.02379 | 2025-09-22 04:38:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3c34904f-b959-3921-a041-8d17814e325e | -3.43111 | -50.28144 | 2025-09-22 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55a3d792-443c-3d11-b214-528c6ac6c356 | -6.44964 | -45.67848 | 2025-09-22 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ef63010-a458-37e5-8b22-113fc20ea4c7 | -9.16452 | -44.61914 | 2025-09-22 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c78a7a2-9559-314c-a1e9-1955e8012519 | -10.40802 | -47.85431 | 2025-09-22 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a584d43-7e70-3abd-abdf-2cc72e8ee1e1 | -3.32742 | -50.08894 | 2025-09-22 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec686f2e-816c-397f-bb5f-58cad970a0ef | -8.0129 | -45.71895 | 2025-09-22 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b0d60e04-ffdb-3a7b-a389-b3a0e8231922 | -10.39523 | -46.09261 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34c5c474-548f-33dc-bbb9-870da574bdc9 | -3.84357 | -55.60107 | 2025-09-22 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 605ccd4c-db73-3310-9ed6-467143408adb | -7.6073 | -44.44422 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1cafa3d-fac1-3858-8581-ba3a9e4b8019 | -5.64932 | -51.46601 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97a2cf44-2787-3841-96b6-e993fb1c101d | -7.93265 | -44.09747 | 2025-09-22 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0c1892c-0cac-3681-817a-48758776a387 | -7.69193 | -44.8863 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e416ffc8-33ad-3a2c-a578-e5b5b9fc4c32 | -3.59478 | -58.58997 | 2025-09-22 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d60d557b-d4f5-3fb4-a715-e83f2ea7ba70 | -7.54617 | -44.78317 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ef994e3-08f4-3931-841a-b26169add4dc | -5.64586 | -51.46545 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24ba2cb2-14dc-33b6-881f-c5c630de7481 | -7.93208 | -44.10138 | 2025-09-22 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4874d690-9fb8-3d99-9c08-774b37fde53f | -7.96139 | -43.90094 | 2025-09-22 04:38:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98286718-d00b-34ae-8708-d8272e2db192 | -3.59542 | -58.58625 | 2025-09-22 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6581ce6-a24a-338b-acaf-232cbe5930c6 | -7.81429 | -46.19604 | 2025-09-22 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4b727aa-e5bc-3d4e-88ab-e127eb8b3fe4 | -5.5837 | -49.2463 | 2025-09-22 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52412f9e-f345-3d0b-9761-2ff007d70db8 | -10.36934 | -46.05475 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fea56673-54f1-3beb-81a9-552c9bc83024 | -7.91265 | -43.8774 | 2025-09-22 04:38:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 26cc184e-49e7-3781-9bd8-6186958caa67 | -5.56176 | -46.28104 | 2025-09-22 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72ab1e42-aa9d-30f1-a16c-2fa5e88c416d | -5.65687 | -51.46331 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 593c8a7b-30c8-3aec-a558-5daab040cc19 | -7.36286 | -44.55611 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9541afd8-d87a-3cea-a8ce-b2cdc053c60c | -7.37345 | -44.56846 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9073d39b-b199-330f-ba9a-565973e15225 | -10.36868 | -46.05946 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ee519eb-1bad-3626-a855-e7ccf3a90321 | -5.41685 | -51.44899 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f4a0311-7de3-345e-9830-2b733d445b49 | -7.60507 | -44.48861 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c16c1799-8ce7-3e9f-82d4-585ebc1fb95d | -5.57025 | -48.98562 | 2025-09-22 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ccfe1f7-aff3-3168-bfbf-36e7e39d4f44 | -6.05013 | -46.39537 | 2025-09-22 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66f5b493-08e7-309f-9dfe-44c4e25290d9 | -3.55429 | -52.20287 | 2025-09-22 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a545fc91-c1d6-3261-ae37-0cb3e38f1209 | -8.02426 | -54.88779 | 2025-09-22 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d107755-ffab-32c5-bfc4-7161a92743ba | -5.33316 | -44.82397 | 2025-09-22 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7743297-695c-36ee-9cf5-74219ea0590e | -10.3768 | -46.0849 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c448076a-a4b9-3e38-bc36-ea316059a53f | -5.77743 | -50.20938 | 2025-09-22 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bac0e24-03d4-3a85-b4ba-3631f4990b7e | -7.80324 | -46.19447 | 2025-09-22 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e841616-4998-39b6-b4f6-e0b63ef40258 | -7.21998 | -43.74609 | 2025-09-22 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a35b844-7884-35ac-8658-5be40a7091d7 | -6.6161 | -44.60377 | 2025-09-22 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a0a6cd0-da79-3ba5-b676-6fa52387e798 | -7.2279 | -43.7513 | 2025-09-22 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c6e37268-2555-3a7e-84e2-31ceb67a06ce | -10.46781 | -48.03415 | 2025-09-22 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80026762-118c-3333-9cc2-b6b17f664db0 | -3.32685 | -50.09253 | 2025-09-22 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8fba815-c646-3552-8cbe-e795b4c47709 | -3.78371 | -51.93752 | 2025-09-22 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f29b1c34-4889-32f9-808a-f787343bebf5 | -7.60966 | -44.48559 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10b40e36-50ca-3adc-8773-3832d93f4da1 | -6.44392 | -45.69131 | 2025-09-22 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0eee3f8-d4d3-3c0f-abc1-db8ef836b691 | -8.00841 | -45.72308 | 2025-09-22 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12469a58-68ec-30c7-aa1a-482564f7ce55 | -10.38063 | -46.08548 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2221e20-f94b-3377-baa9-6f7bd3de385c | -5.83556 | -49.02741 | 2025-09-22 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c1a48cc-1c4c-3615-8f9c-84d09541a07e | -6.6247 | -62.93178 | 2025-09-22 04:38:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95e05c5b-d54e-3b34-beac-cb484d363f4e | -8.03234 | -54.88921 | 2025-09-22 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e92d7674-900a-391c-9dc3-6dacb9f1368b | -4.31554 | -48.08554 | 2025-09-22 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d6a3740-a3d4-3657-8583-8c79cc174003 | -6.38906 | -50.906 | 2025-09-22 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29c5f050-9206-3ab7-9ede-cd7c516bd5ee | -10.25129 | -46.06989 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 98b54945-8f5f-376c-a8e5-82d8cd7bc395 | -8.85098 | -43.02654 | 2025-09-22 04:38:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 002decca-905a-379f-96f7-7ff56ecc030c | -5.39443 | -48.63511 | 2025-09-22 04:38:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8259c1ae-9ff0-3a98-8d2e-fcfd33ff2010 | -5.69192 | -51.76084 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ba5a3a2-78ad-3779-87cb-80a50b405894 | -6.89965 | -44.77188 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f6a7027-980e-3531-b1cf-8d5334d3386a | -5.56219 | -51.79757 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd3188e5-4d96-3dac-93bc-d831205c322a | -7.54667 | -44.77969 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63748702-d9aa-3bf4-b79e-5df73f2050ce | -7.51229 | -43.69182 | 2025-09-22 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5324388c-84da-3316-be1f-18489e6071fe | -3.69761 | -49.57191 | 2025-09-22 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 17ee3fe7-20ef-3711-9dc6-f6bdea86a50e | -5.57874 | -42.12449 | 2025-09-22 04:38:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 10431d12-bffd-3009-9d05-af66973282ae | -7.44143 | -40.10439 | 2025-09-22 04:38:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3a48ddcf-36b9-36ef-8192-8972c86444a6 | -3.94901 | -53.38945 | 2025-09-22 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e885a340-cc70-3c2d-a0a6-04f27c0397fb | -5.5734 | -42.12866 | 2025-09-22 04:38:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 465ba768-d7d6-36aa-b534-d3a6f5d8858d | -7.94046 | -44.10262 | 2025-09-22 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cee9d3fe-8211-3d19-80d4-8a939dbc6b73 | -6.39128 | -50.91373 | 2025-09-22 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba8bae71-419d-3f18-adfd-1748a0d23c4d | -9.70165 | -47.63116 | 2025-09-22 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d67faafe-24ee-386b-8c4b-7240527dbf0d | -6.04006 | -44.1393 | 2025-09-22 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6f2348eb-e9d2-3c63-b22e-be484697db8e | -10.3542 | -46.06033 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c601ecfb-6fe9-34bf-976b-5ce124b7f80a | -6.90117 | -44.76143 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 07e9aaa2-0746-32c1-a617-b644314d17d1 | -3.75927 | -54.81549 | 2025-09-22 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c11e1aab-c522-336c-a67f-3832bafea14d | -5.10958 | -46.16255 | 2025-09-22 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d72d6a9-2409-3d8c-8270-140509b95a62 | -10.38129 | -46.0808 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17c0de05-aa1f-3fbb-b063-79046e4dcf8a | -6.50814 | -46.03815 | 2025-09-22 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README26.md)
