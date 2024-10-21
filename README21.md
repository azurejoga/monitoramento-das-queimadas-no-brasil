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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c631fe0d-a562-35c7-9778-d2cfae2f5a1b | -4.9117 | -45.83603 | 2024-10-21 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 619acf4f-4f58-3a39-abce-9bb90d1104b6 | -4.91046 | -45.84331 | 2024-10-21 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45c8761c-c598-3034-8e66-8ff68864e2cf | -4.9062 | -45.83557 | 2024-10-21 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21613ec4-fd19-3aee-84c7-b07d66cffc89 | -4.90558 | -45.83922 | 2024-10-21 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4bb85fd-9d9f-3987-a460-4ebe71d0d82f | -4.90495 | -45.84295 | 2024-10-21 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2c6f374-6cde-3d3f-8620-2478223928d8 | -4.90433 | -45.84658 | 2024-10-21 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 13af725a-caff-3c85-990c-58472afccdf1 | -4.89663 | -45.82635 | 2024-10-21 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bf91e474-2e83-3092-aeee-1c94dbe0e1c3 | -4.89602 | -45.82991 | 2024-10-21 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91190c9e-f07f-3c20-bf3e-00654ea6b3fd | -4.89538 | -45.83368 | 2024-10-21 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df2e2d5d-14bf-3d38-b728-eda0f6a9f3bf | -4.88999 | -45.83258 | 2024-10-21 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7feda59-b0ac-383d-b3f3-c44b719da699 | -4.75068 | -45.78874 | 2024-10-21 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 044ec120-a86a-3abf-bb97-0d1fc70fa28e | -4.75007 | -45.79222 | 2024-10-21 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1e211e16-2431-34a4-8404-f4fb8d7274f3 | -4.74946 | -45.79572 | 2024-10-21 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5935df40-1e0f-3564-818f-3f4b9b1a7023 | -4.70261 | -45.83992 | 2024-10-21 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15d5003f-4faf-374e-9a04-821d17263329 | -4.70102 | -45.83968 | 2024-10-21 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae884547-ca91-35ee-9945-b3221bc614ba | -4.69572 | -45.64233 | 2024-10-21 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d246cac4-90eb-392b-ba31-a5fb113fc3c1 | -4.6904 | -45.64115 | 2024-10-21 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d2cb4e1-2256-379a-ac43-b0f17f2131c8 | -4.68943 | -44.5928 | 2024-10-21 03:47:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27845fc0-dab0-314e-9651-4a10ed3cc291 | -4.68442 | -44.59201 | 2024-10-21 03:47:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9fea810-7a01-3385-9a22-663743402775 | -4.67989 | -44.58837 | 2024-10-21 03:47:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01352af5-3c72-3a71-8c68-b7add4128300 | -4.66844 | -45.70436 | 2024-10-21 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aeee89d1-4361-3c20-86f7-18b40544d297 | -4.66785 | -45.70778 | 2024-10-21 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20d8558e-0a61-3c1e-a46d-e147cefcbb19 | -4.6279 | -46.07025 | 2024-10-21 03:47:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83f6bf74-4a09-345b-8fc8-455317da3bf9 | -4.62291 | -46.06619 | 2024-10-21 03:47:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 091cdded-4885-3468-8b94-f1267ff2a68b | -4.62236 | -46.06942 | 2024-10-21 03:47:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f2bfdff-9cd0-32b3-8554-aa6f87458c1c | -4.62178 | -46.07277 | 2024-10-21 03:47:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d491ea3d-6f5a-38fb-8a39-58e1da1475f0 | -4.4636 | -45.48135 | 2024-10-21 03:47:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37db22d6-3118-36d4-b423-a4b62280a811 | -4.46014 | -45.47994 | 2024-10-21 03:47:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cfe13f5-cc0e-3ffa-a760-491f569b28ee | -4.45955 | -45.48348 | 2024-10-21 03:47:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fde94cd8-eca1-33bc-bec7-40cbcd31a8ac | -4.45827 | -45.48047 | 2024-10-21 03:47:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc916fff-8f63-321b-ad7a-348cb988e0b3 | -4.44996 | -46.4458 | 2024-10-21 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a014e4c-1ab8-3741-a50b-99f65a19a297 | -4.44422 | -46.44518 | 2024-10-21 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0662c71-334d-3bec-917b-756c992b39a3 | -4.38424 | -45.84044 | 2024-10-21 03:47:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8377a15d-c2ed-3655-87ef-55e2fc1ae088 | -4.31532 | -45.81059 | 2024-10-21 03:47:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66f1db75-5b1c-38f5-bc04-efcecb726241 | -4.30984 | -45.8098 | 2024-10-21 03:47:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18e64c46-f8d8-301d-9b54-14f7914930c5 | -4.2175 | -48.55237 | 2024-10-21 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c000c200-047d-3c32-a3c1-53efc8e62d13 | -4.21687 | -48.55647 | 2024-10-21 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ba618933-5662-33d6-aedc-04ffe897efb2 | -4.21651 | -48.55786 | 2024-10-21 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd9a97ab-6cd2-3481-99ee-7d2344fa9164 | -4.14236 | -46.49308 | 2024-10-21 03:47:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 73f9f694-8140-371e-bee9-beb4f0d58815 | -4.14166 | -46.49722 | 2024-10-21 03:47:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f0f7837d-b838-3c64-a319-4cc2b5d86cad | -4.09967 | -46.14475 | 2024-10-21 03:47:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8e3f9a1-c8f0-3090-9ad8-1c2062a41c8e | -4.0676 | -46.65255 | 2024-10-21 03:47:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6661a6b1-4625-36b9-92ed-babe066bb34d | -3.91449 | -48.33519 | 2024-10-21 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 347252f2-ddf5-3a4e-bd59-9a9d3cf47ebe | -3.90802 | -48.33419 | 2024-10-21 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5f48ca8-dc5d-32f2-be90-ba8cc1832751 | -3.84891 | -48.98963 | 2024-10-21 03:47:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e3baab9-de46-31c6-984d-b583fdb125ff | -3.76838 | -44.40845 | 2024-10-21 03:47:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 040fb260-0374-306c-98de-e3262806a79b | -3.74427 | -44.39848 | 2024-10-21 03:47:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d77cebf-beb3-3ece-b582-4a1cdd6b3860 | -3.74379 | -44.4014 | 2024-10-21 03:47:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2a2b1ff-1db1-39a6-81c6-c0c0090799be | -3.63733 | -45.75914 | 2024-10-21 03:47:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 337fda53-2ba4-328c-b32f-d633167428d0 | -3.63183 | -45.75819 | 2024-10-21 03:47:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50cb1bc9-dac3-3907-9887-61a4724db9cd | -3.63123 | -45.76179 | 2024-10-21 03:47:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c1894ebc-cd19-378c-9bcf-c05f27bc6f6f | -3.61605 | -45.81883 | 2024-10-21 03:47:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7fce0f8-1c1e-3415-8aca-20a5c033f929 | -3.54699 | -46.40849 | 2024-10-21 03:47:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 871d0a93-20fc-37e7-8971-09627fa07eda | -3.46134 | -47.67237 | 2024-10-21 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d50cdfb9-b763-3b4f-8360-1134f3fcca04 | -2.97136 | -47.991 | 2024-10-21 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db47ec12-b972-3254-9aa0-5134f8ca8789 | -2.97043 | -47.99637 | 2024-10-21 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0838906-d64c-3d1f-95e9-da7dc7d04e55 | -2.96944 | -47.99379 | 2024-10-21 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 45590c7b-fed7-38c0-b485-bc84b7c97ca1 | -2.96495 | -47.98993 | 2024-10-21 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7cb796b-99ab-3fda-be18-2f0a8d762084 | -2.96402 | -47.99532 | 2024-10-21 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04c18c5a-fca1-3557-bcbf-0db9a5a6e9ca | -2.96303 | -47.9927 | 2024-10-21 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fee309f4-2e31-37a5-9ff1-85edd0598e0a | -2.90883 | -45.2054 | 2024-10-21 03:47:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0d3a8292-03d6-3897-8516-db53d40cb24c | -2.90825 | -45.20882 | 2024-10-21 03:47:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c462285f-fff8-35eb-b4f8-d18919a2183e | -2.90768 | -45.21224 | 2024-10-21 03:47:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a184c7da-9e7f-3e0f-aa1a-e885b42ad466 | -2.9071 | -45.21566 | 2024-10-21 03:47:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c1fbb1d4-42d1-3281-88b2-8c1acf086e65 | -2.90403 | -45.20115 | 2024-10-21 03:47:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc4aa058-d060-36fb-8ffc-91a58b870cf0 | -2.90346 | -45.20456 | 2024-10-21 03:47:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9f90a9d6-a4f6-3af9-8b8f-6aa2fcc9f533 | -2.90288 | -45.20796 | 2024-10-21 03:47:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 41010ad3-413c-3fcd-8b24-5ec37007818a | -2.90231 | -45.21136 | 2024-10-21 03:47:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7cce9813-28f6-3dec-b44f-113af9b0972c | -2.90173 | -45.21479 | 2024-10-21 03:47:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 30e3899d-3f08-32a4-ac19-d720c445a93d | -2.89866 | -45.20032 | 2024-10-21 03:47:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| deacb48f-ef0c-35ab-b4fb-44785fde8647 | -2.89808 | -45.20373 | 2024-10-21 03:47:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b47697c0-3a05-3f19-948a-c3eac3ae0f6d | -2.89751 | -45.20714 | 2024-10-21 03:47:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6438d440-329d-3d80-9a9e-2bf6d530cffc | -2.89693 | -45.21054 | 2024-10-21 03:47:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c67f8e1c-f345-3ad0-835f-4a0032807e7a | -2.85959 | -45.46452 | 2024-10-21 03:47:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f2c0afcd-e59d-3ca4-9f98-54551160ed11 | -2.85899 | -45.46809 | 2024-10-21 03:47:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9c46c18a-97df-35e2-a583-f79a5a479720 | -2.85839 | -45.47166 | 2024-10-21 03:47:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| df58b6d1-38d1-3e49-87f5-0d505141f1ea | -2.7878 | -49.29813 | 2024-10-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 20093684-c34d-38e6-83ca-ea1c9df63d24 | -2.78086 | -49.297 | 2024-10-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 47167b0a-f9ab-3a23-b460-1ed17b932a0c | -2.77973 | -49.30358 | 2024-10-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 61e408e2-931a-33b6-b146-a6bd2a6b8bf8 | -2.77861 | -49.31009 | 2024-10-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a324c40d-5582-3935-a8ae-2e8d4f227d15 | -2.77278 | -49.30247 | 2024-10-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 37cfeb69-0a45-3ed1-adea-6f142f0b5c9e | -2.77165 | -49.30906 | 2024-10-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 06caed98-4628-3ed1-b30d-33c16757193c | -2.52113 | -45.98578 | 2024-10-21 03:47:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07d91a10-7195-3b99-8612-1a7653fb53eb | -2.51912 | -45.99754 | 2024-10-21 03:47:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3673b6d6-772f-3fcd-a2fd-5f78428f00c4 | -2.519 | -45.98427 | 2024-10-21 03:47:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc774fc9-76e0-34ee-b1fe-1e466940dc09 | -2.48645 | -49.1101 | 2024-10-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c1bb895a-6267-3a75-ba47-bd32447a2716 | -2.48535 | -49.11656 | 2024-10-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8c38da8a-8c64-3586-b55f-31231945f9f2 | -2.47955 | -49.10901 | 2024-10-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| aa6d9027-1d4e-3a3e-b6f9-fad53cb59ac2 | -2.47845 | -49.11545 | 2024-10-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 71af86f5-5713-3ed9-9b4d-5e89dbe68854 | -2.27026 | -47.07926 | 2024-10-21 03:47:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34aa2883-9d43-3591-9c8f-73144227d5a7 | -2.07137 | -46.83905 | 2024-10-21 03:47:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 938d6baf-590d-35f9-bc28-e02de57832c8 | -2.0706 | -46.84356 | 2024-10-21 03:47:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2903b53-218a-3739-851c-bf2cc8528668 | -2.07 | -46.8378 | 2024-10-21 03:47:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91e577c2-87b2-351c-a26e-026e584f15b8 | -2.06926 | -46.84232 | 2024-10-21 03:47:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9a12194-de60-3589-abda-07c044847b17 | -2.06032 | -46.8974 | 2024-10-21 03:47:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 166e2602-0ac8-35fc-8772-7cf2ecd61fcc | -2.05957 | -46.902 | 2024-10-21 03:47:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c5ff7bd-88c6-3dc1-b4af-c9f574d37d0d | -2.05521 | -46.89748 | 2024-10-21 03:47:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 56504e9e-17ea-3fe1-a1a1-60f8c827a3dc | -2.05424 | -46.89643 | 2024-10-21 03:47:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 114d7646-dfb4-3622-830d-01613580a62f | -9.93489 | -37.32648 | 2024-10-21 03:49:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 789f37f4-4b64-33e6-bd5a-ed2c479ea6a5 | -9.93435 | -37.32996 | 2024-10-21 03:49:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README22.md)
