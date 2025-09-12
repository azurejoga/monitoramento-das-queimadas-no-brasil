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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47e77ad7-457d-37c2-bf9d-8ea4190a07c1 | -23.42496 | -47.027 | 2025-09-12 04:29:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| cc891b86-9e32-3c0f-9ecb-3047b6c8d11d | -20.86765 | -46.50722 | 2025-09-12 04:29:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ebcf7a0-0d83-32e2-9800-a46b7890e705 | -20.58587 | -48.57297 | 2025-09-12 04:29:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0d657f5-9673-3961-85d7-f7b22e414849 | -22.18536 | -49.59949 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3a55fae9-c9dc-32d1-84d0-ff6ba1890a48 | -23.32575 | -47.32479 | 2025-09-12 04:29:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 50854dbe-51f2-3b12-964f-1dcbce37482a | -23.34829 | -47.23967 | 2025-09-12 04:29:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 39d7199f-bf4b-37ac-8870-343fe2ea69f9 | -22.52279 | -45.09598 | 2025-09-12 04:29:00 | NOAA-20 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 57ca93cc-806f-35ce-a1c5-f9f95d1d39c2 | -24.11838 | -48.70715 | 2025-09-12 04:29:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d6b7c2fd-008b-3527-a02d-1578174fdfde | -20.58865 | -48.5773 | 2025-09-12 04:29:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9d5c21c-5ff0-36e1-b9c7-4f8faeffa6c3 | -20.23331 | -49.25424 | 2025-09-12 04:29:00 | NOAA-20 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7bd8f58a-a544-30e9-8cb0-87471a11fa1e | -23.45052 | -46.70205 | 2025-09-12 04:29:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f0a33127-bbaf-3906-8063-39a313e7e60d | -22.14227 | -47.83699 | 2025-09-12 04:29:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 556df6c6-783b-3d57-8817-576021d174f1 | -22.18104 | -49.73663 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 499e6ed5-ef6d-3b19-a9a4-8ea3e918b5c2 | -22.50638 | -52.99549 | 2025-09-12 04:29:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 06367a00-f550-3b5a-b1e7-4bca28c59541 | -22.78552 | -47.80719 | 2025-09-12 04:29:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12bd6699-52b0-3a69-b194-e8c4062cc086 | -22.17773 | -49.73604 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| a052be14-5f69-3139-b0cf-ae517f49589f | -23.35248 | -47.15525 | 2025-09-12 04:29:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8f85a7a1-eed0-377b-a661-8a602e992fe3 | -22.65507 | -53.09856 | 2025-09-12 04:29:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ed664f09-4bca-3717-aab9-ac3dc3e41311 | -23.13653 | -47.15538 | 2025-09-12 04:29:00 | NOAA-20 | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 8ec7e699-be6e-3372-bcd7-1d851c589914 | -23.49386 | -47.25717 | 2025-09-12 04:29:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 47e205b2-1818-3b44-9eb9-8b7e0efb8f58 | -21.33549 | -45.02886 | 2025-09-12 04:29:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 24b47ffb-9b31-36c2-a5d2-02abfe147ba3 | -23.10804 | -47.49364 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bbb9881e-8795-3bb6-a7c8-d8420357ba1b | -23.39734 | -46.71036 | 2025-09-12 04:29:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a9a5b698-b068-34b1-bcec-256c5b4fd61a | -21.95646 | -47.55174 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1f38ca8-b6f2-3b27-900f-9651dde711e7 | -20.00689 | -47.64922 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00a7b21a-74a8-37e3-81b3-1dfe8161e279 | -21.64975 | -50.11223 | 2025-09-12 04:29:00 | NOAA-20 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0b9e8ba5-76c9-3d5e-9dc5-49ade262bfaa | -21.94546 | -47.55416 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8073dd94-0ac4-31c2-b24e-f7b9413b0bda | -21.19146 | -47.52953 | 2025-09-12 04:29:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 56.0 |
| b9c99ff7-aa8d-3513-aeab-4a88cd54cb2c | -22.65708 | -53.10791 | 2025-09-12 04:29:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 79da04d3-6520-3867-bec5-08f7d8fc3ad1 | -21.95874 | -47.56058 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef5a9f78-8ae2-3f1c-8bfd-8dc6357687b4 | -22.78957 | -47.80371 | 2025-09-12 04:29:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a7aca64-1c77-3ad8-badd-44959bf89693 | -21.9541 | -47.56814 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0fd20a97-ada3-3a25-834f-36614ebd8d30 | -22.18709 | -49.74155 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d3d95122-5aa4-3479-bb03-421e88107013 | -20.56829 | -43.7404 | 2025-09-12 04:29:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1e06a767-110e-35a6-899d-9f1f6b1890c5 | -23.23313 | -49.42141 | 2025-09-12 04:29:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6790ee17-aa6d-3a02-8c6d-88b7db39af3f | -22.79708 | -47.80082 | 2025-09-12 04:29:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64613587-cf4c-3746-97a5-4f02b24d505e | -23.1425 | -49.66183 | 2025-09-12 04:29:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6f937677-30ac-3a12-a3a0-033c6902b602 | -20.02472 | -48.89435 | 2025-09-12 04:29:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 912d1d4d-6552-3e3c-90c7-b6472a20914a | -22.82097 | -46.42979 | 2025-09-12 04:29:00 | NOAA-20 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 7bbdfe0b-2337-339b-8f92-91d68a8b10c4 | -23.4692 | -47.66532 | 2025-09-12 04:29:00 | NOAA-20 | CAPELA DO ALTO | SÃO PAULO | Brasil | 3510302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e360f53f-f6d6-3958-8dd1-878db045dc45 | -22.61441 | -46.41735 | 2025-09-12 04:29:00 | NOAA-20 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e5ae6206-51b6-3826-9154-ac8b1f5d94d4 | -22.69752 | -48.69943 | 2025-09-12 04:29:00 | NOAA-20 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5b7ce904-7589-32be-bbf8-69fb999e8aa4 | -21.95418 | -47.54294 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d5a685d5-a875-3f9e-a6e4-5082a1001d9e | -23.71194 | -47.40004 | 2025-09-12 04:29:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 61e0f938-ba5e-3cce-9fbe-5f56c18e8a37 | -23.84241 | -51.07616 | 2025-09-12 04:29:00 | NOAA-20 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| da8e5e15-16e8-32d5-83d4-36e4fd35fc1d | -20.80712 | -46.89005 | 2025-09-12 04:29:00 | NOAA-20 | PRATÁPOLIS | MINAS GERAIS | Brasil | 3152907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2d952ad4-dddf-3bff-8376-288a11cb90d4 | -22.25878 | -49.56159 | 2025-09-12 04:29:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a71e973d-7034-323c-9115-28dd9364bbfa | -23.19406 | -49.65524 | 2025-09-12 04:29:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8e373f68-ffe2-3e28-8e52-d898450b1196 | -23.35006 | -47.19996 | 2025-09-12 04:29:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 92c3ad96-d68b-3dae-9931-924d4a01b4c8 | -19.99766 | -46.92584 | 2025-09-12 04:29:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| adb6e384-6efa-3490-8f6f-fac4060bec0c | -21.33483 | -45.03392 | 2025-09-12 04:29:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 06cad5ed-6013-3182-8f07-88401654ab2e | -23.12681 | -47.48805 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f17f1760-7bc4-3ab7-882b-5f5c4e8721f8 | -23.21958 | -49.42709 | 2025-09-12 04:29:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f1a0d945-5cde-397d-81f7-406ae2d32b98 | -21.16943 | -45.11136 | 2025-09-12 04:29:00 | NOAA-20 | RIBEIRÃO VERMELHO | MINAS GERAIS | Brasil | 3154705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0d980eea-7eb4-3551-bb69-afe23fdefa4e | -19.95256 | -49.27034 | 2025-09-12 04:29:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6e0933dd-c1db-3199-9d39-eff09d6420e2 | -20.00973 | -47.65359 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 31cfa8e9-c358-3f65-bbe6-b2525eae143c | -21.17642 | -54.9712 | 2025-09-12 04:29:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c0d608e-8aba-36d0-b62d-231d076a1686 | -20.65164 | -46.53323 | 2025-09-12 04:29:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4c50dbd-b26a-330e-9ee2-3eed458e6aac | -21.29303 | -45.9536 | 2025-09-12 04:29:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| ae9e20f9-7fa2-3786-bed5-674d790af30a | -24.08113 | -48.8912 | 2025-09-12 04:29:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 49877b77-4621-3197-8c33-23cef192e48a | -23.28747 | -46.47701 | 2025-09-12 04:29:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9a2a4e19-cf5a-3be1-a5d2-9a50c894d7a2 | -19.99593 | -46.91307 | 2025-09-12 04:29:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5367beb3-e578-34bc-98c0-a06282f2dc01 | -20.98485 | -46.98508 | 2025-09-12 04:29:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 686c4f07-5a78-3361-bc11-9b236ac03f1f | -23.10863 | -47.48944 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1025689a-2c45-3892-81e4-8a9b7c367a0e | -22.19332 | -49.72353 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c392fe0c-5ed7-3203-acf8-c69740a957b4 | -21.95122 | -47.56348 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 082b1921-ba0f-31da-b867-d46697fbdee8 | -20.00917 | -47.65736 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bd750e4a-c330-31e0-a0c5-3553d9024782 | -23.14367 | -49.65427 | 2025-09-12 04:29:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 9d190e4e-f3cc-3586-b867-58938d27a94a | -21.33363 | -45.01272 | 2025-09-12 04:29:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c1765a5e-7b36-3282-87da-718847453808 | -23.19521 | -49.64773 | 2025-09-12 04:29:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6d4ab880-b8fa-3a40-b0d7-19b9d2c849c9 | -21.94371 | -47.56633 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad3e549d-25f2-3464-aab2-f03259c47be1 | -22.69744 | -46.2204 | 2025-09-12 04:29:00 | NOAA-20 | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2ad646d9-f5d4-33ad-82dd-7678d1ada5e8 | -22.19373 | -49.5895 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 335cac21-f720-399f-a5cc-902f89ddcd36 | -20.58195 | -48.57617 | 2025-09-12 04:29:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fda99b2d-1ee1-318e-b2c4-85529747e945 | -19.95198 | -49.27401 | 2025-09-12 04:29:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 931a99ed-386c-3328-a700-0760235b661e | -21.26945 | -43.8638 | 2025-09-12 04:29:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 1bcec6ad-c9bc-346b-9715-d79e9d0e2b03 | -21.19088 | -47.53357 | 2025-09-12 04:29:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 56.0 |
| a54bb62b-7dca-31ec-a2fc-77bad03096fb | -20.14823 | -47.37888 | 2025-09-12 04:29:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ac64a55-cd93-3d41-b54c-6621ce72ee14 | -21.1786 | -54.96887 | 2025-09-12 04:29:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c9210f1-1bc8-3ad6-a052-88d572f49577 | -21.96688 | -47.55346 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78a5f865-fcdb-37f4-a5a2-f99b86f4d1ad | -22.70146 | -48.69617 | 2025-09-12 04:29:00 | NOAA-20 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a5eee65-93fd-338c-84b2-06cf5eb4ed39 | -20.01145 | -47.64201 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59d737b6-da6d-32c2-a8f6-9240837cc81f | -21.18801 | -47.52897 | 2025-09-12 04:29:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 99987fa5-5c6a-3c15-ad38-0648f06406dc | -21.32129 | -45.01584 | 2025-09-12 04:29:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 25b76605-ec26-35c5-8b94-52550caeb5d3 | -22.19274 | -49.72725 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d9b00e5c-ad97-33f0-96d9-278d4da94ae3 | -20.35001 | -48.40275 | 2025-09-12 04:29:00 | NOAA-20 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbd38673-027a-388b-870f-319805ed34f8 | -23.13469 | -46.75308 | 2025-09-12 04:29:00 | NOAA-20 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0f2b2e23-c0da-346d-a34b-ef0a9737fe84 | -21.62691 | -46.80096 | 2025-09-12 04:29:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 42f714aa-38ae-3647-b4bb-c693abb3888d | -22.85989 | -46.55795 | 2025-09-12 04:29:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 867aaf1a-bd53-31f8-b9c4-e4ae22ff6b9a | -21.64811 | -46.40797 | 2025-09-12 04:29:00 | NOAA-20 | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e3d58414-4e27-334d-bedc-a43778c14d7e | -19.99443 | -47.6391 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79ae82a5-a672-33d2-b910-aaf2349d98c5 | -23.14388 | -47.46903 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 2b73dd05-feee-339d-87e8-f2e7a1dfcf80 | -24.12178 | -48.70774 | 2025-09-12 04:29:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 867b5f90-bef7-3292-8f7a-265ff661c021 | -20.70009 | -46.07187 | 2025-09-12 04:29:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cbde4fe-d527-3dc9-8e30-3d39d9754e0f | -22.75227 | -46.19057 | 2025-09-12 04:29:00 | NOAA-20 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d6541867-1de7-3bd7-90bf-8f833797bed2 | -24.68993 | -48.95535 | 2025-09-12 04:29:00 | NOAA-20 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| df7c1101-c0c6-311b-bfdf-7196ff313c79 | -25.05249 | -51.88998 | 2025-09-12 04:29:00 | NOAA-20 | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f7a9bc53-13e6-3c82-acdc-ab89ab686932 | -22.27748 | -45.38633 | 2025-09-12 04:29:00 | NOAA-20 | PEDRALVA | MINAS GERAIS | Brasil | 3149101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4adb82b8-3aec-34de-83d3-b46c175ea17b | -19.97853 | -47.6286 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90127d75-6546-3c72-a498-a1bc79f9e98d | -23.39372 | -46.70956 | 2025-09-12 04:29:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README96.md)
