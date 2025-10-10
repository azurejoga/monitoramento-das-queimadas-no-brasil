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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6edd0f88-5d73-3850-9b50-d414eddadaba | -8.18667 | -43.33032 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7ca1d203-fb55-33f9-9d1f-31ed529fc0e4 | -7.41689 | -45.16249 | 2025-10-10 03:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb390c30-cda8-338f-b028-f691193cd163 | -8.16526 | -43.32602 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4ce55d2f-6ad6-302a-b561-fc4dd0cdc431 | -7.45047 | -37.33493 | 2025-10-10 03:40:00 | NPP-375D | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 094506d9-abed-34f0-869a-ced7903fe863 | -6.75782 | -42.83281 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| aad8679f-a7c0-360b-b66d-90ae435006e3 | -13.01604 | -41.42708 | 2025-10-10 03:40:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 62f04860-508e-34fa-a0a3-d209b2184d4d | -8.50708 | -46.12918 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 663447b5-572e-3584-929e-bdb951ecca00 | -8.51659 | -46.12236 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5b9eaa7-9a5a-33de-ad6f-d2126a171b66 | -7.68053 | -42.39555 | 2025-10-10 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ac1f49db-e01d-3647-b5e2-f5c6e79348ae | -9.66123 | -43.84427 | 2025-10-10 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5040b13d-f1c7-3355-adb0-2ac5fe2b170d | -6.75236 | -42.84534 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d1600bd3-ab12-3f4d-aadc-f1a6fd9b2b81 | -6.66024 | -47.75536 | 2025-10-10 03:40:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 05f06721-27b7-3fc8-9d53-cb5b2c0275d2 | -6.74523 | -42.8547 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 957edc5d-f0ca-35cd-a30b-cba090cb6f57 | -7.84151 | -44.54928 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4d807ae4-591b-3a82-bf65-34b202269412 | -8.17413 | -43.32113 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ce88e13a-a41d-3263-b95c-e1b4a27cdc36 | -11.6875 | -47.52203 | 2025-10-10 03:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bf7114e-414a-3cca-987b-6b53f30edb8f | -8.18787 | -43.32359 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 97514ddb-52d0-320e-bcbb-800b122dbada | -12.63342 | -45.043 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e5dcb19-2eaa-358f-813e-e8197bf76e57 | -7.77402 | -44.04732 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a231ac6-35fa-32b9-9f4c-aede5690727b | -7.66326 | -42.5839 | 2025-10-10 03:40:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e5897f35-3098-37f1-a8c2-b8aee592285c | -8.1937 | -43.33525 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| d23f00e8-b5d8-3088-ac7e-5312344996c0 | -7.85957 | -44.45373 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4bfdc67e-9299-3ab8-85dc-cb0e7c1f044e | -12.10221 | -45.00239 | 2025-10-10 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cad357da-1859-3156-a35e-5851ab2054b2 | -7.7953 | -44.19509 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e2d316d-2a24-3e2c-a5d1-bc5a8650e236 | -8.51558 | -46.12756 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c31f995f-3987-3f9d-8e98-9ce56f5ca8b3 | -6.62874 | -39.30407 | 2025-10-10 03:40:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8ebbf2be-55b0-36c1-b56e-9a9f382538d1 | -6.62795 | -39.30767 | 2025-10-10 03:40:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2378de26-1bd2-3f24-9c77-a4f2e7d28397 | -8.82444 | -40.55068 | 2025-10-10 03:40:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a8b19698-4fda-3ec9-a476-a6c5d9462d53 | -6.73048 | -42.87606 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3b843126-ff87-3a3a-be65-7f18eceaa35a | -7.79418 | -42.6086 | 2025-10-10 03:40:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 458332d0-96a1-38e2-a57e-340db8d9e3ea | -7.70737 | -42.37932 | 2025-10-10 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 80c07b5d-9529-3927-b53b-7bfba167e929 | -9.90122 | -43.56313 | 2025-10-10 03:40:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2786d9d7-4a93-3aff-8518-547003c5502c | -13.06763 | -43.09186 | 2025-10-10 03:40:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 576df6e0-7b12-314e-9cdd-46da64b4ca46 | -12.43912 | -45.7789 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f21e3af-6b62-39a2-94e8-e259b69e35b7 | -7.57546 | -44.38667 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f4a43d6-3d9c-324e-a4cc-7b133d40b21b | -8.18958 | -43.32752 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a944b2d1-30ad-3a62-b408-615bf2ecae23 | -8.19202 | -43.3314 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c88fed48-4f57-331a-9613-4925983809fd | -12.22995 | -43.79231 | 2025-10-10 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75977f92-c105-305f-92eb-16eccde09376 | -8.2121 | -43.35594 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| db319925-de11-3140-8083-05d3e7de01b4 | -7.13225 | -44.13595 | 2025-10-10 03:40:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5301636c-d2b0-3eb3-b015-bb0b98cbc50b | -8.19431 | -43.33194 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 6247d376-9967-35f0-834e-83dff3da391e | -8.21147 | -43.35933 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 509e3744-d0a5-343c-94bb-84685b3c75a4 | -12.63896 | -45.04414 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2dfd794f-c517-3107-99a0-452e4e8c12a9 | -7.68107 | -42.39249 | 2025-10-10 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0b190b2a-333f-34b8-8d08-4188f541e3ee | -12.63518 | -45.06327 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6c867792-4cdf-340a-add6-8adb7b85e753 | -7.08006 | -43.51442 | 2025-10-10 03:40:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d61a3354-c4a9-3099-beea-662f60381610 | -7.08024 | -43.51847 | 2025-10-10 03:40:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6cc9b4b3-908f-3c75-8bf6-6158b696ea49 | -7.67142 | -42.57624 | 2025-10-10 03:40:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ba850f4c-da8f-3975-a954-300e82b64be6 | -12.10151 | -45.00595 | 2025-10-10 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c22f1d4e-2801-3dfb-a144-c1d052bec194 | -8.19322 | -43.32461 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| dbe4aff2-b674-3373-ae78-cc9561ead7a4 | -8.50717 | -46.13681 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e59035fa-30e6-3132-9f95-c68c97f341b8 | -7.6657 | -42.57843 | 2025-10-10 03:40:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5cba3426-cf40-3707-b8fe-ee74837b3362 | -8.51587 | -46.18792 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 368e5aa4-7d2e-3643-9d32-936682e865fe | -10.16709 | -44.5875 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1220e7f-2b0a-35a4-b83b-aa0ac357f365 | -11.96596 | -45.20788 | 2025-10-10 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c11b5b58-63e6-3232-a394-780523524a69 | -12.62963 | -45.06215 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 0c235c90-f276-38ef-9c48-209933ad9e16 | -6.75352 | -42.8387 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1d5ea529-aeff-300d-9d4d-e14fd5e5fd15 | -7.85443 | -44.45497 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab109fed-7118-37bc-a4dd-2385ea16db64 | -7.41061 | -45.16412 | 2025-10-10 03:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdf9b409-1b7c-3a8b-86eb-f05e0d1c07ea | -8.19783 | -43.34294 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| de4d144e-ecb5-3992-899f-46197c129cad | -12.62253 | -45.06882 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 0cb375d0-ff62-37a7-82ad-84641698d936 | -7.26416 | -44.10027 | 2025-10-10 03:40:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69a74d90-6abb-33e4-b5b3-fa1656559fc7 | -6.75598 | -42.84296 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c982f425-b453-397d-ba44-842cf0674deb | -7.14618 | -42.19518 | 2025-10-10 03:40:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b5c267e9-b060-35e1-b2f0-8698edd303ad | -9.30368 | -40.23481 | 2025-10-10 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0914f278-79ea-3075-90b0-d7a9da7512ba | -11.78849 | -45.04412 | 2025-10-10 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 787fdf40-6023-32f0-9497-1b97d08d92fb | -7.89885 | -37.05985 | 2025-10-10 03:40:00 | NPP-375D | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3d85c7d4-2eee-36d9-92d3-b264d933e315 | -6.58211 | -44.21721 | 2025-10-10 03:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| baf3d052-ffb0-35e3-bfdd-840349e57c23 | -10.15792 | -44.5744 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f556094-f777-3abd-869e-15f96ad84fef | -8.52476 | -44.59603 | 2025-10-10 03:40:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f217c29f-d2d9-37ff-96ed-866ff1b61630 | -7.70407 | -42.38099 | 2025-10-10 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a22e2d1d-f9a2-36e1-9c62-21d7a0ddb5c3 | -6.73109 | -42.87254 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 81d8a4c6-6c6e-3dff-a10e-4908af14e3e6 | -8.19262 | -43.32803 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7d42aade-24a7-3cb0-824a-04b4a4edbd1c | -8.50016 | -46.20103 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 054611c3-7149-3e71-83bf-d815d8f5e2d6 | -6.48133 | -39.81568 | 2025-10-10 03:40:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dde9e405-0d95-34bb-a79f-32847021e382 | -7.79772 | -42.40182 | 2025-10-10 03:40:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 70284e4e-cc93-37b2-9137-191a3b377979 | -9.0983 | -45.03135 | 2025-10-10 03:40:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 48baf630-ab49-37bb-8f77-1645fdc2a63d | -7.79914 | -42.42365 | 2025-10-10 03:40:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 22a36ee8-12b0-3013-8175-f4b2db4fad43 | -7.70355 | -42.38393 | 2025-10-10 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 68e58637-907a-3ca1-aebf-979a9403d940 | -8.18422 | -43.32651 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8bc0d21b-cc3c-3f0f-a1d0-52c003f74bb8 | -6.73514 | -42.84953 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b5b325de-9e56-3dc7-b914-28db0b082135 | -6.55378 | -39.9962 | 2025-10-10 03:40:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| aad14609-3a78-3c91-ac0e-8558fe610d6a | -7.54702 | -44.60073 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7b01415a-eb6a-37da-9f47-425afb02bf49 | -7.66683 | -35.15357 | 2025-10-10 03:40:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 33edf2a0-78a7-3d3b-8762-5ca774a80274 | -8.19021 | -43.32414 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 289ea531-b28c-361c-a3a7-3f92b53b43bd | -8.16585 | -43.3227 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e18f78e6-9cd0-35d0-aa94-9304fd56f850 | -5.65241 | -45.97096 | 2025-10-10 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ce60a37-8a78-318f-8866-fcf148e4393e | -7.73812 | -42.41243 | 2025-10-10 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 829f5f76-0bf8-373c-8362-caedc19cbe2c | -6.07553 | -42.59327 | 2025-10-10 03:40:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 98f08e77-a724-3f1e-b641-621b28bca2da | -7.79998 | -41.65776 | 2025-10-10 03:40:00 | NPP-375D | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c4499fcf-4042-3612-a101-3446760abc7e | -11.68237 | -47.52445 | 2025-10-10 03:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd61c429-dcdd-35cb-8eb7-6724dc29ea81 | -7.63327 | -43.05391 | 2025-10-10 03:40:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c264c58b-5e24-33e2-9624-70a831216917 | -7.61387 | -43.06997 | 2025-10-10 03:40:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| da438a49-bdf3-364c-9815-0f01a7e55957 | -8.51244 | -46.13575 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9f0c8881-c295-3d79-b4cd-fef7001d4fc8 | -8.07148 | -42.94804 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 6210218f-b001-35a2-8717-ffc8cc91b18f | -7.67196 | -42.57325 | 2025-10-10 03:40:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0517d935-9124-3f4f-ab77-a877f0562639 | -12.62481 | -45.05733 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3daf2570-d511-3234-afd3-f6a436284552 | -8.51701 | -46.18185 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8832f005-c863-31bd-8032-c281a2f3eef6 | -9.66056 | -43.84789 | 2025-10-10 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b1d7c3e0-e153-3adf-a5ec-e512f748cca9 | -10.16564 | -44.59517 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README13.md)
