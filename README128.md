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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b374f45d-4826-3bbe-8e9c-6ebd17d5aaa5 | -16.08839 | -53.54641 | 2024-10-01 05:08:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2c9c152-c026-3634-bb6e-da5993a2a2cf | -16.08652 | -53.53127 | 2024-10-01 05:08:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46154557-2a93-3d3a-aa6d-d611447719f8 | -15.68933 | -53.92405 | 2024-10-01 05:08:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96459f45-c889-395a-b549-c025a1436d1f | -15.68688 | -53.91394 | 2024-10-01 05:08:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e97d6dd9-6be5-3f4c-a463-de117711c214 | -15.68558 | -53.92349 | 2024-10-01 05:08:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7437c1ed-4c75-33ad-a0e4-8df56144e0d1 | -15.58697 | -54.31446 | 2024-10-01 05:08:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14ad0dcd-c9d1-3fdb-9162-7c96b64b245b | -15.37635 | -53.75525 | 2024-10-01 05:08:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e43afea-8c6a-3b83-84c6-16f7dfa9226f | -15.37259 | -53.75467 | 2024-10-01 05:08:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f18b5d34-bdf4-3d43-87f2-89b124d565e1 | -15.24933 | -53.78174 | 2024-10-01 05:08:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 755c3993-09cc-3e84-9152-c28e748e4992 | -15.2462 | -53.77649 | 2024-10-01 05:08:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a91dc9c-7d44-3507-bab0-f80da76285a2 | -15.24558 | -53.77464 | 2024-10-01 05:08:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b202f6ab-4b70-37d7-b2f5-300f9b13fdf5 | -15.24557 | -53.78119 | 2024-10-01 05:08:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 99db5ffd-b7a7-3a9b-ba2d-c19a38292ca5 | -15.24493 | -53.78588 | 2024-10-01 05:08:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2608f366-39f8-3011-849e-f094018f9bf6 | -15.24492 | -53.77934 | 2024-10-01 05:08:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a90c2b88-557c-359d-ba40-4b96181544e0 | -15.24425 | -53.78402 | 2024-10-01 05:08:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2db56f78-9a5b-32df-b9c3-437d49e4d03b | -15.24359 | -53.7887 | 2024-10-01 05:08:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0bd272d-e734-3939-a7fd-e02d098feffc | -15.24117 | -53.78534 | 2024-10-01 05:08:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 123244df-d1aa-3617-a914-a3d2f30735f5 | -15.24054 | -53.79004 | 2024-10-01 05:08:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34e8442e-a430-38a7-9e97-686b8525400c | -15.24049 | -53.78348 | 2024-10-01 05:08:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38aebdcf-cb68-3d1a-abe5-c4d5fc0236a5 | -15.23983 | -53.78817 | 2024-10-01 05:08:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76d79b9e-9eb1-33fe-adae-01d7c8047ba8 | -15.23678 | -53.78949 | 2024-10-01 05:08:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e40281d-a876-35f9-8662-7012a1a09e9d | -17.00695 | -54.05976 | 2024-10-01 05:08:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf08d95d-7363-3e4a-87a1-d3377d2516e5 | -18.8737 | -54.50027 | 2024-10-01 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf7756d5-900b-30fd-9fbf-a8170bb93c4f | -18.87304 | -54.50521 | 2024-10-01 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4eb41a53-b201-35ee-bcd1-3bd6d1b57050 | -18.87236 | -54.51033 | 2024-10-01 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f50a3749-b555-3303-8dc0-af9eecc1f44a | -18.87059 | -54.49475 | 2024-10-01 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 74d8db13-504a-3ab8-bc49-401dde077078 | -18.86861 | -54.50958 | 2024-10-01 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1b3ef6d2-40e0-3deb-84f3-0f5181035d8a | -18.86794 | -54.51456 | 2024-10-01 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 738ef485-b9fb-3d46-a469-63cb1acea4b2 | -18.86485 | -54.50889 | 2024-10-01 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54a94a21-2121-3d49-88e5-5a6ea26b7134 | -18.86419 | -54.51384 | 2024-10-01 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1dd1acd3-9d15-3857-a23d-1a976d770ebf | -18.86109 | -54.50818 | 2024-10-01 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 408f2007-5bb8-337c-886e-56158b97c7a7 | -18.82455 | -54.49335 | 2024-10-01 05:08:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 81f226aa-afac-3b98-bfb6-94a4e16b8be2 | -19.99066 | -55.47864 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32e9193f-7dfc-3bf2-ba89-9c17d13eb795 | -19.99004 | -55.48335 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae77c218-0fa1-321f-98c5-a55c60a06d13 | -19.98641 | -55.48271 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d709b87-1614-386c-8650-3bb9809a55a0 | -19.98602 | -55.4804 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 197806e0-3102-3041-adbf-bb088c857ad6 | -19.98535 | -55.48517 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a85452f7-8c15-3022-8d3b-a93befdaa0e1 | -19.98278 | -55.48212 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90203176-3e9c-3119-ad3f-b0cdad518335 | -19.98215 | -55.48682 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65d9e88e-077a-3c86-84ee-05191072d6fa | -19.98173 | -55.48454 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98c5aaa3-ecf4-3d75-a770-a44bf282ae21 | -19.97915 | -55.48153 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78bca91a-3e66-3915-b042-196f4d861c34 | -19.97853 | -55.48617 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51236737-7cd6-3e72-a9ca-5fa94849f2bd | -19.97811 | -55.48391 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9757292a-583a-387d-ac83-bcebbed3ea31 | -19.97747 | -55.48849 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96aa7100-560f-3e49-b7b0-7cb0a4b24ff9 | -19.97449 | -55.48327 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f9f0b61-6e14-3548-b8ca-8321586b23d5 | -19.97385 | -55.48788 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39d86e56-e30a-35c4-907c-f69b4a8d78b4 | -19.97325 | -55.49217 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0f6882d-9132-3e2a-b667-f6ab46524bd1 | -19.97148 | -55.50486 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a267d6e6-b268-35c5-8a9b-57cc121d84b2 | -19.97024 | -55.48719 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7bde3953-32b8-3cb7-acd8-1bad612122d8 | -19.96964 | -55.49146 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c81518e6-f0b5-3797-8413-60d0c70fcf10 | -19.96906 | -55.49563 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e80156c7-5b7b-301d-9337-039e306e2f15 | -19.96786 | -55.50424 | 2024-10-01 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1bc1429-6fb6-3e0f-a3d2-29f094f849c6 | -20.50871 | -54.56389 | 2024-10-01 05:08:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ddb4e13-76ca-3f7b-be41-0fff1404c38d | -21.88966 | -56.10652 | 2024-10-01 05:08:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a5e1362c-44b2-34dd-9fe4-f841fab82160 | -21.70104 | -54.79601 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3029b286-9d50-3bdc-bcb1-5c0278a6239e | -21.6995 | -54.79201 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 870eb79e-c956-3956-95a3-134d23a6d493 | -21.69885 | -54.79714 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2a96083-54ab-3bb9-8ac3-0600123e19b1 | -21.6972 | -54.79544 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f54eff62-d0d1-36ad-8465-939cc1c29177 | -21.695 | -54.79657 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a55b7e0c-ff91-371b-ad11-ca67066857c2 | -21.69334 | -54.79488 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 298d4cf6-e07d-3e04-aa6e-097570694d84 | -21.69267 | -54.8 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7837b855-9a96-3bee-becb-060a12d8ef9c | -21.69115 | -54.79602 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f078a41-e538-3bb4-9432-404c2d2019dd | -21.69051 | -54.80114 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 025d7ebc-1480-36c1-9928-f0c92230f107 | -21.69045 | -54.84652 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 55d6c4ad-07f3-3269-80c9-d6717b889ade | -21.68922 | -54.84265 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42e777e5-505e-34cc-a1ed-d58217c934de | -21.66546 | -54.8581 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6732989-31b8-3ba1-b4d9-f7cfb1ef142c | -21.65078 | -54.8508 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eaedc8d9-a817-39d4-82b3-89ba33de62ec | -21.65012 | -54.85583 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcd99c82-3fdb-3461-86c4-012b27eb8314 | -21.64694 | -54.85023 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ad3a03e-1db9-3be9-be4f-ca71564bf268 | -21.64629 | -54.85526 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 634038d3-d8b9-3613-ba3e-47c38d2ea41f | -16.65174 | -55.2038 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 4017f8b6-145c-32d0-b4b3-ac9e5b482438 | -16.65113 | -55.20797 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| cfe88ede-e87d-3b2d-b0ce-066993a404e6 | -16.65053 | -55.21215 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4c896e86-59d5-329c-939b-97f9d7b08afd | -16.64464 | -55.2027 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9fc4b0f9-d32c-3431-acc6-383c5148b9ca | -16.64049 | -55.20632 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6270ac43-a82c-37ce-a525-bad57a142f0d | -16.63988 | -55.21049 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ca0f3a70-07ca-300a-b7fb-d0acb97559a7 | -16.63813 | -55.19744 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0bae2001-ec73-3659-8da5-e3a426421070 | -16.63694 | -55.20577 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| beff3bee-6eb3-3195-b454-c4311e6625a0 | -16.63574 | -55.2141 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 47810eba-ad5d-36b2-876b-4162babde95b | -16.63223 | -55.18799 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fdcb00f0-2da0-33b5-983a-ad8b809fc945 | -16.63163 | -55.19216 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| f4ede8a3-8064-3c4b-a94f-ab59a256ce8b | -16.63043 | -55.20051 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c18aba4d-69e4-376a-b70f-e3a75bf48984 | -16.62808 | -55.19161 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 7309ee1b-eee8-3652-a19d-bd80c9cd9e04 | -16.62748 | -55.19579 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| f05a4dc6-8792-3759-ace0-1a08fec88e46 | -16.57978 | -55.95729 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8cb53346-e9b4-3f42-bde6-43dd6f1afa9d | -16.57922 | -55.96119 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 29e7005b-da4d-36ad-9da8-77f2d4859ce5 | -16.65408 | -55.21269 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| db0dc4eb-883e-3733-b171-504b732e4e9f | -16.64819 | -55.20325 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 706941e0-dbc3-3652-8cba-12acac4aed31 | -16.64758 | -55.20742 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 4af79977-2eb1-343f-823a-df1ab008d97f | -16.64698 | -55.2116 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| de6984f7-52a8-3a6e-8a4f-ba4db1343867 | -16.64524 | -55.19854 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 665771f0-9a2f-3bb8-9781-9cbe943f18d2 | -16.64343 | -55.21105 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cad82372-e427-3411-89dc-185ce90cbbcc | -16.64168 | -55.19799 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1a2157fc-64f7-3400-9490-fe2e92f2e54d | -16.64108 | -55.20215 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 13f4d978-3434-3b14-80f0-5f76d1c1a705 | -16.63754 | -55.2016 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ccde3f3e-34b3-3c49-98cd-0b24c396a76e | -16.63634 | -55.20994 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f44e624a-2880-3ee8-b208-e12b86387d48 | -16.63578 | -55.18854 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 42c899b3-aa09-3846-bf56-715e38d707b4 | -16.63103 | -55.19633 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 31fcd975-ebd4-3c64-9c20-327f3b53b2a8 | -16.62984 | -55.20467 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5ea9dea0-6ffd-3a61-8959-ed0977032163 | -16.62688 | -55.19995 | 2024-10-01 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |


[Clique aqui para ver as próximas entradas](README129.md)
