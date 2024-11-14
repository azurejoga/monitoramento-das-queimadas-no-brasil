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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6b86dc8-e0ec-3533-b9d8-38b41f7c1ea4 | 0.3285 | -50.97277 | 2024-11-14 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6c48545-e8e7-3950-a2c7-cfa87b9d23bc | -1.80109 | -52.17071 | 2024-11-14 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| de613acf-2c5f-3434-bc6e-f0f114a8eb17 | -1.40193 | -51.12843 | 2024-11-14 05:27:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0279afc5-bc85-3f4f-80cc-f4edba0b7b99 | -0.10041 | -51.50522 | 2024-11-14 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a001735b-35ed-3ebd-b1f2-a54d9297b5f6 | -3.74589 | -50.45337 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b751b6a-09b7-3ec5-ba98-f41c44931101 | -1.21659 | -51.74734 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2c54b556-922c-3360-8516-7b2f8ae7bc9c | -3.47206 | -50.30854 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e989271-db03-3b03-8a29-88c5d2c1bd04 | 1.05431 | -60.60126 | 2024-11-14 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e795a5d1-886f-33f5-9042-ccc678ccf9af | -2.87912 | -51.79842 | 2024-11-14 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e794baf3-ba1d-3aa4-a95d-72c354a7e77c | -17.69234 | -57.54531 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3e18c969-5d99-3c8f-a376-f81bb05dd7db | -16.0739 | -59.70671 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd2fd246-a468-3d7d-829a-3f0a3bc70479 | -16.00696 | -59.39752 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 618a5b97-fa51-34b3-bd6c-b03315080e43 | -17.5849 | -57.54923 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| d8256629-ead6-37c3-a6ed-bf19af76b1ab | -17.72132 | -57.49911 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 957ffc50-6052-3016-9b8d-4ad34907c33f | -16.00999 | -59.38593 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 560006d4-c92e-3aae-aa8b-b1f71f2fece0 | -17.59662 | -57.49096 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a3b0f21e-1335-3612-889d-075983126ec5 | -17.58978 | -57.47003 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ab50e02b-2293-304f-aaf9-6c0b7aaaa276 | -15.8878 | -59.28387 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3e70eead-9f1f-32ed-acc6-93afe3b0c923 | -17.58372 | -57.55899 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| ad2f5976-062d-376e-afb4-fb4c8c7ec191 | -16.09993 | -60.09545 | 2024-11-14 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 21f473bf-d784-341d-9382-23d9eac9ced6 | -17.60302 | -57.47677 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| cc05aa46-10e7-32a8-8359-bb7a09356f81 | -15.90599 | -59.28271 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f5e3a3be-535e-38eb-a514-eb252bb542dc | -17.26296 | -57.47641 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| e6c69042-3210-3030-ada8-da5572ce5b39 | -15.90823 | -59.28333 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d7162e43-0081-30ca-9f64-7dd5218b53a3 | -16.00386 | -59.40106 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82ee5144-5c70-358b-9606-c5afcb75e057 | -17.63198 | -57.54545 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 812ed755-065a-30c9-b601-6ff9190caa92 | -17.59439 | -57.47063 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0f583263-e9f6-3914-9802-32c34aaffaf7 | -17.59261 | -57.48543 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 3f2f83d8-5af7-308a-88ef-5367228699f7 | -17.58031 | -57.54863 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 4494e6ed-3bc2-3554-901e-f4a907a9ba0b | -17.58948 | -57.54984 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 9ebfebfd-8cee-3293-afb9-fb975bc4842b | -17.60063 | -57.49648 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b1460281-c0c3-3d57-9049-b77dd2dbe542 | -17.21458 | -57.22609 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f31afc99-3ba2-30d6-9147-ad5a887e8ae0 | -15.87538 | -59.28539 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a5ffd55-071d-3814-ad6e-75457ac914c0 | -17.59602 | -57.49588 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d0ccbd99-75ac-3b2c-b96e-dcb1a461216a | -17.58768 | -57.40925 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9e9645e4-c334-3d94-a779-0edadae4df00 | -15.41079 | -58.60654 | 2024-11-14 05:29:00 | NOAA-20 | INDIAVAÍ | MATO GROSSO | Brasil | 5104500 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d1b72f8-6fdd-3fef-8281-5709b4160c8a | -15.8819 | -59.29737 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 848237d9-8c13-383f-824d-13d722ccf134 | -15.89626 | -59.28155 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3079eab6-5dfe-34a9-9a35-6fa21f94b037 | -17.25837 | -57.47581 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 67adc5d5-e21f-38c0-b7dd-7f44a27c5cfe | -17.61302 | -57.54794 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 463fa84d-b425-35b1-a420-106770cefdcb | -17.59348 | -57.5553 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| c3fbaf76-485e-3669-9992-f28697a94460 | -17.5932 | -57.48051 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| baa5a717-60fa-30fc-a041-b98db912263c | -16.00631 | -59.40247 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df36244d-ff5e-3ed5-907a-ea6fec574d69 | -16.00852 | -59.39665 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d95f727-6db1-39eb-91c2-dd88af25e7c6 | -17.24578 | -57.46423 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 16aa5af4-4db2-3819-8caf-acf95a94c50b | -17.63718 | -57.54114 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b927fdf0-c6ee-3220-9b8c-c9a917096fbd | -17.6309 | -57.55219 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 26b280bc-01ea-31d4-add6-7dc2c454492f | -17.59866 | -57.55102 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 51c594ad-d9da-33e6-8a0b-8c71b7856570 | -15.93545 | -59.27546 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6ae6eae-aab4-3a22-b605-39230cbcfe5f | -15.86992 | -59.29569 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7774da98-9181-3a64-af7c-2cc266eee615 | -16.18479 | -59.35778 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0476a8d1-e6f0-3091-9ff4-659511fcc859 | -16.00234 | -59.40186 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04cd69cb-6b27-3bc2-853b-ca0a9bcc90eb | -17.5729 | -57.53277 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 09976d0c-b3f8-366e-822a-da5d799a602f | -17.57972 | -57.55352 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| ab44cccf-595f-3f3e-a15b-c8def72ceaaf | -17.28786 | -57.30895 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e27b85c4-ddda-379e-a80b-45cce17b4121 | -17.70612 | -57.54712 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3a8463b0-7cf6-33ed-bcb7-5d34f431f3cf | -15.91 | -59.2832 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| de16d2de-3ac7-3f34-bd49-539468063f2f | -17.59083 | -57.5002 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 31361dd9-50ab-3a77-ad83-89c023105b82 | -17.58149 | -57.53886 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 89df0efc-91fe-3d01-ad68-e574ab7a7302 | -17.24978 | -57.46972 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.2 |
| 7636a999-97e7-331b-ab9a-5c7d535dd3f3 | -17.57514 | -57.55291 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 484df935-72a0-306c-a9ca-0d28b70f3c92 | -17.27095 | -57.48737 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e54eb1a5-2b06-35b2-9caa-943758978c7e | -17.63494 | -57.44574 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 93a7c4f8-159d-3c00-bb1e-a56b53538ac9 | -15.90423 | -59.28283 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 610406e3-819e-3680-a0fc-8bf698652146 | -17.5809 | -57.54375 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| fc81697c-4c20-3a97-9090-f66c14307f84 | -17.5769 | -57.53825 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3c1bdc3e-44c0-3ead-9a04-ab497efa3abd | -17.63137 | -57.55033 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| bf1a12c4-f095-3898-9b4e-94f4eefe8da7 | -17.63032 | -57.44514 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 46370ed7-419f-346b-a458-98846623f17c | -17.60843 | -57.54734 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ece554c7-f9b6-37ca-b9f7-4293ffeedf2f | -17.59721 | -57.48604 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| f3cede3f-4ec0-3096-ab3b-431f15245557 | -15.88381 | -59.28321 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52b3c8e5-4d86-399c-a48c-8b9fe23bde79 | -17.26178 | -57.48616 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6b52718b-9bf7-3c87-8d17-af960ac5d6d5 | -17.59407 | -57.55042 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| b8a42d67-8b4a-3230-8ae6-eca5538c2340 | -17.2925 | -57.30956 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 92d0856a-a009-33db-b892-148407e2d7d0 | -17.61821 | -57.54366 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ddec24c7-c31b-33dd-add8-fd3367900a0a | -15.89177 | -59.28456 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b80f54cd-7f8d-3400-91c6-8e240f4c9078 | -17.71011 | -57.55263 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0e220e41-006a-3391-a89b-2621668acf38 | -17.60783 | -57.55222 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 551cc206-8e2a-3ec9-b51f-27c5e0ad631c | -17.70731 | -57.53731 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 1e430ee6-5da0-3979-836a-0948a6ee6d40 | -15.92346 | -59.27368 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f6adf75-d738-35b7-bd9d-0aa008e98702 | -17.25437 | -57.47033 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.2 |
| feae2726-abb7-3328-95c7-a3ece92fd5ab | -17.29169 | -57.47026 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4f808330-4b28-3326-a8e2-dd9ba88e7fca | -17.26237 | -57.48129 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 951f7cc4-3aa8-334f-ae5b-fdffea954fcb | -17.63147 | -57.5473 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 505e03b1-9e1f-3e04-b8bc-3341250b6c8d | -14.4989 | -56.91929 | 2024-11-14 05:29:00 | NOAA-20 | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb5bdb67-61cb-3771-875d-ead6158f66bb | -16.95347 | -57.643 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 570ca89e-3613-375b-a027-a47d30a8ce30 | -17.5883 | -57.55958 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7f0aa918-c993-3e45-b38e-8ab4da8c7360 | -17.56772 | -57.53705 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f356dad0-19ce-37c3-b16b-e4591851c723 | -15.26335 | -60.23351 | 2024-11-14 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2e02616-75ba-3074-a9a9-025422c5f9f5 | -17.63663 | -57.54299 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| eddec064-849d-3d73-8b69-38144bf7099b | -16.1888 | -59.35826 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7731917c-a7c5-32e3-b297-3e1246f3f014 | -17.2532 | -57.48008 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 579be8d9-dfe5-33ed-a07a-cd8feb601166 | -16.00925 | -59.39135 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11cea00f-e020-3a60-9250-bc1461920230 | -17.63204 | -57.54239 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 426287ea-d140-3c99-b40e-c31625a281b7 | -15.87391 | -59.29625 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4199c068-9656-3fba-a707-57f38912fbad | -15.88636 | -59.29441 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ed69dee-598c-37b7-94fe-e61e26ea7d0f | -15.88236 | -59.29396 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb4d04cb-3381-34db-8546-9d52d17b1b55 | -17.59201 | -57.49036 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0635f13a-e289-372c-9549-e9d62c00dca1 | -17.23601 | -57.4679 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 7b19861d-0849-3af7-b40d-1f2b5b6851e9 | -17.26696 | -57.4819 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |


[Clique aqui para ver as próximas entradas](README54.md)
