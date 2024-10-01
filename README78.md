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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28a42b68-aa1c-36c2-82f6-d94d37756360 | -13.21356 | -48.58191 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b228eab6-d97e-304e-8d1a-3088284c1973 | -13.19903 | -48.55126 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1e804e33-793e-3d63-bd30-5b7dd00b6e6d | -13.19528 | -48.5506 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bcc90fbf-96e6-3e13-99d9-6f302709b414 | -13.19442 | -48.55561 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 102a558f-c10f-3845-9d9e-55efe72a739f | -13.11916 | -48.22543 | 2024-10-01 04:14:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c8e8a96-3f68-3b1e-ad01-47a3b94c81fa | -13.11378 | -49.6278 | 2024-10-01 04:14:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03891f92-ae66-370d-898c-f31b388436aa | -12.97953 | -48.53992 | 2024-10-01 04:14:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 57c41612-2c5e-35da-9990-3b757eddceb8 | -12.97576 | -48.5393 | 2024-10-01 04:14:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 41fee414-5e0b-3790-b8a7-232232d764aa | -12.97198 | -48.53871 | 2024-10-01 04:14:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3199eecc-35bf-3106-8e36-97249d573143 | -12.52339 | -47.97965 | 2024-10-01 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d08d123-8534-3bc8-b9e0-02dcda97c852 | -12.51972 | -47.97898 | 2024-10-01 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0d82134-598d-382d-86e0-5a9a8c73ac07 | -13.11546 | -48.22479 | 2024-10-01 04:14:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8535a35f-9de5-3ad8-b141-b064102e07d8 | -12.51897 | -47.9834 | 2024-10-01 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea9cbb10-1a01-38e1-b8c2-87eaf05e1aeb | -15.0784 | -48.94506 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a345f4ca-c834-3add-92fc-f2d9508b39ec | -14.79364 | -48.74818 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0a14193-1cc5-3335-906b-d9c7642ac541 | -14.79135 | -48.76148 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aabf7bda-80af-3d74-af6a-eded2e23a344 | -14.7906 | -48.76585 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 008a5902-8796-375b-a723-0366991ac715 | -14.78917 | -48.75192 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac1b04ea-b32c-33b6-b566-bd008d94af69 | -14.78764 | -48.76078 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ad4b872-a601-3704-b787-0fd724805c57 | -14.78688 | -48.76515 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbaa35eb-0b60-3051-b9a4-07f6bc7165b0 | -14.77188 | -48.78535 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8efe9cbe-1cc9-3087-82c2-c9af9d9bb1fe | -14.77131 | -48.76653 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5968800-7aa0-362b-9e70-c03ee8fee0e8 | -14.77057 | -48.77077 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b8baf1d-ea46-3c42-a970-6084f7e1a3f4 | -14.76982 | -48.77511 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 757559f5-7d82-3e85-a1cd-69a62c5a63b4 | -14.76904 | -48.7796 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5e6f21b-0a8a-3d2a-9fb2-8229a286adf0 | -14.76819 | -48.78452 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5793765d-6cd1-3357-a70b-89d33ecfd2ee | -14.76449 | -48.78372 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 990b9927-821f-349d-8f4e-953315b00f4c | -14.76365 | -48.78856 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ce1dfdbe-3a82-3708-b954-ac5373d5c404 | -14.76076 | -48.78308 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7e1d78a5-8b64-37bb-adb3-7e438b5f7a6c | -14.75991 | -48.78798 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b29c7eaa-d56a-3b86-a62e-abcdd8ff01d3 | -14.75702 | -48.78255 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1f7cf55f-9c8e-3ed2-91d0-529e79a63503 | -14.75413 | -48.77708 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 14dcdc1e-1225-3c42-b4ee-173543c490bb | -14.75327 | -48.78201 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7a6afb2d-5741-3903-9d99-8b1d0cfb08c7 | -14.75039 | -48.77655 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 973c53a5-22f4-3aab-8565-478d777000c5 | -14.74832 | -48.74445 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f02766d8-05a5-34b8-ac71-71a92f66c013 | -14.74664 | -48.77603 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d92b0ba-1cda-3854-8d7f-531fb8894385 | -14.74538 | -48.73938 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6a58db6-6f3d-3c72-825a-cef07789a808 | -14.74459 | -48.74386 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13ea3367-d943-3241-9ff6-5817583896cc | -14.74456 | -48.76597 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13f5454b-330e-3165-a0a7-586cc49c6184 | -14.74374 | -48.77066 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3fd063ce-3210-39eb-a4f7-8d8804237ae9 | -14.7429 | -48.77551 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 78a6530a-ccd2-3b4d-8041-dfdd85322480 | -14.74082 | -48.76541 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edc13f73-0b0c-36fa-8e39-1ad44798a702 | -14.74 | -48.77013 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2cbf5aba-e709-345f-aef9-a2b230f59713 | -14.73915 | -48.77498 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0383613c-1b2b-307d-823f-20094cdf5e6a | -14.73786 | -48.76042 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a12da9a8-843a-364b-bcdf-d262d23e03e4 | -14.73708 | -48.76488 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ef268ed4-b3fc-3c6f-ac71-e0704db8c405 | -14.73626 | -48.76958 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 921593fb-3f87-3fe8-9698-10600f142c92 | -14.7356 | -48.75143 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5360c22-00c3-3150-8d59-9aefd0bdaa07 | -14.73409 | -48.76005 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e3a14122-36b5-3f6b-8f17-e775ee162f5b | -14.73331 | -48.7645 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b9294cfc-1231-3fb4-b8cb-f09e980897fd | -14.73264 | -48.74644 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebf069a6-7542-3e61-ba0d-b39a24463230 | -14.73186 | -48.75088 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 437b3442-9812-3326-ae09-1d775128538c | -14.73109 | -48.7553 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fd5752f0-4a0e-3106-aca3-fe5b60a5c6d3 | -14.73032 | -48.75969 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6d0e02b1-2c7d-3500-a38d-7ef1d956bac1 | -14.72954 | -48.76411 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d7b4dbec-63a4-3542-9bee-859013fc30e6 | -14.72876 | -48.76855 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f5d52193-39ed-3612-8f00-cd900c79f07f | -14.72736 | -48.75467 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 78015e54-3ad4-3e11-8f3b-444a79676df9 | -14.72661 | -48.75898 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a3d96e72-3301-3dba-8daf-8c96dd674e47 | -14.72585 | -48.76329 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9c1cd108-154c-3cd4-864e-1ba1efd0e11b | -14.72506 | -48.76776 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e83b7cfa-266f-3ded-a837-9328780bab24 | -14.72366 | -48.7539 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 24156150-9869-3f36-b35e-f4daf6826e07 | -14.72292 | -48.75814 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5c724298-e6b0-32fd-9955-0e72a3c7ebf6 | -14.64792 | -48.82766 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fad5c41a-e6e9-3656-b6ac-643bacc6e1b1 | -14.2778 | -48.65 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e454bf6-87da-38bc-b208-1580ecc5f8a2 | -14.04672 | -48.43911 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1275593-a8e8-368a-84e0-a754b90e02aa | -13.89941 | -49.37352 | 2024-10-01 04:14:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 563ade56-5b34-3a75-84ff-42d60a8438ea | -13.72573 | -49.42271 | 2024-10-01 04:14:00 | NOAA-20 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce4dc3df-0c02-3925-898d-947c37be1062 | -13.72498 | -49.42494 | 2024-10-01 04:14:00 | NOAA-20 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 949699e1-2f64-3c4c-8b23-5f9dff7af24f | -13.72181 | -49.422 | 2024-10-01 04:14:00 | NOAA-20 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 66f3dc88-803d-3397-b49c-153be9d65c44 | -13.72105 | -49.42422 | 2024-10-01 04:14:00 | NOAA-20 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f4be009-550f-3585-9210-962aa131439f | -16.36119 | -49.56938 | 2024-10-01 04:14:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe4b256b-2225-3215-8648-e3f623bb5df3 | -16.36034 | -49.5742 | 2024-10-01 04:14:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6bf6599-6754-38ed-b326-6b666a32902d | -15.15503 | -49.59217 | 2024-10-01 04:14:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7f98d4df-d82c-369b-b910-cd1d9e6fc5f9 | -15.15415 | -49.59714 | 2024-10-01 04:14:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 40cc0c5e-fd6d-373b-9850-18c95a30d06c | -15.15116 | -49.59143 | 2024-10-01 04:14:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 094ed28d-31bf-37e3-b5cf-d2ca3730fb88 | -17.28456 | -49.47289 | 2024-10-01 04:14:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2180ef3c-bb25-362d-8dca-721474ccc0c8 | -17.12543 | -49.87003 | 2024-10-01 04:14:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc1f3bbc-29d5-399e-89bd-1f568f80b43e | -17.00891 | -49.77969 | 2024-10-01 04:14:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed0b8051-4764-3cb0-a227-c2723f94e631 | -9.98113 | -50.17587 | 2024-10-01 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3105b69b-a3a0-3bb6-8e62-3a4e16064a8b | -10.04926 | -50.30263 | 2024-10-01 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3bdd95b-f5ad-37b5-bb40-82a490d4f494 | -10.04562 | -50.29745 | 2024-10-01 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81dfadfc-9856-3b52-9372-0596f200da76 | -10.04485 | -50.30183 | 2024-10-01 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa60998a-e363-35f3-a618-08a91a68ae9d | -10.04198 | -50.29229 | 2024-10-01 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70636474-b179-3307-8001-a84ca3994f1a | -10.04121 | -50.29665 | 2024-10-01 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88b32559-e960-3f4d-8c82-439947cb7d5f | -10.56169 | -49.47784 | 2024-10-01 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a219b7af-ae39-3386-afb4-7d0be4eaa39b | -10.50976 | -49.78154 | 2024-10-01 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebb5b4fd-8b12-32cd-ae37-0b5f348b1de0 | -10.50973 | -49.77936 | 2024-10-01 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c27ac6d-1fe3-3c85-bd8e-281429c3a52d | -12.21605 | -50.47935 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b79b753-fd2e-37e7-ab13-0be10b62137d | -12.21249 | -50.47437 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00abb5f6-46bd-3376-8866-a4bbd55fca81 | -12.21175 | -50.47853 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e144de33-02bd-369a-8406-1a73af872be7 | -12.20672 | -50.48188 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55abc677-37ba-37b7-9725-f45515805ffd | -12.20598 | -50.48605 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c549486-cb0b-37ac-8b49-b81646f46797 | -12.15254 | -50.07588 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 33115117-ab0e-3d30-a2f5-cc94a1c80474 | -12.15185 | -50.07981 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a6854e8d-a2da-3966-a072-1f5fd18f0460 | -12.14905 | -50.07118 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bac75c8e-a2dd-39e6-ab84-e72bc478fe33 | -12.14835 | -50.0751 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 03994189-b8bc-386b-858f-3ce56ded07b7 | -12.14766 | -50.07902 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 12b2ac3f-b532-3d53-8ee9-0a28b489e4d9 | -12.14696 | -50.08294 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 39967b14-4444-3ef0-a344-6021b08ff588 | -12.14556 | -50.06647 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 459a45f5-d808-3eb3-8a62-bd6d0a3858a1 | -12.14347 | -50.05391 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |


[Clique aqui para ver as próximas entradas](README79.md)
