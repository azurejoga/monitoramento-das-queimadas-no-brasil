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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8b4d878-abf8-3cda-b3fd-6f40aa6d73c0 | -14.38382 | -45.99904 | 2025-10-10 04:02:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42141e33-39bf-32bc-ba6b-86298e592e3f | -14.72623 | -48.36306 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69f83c62-ed10-37f7-b4cd-6c5ea515751d | -16.74346 | -43.97235 | 2025-10-10 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4498910e-c1c1-3ee4-b53c-5052f4640b65 | -14.87743 | -48.23704 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 824a4f4f-a803-3ef4-9a62-ab49c6349e3e | -11.8589 | -44.9161 | 2025-10-10 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b788d97c-15c1-3334-96ab-f947df69ed0c | -15.12228 | -48.71475 | 2025-10-10 04:02:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d2167f56-d619-314f-b350-d62d0d921ab6 | -11.97077 | -45.21155 | 2025-10-10 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a04cb800-e262-333a-99c5-b8a898e5c383 | -13.53576 | -43.0116 | 2025-10-10 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a9e6a23b-f438-3b85-9019-6812e1748bf9 | -13.526 | -48.12016 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 526c0863-000a-3601-a33d-5d15df00cbac | -14.57468 | -47.45868 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cc6b07af-ca52-3e51-bd89-eebe7b9c1892 | -15.75054 | -48.99162 | 2025-10-10 04:02:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58867138-a385-3b12-8dad-2ff79cc825e5 | -12.66051 | -43.42636 | 2025-10-10 04:02:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b6c5324-346b-3d12-8bb8-662fe3367414 | -10.93123 | -42.84238 | 2025-10-10 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 85f6ab7d-0cc2-397c-9a89-30400c76f571 | -17.66084 | -44.44917 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 672672c4-9608-333d-9dbc-2586bbb1913e | -12.77793 | -45.78188 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 585d139a-f467-3e18-853a-d4b2eaef02ea | -13.29716 | -47.13362 | 2025-10-10 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0663d4d1-e83e-3917-9bb7-4f0d2f7cbb6b | -13.37628 | -47.75188 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d30ff6ef-0485-3a42-bcb8-f047bf60b305 | -14.08283 | -44.53556 | 2025-10-10 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf2e9c49-e220-3fb1-af43-45089adeb1d9 | -15.74694 | -48.98587 | 2025-10-10 04:02:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96749400-874d-3fb1-8bff-b4e5ca729fdf | -15.40683 | -47.99809 | 2025-10-10 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4fdd6bb6-08ba-3bec-9d91-036ca2ff86c7 | -15.57102 | -44.4257 | 2025-10-10 04:02:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9a0ddd16-5560-3b3a-8c4c-6d7e8d5bcb7d | -15.42496 | -44.27774 | 2025-10-10 04:02:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 01433bee-e5d3-3afc-a408-3057e1221f11 | -18.04957 | -44.9802 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dc237e70-eb95-32c6-a33c-cd12503016ed | -13.4149 | -47.25396 | 2025-10-10 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5845ae27-145a-3f37-96c5-b338dbb5d55a | -13.83413 | -45.80515 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 993f8505-4cce-3c17-8234-d65bcc2f1a26 | -13.38715 | -44.22919 | 2025-10-10 04:02:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a6e58d3-9c8f-3197-a5c1-dabcc202a2c5 | -17.93295 | -44.08252 | 2025-10-10 04:02:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cc290782-59bf-303f-b4ae-b9d7ee1e569e | -13.04657 | -46.80509 | 2025-10-10 04:02:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a79db4ab-c211-3e2b-8c06-d3461d568ffa | -16.28008 | -47.1663 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0495389f-ee99-3ff6-a1a2-f741faf7848e | -14.93393 | -46.76006 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43cade19-aa71-3834-94e8-5e243d5a10c6 | -16.0534 | -48.08108 | 2025-10-10 04:02:00 | NOAA-20 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8aee7359-5e20-3f67-bcb8-a9f6ab95a43b | -14.9435 | -46.77533 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bea178de-cd7c-3847-a696-97fe453ebbd1 | -14.37912 | -46.00327 | 2025-10-10 04:02:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f3980c6-a4f8-3262-98f7-89d59d253ac8 | -15.35711 | -44.16029 | 2025-10-10 04:02:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fe7e1e08-41b0-38f5-9ff4-a23246ce78ac | -16.26946 | -47.15671 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4335688c-858a-378c-82d6-bfb9c04283c7 | -16.53999 | -48.89688 | 2025-10-10 04:02:00 | NOAA-20 | LEOPOLDO DE BULHÕES | GOIÁS | Brasil | 5212303 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf2f580a-114b-3011-8aa0-237bf4183c7e | -14.92533 | -46.78462 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a0dc13e-f19e-3fe7-8fa1-dc82bf338f2e | -14.57048 | -47.45801 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 182a2472-f850-3d4b-b3e8-1820ff606b9b | -14.91939 | -46.79454 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8295675-f2cc-3bae-81e0-b8160506e2cc | -18.02173 | -45.01727 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3258c464-bf03-3348-82c1-c733bdb5cd6f | -14.87623 | -48.21945 | 2025-10-10 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| af41f391-b7e5-3440-bb69-412b87a09f5c | -14.87659 | -48.24151 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0770da92-2f5f-3372-b0b2-e76ec96110d3 | -13.29222 | -48.48993 | 2025-10-10 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01fb37d3-c8c8-38d7-b152-e302d76acfea | -14.84258 | -48.46919 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fbd5283-d20c-3850-b5ab-e99efdceb472 | -14.89485 | -47.228 | 2025-10-10 04:02:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2031b029-34e1-3ffc-95cc-968c2293154f | -18.01754 | -45.02075 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| bbe2de34-69c4-3b1f-9fda-45d74cc7296f | -13.84473 | -45.85754 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b5fb143-e4db-30a0-8af6-165a6726668a | -13.82608 | -45.78362 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 324597ac-2368-3878-8602-6bafa7168f0d | -15.31734 | -43.86831 | 2025-10-10 04:02:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 193f9fa1-2b81-3185-8bea-c6ff065fb30a | -13.62909 | -47.63177 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c99d688-e737-34dd-9749-2292009f9806 | -14.93202 | -46.77055 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f9bb1aa9-2ff8-30b4-a2fb-ca173b6b76d7 | -18.0704 | -44.971 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a8709d4-ee2e-334b-babb-e493bb22d6ea | -12.63557 | -45.05375 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 49ff0fd5-0fa2-3fc0-80e6-d1544e2b625c | -12.92707 | -45.05694 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 402674e4-b5c7-36de-b65d-f9cfb0e67219 | -15.42844 | -44.27837 | 2025-10-10 04:02:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ba3b303d-f831-3a7a-89fe-7c8a9071c31c | -14.11946 | -42.76979 | 2025-10-10 04:02:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 954c54fd-279e-390d-b2a6-306c8ca29722 | -15.46962 | -47.98422 | 2025-10-10 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd7f0be3-bd58-3e92-a61e-cdfeb148386d | -16.28993 | -45.24659 | 2025-10-10 04:02:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d40ed7b-5a6f-3c03-9840-513a6d0deb29 | -12.57861 | -43.85806 | 2025-10-10 04:02:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38d4d0b6-8483-3b1c-917b-be971ec8a2af | -13.29772 | -48.48574 | 2025-10-10 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 416e60ba-0031-3026-808f-f360f3fc3a94 | -16.29873 | -47.15471 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ce3cdb1-525b-3046-bea7-bba80b790664 | -14.38297 | -46.00396 | 2025-10-10 04:02:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 765f5f7b-2e1a-3beb-b2f3-1ff1065f9f5f | -15.56753 | -44.42507 | 2025-10-10 04:02:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 60b066f0-2b32-3486-93b0-36c1bfae19d9 | -13.3132 | -47.99567 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 92e1fda7-87f5-397c-a00d-1d8455456feb | -15.00818 | -46.28382 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| eb12964e-8f9a-371b-8225-bbdaa50a2d98 | -17.94711 | -45.03247 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f6b831e-9b9a-3d83-a11e-f374090a5f69 | -15.2227 | -42.35832 | 2025-10-10 04:02:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cfb34682-aef2-3f7a-b335-9dbfac9be873 | -13.01675 | -41.4267 | 2025-10-10 04:02:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| cd7ca001-d0a5-3daa-8970-da3931130f50 | -13.33254 | -47.32365 | 2025-10-10 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b36c5376-f17c-3950-9f5b-cfef5b73388b | -12.37344 | -46.49277 | 2025-10-10 04:02:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c347f957-f458-36ae-b33b-977cfea0bf52 | -14.89953 | -46.85781 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f104121d-766a-3010-b7e0-31db87dc127e | -12.61453 | -45.0642 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64a210f2-c059-3312-8155-28e39010dbb9 | -13.82523 | -45.78849 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7094fd7-b3d2-3e13-ab38-252e77c16740 | -11.09524 | -41.05568 | 2025-10-10 04:02:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 2d960087-10f1-3a07-8555-7210ed9ed768 | -15.46528 | -48.53857 | 2025-10-10 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a12a3aba-593e-38af-ac5e-1808e73f4f00 | -13.32891 | -47.74022 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d90c3d57-dac1-379a-b3e4-4e591db7fe18 | -13.35445 | -47.6031 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 94ab6ae4-5b32-3cf7-a56b-bc7c1a1809a2 | -12.10028 | -45.00169 | 2025-10-10 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f140a4ef-d4ca-31f9-b083-7ec89a222587 | -17.24519 | -46.94394 | 2025-10-10 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 240404d1-8b7c-37cf-8ac9-9a301d765762 | -15.55255 | -45.29415 | 2025-10-10 04:02:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4103358-19c9-3b4d-8fd1-ec69412d4e12 | -13.3632 | -47.7496 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b65d2807-bd88-3c95-9480-2691ea450672 | -11.71904 | -44.29251 | 2025-10-10 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a85a78d-806e-3500-825f-4dc37c66d5d5 | -17.93084 | -45.01767 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 27993432-be9c-349b-8aca-dbc2f4eba842 | -11.63181 | -47.53197 | 2025-10-10 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fde0d921-8190-3600-9607-497747c07f80 | -13.35622 | -47.21741 | 2025-10-10 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37c942d2-d3ce-30d4-a4fc-d3ba58c7a36b | -15.82343 | -43.78223 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 905e5054-d160-32da-9dde-0f0d6e63eae9 | -13.06389 | -43.84328 | 2025-10-10 04:02:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a1813f03-564f-3fe2-bb10-99b15f6a7cc1 | -14.91169 | -49.10361 | 2025-10-10 04:02:00 | NOAA-20 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 093b7022-ce60-3924-b558-aff2623f4e9c | -15.46482 | -48.53576 | 2025-10-10 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ff11e66-4765-3df3-9835-25aa0c74fd39 | -14.9475 | -46.77601 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f5616fe-b025-3c5e-82b6-4ca36335b8cf | -15.06627 | -46.6085 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5cfe4355-6cd1-3b0e-9893-0a6dcaf3880b | -13.88104 | -44.24695 | 2025-10-10 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df968d21-2408-38d1-8616-77cbb4b2e870 | -11.85759 | -44.91878 | 2025-10-10 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42a04454-6635-3d85-9ee5-ad8af7d0e8bb | -17.92946 | -45.02581 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 228f7a38-9f83-3fc7-b83b-0dd0c028303f | -17.20806 | -47.65678 | 2025-10-10 04:02:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cf167ee8-8620-3866-9962-110e1f930ae8 | -13.31799 | -48.47751 | 2025-10-10 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78e36e4f-8d6b-33ae-8b62-26653fab8407 | -17.94228 | -45.0188 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79d43697-36b5-331a-8c14-4b4465cdc505 | -15.19942 | -43.73484 | 2025-10-10 04:02:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aeda4b4c-df1b-3fec-a5e5-f6652f21a6af | -17.38538 | -46.65997 | 2025-10-10 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee2e02fd-ff46-3ca8-a1c8-7c354355b23d | -13.41002 | -47.25603 | 2025-10-10 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README32.md)
