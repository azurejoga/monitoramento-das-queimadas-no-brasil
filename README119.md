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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cb0aacb-23f6-34f2-a2c3-2a28c871ad74 | -15.8976 | -57.18769 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb9e8cbd-f582-34a5-8a26-8ed554e1f894 | -15.89428 | -57.18715 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5beb07f8-18e5-38bf-b318-a68141eed5bc | -15.89041 | -57.19017 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 769df854-d29b-3b57-a906-c5e7c63b1815 | -15.88764 | -57.18603 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 457d354a-e3a1-3d15-96de-98455bf3d990 | -15.88709 | -57.18962 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35fd6ca0-7766-342e-afe1-f75aaf93ec48 | -15.88432 | -57.18548 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d739a9ab-b3aa-36a0-907a-6cbf482cd07a | -15.8092 | -57.34262 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb22fb22-7eb9-3172-8505-9affa5405b78 | -15.80865 | -57.34626 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41899df6-899a-3786-b823-e8c1a12e0e26 | -15.80755 | -57.3756 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b314f5f-8c3b-31e7-8168-32a28ce17d83 | -15.80533 | -57.36795 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fdd514b-b4d9-303e-bab0-82a7ae178479 | -15.80533 | -57.34573 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f95641a-b5fc-37c1-bc47-38dd57e6fc03 | -15.80478 | -57.37149 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d84b89ac-89af-3fe6-8f89-5cbcce363de9 | -15.80478 | -57.34939 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d29012e-5f78-3291-83cc-3962c6127d51 | -15.80423 | -57.35305 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04172379-c093-3a21-b71b-7287b23e7e53 | -15.80367 | -57.35666 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83d2eb2e-4f13-3806-8dda-523163bf09b7 | -15.80202 | -57.36737 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6cbbd87-3766-3752-b773-fcf248577180 | -16.63543 | -57.25124 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 161.3 |
| 1440aa1a-64b3-3d67-b566-c3d2a0ffa0e6 | -16.63488 | -57.25488 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.6 |
| 62da8ad0-c824-368b-a23e-6a00fc7f3179 | -16.63432 | -57.25851 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.6 |
| 7567c1af-607a-3f3e-82be-8894bec332bf | -16.63377 | -57.26215 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7a06ed9d-0adc-30b5-bccc-074a4222de6d | -15.56293 | -56.90762 | 2024-10-01 05:08:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76dd9a94-fc2d-33be-b3c6-2c321b861b03 | -15.55959 | -56.90714 | 2024-10-01 05:08:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4d0688a-ec4d-3bd0-b795-ed6f9f07600b | -15.55681 | -56.90294 | 2024-10-01 05:08:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6f37a9b-4981-3731-8be8-9092da05e67e | -15.55626 | -56.90666 | 2024-10-01 05:08:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8114bb7e-3a20-3361-ab1f-a6002cfe75a2 | -15.55348 | -56.90245 | 2024-10-01 05:08:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34d53135-994d-3279-9829-9fb65ec73aff | -15.55015 | -56.90197 | 2024-10-01 05:08:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0453622-411d-3ab4-8eeb-71c72f0a5b7a | -15.41946 | -56.86975 | 2024-10-01 05:08:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d923b976-2676-3368-86c5-dcba581aa893 | -17.11304 | -56.73837 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 5efa364e-b607-38df-adc0-892ef9fb4e92 | -17.09955 | -56.73619 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ccdf1c6d-1388-31bc-99ab-2994c344b6e7 | -17.09618 | -56.73564 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 50db1859-31c9-3c03-9b03-709ddcc790a0 | -17.09562 | -56.73939 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 006d38a2-bb67-3a6a-a18c-5c81e5871f0a | -17.09451 | -56.74688 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d2c1fbb9-a47d-3e47-b0a7-3f6b648bccda | -17.0928 | -56.73509 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| d265edf1-76c8-3007-85d7-2c6d9ca36112 | -17.09121 | -56.73557 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 15dca72b-4364-392f-8805-4fb52fcfa058 | -17.09114 | -56.74633 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 322dbcc3-73eb-334d-ad70-d2390fcd582c | -17.09003 | -56.75383 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1c81a1da-22d9-38ec-a0b1-9f65ecc14abc | -17.08952 | -56.7468 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a7e7b9cf-d0bb-34a6-a049-ae28d1c1cd5d | -17.08896 | -56.75054 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 41f5d754-1078-362e-bc73-2eb8f6844a60 | -17.08839 | -56.75428 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 4ccba647-1794-31a9-be69-8c30c73dc2c3 | -17.08728 | -56.73877 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 68447395-6efc-3626-b427-5639843b9916 | -17.08672 | -56.74252 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| bc3cdeff-d454-3d8f-ae28-3d1892848106 | -17.08503 | -56.75373 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| d64f594e-3cd9-3d5b-aa7d-d320b23802d7 | -17.08447 | -56.73449 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 997cf1ab-df64-3f7f-9010-42445560e56a | -17.08446 | -56.75748 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| e02e93db-ffa5-3a50-9f35-233a9e5c2419 | -17.08391 | -56.73823 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| da2d3cfa-baca-3b6a-9a6d-6e21203c323c | -17.08335 | -56.74197 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4b40d7aa-780c-3e66-ad4c-7f34c2334987 | -17.08278 | -56.74571 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d3277e8a-1225-371f-8dec-7ba7a16c2941 | -17.08165 | -56.75319 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2b9ddf8f-bcfb-3599-8cda-eedc684b3e84 | -17.07829 | -56.75264 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e4fe5a96-d55b-3aea-b7f0-1f26c8aaf2f8 | -17.07716 | -56.76012 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8d47785b-8a7c-370b-b845-54b48662dff0 | -17.0766 | -56.74088 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| fccbb81c-23a7-3858-8536-4053cab5e1f3 | -17.07435 | -56.75584 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 664f86d3-d957-309d-9c51-6758347e12ed | -17.07323 | -56.76332 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 11e48a11-e498-3488-8a1c-1059449fc0c9 | -17.07267 | -56.74408 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ca1d654d-6ce3-34bd-9123-62d80b85cf92 | -17.07211 | -56.74781 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2ba36102-68a0-3ca4-ac8d-0ec34b974915 | -17.07043 | -56.73604 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3e62a0b2-da8b-35af-840f-2977b59cbe61 | -17.07042 | -56.75903 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| af9c82e8-8acc-35be-93b7-cce49c11a78d | -17.06986 | -56.76277 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8c3d1eed-d9c6-3dee-88d0-09ac86a6423e | -17.06986 | -56.73978 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 051b9266-7c22-390e-a249-c3a63430c05d | -17.06818 | -56.75101 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3bd8406b-21cd-36c0-91d5-d09e710e3f31 | -17.06706 | -56.7355 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4598cd18-3e95-3997-a599-50f73e96a03a | -17.06649 | -56.76223 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 66843940-e50b-35f8-86d7-290368712ef2 | -17.06593 | -56.76596 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5d59e362-1abf-3604-97d7-d180198ae897 | -17.06256 | -56.76542 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d5aeacdf-12c7-3128-a458-f844ad0c32ca | -17.06088 | -56.75365 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b008e0f4-4588-3c9c-9e3d-ba4f4b3de1e2 | -17.05639 | -56.76058 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b3d00af7-bdeb-3550-aabb-3bee858ec4aa | -17.05077 | -56.75201 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1ecbf935-afcb-37cc-84f6-1e2f666b4a0e | -17.04965 | -56.75949 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| dc043392-a68d-3497-914e-f0e79405d3ea | -17.04964 | -56.73652 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 619ce2bc-ed1d-3b23-8ba6-b72f8b5dd863 | -17.04796 | -56.74773 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 20c2d106-e1de-3f82-a19e-37a8ffc32e5e | -16.64819 | -57.23471 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 92208e42-34f9-36e8-9fb7-61e96db20d8c | -16.64541 | -57.23053 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 903f7b16-b423-36dc-b9f6-437f1b883d6a | -16.64209 | -57.22998 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1e6413ed-18af-3865-869f-4893298c4711 | -16.65483 | -57.2805 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 706558cf-da6a-3089-8917-fd492865a3bd | -16.65316 | -57.2914 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 449bbfb9-b8d4-3aee-ba18-01a6dd6fd966 | -16.6515 | -57.27996 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 2ae55a57-0160-328c-b05f-752983f8e689 | -16.64874 | -57.27578 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e260cb5c-3b7e-3690-9b0d-18cf31e3863a | -16.64651 | -57.29031 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e2172cb0-cdc4-3a78-b8d6-e950f3820271 | -16.64596 | -57.29394 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2a377d9c-6d5d-3805-bc5a-55d76a500b38 | -16.64541 | -57.27523 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3f49b88f-a751-3aad-a06b-418acc4a7959 | -16.64485 | -57.27887 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f85600c3-19c9-3fe0-a44a-4f70f7daebc8 | -16.64208 | -57.27469 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b601f2b3-61ef-37a2-9f51-63e20adb3367 | -16.82419 | -57.54976 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6c803da8-f032-3587-9b03-0588baf7ef32 | -16.82253 | -57.56059 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3821671d-b70a-3ef1-b49f-818005941f27 | -16.82199 | -57.542 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f30894b7-4a9d-34cb-98a0-7cb47c91d38b | -16.82149 | -57.47887 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 23dca19b-7c27-3eea-9d1a-e5b6bfe4ab3f | -16.82143 | -57.54561 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| aac7fc06-28dc-3eea-b7a9-3660b0e03b49 | -16.82093 | -57.48249 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 110bfabe-fd57-3315-a15e-799d5e078819 | -16.81921 | -57.56004 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b252f9b9-7556-3284-8910-5731bfacdf66 | -16.81867 | -57.54144 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 8b8f405e-86f1-3c70-8768-65a2d869c4cf | -16.81761 | -57.48195 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 00c5d9e9-217e-3600-9369-c80786b60ea5 | -16.8065 | -57.55423 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c9a9fdf4-39f5-390e-8855-a977890ac917 | -16.80595 | -57.55784 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 734e1d58-0ead-3d01-81ee-4e128e993e0a | -16.80047 | -57.48281 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| cbb0781a-16e1-3d3c-b2c7-c9a2e93b6b2f | -16.7894 | -57.4884 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| cb7206cd-75a6-33b3-a01a-cc3f81077c24 | -16.78885 | -57.492 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 391c61fe-b8bd-382e-9fd3-0bea56bf0838 | -16.78774 | -57.49924 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| c6ace455-74f3-37e4-9de2-b3f3bf5c6a57 | -16.78609 | -57.48784 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| fe824861-49b7-30df-acfe-793a0b0ade73 | -16.78553 | -57.49146 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3a6f9043-13ca-3f96-9f27-d360fb61fa7b | -16.74317 | -57.48041 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |


[Clique aqui para ver as próximas entradas](README120.md)
