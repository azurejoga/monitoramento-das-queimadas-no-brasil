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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 700cd49a-5070-396f-8c6b-43ce47e9e9e0 | -15.97434 | -42.00941 | 2025-09-28 03:38:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 11346afd-27f4-397a-aaf0-4d95c919b8fd | -14.77622 | -45.69101 | 2025-09-28 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f09b1eb-3b0b-3839-afff-158e62159577 | -13.39894 | -48.15479 | 2025-09-28 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 69b5e79d-ca66-3fe2-afac-b55887043b86 | -12.95327 | -46.38492 | 2025-09-28 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fa6d0eda-a05a-37fc-8731-81c5900aced1 | -12.01678 | -47.90902 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed68abd6-a8c0-3e67-b817-1f8b6bfb4db7 | -10.91422 | -45.7333 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10a2226a-03bf-3395-87c2-96d4655a0497 | -12.95416 | -46.38062 | 2025-09-28 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 804de2aa-a0cb-3689-9f1c-29eb37f177f7 | -11.98268 | -48.00909 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6939041-45a3-357d-afdb-1a27d3eab107 | -13.40563 | -48.15546 | 2025-09-28 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf67d740-479c-3bf9-a8c5-e4ed8c928b12 | -12.44087 | -45.20753 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| de057565-5233-33b6-9633-8960719dcdec | -12.89681 | -45.17638 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27592bd5-539c-3cf4-a945-6faef2501a28 | -11.98716 | -48.00482 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 39e825d2-b880-3187-9aba-d9eae18630dd | -15.05714 | -42.33513 | 2025-09-28 03:38:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| aca70517-2258-3c1f-8122-b168204abf63 | -11.7966 | -44.90937 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67e679bb-bf80-327d-b9ea-6b74077e1080 | -11.77648 | -43.76611 | 2025-09-28 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ba3fa05-8fec-3dbd-87b6-d94402808c9b | -14.87776 | -47.97626 | 2025-09-28 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| babf993f-1a27-3779-bf23-d903a6d03ace | -11.69295 | -44.43678 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 44f30f19-8e47-3ea7-90c0-0bf826550efb | -12.91812 | -45.18455 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8eff9b60-251b-367e-b1c9-bd9ada5c02ce | -14.84027 | -45.57377 | 2025-09-28 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9da487b-b1b3-3814-959f-8526d9922728 | -12.00147 | -47.08818 | 2025-09-28 03:38:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8a41398a-b10e-35dc-ba41-049d992a858c | -13.25512 | -48.45449 | 2025-09-28 03:38:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b9662bc-84ff-3f9d-8812-15a8031147f3 | -13.52386 | -47.40558 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| db36516b-831c-3668-a9c9-ea219deda6cd | -11.35475 | -45.04583 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6826a673-66ff-30e1-b651-04735f22eb60 | -13.76982 | -47.86943 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 253bde34-2482-38be-a394-3b386a8a6481 | -10.91153 | -45.74681 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 905ace6d-4ba1-3ba6-b28c-16ccb276b81c | -11.43308 | -44.96026 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0aec623c-0c69-37cf-9c0d-6033e2551114 | -11.6161 | -44.41782 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddaf0f27-bf7c-3498-a832-4cf5a99c0220 | -12.9875 | -49.44893 | 2025-09-28 03:38:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1d35b59f-5b54-3e41-b121-5b0fe02bf20a | -13.62596 | -48.07055 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 40e7a5df-b783-3fc0-947b-c802bcf3496a | -11.50894 | -46.95383 | 2025-09-28 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6bb75e4-4f7b-3350-9d58-2741eb5bac2e | -13.777 | -47.86707 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7bbe4809-0ff1-3e43-bf1b-68cca7be85d0 | -11.9844 | -47.88683 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 84b85d63-55e2-3113-b183-ae9b5041f362 | -12.92805 | -45.16325 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b93507dd-5ccc-37be-a7db-e1df911819d5 | -11.95554 | -47.97258 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| afdeb0e9-1c3d-365a-b7cd-5e8284984b9d | -11.7117 | -44.42599 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92133a0b-fe70-3124-be87-d0771226ba96 | -9.04375 | -45.5152 | 2025-09-28 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e30cca40-f4fa-3437-8ae6-0687817e2296 | -14.54026 | -48.40512 | 2025-09-28 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ced896ad-0e7a-36ba-b062-5822dd16067e | -12.41558 | -44.11187 | 2025-09-28 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bcdbde0-4cc8-3202-afc2-1587ec41fa85 | -11.58198 | -45.48966 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7319fb99-61d7-3b97-851f-a57326b07954 | -14.59117 | -48.26381 | 2025-09-28 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 879169c4-859a-3ac3-b1fb-1324598ea5cc | -11.98715 | -47.8856 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 01fbfd5f-673f-3e97-9a4f-2c3b1da423ef | -15.18661 | -50.09825 | 2025-09-28 03:38:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aac9710b-e686-382b-bc16-c6e8acd37e62 | -10.11981 | -45.65989 | 2025-09-28 03:38:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c5b207f9-b4a0-3712-9d6c-246625800856 | -11.36039 | -45.04683 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6581064-6dbb-3299-a55f-ac56d04996b5 | -13.33892 | -47.28677 | 2025-09-28 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61e30e28-5d52-3ebf-8ffc-241ec4b2dfe3 | -13.57407 | -44.4431 | 2025-09-28 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e3f5e04-1cd5-3d48-9114-65ccde1b15e2 | -14.87543 | -47.97385 | 2025-09-28 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09c168bf-26cc-3d88-9b3f-1bb6f43cbd99 | -11.95094 | -47.9795 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9256b2b7-219f-3fc4-ad51-d76982f525e2 | -15.15213 | -46.41903 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0fff498-0e86-331f-a95b-08abab85dc48 | -11.9429 | -47.9333 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1c851df0-1475-3c03-a36f-90979e78326d | -11.3815 | -44.96663 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f50a9976-dce9-3086-8d1d-a132678aa5c4 | -9.11422 | -46.67751 | 2025-09-28 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e42d015-ba93-37f3-a650-b6fe593b1656 | -15.81705 | -41.89511 | 2025-09-28 03:38:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 784a5229-464f-397a-9ce8-ae7611be121f | -15.22037 | -48.06479 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d51af34-75a6-3e5f-b666-eb284749366d | -11.40385 | -44.90988 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9fd3da4-a6da-3b2b-b3b0-aa9949d726ba | -10.29668 | -45.39835 | 2025-09-28 03:38:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c0d23176-2142-3c5b-8137-860b5dd78939 | -11.37516 | -44.9391 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7efa1bd0-a3db-3535-afc2-c7d87e09797b | -12.00712 | -47.95678 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| feff2977-4063-36c9-9ed8-4c4612e11057 | -11.51018 | -46.94763 | 2025-09-28 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51184611-28f6-32af-be22-4caaf37bf769 | -13.53973 | -43.50464 | 2025-09-28 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 504c7bdc-28df-3751-b8c7-d3588a9af8dc | -11.40456 | -44.90611 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b20e820-4939-3c97-8df3-902c52285c0c | -11.44366 | -44.99546 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4f65d352-7e9f-38ef-bb9f-ee19c908b857 | -12.69217 | -46.87913 | 2025-09-28 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a4cd00dd-2184-3618-938a-bcb40408d208 | -11.71966 | -44.42735 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0b06ade8-4560-368a-9cc6-3757a03ebe81 | -11.69418 | -44.40088 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 010d80e2-af6e-360b-be50-009d51ae82ff | -14.78623 | -45.64159 | 2025-09-28 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c0ced79-15dc-3568-9f3f-a0930435f48c | -12.91664 | -45.19204 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 18e2c83c-0da8-3bb6-8b72-d4fc6e9b8865 | -12.67955 | -46.87823 | 2025-09-28 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 984cf3fd-9992-3e15-9167-323ecf5e12d1 | -11.04807 | -45.88405 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e369c9c-71cc-3237-85e1-c863411ccc1c | -15.20759 | -48.06288 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4aed503-93ee-3c9f-aaec-84c2246b792c | -12.97677 | -46.85549 | 2025-09-28 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bd4ca57-603b-3b78-8ded-368ab7096185 | -15.90098 | -46.20538 | 2025-09-28 03:38:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c29aee6d-ca63-3743-94ee-4825cbb4506a | -15.32754 | -47.90327 | 2025-09-28 03:38:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b5587dcc-d44e-3db7-820e-96ae7fb33524 | -11.42408 | -45.03646 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c3864c91-9bfb-373e-8f50-3e2dae0f9ceb | -15.21107 | -48.05939 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf5d9b27-7fd7-3489-b63f-1ea676cc3bb6 | -9.06529 | -45.53321 | 2025-09-28 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a97ea7e0-1ad2-3e33-a381-0e36149626b6 | -9.29099 | -45.71124 | 2025-09-28 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 438a4a35-1749-3d22-b96a-3070347f1f24 | -12.68673 | -46.87443 | 2025-09-28 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 626e075d-2453-3925-a736-48c6a178d41a | -15.05625 | -42.33982 | 2025-09-28 03:38:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 3721993c-a882-3187-be67-833977466904 | -12.44026 | -45.20304 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0134453f-b8b3-3cc0-96ce-8b603423aa2f | -11.95225 | -47.97334 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 109deacb-3f7a-342e-a530-d12c56440c42 | -11.66042 | -45.33762 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcd265a9-5b27-349e-a4e6-16ad1f76292c | -12.25554 | -44.09997 | 2025-09-28 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 039889de-319c-38ad-80a8-3b13cfc6e742 | -15.44397 | -48.22768 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e70633ec-87bd-3bd3-8c17-b84f3aae9e42 | -13.63909 | -44.41389 | 2025-09-28 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 45898952-ed72-3ba1-a86f-7ce0aa655f4a | -13.62557 | -47.31327 | 2025-09-28 03:38:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72f805d8-9405-3a0c-a8a2-f57cd19f52e7 | -12.68752 | -46.87054 | 2025-09-28 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 570439f1-cc86-3dba-bb63-16c78ead6481 | -14.83944 | -45.57535 | 2025-09-28 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efc4d40f-26fa-3f1f-8398-fab8c7b93135 | -13.34484 | -47.28955 | 2025-09-28 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2716763c-5818-3707-9968-d49b20d92757 | -11.94414 | -47.92727 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b0f75525-d2c5-3dae-a7d6-c2aee8f95b4e | -11.35756 | -45.00074 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc8f52af-5ad8-3182-a64c-890f2a155dc0 | -12.42161 | -44.11325 | 2025-09-28 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58a03ede-970f-31c9-9d29-1ef8b11eade9 | -13.01773 | -49.46324 | 2025-09-28 03:38:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cee147f0-2a29-3a24-96bd-f0ab2daea27b | -11.41527 | -44.91052 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1554b0d6-c385-3550-97c6-59daae8ee1b1 | -14.40157 | -42.48837 | 2025-09-28 03:38:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7c56df92-26d4-3856-a8c1-bd3fa1ae1c4f | -13.60921 | -48.08551 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 909ece77-e7f1-321c-a7ce-183d3ed6fd34 | -11.95426 | -47.97878 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 32bdfcd6-5daf-39d1-bac8-626489feefec | -11.40287 | -44.90759 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 089c5638-8d4e-3419-8584-be10c34abbbe | -13.58344 | -47.30724 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ba760f6-c678-347d-976f-e98ebf9f4e59 | -11.79158 | -44.90563 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README19.md)
