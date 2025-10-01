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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e9336dd-1fff-3ba7-8729-ac3d60f3b39f | -11.62699 | -47.49253 | 2025-10-01 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6ceeae1b-ec92-3a61-9900-757c24038744 | -13.37624 | -47.31335 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f590f99-9eda-38bc-aae1-6fca57d5990d | -14.057 | -45.03478 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7774551f-7179-3a49-a504-9a4098371828 | -14.18535 | -46.12073 | 2025-10-01 03:30:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 16948d1f-1ca8-3c52-9316-2f1e91447885 | -9.93846 | -43.6051 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70436e6c-24d6-3719-a956-bdf989a4274d | -13.52881 | -47.26742 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9816b14d-843c-3b99-987e-1ac3a591fc82 | -11.63991 | -47.50231 | 2025-10-01 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5f6e594-0135-3ea9-b4ff-6c567d935d9f | -10.83754 | -46.66315 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 17dfe838-dbaf-3ca8-bdf5-d2ed369f7a24 | -14.17238 | -46.11913 | 2025-10-01 03:30:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 83544390-d026-3e3d-a407-6a747e511cd7 | -11.82916 | -44.97351 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f55e85e7-fdda-384f-9b3f-fee14d584f2c | -11.51937 | -43.55027 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4a4ebe9-b568-3cf3-8e0b-7a59d62d05a7 | -12.86765 | -46.77431 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87233692-41a5-3a45-8a0e-07ffd50ceeb2 | -11.43232 | -43.50288 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20af2cb1-273a-30f8-a66c-edc71560781f | -12.78391 | -46.86697 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9fce2bc-8d2e-3e88-9192-474a71fdd74b | -13.12678 | -47.43295 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4640c821-0b83-3dce-84e8-d2256a59d00a | -13.46166 | -44.38056 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b586f44e-7fff-37f6-85cf-5af363b54764 | -11.50199 | -43.51748 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea8da5ad-c1df-3794-9ae3-1f30b07f12de | -12.18767 | -40.40801 | 2025-10-01 03:30:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 04b3139d-2839-38c9-baa6-86d435a781d9 | -13.29721 | -47.24433 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 891ce3d0-6127-3dbf-b4dc-d9cd67d52eb3 | -11.66518 | -47.49988 | 2025-10-01 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 624b40d7-b507-3a00-a7d2-591961ada87c | -10.90507 | -46.51028 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e9ff5fd-a4bd-387f-b2f3-a18d403390c1 | -13.33016 | -47.8387 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 38f6087f-21b7-3ffa-8a55-b6fdcdc92234 | -8.89883 | -45.05156 | 2025-10-01 03:30:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ce7ce996-b06c-3f56-a8ff-58705391fbac | -11.46554 | -45.09376 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 9925467f-f42a-365e-aa5f-26868e407762 | -9.94101 | -43.65533 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 675be332-420d-3428-9c39-fb7fb5b5c3d1 | -11.46675 | -44.98839 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b8b1a251-1272-312d-a25b-abbbc3a74e8a | -11.50957 | -43.53959 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8c6089ed-972f-31ac-8e7b-7954e544d719 | -11.45592 | -45.02673 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e017801-e59f-3e4b-aa35-77e75212df57 | -11.8139 | -44.92979 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb0f266f-c6a5-3a7d-ba1b-313a56292c78 | -11.83836 | -44.99185 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9794c94c-a833-33ef-af63-af64ff4ab4ee | -11.99134 | -46.65194 | 2025-10-01 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84481518-3b92-351c-8896-9a9f1e962315 | -11.39593 | -44.89987 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b94c65cc-747e-3776-8160-159acce101c3 | -10.21273 | -43.0461 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 16681051-ccd8-3b80-9452-99b6682597f0 | -11.99628 | -46.65989 | 2025-10-01 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfb3d3a8-0a6c-31d3-a20b-f5065e7e0b7c | -9.35453 | -46.33807 | 2025-10-01 03:30:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e33faddf-dc98-3f79-9d4d-3e8d68569e9e | -10.91 | -46.51835 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6af017c-22bb-3a3d-bf7c-85d87f7f5ccc | -11.46846 | -45.09326 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 5d709717-b8e3-3b1c-94a9-ba9ade245e8d | -12.88559 | -45.27001 | 2025-10-01 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30b02391-f6d3-340a-a8bc-001fb788246b | -12.6685 | -46.8708 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f5391d3-f200-318d-96c4-0a6e27b9633a | -10.81946 | -46.64564 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fc57c72-bc51-37db-8410-162d6658e6ce | -13.31742 | -47.35181 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8c5f7702-3310-38e7-92ca-aace3258edb1 | -9.92668 | -43.69772 | 2025-10-01 03:30:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90880150-302a-3f53-814b-3c424cdb87de | -13.6534 | -48.03501 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1adc33d-b0eb-342f-aa96-5a97f8bacb82 | -11.81317 | -44.9662 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4813e1e-5d38-32b7-ba0b-927893fa94b3 | -10.82447 | -45.38324 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6656eef-e908-361d-89b7-c5c54af02e2e | -13.21113 | -47.34013 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 40bba210-e256-3bf6-b774-bc9194d627b8 | -13.66556 | -48.04776 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d79a468f-c9e0-3dad-8f51-cc9624b3810e | -10.91247 | -46.5749 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40a8ec1a-af49-30b0-a7e9-374a18440384 | -11.84531 | -45.02154 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 06726107-d470-3321-8cc9-fedf29f0bd0d | -14.02158 | -46.31826 | 2025-10-01 03:30:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 17e842be-647a-3988-99dc-78597e853363 | -11.45336 | -44.97577 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29fc53c5-5edf-3500-a3ee-34f571523edb | -11.80873 | -44.97863 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 749ef2d6-6655-3a26-87fc-4c3b137faed4 | -12.84877 | -47.03086 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6bb05918-467a-326c-82a4-defcfed4bf71 | -10.73894 | -45.37362 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3b1c059-ed31-3801-84bb-8bbe435acb7f | -9.93093 | -43.67574 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b168ba8-a472-3939-bfc4-18797a3d1e3a | -13.36481 | -47.29906 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2bbf7e59-87f6-3703-88ed-30059a279d3a | -9.34987 | -46.335 | 2025-10-01 03:30:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9e4c9aed-8e02-33cf-9680-995dd21b3ea2 | -11.82617 | -44.95642 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7aa4328c-78db-3ba3-943e-0589fd2d266c | -13.32422 | -47.85121 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 03c485a0-037c-3bad-915e-1e61ded0d1d0 | -9.26264 | -45.69118 | 2025-10-01 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f92f18ee-a1fe-300c-a142-203a961caad0 | -13.65343 | -47.32082 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2fd2957d-3851-38ea-8df9-b4826f7e43c8 | -13.75874 | -47.97776 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8a01ab88-aec7-3cd1-bb4b-2744ea3a1cea | -11.83214 | -44.99065 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 287f30ce-dba8-33db-b2fb-5a24c4cd0a2d | -13.33453 | -47.33952 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f47e5e57-dfe0-3947-81a6-f4fcf2ee9688 | -13.33122 | -47.85331 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8cba0bac-e5bf-3f50-983e-a410033b941e | -13.21122 | -47.34566 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 41ff8833-53b9-3cc8-a2f9-c9502962238c | -11.83236 | -44.95774 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92a4b931-02e5-3507-82ff-253d1b3844e0 | -9.32756 | -45.69231 | 2025-10-01 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 068b108b-c8a3-38d0-b9a5-11b667e43e56 | -11.35752 | -38.2835 | 2025-10-01 03:30:00 | NOAA-20 | OLINDINA | BAHIA | Brasil | 2923100 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b840d67f-e343-322a-8bd1-147321e278d3 | -9.93428 | -43.6584 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c866369-53c8-30af-b35e-c1dfe4045dee | -10.831 | -46.66694 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7f0084e-4989-3298-8420-4e4c60311d4b | -10.92552 | -46.51552 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 755a0d2f-a6bc-39a5-8a35-e5d66c124299 | -11.46945 | -45.08843 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0d12774a-5ffd-395b-ab4a-8a288ba3f687 | -10.91005 | -44.34027 | 2025-10-01 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d05c8546-1848-3523-b6ed-0c632f477372 | -11.46841 | -45.07917 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 485bae32-f00c-3254-9f5c-5db7c038ddbd | -11.46319 | -45.07251 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f17274b-74a8-39c4-88d7-2ea2a7ea7896 | -13.77386 | -47.97679 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 80fcfe86-ef85-31cc-aec2-63b33776d0c9 | -11.46231 | -44.97799 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7887bfca-9d04-3198-bae8-e7b70fc7ba1d | -8.53747 | -44.69598 | 2025-10-01 03:30:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd02a944-e8a8-36b5-a3d9-89b33c86dca4 | -13.6754 | -46.79409 | 2025-10-01 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 471b5813-f624-3897-800b-5ef86440d01d | -8.55577 | -44.73988 | 2025-10-01 03:30:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 98077194-1111-3374-aa07-4c5b6d6e6c2b | -10.80854 | -45.36213 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86222521-e3f9-3207-8365-06dc3645dfe6 | -12.41943 | -44.09832 | 2025-10-01 03:30:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb9ac2a2-4778-3a32-a41e-77db42032418 | -12.66886 | -46.86584 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e8fb477-c49a-3c89-ba0f-436bf2024421 | -13.7708 | -47.95708 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5be19719-d430-3fdc-af03-22430670fb17 | -11.47166 | -45.10974 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 65656212-059d-3f2d-b3d1-011bb9c085cb | -11.80923 | -44.98621 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc6cf1d6-5c07-3d88-b6a1-2ff4ba84ae5c | -11.46067 | -44.97182 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ebf14991-fd73-3ee9-bd77-affef031fbda | -13.77252 | -47.98282 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5414d089-5edd-305d-b5df-9e68c95e9be6 | -11.44714 | -43.5184 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd46c5ce-656e-39a9-81f8-a47eef0c11d9 | -11.82406 | -44.96683 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7907df5b-81d1-3fe6-8b9b-01043f380846 | -11.81386 | -44.98518 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 303d74a7-777f-3a87-9cd1-07ba8859f679 | -13.21878 | -47.34419 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3f137a8c-b69e-32a6-a253-8619e612099d | -8.55366 | -44.75086 | 2025-10-01 03:30:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b410a20f-dc61-3d2e-9b9b-52af34b01c92 | -10.90655 | -46.57339 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0afceecd-031c-38b2-a9c5-1a65a5a79b94 | -13.66361 | -48.05659 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a6a4ace0-8916-3d47-a4ef-8141ac84b1bf | -11.82007 | -44.93115 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3ecf2e2-4297-3e15-8c8f-c1ddcb98fb84 | -11.59354 | -45.0406 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| df4249d1-3307-3194-839f-116b3d047767 | -14.20691 | -44.93377 | 2025-10-01 03:30:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 857bee93-3155-32cd-8f53-7aae309895dc | -12.87494 | -44.60656 | 2025-10-01 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README16.md)
