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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1108a53-7b71-3a4e-a9c1-b95471d38612 | -6.59076 | -45.95004 | 2024-10-10 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4a17c7f-6333-33a2-8deb-d3577350a2a9 | -8.87434 | -45.86226 | 2024-10-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 315f9508-6c98-3ec7-a918-ecf8b6f97c3c | -8.86981 | -45.86132 | 2024-10-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 72b0cd13-65b8-32a2-a8ab-06e346310d9a | -8.57749 | -45.7781 | 2024-10-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ab09b8c-890d-3c40-a8a6-6ccfe0b41e1f | -9.14729 | -46.3923 | 2024-10-10 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 19a6308a-86e8-3eaf-9c4a-4cfcef7b5bf3 | -9.14588 | -46.38925 | 2024-10-10 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a75f1587-0012-3eb0-9695-faab9086f68a | -9.14495 | -46.39458 | 2024-10-10 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5e9c4f12-a7b2-3deb-8ac4-3c9ffcdcd129 | -9.14266 | -46.39114 | 2024-10-10 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4da91642-5a8b-3ebe-973d-815213f90d94 | -8.625 | -46.4938 | 2024-10-10 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4614a919-ede0-35da-a6fc-a862a6045ff2 | -8.62024 | -46.49287 | 2024-10-10 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f343626c-a236-33b0-babf-8fd8dc67733f | -8.40003 | -46.9656 | 2024-10-10 03:55:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8ae985b-2827-3651-bee9-7a46ff6a704e | -8.25296 | -46.86734 | 2024-10-10 03:55:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7dec0d6-8679-3439-b1c9-d3feb2b88a3d | -8.2394 | -46.27717 | 2024-10-10 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 11d441e4-52d7-359b-920c-ef5aade1ddb6 | -8.13738 | -46.26766 | 2024-10-10 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f856f5ee-7334-38df-b17e-4f8236e60cad | -10.28016 | -46.7356 | 2024-10-10 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e5210b22-244d-307e-af9c-79d4e6ad26d0 | -10.27897 | -46.73324 | 2024-10-10 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3d97634d-2baa-376f-8caf-034964aa9ad4 | -10.27812 | -46.73806 | 2024-10-10 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 74f2d7f9-715e-3ed7-9c62-db6ea22209f3 | -10.27456 | -46.73955 | 2024-10-10 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58af35a8-3df0-3a79-9c33-05b5837debd0 | -10.27336 | -46.73743 | 2024-10-10 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f980e6c5-4844-3019-b575-c37f80683598 | -10.26979 | -46.739 | 2024-10-10 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cebfb5e7-5b60-34ed-b041-d6797c434285 | -4.47683 | -47.73874 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65fdffe6-f3d9-35fa-a9d2-bc983454b07c | -4.47595 | -47.73808 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a7d53a8-e76b-371d-a992-09c418a8626b | -4.47193 | -47.73383 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8b0009b-c987-308c-9fc5-884863162cdf | -4.47127 | -47.73774 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6e2e570-3784-3bd8-a5b4-3db806f0cf2f | -4.92938 | -47.58269 | 2024-10-10 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7007a487-5d4b-3735-bced-d6fd56147253 | -4.92385 | -47.58208 | 2024-10-10 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2d4adbc-83f7-34cf-9038-a9a4f42194b5 | -4.47108 | -47.73324 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6dd0d33b-4f37-363b-83d8-4e5944eff1c5 | -4.31814 | -47.7025 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| de55e951-f26d-3c59-abb5-2cec4ad006d9 | -4.31752 | -47.7061 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8db87e2c-acc2-32b5-b253-fbb0484696f9 | -4.92567 | -46.73904 | 2024-10-10 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98b50382-5b55-307e-856d-d00c990fe843 | -4.84011 | -46.85884 | 2024-10-10 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5008d3cd-a7c2-34ec-9fcf-111f997c438e | -4.5496 | -46.40851 | 2024-10-10 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04778938-7ea2-3bf7-b674-a07f0b5a4a5a | -4.48095 | -46.59485 | 2024-10-10 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63f6e769-f934-3a9b-9b33-ddff3516ffa6 | -4.47576 | -46.59417 | 2024-10-10 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc9c6e63-b471-313c-8252-40469d3d901c | -4.47523 | -46.59723 | 2024-10-10 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 78f1ca86-1d1a-380f-b861-b402b506f619 | -4.26284 | -47.20093 | 2024-10-10 03:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 594955f8-50fe-3522-97e2-8d95c96148bf | -4.25801 | -47.19679 | 2024-10-10 03:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7dfd000-0813-3416-bc9e-79ad290a5b65 | -4.25745 | -47.20003 | 2024-10-10 03:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 64d3259e-3ea9-3cfe-968a-02b2cf6d5ad5 | -4.93132 | -46.7371 | 2024-10-10 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22dae4ba-46b1-313a-8a65-f67a093281f9 | -4.9262 | -46.73594 | 2024-10-10 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb10c2a3-e72d-35a8-aedc-c4699bdc07a2 | -4.90377 | -46.83599 | 2024-10-10 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb2fd3b0-a15e-3fb9-8d91-f9deae8b1d88 | -4.84922 | -47.52 | 2024-10-10 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6dc5614c-100a-34a8-a4e3-2d0229bfeed6 | -4.84824 | -47.51928 | 2024-10-10 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 902158ee-0f70-31ec-bcb9-631f2ece814c | -4.84041 | -46.86131 | 2024-10-10 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1a83898-df71-3e25-9f95-9f60c402c4ea | -4.83959 | -46.86193 | 2024-10-10 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 312d0d72-cc0c-33a7-aa6e-098d2e6cb651 | -4.83576 | -46.85717 | 2024-10-10 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d715e7b-dd45-3e06-9420-253541d389b7 | -4.8352 | -46.86034 | 2024-10-10 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a4e648b-5a11-33fa-8725-3b677f883271 | -4.83491 | -46.85786 | 2024-10-10 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a90e9ef7-0620-3069-9ef1-9c9953cba9c7 | -4.4856 | -46.59863 | 2024-10-10 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec28a475-29e3-3676-9b96-29bd71ad7de2 | -4.48043 | -46.59787 | 2024-10-10 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b252417-2eec-3d9b-b4e3-38fe848633d9 | -4.27258 | -46.42649 | 2024-10-10 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| f7d0a1e0-adfb-3765-b359-657605986366 | -4.27207 | -46.42948 | 2024-10-10 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1901c8a6-fa4b-3014-8b21-18945126b7aa | -6.54223 | -47.11612 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c00fc5eb-9503-3836-a2e6-5a73c7823895 | -6.53706 | -47.11533 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f56417d-d3cf-386f-8cac-c60921353b14 | -6.53649 | -47.1185 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91b8162a-e674-39ee-896f-534c2dae61b9 | -5.43288 | -47.6862 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7980443e-5d71-3fe5-9c5b-1a787c140389 | -5.53974 | -46.69471 | 2024-10-10 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 248ca21f-f564-360a-820f-ae0d63fe720a | -5.49623 | -46.91265 | 2024-10-10 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9dc7c0f5-51b0-3302-880b-33686909cd20 | -5.49567 | -46.91586 | 2024-10-10 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 544b8002-7b30-3fdf-b58b-df8cb4e7df91 | -5.43349 | -47.68266 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9e7055f-a514-380e-8d1f-d1ff0417d5a8 | -6.41957 | -46.67521 | 2024-10-10 03:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6fbeca66-ab0d-308d-a4bb-2bc45197aa92 | -6.292 | -46.995 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28e097f6-b52e-3c0a-9f14-7ecf1982db77 | -6.28739 | -46.9911 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c17eef22-de01-3c06-8879-ac73f52bcecd | -6.05168 | -46.59853 | 2024-10-10 03:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78a0bd38-8556-31a8-b8de-6f4ac5182298 | -6.05067 | -46.60443 | 2024-10-10 03:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd664883-f96d-34fc-a7f7-11ae34fd00a7 | -6.04618 | -46.60049 | 2024-10-10 03:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e691286-9142-38be-b988-c429820367d1 | -5.84434 | -47.42155 | 2024-10-10 03:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cc21351e-a810-3394-8139-9a12de4b9cdc | -5.83841 | -47.424 | 2024-10-10 03:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f6bca0a6-f807-3a82-bc31-c5e74c7694ea | -5.83568 | -47.41769 | 2024-10-10 03:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 08d0af74-7a77-3a80-b159-a95aff277d1f | -6.29254 | -46.99193 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cb06178-6144-3c9f-b1f2-27936b35d926 | -6.29146 | -46.99812 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bbe5157-cd20-323f-a632-b16833b10573 | -6.05118 | -46.60147 | 2024-10-10 03:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d7d365f-2921-3919-9ca6-e9f5664196db | -6.04668 | -46.59756 | 2024-10-10 03:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d09f113c-df96-3b62-a9bf-db9d0196428a | -6.04064 | -46.60258 | 2024-10-10 03:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49053759-232e-3a8b-8a49-095462a82b21 | -5.84251 | -47.43184 | 2024-10-10 03:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f03bf21e-8de3-307a-8a4e-8d31c844458d | -5.83902 | -47.42061 | 2024-10-10 03:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2509a4f2-9002-35d2-8ee3-dca061e591dd | -5.83781 | -47.4274 | 2024-10-10 03:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ff659552-dfbf-37e2-bb56-1e694c8861c6 | -5.8372 | -47.43085 | 2024-10-10 03:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f2639d5-3e24-35f1-ab6b-b9813befb379 | -5.8351 | -47.4211 | 2024-10-10 03:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c260dfa2-b57e-3957-81e9-e05e5679fe02 | -5.83452 | -47.42451 | 2024-10-10 03:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 812c0372-27c8-3cad-8ecc-75d382ed6efd | -5.83394 | -47.42795 | 2024-10-10 03:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4735d00a-a092-386a-86b6-dd5fd4d8a932 | -5.83246 | -47.42661 | 2024-10-10 03:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c2d756f-1653-3d1b-b457-31e9e136d54d | -7.76906 | -47.03397 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb36f40b-b45b-39f7-ae15-50827631f0b5 | -7.76802 | -47.0398 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7cc07cf-47d2-3a4c-bb09-9eac1da9b1cc | -7.7635 | -47.03606 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b554073-53bd-3a33-a0ef-2b7d44bb2613 | -7.76298 | -47.03897 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 513b8dc5-7394-3fb8-8a25-6707fa4d2657 | -7.49535 | -47.20551 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e60f8a3a-648b-379f-9221-baaf6bd116b7 | -7.49246 | -47.20522 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c86c6dae-6be7-338e-adca-eb8e7b0bb14e | -7.49025 | -47.20459 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5110e7ee-ed97-35ac-912e-007cd49c51ec | -7.44037 | -46.96737 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbb3ca9f-75fb-33ee-92e6-74cefe97779b | -7.24219 | -47.49649 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8efbe25-f6c9-37ee-848d-f3f164ec4db8 | -7.24161 | -47.49968 | 2024-10-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebe0a41a-c96a-3c99-a23f-1f4743b0f4d8 | -7.94941 | -47.7165 | 2024-10-10 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b12c92d-6489-3770-98b2-3b5209a6cf64 | -7.94883 | -47.71969 | 2024-10-10 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd17ee77-7183-3e5f-9d19-8d7f911a1b30 | -7.94418 | -47.71554 | 2024-10-10 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aa549052-a567-3a0f-8145-092d935c05db | -7.08813 | -47.87416 | 2024-10-10 03:55:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e92734d7-1bc4-31be-b7f0-8c2bb9d2c1ca | -7.08279 | -47.87305 | 2024-10-10 03:55:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d93f17bf-d4b0-3260-8a86-023545be6a67 | -6.93158 | -47.72562 | 2024-10-10 03:55:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53c931c3-443e-38da-8fef-7b7745b6b95e | -6.93101 | -47.72888 | 2024-10-10 03:55:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 387109e5-1e97-30af-b706-999b6480cee8 | -6.93044 | -47.73214 | 2024-10-10 03:55:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README49.md)
