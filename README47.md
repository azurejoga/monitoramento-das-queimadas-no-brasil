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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcd7dc15-295d-3128-b5c3-dd1e1a4c3a5a | -7.68187 | -49.86333 | 2024-10-24 04:34:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0073f7a3-c5be-3116-9182-cf28c1fcc318 | -7.53166 | -49.26896 | 2024-10-24 04:34:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 916d703d-85c9-3ed1-aab3-cf7d8dd77041 | -7.36132 | -49.58749 | 2024-10-24 04:34:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfba29aa-8469-34f5-b03e-5052e7f0ad61 | -9.31689 | -49.40881 | 2024-10-24 04:34:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6997913f-e1e0-3bbf-8de4-3590f3627d65 | -9.31373 | -49.40839 | 2024-10-24 04:34:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46d3ab9d-443c-3d01-8ed5-cb61720b2367 | -9.2743 | -49.63494 | 2024-10-24 04:34:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e3142a7-b7ee-3c9c-9d45-b99fae61b19a | -9.27336 | -49.57632 | 2024-10-24 04:34:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42a708e6-27ee-3a1a-af49-ef4168a8d8da | -9.27002 | -49.57579 | 2024-10-24 04:34:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2840e4c2-32e6-3d55-90eb-68f339f043e2 | -9.26669 | -49.57526 | 2024-10-24 04:34:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0f08ad4-0fcf-3c45-b312-ea6a37794f1c | -9.26612 | -49.57882 | 2024-10-24 04:34:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b6b380a-1a31-3c1d-918a-25dcc8c475ce | -9.17066 | -49.8314 | 2024-10-24 04:34:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7fe5549-b6f1-3519-9a91-bd89921e9b03 | -9.16469 | -50.06113 | 2024-10-24 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ceca3950-484d-31a5-a9c3-d18c2009ac83 | -9.0022 | -49.18441 | 2024-10-24 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffe55308-d771-3f06-8770-af0f2314b4cf | -8.58373 | -49.22504 | 2024-10-24 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8137b58-8229-3aa3-8feb-62ae1e76e52f | -8.58125 | -49.22036 | 2024-10-24 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5e4c051-9ae9-3d1e-9e0a-c9333db063db | -8.58069 | -49.22388 | 2024-10-24 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2728fc49-38f2-37ce-8092-e88256d6a208 | -8.57792 | -49.21983 | 2024-10-24 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0f64583-0fd8-3ad2-91da-412150a71ade | -8.57736 | -49.22335 | 2024-10-24 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf5acee3-3709-39d9-ab7e-7f1232cd4107 | -8.5746 | -49.2193 | 2024-10-24 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3bde9923-df5c-30e3-beef-65cfdadbce9f | -8.54072 | -49.55632 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9963afa5-1e58-3089-ad26-925aa3f43c5e | -8.46703 | -49.52922 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd8f9ab4-4f83-357b-9410-d4d5665ee82a | -8.3926 | -49.96957 | 2024-10-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69f61bba-4ba4-30c2-9b02-94d5967a8945 | -8.3904 | -49.9617 | 2024-10-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e8ac083-ffd9-3f51-99c9-98e6a2e327b3 | -8.3898 | -49.96536 | 2024-10-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f8a9344-b02c-364c-bbd1-9e6a304033b3 | -8.38921 | -49.96902 | 2024-10-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ada921b4-b602-3345-9158-8a51917b1e43 | -8.38642 | -49.96482 | 2024-10-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddaba42f-d0fc-3e20-a468-b901019b8f3e | -8.38582 | -49.96848 | 2024-10-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3338c7c2-b5e7-31ce-a104-73424cb4799d | -8.33981 | -49.98771 | 2024-10-24 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d74d9ae8-684a-35ef-b75e-8f62bad576d5 | -8.30996 | -50.13049 | 2024-10-24 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 830ae916-7782-3933-843e-1cd72a5910af | -8.26195 | -49.47088 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2928b403-5530-37e9-9c09-ebeb1a97be0d | -8.25803 | -49.47392 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3f4daac-aad7-34e8-8df2-9906736cdac7 | -8.22214 | -49.91253 | 2024-10-24 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bff8cca-afca-38bc-b605-b3394beff3a7 | -8.19492 | -49.67346 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f421d0d-f7ce-3bac-9cf8-f8ef09a0076a | -8.19214 | -49.66931 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a5f5fca4-dee9-3b89-bbea-c5dc6e40c962 | -8.19155 | -49.67293 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d676f68-9b23-3533-b1f7-02577d2328c2 | -8.15352 | -49.29639 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2613dfbd-5f13-3c7c-b981-f8331dc1c511 | -8.15295 | -49.29993 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1d14da7-e22d-33c9-8c45-a393eee54ee9 | -8.14873 | -49.77698 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cd517de-cd72-3b62-acc5-bdc568d52f05 | -8.14815 | -49.78061 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 780e3a79-27ab-3831-9f57-b75be0198782 | -8.11783 | -49.35244 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19673d32-8531-3fdf-836b-0a5b5909344a | -8.09281 | -49.33755 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94a451bd-7c97-3484-a60f-b2aab0539407 | -8.09224 | -49.3411 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45cae8af-a382-3b0a-a5c7-6b7853af747c | -8.06597 | -49.37691 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f4c8dda-2726-3368-a0f3-3e5888be9c0e | -8.06263 | -49.37635 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4b13aa6-9018-3421-9294-7fb193405e22 | -8.06207 | -49.37991 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dec3d332-68fe-38e7-ac64-fbaa6d3ed20a | -8.05486 | -49.97182 | 2024-10-24 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a94b6045-b141-3f67-8c6c-37518515357a | -8.0263 | -49.75364 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87c50108-1c7a-334c-8b05-fcc3b1f421f4 | -8.02571 | -49.75727 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 069f3168-030e-3206-b89c-fc557ca6e29e | -8.02407 | -49.63828 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 342c020e-5236-3bd0-bdf2-17158a6f2a9a | -8.02129 | -49.63413 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73726a7a-2d5e-35d3-be7c-529918dc0763 | -8.02071 | -49.63774 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 85dab994-b1e5-35ae-bb1e-c26130a666ab | -8.01793 | -49.63359 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e925edaf-3fe1-3ee4-b61d-40d269d4b305 | -7.97382 | -49.46472 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1f3d02c-25d7-3e1a-9894-2fbfeb96e944 | -7.96827 | -49.45649 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d255ba00-6c7f-3a0a-af5e-d44dd0450b8d | -9.43542 | -48.87816 | 2024-10-24 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f79e625-e934-3215-b72f-ae97a0e81bc6 | -9.43432 | -48.88512 | 2024-10-24 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f29e8d6f-5988-3d02-b8d0-ace776ed02fa | -9.43156 | -48.88112 | 2024-10-24 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc6d5675-3a3e-3f4b-8bbd-128ca5ca4a99 | -8.67311 | -49.09168 | 2024-10-24 04:34:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c797574-0171-305d-b989-13fd469f3b84 | -8.38281 | -48.64785 | 2024-10-24 04:34:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d535d6e-930e-320f-9e40-11ae11e14485 | -8.06632 | -48.90401 | 2024-10-24 04:34:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e331d742-7843-397c-8e77-58b1c06bf72a | -8.06577 | -48.90751 | 2024-10-24 04:34:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a69fb7c-3c2d-3eb4-b028-0951bddb81c2 | -9.8414 | -49.04397 | 2024-10-24 04:34:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4128516f-a7d9-3597-85b2-a9109b3e63de | -9.64239 | -49.65083 | 2024-10-24 04:34:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85a68d75-e48d-3c42-ba86-f4953b618301 | -9.6133 | -49.68265 | 2024-10-24 04:34:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a91a195f-5d38-3576-886a-66be1c6d2242 | -9.60997 | -49.68211 | 2024-10-24 04:34:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba458ea6-d3bc-33fb-bc88-b9630313355d | -9.60789 | -49.16412 | 2024-10-24 04:34:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58575681-8e61-33cb-bafe-d1b82c597174 | -9.5724 | -49.64315 | 2024-10-24 04:34:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f9b378f-ffd2-3155-a6ab-a4ea8c1670b1 | -9.57184 | -49.64671 | 2024-10-24 04:34:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a987547-fe37-32f7-be94-a81fe2e3bc51 | -9.5685 | -49.64618 | 2024-10-24 04:34:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2ac3edd-f2a3-3b48-ba31-420bdc03c193 | -10.89135 | -49.26903 | 2024-10-24 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ad6cdc3-b6e8-3119-ac3e-736c997a644f | -10.89079 | -49.27253 | 2024-10-24 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f42e396-00f9-3bad-aacf-ff4b80bfe9f7 | -10.87265 | -49.53616 | 2024-10-24 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 96384e75-756e-3951-9c7d-51b1e39d0a37 | -10.87209 | -49.53968 | 2024-10-24 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 77b92fd5-59ab-3155-8751-91eef354ca15 | -10.8699 | -49.5321 | 2024-10-24 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 51f02d0d-57f2-33af-9f9f-f2e48d28f268 | -10.53519 | -49.10998 | 2024-10-24 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf2a2fec-aa46-3882-b6ba-5c7a60192a60 | -10.3288 | -49.36054 | 2024-10-24 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d458fe4-f376-30a6-b033-c5f954cc3f37 | -11.73286 | -49.86209 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9fb6b2d-af78-34e3-be0d-ea4f89f7ed72 | -11.72954 | -49.86155 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79752535-e91a-369a-934b-a650384d50d4 | -11.72905 | -49.84327 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19152189-1218-3702-bba6-654f6a6e6d50 | -11.72848 | -49.84682 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9e1a8d0-ecb8-31e5-bfda-91aa0d1e3a15 | -11.72573 | -49.84273 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb262536-025f-3c94-974e-d4c89b42ecaf | -11.62393 | -49.81892 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5a85c5c-7001-31f7-8987-f849a18be7f9 | -11.59509 | -49.82876 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3f06f7d-bf30-3389-8b0a-7dafcb662cbd | -11.59429 | -49.89782 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cadb0229-0607-31fa-bc1b-f7a593e41d9a | -11.58812 | -49.91505 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fdd6549-9613-3469-bc12-dbcfba0a73b0 | -11.584 | -49.83422 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b90b74b1-ca23-3053-9ba8-f9604610c3dd | -11.58067 | -49.83368 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad4ecd0b-3554-3127-beed-14de939bf5f9 | -11.57945 | -49.8626 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d44a8ea2-a48c-322b-b67e-1f3a943a5521 | -11.57517 | -49.3549 | 2024-10-24 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2ffdf48-40b7-37d1-b954-02ecb65a0819 | -11.57187 | -49.35437 | 2024-10-24 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d55c3d39-a6b2-3b64-8945-51051057fc16 | -11.56493 | -49.88937 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7a63321-8784-3bd1-a996-d1e18243e4c8 | -11.49611 | -49.87385 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cd8163b-7ddb-316e-a267-3d8a9b851960 | -11.49392 | -49.8662 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e60052d-45c4-3fef-8327-8bfdc08d3021 | -11.44395 | -49.45256 | 2024-10-24 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2814c8fb-7934-33ed-a913-da37b3ee2ba5 | -11.28506 | -49.93813 | 2024-10-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13763b7c-10ea-3323-9ca1-7f0dee46dfdd | -11.25508 | -49.93322 | 2024-10-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42dad5d8-8ed6-38fc-a32d-9e25920d8f21 | -11.25394 | -49.94035 | 2024-10-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c1f910e-c381-31c1-a9b0-c4c906615e88 | -11.25336 | -49.94391 | 2024-10-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebf8f904-6bcc-31c3-bce6-f3ed5370597b | -11.25279 | -49.94748 | 2024-10-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 392bc227-ee43-3e79-9c8d-1b9d6ba7277f | -11.15929 | -49.80819 | 2024-10-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README48.md)
