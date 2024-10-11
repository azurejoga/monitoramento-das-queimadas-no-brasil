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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d494de72-a1cd-3405-ae5d-5d3f1e664075 | -1.75458 | -55.32917 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9703cee0-0a2b-3439-ba8d-9425fc690bb0 | -1.75398 | -55.33307 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64d2ab87-ca96-3ab6-881d-5284d3ab4008 | -1.70384 | -55.09229 | 2024-10-11 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d20b06e-e579-3e47-bc88-6f9927973be1 | -1.66823 | -55.13567 | 2024-10-11 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 796592bb-defa-3fcf-bf55-85929df00e94 | -1.66763 | -55.13965 | 2024-10-11 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c8159ca-910c-3585-ab85-24416e1cd58a | -1.63737 | -55.05398 | 2024-10-11 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de89adf2-556a-3509-bae2-f99b6d86f116 | -1.55022 | -55.94925 | 2024-10-11 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de60cd0b-e2a0-3bf0-8c9c-960df3bd71fb | -1.54563 | -56.33551 | 2024-10-11 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ca3883d-fd7b-3bc0-a672-4c1cfe1ff5fd | -1.52987 | -55.42256 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9a85799-2c37-34db-9a5e-638a0ce75841 | -1.52758 | -55.41431 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c852177-759a-3403-a798-6d24aaeba025 | -1.52699 | -55.41817 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6892e3cf-ed7f-3e04-9c1a-7df07b8631e7 | -1.5264 | -55.42202 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c081e3ac-fa10-342f-b9d9-b1be49cbe7de | -1.52581 | -55.42585 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f20819fe-e35a-3612-b548-0b036105514e | -1.5241 | -55.41376 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17c62ef8-e636-3d5e-bd8c-2eb529c8576d | -1.52351 | -55.41762 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9697fa8-2f34-398f-8b95-7b3632b8d569 | -1.52292 | -55.42148 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c98d820-0b62-3f78-a77f-d3eef7c5b9de | -1.52233 | -55.42531 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8df5f661-144e-35a1-af36-07739ac7fd44 | -1.52063 | -55.4132 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 090fb870-3253-3b60-acf3-90f20691e7b5 | -1.52003 | -55.41707 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfa9bf0d-c415-31a3-85bc-0d099da9c4db | -1.51944 | -55.42093 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b630e48-bd9c-3711-ae0a-b1eb9c4710d7 | -1.49976 | -55.93379 | 2024-10-11 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 88826f0f-4804-3af6-913f-5cfc25ac55c4 | -1.47572 | -54.97301 | 2024-10-11 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| faa4876e-31e1-3d2d-806c-250062ffdd0f | -1.44399 | -55.20365 | 2024-10-11 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f5565c4-0264-3381-bf5d-86c3707451ff | -1.43346 | -55.08196 | 2024-10-11 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1afe7a1b-cb3f-3126-b2dc-faa1b1d16d0d | -1.3434 | -55.47396 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03224c17-489f-3c8e-908e-7d60e9642d13 | -1.34281 | -55.47776 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dadd7d5b-c8bc-3671-a22c-0a70fd42962e | -1.262 | -55.90564 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50963b87-ec29-371b-8545-fa834de4760e | -1.26142 | -55.90932 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61b278f0-896b-3004-ba8b-a4d3572bbf01 | -1.25424 | -55.70728 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04fa8f1f-2b09-3670-942b-04f96045664c | -1.25138 | -55.70304 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cbabb29-adb2-30bd-b27d-9b1a30f66489 | -1.2491 | -55.695 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c626c19-96b6-30ea-ab39-988a5473df4b | -1.24853 | -55.69876 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5cb4b8e-aa24-3bb9-bebe-40e6858f28ce | -1.24795 | -55.70254 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cdbbeae-2e86-36f3-bb00-f7338a6801a3 | -1.24004 | -55.68611 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84f9079d-9570-3d99-885c-373fdff21238 | -1.23602 | -55.6893 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20ed85f6-0f6f-3a8a-ac06-5fffc2a9db8f | -1.23588 | -55.8941 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80e3d4d8-db75-3cce-9f18-8eeee58f429b | -1.23306 | -55.77649 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37cbc564-733a-3bb2-bbc9-5f570d7a1776 | -1.21782 | -55.64841 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64284197-3fc8-36b8-b8cd-63ea8504c695 | -1.21596 | -55.86088 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 237c58f7-d9fc-3fa5-a69c-cf70e4a8226e | -1.21255 | -55.86034 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a92f8ff8-f1c0-323e-867f-37ba126aa322 | -1.20623 | -55.87825 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6cadeeb-5c68-3183-9c94-7b2b299b32e7 | -3.60487 | -55.4557 | 2024-10-11 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24295215-8480-3b1c-8490-9c78b87858ae | -3.55095 | -55.47737 | 2024-10-11 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aad0e99e-e9c1-3329-9ba6-1821d9d1748b | -2.43524 | -56.37152 | 2024-10-11 05:16:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 108e97db-c438-353a-b87b-d214fd284202 | -3.60548 | -55.45167 | 2024-10-11 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7382aee-4e14-3568-a765-1deb247e9d1c | -3.1552 | -56.6186 | 2024-10-11 05:16:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f46c9ec1-7477-3a3d-821e-28ba3eb851c7 | -5.03913 | -56.12333 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 474bea98-2f72-3503-871d-fe98af6d9f07 | -4.97907 | -56.18998 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2bdd816-b5ce-366d-92a1-044e95202141 | -4.97718 | -56.19063 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 148fcfb2-b473-38d9-8cb5-77434b1faa9a | -4.90449 | -55.9397 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8ae4599-2275-3354-b995-9579fb8d9692 | -4.86759 | -56.20878 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f370e1cc-fadc-3b78-919d-000f097fc2aa | -4.8377 | -56.20452 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd4c4872-d116-38e5-9ad8-5728bc2e2e4e | -4.83422 | -56.204 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3632ca43-968b-3f8d-8f3d-a75b938ce7d2 | -4.79943 | -56.22222 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20de28f0-dbe9-33d9-a6d3-36eebb9a7397 | -4.79596 | -56.22168 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4db5d0b-0f68-3bf1-b410-24ba85c2966b | -4.78814 | -55.89121 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5342133-cd73-3acf-ba39-7503b737e182 | -4.72108 | -56.14061 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01ec9885-cb0f-3901-a4f1-d8e60f40b8fb | -4.6635 | -56.10883 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0beac105-d922-3bfb-9ae5-77cbfafdb9bc | -4.66001 | -56.1083 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a21e6db-c5bc-3327-9205-856c28f90eb6 | -4.6453 | -56.01874 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 029bd36b-9b7a-349b-ae3a-6fd572910fdb | -4.53446 | -56.125 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f2f96cb9-610e-3edd-84bc-40ced10c61b0 | -4.47499 | -55.71246 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4a1f1613-6b2c-3e17-9492-75d17e3ffb46 | -4.05657 | -56.26435 | 2024-10-11 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cab21447-63ba-3323-846e-cab76ca74bb4 | -3.99722 | -56.08167 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b3ebae0-d706-3cf9-ab1e-bf8760335ef0 | -3.99664 | -56.08545 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45fdc03b-082d-3ead-9226-e9a1d7a80d6b | -3.99376 | -56.08114 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 887512c7-0014-34e0-8a80-48bbfbfaccd9 | -3.99317 | -56.08492 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13646b14-7b61-3c10-a4ae-908bd82469b4 | -3.90438 | -55.53497 | 2024-10-11 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46331f99-a31c-3571-9fce-5e5a95ffd804 | -4.98313 | -56.16306 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f026b704-c9c7-38ab-b656-81b7e58d5952 | -4.9785 | -56.19379 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86ed2aee-ee9c-3c14-a65e-4a8cee440418 | -4.92365 | -56.26077 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8df1711d-e31a-326b-9069-6658619a5a9f | -4.90424 | -55.93623 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdab5181-74a1-35c6-8419-f89f45a03107 | -4.90362 | -55.94022 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07fac2e4-3797-39ac-9476-4aa5b4d33cbc | -4.82118 | -56.07974 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f40addf1-5f8c-3021-8100-92b9ef735bee | -4.80001 | -56.2184 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6747dc97-f7d9-314d-9202-0d1a33a8c173 | -4.78753 | -55.89516 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 801fc246-ae57-318c-a492-935b2fd5e471 | -4.72456 | -56.14112 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ff455c4-1125-3389-89d5-08bf9f66c9f7 | -4.66138 | -56.1114 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2688996c-1ab7-3163-bf47-57c9a968e67b | -4.64468 | -56.16115 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df492ef2-9e63-3505-8c3e-cb5b531c79c4 | -4.6077 | -56.124 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd36f2c7-0166-3e75-a0e3-526263c30e5e | -4.5661 | -55.73327 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 022ee872-d3b8-3322-a7c5-9b2fab96c0ff | -4.55224 | -55.5372 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 817b5860-679e-379d-b65d-dbb3fc8ffefa | -4.53161 | -56.12043 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15fa35a6-35f3-394e-bea8-51e8ba641cc3 | -4.531 | -56.12437 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7e8ccf63-755d-37e4-929e-4532bdf28fcf | -4.31894 | -55.59525 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9cb0ddc-1f90-3e99-bab8-36e6e0a7e8fc | -4.31834 | -55.59916 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53ed1d58-ea33-3ff5-b6ab-77cec4faeb0a | -4.21769 | -55.66584 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13569132-a66f-3c9d-96ce-a78a888de070 | -3.90793 | -55.53551 | 2024-10-11 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7831cc53-d122-373e-8a66-6068836dd61f | -3.77693 | -56.79788 | 2024-10-11 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c1794435-a279-378f-9590-9eb99317111b | -3.73193 | -56.77615 | 2024-10-11 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4354448-26cd-3612-85cd-ebb1027d292f | -5.12408 | -56.11514 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72c28f56-6716-3ccf-87c7-48d4adc1d3b1 | -5.11049 | -56.22836 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3fad672-9a22-3c26-a024-6f7a837f77ef | -5.1099 | -56.2322 | 2024-10-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9dd2d85b-0351-3bd7-8254-c42cf868ca0a | -5.015 | -57.01228 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0550e10d-068b-3dc8-9517-4d0d019a3f83 | -5.01444 | -57.0159 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03004c32-24bd-324d-ac0e-b036fd50e034 | -5.01162 | -57.01174 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 834e9605-db80-3582-8980-c29c0df63202 | -2.05804 | -57.08341 | 2024-10-11 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 427142f7-27b5-3669-ae1e-e4f200000685 | -3.66263 | -57.09094 | 2024-10-11 05:16:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee659638-c730-3730-84d9-e648573b2c28 | -3.24898 | -58.19071 | 2024-10-11 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44b551d9-6ea9-3748-a7e2-91d496c192c8 | -2.98702 | -57.08411 | 2024-10-11 05:16:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README83.md)
