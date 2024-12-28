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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66931bcc-4536-3f1d-82b6-288fdbad41bc | -3.98858 | -46.69763 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 967c297f-8cb9-328d-a72f-b5169909da0f | -3.88833 | -46.69265 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e7c23652-d3fa-31a5-abda-ec896f5bc16f | -6.20334 | -41.57055 | 2024-12-28 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8800576a-b99d-366a-9837-74a7849ef334 | -5.90825 | -43.48104 | 2024-12-28 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c00a9f68-f864-3a35-972e-21d1279743bf | -2.90635 | -54.48895 | 2024-12-28 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 34537b1f-1af8-3bf3-8b39-1fb15501feb1 | -5.37269 | -44.8425 | 2024-12-28 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b7da68e-6008-3173-b717-b259d968e5db | -4.04667 | -46.72105 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d2527188-e916-39ba-9868-f3c7eb236eea | -2.22626 | -50.45742 | 2024-12-28 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f03b547d-43a9-357b-ad7c-e96d9769cd7c | -5.92933 | -43.77871 | 2024-12-28 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 528ed133-c297-3518-98ae-a12a788e87c2 | -2.21997 | -53.64529 | 2024-12-28 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| afd7a966-5c56-38e0-8cf3-e79ac6117ce7 | -6.11769 | -43.94427 | 2024-12-28 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d8cf193-2348-343d-b49d-e67e31182339 | -6.39281 | -38.91059 | 2024-12-28 04:14:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6d9f2e7c-7e7f-3ad2-8979-eb5766bfe93d | -2.51617 | -51.8556 | 2024-12-28 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8061bfee-3fb7-3c83-ad5e-ceb5b9fb7093 | -5.24569 | -41.38858 | 2024-12-28 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7b87014b-3978-33dc-82d5-138bba74c019 | -7.92554 | -39.54562 | 2024-12-28 04:14:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c427c18e-08e8-38bf-868e-993099c0958f | -5.98735 | -44.59706 | 2024-12-28 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26452ac7-888f-3c04-8534-5fc712d35039 | -3.97495 | -46.34415 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6df91af-dc8c-3c97-a1b6-b47142e0ffa3 | -3.95017 | -49.44888 | 2024-12-28 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ed10a46-410d-33a6-9cf0-e6ee3b0d27b2 | -3.84155 | -46.69466 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f1306baf-9efb-35c1-8695-fccf02540946 | -4.77912 | -38.55078 | 2024-12-28 04:14:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9da8b913-1d2b-33fb-a6fa-9dd36e3916e5 | -2.00263 | -45.58976 | 2024-12-28 04:14:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 92a1817b-fb3c-3754-9ae1-9b49610701c2 | -4.48704 | -45.67874 | 2024-12-28 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7d769fe-fd71-3dd1-a6e9-a78ee401d15e | -3.85518 | -45.29956 | 2024-12-28 04:14:00 | NOAA-21 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c28ebb5-1c7f-320e-8e6a-795dda841f53 | -5.10324 | -38.29357 | 2024-12-28 04:14:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4509296b-081a-34eb-92b6-d4854f437d28 | -3.96515 | -46.67546 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 024bde14-5d5b-3c82-baa3-85562925d2e3 | -4.03914 | -46.71981 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e9da931-8a1c-3fd6-9b51-4d958ddf9d76 | -3.81615 | -46.70682 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfb2a4c6-0e53-3041-b864-b0f55984b83e | -3.95758 | -46.67445 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d84c7d9-ecc6-37aa-a662-c7f74f74eef8 | -3.97487 | -46.58513 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60de72e8-2a9f-3421-9013-c35f48e8f017 | -4.01109 | -46.92062 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd789944-da45-3267-ba7f-521e26f11cc6 | -3.92617 | -46.98466 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 768f3d84-c985-39f4-b750-8ebc091f1218 | -5.93767 | -45.57014 | 2024-12-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65191fc8-3265-3bbc-aafb-85ad3e22ed3a | -3.9071 | -46.89111 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 49db83a9-4c2b-335c-8829-5926d5df9f58 | -7.26 | -41.30698 | 2024-12-28 04:14:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b5f3182d-e03f-3fca-9ab1-f1e6176c41df | -3.81688 | -46.70221 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e558ad37-e867-37ee-ba7e-7b2ec51fd11c | -4.53911 | -44.05097 | 2024-12-28 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e966328-6add-30a3-aa94-f6a70811454c | -6.71695 | -44.15775 | 2024-12-28 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3169157e-6213-3948-bf62-f3a19d8493b6 | -4.00048 | -46.93804 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c26c66af-43d7-3564-84e6-62c94f5c81bb | -5.23783 | -41.3948 | 2024-12-28 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 349260e1-88df-3886-ba4c-09b644bd819e | -5.24066 | -41.39889 | 2024-12-28 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 86d0ee7e-afe8-33ad-bbff-41932f689ba7 | -5.64675 | -43.71609 | 2024-12-28 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1b72502-2bb5-3679-ae00-8cb48c895557 | -1.36848 | -46.61332 | 2024-12-28 04:14:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44c8bd2d-6717-306d-a7f6-2d91755c669e | -2.21841 | -53.65471 | 2024-12-28 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0403cfb9-9bbd-36b5-a79c-5ed85979a397 | -2.48652 | -54.1658 | 2024-12-28 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b44b5051-d816-3849-ac83-e8ca2058d823 | -5.53233 | -41.73743 | 2024-12-28 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cfe8624b-18a9-3b82-bbb3-9ec69b09da98 | -3.94299 | -46.76285 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fe80c1ee-7e87-33d1-a213-ac0459710c03 | -3.9024 | -46.98552 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da1e3419-1850-3e91-99e5-0de607d05f95 | -2.33595 | -46.39862 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed071b66-48f2-3462-8729-3f772b391857 | -4.53382 | -45.56765 | 2024-12-28 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61f4f2d7-ed52-34c6-80a6-90a962fd3e22 | -4.03302 | -46.85624 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d6d8776-0d50-38b7-8d1c-bb8f1dc259cf | -5.24176 | -41.39165 | 2024-12-28 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 41a379e1-9e4e-36db-9ef5-bb4b0b0dbc28 | -3.89283 | -46.6888 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b680855-25cf-387e-89d6-98800a77327c | -3.96061 | -46.67952 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 95ad548f-0231-3f0c-b62d-c7bada2e1630 | -3.77471 | -46.81987 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d020e4e3-2f46-3261-b79a-39f854b09a6a | -4.04932 | -47.041 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 40866268-f2a8-3553-bbda-42023591fe25 | -4.01876 | -46.55883 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7422b7e6-20d7-39e8-927d-217c9991a946 | -2.29255 | -45.70071 | 2024-12-28 04:14:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c448c20b-6ceb-3335-a770-ef1896722cea | -3.84561 | -46.4978 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbfebce9-e492-373e-a9e1-e34e8038abfd | -3.86869 | -46.67075 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7777189b-beb3-3265-adac-4b2eee8843ec | -3.84431 | -47.03759 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab3e560f-6e5a-3fca-be2f-da810d42677c | -2.07726 | -52.04625 | 2024-12-28 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b606463a-abaf-3379-a1b1-df25a83df102 | -4.01185 | -46.91587 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8f42d15-30ed-3288-bcaa-ba282efd71f1 | -4.06476 | -46.99435 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 63e9b1ed-2ff5-3e90-b297-2d56c1a382df | -2.34011 | -45.82615 | 2024-12-28 04:14:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2e77a9c-dab2-3d93-91f1-e7dd2e5f7c4d | -3.99468 | -46.73161 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 49cf65b5-b979-3347-ac29-9eb803b0f884 | -3.89517 | -47.01586 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5ac28a5f-2013-3844-9965-307032b5bcec | -5.56658 | -46.29322 | 2024-12-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24dd7381-fce7-343b-9b82-c91f0f7084d7 | -4.08012 | -47.09491 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01439bba-7137-3be6-8383-70dbac696d2d | -2.48694 | -45.79849 | 2024-12-28 04:14:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f943d573-896a-3b11-a714-5c77a28bdb1b | -6.44734 | -44.37774 | 2024-12-28 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d644fe5-8828-3922-8b7b-1eb1d1420a17 | -5.76534 | -35.57005 | 2024-12-28 04:14:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 5.0 |
| fcdf3775-2b1a-33dd-8d9b-cd40bdac10ff | -5.09604 | -45.1 | 2024-12-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f94daf49-abce-34b6-bf5b-eb290e5a0ca7 | -3.99234 | -46.69823 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ddd1f8d-c37b-32ff-b2fa-ba549871bcbb | -4.04314 | -47.05475 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9aff2dfb-af97-363f-9f4d-815ff3ac05f7 | -4.00803 | -46.91527 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c97afb5e-b229-324f-a608-2166d807e230 | -3.56198 | -40.85535 | 2024-12-28 04:14:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3f4cc8c6-666a-3296-9755-7e7ec6431da5 | -3.97553 | -46.58866 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a8ceb73-4063-323a-9dea-17111077216f | -3.81773 | -46.72123 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5ec730c-155f-335c-9d01-f3c2993238b6 | -5.31682 | -46.06968 | 2024-12-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 92910135-78ae-302b-af77-6d96d5fd6bfe | -3.94776 | -49.44633 | 2024-12-28 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ac2d71d9-5167-37d2-8ad8-5ccb1889e1d5 | -4.71585 | -43.44807 | 2024-12-28 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bef9870a-7075-3f48-b0f7-bef9427ce091 | -2.33247 | -45.80299 | 2024-12-28 04:14:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 25bf36fa-4949-3486-b49d-7d9b3c52d8b1 | -3.8087 | -46.72923 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 592dccd0-ce21-32b0-a606-5da322885e0d | -4.03288 | -46.85408 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5831b89-3b84-3cc0-aff3-017b20b93e45 | -2.92233 | -41.09363 | 2024-12-28 04:14:00 | NOAA-21 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| aa3a9724-2fc4-3096-b32d-c0d4fdbc9e2b | -4.73965 | -44.64975 | 2024-12-28 04:14:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 389ce2fb-6ede-375e-a177-051b2dbba6b5 | -1.1532 | -48.84855 | 2024-12-28 04:14:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 022b2f7d-2c20-3e0d-b0ac-f8911a81257a | -5.91156 | -43.48156 | 2024-12-28 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 76acbfdd-92c2-313c-83c9-9abf51f88cb2 | -2.28766 | -45.59211 | 2024-12-28 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ad5e37b-6793-384f-81ea-e8d657dfcda6 | -4.11667 | -46.72114 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39efe8e8-e401-364d-a178-b766557578ed | -6.70874 | -44.31802 | 2024-12-28 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9c6a4c8-f796-3d71-ab95-e65fceed084d | -3.95304 | -49.44251 | 2024-12-28 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| beee8d9c-8456-36de-8add-f8456d7ef675 | -1.3411 | -46.99245 | 2024-12-28 04:14:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9448b987-abd5-3561-a799-7125769e7593 | -3.80382 | -46.8578 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcfc450d-f7f7-376c-908f-7b4cef2415c4 | -5.33479 | -45.14507 | 2024-12-28 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21e50f5c-74d1-3b7e-960e-7d6b06946a4f | -2.17352 | -45.40677 | 2024-12-28 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b151dd84-ed36-33ed-b02f-a8975111b8a0 | -3.92313 | -46.97923 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f979561d-3dba-3e8b-9140-38582767369f | -3.53423 | -40.9221 | 2024-12-28 04:14:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5eacc1fd-7d6c-3935-bfe2-fafa9c2a1c2e | -3.94371 | -46.7583 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9337d653-ccab-39e0-bd22-48d61314ab0c | -3.87005 | -46.56124 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README11.md)
