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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b409a802-cbca-3770-9ac5-979e1c39c8bc | -6.9414 | -42.907 | 2025-06-14 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 5893c897-0e27-3356-97df-f004175d6961 | -7.2217 | -43.0917 | 2025-06-14 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 4eb9574c-feea-3e9f-b7a2-77fc2a6f64c0 | -11.7969 | -57.3428 | 2025-06-14 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 2d4dff63-c7fb-33e6-9081-14828294e61c | -10.9355 | -56.8322 | 2025-06-14 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 86f4ae7a-674c-3c7e-b513-4a7b450a8ff8 | -14.2121 | -57.4098 | 2025-06-14 00:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 531931a3-1b41-360f-a728-d6f6b311b48b | -7.2214 | -43.1153 | 2025-06-14 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 4f52156e-84fd-33f0-bf14-62986e2004ce | -11.8156 | -57.3612 | 2025-06-14 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 8c877bcb-d294-3eeb-aa4d-dcc47cf67b5d | -6.6112 | -43.8941 | 2025-06-14 00:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 21e4989e-8ef2-36d1-9acf-a26036f3998c | -11.011 | -55.0967 | 2025-06-14 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| bbdd6e34-b7d6-3c42-84d4-3a15e4d407c3 | -15.1119 | -49.6193 | 2025-06-14 00:00:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| e60c099c-b79a-312e-81bd-2e5a43a2588e | -16.1967 | -46.4589 | 2025-06-14 00:00:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 3c416951-33ef-3ab1-8211-9dc8bdfb01fe | -11.8158 | -57.3413 | 2025-06-14 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| c66c1cf0-ad49-3590-af4b-a1916883313c | -6.9602 | -42.9052 | 2025-06-14 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| a1ea04c5-ee5a-31c9-a6b0-03924685534f | -10.9353 | -56.8522 | 2025-06-14 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| fcb8bf07-6417-32b8-ae8b-a3878a4cf2f2 | -9.3929 | -57.5344 | 2025-06-14 00:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 2d7918ff-ff8f-32d2-b0ee-84c4ae703929 | -11.0113 | -55.0764 | 2025-06-14 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 994fcb5b-cedd-30b6-9faa-be5a34839aa9 | -10.9205 | -54.7795 | 2025-06-14 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| ad695fcd-d5ee-314f-963e-75d59447b373 | -7.2403 | -43.1134 | 2025-06-14 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| b4cf0289-8058-366a-8de6-59bf9df46e3b | -9.393 | -57.5147 | 2025-06-14 00:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| b65dc255-19ce-3680-a6d5-e58e344a4179 | -6.9416 | -42.8834 | 2025-06-14 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| f57e3a5f-6365-31ed-9dcc-9459b2799ba1 | -10.9167 | -56.8336 | 2025-06-14 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 96de37f1-a6d6-3671-a780-d68e5fdc790a | -7.2405 | -43.0899 | 2025-06-14 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 31011a35-1de8-39bd-8635-d7a3aa507560 | -13.9062 | -54.6084 | 2025-06-14 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 69946c13-2c6e-3d80-843a-5ffb674e1b10 | -13.887 | -54.6106 | 2025-06-14 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 24d5d9f6-faba-386e-9523-0b6f7e1653bf | -12.6236 | -57.8926 | 2025-06-14 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 7b716f15-7bf6-345b-a27f-b91f5dadbf30 | -6.9605 | -42.8816 | 2025-06-14 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 784d6149-e947-39c0-b80d-314c14df6c17 | -10.65531 | -44.48399 | 2025-06-14 00:01:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 0dc5f126-5edb-3903-993c-e18e65b6beea | -10.80965 | -44.35532 | 2025-06-14 00:01:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f7b9e848-6b9a-39a2-b6d9-c9153542ab9e | -13.03687 | -44.11925 | 2025-06-14 00:01:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| bd80c21e-a803-3da1-a2b3-9a9d8a5b24ad | -12.27321 | -44.61821 | 2025-06-14 00:01:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 7357c647-1658-314d-9725-83aa1743f7e4 | -13.03646 | -44.11395 | 2025-06-14 00:01:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2c734e6d-5493-3fae-8762-eee695847ca9 | -10.64257 | -44.4856 | 2025-06-14 00:01:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 09c75f28-16fa-3ef3-9278-4fe7f92857d4 | -10.65769 | -44.50366 | 2025-06-14 00:01:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 22f8bf47-77a4-381c-81b9-621abb09c309 | -5.91251 | -43.45784 | 2025-06-14 00:03:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cfb5237a-8f17-353e-b962-3ffac34b9a33 | -6.21506 | -43.32993 | 2025-06-14 00:03:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| e858fef8-0c61-3843-8143-38dbfb750fd3 | -7.2417 | -43.09328 | 2025-06-14 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| df1ffa31-e2db-3b4d-984c-3e692557cd1b | -7.21875 | -43.11581 | 2025-06-14 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 44.0 |
| e2addcfa-3151-3493-9aa8-51bcc95cb6ee | -3.77342 | -41.60573 | 2025-06-14 00:03:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 7c32a04f-f5de-3df7-819c-49a4aa7e0b34 | -6.59918 | -43.888 | 2025-06-14 00:03:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| c0863a9f-94fc-36b2-bab5-c7872fda2047 | -5.77522 | -43.47449 | 2025-06-14 00:03:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 527cb2a3-0804-32d7-ab45-9f15b88c6e96 | -6.95316 | -42.90628 | 2025-06-14 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 47.8 |
| 57d260f3-b2d2-318f-93d9-eac28745f6a8 | -7.22953 | -43.1143 | 2025-06-14 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 35.3 |
| 42d4944e-b87e-3fbf-a9d3-7fd8af5e3fdd | -6.95146 | -42.89323 | 2025-06-14 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 152.2 |
| 7555e7b4-a57f-3b0c-8b90-a803fff7950a | -6.60123 | -43.90316 | 2025-06-14 00:03:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| de5011d8-9c3c-334f-beab-7b3d6cbebbd2 | -7.23264 | -43.10817 | 2025-06-14 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 4291b3be-778e-3697-bccd-9efe005ad243 | -7.22014 | -43.0961 | 2025-06-14 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 84a6e6fb-5108-3da5-9fe6-47e4a9fed54c | -7.62256 | -43.65069 | 2025-06-14 00:03:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fa04e27a-4c1c-37a6-ad44-13ffde3d26c1 | -6.68922 | -43.97355 | 2025-06-14 00:03:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 131c2ad3-234d-3e99-b3a0-e69187f6df20 | -5.90166 | -43.4593 | 2025-06-14 00:03:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 699e879a-c630-3f3f-b094-55d6d909efbb | -7.23092 | -43.09467 | 2025-06-14 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 29626759-fa46-3f2e-a5b1-5f169b3a544c | -8.08031 | -43.1083 | 2025-06-14 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.9 |
| 4d28e992-fd73-31ea-a1e2-5ca6b79255d0 | -5.77705 | -43.48817 | 2025-06-14 00:03:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 07838a22-ab17-3128-adc1-6c7556020a2d | -6.61094 | -43.89641 | 2025-06-14 00:03:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| e9eccbb1-56eb-3e3c-ba1d-991824c65211 | -5.50084 | -35.58484 | 2025-06-14 00:03:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 6cd00933-921b-3950-8d97-e2405fdd7331 | -6.60149 | -43.91306 | 2025-06-14 00:03:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 170da508-1358-3bbe-bdcd-d447f1a64783 | -6.96239 | -42.81307 | 2025-06-14 00:03:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| c761e5b2-9797-34ce-bd3f-d1f66bbc55a2 | -6.59954 | -43.8977 | 2025-06-14 00:03:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 3843944d-d0bc-351d-816f-bb80da77c87d | -6.95021 | -42.80172 | 2025-06-14 00:03:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 6bb8d446-225e-32f3-806f-e293531fffb4 | -4.6111 | -38.52896 | 2025-06-14 00:03:00 | TERRA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| e703c78c-e0da-316e-98b0-a4a9a34b89a6 | -8.06936 | -43.10967 | 2025-06-14 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 624acede-b187-3b44-b00c-761669d97412 | -8.08209 | -43.12226 | 2025-06-14 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| bd6f85e1-4389-35b9-9a0e-8c018b897391 | -7.21694 | -43.10225 | 2025-06-14 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.7 |
| 4fba796b-dbe1-3c62-93ad-fd2357be823c | -7.22186 | -43.10967 | 2025-06-14 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.3 |
| 77900aea-b4b0-37eb-b829-70c7d17ad1c4 | -9.39477 | -48.41138 | 2025-06-14 00:03:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 7a6b1270-f469-316b-9ef4-2c348264ede7 | -9.40827 | -48.41659 | 2025-06-14 00:03:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 5bcc263c-da51-3b23-853b-0a0e8c1f9885 | -6.94977 | -42.88029 | 2025-06-14 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| a78e8ca6-855a-3024-a588-b9fac33e6c10 | -7.22771 | -43.10078 | 2025-06-14 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| df4222a7-6832-32cd-b4f9-2c0fcd073afd | -7.24344 | -43.10682 | 2025-06-14 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.6 |
| 220e7b22-ed35-3934-abb5-f1da5874feed | -7.24518 | -43.12038 | 2025-06-14 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 33261540-b952-3c92-833c-f9c80502b198 | -7.6319 | -43.63393 | 2025-06-14 00:03:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| d42f2881-8c32-3984-9d3e-ca1e743a91d8 | -6.2196 | -43.327202 | 2025-06-14 00:05:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd5462f0-ce00-3fec-9983-5d920e8931dd | -10.6505 | -44.500401 | 2025-06-14 00:05:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb9bfa3b-9a47-3040-bb46-30c904a7bc78 | -7.6337 | -43.655499 | 2025-06-14 00:05:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 87e9080b-9765-31f1-9d99-7233129c95a9 | -16.195499 | -46.471699 | 2025-06-14 00:05:00 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 363d7c66-0067-3020-a6d0-65aa25200cd2 | -7.2396 | -43.1171 | 2025-06-14 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 379c65d8-3f37-33d4-961c-00e9f3be8ee2 | -7.2179 | -43.111801 | 2025-06-14 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 89881a7f-45f4-3496-948c-1085f83c1e34 | -10.6477 | -44.487099 | 2025-06-14 00:05:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9018d0f0-df05-32e2-a96e-0e62346187e1 | -6.2119 | -43.339001 | 2025-06-14 00:05:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 995b7da7-8306-36b6-b9c7-9d03930b67c3 | -5.883 | -44.357498 | 2025-06-14 00:05:00 | METOP-C | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3815030e-59ca-34d4-b1cf-a217021ccc2b | -10.6603 | -44.498402 | 2025-06-14 00:05:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 97699936-9913-3498-b98c-203ff250f9c5 | -7.6314 | -43.644901 | 2025-06-14 00:05:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 684bf96a-b1ff-3e60-b88c-b3cd4d9ef16c | -7.6291 | -43.634399 | 2025-06-14 00:05:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ed19b4b1-124d-3c75-ac1d-856b8cde0513 | -8.0784 | -43.111 | 2025-06-14 00:05:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7c75a4ff-7dfb-39e5-b3b4-0ddd7a20d325 | -4.6116 | -38.5327 | 2025-06-14 00:05:00 | METOP-C | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| feebf8ad-89da-3553-af37-0260a88de4e1 | -7.6216 | -43.646999 | 2025-06-14 00:05:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6ff9e64b-67fb-35a1-8e9f-61497e4e1309 | -7.1678 | -43.537998 | 2025-06-14 00:05:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6ac1243b-9248-35a5-a049-ae4f5c08ec7e | -3.7787 | -41.6087 | 2025-06-14 00:05:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7bb2e4e0-3595-373c-bdb9-dc1000041421 | -6.9562 | -42.900398 | 2025-06-14 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c163376e-0661-3f9e-a4a1-eccf30b16cde | -6.9542 | -42.891102 | 2025-06-14 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b554a39e-1773-3a6d-b9cc-e96a52178ac2 | -16.185801 | -46.473598 | 2025-06-14 00:05:00 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3370cd42-a7ce-3388-b5bd-b903ba898686 | -7.6239 | -43.6576 | 2025-06-14 00:05:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 95a59ee7-7cfb-3e55-9c6c-d3f58f16fcff | -7.2298 | -43.119301 | 2025-06-14 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5c37e397-0c49-38cb-b95c-7f367b78758c | -6.9456 | -42.805901 | 2025-06-14 00:05:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 253d3d46-61ea-3f01-8fbc-c41ec424fb9f | -6.9583 | -42.909698 | 2025-06-14 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 42ed6b8a-cfae-32d2-8956-e59766718ca8 | -6.9554 | -42.803799 | 2025-06-14 00:05:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7c7cabd8-6376-3a83-af9e-f35be536c666 | -7.2277 | -43.1096 | 2025-06-14 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 266c4bc5-586c-30f3-9ab6-051040b983df | -5.7703 | -43.474998 | 2025-06-14 00:05:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c752b8b-28b2-3af3-b742-fce7f0b21291 | -10.6575 | -44.4851 | 2025-06-14 00:05:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1e2ea30-1686-3eee-a326-a4ab163d011a | -6.6112 | -43.8965 | 2025-06-14 00:05:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7653183-8aa9-3239-ab70-7a816eba7303 | -9.3919 | -48.410801 | 2025-06-14 00:05:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
