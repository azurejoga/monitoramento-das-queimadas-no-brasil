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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02988d84-fde1-386d-b206-e1e54b36f127 | -17.08464 | -55.99662 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 223dcbf8-e02b-397e-b974-116a3c85fd72 | -17.07964 | -56.00528 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1a78192b-041a-3e6c-bf95-429ea4fbcd2b | -17.07835 | -56.01447 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| bebf31a4-c7ea-3601-babb-85148f21670c | -17.07592 | -56.00474 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9787894f-10ea-3848-98a7-3e101aaa48de | -17.07515 | -56.0374 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| e99092d1-3746-3d5c-ae0e-303da2234d3c | -17.07093 | -56.01336 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bd33ddec-33dd-3b58-b2f2-623fdfe41424 | -17.06913 | -55.99903 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0327a2af-1865-3d75-a9d8-bf6efedcbf96 | -17.06709 | -56.04087 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d5790eb5-6682-3ce9-adb0-c51829a9bc27 | -17.06541 | -55.99848 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 18cff20a-755b-312d-99a5-6648808632af | -17.06169 | -55.99792 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 23f23192-91c1-36ce-98e7-3665aa99801c | -17.02447 | -56.0205 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e4fba099-a6f5-3bd1-b510-0089f6f1dfbd | -16.90019 | -55.87926 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| eab76b1f-6ad4-3b87-8049-2370bf234886 | -17.08207 | -56.01501 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2ecd114c-d373-3b2e-83e5-77d1c40dde69 | -17.71589 | -56.27069 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d0f0e05a-88de-3822-be8d-0feef6412bec | -17.07899 | -56.00988 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 101b0566-6eb2-39d4-90b0-1f62618f5ed3 | -17.07656 | -56.00013 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 81b7badd-bda5-37de-ab2f-fad1880ac899 | -17.07579 | -56.03281 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8dba7f7f-dabe-3c84-9709-c5bd0f8cfa25 | -17.07528 | -56.00933 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 19bfad8d-ad9b-337d-82fd-c7763e621703 | -17.07464 | -56.01391 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c29ba3e2-ff0d-3ae3-b5ef-7684ac7a3f9c | -17.07284 | -55.99958 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4c65ba79-0155-3278-9095-01ba7edb0f1f | -17.0722 | -56.00419 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f3c16e06-7709-32cf-9ae1-0f817c921573 | -17.07156 | -56.00878 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b4fd0949-e006-3b32-85f7-4ec82b556c5d | -17.06848 | -56.00364 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3bb6984b-0aa5-39a7-9127-729a620996ea | -17.04121 | -56.00895 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 7ff57302-88fa-37da-b6f9-074e732fe71e | -17.02076 | -56.01994 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 31983a96-cb46-395b-a26c-f19b21e5138c | -16.90168 | -55.87706 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f62169f2-3098-3808-baa6-5e5f1b2c18f5 | -17.73498 | -56.2689 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f46a6eda-88aa-3801-94f3-200bf782a83c | -17.73188 | -56.29165 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 158e8f16-a14b-3e65-bab3-c4f7593b1146 | -17.73128 | -56.26835 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e9386483-4f2c-3b67-b14a-e226a6036afe | -17.73066 | -56.27291 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0f33aa43-c71a-369f-aa27-033e4ba9dab0 | -17.73004 | -56.27746 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 65c506e1-5451-3fc4-b7b4-a4b5242eb827 | -17.72943 | -56.28201 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 14403d0a-1cab-3a92-b97f-7e24421f5615 | -17.72881 | -56.28655 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 90898783-1767-3774-9992-7f4277aa7d52 | -17.72635 | -56.27691 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 61041e28-50e4-3876-baf8-1cdc11d11f49 | -17.72574 | -56.28146 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ca76034c-0e91-34a9-92e5-3ef1d0e2da95 | -17.72266 | -56.27635 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| eb0b0357-3faf-3846-86c8-411e19dcceb7 | -17.72205 | -56.2809 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2453968e-8f03-3739-a168-cc5443133875 | -17.7205 | -56.2744 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ff54e1b9-6652-3eb8-81c9-23ccbedc789c | -17.71986 | -56.27895 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1448441e-3e67-3114-8da3-63c5dede043f | -17.71897 | -56.27579 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d5fce462-c5a0-345f-aedc-c2e2397ae73a | -17.71745 | -56.26931 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4bce142a-aa01-3c57-8d74-aa227ea1f172 | -17.71681 | -56.27385 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d3c4fe0e-d24b-3c65-9a3a-05bf36651fa0 | -17.71528 | -56.27524 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e1575bb9-864c-3c36-9288-0e075900754b | -17.71361 | -56.29654 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b066d480-ec69-3852-a9f3-345dea282b5d | -17.71221 | -56.29797 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fd388c28-9391-3822-8802-e5cfd3e88355 | -17.70993 | -56.29599 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d2dfc3ad-ff22-371e-985d-c9ef0608395f | -17.69975 | -56.2341 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 885d97e0-ba36-32ef-8a51-f7425b162e9f | -17.69912 | -56.23868 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1b033538-6274-305d-ad74-35e2543a53a1 | -17.69848 | -56.24324 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 16426c2d-8637-380d-a049-145d432b01ac | -17.69785 | -56.24779 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4536351b-e29f-308c-9235-d38619266812 | -17.69606 | -56.23355 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0d2b6d60-6361-3627-8e47-d9765dcf1c00 | -17.69542 | -56.23812 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c671af01-a087-33a3-bfab-3cf8045d918e | -17.69478 | -56.24268 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4fc039b9-9382-38da-8cfd-e79116a2598d | -17.69415 | -56.24724 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9c9b6504-aa0d-3fb8-b900-4ccd693478af | -17.693 | -56.22842 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 32de113f-f60a-3b25-8b20-e95f83542fc5 | -17.69236 | -56.23299 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0cce60e6-0f42-3927-894c-b0b1810b9c4e | -17.69109 | -56.24213 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 604d74cf-f802-3a36-8a75-ddfc9b93235f | -17.69045 | -56.24669 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 14420538-c0d8-3f77-9a05-2df31b5cc67c | -17.68739 | -56.24157 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 3fdb4a5e-d975-3eaa-a5a5-e8be3cfcbddf | -17.68676 | -56.24613 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6fedc13e-f4c0-3f2b-9373-f2f30aeb2f60 | -17.68465 | -56.3153 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 216ba78e-24a1-35fc-9d8f-0d2c65b4c409 | -17.6837 | -56.24102 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| b1b175d9-191f-3697-9eee-7329f37871af | -17.68097 | -56.31474 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 7e4755fc-45e8-3ff8-9fb0-688c47b95fd3 | -17.68064 | -56.23589 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 89cbf8ef-7501-3165-b174-c030e4b3a751 | -17.68034 | -56.31926 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 89fcd0f5-1ab4-34cf-b649-ca1377d246f2 | -17.68 | -56.24046 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7b2bc8a2-ec78-35ab-b5b9-4c3aa96d4f12 | -17.67694 | -56.23533 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 473775b6-ad79-3c65-82ea-7ef42c5cad7f | -17.67324 | -56.23478 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f63faae9-e00d-374c-a6e3-cc9abe7e8ccb | -17.66954 | -56.23422 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 44e5404e-ec46-3096-af1e-e392f2e423b3 | -18.26729 | -56.49101 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| db674f3c-e1aa-36cc-8671-fe60d0483835 | -18.26725 | -56.5186 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 2bede71c-abcb-38bf-a70b-914854e2a4b5 | -18.26667 | -56.49553 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 10c58fb3-e479-3b53-bf2b-7321a4ca10de | -18.26663 | -56.52311 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.8 |
| a0de518a-511d-3839-b242-cbe3833cd31e | -18.26605 | -56.50003 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4e5a2432-ba2c-3e50-a045-ff1410f51f0b | -18.26601 | -56.5276 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.8 |
| 855358c3-e41d-3eb5-bd7b-d082e786f71f | -18.26543 | -56.50454 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.3 |
| dff9c546-3779-3038-b8a2-6ea415a10160 | -18.26481 | -56.50904 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.3 |
| 8139534e-60f6-395c-902c-b5025cd605f6 | -18.26423 | -56.48594 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cf30bc02-cc17-3072-ac0c-276eb3a7435c | -18.26419 | -56.51355 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| ac8dc327-1e4d-355e-8280-6074d6e027e2 | -18.26361 | -56.49046 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 32817898-a705-3b0b-a982-5cd7fca40e37 | -18.26358 | -56.51805 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 3de4a888-9a53-33ad-a3d1-485a61024896 | -18.26299 | -56.49497 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 626c5007-ca7f-3953-89f6-cc0ca20522fe | -18.26296 | -56.52255 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.8 |
| 050d7384-05cf-3a75-8139-7204bc10f405 | -18.26238 | -56.49948 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 2572b77a-2ffb-3635-ad74-86126d94a292 | -18.26234 | -56.52705 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.8 |
| bf89425f-37bd-3d82-814c-5cd343b27012 | -18.26179 | -56.47635 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d2351cf6-1510-314a-ba8c-c12ce863cb1a | -18.26176 | -56.50399 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.7 |
| 892ca305-c860-3ff3-8bc1-f631f2a66b9b | -18.26172 | -56.53154 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 115937f7-6838-38ae-b3ed-d3c48d962797 | -18.26118 | -56.48087 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 86484028-b533-3aad-b517-4deae1f95b55 | -18.26114 | -56.5085 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.7 |
| 9d34119a-fbd0-3495-a73f-b6ad1d7ccf6f | -18.26052 | -56.51299 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.7 |
| e6c11d19-5a49-3feb-a69f-d0575eaf50ed | -18.25994 | -56.4899 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6e1491c8-2e66-3acf-991a-b40efcb316bd | -18.25991 | -56.5175 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.7 |
| c02f083c-4460-387c-886e-f9e4ec0e5fde | -18.25932 | -56.49442 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| d7b8d6cb-9a8d-38bd-b70f-1444b2c2c857 | -18.25929 | -56.522 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 55fff35e-c635-3059-8045-59b3f53248d1 | -18.25871 | -56.49892 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 4ad2d354-d80e-3a73-90a6-d7695579a52d | -18.25867 | -56.5265 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 9ce0145d-7375-369b-8f19-79c9271c5335 | -18.25809 | -56.50343 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.7 |
| 321d8947-9960-3838-a7a8-579897b77e71 | -18.2575 | -56.48031 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9eb68638-b875-3cbb-8f5d-5470f1796b62 | -18.25747 | -56.50794 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.7 |


[Clique aqui para ver as próximas entradas](README123.md)
