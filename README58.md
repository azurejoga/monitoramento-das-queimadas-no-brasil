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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f996ae54-4af7-35d0-91f9-715a957c6f6e | -15.62172 | -57.47535 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1e00148-228b-3425-b778-3b9bce389ff4 | -15.62103 | -57.47948 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e173df97-2097-32dc-90f2-72845ff572f1 | -15.62027 | -57.46233 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2dfeb0f-ad31-30de-b74f-0273fe454e22 | -15.61958 | -57.46645 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0113b5a3-07e7-320c-b199-7a8b70df920b | -15.61888 | -57.47057 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f77bee68-ba2e-331d-87e6-164b8fdf14f0 | -15.61818 | -57.4747 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee04c953-dd77-3213-ae09-d78a6c3d4a71 | -15.61749 | -57.47884 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 276e11ef-18a0-3301-9810-936128f2a919 | -15.61604 | -57.46581 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54a005b4-2b21-3df3-beb2-30ed6d2cc183 | -15.61534 | -57.46992 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6204372a-80ca-36af-897f-6d3862dfdf8d | -15.61464 | -57.47405 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb34fad4-9d6b-3e58-9b7f-1bb4836d28ad | -15.6125 | -57.46516 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d6aad30-c4c1-34ac-8b34-c623956f25a0 | -15.6118 | -57.46929 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 861f538e-c039-3ee6-9049-2405508c32a1 | -15.61111 | -57.47342 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6c8737b-6790-37b8-b9cb-7c59bb8951c7 | -15.60896 | -57.46453 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57974689-86d7-32b7-a26b-0d9829fd71c5 | -15.60826 | -57.46864 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d9030a0-e625-3239-8304-ec45b0c90c40 | -15.60542 | -57.46388 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4882e688-9a7e-347a-b0bc-0a3a32a0915e | -15.60472 | -57.46801 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ec7bab3-0eb4-3c29-861d-0180a4efee22 | -15.60259 | -57.45911 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c521dce-258e-397d-9a01-3e27df9a2d33 | -15.60189 | -57.46323 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0429e933-547e-37eb-9e20-e5cc98b92d0b | -15.59844 | -57.5051 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7ee3416-433c-3078-ae0c-7c0c8bd50aeb | -15.59835 | -57.46259 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a86f98c7-f4fd-351f-a78d-856c279cdd6a | -15.59765 | -57.46672 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a69757a-e774-34e5-9d75-2c0f94c23a6f | -15.59695 | -57.47086 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fa8b23ac-6f9b-35a7-8fb5-d23ee27a1c9f | -15.5949 | -57.50444 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aa595c2d-394a-384b-b479-2946a911bd37 | -15.59411 | -57.46608 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd324a9e-1d76-392f-80df-823140eb096d | -15.59135 | -57.50378 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e63ec7a-6a34-3e9e-b099-e02bacc0bc18 | -15.59065 | -57.50793 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3833edd1-dd1e-3e3d-b6ef-ae225fae0d2d | -15.58917 | -57.4737 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7cb5a747-2e59-3e35-ad83-4e56d3659d94 | -15.58846 | -57.47783 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9257119-62bf-3267-9078-1b44fc9141c4 | -15.58563 | -57.47304 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 588fcb99-c99a-32a4-b8f1-88a6292ccc54 | -15.58492 | -57.47718 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dddb4f98-ac71-3603-a3cb-26aa7c6fee8a | -15.58422 | -57.4813 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 976dc089-3303-3193-8390-5f99843321ac | -15.58139 | -57.47651 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3685583-eb93-3296-aa7a-14f28430c46b | -15.58068 | -57.48064 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c397828-caf6-369b-aa7a-8485f0035228 | -16.51256 | -57.35573 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d9b59af5-f77f-36dd-b889-53a025e8e0d8 | -16.50907 | -57.35509 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f4cfde9e-6f2c-388e-bf10-566103ea1861 | -16.50839 | -57.35911 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 15276d61-c322-3809-9abb-fed81574d670 | -16.50558 | -57.35445 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 58417df3-2403-3144-9f40-04426fa50f9f | -16.5049 | -57.35847 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c009fdeb-56be-320b-ab91-403943ca5cf7 | -16.50423 | -57.3625 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 420a31c7-0fa7-37f6-b05b-249cbf65c23c | -16.50074 | -57.36186 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5ea63986-2938-3af6-818c-c470e5c1189c | -16.48823 | -57.37202 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 529c2780-ef42-383c-ab78-a63e2ccb611b | -16.48474 | -57.37138 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| de8530db-48d5-3c2a-957e-696fdd6c72a4 | -16.48406 | -57.37541 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ed26244c-84a5-37c4-8e26-c5127bbac87e | -16.4827 | -57.38348 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e26b01c9-7774-38e0-a5a0-f248e0d766a5 | -16.48201 | -57.38751 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| aa7d8f09-7230-3025-98af-ca062406e011 | -16.4815 | -57.43324 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7e993f6b-a5ee-390b-a1f4-1af582eabad5 | -16.48125 | -57.37075 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 54465e0b-990c-3dfb-bd5f-d9456bc6c105 | -16.48057 | -57.37478 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4b4b607d-1713-369e-9222-4acea3f59c46 | -16.4792 | -57.38284 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| da57e8ff-40f9-3279-ab9a-e6e9236f5a57 | -16.47707 | -57.37413 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e9e671f3-9eaa-3264-837a-322a4ded4430 | -16.47639 | -57.37817 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7af01137-d5d3-3726-af3e-1bc52aac031e | -16.47571 | -57.38219 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fea2486c-d072-3c4e-8c6a-67bbfb69af6b | -16.47358 | -57.3735 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8ff988dd-81da-33d4-affa-fc8a0d6712d4 | -16.4729 | -57.37753 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 51f04a1c-9fff-302f-acb1-00c2918cf9b0 | -16.47222 | -57.38155 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7cd77df7-51a4-32f6-91a0-eec5fdfbec2a | -16.47009 | -57.37286 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4b63e168-ba1c-319a-a819-07d233949483 | -16.46941 | -57.37688 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d3f3e1b6-d7f3-3028-aaf8-8648641b87c6 | -16.4666 | -57.37222 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4d8cb1a4-962c-37cb-a803-779c8e3ed2a5 | -16.46591 | -57.37625 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9c6989d4-7b75-3cfb-a57d-d493ba517c95 | -16.45462 | -57.33681 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 07731e3e-25f6-388d-a8d4-24efde88fe46 | -16.45114 | -57.33618 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 2b894db2-3e89-38e0-a5fb-ccc80cbedd99 | -16.11967 | -57.53352 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 630730e0-8cc0-3063-b159-4d3d785c0101 | -16.11762 | -57.5242 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8c51e02-02ad-34a1-842e-e37880bd4270 | -16.11688 | -57.52855 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a1bf76b9-73cf-347a-8256-d8f914ff0331 | -16.11615 | -57.53286 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e356a96d-8e35-3d71-8f37-9b5c0e1d715a | -16.11336 | -57.52787 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f591d5eb-0c3b-38e1-b4f4-ce4df3c534f4 | -15.91421 | -57.43987 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ec2a7a28-c995-3e88-8300-f747452be5df | -15.83451 | -57.39666 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f039469c-0fb7-3cc8-90bd-40371e9031fe | -15.83379 | -57.40094 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 72df6f36-2ba6-3fb7-a601-48d5b50d254f | -15.83313 | -57.38338 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a78d98a8-2ecb-36b3-9702-cb70a483b5a5 | -15.83101 | -57.3959 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d14f1df-333f-34b7-a5d2-009d9987e445 | -15.8303 | -57.37868 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2983712-9804-3bb8-8110-929c0f67808b | -15.83027 | -57.4003 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ffdfd56-fe0a-3ee8-8729-796e27bfe6cf | -15.82963 | -57.38262 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c1c8988-0846-3ab6-add4-88c9054d1a27 | -15.82749 | -57.39529 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb445c42-2455-3b63-8e04-43ec8d5073ad | -15.8268 | -57.37796 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 141cb966-f3b7-3c17-9ffa-de5203b515ab | -15.82674 | -57.39973 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc91d08d-0b0f-31f8-b949-570fff81cd6f | -15.82612 | -57.38197 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 213f1d68-8c2e-386a-9653-f4fbbc4eba80 | -15.826 | -57.40412 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8910465b-0cc7-3257-be6b-61b0e0eb36e7 | -15.82329 | -57.37724 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17427e48-bb45-3658-bad1-26994e611634 | -15.8232 | -57.39922 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 43d4626a-5301-3343-a8dc-22cac7eb634d | -15.8226 | -57.38132 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc3e745c-bc1f-3b16-82bf-6e65dbfde2b9 | -15.82091 | -57.34862 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0b3cebb-e03d-3811-862f-929cba6534ca | -15.82046 | -57.37258 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c399b954-b378-3f99-8ae9-7d07f46e030b | -15.82039 | -57.39439 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2edbdc0b-2791-3539-8076-02f54a8a36c4 | -15.82025 | -57.35254 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c012c28f-588f-39c7-ab18-52e2fbfd9187 | -15.81978 | -57.37658 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a896689f-3e20-3502-bbcb-5d905a54f7b0 | -15.81966 | -57.3987 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 668f2116-4cb2-3dec-95ab-ec81889f12d8 | -15.81907 | -57.38078 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41c7130d-3216-37b4-ab9c-1dfb547ec731 | -15.81829 | -57.36404 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b80a23b-70f8-3cd7-b1cd-38987a809ee7 | -15.81763 | -57.3679 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c5f58503-923d-3574-ab48-f0b66bfc4590 | -15.81741 | -57.34792 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fea6adb1-5888-383d-92fc-6af829c47bdb | -15.81696 | -57.37188 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 20424f92-0ed7-38a0-9bc6-61ef4a8a411c | -15.81676 | -57.35179 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8733c779-6d3b-3b50-af62-94cfcf3ee336 | -15.8161 | -57.35563 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d3b271c-a791-32bc-8ee1-fc6fdad493bd | -15.81545 | -57.35944 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51e47e69-6b61-398f-9417-7b8ce189bb8c | -15.8148 | -57.36327 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c0fbfdde-afa1-363f-8020-4c45c6ef4820 | -15.81346 | -57.37112 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acf8177f-d9ba-30ae-922f-77b8ead5c97b | -15.81326 | -57.35104 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README59.md)
