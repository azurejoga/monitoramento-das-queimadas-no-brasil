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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3529e30-e872-3e7f-8abf-c6ada89dfadb | -12.44959 | -47.53005 | 2024-10-06 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93a367e3-1176-340f-85eb-0a9704b11cfa | -12.42363 | -47.05881 | 2024-10-06 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09ba0350-65d3-3587-a919-cdcaa5a6c092 | -12.42305 | -47.06241 | 2024-10-06 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 95d74336-b50b-3910-a9d3-44fd46006277 | -12.42087 | -47.05466 | 2024-10-06 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c2106fc-a5a5-395c-bdb5-94db4eb63d88 | -12.42029 | -47.05825 | 2024-10-06 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40b53c65-b4ce-36ee-8647-50c2a07b9e70 | -12.41971 | -47.06185 | 2024-10-06 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9a77ab98-aed5-3038-9bc0-f6c0eaee5ee2 | -12.41753 | -47.0541 | 2024-10-06 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8fe51857-3a4b-3f23-a02c-6d3cd1f54b7a | -13.60736 | -48.13477 | 2024-10-06 04:19:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e9c35b7-61ae-34d9-82af-154823b253e1 | -13.59523 | -48.1445 | 2024-10-06 04:19:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78815e99-1782-31cd-b20d-387b5e8c2017 | -13.59338 | -48.11341 | 2024-10-06 04:19:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a154cc3-d310-3028-9716-5b575b2b023a | -13.59182 | -48.14392 | 2024-10-06 04:19:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a28145e-e836-3d78-9328-bc4d634a0dca | -13.58841 | -48.14335 | 2024-10-06 04:19:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ccc2431-83a5-3153-800f-23164f808656 | -13.585 | -48.14279 | 2024-10-06 04:19:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 867dd2eb-8635-3ee4-9398-77ab2671903d | -12.98053 | -47.65188 | 2024-10-06 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 079be257-7dc4-35a0-b23e-f25850635423 | -12.97497 | -47.64338 | 2024-10-06 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 968abde1-e695-3c18-bd6d-ed0583b09777 | -12.971 | -47.64651 | 2024-10-06 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7521e0f-eb90-385d-b4da-4dd328c8c48a | -14.52595 | -46.93795 | 2024-10-06 04:19:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3adb2ff-1af1-3784-afaf-a9c42a0bf015 | -15.19025 | -47.50161 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26765e61-c5ae-3500-8632-a37296726d83 | -14.03125 | -47.27012 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 255f96e9-7315-3cc2-aa59-449e496d4e4e | -14.0301 | -47.27722 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0930ed0-0af4-3486-925e-126e33f7b4a4 | -14.02953 | -47.28083 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b12141b4-1cbc-30c6-ae80-af7d26074a06 | -14.02894 | -47.28454 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb5ee4ab-b8e6-34ca-8e1f-623ecd91cb51 | -14.02792 | -47.26951 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d43c091-fd10-3f84-95af-00581edb0a4e | -14.0262 | -47.28025 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a036cbe4-45a9-3481-b774-0fccaeccbf49 | -14.02561 | -47.28396 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64d0c03d-fc48-3e3d-a994-d5f4a49a441a | -14.02287 | -47.27967 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8e79f58-e0c6-3ffb-b071-fbb73d2df73e | -14.01954 | -47.27912 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6789a42-80f7-317a-9e88-2d6909b3a7cc | -14.01621 | -47.27858 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bec8f34-e9ca-3343-9009-44abe74f361b | -15.18968 | -47.50518 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e513799-1377-319f-a859-e97ad16fe1f8 | -15.18853 | -47.51229 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96018db8-a69c-33de-873e-0c2d92ea6b88 | -15.18635 | -47.50465 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a036946-b5dc-3774-9640-5e2130d0c765 | -15.16182 | -47.08434 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6173d5ba-4e3c-3e9d-bc60-053b6b7d193e | -15.15576 | -47.07961 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31c06955-85fc-39fc-87bc-d90ef7056b0d | -15.24643 | -47.14965 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a30559bd-6f3a-398e-a379-4a7741843c9f | -15.20529 | -47.49311 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29845a16-a64f-348e-a56c-2a5f4970e76d | -15.20472 | -47.49668 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f8532ab-e3a1-319a-a7e2-de987641d0c3 | -15.1891 | -47.50874 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 565928fd-d547-3396-9395-5405240421cb | -15.16238 | -47.08074 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2aa0d548-1087-3786-ad9e-1f76560ba7f7 | -15.15907 | -47.08017 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89354d41-a939-3990-9fa3-c236c7c992fa | -15.12812 | -47.08232 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19b52701-1547-3a04-9e30-ed8ac10580d7 | -15.12424 | -47.08532 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d79d4769-fe9a-3c24-a8de-fbcfab87b09f | -15.12093 | -47.08476 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d1e0832-bd73-3209-b847-e608088bb609 | -14.00523 | -47.93298 | 2024-10-06 04:19:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92622848-cf31-3de2-b5bc-d7da7aa4daf7 | -13.90683 | -48.06192 | 2024-10-06 04:19:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6548d706-f02f-39e2-b486-f6e71e5f5d2d | -13.90623 | -48.06565 | 2024-10-06 04:19:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cccc1892-077d-3a85-b1fd-299486f96c4b | -15.15245 | -47.07905 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93bf9bda-a8b2-3648-b3ad-3ac32497cd50 | -15.11317 | -47.0908 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6240ca87-253e-3585-9293-9286d10cc42b | -15.10985 | -47.09024 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b0edb38-235b-3103-9ad2-2677e44b24ff | -15.12755 | -47.08589 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3138b995-a6e4-3bab-8feb-1652380aa730 | -15.11705 | -47.08778 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 565340ff-e05b-3e52-9373-69cbca42e74e | -15.10597 | -47.09326 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82cf8369-510d-37a7-a821-5c997e3bc50d | -15.43964 | -47.70319 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 34fcc44a-9559-3f56-bcb7-d5bf648a3f35 | -15.41572 | -47.70277 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35027c76-9caa-38e5-bb97-9d1dee7774da | -15.40417 | -47.68953 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bc36234-ef80-3c8c-898f-1bed3a540fef | -15.38675 | -47.41952 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2de3198-92c1-3d51-b634-4dd8989b827b | -15.26031 | -47.48772 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7b5ab61-ff83-3cdb-8693-e74526a225f3 | -15.15517 | -48.05074 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 484ac602-837a-3ff0-bdd4-c031c62166fd | -15.43441 | -47.42004 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68e88ced-805b-3348-a988-b1cdc174faa2 | -15.41906 | -47.70335 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab692ef1-a1d9-329c-bfdb-f4b7e69e684d | -15.41514 | -47.70639 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be9c0e54-aba5-3b45-8137-37adaed2feff | -15.38733 | -47.41594 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de807eed-d1fb-3e6e-a24a-3b68092c345f | -15.18538 | -48.4426 | 2024-10-06 04:19:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0fd8bf0f-dbfd-3b11-b209-1fd3a38f83c7 | -15.15578 | -48.047 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7421ec36-5f07-3ea8-b226-1e43ee72393d | -16.20494 | -48.71006 | 2024-10-06 04:19:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8979b3da-b9ab-3922-8c83-35b2c033e095 | -16.20447 | -48.71136 | 2024-10-06 04:19:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e321ac6-0962-3015-9cac-697ddb29dc86 | -16.2043 | -48.71388 | 2024-10-06 04:19:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b1beb2e-3220-3e18-9a83-75a6b27ea2e4 | -15.43684 | -47.42422 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2f6de3a-b5a6-3e6c-8c37-ec4c94281a76 | -15.43591 | -47.68393 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e54ec441-f8ad-32eb-b48f-4fd84859b429 | -15.43573 | -47.70622 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb0ec6ac-85c9-3dde-9b29-12f28fb8dc58 | -15.3918 | -47.40931 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e298765-bef1-340a-a2a0-eb62d3622056 | -15.384 | -47.41539 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df3d7b92-cc09-38e4-bc98-b1533b7d6a9e | -15.37678 | -47.41789 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d73b9a81-9ef5-3cfc-b473-63432c182140 | -15.2697 | -47.49304 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 278d8486-d1a5-307e-9ffe-e17e0a1ef7dd | -15.2564 | -47.49072 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95def1df-263a-345c-a1f4-f70da6a78ca6 | -15.18121 | -48.08196 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f2d0170-c1c8-3bc6-b1dc-485643996362 | -15.16037 | -48.04015 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f457435-f324-3f0e-aced-8cba348ca095 | -15.15976 | -48.04387 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e189d615-f956-3f05-8db0-11f2910dc74b | -15.15639 | -48.04329 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9207548d-1bdb-3dff-8c4d-dff22e4652e5 | -15.5682 | -47.85612 | 2024-10-06 04:19:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c32de6d-c0d3-3575-bc48-be261941c8bb | -15.43924 | -47.6845 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9f880a4-91b7-3244-821a-d85ec27eebdd | -15.43532 | -47.68755 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45ed67ca-896d-3530-aa08-b306b4b9c25f | -15.43181 | -47.70926 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2509f18f-24eb-3395-acf4-4edf8cc925df | -15.3879 | -47.41235 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd0c2d2f-c575-34ef-8556-8f9134d5d785 | -15.26305 | -47.49186 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b32285d-a6eb-3dbb-94e4-766ff49d5a5a | -15.25973 | -47.49129 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29217896-0459-3bf0-aee7-7a405fa9b809 | -15.25756 | -47.48359 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c4ca111-2eb7-3005-91dc-720c0b4e202e | -15.25423 | -47.48303 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a4d37b7-1ed4-3447-a86e-6c52cef2b022 | -15.18518 | -48.07884 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a78d2c6-c1ad-3dcc-b28c-3e3f3e26eb8c | -15.16709 | -48.04131 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7900a61-61a5-3bf6-8442-cdb11b4493d3 | -15.16373 | -48.04073 | 2024-10-06 04:19:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7240107-4989-3085-af6d-83153d59b5b1 | -2.74361 | -46.79661 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bfb0c09-59a5-32ad-9946-fd0e5ab3f163 | -2.74003 | -46.79603 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70df4538-18d1-3a31-929d-aa1b7092be6f | -2.73937 | -46.80011 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37c5a221-c26b-3d46-9936-5db67c7c5c6c | -2.73815 | -46.71657 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f07beaaf-8ec3-37ec-865f-d72cb9fa566a | -2.73514 | -46.80362 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bf86b27-0427-328c-8239-34fd2ebbfdf2 | -2.73156 | -46.80304 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fe394c1-2a25-364c-9e16-4e056c213ade | -2.7309 | -46.80712 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4971381-f861-3bb8-8bdf-bded4af9e902 | -2.72667 | -46.81061 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ad9a660-ecf8-3e9e-83cf-7b6bc8edc11e | -2.72309 | -46.81002 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a44b4b4-6c0e-3077-ac12-1121200c7bd5 | -2.72243 | -46.81409 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README73.md)
