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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edd1221e-2241-3875-bc67-16f99e2095f3 | -4.07163 | -54.43825 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 550ee26d-36ee-3f8d-8930-96402e9d9675 | -4.046 | -53.91044 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d555cd9-e06c-31d5-be66-542e063b2cd7 | -4.03468 | -54.2832 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3ac6a82-6915-32d9-ad9a-2c8065502d35 | -4.01768 | -54.82142 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0705132-6e45-3647-b353-67ec15fe1680 | -4.01711 | -54.82499 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3ad7ffd-2cac-3d34-b13c-bdee6573af4e | -4.01434 | -54.8209 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c17a3a26-5792-3c1f-a6c7-a111c9369023 | -4.00513 | -54.44921 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5caaac59-0012-3401-b562-78f64a3d0643 | -3.98014 | -54.34921 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e539c1aa-7eec-3b43-bd75-702c5bd519ab | -2.03423 | -56.06343 | 2024-10-28 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89417073-ba12-39c2-a6f5-96fd215412ec | -2.00948 | -56.3735 | 2024-10-28 04:57:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 462b3e8e-6219-3470-880e-00a632f16044 | -2.00613 | -56.39433 | 2024-10-28 04:57:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e67ad739-19fc-39a7-881b-b17f3eb31fb9 | -1.97387 | -55.89453 | 2024-10-28 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62d9135c-25eb-31bc-ac07-1f07f7e1f28c | -1.96471 | -56.01967 | 2024-10-28 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40809dac-f872-3cd9-907b-d4b929975db5 | -1.93209 | -55.63238 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a032f3fe-4096-3c76-a822-c967fc29cd93 | -1.3203 | -55.82952 | 2024-10-28 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6aada26e-236f-380c-9807-a4917197046c | -1.31675 | -55.829 | 2024-10-28 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6d0f6d4-2dd1-3cf2-ac88-ea01399065c4 | -1.30107 | -55.72156 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebdf5add-c722-36a4-8565-280525ca56a3 | -1.30045 | -55.72552 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd8fe80f-14b5-3a7c-82e0-3058a6d33855 | -1.29754 | -55.72101 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 669866c0-bcab-3972-ae39-7dcc084d517a | -1.29692 | -55.72496 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fdf5016-c6b8-3d31-b3b9-517970cf0390 | -1.29464 | -55.71649 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2efc7ba0-5a82-3568-9f06-afb230ee1bf5 | -1.29402 | -55.72045 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c0113ceb-b406-3f42-b386-d25521cde673 | -1.2934 | -55.72441 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20ebd7c7-48a0-3ed6-a728-3c4b70c0f182 | -1.28468 | -55.77992 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d974800-1bcd-3d42-90f0-44f473b65218 | -1.28114 | -55.77935 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b4a3f62-9621-356a-ac27-4ebb8b876ffa | -1.26004 | -55.70699 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f6fd15e-0b73-3125-8a43-e27a7d6ef979 | -1.25941 | -55.71094 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f4ce919-a123-35e1-b203-06dda9f33152 | -1.23382 | -55.89491 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfa89952-0e84-3c32-970a-d44a194094a0 | -1.22335 | -55.77824 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13c1892b-72c5-3546-b59e-28a669920635 | -1.21569 | -55.87151 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35069f4d-3c86-36f0-a7b6-2890704e39ab | -1.19957 | -55.9267 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05fe43ce-21a4-302f-958e-588f2b1fdcdc | -1.19893 | -55.93071 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c28071d-8eb3-3d6e-b7e8-317a2183d2e8 | -1.76172 | -55.09106 | 2024-10-28 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 721dc2c9-f5f4-35f7-9be3-ae56363b2fd0 | -1.74809 | -55.26447 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65fe3c4b-24c8-33a2-9b23-c5778ea267ae | -1.74465 | -55.26392 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb888321-a869-3130-8897-3a7eb5f98657 | -1.73429 | -54.99632 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fd7e7a9-d06c-3bdd-923f-c7038bb3a7fa | -1.73371 | -54.99999 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e27bc11a-1717-3d59-b906-e3f76ca38c70 | -1.73207 | -55.25436 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f089de5-a25c-3994-b440-faeec66a18f3 | -1.7303 | -54.99947 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 867fccef-b463-3b7e-9499-22c4985919b3 | -1.72966 | -55.26936 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d44a5a76-cf1d-3a68-8b6c-702a34fe6a72 | -1.72914 | -55.00682 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 134de791-76de-3536-934d-4fdb13e975a1 | -1.72232 | -55.00574 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c19f2a52-33b1-3457-b5c7-31d2fd04d32c | -1.72174 | -55.00943 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b51ac91-e50c-347c-9a30-f2db43809871 | -1.71891 | -55.00521 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c647da3-4dea-3e0b-a30e-c68416f16141 | -1.69298 | -55.08067 | 2024-10-28 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86660d9e-130e-3a25-a15e-426cbee0d6fb | -1.6917 | -55.11086 | 2024-10-28 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9752712a-5f20-30da-94ba-b3db43e6937f | -1.68955 | -55.08015 | 2024-10-28 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15abe56f-a21a-304b-8e79-73183ad4b942 | -1.6816 | -55.30864 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87c81eb8-a92e-369c-b36c-dd915fe85ada | -1.67858 | -55.10507 | 2024-10-28 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7acc229-9ce3-3328-a637-281d034cc3fd | -1.61849 | -55.50556 | 2024-10-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6449d8ba-eb01-342d-a069-830ae14b37be | -1.60457 | -55.70625 | 2024-10-28 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 72e3e8a6-18ab-3e00-9e76-5ba7170f5b14 | -1.5634 | -55.82916 | 2024-10-28 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1d09fbf-bedd-3934-a8e3-629e1ff13bbe | -1.49681 | -55.09988 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8327cdad-9ec4-3f00-bae4-39e823d6a623 | -1.45959 | -55.11307 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e727bd3-a162-3944-8156-b9e353930a02 | -1.45615 | -55.11258 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e9b7c48-7dd1-36cd-aac5-12cf3351a6f0 | -1.44815 | -55.20732 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cfa735c-df82-30a7-85bd-5e2705cae417 | -1.43581 | -55.06381 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 36a26bcf-80bb-30f7-b228-52198e8de12c | -1.42177 | -55.28432 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 694a65ba-0b1e-3a1c-82f6-937d40e1fab9 | -1.42053 | -55.86101 | 2024-10-28 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4e2c302-a293-3881-a200-7d81eddeb5e5 | -1.41989 | -55.86501 | 2024-10-28 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bbb8abc-f533-3d1b-b3fe-86b78d75c610 | -1.37738 | -55.85875 | 2024-10-28 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 377141dd-28aa-325d-879e-7a00954f1fda | -1.37675 | -55.86275 | 2024-10-28 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74359d4d-31a5-394c-bfd1-2ca21a93df90 | -1.37383 | -55.85822 | 2024-10-28 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a9fc1e1-251a-3fcf-af66-0717fc96f313 | -1.37375 | -55.39418 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 329cc744-6b75-32cd-8ed7-09c4df1c4fad | -1.3732 | -55.86222 | 2024-10-28 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb28617b-453a-3c89-b5b9-521fb7b1afb5 | -1.37315 | -55.39802 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55efbff3-d678-3c4c-b244-587ab72c1aa0 | -1.34164 | -55.8779 | 2024-10-28 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce1bdd85-7c70-3dd5-8578-e25be8dd0062 | -2.36431 | -56.52019 | 2024-10-28 04:57:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30ddb015-e559-3442-a07d-f8aef7825217 | -2.28022 | -56.43476 | 2024-10-28 04:57:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3ac89dd-9744-3633-8e9a-a4c395ca0c07 | -3.63103 | -55.50533 | 2024-10-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e33ea4bd-f13b-32ac-bde6-f93d31439964 | -3.57441 | -55.61866 | 2024-10-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9973380e-814a-37cb-82d0-4293fbb87428 | -3.56647 | -55.51437 | 2024-10-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7db4b90a-af6f-3682-b6c8-cd963e9dffe1 | -3.55814 | -55.47887 | 2024-10-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10df6b98-8ee2-37d9-b837-f8e470fc7f8f | -3.54031 | -55.50256 | 2024-10-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa2b1ab7-e917-317f-96d8-4d831210b25f | -3.54015 | -55.5029 | 2024-10-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2b150cd-4081-3e62-80b8-cc87aa63a8ea | -4.21839 | -55.50242 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 61189751-2984-334e-a09e-aa1e35a09493 | -4.21498 | -55.50191 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ff1935d4-4c31-317e-a3d6-65d3d08c8604 | -4.08781 | -55.87994 | 2024-10-28 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b346203-36ea-3dc5-b23f-1b3bdce45482 | -4.07151 | -55.82699 | 2024-10-28 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fb9ea68-1f8d-3587-bbc6-f717ed907e4a | -4.06286 | -55.57259 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9ddbbcf-3eb8-3dc2-93bf-324b42d167be | -3.99021 | -55.43647 | 2024-10-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0884800-4dd1-3cdd-9723-635f012bb9c8 | -3.77432 | -55.97623 | 2024-10-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2cc9eb9-52bd-3d9c-ba81-db1c2d1a7e4b | -3.72993 | -55.658 | 2024-10-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f550cd7-ef47-3f4e-b9c9-8278a74fe2fd | -3.72616 | -55.48198 | 2024-10-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f07f62b7-4156-3b69-b7e0-414af7059b66 | -3.72557 | -55.48567 | 2024-10-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6db284d7-9869-3a4d-89e3-b4f51373d2c6 | -4.72761 | -55.76694 | 2024-10-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0da68994-376c-3f16-8852-5681846b0747 | -4.71562 | -55.68913 | 2024-10-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d62dd4d6-0c50-307c-97fe-f2c62cb361c3 | -4.71221 | -55.68861 | 2024-10-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe91bb27-0d78-3513-9cdc-35208d405930 | -4.71161 | -55.6923 | 2024-10-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c248dd7-e8c4-39f8-b2fd-c1047d10d79b | -4.71101 | -55.69599 | 2024-10-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e3b0d8b-9e7e-3100-8eba-f150354f482d | -4.60803 | -56.12007 | 2024-10-28 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0aa5743-7afe-39ed-92d3-10d305142d61 | -4.58209 | -56.10424 | 2024-10-28 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b11d2f8-aee8-3e87-bb7e-051b1dd49848 | -4.57951 | -56.00992 | 2024-10-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9cc1b98-88e7-3bc6-84dd-a5d002488ac9 | -4.57605 | -56.00939 | 2024-10-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bb98609-530c-32eb-82d0-f94993fb22b0 | -4.39098 | -56.32515 | 2024-10-28 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d10fba35-967f-3368-ad55-a5eed13b6a8b | -4.38989 | -56.32579 | 2024-10-28 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8da7f777-8ce0-333d-86bf-1e8ba66e83ee | -3.9519 | -55.76142 | 2024-10-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05f7ccc9-e0b4-3314-9509-ebcd2e5aa059 | -3.90169 | -55.88184 | 2024-10-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40df8d1c-aa57-3837-93d7-291cdf4e952e | -3.86116 | -55.67076 | 2024-10-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8698ff8-4dfa-3ce4-8ef4-830dd341ae79 | -3.79698 | -55.8778 | 2024-10-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README70.md)
