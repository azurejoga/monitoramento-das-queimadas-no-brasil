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

## Dados Diários - Página 175

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8288973-10b3-3ecf-87e9-4121b79a1d7c | -9.81271 | -56.41679 | 2024-10-09 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 649378fe-0f6e-38a6-9bb6-8b54c1cde0ed | -9.81216 | -56.42027 | 2024-10-09 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d16ca8d5-974d-3b43-926a-914ca4b82e57 | -9.58646 | -56.47324 | 2024-10-09 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5484eae-4a9e-3ab2-ae3a-8d1dfc76de64 | -9.58592 | -56.47672 | 2024-10-09 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ec79b80-486f-3849-8c41-5c9970218b2b | -9.58261 | -56.47619 | 2024-10-09 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 256fc1c8-eb76-3385-973a-456571bb2a33 | -9.49535 | -55.96983 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8160aa41-297d-3232-bae7-8cb85f1d48ee | -9.48837 | -56.07961 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cb33e878-a99d-3dd9-a5ad-933937685a6a | -9.963 | -55.3369 | 2024-10-09 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0cbb7ef-1304-3700-9f51-b3f4673507c0 | -9.95964 | -55.33638 | 2024-10-09 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 986ffa59-aa48-3f62-98cd-984b9b574f63 | -9.9591 | -55.33995 | 2024-10-09 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f4ff3be-18f5-32ab-bb95-737e1752c560 | -9.95629 | -55.33585 | 2024-10-09 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50f38160-113c-3cee-b3c5-21c990852b4c | -9.95575 | -55.33942 | 2024-10-09 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55e19072-2c56-3fe6-962d-fd2b8c904fdb | -9.95349 | -55.33173 | 2024-10-09 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ea02453-9fb6-3059-a79f-583596603d0c | -9.95294 | -55.33532 | 2024-10-09 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72f62e97-1a9b-33e0-b00f-25cce8e8a50c | -9.95069 | -55.32762 | 2024-10-09 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee43713a-3124-34a4-85b7-580bf5f0f454 | -9.95014 | -55.3312 | 2024-10-09 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eddf8ede-e4d1-3684-a44c-b234a9c8fb45 | -9.73222 | -55.62523 | 2024-10-09 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36a5dd26-eb67-330d-894a-396e13aa6436 | -10.8046 | -55.84732 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5c8c4f3-ef9a-3ee4-a81d-126bedccd8fd | -10.80073 | -55.85034 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13249278-f68e-3a26-a131-1f1949aa5cfa | -10.79407 | -55.84929 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d04b28a-6168-31be-9b35-9b6c17304a1b | -10.40203 | -55.26032 | 2024-10-09 05:04:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98a4c282-3ef5-3d90-a72d-0e890fa09d2b | -10.39585 | -55.25564 | 2024-10-09 05:04:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e8614ed-8144-330c-bfe0-b29e1b9a1ae4 | -10.36055 | -55.86481 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| eb36ffac-3d79-31e5-8b53-acf506645b67 | -10.35723 | -55.86428 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f6112efc-6a7a-37d8-9f1b-8c9c055347fd | -10.3539 | -55.86376 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e3580b57-245c-31b8-98dc-a85a5ba93600 | -10.12246 | -55.18457 | 2024-10-09 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fa2c18e-f3fa-3140-8712-a6f4ccb7a82c | -10.0916 | -55.18349 | 2024-10-09 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0df7081e-36da-3192-aa22-3c80a6a1d868 | -10.66896 | -56.34915 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4414d032-9764-3f8b-92fc-4d3e8dcac36e | -10.63444 | -55.89327 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5a782b27-e09f-3f78-a8d6-6e2a45f3f994 | -10.63389 | -55.8968 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 40e9d61b-93af-3ad4-bd69-9e5156134bae | -10.63226 | -55.90741 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9620f24-91ec-388f-95d0-daa121dbcdd2 | -10.63171 | -55.91095 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5bf8359-5761-3e9b-b962-9f233b2be35e | -10.63166 | -55.88921 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f6ea6708-f4c9-3f05-be9a-561b98b29328 | -10.63117 | -55.91449 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72a3591e-320b-3bf3-9395-5fde48b71160 | -10.63111 | -55.89275 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 817199c1-c6c2-33e4-aa89-ad756805ae82 | -10.63057 | -55.89627 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ec747eb5-4d28-31cd-9e76-0e7feb136dd8 | -10.63002 | -55.8998 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bfc052a8-aafe-3599-ad1e-2e19284f9774 | -10.62948 | -55.90334 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7a006559-bde8-3e73-8c10-041620c649db | -10.62893 | -55.90688 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c152903c-a946-3c54-b108-5409afd8a732 | -10.62887 | -55.88516 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e8d5ca9-b6d6-3668-912c-1f4db8e61e24 | -10.62839 | -55.91043 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06d8b8bf-ff43-3099-96d7-480a7b86fe10 | -10.62833 | -55.88869 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f9b69a2f-a6c8-33e3-8867-c867f8dff504 | -10.62784 | -55.91396 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3117fee0-3720-38e8-afef-ae23ce7e6622 | -10.62779 | -55.89222 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a787b201-87f3-3191-9e66-2723fa34cad8 | -10.6273 | -55.91751 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7e06468-0f99-3cc2-a984-46dcee1f9d3b | -10.62724 | -55.89574 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 665f5b3e-c6ce-3129-92a6-9daf2e8c87aa | -10.62675 | -55.92104 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 983f8fdd-af57-34b8-99cc-484329f7f8b0 | -10.6267 | -55.89928 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0f96fd37-4994-3ab0-aa83-b1b9431edb7e | -10.62621 | -55.92458 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 64470db8-d562-3f28-9c26-cd2b27a27c7e | -10.62615 | -55.90281 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ed06769c-50ae-3677-865f-95305720b437 | -10.62566 | -55.92811 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8789859a-5078-3efb-b660-3a70037b49a6 | -10.62561 | -55.90636 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 271679f8-b3a9-3219-a95c-16b9e20bc9ec | -10.62555 | -55.88463 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c83ad97-7c28-30b3-80a8-00b10be7d051 | -10.62506 | -55.90989 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d971c67-a91d-3dbb-9d74-e8d8d1968e2e | -10.625 | -55.88816 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3a436e9-4524-3f4a-ac3d-183910f89dec | -10.62452 | -55.91343 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d6ff49d-e36c-3a93-835b-b5b427128059 | -10.62446 | -55.89169 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5473c6d-b4fd-358a-8b58-bb2977742c77 | -10.62397 | -55.91697 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92d33505-3de6-3efe-aa93-ac04c2fcebf6 | -10.62392 | -55.89521 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea2e91dd-06a5-3837-89e2-9e7cdd62568c | -10.62343 | -55.92051 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1ca805b-4d54-39a4-83a0-a724696970aa | -10.62337 | -55.89875 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4da76d85-6ebd-3e1c-859c-8b7a2de5db95 | -10.62288 | -55.92405 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 75b3bd94-b042-302d-886f-436ec166e7af | -10.62283 | -55.90229 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7c4a9ef-30e9-3580-8082-3e41ed29cde3 | -10.62234 | -55.92759 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 04afa6ae-d610-3445-8963-9960749d7205 | -10.62228 | -55.90583 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2175a1d-7124-3269-8afa-88d0d8affab9 | -10.61956 | -55.92352 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 2dfe8ffb-9fb0-3ad3-9900-6495a1f4f1fb | -10.61901 | -55.92706 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| a58b17c9-d934-307b-87f1-7b8d56d6648a | -10.61678 | -55.91946 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| d4e8db2f-f482-3fae-a290-eee10eefed45 | -10.61623 | -55.923 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| a211466a-fa19-3496-aa2b-c76b0e677eb5 | -10.61569 | -55.92653 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 526da850-e745-335a-9597-c932ee32e723 | -10.56885 | -56.55538 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87d141ea-49a1-3e4a-ac74-e1ce4dbe1578 | -10.5683 | -56.55887 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66feb7ae-76cf-368d-9517-da341b9b016c | -10.56499 | -56.55834 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31aadf88-2635-3bc4-85f4-393fdb6f3bc0 | -10.14321 | -56.23702 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc62fc76-daab-34d7-abb8-fdfa18f7de70 | -12.09555 | -56.82544 | 2024-10-09 05:04:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b705b00c-297e-3b27-b5f3-c30c6f32efe9 | -11.89497 | -55.90816 | 2024-10-09 05:04:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b14f066-8e61-3275-8150-c49ad8373152 | -10.91113 | -55.79516 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8245f67-e6cb-3dfc-915a-146403b01fa6 | -10.90834 | -55.79109 | 2024-10-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e1b41b0-aabe-3b2b-bf36-7905d38df39e | -13.50083 | -56.65234 | 2024-10-09 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaefc976-492e-3e50-9a36-5b30f73d8fa1 | -12.80156 | -56.95755 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f9c762a-23bc-39f7-b8a7-93ba370ac5e6 | -12.79826 | -56.95702 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 462da6d5-fa4d-3d97-b9d0-8cdfec6e045a | -12.61579 | -56.51451 | 2024-10-09 05:04:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 025b9f9b-41a0-3352-b46b-5971b2aad578 | -12.61524 | -56.51806 | 2024-10-09 05:04:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0be74a8-b3a2-365d-b48d-e2329916a330 | -12.61247 | -56.51398 | 2024-10-09 05:04:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3c60c27-c242-35e1-831a-990661e86fbf | -12.61192 | -56.51753 | 2024-10-09 05:04:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02047516-9eb9-3fe1-835f-9d2b9ff37739 | -14.33957 | -57.58885 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f2a02a1d-4989-38e1-9199-ca4cc2249448 | -14.33901 | -57.5924 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc4fd643-e03d-3c66-ad85-ded0f5ef8508 | -14.31533 | -57.57029 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 223ea49a-6f27-3006-8214-67a7a4a55770 | -14.31477 | -57.57383 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72ea35f1-52e7-3e57-9125-f5d8693b65fc | -15.64497 | -57.38286 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7817b5fa-66ab-3639-abc2-bce7be9a8fe3 | -15.62675 | -57.36879 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d14364be-d909-3e1e-8cc5-c2cc0b6dba55 | -15.62012 | -57.36772 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13755e52-7d51-36c6-8456-ab245eba7f32 | -15.61349 | -57.36663 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acdacb5f-ee28-3d4d-9dcb-deea86d4a6d7 | -15.6063 | -57.3691 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7524987e-776b-3303-b806-2e1408bb074b | -15.60299 | -57.36854 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f92645d6-5670-31ee-a75d-69bf992f8586 | -15.60244 | -57.3721 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee8f6863-6494-39e0-a425-459b2a7b9f5e | -15.60023 | -57.36444 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c3241b3-22c7-35a4-a2b4-c1da92f65fd4 | -15.60021 | -57.43044 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd1d5208-3650-3346-8ce0-98186b8ef6e2 | -15.59913 | -57.37154 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec567026-4e6f-3b38-83a1-152b872ea829 | -15.59634 | -57.43347 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README176.md)
