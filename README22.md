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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c9b1958-2f79-3ae0-b22a-ecd610fe1667 | -2.69188 | -45.65889 | 2024-11-23 03:53:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b86f5fb1-7311-39bf-aef4-edbf22a0705e | -6.15185 | -46.68051 | 2024-11-23 03:53:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 468597bb-7d80-3a12-a591-ab70b1c1fc36 | -8.76704 | -38.46872 | 2024-11-23 03:53:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ce4f5370-6528-392a-af46-dd608be97a1c | -2.82292 | -45.16353 | 2024-11-23 03:53:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ede06dc4-7b7e-3189-8752-4f251d515a88 | -2.76513 | -45.93245 | 2024-11-23 03:53:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 26.9 |
| d01a5fac-a6e1-3609-b732-ab17915a5e88 | -8.80414 | -40.39421 | 2024-11-23 03:53:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4fdaeffe-2142-35b1-9b04-d3de9600a225 | -2.18584 | -45.67962 | 2024-11-23 03:53:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a347acb2-d7fd-3488-9fae-8b3c31286e2c | -8.31565 | -35.23179 | 2024-11-23 03:53:00 | NPP-375D | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| caffc2d6-3925-3b83-84cb-fd7ff4fa2f7e | -1.89465 | -46.4339 | 2024-11-23 03:53:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abdceb7f-5948-3a9c-abdf-a72be7d517a5 | -9.81689 | -39.14812 | 2024-11-23 03:53:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bc6d95db-e42d-3c30-a141-5add06c7378d | -6.74396 | -43.2468 | 2024-11-23 03:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cf78b65c-fb7a-3a03-b093-c6f9cb70d911 | -1.79567 | -48.44205 | 2024-11-23 03:53:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| feb238c8-31e3-3231-9f1c-71221f6c18cf | -1.79774 | -45.717 | 2024-11-23 03:53:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5767ffa4-8268-3248-b218-614c960ff96a | -2.4159 | -46.03494 | 2024-11-23 03:53:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df9c78fc-a2a1-3d8d-883d-97914c185e60 | -6.14512 | -46.68887 | 2024-11-23 03:53:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf054cd7-3154-3b67-b2f1-1093577210a5 | -5.57529 | -50.95055 | 2024-11-23 03:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1466d0cf-d17f-38f2-bc6c-14bf6a5ec299 | -8.15544 | -38.24346 | 2024-11-23 03:53:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ae268f6f-8ad0-35f4-8a2d-3fd56c34b3f7 | -6.50218 | -43.86247 | 2024-11-23 03:53:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71aee8cd-ba26-3873-845a-55cb51bdc496 | -7.8319 | -37.3964 | 2024-11-23 03:53:00 | NPP-375D | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5bf3e6b3-c645-3fc0-9a25-e86227d31cc9 | -2.69524 | -46.0983 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b01c67f5-8062-3a54-b310-751fcee56843 | -7.0774 | -49.20923 | 2024-11-23 03:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b51b1e2-56ec-30b6-853e-f27d4027ffee | -2.70825 | -46.24759 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c7274a6-3ac7-3cb8-a701-f97c1301ac24 | -3.2358 | -46.43023 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78701c4d-fb2f-34ac-8bfd-21f26c828d51 | -4.10826 | -42.47481 | 2024-11-23 03:53:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| aa36f911-e859-3a4f-b3a4-079e57ce13f2 | -3.13095 | -45.25318 | 2024-11-23 03:53:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5e8c739-5201-3494-9176-bfdb8e7ab26f | -2.72112 | -45.70306 | 2024-11-23 03:53:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b541aeeb-9aa4-3377-8c28-4aca757727c3 | -2.70456 | -46.27008 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cf9b2ba-6e5e-3e32-8678-bcb5f61a361b | -4.39233 | -40.76328 | 2024-11-23 03:53:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4de01c53-ea4a-3ed5-89eb-23e0c5f6af45 | -8.1497 | -38.24268 | 2024-11-23 03:53:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ba47f68f-6d53-3585-ad12-88ff2629d901 | -2.71406 | -46.27822 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab4a74d5-d41e-332a-ae3f-d93ca93c70d7 | -3.53669 | -45.21806 | 2024-11-23 03:53:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9837b3f3-2f7b-3754-b4dc-4519876d9d45 | -2.67982 | -46.25598 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6334ba73-4cc3-30b2-a29e-9fd41b512346 | -2.71138 | -46.09777 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 585c7bb9-7476-3f9a-bc52-25f79b8c50b0 | -2.75998 | -45.93159 | 2024-11-23 03:53:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8849b5be-412e-3282-8352-bbc23bfe369c | -6.15797 | -46.67566 | 2024-11-23 03:53:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d055209c-97db-3f12-8e75-21db6d9e4dca | -2.18634 | -45.67664 | 2024-11-23 03:53:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57d98523-5a0c-34af-902e-ea3b535e4b71 | -2.71967 | -45.70072 | 2024-11-23 03:53:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22ea5dab-b896-35e6-b24e-b9dbf96661a1 | -4.10912 | -42.46968 | 2024-11-23 03:53:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 564f1ac6-c493-3a0d-82c7-0f0a410b33c5 | -2.70567 | -46.09995 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5d35da9-a1f8-3500-b3c4-8b8f16613061 | -3.27111 | -45.13177 | 2024-11-23 03:53:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55e0c8c5-1f9b-3d1b-975c-2e0253137c92 | -3.84816 | -43.93957 | 2024-11-23 03:53:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c89896c7-bcb5-3a2b-abac-3070d439ce54 | -2.70879 | -46.27736 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 61c835aa-d2fc-393b-8027-ea35995f9555 | -10.58368 | -36.98705 | 2024-11-23 03:53:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b7d515e4-4f92-3919-bfb7-e93aa64d49d9 | -2.69092 | -45.66476 | 2024-11-23 03:53:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2573effd-b77e-3b4c-8cba-c385ad0efdb0 | -6.74454 | -43.24335 | 2024-11-23 03:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 87d4c897-402a-375a-8ca1-cbc9f1a37736 | -2.68454 | -46.26018 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cf64f64-f1ca-38b2-a545-c73cc994f7e2 | -9.73381 | -37.02907 | 2024-11-23 03:53:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 5351c236-5f29-3591-8fee-40d96b118092 | -3.40608 | -46.24537 | 2024-11-23 03:53:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbb0e265-10f9-3efb-b455-e46b0473d5e1 | -6.33016 | -46.0312 | 2024-11-23 03:53:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1080cc56-bbd3-3a22-afd1-2426760a810b | -2.82865 | -45.15897 | 2024-11-23 03:53:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a16ec86-a61f-30ba-aa7d-cff624219611 | -3.84746 | -43.94389 | 2024-11-23 03:53:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8617cd7b-54cb-32c4-acb5-695bea25ce79 | -1.96776 | -48.38541 | 2024-11-23 03:53:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b7a4326-63fe-3532-9192-df155a06bcfb | -2.82596 | -45.15993 | 2024-11-23 03:53:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dad2f447-5ae6-3b75-837c-64af081218d5 | -7.3044 | -39.61877 | 2024-11-23 03:53:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6d7afd20-a1f7-3119-95a6-ee5449bd1d4f | -3.17123 | -45.7267 | 2024-11-23 03:53:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d58f837-8086-3ed9-8ddd-e0eaae01e952 | -3.17075 | -45.72958 | 2024-11-23 03:53:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 924e9452-d439-3a55-8040-c231872f129a | -2.15119 | -50.91504 | 2024-11-23 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f69757e-dac7-3ecc-9f82-dfa933f569fa | -2.70087 | -46.25959 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d48ad0e9-9648-3b78-8d9c-f746c67c6ce7 | -9.37124 | -40.45161 | 2024-11-23 03:53:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1941f4e8-8839-375e-aa0c-ab0ae88d9620 | -3.60139 | -41.67443 | 2024-11-23 03:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ac43d7c1-0899-3fbb-a27d-3c196c3fc019 | -2.69455 | -46.26514 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9080caee-b063-333c-8bcd-289924380fd9 | -5.57398 | -50.95097 | 2024-11-23 03:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aae54c46-de8a-342c-b99c-9bb80fe9f5e7 | -3.84374 | -43.93888 | 2024-11-23 03:53:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aead6cf2-d432-396e-8d1c-6ed9b45058f4 | -8.52568 | -37.06197 | 2024-11-23 03:53:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bcb61246-a9e5-3c30-a38d-1a320cddfb7f | -2.82109 | -45.15909 | 2024-11-23 03:53:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 90887fc9-cea5-3e0f-99df-caa842c399af | -2.41641 | -46.03183 | 2024-11-23 03:53:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ce36b32-afb9-3194-bdc9-7ed40ea6b0cb | -7.75112 | -38.36504 | 2024-11-23 03:53:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ce1c5cbb-95a6-332b-94e1-7095272d179c | -6.15287 | -46.67469 | 2024-11-23 03:53:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c7776c5-01c6-3eb7-a6c5-a1f7d29938da | -2.18376 | -45.67899 | 2024-11-23 03:53:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6a74c78-e7ce-3f4a-a1c0-de53992ae1a7 | -2.48028 | -46.03672 | 2024-11-23 03:53:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 231a1441-8491-3058-b515-bddf5c522bd3 | -2.69877 | -46.27241 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea046fd9-eca3-375e-b0f0-ae695d4215cc | -5.97085 | -46.30457 | 2024-11-23 03:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9cbae09e-f7ba-3cab-a216-76fefe7023e0 | -2.6914 | -45.66183 | 2024-11-23 03:53:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31700513-8794-3b76-b62b-82fa9b7de7a9 | -9.72635 | -37.03178 | 2024-11-23 03:53:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e7253725-93e1-31da-a6a8-851d9e88a60d | -2.69053 | -46.09441 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb70fad3-5dd2-3766-bb58-ee8443fbef80 | -8.66925 | -40.40695 | 2024-11-23 03:53:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 19b0d506-814e-31ce-bb73-81f08457ea2b | -2.69982 | -46.266 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f53f1dda-7ade-3ba3-afac-99fb0c1f29ac | -7.58511 | -40.00317 | 2024-11-23 03:53:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6d3bd62f-22b5-3a8a-be76-f1fc329de60b | -4.1075 | -42.46755 | 2024-11-23 03:53:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 45fd4b9b-56ed-3df4-a2b2-75ba9bf7bc1e | -1.96819 | -48.38651 | 2024-11-23 03:53:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e243aa56-7eee-3b90-9c74-635776c2176d | -9.81634 | -39.15161 | 2024-11-23 03:53:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2389aed5-c2b5-354d-a59d-f6452aeb342e | -6.33231 | -46.03313 | 2024-11-23 03:53:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0f925f3f-77a4-3b11-9267-21082fa20334 | -8.61767 | -40.53155 | 2024-11-23 03:53:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a00d9455-ca3d-3b05-818e-e640f7e65fe8 | -2.66544 | -46.1482 | 2024-11-23 03:53:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a251e47-8076-3d6a-a034-a37fe9453ccd | -2.18534 | -45.68258 | 2024-11-23 03:53:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f267892-d20e-30f7-a4b7-c7bd647a381a | -2.13591 | -46.40347 | 2024-11-23 03:53:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2054f946-2f86-34d0-87b1-2fba7aca5c95 | -6.93881 | -42.82666 | 2024-11-23 03:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 775e0daf-4fb1-3314-949d-ff8acc426ba4 | -3.38636 | -45.29401 | 2024-11-23 03:53:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47103303-954f-3436-97bc-7f74e1134163 | -10.58022 | -36.9865 | 2024-11-23 03:53:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ff41ac16-eed9-313d-b717-f12645d87793 | -7.75167 | -38.36156 | 2024-11-23 03:53:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e5d3e6b5-0c8e-332c-af65-4023d8807290 | -3.14947 | -44.48517 | 2024-11-23 03:53:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfc2df4f-f2d2-3485-9d97-6d94dafe4a44 | -6.14055 | -46.68483 | 2024-11-23 03:53:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| af414e0f-548e-3b63-9af8-749b56b76f2f | -2.66906 | -46.15869 | 2024-11-23 03:53:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f1e0d49-9837-3fc8-95ed-55bedd9a9d5e | -6.94271 | -42.82736 | 2024-11-23 03:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5d0828f8-4c40-3eac-a5ca-baee1c5c7201 | -4.1131 | -42.47034 | 2024-11-23 03:53:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c5ad159f-09c3-3d8a-b694-b94fad5783d6 | -3.60342 | -41.67796 | 2024-11-23 03:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8df68dc0-0f30-3966-babb-fea9861bd775 | -7.05267 | -40.41656 | 2024-11-23 03:53:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5139e0cc-fd55-3351-ab0c-e1f7892a4c1d | -6.93736 | -41.72615 | 2024-11-23 03:53:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 61b263f0-ea67-3996-aa8b-569502862f4e | -2.08699 | -46.28328 | 2024-11-23 03:53:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0bb6d97-c3f6-3455-b4d1-5b5f71ef0b30 | -3.95432 | -41.49455 | 2024-11-23 03:53:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README23.md)
