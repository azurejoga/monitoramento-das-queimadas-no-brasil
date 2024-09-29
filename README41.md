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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0953833c-1656-3c15-a5ed-0866fb149301 | -6.26188 | -43.77053 | 2024-09-29 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c07dd709-61d8-3b53-a5d8-a54a20402d54 | -6.25721 | -43.76614 | 2024-09-29 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 438865fd-1bcf-3d2d-b405-89658b75e2ac | -6.1588 | -43.51243 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d4bfff7e-8f9c-3727-989a-fc3995ac07f1 | -6.15854 | -43.51349 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 076b42df-6eb5-3698-ac04-6650d94bef1e | -6.15833 | -43.51562 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f9c3daa7-dfb5-3b1e-b762-14295c14a89b | -6.1581 | -43.51669 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5e4fef4e-53b1-3b05-a7db-ff924fbb179d | -6.15329 | -43.51264 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d820a0e4-11a8-3510-bb18-25a769a14b2b | -6.15308 | -43.5148 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0adddbd-c382-3213-a8d0-f45fb4e3cdbd | -5.9466 | -43.87645 | 2024-09-29 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e1ac50c-1503-30ac-992f-736a25636173 | -5.94617 | -43.87946 | 2024-09-29 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9bfdb39-5f9f-3593-8e72-08257ee70bc1 | -6.17311 | -44.29576 | 2024-09-29 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7b07661-2334-36d6-9198-58fc3051edc2 | -6.16808 | -44.29532 | 2024-09-29 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7fde1e7-599e-321e-a230-38556d016188 | -7.86143 | -44.60348 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b21fa9c-ebd9-325f-9dbd-4cf636149adb | -7.85682 | -44.59982 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 164482f6-2798-3a6f-a406-2dbf1f6ea543 | -7.84376 | -44.58314 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed440b3f-552d-3b3e-b988-e85c018efa3c | -7.83875 | -44.58242 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e424646d-3eb6-3325-9b8c-343530189196 | -7.83836 | -44.58532 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3c192f11-e3b4-3b60-bdad-d3e0d7e17118 | -7.83797 | -44.58822 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 28ab6a35-e518-3f49-ab39-b26ec189c15d | -7.83758 | -44.59115 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 82f18460-734b-3ec5-89ab-1d8c9f45b26e | -7.83413 | -44.58059 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c09de4e9-3bdb-3541-9cee-63e71c10823c | -7.83375 | -44.58159 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3dc5a449-44f5-3bd8-8752-cd21ba4a8be3 | -7.83373 | -44.58346 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 77d8f144-29bb-3ffd-a7e9-6bd1e1fdf0f3 | -7.83337 | -44.58446 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 45d62708-0f49-357e-aeb9-e03b1ae296ce | -7.83332 | -44.58632 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c82b7c15-d6fd-34da-a748-4dc6077865b7 | -7.83298 | -44.58735 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 156f9ee4-2624-31e2-abdd-f9b7afb8594e | -7.83291 | -44.58925 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90e0e34d-9d36-3930-9fcc-4d3b0f8a41fa | -7.83258 | -44.59032 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9ab054cd-41c6-343d-8db8-abe49201a7d6 | -7.82915 | -44.57972 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1c5edecc-6c6b-3204-a3c8-468cd99c3ee4 | -7.82914 | -44.57785 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d9d2a925-fcd7-3760-abfa-65d54b5ecb57 | -7.82876 | -44.58069 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0c2deccd-0551-38b1-8022-45a5d906ee3b | -7.82874 | -44.58257 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e5906181-bca8-38e4-8aae-56e55416eda2 | -7.82838 | -44.58356 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e465238c-68cb-380e-a619-2b8e9ed097bc | -7.38571 | -44.08829 | 2024-09-29 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b2534b8-e15b-359c-af2f-e1f801c8990b | -7.38527 | -44.09152 | 2024-09-29 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e68e147-d1a5-303e-92a4-a67d27a5e135 | -7.38055 | -44.08764 | 2024-09-29 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f97257bb-accf-314a-9cf2-bf2e58d951c9 | -7.08111 | -44.15577 | 2024-09-29 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0960d2a-4650-376c-af03-b3e8aa6a31fc | -7.07603 | -44.15491 | 2024-09-29 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbb66e8a-0f0a-357f-9364-ba9fc97a0348 | -6.58291 | -44.182 | 2024-09-29 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce8d4f32-f6a2-35d4-9c8f-c11b2f41083b | -6.5825 | -44.18487 | 2024-09-29 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83468cc3-d150-3010-8de8-c12dd998a397 | -6.57864 | -44.17579 | 2024-09-29 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0c1a9a3-8b1e-3c6f-a7ea-8d5fc9cf97c7 | -6.57821 | -44.17874 | 2024-09-29 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad5622f2-1cb9-310b-baae-9e531be628c5 | -6.57781 | -44.18157 | 2024-09-29 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f7eb839-0201-30f0-a9ef-e2406645b62d | -6.57355 | -44.17524 | 2024-09-29 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4b3f6b0e-2ecc-3bc7-b9ac-d40c49abe1d7 | -6.57313 | -44.1782 | 2024-09-29 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60a54b13-834c-3373-b62a-b50aa94f3cde | -7.59175 | -45.07735 | 2024-09-29 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11ace5c3-a781-3500-a005-9ff9f1720e6a | -7.58839 | -45.06606 | 2024-09-29 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1ca75b8-531a-3a4d-a65b-1c02fed187a7 | -7.58764 | -45.07148 | 2024-09-29 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd049ace-c8a4-37c7-8ca0-210bbe82a11f | -7.58278 | -45.071 | 2024-09-29 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5162b37a-26a9-3ced-b5c5-211b9318fe5b | -7.56507 | -44.71473 | 2024-09-29 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe698f2e-7179-3c30-9f67-27852143b974 | -7.29934 | -44.97149 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8532d8c4-1b0a-359a-9238-16d382764625 | -7.29858 | -44.97692 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a5d16572-8520-33e4-965c-96563f3d7fea | -7.2945 | -44.97082 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 44992846-bba2-32fd-8b16-c57681a37437 | -8.76366 | -45.17645 | 2024-09-29 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4979a8cd-297c-3b5d-bb20-c7bb3877a29c | -7.29374 | -44.97622 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4e93ab03-81b0-3f99-9f13-c7d67de47dd5 | -7.28968 | -44.96997 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a37c0298-91e8-3664-bb86-6ef4c90f036f | -7.28892 | -44.97539 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d8ce230e-b858-3ce1-97c6-02c8f9c59fec | -7.27487 | -44.93423 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a93b4415-1048-3f6a-8bf7-14d7ffccbbe0 | -7.26516 | -44.93291 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f1829e84-e7ca-38b3-af83-24701ab7c605 | -7.25686 | -45.02887 | 2024-09-29 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a580e5b-07a5-347b-a0a9-2a232ab9424d | -7.25421 | -45.01239 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25a0c92d-2927-3dc5-94bb-47ba391e5f61 | -7.25277 | -45.0229 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 441c32fd-1ee3-39b8-98bc-fce2b24e12f0 | -7.25204 | -45.02816 | 2024-09-29 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 342c4c80-dd93-3502-b641-6a9bd1762a7a | -7.2506 | -44.94019 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 189f5715-5ca2-301f-a029-e9218d6a656d | -7.24977 | -44.93692 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4fc118ab-a8db-32ee-8848-6d16966ba000 | -7.24938 | -45.01173 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36bdbe37-c44d-3ed6-a146-d501c7c9b14d | -7.24906 | -44.94216 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 904e90dd-9445-3fc0-a2d1-da788c07f226 | -7.24866 | -45.01698 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51e99598-8af5-3958-83aa-435b504b1d0e | -7.24794 | -45.02222 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 583b15e9-7751-33b9-bfac-e4f7cb179fa1 | -7.24572 | -44.93975 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bc96e91b-081e-3138-9acf-52a8eb926cbd | -7.24498 | -44.94485 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4923a1f4-543d-3d43-9214-53cd25569961 | -7.24482 | -45.01419 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93513b80-325c-3878-8ec2-05c3bbb8e964 | -7.24418 | -44.94164 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 26ef62a5-0609-35b7-830f-ecdd2705b9c4 | -7.24406 | -45.01944 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6546c59b-5a5e-3e9e-9183-58822d387258 | -7.24383 | -45.01639 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 915dfa50-bdde-35bd-b80b-6c279d7bd1c2 | -7.2268 | -44.96054 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aeb744a6-1860-3757-af5e-1cca1c85dc8a | -6.91182 | -45.05222 | 2024-09-29 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c9e95a2-0ed2-379d-8a62-6c9ce848f89d | -6.61414 | -44.67614 | 2024-09-29 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7bb6c7d9-6f43-3c34-9b7b-e930175570ba | -6.52776 | -44.61506 | 2024-09-29 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e240da0-01af-367f-abb8-c4cc2b3afbf9 | -8.79556 | -45.12532 | 2024-09-29 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f033eb8-d238-3c70-9f52-694f373f34e2 | -8.76587 | -45.16017 | 2024-09-29 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a291e4b1-215d-3213-a3f7-4c59841660f0 | -8.75952 | -45.17032 | 2024-09-29 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| deec5a95-bc31-361a-9b86-0dd8be70301b | -8.75878 | -45.17574 | 2024-09-29 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1fc3e6f2-1a12-357f-b6fb-d3f069c24976 | -8.75805 | -45.18116 | 2024-09-29 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 60bb6da9-85e4-3963-bc96-56d8eac35ec2 | -8.71659 | -44.80722 | 2024-09-29 04:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b52b773f-09bf-333c-b79f-9c2b76226950 | -8.50995 | -44.71307 | 2024-09-29 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 808b5136-fbcb-377f-b2b3-b5cae3cd8d46 | -8.50956 | -44.71595 | 2024-09-29 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| faf3a9c7-ae4e-3756-88b5-e05982531378 | -8.50917 | -44.71883 | 2024-09-29 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 41.1 |
| c3c6a70a-8f53-3965-b99b-c7faa90b8db5 | -8.50878 | -44.72171 | 2024-09-29 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 6fe0fc2a-4fee-3ab0-ba26-27e80d7adc5e | -8.50839 | -44.72458 | 2024-09-29 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 18cbe382-b999-3f7e-a3e6-904083383642 | -8.50416 | -44.71812 | 2024-09-29 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 53bc5c36-d798-36eb-a4d5-a6f365e49f35 | -8.50377 | -44.72099 | 2024-09-29 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d433210-ed3e-35b3-8590-6b9ed506d96b | -8.30639 | -45.34544 | 2024-09-29 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4825f439-c03c-317d-bd98-a9f7d790dae4 | -8.30227 | -45.33987 | 2024-09-29 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83f34431-1b9c-3c7e-8e8e-b4d05e8331c7 | -10.66165 | -44.50217 | 2024-09-29 04:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2b1c1a8d-622a-3cb8-8316-beaca370f565 | -10.66123 | -44.50543 | 2024-09-29 04:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0308f9bd-a101-3c36-978a-099c3e3ca76a | -10.6564 | -44.50148 | 2024-09-29 04:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d533db83-6dc3-3233-a2ad-278b43201045 | -10.65598 | -44.50474 | 2024-09-29 04:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bd32b55e-9065-3084-b34d-84180914bfb3 | -10.15533 | -44.91288 | 2024-09-29 04:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a08913a8-bdd7-3ecd-ab58-640f8e472e89 | -10.15494 | -44.91589 | 2024-09-29 04:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b07047e6-7d0e-355f-8597-ecfa1b5c6867 | -10.14989 | -44.91507 | 2024-09-29 04:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README42.md)
