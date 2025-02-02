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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7056b6d5-fae5-329a-9310-e1e349cca3eb | -19.78735 | -55.33912 | 2025-02-02 04:42:00 | NOAA-21 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41f1e174-4c20-3ec7-b2a4-6521f1e255dd | -18.54982 | -39.94449 | 2025-02-02 04:42:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 3b16ca3e-9459-306c-ae73-c8cb7ec46eb5 | -19.79085 | -55.33986 | 2025-02-02 04:42:00 | NOAA-21 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23622ca4-df56-3921-a6a4-7b85d67e2338 | -19.59303 | -55.30491 | 2025-02-02 04:42:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05002486-887e-33bc-90e5-c38b72209f65 | -19.02239 | -57.62292 | 2025-02-02 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1b0ae3d5-fe90-3665-8651-a64430a0c436 | -18.54678 | -39.9434 | 2025-02-02 04:42:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| fa477fac-fd81-34b5-96bf-21e9ee83a67f | -19.78197 | -56.01306 | 2025-02-02 04:42:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 12ecb6bf-2ef2-35b6-b30c-ea1916285755 | -19.79435 | -55.34063 | 2025-02-02 04:42:00 | NOAA-21 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39d29c91-c839-32b0-bff8-f7b4574b156c | -20.47922 | -53.67658 | 2025-02-02 04:42:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa41aff6-8bae-3ac1-acb3-7b27a62913ef | -19.79508 | -55.33646 | 2025-02-02 04:42:00 | NOAA-21 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc11e9b8-2689-37b6-ad9e-5506eee88257 | -18.55032 | -39.93924 | 2025-02-02 04:42:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 5587f672-0231-30b7-b83a-ae0e67689b6d | -21.30098 | -55.9057 | 2025-02-02 04:44:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39c56470-2b4b-3adf-a9f3-76e0a4fe6f97 | -22.53914 | -48.81222 | 2025-02-02 04:44:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 415583ff-4224-3fe4-ba4d-6bf79eae27a9 | -29.73995 | -51.26391 | 2025-02-02 04:46:00 | NOAA-21 | PORTÃO | RIO GRANDE DO SUL | Brasil | 4314803 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 120a2a6b-1bd7-30d6-a8d7-6967652fdfb6 | -30.1967 | -55.2792 | 2025-02-02 04:46:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| 7d74bc64-1161-3ddb-80eb-72c3ddaaee46 | -30.19277 | -55.28249 | 2025-02-02 04:46:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| ca4f4caa-3aa8-363f-a4b1-88cd917bf746 | -29.88273 | -54.80338 | 2025-02-02 04:46:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 81cb30d9-498d-3fe8-8500-d57ce49c6ef6 | 4.19754 | -60.94949 | 2025-02-02 05:01:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6a5d5ce-e857-3a5c-8a40-67726ff78705 | 4.60543 | -60.70404 | 2025-02-02 05:01:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 789949f3-6d43-3746-ba26-10580f46e9ae | 4.30726 | -60.60371 | 2025-02-02 05:01:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c73544d2-bfe4-38ad-9240-ef68ab6dc73b | 3.72696 | -60.49564 | 2025-02-02 05:01:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 87072bed-299f-3883-b862-a3bd04917ff3 | 3.92681 | -59.72879 | 2025-02-02 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bed6f10-1cd4-3aed-86da-c1ca425e00c7 | 3.73154 | -60.49495 | 2025-02-02 05:01:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff489130-8061-398c-8866-17fecd4b1500 | 4.61019 | -60.7037 | 2025-02-02 05:01:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83a8106a-27cc-3806-bb39-b83dd9fe9bfd | 4.19279 | -60.95025 | 2025-02-02 05:01:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f3ebb08-796f-3890-b0a1-241710a10330 | 1.94804 | -60.84037 | 2025-02-02 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5e1a86bd-d5e1-3e74-aec3-0dd538be4253 | 3.93117 | -59.72811 | 2025-02-02 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d2ebc6e-33d9-30ff-a702-fed223c39e7b | 3.9262 | -59.72463 | 2025-02-02 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79efd060-d897-390b-a603-62230f26d436 | 1.31675 | -60.42469 | 2025-02-02 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf17c1e7-de03-3280-9b34-b827e2a989fb | 1.94273 | -60.38546 | 2025-02-02 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f447a34f-ccc5-3732-a1a2-16b132d9982e | 1.94874 | -60.84499 | 2025-02-02 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1af11984-cd98-326d-a167-c13031177636 | 1.7175 | -60.32095 | 2025-02-02 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4862a6a5-0e00-3a9e-b011-591c509ece13 | 1.94348 | -60.84111 | 2025-02-02 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4a1ee2c-baaf-3afb-a428-0c59c666ca6f | 1.31742 | -60.42894 | 2025-02-02 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b415850-6901-310b-a25e-27ec3e66a355 | 1.94735 | -60.83577 | 2025-02-02 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 717143cb-74c3-3526-9e00-5b67a0db0ff0 | 3.50161 | -60.79794 | 2025-02-02 05:01:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 239cc18a-9257-319d-ad6b-9379810af824 | 1.93833 | -60.38627 | 2025-02-02 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a8f7149-7357-3662-8b51-80b639fda34e | 2.45391 | -61.31758 | 2025-02-02 05:01:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4c74e219-ad7b-39cd-8e20-78fa86926a69 | 3.54938 | -60.37165 | 2025-02-02 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09947efa-1aa7-3fa0-a5cd-2f6e35565d54 | 3.93056 | -59.72397 | 2025-02-02 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e1aef32d-241c-3ca0-9a98-6a818c9e8e90 | 4.31188 | -60.60276 | 2025-02-02 05:01:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a1cca399-80d1-3420-8902-35fd053cff76 | 4.59147 | -60.71814 | 2025-02-02 05:01:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 758c450f-67d3-3c8a-b848-70835780cdb8 | -11.90339 | -63.87964 | 2025-02-02 05:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c470a3e-9ea6-3c39-a57f-0cea8b714de0 | -11.88968 | -64.00396 | 2025-02-02 05:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b21bd792-a839-3b8d-ad1c-5befbea88a56 | -19.79064 | -55.34169 | 2025-02-02 05:08:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7db27cd-5b10-3fa4-862c-9a4d6fc4db8c | -19.79127 | -55.337 | 2025-02-02 05:08:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62542f62-6591-3579-b4c8-53597600bc4b | -19.0224 | -57.62125 | 2025-02-02 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e662044e-b0df-304e-a60a-e8e6a5d501cf | -19.11708 | -56.22908 | 2025-02-02 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| bd69411a-25a0-3cdb-8337-5a0a8ee19f82 | -20.54634 | -55.83989 | 2025-02-02 05:08:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17ba5777-95f7-3a2b-bfc2-8ac145ed1fc8 | -19.795 | -55.33746 | 2025-02-02 05:08:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86ed699a-941d-38ad-8f91-b7202a181918 | -12.40298 | -63.99479 | 2025-02-02 05:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c176a4e-add8-37da-a770-3f789c6ab28a | -19.11579 | -56.23134 | 2025-02-02 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fc8a1035-1708-3255-b2c3-19e66e31e536 | -19.11932 | -56.2319 | 2025-02-02 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 324fe413-7b23-3411-a860-5204784735cb | -19.78691 | -55.34124 | 2025-02-02 05:08:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd17169c-c48c-30be-bb65-e82db2bbca65 | -19.11648 | -56.23322 | 2025-02-02 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 57183e35-b3f3-3c5b-9d14-8288975daf50 | -17.71852 | -54.08278 | 2025-02-02 05:08:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4301732a-7dad-3834-98bf-490ba2fc9c1d | -21.29828 | -55.90457 | 2025-02-02 05:10:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b46e8124-8a52-309b-ad83-2b81b4c5be9c | -30.19834 | -55.27972 | 2025-02-02 05:12:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 0371e1b7-1481-3c33-81b7-6d93ee1e5dff | -30.19407 | -55.27933 | 2025-02-02 05:12:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| e9e0d767-72d8-3644-b7f9-013fd4965435 | 1.94308 | -60.38544 | 2025-02-02 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b1b6bc3-e08a-3226-9c4d-265435670c33 | 3.50227 | -60.79559 | 2025-02-02 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95f3a170-688e-3b12-99ee-bd5ce968942d | 1.47501 | -60.75756 | 2025-02-02 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53991df2-f98e-3197-b757-2357346f4bdc | 3.92893 | -59.72518 | 2025-02-02 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 668f6983-3410-3b78-86c2-6ce651b53017 | 4.31177 | -60.60479 | 2025-02-02 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b887039-8ff0-3b58-b9aa-a8a53bc9a651 | 4.19554 | -60.9502 | 2025-02-02 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8bf0408-dc6c-31f8-88ce-01c37fbffdd3 | 0.73129 | -59.68192 | 2025-02-02 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a5fee32-9cd6-3a66-876f-ce326567225c | 1.94639 | -60.83866 | 2025-02-02 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e290a06c-6cf0-3082-9ead-7206b2786702 | 1.93978 | -60.38596 | 2025-02-02 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7388eb89-7cd0-36fd-8c61-d2a2e890b099 | 4.31122 | -60.60135 | 2025-02-02 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab229832-855e-3f7e-b843-3a412e83b87b | 1.93648 | -60.38647 | 2025-02-02 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fef99c41-3d16-364a-a93d-2e40eb81345b | 4.3242 | -61.1004 | 2025-02-02 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37599a82-0e27-369a-96ff-da5a35d921d0 | 3.61465 | -59.8661 | 2025-02-02 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8176aad7-c9d2-327c-9a17-610ee8d24dff | 4.30791 | -60.60188 | 2025-02-02 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db67fe2b-a74a-359b-97d6-c30cb1d686c4 | 3.65106 | -60.79002 | 2025-02-02 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c2e2a71-ccd8-3f66-b754-49c1da711ef3 | 3.64778 | -60.53082 | 2025-02-02 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26f830cf-2635-387d-9cd6-08f3607e96be | 1.95024 | -60.84159 | 2025-02-02 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 124331fa-d284-35c7-82d1-829f8a1331c8 | 4.30845 | -60.60535 | 2025-02-02 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dde3b48a-5f7e-32e1-bf54-cf5c8b9c0801 | 2.45356 | -61.31979 | 2025-02-02 05:27:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7e8a21af-902b-30c5-9445-2b67c65b403f | 3.50282 | -60.79907 | 2025-02-02 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f1b9ea4-5973-37b5-a06b-cca8e8c124d2 | 1.4176 | -59.96111 | 2025-02-02 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60ed81ce-e5f2-3b43-b02d-e611826618d5 | 1.82262 | -60.63618 | 2025-02-02 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9885ed79-f36b-3ff0-a7d3-30efab3f4bd7 | 1.71408 | -60.31209 | 2025-02-02 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14c34de0-3ca9-382e-9bf9-e58eeb5f3a54 | 1.9497 | -60.83814 | 2025-02-02 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c048f3ba-0ada-3390-a2c1-f460b7e95aa0 | 3.92947 | -59.72862 | 2025-02-02 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3554d977-7ab8-3341-85a2-6a6cc7ef0a72 | 1.94748 | -60.84556 | 2025-02-02 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb207459-86aa-3ef4-99e0-45c32cdefa4c | 1.41706 | -59.95768 | 2025-02-02 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afe7806d-7752-3099-b8d5-91b6c3f13d65 | 2.52845 | -61.34502 | 2025-02-02 05:27:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c4bf0a3-0d05-3b55-9ea6-dd970de16695 | 1.7157 | -60.32237 | 2025-02-02 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e91ca7e-f0ad-3896-bd07-392c1c345f4d | 4.12711 | -59.98937 | 2025-02-02 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 459a20c8-c7be-3d18-a67c-0ce2db75233b | 3.6141 | -59.86267 | 2025-02-02 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3d17f4c-3ae6-340d-91b8-7a30b72d932b | 4.32309 | -61.09325 | 2025-02-02 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2504fbbb-30c2-3a19-a620-a35ee2147a07 | 3.71232 | -60.74846 | 2025-02-02 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e9bbe103-822b-3f8e-b42a-a418806dcf2e | 2.55351 | -60.39848 | 2025-02-02 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90b0b04c-1961-34d3-9c84-0d9be87fd192 | 4.60638 | -60.70888 | 2025-02-02 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e696693d-33b7-3c1b-9265-680fb72309a6 | 3.73016 | -60.49324 | 2025-02-02 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dea0dd9d-cb7e-3c1f-a413-a8b29602a629 | 3.92617 | -59.72914 | 2025-02-02 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0139334-ca1d-3bc1-b992-edfed3c41879 | 1.95079 | -60.84505 | 2025-02-02 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8419635-915c-3621-80aa-d8c30d8df024 | 1.719 | -60.32186 | 2025-02-02 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 813fa1e7-877b-3815-8a98-23d8767a334f | 1.31753 | -60.42686 | 2025-02-02 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 06a72165-4e4b-3f0f-bf27-6e279e548bda | 0.73074 | -59.67844 | 2025-02-02 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README3.md)
