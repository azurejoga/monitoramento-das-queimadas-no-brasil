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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfd30e65-8544-3e68-b93a-5af344a4c797 | -11.6924 | -54.54638 | 2026-09-01 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75a162e0-2b01-3d81-bd0c-cbb584f47bad | -14.28841 | -51.71019 | 2026-09-01 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d176e928-4db4-3dfd-92b3-bbf01e7e4ae2 | -14.46097 | -52.50767 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a21f113-40cc-303e-822b-5a471e6b87cc | -14.41362 | -52.50333 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6b15fa5-04cc-37e8-b9db-7221e78322a0 | -17.14215 | -46.838 | 2026-09-01 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fa2fed5-1fb0-3a30-9114-82342937b0ba | -14.1256 | -52.79642 | 2026-09-01 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 408a8d68-f72e-324e-ba4f-5bc9d0b1ace2 | -14.12619 | -52.79274 | 2026-09-01 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 151c7deb-f2c6-3770-b2c4-60b868a0d1d0 | -18.49961 | -48.44126 | 2026-09-01 04:42:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2448a6eb-319d-3468-90d5-f65d4b732b18 | -14.45865 | -52.52208 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 28df8c93-c8df-3715-9d4c-79c6c8ca1e42 | -17.37726 | -42.37072 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 704166e8-559b-3f97-9fdf-5f0c47e602f8 | -13.55081 | -48.24599 | 2026-09-01 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 391ac76d-478a-3a35-8a84-67e95073ad97 | -15.01487 | -52.76961 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4200451-9ac8-3ee8-9ce5-0ded46df4249 | -16.37398 | -54.52094 | 2026-09-01 04:42:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d59556a5-d366-3674-93c6-c851b2c2daa3 | -14.43758 | -52.5037 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9197d1ff-c085-38b1-ba6e-ba23a092a261 | -16.59647 | -50.23899 | 2026-09-01 04:42:00 | NOAA-21 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87879ace-249c-3abd-ac66-5bb6a9306049 | -15.24055 | -53.84428 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e754537-dacc-33c9-886c-68d2882a5dec | -14.46983 | -52.51663 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 62e38d08-0cef-3b78-b38a-129458b9ce52 | -17.18657 | -54.29541 | 2026-09-01 04:42:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6259fa7d-b709-3fe4-be60-64ced181ad7c | -13.54724 | -48.24547 | 2026-09-01 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43cfb909-c88e-3899-9325-84b56859073c | -14.6681 | -53.54449 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 32f2a8cb-d665-36b4-b90f-f71f567fcacf | -15.21847 | -56.35495 | 2026-09-01 04:42:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c00812de-f763-324b-9159-db10c6a72c0b | -14.7233 | -53.59271 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| daff669b-a90b-30c7-b894-a6b7786214c4 | -13.38411 | -51.77236 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 858da2a3-8d47-3b4e-8767-14dc343fb631 | -13.38455 | -51.81257 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50633d3a-58c3-33c1-849f-ada787f3b16e | -14.46141 | -52.5263 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2fb7028e-f08d-37ba-a9b5-83a0a7e34c8a | -14.45923 | -52.51849 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8d82eeab-fa99-3dbb-a37c-43624802d70c | -14.46145 | -53.32511 | 2026-09-01 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| faedf798-b9b7-3ca1-b37d-7e5684a181b7 | -13.19797 | -44.07633 | 2026-09-01 04:42:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 512cc574-5b5e-3a98-b31f-5e24715692e2 | -13.09714 | -45.17874 | 2026-09-01 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d4a3599-8da8-3fad-8ee2-2d28f72dcb0d | -13.99299 | -54.40191 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40c32ee3-846e-3bed-9378-ff74f008fc5c | -17.31929 | -42.70246 | 2026-09-01 04:42:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a35b36f-9090-3828-b564-2f63cf7039db | -15.59118 | -46.46011 | 2026-09-01 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bea641b1-dbfd-3d29-b415-96beef5a8bd1 | -14.60646 | -53.59719 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a3701b6b-849e-321c-89bb-057879092614 | -14.38244 | -52.53204 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5da0b118-4589-3e35-8573-d511d75294b6 | -17.3908 | -42.36005 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5fc4bf8d-d786-3a85-8e05-7b30da5903cd | -17.38535 | -42.35944 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2215b173-bde5-3883-b735-0c863f61014d | -14.6883 | -53.59073 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aebe96dd-84b8-31af-af0e-a60dd2b2f7df | -15.74931 | -56.41351 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0fc4f8f1-b63d-3ab9-8d57-487e441bab1c | -11.68792 | -54.55025 | 2026-09-01 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4430ce13-458b-31cf-9fcb-d4449cbf3b15 | -14.46315 | -52.51547 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a0c411f3-6664-38ab-90a3-90342b6d49ca | -14.72305 | -53.57286 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b17a496-a19d-345f-87d4-5099ecc6bf3c | -12.89023 | -45.83952 | 2026-09-01 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cac0ce8f-7e38-3d2a-bbf9-230fc82b9d2b | -14.45037 | -52.50955 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a340518-d174-3382-b711-3e489d1da5ed | -11.48419 | -58.51581 | 2026-09-01 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73b6778c-e55c-380d-9cac-f4f6d71e4314 | -17.90215 | -50.6469 | 2026-09-01 04:42:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 728c042d-49d3-3111-98ac-75644c0388e4 | -13.45352 | -51.8712 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 069eb75e-7661-36c9-a04f-dc9628917702 | -13.47482 | -57.03275 | 2026-09-01 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96425a8d-c5bf-3fdd-b5dc-7f53ce624496 | -14.97218 | -48.14605 | 2026-09-01 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0a4c2e8d-ed32-3502-a6b4-f59eb4e5d1db | -15.6065 | -56.3977 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 03085f95-527c-3ed4-8970-5aca2eb91341 | -14.27493 | -52.85595 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70ee9e9f-9a0d-363b-a070-4997aec75621 | -17.4456 | -52.26394 | 2026-09-01 04:42:00 | NOAA-21 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| da71720b-1bc8-3b05-ab73-a5a4b0777c0f | -14.03063 | -47.80545 | 2026-09-01 04:42:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a3e2bd4-4d6c-3d28-9440-5e65a050f8ad | -14.25902 | -52.86851 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8e4e415-f6c1-33e9-b210-a3827e29e7f8 | -13.8184 | -54.00932 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 37bc9f18-12be-3aab-ae4f-ae90196f2b9d | -16.14507 | -52.38031 | 2026-09-01 04:42:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c3afe596-0b5a-3cb3-ba34-872f8f6da223 | -15.83483 | -47.68039 | 2026-09-01 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66d01b87-fed2-34e9-a4ec-c209bbffacef | -14.73081 | -53.58997 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75fc8624-cdc1-3d31-b42b-9e93f2b127e3 | -14.40118 | -52.47928 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b5b8946-fce7-3ebe-ac7b-5773517e3b1e | -15.49014 | -56.00915 | 2026-09-01 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0282999d-03fa-3d7b-8d66-d61306cbfa2d | -15.19051 | -46.22931 | 2026-09-01 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d4994ec-330c-3356-802f-7ef9f4e2cfac | -12.9563 | -45.96375 | 2026-09-01 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e7af7eae-0eaa-3fac-9ecf-fa32f7358947 | -17.79383 | -39.70734 | 2026-09-01 04:42:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 17ce16fd-af20-3653-8bd1-c10afeeab044 | -15.0121 | -52.76542 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3380961-7e3c-36b6-b2f1-92707b585ed2 | -15.76474 | -56.09097 | 2026-09-01 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| cafd2213-7078-3fd9-ab22-3292680fbbcb | -14.26179 | -52.87278 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70a3f97e-ff02-3928-9e7d-ae2865946d74 | -14.56975 | -52.10446 | 2026-09-01 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 920da67c-5db2-3d3d-8997-038e17c29056 | -15.77077 | -56.0942 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 52db8faa-80cd-39d3-8165-840ffbb56374 | -15.6529 | -50.1055 | 2026-09-01 04:42:00 | NOAA-21 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7e48fc57-ea64-3934-b6dd-311c5d2e87da | -15.60426 | -46.57718 | 2026-09-01 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db9be549-b7c9-3572-b907-0ae78d1d566e | -11.48319 | -58.5213 | 2026-09-01 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 840d219e-f2b5-351d-982e-ecfa9af16dfd | -15.76006 | -56.09518 | 2026-09-01 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 5c7f87fb-cbea-3932-8763-43f6ce78933c | -15.55624 | -56.27345 | 2026-09-01 04:42:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1000d95f-293a-3f24-9296-d2285803eccc | -14.25937 | -52.88758 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03b5eb1a-d858-31ae-a919-e314e8aa4e60 | -15.76556 | -56.08619 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 05f84233-bfcd-3cca-9d77-be019131e451 | -15.66771 | -45.91118 | 2026-09-01 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b769ec54-edb7-3a73-a986-01ed7a5bebf4 | -17.72694 | -49.22915 | 2026-09-01 04:42:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5690b85e-58aa-3ad2-956a-6e1ea426e546 | -14.73424 | -53.59061 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b38a9e8-2343-3c55-8849-9ecd5aed781c | -13.32902 | -51.77735 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7617b9ea-a07e-3742-8238-a67ecb1c6018 | -15.0001 | -48.15905 | 2026-09-01 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e49f802-76da-3d88-97e1-b35798daa002 | -13.38248 | -51.76118 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 860169b9-067d-34df-84c2-e9d26fafa1e6 | -15.59974 | -46.58028 | 2026-09-01 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dae5cede-8d7f-3d44-8906-b2b5e10239ae | -15.7484 | -56.41855 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a3e59f84-586b-30c3-8889-0124aff98655 | -13.32636 | -51.72952 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed2d15c7-289b-3b14-993e-7a11fc47c0d5 | -15.66642 | -47.27114 | 2026-09-01 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2106f04a-5cbf-3b49-8881-3f9a4ebf6ce4 | -15.61679 | -56.38698 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3ea0250b-9f43-3ade-8349-bf8273d91bf8 | -15.2233 | -56.35055 | 2026-09-01 04:42:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf7752e3-36b2-3975-bb2c-4b083f152614 | -15.01822 | -52.77015 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7f0f9bde-f09b-3af1-a62f-79b363b1de30 | -14.40453 | -52.47984 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d18ec1f-d48e-3be3-ab1b-b61836c731b4 | -16.36323 | -51.02013 | 2026-09-01 04:42:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b735a30b-7867-307f-9e86-089ae534bbcb | -14.38462 | -52.53987 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97de257a-57f4-3360-8a6e-c97a308a435a | -16.70846 | -47.64092 | 2026-09-01 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7336032b-0867-329f-97ba-f8c62c2d57ec | -15.40579 | -52.72669 | 2026-09-01 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9f1a3e4-fdc0-31a7-8795-203df3c947da | -15.39553 | -53.75882 | 2026-09-01 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e52fa21f-2b61-3352-bc0c-dafd8ddc3794 | -12.60068 | -49.03745 | 2026-09-01 04:42:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e73a4dd7-7f84-3073-9ab8-a3cea6e8ccee | -15.6255 | -56.38327 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 576e7b04-03fc-39fb-9a41-b275230ed5ab | -17.37649 | -42.37777 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17e6919c-9d93-341e-8995-a2f3b4a900f2 | -14.46257 | -52.51908 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1a49fa0d-f376-3b01-9f7a-a51089de4c3e | -14.51683 | -52.28716 | 2026-09-01 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0226533-c497-3530-92a1-5d515718bd72 | -18.15481 | -49.59866 | 2026-09-01 04:42:00 | NOAA-21 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Mata Atlântica | 38.9 |
| 79588e50-43a0-33fc-8c51-f8e58565cf05 | -14.41082 | -53.09626 | 2026-09-01 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README47.md)
