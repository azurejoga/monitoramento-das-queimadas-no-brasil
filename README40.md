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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50732e44-7807-304b-a6df-ad94aadb13d6 | -2.3164 | -46.65529 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ed6697c-5933-3dca-bcbd-c58e66d4c632 | -2.31577 | -46.65241 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d012e895-e914-3622-9398-13781bcbc783 | -2.31546 | -46.63837 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc8a6c76-45d2-3c74-aa3a-9c9886da3ff9 | -2.31538 | -46.63143 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8502e5a3-391f-32f9-b69e-f180d5e40535 | -2.31513 | -46.6565 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e612d03a-f0a0-301b-8ba1-0c33af748b2c | -2.31474 | -46.63549 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74780ab6-f832-3680-8125-c595265af13f | -2.3141 | -46.63957 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 455e179e-261b-32fa-a19c-bbeb97dd9f18 | -2.31281 | -46.65471 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4416579-699a-3393-afc3-10d80981cbde | -2.31218 | -46.65183 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c59361a5-4bdb-3218-b4b9-8cba2ed83551 | -2.31178 | -46.63087 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4032dc43-0c28-376d-b9fb-c0e107efa061 | -2.31115 | -46.63494 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cab02d0-a9ae-33f9-b6b7-9564a8c6e8cc | -2.30858 | -46.65125 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52bcab03-f3ef-30b2-9aee-83b71afbb019 | -2.30499 | -46.65068 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4eda914b-da5f-3ed5-9503-14194f094827 | -2.3014 | -46.65011 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cefcea8c-7a2b-3897-932e-2048ebf84976 | -2.29845 | -46.64545 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5218bda-10eb-316c-a95c-cbf1d2d41d46 | -2.29781 | -46.64953 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c80dfde-14d7-3acc-be7a-00cadb9cfe60 | -2.28523 | -46.75292 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f123e35-e8a8-3c56-a94b-2b2551bf48c0 | -2.28162 | -46.75235 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e085d6d8-6bff-38ff-a1f8-71e91daa5871 | -2.28126 | -46.73114 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0212abbe-fb57-3f9e-b024-157bc983b2fb | -2.26978 | -46.73355 | 2024-10-26 04:17:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e25ea915-123f-34ad-91be-221d4047236d | -2.19235 | -46.42258 | 2024-10-26 04:17:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04fca4e9-fa5f-37f0-80a3-435ca49c4ac7 | -2.19171 | -46.42657 | 2024-10-26 04:17:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9543dd99-59f6-3d3b-a527-1492927ae219 | -2.18943 | -46.41802 | 2024-10-26 04:17:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aab96ec8-3801-3e82-b73f-8ccd54a9d931 | -2.18879 | -46.42203 | 2024-10-26 04:17:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 685f319a-d403-31e8-a18e-cc0f23cfc82c | -2.158 | -46.94302 | 2024-10-26 04:17:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 883c179c-a6b2-3dfa-996e-0ffc0e08b321 | -3.54372 | -46.41087 | 2024-10-26 04:17:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0048a983-474f-3f37-83e2-caa51723eda2 | -3.54311 | -46.41156 | 2024-10-26 04:17:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a9f01d1-20d4-3a23-aa3e-dbeca0ef4130 | -3.33368 | -46.27624 | 2024-10-26 04:17:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 039f2501-719c-38c3-a960-b68b379196d4 | -3.30149 | -47.0245 | 2024-10-26 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db4974a9-c3e9-3c03-9ef1-6bab84623ae2 | -3.29787 | -47.02392 | 2024-10-26 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7564a77f-9cad-38ec-ada0-cbe53c66c1c9 | -3.19086 | -46.17974 | 2024-10-26 04:17:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1c500bd8-d3e7-39b2-b405-d83b33c10ed7 | -4.91612 | -47.72469 | 2024-10-26 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 976e3a5b-3aa8-3d02-a036-d77bd132da8e | -4.91541 | -47.72906 | 2024-10-26 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3f9a6e33-b05d-3bf2-955f-bbd192139269 | -4.369 | -47.48222 | 2024-10-26 04:17:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3feedc8b-a9ce-3dca-bc0e-550e55f4219f | -4.36534 | -47.48164 | 2024-10-26 04:17:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ce2841f-71d8-34f7-b447-83595bc40612 | -4.29756 | -46.76956 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce1661ea-729d-3cd6-97a7-2dc0ea25881e | -4.18416 | -46.62337 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef2cd57b-1d2f-3521-80f7-faefa31bf7e7 | -4.15025 | -46.83264 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c62088e5-b12f-3e90-9826-7bbf4ea4560b | -4.14669 | -46.83208 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72033247-81b8-32e3-ac15-7a04de705818 | -4.14313 | -46.83157 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a00e8dcb-91d5-3320-bdf2-e5ce854077b3 | -3.99097 | -46.47894 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46c5a3c7-0fc4-384d-a01d-0b126d94d3b8 | -3.96107 | -46.41434 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76461a7c-9ad0-30e7-9c97-29c5ea71970b | -3.9545 | -46.43314 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83a0a7f2-c6b6-3b27-a22b-fe7c45a15fd8 | -3.95101 | -46.43254 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cbda6aa-b866-3ea8-9623-d82aabc37142 | -3.94813 | -46.4281 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49c76257-2a12-3a75-abe2-db7b0f62cc8b | -3.94053 | -46.43079 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1bf9785a-1c8f-380e-8c97-f17112da51aa | -3.93703 | -46.43023 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 245af967-cff7-3872-9362-6a12edd57984 | -3.93334 | -46.16391 | 2024-10-26 04:17:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dfcf338-9835-3152-92a2-1386df038f33 | -3.92016 | -46.42365 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77d565e5-9d89-3f32-92b6-06ae7c1657b4 | -3.91665 | -46.42313 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27326b9d-bd4d-3984-b3ed-ea05ed145d6c | -3.88371 | -46.44945 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4461382-c183-3231-aa2f-d40a8927e7f0 | -3.88308 | -46.45332 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9dbde8d7-ffbe-3ea8-b9de-0f877d2ad78a | -3.87381 | -46.44403 | 2024-10-26 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 250ab512-2db9-384f-a83a-9a0403f78676 | -3.8108 | -46.9221 | 2024-10-26 04:17:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc149a4f-6b86-3fb0-acbe-aa66b6562fdb | -3.81015 | -46.92611 | 2024-10-26 04:17:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff9c8cdf-fe48-3740-9ef9-08a471e5a1e6 | -3.77454 | -47.54191 | 2024-10-26 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d21bb21d-d64b-30ef-bd99-df88d4d5c9ec | -3.60715 | -47.25834 | 2024-10-26 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 159f825f-dded-3650-9c76-3b705defce9b | -3.60648 | -47.2625 | 2024-10-26 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9da6978d-da92-313b-8f77-79fcf6c7181c | -3.6058 | -47.2668 | 2024-10-26 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac0ad082-26c9-32bf-af0a-8d9cbbc42e42 | -3.60543 | -47.52093 | 2024-10-26 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e62d20a5-842c-35b9-9fa0-a8facb97d31f | -3.6035 | -47.25773 | 2024-10-26 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47bbfff5-87d6-3f17-8f56-407a59544e20 | -3.60216 | -47.26617 | 2024-10-26 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b911c4c-23ea-364e-8054-835b3d34d57f | -3.60148 | -47.27045 | 2024-10-26 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9be78b75-f332-398c-b113-cd4a03670c4b | -3.59783 | -47.26981 | 2024-10-26 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a247ab3-fd0f-305b-b247-83072df0ef55 | -3.59485 | -47.26503 | 2024-10-26 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 147b3461-4236-3efc-8575-a7bc6ac5a7d5 | -3.54983 | -47.35836 | 2024-10-26 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ce4d23c-2c42-3a37-9601-d5bad65c6879 | -3.54616 | -47.35778 | 2024-10-26 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e279f66-5d65-3a53-afb7-a22a4ae4d408 | -3.54545 | -47.36218 | 2024-10-26 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7657ea3-98d3-3f78-8ad8-7e634abfe38c | -5.03014 | -46.70456 | 2024-10-26 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ac6f7d5-57dc-3c97-aba2-664ea920671a | -5.00948 | -46.89817 | 2024-10-26 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b015253-01c1-3723-9adf-e0082ddeb30b | -4.87533 | -46.88184 | 2024-10-26 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab1e04f7-7cee-36d4-b168-9bcb310ec6f9 | -4.87476 | -46.88117 | 2024-10-26 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7870ff04-e050-3c3e-9008-cac3854ea267 | -4.87179 | -46.88132 | 2024-10-26 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a24ff910-0933-3f60-a3a4-a9c693be96ac | -4.77627 | -46.50751 | 2024-10-26 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00ce4de1-3151-3906-82cf-7ba02f9a6dcf | -4.77278 | -46.50697 | 2024-10-26 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 566b80be-76bc-35ae-ae87-aa7a093a042a | -4.605 | -46.4703 | 2024-10-26 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b4a2b44-16b9-36fe-a945-19de7c46c891 | -4.58034 | -46.69548 | 2024-10-26 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40131d5c-df2f-3ebb-8a80-e9fd3ef481e2 | -4.57992 | -46.69635 | 2024-10-26 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58d1867a-e5aa-3a41-9d60-6e91a6e2ee03 | -4.54737 | -46.60698 | 2024-10-26 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c575185f-dcdb-3bd9-b646-b3878c9acda6 | -4.54457 | -46.46851 | 2024-10-26 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ef5242b-71aa-352c-892e-932010a53b13 | -4.54171 | -46.46407 | 2024-10-26 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcc96680-c6f5-3206-b223-001128c38d3f | -5.55889 | -47.02623 | 2024-10-26 04:17:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f88eb584-83d4-38e5-b600-e58e43b93eb8 | -5.55826 | -47.03017 | 2024-10-26 04:17:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c5c4f0f-fdd2-3c1e-90b3-45b0a89123c2 | -5.51491 | -47.20774 | 2024-10-26 04:17:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 685073fb-86bd-3c9c-996d-ba0e041b8dd7 | -5.46536 | -47.09362 | 2024-10-26 04:17:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dce2c100-9de3-3eb2-835d-91df2a468c06 | -5.44893 | -46.45247 | 2024-10-26 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d686af4b-ad93-39b4-ab95-5c382b8c4b83 | -5.41344 | -46.56289 | 2024-10-26 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7609bc04-d30a-3d29-8cf8-20d52def2e60 | -5.4124 | -47.15076 | 2024-10-26 04:17:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f64a205-c608-305b-a6b7-a12d0bf42433 | -5.39919 | -46.47514 | 2024-10-26 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6fdaa72-0e7a-3c96-9b4b-b7c308bfb513 | -2.10208 | -48.36951 | 2024-10-26 04:17:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfa04824-50d6-3d6f-8fac-163b7891ff8d | -2.05216 | -48.6819 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24277220-500d-356a-8385-535a735d13a9 | -2.01667 | -48.514 | 2024-10-26 04:17:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7542004e-b37e-3d07-9b29-e9e11f02fadd | -2.01662 | -48.51732 | 2024-10-26 04:17:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe439f04-13a9-3b7d-ba02-66738d8dc9a7 | -2.01612 | -48.51752 | 2024-10-26 04:17:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92979fcc-3d43-305a-aea3-a34a9695002e | -2.00643 | -48.5267 | 2024-10-26 04:17:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ab366ab-063f-3c46-baef-e4085269da87 | -2.00588 | -48.53019 | 2024-10-26 04:17:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 93e0364a-fbf4-37b3-b236-4d73acd0f23c | -1.98145 | -48.68564 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6655497f-b57c-3243-8559-975ee0a4e92a | -1.97739 | -48.68498 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7792795c-2808-3470-a71a-26541e272aa7 | -1.92354 | -47.96009 | 2024-10-26 04:17:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90252c5d-1737-374e-8bbd-059eb6c492c7 | -2.17124 | -48.8233 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README41.md)
