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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f349de72-6413-3bc9-967f-3bf909c675a1 | -3.10578 | -54.16015 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| f0dba7aa-5e81-36ab-8e97-4ff7e7e1289c | -3.1054 | -54.15742 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 464571bb-99fc-3e54-a41f-7075b6468e6c | -3.10346 | -54.15026 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ccf76b8e-19f3-3ec1-9ed3-8ea47f0bda94 | -3.10273 | -54.15489 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 318cf7ca-fdbc-3b8d-812e-dc061df31050 | -3.10232 | -54.15216 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1481d06b-9c8b-32d3-8aed-f84bfcd587c1 | -3.102 | -54.15957 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 155fd489-ef97-32bf-a10b-7ad84fa9e0de | -3.10162 | -54.15683 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3ca14dba-ba26-3817-ab0b-5099bd020702 | -3.09967 | -54.14969 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 237aa542-7d29-3169-b9bf-c02c51525d12 | -3.09894 | -54.1543 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c1e09eed-9ae4-3874-b6eb-e1e696a395d0 | -3.09853 | -54.15158 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 747866f7-71e9-35c1-8b82-6f4014d169e2 | -3.09821 | -54.15899 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2783496f-5103-39fe-8234-05127932f083 | -3.09783 | -54.15623 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| aa6f126b-4a3e-3452-afe5-5134d418d441 | -3.09516 | -54.15374 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea30cc47-b329-34b5-85ea-82c8383f4c64 | -3.09443 | -54.1584 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16225f90-0b3d-3a31-92fb-5878e98e247c | -3.09064 | -54.15782 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70a94290-7971-3f57-ac04-94cd8b671496 | -3.05216 | -53.89973 | 2024-10-23 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c9ad792-4358-3578-8b9e-cac45bf24927 | -3.04832 | -53.89914 | 2024-10-23 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e46e81dc-2514-32ce-b204-3ec6a02de9d4 | -2.94964 | -53.70475 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 882820ae-302c-328d-9934-2819b7aede17 | -2.94892 | -53.70778 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 928633c5-f713-35f8-8d28-fc1807bcb19b | -2.94579 | -53.70235 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 170db56a-480f-32a2-8bd3-150e811c87d4 | -2.89422 | -54.25446 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59efeb7f-99b9-3e84-8cb5-85c2dd8ceb0d | -2.88496 | -54.11675 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4e772d1-a19e-315b-bf4e-ad1cc1bffc1b | -2.86791 | -54.47747 | 2024-10-23 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd262cb8-8aba-3e9d-af93-6f367eeb1f2e | -2.8396 | -53.9823 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c28d52b-74cf-367f-8483-5fe3e6f46440 | -2.8389 | -53.98696 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 812538a5-98f9-31c3-83e7-7f3305110972 | -2.8058 | -53.95554 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22d4d87f-0b91-3ddc-a7b6-87f14936684c | -2.80501 | -53.95276 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82b30de8-ea34-34c8-9377-0eca1f98cab2 | -2.77468 | -54.72514 | 2024-10-23 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad7e9d83-e82f-3432-a12c-9de1621efaa1 | -2.774 | -54.72946 | 2024-10-23 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5a43550-a12f-3d59-bd84-9f7308aa60ac | -2.7585 | -54.03398 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 430953f5-6f39-3893-b6e9-76fc7f1118fc | -2.7547 | -54.03339 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 576ee483-1c92-34ef-80dc-528695a404cd | -2.75399 | -54.03802 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0dcb1655-6a04-3111-ab9d-210367ebd597 | -2.7509 | -54.03281 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2262a3c3-a882-3f9e-b552-c4ab05eb5f6b | -2.73326 | -54.14716 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a07eba9e-bef4-3598-94c8-bf3f307a0628 | -2.65094 | -54.30907 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 352bab9e-59dd-3331-b210-70eb919b43a7 | -2.58091 | -54.01189 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e94ce5d3-c97e-3e6e-b508-9c55ccc2cf48 | -2.58019 | -54.01648 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 016918ef-dcae-3148-b928-1ad30a974f97 | -2.58006 | -54.01404 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 06a794d7-36af-3aef-a957-7b5c3b47d443 | -2.57639 | -54.01589 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23366e07-4a29-3aa6-8b0e-e354583ed9fb | -2.56881 | -54.01472 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9fd5fd7-55c4-3a5f-b9be-7b50e8ababb1 | -2.56502 | -54.01415 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bf401dd-1489-3813-8cd6-6f4a0adc4b96 | -2.5215 | -54.24368 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80e9574e-bbc8-3bab-8767-b37c28aecd3c | -2.51624 | -54.10399 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18465149-b7df-3972-99da-4734b03eae34 | -2.51553 | -54.10863 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 92a6a990-3240-3077-bea2-a2ff0866d533 | -2.51174 | -54.10813 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2997068b-5eb7-389a-95dc-2151dc9eab0b | -2.42516 | -53.89476 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 549170bb-f1fe-37b5-bff1-5d2aedcdcfe6 | -2.42136 | -53.89413 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c71eea84-5dfa-3ece-aa2f-7315f13d3adc | -2.33138 | -54.33274 | 2024-10-23 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f16c984c-2b6c-3eaf-8be4-f99903b162c2 | -2.33071 | -54.33713 | 2024-10-23 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b765e611-b9b2-3785-b4e3-05b4b70fad1b | -3.21922 | -54.85873 | 2024-10-23 05:14:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cb6299c9-1e12-359a-9d7e-d9a5e870634c | -3.11157 | -54.16795 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0be10da-8dc5-3079-aef0-6d340ae63ede | -3.10883 | -54.1654 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 1dd10074-6444-3f80-8b82-e91bb055fe67 | -3.10849 | -54.16269 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 6fd477fd-b13d-37b3-8784-ffa6d29cdefb | -3.1081 | -54.17005 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 9513ab1d-a1a9-344a-995a-b9c0438998fc | -3.10779 | -54.16736 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| be68fa06-8d46-3034-9ade-600c8772ec49 | -3.10709 | -54.17199 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0b3c60dd-9189-33e4-8efd-68c661314708 | -3.10505 | -54.16482 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 3c2112e0-ff4c-38e3-a545-a78c62165d06 | -3.1047 | -54.1621 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| ce72b972-9b31-35e8-bb75-9c2cd3844f3a | -3.10432 | -54.16948 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 8e424316-b06e-3328-9dc7-2f0c259941ad | -3.104 | -54.16677 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e5a2f2ea-2ff7-3662-ba21-0a29b7fdea01 | -3.10359 | -54.17408 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d7758402-724e-397e-87b1-38045acb3ee2 | -3.1033 | -54.17142 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 4673abfc-9c18-37d9-aa00-93a2ad2912d9 | -3.10288 | -54.17865 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d19abe7-9fc5-341a-85f1-eaea1daba8ea | -3.10261 | -54.17601 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41d9c4f0-542c-3a3f-83e5-349a321914d9 | -3.10193 | -54.18058 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67cc536f-b5cc-3c4a-a5c5-57cd5e7a960f | -3.10126 | -54.16424 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8339ecf3-f5ce-3490-a075-5e9d87448d1b | -3.10092 | -54.16152 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d628322c-cf7d-3661-955b-cdc76f7e27d2 | -3.10053 | -54.1689 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adc926cf-d612-34d2-8340-50df75231ae4 | -3.10022 | -54.16619 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb6d61c1-8048-36d0-b32e-b950df1693d9 | -3.09981 | -54.1735 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 527b7db6-781c-3986-b9ba-2aa54c57be36 | -3.09952 | -54.17084 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68f88b28-e622-3233-9722-276aa2438ccb | -3.09909 | -54.17809 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b18f9dc7-aca1-3996-a84f-7c6e8a32a521 | -3.09883 | -54.17545 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62652dcb-a043-35de-a588-0fbef1c0de20 | -3.09838 | -54.18264 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6fe5434-4eab-38a9-bd1a-0b48bbb398df | -3.09814 | -54.18003 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cab31cc-096d-3413-ad3d-ee38145d079f | -3.09748 | -54.16366 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 06d3a6e9-2e31-3175-9a13-7e1adae5a999 | -3.09713 | -54.16093 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 20b4ffe1-f149-3966-bdc1-e13817d63a1e | -3.09675 | -54.16831 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ce660bc-f04e-3cb5-a3b6-2ea8c6f82bd4 | -3.09643 | -54.1656 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b761c67c-df02-31b5-a56d-1605c0ce05af | -3.09603 | -54.17294 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91a6917d-7a19-364a-8068-20eb981b168c | -3.09573 | -54.17026 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e0f6067-8253-30b9-9eca-561506387930 | -3.09531 | -54.17752 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70c2844f-e4af-3484-9bea-790aa5f8d297 | -3.09505 | -54.17487 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 258b790f-4dc4-3fb0-8b23-bfff8da7309c | -3.0937 | -54.16306 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29adcab6-0466-369a-8b44-739e8e4d1e77 | -3.09297 | -54.16771 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63a1cd12-5354-3d37-99aa-cff4acce6ccc | -3.09225 | -54.17234 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ceebd01-11fc-3b55-a70b-ab4211317784 | -3.08992 | -54.16246 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a3f4571-d0da-30f7-b069-0fc7d2b3dd5a | -3.08541 | -54.1665 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2daeb092-3a24-30b6-b291-6aac2a9900eb | -3.08469 | -54.17114 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1068411f-05c9-3efa-860a-42b2a1eef7f4 | -3.08397 | -54.17575 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 233b9fcf-0c56-3513-98fe-fc041b962bf4 | -3.08091 | -54.17054 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26f57e68-53c9-3579-9c1c-ac85cd99aa60 | -3.08019 | -54.17516 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a490bb7-4506-356c-9e99-77c26e882d97 | -3.07641 | -54.17458 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fe0c843c-1453-323a-86a3-9e1d9ab8661c | -0.40023 | -55.64242 | 2024-10-23 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d85306d-c79b-31fa-a64b-8910c72c2c6e | -2.03396 | -55.68299 | 2024-10-23 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52b83501-1033-3382-9240-871af8d243c6 | -2.00618 | -55.70197 | 2024-10-23 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9716ef28-60df-3a04-9a58-6be3ad8b0b82 | -1.99963 | -56.51216 | 2024-10-23 05:14:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81d53c88-2f7c-3a7a-b7c7-bb571442be88 | -1.9957 | -56.5152 | 2024-10-23 05:14:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf1a4806-ef08-393c-8dc4-f70f94e3ad18 | -1.95159 | -56.23563 | 2024-10-23 05:14:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6308dfc5-6842-3d9b-bbb4-b622d9a74b06 | -1.91745 | -55.66977 | 2024-10-23 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README51.md)
