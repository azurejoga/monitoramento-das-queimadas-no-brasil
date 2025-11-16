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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac9e6d36-742a-3990-b455-31ef956f681c | -4.39901 | -45.81933 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 2796e9c0-fa21-35f4-9fb1-0c99850097ce | -6.00013 | -41.92476 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| a68352b4-bdc2-34f0-9162-3a43dceb4438 | -6.57744 | -47.89336 | 2025-11-16 00:13:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bf2ccb94-ed4a-3dd7-a12d-76b4f307245f | -4.64744 | -44.6843 | 2025-11-16 00:13:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4168c2f5-1e00-3f42-a46e-4e58b92d35a3 | -7.13732 | -42.69674 | 2025-11-16 00:13:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| cc6dcab9-20a4-32d6-ac76-0d7b650dd5c1 | -5.42578 | -47.32542 | 2025-11-16 00:13:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bfbbd86b-11da-3719-947f-acbe3a99ce4d | -3.88861 | -47.19335 | 2025-11-16 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 88bc5b01-917d-3ee9-898b-c9a26bea0e99 | -3.96082 | -44.84934 | 2025-11-16 00:13:00 | TERRA_M-M | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 8f327ee1-02f7-3499-ae26-038fba99a525 | -4.12573 | -46.37741 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4dd3f396-ca2b-396f-8130-abb96dfde683 | -4.69775 | -46.30871 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 1b3ac808-67c8-3fb3-bb97-e9571c9b3637 | -6.5074 | -47.6244 | 2025-11-16 00:13:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d74edabe-3062-3783-be71-dcc61c62534e | -10.16693 | -49.32035 | 2025-11-16 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0e84e420-67b5-384e-8429-8de701608722 | -4.52291 | -42.17348 | 2025-11-16 00:13:00 | TERRA_M-M | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 7844ef45-184c-3fde-b0a6-97d37cd0dcd3 | -3.85045 | -40.77598 | 2025-11-16 00:13:00 | TERRA_M-M | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 33.0 |
| 41b1a699-efbf-3de7-a228-1523db75e723 | -6.45025 | -47.27594 | 2025-11-16 00:13:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 24e4d81f-2301-3ec4-b4bd-adbcdadc8ae0 | -7.71318 | -47.30223 | 2025-11-16 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3789f29e-301f-3f3f-9d6a-3b1a04ba89d1 | -8.31231 | -45.41103 | 2025-11-16 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 60e3cec5-5c66-38d6-a380-f3381e420a3c | -5.84281 | -47.68539 | 2025-11-16 00:13:00 | TERRA_M-M | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e1137f5c-e6a1-36ff-9087-aa07087810bc | -9.7403 | -43.94896 | 2025-11-16 00:13:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 2c506e13-67b6-37ab-8c78-963dbeff6c14 | -10.36277 | -47.33416 | 2025-11-16 00:13:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 88db2e02-4cce-3ec7-86de-f7679ad17c46 | -6.03563 | -48.18999 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 548c9bed-8bfe-344b-a397-a088780bc4fa | -8.06318 | -43.10119 | 2025-11-16 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 467.7 |
| d3f38860-7f08-3ed7-973a-d7e3e0de0f08 | -7.00938 | -45.16837 | 2025-11-16 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a65ed070-921b-324c-a10c-32b669207878 | -4.84003 | -47.54727 | 2025-11-16 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c720c94b-0605-3521-83fb-ee0b68f3bfac | -6.72233 | -42.9463 | 2025-11-16 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 7b2c73dd-904b-34e0-a71f-0e2576534886 | -3.95956 | -44.84029 | 2025-11-16 00:13:00 | TERRA_M-M | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 0ba0cce9-e72e-33c6-a28b-f548eeb685b6 | -5.47611 | -40.95833 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 62ac5c94-db13-3a73-9282-225f0f534dfe | -7.63224 | -38.93551 | 2025-11-16 00:13:00 | TERRA_M-M | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 53.1 |
| 8ef134c2-69a1-3f78-87b2-0cd0f368ad76 | -5.26902 | -49.3275 | 2025-11-16 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 78900ce3-2baa-398a-9b11-bf89545b3587 | -4.34879 | -46.31851 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 97e51cfc-a720-306d-9baa-51a358587205 | -4.58792 | -44.32819 | 2025-11-16 00:13:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 0a48110f-4b88-34db-806c-1ba14eca56ce | -8.20354 | -43.57037 | 2025-11-16 00:13:00 | TERRA_M-M | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5f4d2e62-da96-3ab3-bdf7-aaba951f827d | -6.81806 | -48.78508 | 2025-11-16 00:13:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f9a2e67c-24bd-37d9-85ac-057da4ce08e1 | -4.73543 | -46.38528 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 127.7 |
| ffe485c2-2355-31cd-8682-793fdcd65b47 | -6.92752 | -45.17686 | 2025-11-16 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7e00c001-88e5-3e57-b754-5385a1fdb06f | -10.00328 | -44.77488 | 2025-11-16 00:13:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 547a946e-d8f2-346b-a7d5-992b3b8a25c9 | -6.71482 | -42.12093 | 2025-11-16 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| e7357bc1-c936-3310-ba30-9ce3be06b8c3 | -10.54338 | -47.94627 | 2025-11-16 00:13:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ddf79a67-0ec0-31ab-8ced-306b92a90a2d | -6.6211 | -46.64049 | 2025-11-16 00:13:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 959907a9-7f8c-3b6f-bdc9-d2e97465bf01 | -9.83836 | -44.18554 | 2025-11-16 00:13:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 93129155-ef05-363f-9027-61d6cab643ab | -7.92402 | -47.10068 | 2025-11-16 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 599e2286-2a34-3da7-9497-5a9f3394df68 | -7.01699 | -45.15826 | 2025-11-16 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f4c771f5-0675-3f53-9442-06c57e16aacd | -3.93287 | -47.04649 | 2025-11-16 00:13:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 426e3b66-cbb2-3eea-af84-e2729c9863c4 | -3.13354 | -41.87634 | 2025-11-16 00:13:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 9958ebe9-220a-3d0b-8502-e7e78472a809 | -3.72535 | -46.0014 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| cc176ed8-7a17-3331-a89d-c4d4b47d03fc | -4.00143 | -44.28339 | 2025-11-16 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6d00d2d2-6501-3795-97c5-ee39aa87a330 | -8.86789 | -50.19771 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b6f24883-e327-35b5-b77e-060d37e4cf87 | -4.46612 | -46.30521 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 29bd3d8d-bea7-3d32-8f1e-59fd6d7e3a3c | -10.6647 | -49.36375 | 2025-11-16 00:13:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 580240c2-603e-33a6-970f-93aec0808a68 | -5.99836 | -41.91286 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 55.1 |
| 354ab3ed-ac21-32fe-a23e-40f4dac37c58 | -8.21258 | -43.56897 | 2025-11-16 00:13:00 | TERRA_M-M | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 99113381-5a8a-3a67-ac55-43c6be1babbf | -10.00205 | -44.76594 | 2025-11-16 00:13:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 4fe7929d-2bcd-3d9f-a3be-4dc4618929b5 | -5.4751 | -40.96426 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 28.3 |
| ec2cf67e-db3f-3102-9465-9b817377e735 | -6.67329 | -42.04559 | 2025-11-16 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 140.8 |
| 2ab13247-c44a-31fc-9d21-47b080942109 | -5.60834 | -46.36704 | 2025-11-16 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f2c20ba8-17c0-311c-85fa-b1f8df29bdb2 | -5.52632 | -40.99331 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 2eecf379-d114-38f7-a061-8f7c215aeab5 | -9.34837 | -46.60525 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 19cc2bfc-beba-31c2-a844-bb20c67c5f6a | -9.05891 | -44.7504 | 2025-11-16 00:13:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 8234e294-4744-3911-b7d5-8fe5bc95d325 | -5.96288 | -43.75126 | 2025-11-16 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| e4fed985-70e5-3a48-81cd-7b594735577a | -5.97707 | -47.99753 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 56be224d-f9aa-37de-96c7-29ebca1ca33b | -6.40023 | -42.2832 | 2025-11-16 00:13:00 | TERRA_M-M | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 311ab5e5-ed8e-3325-b3f8-8309b88ec79d | -6.21954 | -47.28014 | 2025-11-16 00:13:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| de53cc21-eb29-3521-ba24-46f4da1885f2 | -3.99548 | -45.89156 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1aa961dd-cfb3-329d-912c-75bb6284a20f | -5.52827 | -41.77747 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| d8a8e3c3-1cfb-30e0-85cd-1174a0cddc7a | -5.51538 | -40.99522 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 63b4f670-9b40-39f2-81b9-234560f1a6aa | -3.82094 | -46.02693 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 9252bce9-7156-38eb-aed5-e02f51f9d5d0 | -3.82215 | -46.03574 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d4f002aa-b9a8-3921-83d3-9781a77a42b3 | -3.99854 | -45.78347 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c3ea505f-80ca-372d-a2cb-36bebccf2c60 | -7.15427 | -41.76366 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 10461e5e-a149-381a-ba2e-e7793420aa69 | -9.72506 | -43.9696 | 2025-11-16 00:13:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| e4d85f5c-8a24-3b32-86a5-315692049bb7 | -9.8371 | -44.17657 | 2025-11-16 00:13:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 224ede71-3987-3507-8c83-b34e06c0e3c0 | -3.86703 | -40.64479 | 2025-11-16 00:13:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 9f0251bb-3787-3887-b921-479de15b1950 | -6.25678 | -47.08126 | 2025-11-16 00:13:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 2858c91a-38f9-3b29-9bb9-d8671a399b10 | -4.31037 | -45.63434 | 2025-11-16 00:13:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 09d0ea4b-f586-3b37-8a17-5b3cfb7bf21e | -3.991 | -44.27531 | 2025-11-16 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b4ef4b1c-55eb-3d1f-824d-79e6726f399d | -4.74433 | -46.38404 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 8122e901-3f13-301f-9e1f-79410da8399b | -4.62655 | -47.40279 | 2025-11-16 00:13:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 2eb30582-d9bc-316d-b352-6d918f17da0a | -6.70636 | -40.80674 | 2025-11-16 00:13:00 | TERRA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| f03d1996-8a26-38fa-91d0-f3b2970c15ab | -6.81069 | -39.13802 | 2025-11-16 00:13:00 | TERRA_M-M | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| ae6dd77d-6ff4-38fa-9ff6-bd72de1fa7dc | -9.71299 | -48.91588 | 2025-11-16 00:13:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 424f530c-ec91-38ab-99ad-d4b9442d5e7f | -6.77971 | -43.54187 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 6dd2d374-1e44-3dd0-ab97-3b9f7b5d1d8e | -3.64443 | -45.48297 | 2025-11-16 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3be54c9f-b40f-3b2a-967b-b65c9c46dae9 | -5.98819 | -41.91443 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 493a089c-fc17-35a9-9841-78d1310b20df | -3.79355 | -44.18062 | 2025-11-16 00:13:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| eae7554c-d62b-3176-a053-71925e5d7672 | -6.31193 | -43.81183 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 438d471f-e1b3-3164-97c7-a2f8961b5fb4 | -4.49346 | -47.65306 | 2025-11-16 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 36a459f2-8b1d-34c2-befa-3c24e8269d6b | -4.13385 | -45.36552 | 2025-11-16 00:13:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9c89202b-fa54-3d83-9a55-31058f9732da | -9.84738 | -44.71832 | 2025-11-16 00:13:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 888fad13-9a7c-39f2-971b-c175dc473c99 | -6.90226 | -38.88329 | 2025-11-16 00:13:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 42966ad0-53ef-3ef5-a99d-b8ca1003a3cb | -6.57884 | -47.90393 | 2025-11-16 00:13:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 0cf2a1c4-f1a2-3c8d-9d61-3484a6662dbb | -4.42066 | -43.39941 | 2025-11-16 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 677ab05d-0d50-3b96-9fd6-e1fdcbc0ae43 | -5.34671 | -47.21552 | 2025-11-16 00:13:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9f187b22-220d-33a9-8581-7d1d61d5be00 | -5.16244 | -47.41929 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 260398e8-a362-3ac1-bcb3-70daa3596ac4 | -4.02777 | -42.07727 | 2025-11-16 00:13:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 3d6cb84d-4402-3c88-a74c-9020b7db0c5a | -9.45385 | -44.86285 | 2025-11-16 00:13:00 | TERRA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5aa0054b-13c7-3369-ae2e-4c2dbfad7ff1 | -9.56164 | -45.72766 | 2025-11-16 00:13:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4880d7a0-35c0-336c-a726-20286b7c0a91 | -4.1057 | -50.7254 | 2025-11-16 00:15:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1b2b95f7-d332-374f-8093-918ae963d05f | -1.67005 | -47.40257 | 2025-11-16 00:15:00 | TERRA_M-M | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 33a9ffbc-7445-3810-a412-b2510b68d2f7 | -3.16223 | -45.73148 | 2025-11-16 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99a331b6-3acd-3a0c-b51f-94248114395f | -2.42142 | -45.70462 | 2025-11-16 00:15:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |


[Clique aqui para ver as próximas entradas](README8.md)
