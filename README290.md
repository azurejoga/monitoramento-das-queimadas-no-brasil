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

## Dados Diários - Página 290

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd1048ed-f8e9-3286-a46e-589c0cc7f25b | -6.38554 | -37.8672 | 2026-10-08 16:20:00 | NPP-375 | BREJO DOS SANTOS | PARAÍBA | Brasil | 2502904 | 25 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 81c23d26-7115-3eb1-9064-87afe84dc4a4 | -6.33972 | -35.13118 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 691873c8-55e2-3d80-9a86-f662bab7327b | -2.39942 | -51.30112 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b0f157fc-6dde-3bc3-b030-832a9a380bbc | -6.02404 | -51.72598 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e7ff7165-2385-3d3b-8431-a02523d880ce | -3.89687 | -44.12385 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 30f5e373-7e9c-3d9f-96b4-63d766d12e78 | -6.15954 | -47.93032 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| ac711156-47dd-37a8-86f5-bf8b4774044a | -6.44328 | -45.93037 | 2026-10-08 16:20:00 | NPP-375 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9b47a71d-00ed-30a2-a4f3-b551297db241 | -3.79275 | -41.07917 | 2026-10-08 16:20:00 | NPP-375 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bc92dd7b-d617-3be6-8cac-26002b10f1cf | -3.51814 | -44.31796 | 2026-10-08 16:20:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 03d15e88-73fc-3683-a129-e75b7ec6bf1d | -5.37669 | -44.20493 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 7cf0d855-0c47-3c21-b8ee-42d09e8b0eca | -6.88223 | -43.69183 | 2026-10-08 16:20:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| d90689a8-9327-3884-bf55-ee0f2c59b3f5 | -6.31404 | -45.05827 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 5bbcba10-8f89-3734-94ad-5ee47884746c | -6.85608 | -39.46443 | 2026-10-08 16:20:00 | NPP-375 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 52.4 |
| 2badf03e-76de-3871-bdea-852f1544e0cb | -1.72438 | -48.28775 | 2026-10-08 16:20:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8b3b4e76-2635-32ca-a953-d5537856565d | -8.27165 | -46.9053 | 2026-10-08 16:20:00 | NPP-375 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| aaf2e2c7-0342-397b-a248-40d73f24af87 | -6.97836 | -47.67609 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 81740a6c-224d-3533-a2e2-6980d76c9c5d | -3.01142 | -54.08797 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 12ef82e6-c41b-3aac-a1b4-6e9b85540188 | -6.93022 | -43.66696 | 2026-10-08 16:20:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4828db9c-7eab-325c-b938-91d002fc329f | -5.78281 | -50.10374 | 2026-10-08 16:20:00 | NPP-375 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 08b43430-429e-3885-87b4-82641d9e6e3a | -6.31668 | -35.13485 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 61.3 |
| fba446cf-eae9-3a46-a9b8-d3c62552ae5d | -5.331 | -35.55829 | 2026-10-08 16:20:00 | NPP-375 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 6.3 |
| bdc915ba-e678-3fd1-97fe-d79415c3809a | -5.71849 | -41.63601 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0b8f816f-7dc2-39f1-a66c-f68cede2ee8a | -3.5064 | -43.82972 | 2026-10-08 16:20:00 | NPP-375 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 19e52530-fba5-3d05-a49b-77c73b275de5 | -6.05618 | -42.59963 | 2026-10-08 16:20:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 577c2c31-1c21-32bc-9d70-2e4f4c2e7272 | -6.93368 | -45.25618 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6e705c8d-67c4-38ce-98dd-312466200df0 | -6.17368 | -44.85772 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 00ea7832-b0b6-318e-838f-621fdc64da24 | -5.08939 | -37.50371 | 2026-10-08 16:20:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 7.0 |
| efe823ba-cb42-325a-a95d-d2555ef352aa | -3.30402 | -41.02553 | 2026-10-08 16:20:00 | NPP-375 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a96a12f4-7296-3ae8-8cb5-26027bd0d20a | -6.92951 | -43.06898 | 2026-10-08 16:20:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 41fba51d-488d-385d-b72a-7ffcb6e59e1c | -3.00639 | -54.10383 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 356f93a1-cf9b-392d-b1ff-89e9a38ea368 | -4.02751 | -44.7596 | 2026-10-08 16:20:00 | NPP-375 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fe076a60-4cdb-3d8c-a71c-4309ae6079b9 | -5.47409 | -45.69013 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| eb0f2165-0cca-3dc1-a046-88a4855c0980 | -5.09821 | -46.21132 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 259.9 |
| 24a7f018-e876-31cf-9801-1e8c32238447 | -6.84885 | -39.55086 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ae46cf83-2d89-3e41-808d-02f365b6e20d | -6.95428 | -44.41993 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42825667-904a-3d3f-ab9a-e130f31d8ed9 | -5.9877 | -41.3652 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 55d1c571-aaf5-3c74-8df2-96a86d15fd7f | -3.00836 | -53.90348 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1a6ebf67-4689-3c19-8edb-af25cd1901a3 | -1.77865 | -47.9048 | 2026-10-08 16:20:00 | NPP-375 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2d9e4788-407f-3d13-9acc-dbe3644558ca | -5.74787 | -41.7134 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 707b5f2f-73a1-3836-b0ea-a1a909ac7350 | -5.17469 | -48.96676 | 2026-10-08 16:20:00 | NPP-375 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 0d0ca32a-2634-308b-a1cf-e4fd20ff89a3 | -7.39164 | -46.20401 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e2d7642b-8df3-31e1-bde2-d1bcbfe9f92c | -6.29401 | -43.87444 | 2026-10-08 16:20:00 | NPP-375 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2a868afa-1ad0-31e8-8782-0e83416e7368 | -5.35937 | -43.07419 | 2026-10-08 16:20:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 88eb939c-78b6-3639-a4b2-61c63ddd3c7f | -5.69716 | -53.45888 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| f4cf1a0d-2a5c-3aae-9f42-d9e2dedd6a1b | -6.95067 | -45.28293 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3e9163e0-88a9-340f-b3e6-158dc0aaf2e8 | -2.07559 | -46.57272 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 480.7 |
| 8fbf7b5c-8c8d-3055-98e9-92797a313fd9 | -4.74567 | -40.50248 | 2026-10-08 16:20:00 | NPP-375 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| f7d7cd91-bfc5-34a3-958a-091dd5aa8166 | -5.37335 | -44.20277 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| c843dd0b-8742-395e-96e9-7e86ab2ce4f3 | -4.93704 | -42.81037 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 26.0 |
| e83adbfd-bb7b-36da-8ba7-4d6ae84818dc | -4.64091 | -50.96439 | 2026-10-08 16:20:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b9c712db-94c2-3503-9fdf-3047e28b5ead | -6.59966 | -37.89615 | 2026-10-08 16:20:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 6979f982-0889-39ff-81af-d06dc20f983b | -6.85329 | -39.46841 | 2026-10-08 16:20:00 | NPP-375 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 96ed8904-8b57-35d4-957c-25def8153d42 | -6.96703 | -47.66955 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 96987960-1795-32f9-890a-6c55f12362b6 | -4.68966 | -42.92245 | 2026-10-08 16:20:00 | NPP-375 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b046c544-724c-321d-8445-40bb17badc38 | -6.68717 | -44.11234 | 2026-10-08 16:20:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| ac2ce2a7-6a6f-37af-973b-a9a64fb7bcb8 | -1.901 | -45.41973 | 2026-10-08 16:20:00 | NPP-375 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 65bc3f16-d185-3faa-8b28-bc9c86f55ae7 | -7.74846 | -43.81011 | 2026-10-08 16:20:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 60e8a780-e5c0-3139-be78-09622a4f6a74 | -5.37868 | -45.86576 | 2026-10-08 16:20:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c956bd5a-dd30-33b1-97fd-70b9de07b98e | -5.79399 | -43.75221 | 2026-10-08 16:20:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c0ab66a4-7453-36a2-82ad-b6f4dd3ee8ef | -2.43032 | -49.62728 | 2026-10-08 16:20:00 | NPP-375 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 47efcfb6-cee0-3188-95ec-9970d977d001 | -5.52476 | -45.57702 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e6490cd7-4db5-3149-9d3f-1d7b8cd60383 | -6.88613 | -43.69123 | 2026-10-08 16:20:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| fbac19ed-ce97-3ddc-817a-1d4254a01e1f | -2.98388 | -54.09105 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 55d7c676-27c9-3cfc-8b41-3d6551ca21b3 | -6.23373 | -43.73127 | 2026-10-08 16:20:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0e249a68-b97e-3674-bd44-bc5a2fee3209 | -6.67225 | -45.36975 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| d224aa50-77bf-3a19-b692-b7cfab77efce | -5.74845 | -41.71722 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 44.6 |
| b9d9029a-11b3-345a-a925-db9e8a87dbae | -2.47619 | -46.01787 | 2026-10-08 16:20:00 | NPP-375 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b1c32238-b095-322f-823a-e01f375d2017 | -5.8519 | -42.62749 | 2026-10-08 16:20:00 | NPP-375 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a077e4d8-ca97-369f-88cb-86376a9c7dcc | -6.14543 | -52.64969 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 26035fb3-3a70-30c2-b3d3-6de800afa4bb | -5.83942 | -35.4053 | 2026-10-08 16:20:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 6.3 |
| e8e12405-efa1-3b8f-be17-9027e7eadb66 | -5.53251 | -44.28857 | 2026-10-08 16:20:00 | NPP-375 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 46042736-31ca-30af-a1c7-614ee278d033 | -5.53189 | -48.17396 | 2026-10-08 16:20:00 | NPP-375 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cf43b089-09f9-34b8-a5dd-918e9cde1852 | -6.53073 | -45.38092 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 21c90e37-7fed-3528-b9a0-37c523e57c1c | -5.45567 | -45.59517 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cc9df30d-b925-3b3a-8d6e-244ee91a0f46 | -5.68122 | -42.57943 | 2026-10-08 16:20:00 | NPP-375 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e8cc73e5-da5f-341c-857d-a775560130cc | -5.37504 | -44.18715 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9d92d154-271d-3b24-af3f-b2b7bdc1aac6 | -4.72005 | -44.1861 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5e8bcdff-91a9-33fc-bdaa-3556d6208fc4 | -6.34457 | -43.83662 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 85a859f9-1993-35dd-9b1c-ed77b9e46877 | -6.42973 | -44.81713 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1361e8ca-6041-344a-a248-2668dd3d6994 | -3.18012 | -50.58484 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0ccf4cab-895d-341e-bc10-ef02de737442 | -5.98981 | -40.93502 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 37.2 |
| 8de195a8-0391-3012-a9ad-7895951a3459 | -3.01363 | -43.34036 | 2026-10-08 16:20:00 | NPP-375 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dfb4f634-9f81-336a-a4af-a6959e3f3360 | -3.09946 | -53.96236 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| ccb97d71-0606-3288-9e1b-086190223e4a | -3.00355 | -54.07316 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 4cb04bad-928f-386f-bef5-31b22a477622 | -6.12816 | -52.72568 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cc37da3d-be8a-36a5-82bc-580cb2c0bb87 | -3.78691 | -41.65928 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| a99f87e0-8b59-31ed-9e4f-2ef4822d5be0 | -6.05719 | -42.91426 | 2026-10-08 16:20:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 08dc818b-ee6e-3348-86ac-d68a27651dbe | -6.99488 | -41.47861 | 2026-10-08 16:20:00 | NPP-375 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| c598878d-f26c-376a-8e3a-c74b117ce322 | -6.7712 | -44.1277 | 2026-10-08 16:20:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 633a64e5-837f-3a33-a7d0-6cca01c26ea2 | -3.29653 | -44.68297 | 2026-10-08 16:20:00 | NPP-375 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4354b8dd-beed-318c-b5fe-72acd3e88767 | -5.21768 | -44.63043 | 2026-10-08 16:20:00 | NPP-375 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c31807f1-7a2f-31f3-8bb7-0449827b6e30 | -4.98098 | -42.60266 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 1939c599-76d1-352d-82ba-133160126d00 | -7.53624 | -42.0919 | 2026-10-08 16:20:00 | NPP-375 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 33.2 |
| 63c0df3f-6060-3532-8da8-2e6900b3c025 | -3.30896 | -44.70436 | 2026-10-08 16:20:00 | NPP-375 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| cc669a98-a239-3b39-8683-aaa2998800fa | -2.99933 | -54.04401 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ec6d842d-d876-3339-90c3-960c7451014d | -4.26387 | -38.72714 | 2026-10-08 16:20:00 | NPP-375 | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 993eb5fe-49f1-33a5-83b3-262c45cd3dca | -7.08611 | -43.08692 | 2026-10-08 16:20:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| befcfe40-67e4-3f90-bb75-6bfa5ad0e163 | -4.62873 | -43.49767 | 2026-10-08 16:20:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ebc4ad07-b5af-37e0-abd1-1f56d610fdfc | -5.78488 | -45.3873 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7d9a9ff4-4b90-3853-8e64-259209678d7b | -6.14457 | -52.64312 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |


[Clique aqui para ver as próximas entradas](README291.md)
