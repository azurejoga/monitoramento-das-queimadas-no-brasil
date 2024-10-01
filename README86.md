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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76dd34b4-2845-31a5-86b9-76f80bc91326 | -17.01072 | -56.08416 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d1f80d41-351d-3e80-a3ff-476ba164f1ff | -16.9725 | -56.21629 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d8d11daf-0227-3116-8ecf-50e637861889 | -16.86182 | -55.91183 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 032df2ff-f67b-3d62-9e29-4b6188a3741e | -16.86097 | -55.91582 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 97b3a25b-6ba2-36a7-a42b-6abad3ea7006 | -16.85706 | -55.90659 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| e9ed89a0-a10a-3019-83cc-161a725d0806 | -16.85621 | -55.91056 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| e232e0bf-915a-3cb7-86b7-07a5e5aa1cb3 | -16.85538 | -55.91452 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 29e35bc0-25ce-3cf5-9b53-4cb447a536e5 | -16.85369 | -55.92246 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 1d06ec4d-ed6c-366d-a82e-daa0b5666c35 | -16.85285 | -55.92645 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ae27d8d1-8308-3db1-b911-1ab04d6b88dd | -16.85062 | -55.90926 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ffb3d101-c28d-3ae8-b177-b17e3a96a6c7 | -16.84978 | -55.91323 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6fc18128-7900-3d67-95e0-96951b052fea | -16.84809 | -55.92117 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4ba57a7b-ce35-32c4-9101-8ff4fd60a3a2 | -16.84725 | -55.92514 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 10671b73-5bb7-3234-9832-d1ff7a5a5ec1 | -16.84027 | -55.90268 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8ca2fca6-360f-3226-9a1f-616ce2b98f1e | -16.83774 | -55.91457 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 086c2ba2-470a-3448-bf4a-fa687f13c05d | -16.83698 | -55.90412 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6f7f6ecf-1783-3f28-82df-6248efda179b | -16.83535 | -55.91204 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| c0578339-174c-34e0-b0f3-62abc58e419a | -16.83468 | -55.90136 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 166af0f7-121e-3bbe-92b3-ea9c242dcfc2 | -16.83453 | -55.91602 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 17762a0f-7efd-3aab-936b-3df01be42543 | -16.83384 | -55.9053 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 037ae697-d7b8-3003-bc0f-83285ae6560c | -16.83371 | -55.91999 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 255255b5-726f-30bc-b5c0-3d7f388ef022 | -16.83215 | -55.91322 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 5dd91e2d-9f10-3970-ad9a-30796a3ca8b4 | -16.83207 | -55.92796 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 9590a086-c19d-3844-a6d7-54c58b43d6ca | -16.83058 | -55.90672 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 39813d66-6cf7-3979-a7a7-b108bc512e44 | -16.82961 | -55.92514 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 30352a2e-ca8d-309f-ae60-4fa93e0a985d | -16.82894 | -55.91465 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| a4f0e37b-f22e-3951-83be-9a5af1fc87fd | -16.82875 | -55.92913 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| dee820c1-eed2-31e5-bd2c-d857cc50fcc5 | -16.82741 | -55.90793 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f13f6b48-7db8-3e21-9abb-39b955df2833 | -16.82647 | -55.92662 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b32ab103-07a1-3094-91f2-e63a1050da93 | -16.8257 | -55.91588 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 6565cc9f-432d-3df2-91ae-9a49d4297d36 | -16.82486 | -55.91985 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6aa14f9b-1314-3358-b016-ae9cc5bae6ea | -16.82465 | -55.96398 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| dd9cc9a4-c9c7-39fd-94e8-0e2282608537 | -16.824 | -55.93861 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3aa6c848-a2a5-3ebb-8a34-21a5054f037a | -16.824 | -55.92383 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9f629584-9c71-3664-b04b-af06de95cc3c | -16.82317 | -55.94261 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c4e851fd-82b7-3094-a9f5-145007dcaa72 | -16.82315 | -55.92781 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 200e8ec5-e4ff-31bd-b63c-256f0bb2fa7a | -16.8223 | -55.9318 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 58844ef0-e0b2-33eb-8d7d-845e9cef92a0 | -16.82194 | -55.96103 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 97c316d3-ab10-34d8-9a82-ee0dcdb2e042 | -16.82059 | -55.93977 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 51376b90-63af-38d4-a8d8-03ca8be8753e | -16.82004 | -55.92929 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3b87e34d-409d-3f67-9102-0079d4ca55fa | -16.81922 | -55.93328 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 69175910-7ef0-39d1-bf26-4d0c78ac13f0 | -16.81584 | -55.93446 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 382a928b-39db-3093-be0e-71f063485a30 | -16.81196 | -55.93991 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fa3821d1-cdcb-33e6-8463-73b0832497b2 | -16.81113 | -55.94391 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 41d7174b-dace-323a-b1f3-214cfc78b8eb | -16.8103 | -55.94792 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4abb577f-f6d3-32da-a56b-74ac75a15e5f | -16.80947 | -55.95193 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bb62b568-eb5c-32e9-9ec7-e9a914b59ed7 | -16.80938 | -55.93714 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0a93c7db-982f-3dc0-a02e-49b6adfd7583 | -16.80671 | -55.88038 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3efe237d-a1f9-354b-a8bc-9889960b30e2 | -16.8062 | -55.82659 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 309ad0a3-c2cc-399d-a034-5cf5e4fb79d9 | -16.80588 | -55.88432 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cde11884-5b27-3f01-88fa-5d26891a6f69 | -16.80551 | -55.94265 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 923dfb8c-94cf-3abe-a7cb-2adec7e84c72 | -16.77463 | -55.78231 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c1159b0e-d815-34c2-8bed-8856ba139703 | -16.7738 | -55.78621 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 69727619-2958-3073-ae99-62eed6322464 | -16.77215 | -55.79402 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e600bc3d-5ff4-3972-accd-4e1096c50ce0 | -16.77051 | -55.80183 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c7fc3175-ef0f-342a-81f3-5d7a774205e0 | -16.76885 | -55.80965 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 58cdc2fd-7c1a-3efa-b0b5-9b110cbf52df | -16.76824 | -55.78491 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 17ada4ab-8b17-3262-b588-c5bd0f982daa | -16.76577 | -55.79661 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| c02e6ca2-e537-3b3a-a3b8-9439b019b35c | -16.76495 | -55.8005 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 7205bed2-11be-339b-8c0d-4836fa722cf2 | -16.76269 | -55.7836 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8caad5d7-7072-3813-bde9-71f1d3327408 | -16.76246 | -55.81226 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 511b36dc-914a-3865-a40f-2805ebec91bd | -16.76103 | -55.7914 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| afacee1e-c132-3496-b680-0cfda55b45e9 | -16.76021 | -55.7953 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| e591eb60-6c57-371c-9438-2acc2750dffd | -16.75772 | -55.80703 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 06290c95-3482-30f4-baf5-a55283ab2200 | -16.7563 | -55.78617 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 140bb7e9-da19-3028-becb-5334e14a0dc5 | -16.75547 | -55.79008 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c8919005-4057-3cf0-b008-9a71abe62531 | -16.75523 | -55.81879 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 3cb36f4c-4feb-367e-adc2-5aa9dc4ced87 | -16.75464 | -55.79399 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 01f52e75-ea51-30f1-915f-6573e9f9e384 | -16.75439 | -55.82272 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f2d85cce-6373-3a5f-ae7f-025630e9c4e5 | -16.75381 | -55.7979 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 829d79e1-45b3-3cef-b4bc-67d54cad04f5 | -16.75116 | -55.79466 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 50fe4fce-60c0-38ab-8cde-f5a25eb25911 | -16.75035 | -55.79858 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 25734479-5e33-3f9a-a673-537ba7099532 | -16.74991 | -55.78877 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2be98776-2ee5-3010-91fe-959097004204 | -16.74954 | -55.80251 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9333dbbd-08f5-35e5-8f43-ec621ba9f264 | -16.74908 | -55.79269 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b3a65783-642e-3d0d-84ec-3873f9bdaaec | -16.74741 | -55.80054 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ed448c27-2f9f-3456-9d65-00f4dbb09b8a | -16.74398 | -55.80119 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b066c617-a217-3e2f-81e6-4581177c5d21 | -16.74318 | -55.80509 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 68b8ba9c-8a9d-3d61-ae1f-2c453bdebbf0 | -16.73264 | -55.49314 | 2024-10-01 04:17:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f483697f-6666-3de2-ac9d-d3ceec790b57 | -16.73186 | -55.49685 | 2024-10-01 04:17:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fe3edd6b-f278-331b-8ebc-a95d3ac8a883 | -16.72937 | -55.8722 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0709a5ff-9f10-3189-97dd-84212d340840 | -16.64766 | -55.95356 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f8136520-9655-31b8-8dce-cfb79261830d | -16.64682 | -55.95758 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1d338496-5d33-3c41-80d3-fe7e2eccd86e | -16.6195 | -55.94704 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7e160fd3-47a5-399f-9611-bd602619e844 | -16.61864 | -55.95106 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 10fd6b9d-fe51-36f3-bbcf-d0eb918ee1f0 | -16.61163 | -55.9455 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 09d3aac9-73d1-32ae-8f3b-e13ce96e91b6 | -16.60683 | -55.94014 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 997085cf-d3e8-3010-a267-e19b2b6e05bd | -16.60517 | -55.94818 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 72644e38-47a3-37f1-b3c1-90d0ab680a21 | -16.60434 | -55.95219 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 310af8c6-7f10-341f-b841-3c8571a74d1d | -17.08211 | -56.71079 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 88e2ce63-6a85-3d9e-8b04-f79221d51e2c | -17.07801 | -56.7107 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 1b86fa0f-865a-347f-b3c6-69b618ee4e7e | -17.07627 | -56.70938 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 93cb0f30-f414-31f2-ba09-fdbc4dcbf13a | -17.07217 | -56.70928 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 83e9dc2b-07c6-3117-8ad9-d6c52ab7d051 | -17.06048 | -56.70644 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 4a57ecd1-13fb-3e2c-8f96-7a774bd395f6 | -17.18564 | -56.2004 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 87b0176c-46ef-3c44-9df2-f6ae9cf9116b | -17.18556 | -56.20867 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c670e131-a4da-3069-94f8-0bd427e857e7 | -20.01249 | -55.98705 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 327bc912-3f1c-3b2c-ae48-5f57eb56062e | -17.18468 | -56.21275 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| ebe46df7-15b2-3a6f-a8cf-3b5e1412d7b1 | -17.18394 | -56.20855 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| ec50d207-dd40-334b-bc77-b757b5d28c47 | -17.18379 | -56.21683 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |


[Clique aqui para ver as próximas entradas](README87.md)
