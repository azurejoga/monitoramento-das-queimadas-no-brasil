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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 250ae952-337d-38e0-8ab0-9ad28d83ec8d | -7.2031 | -43.0701 | 2025-06-20 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 7be49230-135a-34c4-bbcf-d8b02db9e83a | -11.1274 | -46.6598 | 2025-06-20 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 0414a063-4714-3e6f-a0b5-a4ecf664c36d | -11.9518 | -58.7574 | 2025-06-20 01:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| f608f90e-d873-3db8-aa92-64b527e24b4f | -11.1465 | -46.6573 | 2025-06-20 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 1bd1343d-13f1-34b3-ac2c-5879f68bea6a | -7.2217 | -43.0917 | 2025-06-20 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| dfe8163e-b44d-3798-9d82-b977b6a7cb6a | -9.4648 | -57.8449 | 2025-06-20 01:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| a6c48634-9f76-3536-adc1-5c4288a95748 | -11.952 | -58.7376 | 2025-06-20 01:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| c5ce69c3-b6d4-30c1-9c98-fc416e411cba | -7.2222 | -43.0447 | 2025-06-20 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 82cef2a4-8160-3952-88cf-acad0fabdbd2 | -19.7784 | -48.3011 | 2025-06-20 01:40:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 76276e20-18a6-3420-8ab6-8feab70c7f2e | -14.0404 | -53.3669 | 2025-06-20 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| d52f6d70-031f-38c1-b1ee-bb1634a94cdf | -9.4807 | -56.0801 | 2025-06-20 01:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| f86618e9-78d5-33e7-8149-c2f4084fa1e6 | -16.2852 | -58.2697 | 2025-06-20 01:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| ee4f3b94-f30e-3525-b282-89edec97e913 | -19.7587 | -48.2824 | 2025-06-20 01:50:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 57d5d23b-7d4b-3deb-9622-dc467484265c | -11.952 | -58.7376 | 2025-06-20 01:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| c2bd09e7-6aaa-3f48-ac9c-cc7ed78ace4e | -7.2219 | -43.0682 | 2025-06-20 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 225.6 |
| 53c44f9d-c872-3342-88bd-1c0600ca97a5 | -16.3047 | -58.2676 | 2025-06-20 01:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 198.4 |
| 52ab5102-c1a5-380a-aa2c-79ff24dfb9b8 | -9.4648 | -57.8449 | 2025-06-20 01:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 47955133-88f0-3951-a92b-e99d0e37f0f4 | -14.0404 | -53.3669 | 2025-06-20 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 4f8ded6e-3044-3c3c-a5de-70ccd36262ba | -16.305 | -58.2474 | 2025-06-20 01:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.5 |
| 4d30c145-5063-3f07-9b22-5aff91ac16f1 | -9.465 | -57.8252 | 2025-06-20 01:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| efdf2d27-3e86-38c4-ab76-9e0eaee1befa | -11.9518 | -58.7574 | 2025-06-20 01:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 4b8ef89d-27e9-3356-a73e-577b15943071 | -7.2031 | -43.0701 | 2025-06-20 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 65f9f709-095c-3ff0-8264-1b227cd4b38d | -7.2217 | -43.0917 | 2025-06-20 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| a886d354-e2c7-33b6-83bd-f7ad5bde3282 | -9.4994 | -56.0788 | 2025-06-20 01:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| fdcefb6a-8109-3d6d-ae04-2ac0664cf9c1 | -11.1274 | -46.6598 | 2025-06-20 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| adba5b22-13fb-3fef-aa04-139be472717b | -19.7791 | -48.278 | 2025-06-20 01:50:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 678206ae-add6-3be6-9a9f-24ac76378a53 | -9.4648 | -57.8449 | 2025-06-20 02:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| fd781e37-99e3-3ec3-a7e8-67aa3aedaff6 | -11.127 | -46.6823 | 2025-06-20 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 29943f44-8bcb-355c-b8b5-b4b5904bf52c | -16.3242 | -58.2656 | 2025-06-20 02:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 33ebd33b-0909-327c-a433-1ae657b1bab1 | -11.952 | -58.7376 | 2025-06-20 02:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 8f0f206d-499f-305a-9f4a-511f619fadd8 | -16.3047 | -58.2676 | 2025-06-20 02:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 145.8 |
| dd7b08c2-259b-33f2-b1d1-4cee605d697f | -7.2031 | -43.0701 | 2025-06-20 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 427ab695-6d24-39e6-b1b2-d706c3b02a0a | -11.1274 | -46.6598 | 2025-06-20 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 1b80fe98-98f2-38a8-994b-5f8fb1f44b4f | -11.9518 | -58.7574 | 2025-06-20 02:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 578bba3c-be71-3818-af0f-a59a350ee0ba | -9.4807 | -56.0801 | 2025-06-20 02:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 3a2aad2c-c732-34da-bca9-ccff9fefe1c0 | -16.305 | -58.2474 | 2025-06-20 02:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| f6d9f6ac-5711-3c73-9e6a-4ef620fe94ab | -19.7791 | -48.278 | 2025-06-20 02:00:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 77f90693-0761-3e26-bda5-d349b6f2aacd | -7.2217 | -43.0917 | 2025-06-20 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 11458f16-4bbd-3e04-ad38-8c76171c41c8 | -11.1465 | -46.6573 | 2025-06-20 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 44a794f0-d994-36d1-a784-9742c171a6d3 | -14.0404 | -53.3669 | 2025-06-20 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 3cc704af-f159-3352-9078-470c268ca295 | -7.2219 | -43.0682 | 2025-06-20 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 169.1 |
| b318202a-e20c-31b5-9559-aef37982c93b | -19.7587 | -48.2824 | 2025-06-20 02:00:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 63.8 |
| d8fef943-60e0-3d59-bc1b-e5826aac06a0 | -16.2852 | -58.2697 | 2025-06-20 02:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| f716d4e9-fd32-3356-a639-71d377209afd | -9.4648 | -57.8449 | 2025-06-20 02:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 432f649f-ab06-37cb-9fef-b0a81a6eb7de | -16.3242 | -58.2656 | 2025-06-20 02:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| d209e452-1beb-30c6-b936-080b0cabadb5 | -16.2852 | -58.2697 | 2025-06-20 02:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 1b5bbfac-14af-3711-8023-4e6d99a3d8d5 | -19.7791 | -48.278 | 2025-06-20 02:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 52.3 |
| db7dc214-c920-32e1-8e59-49c7f7be4f87 | -16.3047 | -58.2676 | 2025-06-20 02:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 162.0 |
| f7567549-8333-3d22-8d18-ac9d4a74d731 | -7.2219 | -43.0682 | 2025-06-20 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 158.6 |
| 6f9653b8-7334-3aa3-b84c-a7473ab4830f | -9.4994 | -56.0788 | 2025-06-20 02:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| e9be3b15-0973-37a8-b08b-cc4783f25c93 | -11.952 | -58.7376 | 2025-06-20 02:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 3377c4b1-6166-3aad-b550-244458c9e20e | -11.9518 | -58.7574 | 2025-06-20 02:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| d489ea55-e575-3f5b-800f-e1b86e486f8f | -7.2031 | -43.0701 | 2025-06-20 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| d9bbc62f-a20b-3dc0-a603-86493f4ff713 | -14.0404 | -53.3669 | 2025-06-20 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| b4125d4b-76dd-33c6-8c0c-5653be83b01b | -16.305 | -58.2474 | 2025-06-20 02:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.4 |
| 11875ba3-b0b6-31b1-9bdf-e7f6250e1dc5 | -9.4807 | -56.0801 | 2025-06-20 02:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 798c7fb5-3541-3d63-8696-7952908a4ef0 | -16.3047 | -58.2676 | 2025-06-20 02:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 140.9 |
| 459cd451-299a-304c-8a3d-c60b250a8858 | -11.1274 | -46.6598 | 2025-06-20 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 715fa3ed-f1f1-3ed7-bf75-a901af0a7198 | -9.4807 | -56.0801 | 2025-06-20 02:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 1b9f147a-fe10-336b-b16b-e59707f24c42 | -16.2852 | -58.2697 | 2025-06-20 02:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.9 |
| 0ba6e594-2493-39dd-b0b7-1a3ad3b44e9a | -11.9518 | -58.7574 | 2025-06-20 02:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| ebe04df1-2d4d-3453-a148-d860cb6cf3c6 | -14.0404 | -53.3669 | 2025-06-20 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 91441187-d733-32b4-869a-e5471a2c6c24 | -7.2219 | -43.0682 | 2025-06-20 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 124.7 |
| 58f6bdd6-cd83-3cd2-adc4-5709879067df | -9.4648 | -57.8449 | 2025-06-20 02:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c231ea05-4395-3541-9c4c-01ce673145b2 | -7.2031 | -43.0701 | 2025-06-20 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.4 |
| ade04f68-4cd8-38a3-858a-c1dba914a739 | -11.952 | -58.7376 | 2025-06-20 02:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 22aa1bec-2660-3cab-ae7b-2a84876f22ba | -16.305 | -58.2474 | 2025-06-20 02:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 9262902c-f1bd-36bc-9afc-40986586b4f6 | -16.3047 | -58.2676 | 2025-06-20 02:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 160.5 |
| 4fa11956-f12c-3eec-bfec-2ae37dbcbbbe | -11.952 | -58.7376 | 2025-06-20 02:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 5ad1bc35-4f75-3c50-acda-643669807b49 | -9.4807 | -56.0801 | 2025-06-20 02:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 6bdd8c15-7c38-3670-99be-451801d54c77 | -11.1274 | -46.6598 | 2025-06-20 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 0f8cfa7d-e83c-3910-9311-943490283f77 | -14.0404 | -53.3669 | 2025-06-20 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 3a4b2e44-23f8-35e7-8004-c6d86f02e37a | -16.305 | -58.2474 | 2025-06-20 02:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| bff5bd1c-ccc2-3b1f-8c47-971967eba179 | -11.9518 | -58.7574 | 2025-06-20 02:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| f7dfecf0-7850-38bc-baa8-eef56a823639 | -7.2219 | -43.0682 | 2025-06-20 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 141.3 |
| 17e06b9e-b8fd-3c14-9279-0b395accd053 | -11.127 | -46.6823 | 2025-06-20 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| e1d48a49-dd76-3f80-858a-48320308a0cb | -11.9518 | -58.7574 | 2025-06-20 02:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| d80871db-df17-35a4-b4f1-6ba559d834a2 | -11.1274 | -46.6598 | 2025-06-20 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e3ed262b-86be-3688-92df-6143c45b45dd | -7.2219 | -43.0682 | 2025-06-20 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.1 |
| 34faf571-e658-31ce-9c3f-7a119e787675 | -9.4807 | -56.0801 | 2025-06-20 02:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| e5652b42-50a8-368a-8146-33a11f3da151 | -11.952 | -58.7376 | 2025-06-20 02:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 0239afce-8ed9-3022-a8d3-4e289ef3192c | -9.4648 | -57.8449 | 2025-06-20 02:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 4865b7f3-adec-3450-a488-d8ce77c25564 | -9.4807 | -56.0801 | 2025-06-20 02:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 20d2ff28-dc72-3620-ba2e-6b2eeb0d65b0 | -11.952 | -58.7376 | 2025-06-20 02:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 94399e7c-2db6-3e2e-8615-a42a5eb7905a | -10.4944 | -47.0302 | 2025-06-20 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 89e2fac5-0228-3049-a43a-6109d39e73a2 | -11.9518 | -58.7574 | 2025-06-20 02:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| bb0cd7fa-2281-38fe-b28e-2de951acd10d | -7.2219 | -43.0682 | 2025-06-20 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.7 |
| d7dbc52b-e987-309d-b79f-52ccd6b53696 | -7.2219 | -43.0682 | 2025-06-20 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 31bd82f1-7b25-355a-84e9-6d2aa4758cf9 | -9.4807 | -56.0801 | 2025-06-20 03:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| ac2eaa19-4a5c-3d97-a791-b965342b1663 | -11.952 | -58.7376 | 2025-06-20 03:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9e85e9f2-b666-3749-87eb-fba0f0c5672f | -10.4944 | -47.0302 | 2025-06-20 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 373.4 |
| c0fe6c18-ed93-362b-85b1-05a3cf670936 | -10.475 | -47.0548 | 2025-06-20 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 268.4 |
| c6c482d8-4319-3941-8e40-650792e5a318 | -10.494 | -47.0525 | 2025-06-20 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 2713520f-e7c2-3c44-931e-4d5c49a4d655 | -11.9518 | -58.7574 | 2025-06-20 03:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 8e587142-6f03-3d32-93c8-b24280d7cc9c | -10.4947 | -47.0078 | 2025-06-20 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 7dbb0fef-7e57-3ad8-a379-2413aaa76ce5 | -10.4754 | -47.0325 | 2025-06-20 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 225.3 |
| 4d30e242-0bee-3599-a79f-8f6faaa9079e | -9.4648 | -57.8449 | 2025-06-20 03:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| e569d4d2-bccd-3233-b70d-1b308b0d30c6 | -7.2219 | -43.0682 | 2025-06-20 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 3e1965d3-2f63-3e25-b8ec-9eb3bb3063b4 | -10.475 | -47.0548 | 2025-06-20 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 195.8 |
| 1e6d6e4b-59db-3ed1-92e4-81c7909b380d | -10.4944 | -47.0302 | 2025-06-20 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |


[Clique aqui para ver as próximas entradas](README6.md)
