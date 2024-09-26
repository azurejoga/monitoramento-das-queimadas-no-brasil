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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4451a1c-e4ff-326f-9fe5-9d93ddfb456e | -17.0648 | -56.174 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8a1b8be0-6d9c-333b-9976-e2e374aafdd4 | -17.0676 | -56.185398 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0ec613d0-2981-35e3-978c-1ad19823cc25 | -17.070499 | -56.1968 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4e96dfe0-62e3-3d55-9457-9df573345f22 | -17.0734 | -56.208099 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e2b7fdb1-6b3c-3636-b092-c91c5eedb099 | -17.0763 | -56.219501 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e75f6d3d-2b9d-301c-a814-9d24a703e9f3 | -17.107401 | -56.342999 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7119d3ef-5716-3020-8b00-f447aa710490 | -17.110201 | -56.354198 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 92bcf32d-0f71-335c-b3c4-59b2f677b6bd | -17.0492 | -56.153801 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3d0cce6b-7ae0-3705-bf04-a903d8e56bb4 | -17.052099 | -56.165199 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 210ab881-d704-3efc-a7e1-4037512137cf | -17.055 | -56.176601 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f15e409c-af19-3f15-ab92-1de89563d4be | -17.0578 | -56.188 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c9907bab-b29d-3c99-aab0-3db5521be02f | -17.060699 | -56.199402 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 702936b0-a8dd-3e84-b620-abb116a96266 | -17.063601 | -56.210701 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2384dda5-8d14-346f-865c-48b7b6250e93 | -17.094801 | -56.334499 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9c7231d4-e4fd-3f14-97e0-678d05f78b40 | -17.097601 | -56.3456 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 80599aaf-f4f1-3d9f-a5f2-29b6e1547220 | -17.100401 | -56.3568 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 184541dc-beb3-3053-bf66-96b13cfea6c2 | -17.0453 | -56.179298 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 10888aa2-0729-3557-b001-287ae50c7352 | -17.0481 | -56.190701 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 625bec70-0c32-338d-9420-42b0e1aaf25b | -17.051001 | -56.202 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 62d8e3ee-247e-31fd-8393-95e61d46d205 | -17.0879 | -56.348301 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bcc517fd-6c19-3a48-916f-7ad816fc4ccf | -17.035601 | -56.1819 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9048d1cf-3b07-3171-91cc-a771db8f84a4 | -17.038401 | -56.193298 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 11065792-4617-3651-9766-82d863a22ba0 | -17.0413 | -56.204601 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0306ae52-98b1-3d10-90b6-bc71ce2e45f6 | -17.031601 | -56.207298 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1667d847-bf96-399b-9768-86e3147d1efa | -17.0345 | -56.2187 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 91955f21-3ef1-3e26-9058-0439d157b483 | -17.057501 | -56.392101 | 2024-09-26 01:47:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6514f363-7885-3ad3-9fa3-40fe8624f01c | -14.8869 | -51.493599 | 2024-09-26 01:47:54 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f0802399-bc14-3b4d-8bd6-72f741fe3217 | -14.8704 | -51.4715 | 2024-09-26 01:47:54 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f767eb63-efed-356c-931f-627f9bf4042e | -14.8773 | -51.496399 | 2024-09-26 01:47:54 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 795cf77d-0e96-33c7-a034-268b5f5a51fc | -14.8842 | -51.521099 | 2024-09-26 01:47:54 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7beedebd-f500-3dd2-9114-6e0f3122f44c | -14.8678 | -51.499199 | 2024-09-26 01:47:54 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a9bb1e5a-0896-3a36-bb36-b67f6fa24bcf | -16.631001 | -58.445 | 2024-09-26 01:47:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c25441ae-b1f9-31e2-8d94-ed14e37b7722 | -15.8501 | -57.409901 | 2024-09-26 01:48:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8bd1aba1-397f-3f25-a62a-5f6c4dddd890 | -15.8526 | -57.419899 | 2024-09-26 01:48:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb91704b-3090-37eb-af2e-2893ef59592a | -15.8379 | -57.402401 | 2024-09-26 01:48:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d27ff92-8cb7-3279-9729-9838f92ed070 | -15.8404 | -57.412399 | 2024-09-26 01:48:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7d170d6e-9819-373e-964a-39aa4b8e715c | -15.8429 | -57.422401 | 2024-09-26 01:48:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2243baa-17ab-3ddc-bb5f-2858fb5464b4 | -15.5848 | -56.9258 | 2024-09-26 01:48:06 | METOP-C | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 78f1a2ea-eca9-3715-985b-bfef3b851726 | -13.2965 | -51.3125 | 2024-09-26 01:48:19 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c2f51e58-0b4a-342a-83d1-09ec1ff67dc3 | -13.304 | -51.339699 | 2024-09-26 01:48:19 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d1e29777-f8ee-30dd-96f0-2214e136cf4a | -13.2869 | -51.3153 | 2024-09-26 01:48:19 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c4eb8a8f-9a2e-3de4-8e22-bb86abab75ef | -13.2944 | -51.3424 | 2024-09-26 01:48:19 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e1976136-2b4a-3045-bd8d-57c37f4b72f9 | -14.9469 | -57.9473 | 2024-09-26 01:48:20 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98ee12f5-bec1-3454-b28f-5b8bc1c08ecb | -14.9102 | -57.9669 | 2024-09-26 01:48:21 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db8dfd1e-23fc-3665-a6ce-4f979ad511ac | -14.9126 | -57.976501 | 2024-09-26 01:48:21 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae118f9f-b302-39b3-b254-e186b0cecfbc | -14.9149 | -57.986099 | 2024-09-26 01:48:21 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62577425-9ff0-32a3-9559-425b92427071 | -14.9005 | -57.969398 | 2024-09-26 01:48:21 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d6f79f5-c34e-330c-bcb3-757d23a2e649 | -14.9029 | -57.979 | 2024-09-26 01:48:21 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14ad423d-90db-3afd-9eaf-0a890eeb5c3d | -14.9052 | -57.988602 | 2024-09-26 01:48:21 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15bd56ae-ff54-3709-ad8b-da113f118de1 | -14.9025 | -58.019699 | 2024-09-26 01:48:21 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee2d1445-ab4c-3761-bc7a-5ffd80a334e4 | -12.8148 | -51.212601 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a6c90186-3ccb-31c6-b901-00da36b0b427 | -12.8225 | -51.2407 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ce258b5d-7813-3851-a58f-590f64bdaa39 | -12.838 | -51.296501 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1991aceb-85bf-371e-b6c8-93ac44bb69c5 | -12.8456 | -51.3242 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3c103842-4ffe-3efd-ac5d-9b20d06f43f8 | -12.7974 | -51.187 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 32c33c66-0991-3586-a05e-1f45dd62db3e | -12.8053 | -51.215302 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5296f314-cf95-3ddf-97ef-e829351d0269 | -12.813 | -51.243401 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bf92b271-6df0-3e4f-82bb-776fc89d27a5 | -12.8208 | -51.271301 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6ebb9e40-6fa7-32de-a07e-44742c7e2c86 | -12.8285 | -51.299198 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2183892c-0d54-3145-a9b9-241def0951b1 | -12.8361 | -51.3269 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 02453365-a48d-3bfd-b79b-929045fedddd | -12.7878 | -51.1898 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2b0a8233-ebcf-3f60-b3b2-826e7f59fd24 | -12.7957 | -51.218102 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7415565d-af02-32d7-8740-e8d48474982e | -12.8034 | -51.246101 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a9f6a08b-8205-3053-930f-2c61d9628ff3 | -12.8112 | -51.274101 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cfc9d673-74fd-3e39-83db-23f32c5c15b0 | -12.8189 | -51.301998 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2282f1df-2854-3064-a6c8-d7469522b45c | -12.7783 | -51.192501 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0de83555-4867-332d-b580-24c81b48bdfc | -12.7862 | -51.220798 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0d2004df-9cc6-3579-bb0f-798e4e74f7ed | -12.7939 | -51.248798 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6a8f5481-5955-399f-8d97-464cb2cd8370 | -12.8017 | -51.276798 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 00052e06-910c-314b-ab6d-d9682abe7bee | -12.8093 | -51.304699 | 2024-09-26 01:48:26 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6f742767-127e-342f-b45c-aec6c9601dde | -12.7687 | -51.195301 | 2024-09-26 01:48:27 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e7696c5c-c53d-3e1a-bbb5-71e285add824 | -12.7766 | -51.223598 | 2024-09-26 01:48:27 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 437fa6af-27b6-328e-adb5-e68e9655edac | -12.7843 | -51.251598 | 2024-09-26 01:48:27 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 96ff2d49-b294-31c2-892e-948534d53292 | -12.7921 | -51.279598 | 2024-09-26 01:48:27 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cacffbec-7848-3ea0-aac5-18fa716d5cf4 | -12.7997 | -51.307499 | 2024-09-26 01:48:27 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d048078c-a144-3988-8e6a-10da3aec5a31 | -12.8074 | -51.335201 | 2024-09-26 01:48:27 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 28eba80d-6813-3cc9-b036-9fc78ba9033a | -12.7671 | -51.226299 | 2024-09-26 01:48:27 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4935b681-7eac-3775-83ff-fe18da01f3dd | -12.7902 | -51.3102 | 2024-09-26 01:48:27 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4863aaf4-896a-3e0b-9963-cc0eb1e6abd6 | -12.7979 | -51.337898 | 2024-09-26 01:48:27 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c98489fe-bce8-3e52-adaf-25214d8ad433 | -12.8055 | -51.365501 | 2024-09-26 01:48:27 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 633934dc-be12-3905-8bb4-67ec4a73cc2a | -12.7883 | -51.340698 | 2024-09-26 01:48:27 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2ea1644e-959a-3fb4-8928-b374fa9ff234 | -15.0626 | -60.2439 | 2024-09-26 01:48:27 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc295a20-32e8-3a19-8b05-074e04898f7b | -15.0528 | -60.2463 | 2024-09-26 01:48:27 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f58b6292-584e-37ee-ac4b-a90fb8eccf8f | -14.7954 | -59.4189 | 2024-09-26 01:48:28 | METOP-C | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c17b4ca4-86db-30d0-a370-8225b543b662 | -14.7856 | -59.421299 | 2024-09-26 01:48:28 | METOP-C | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4937b8ad-3c5c-3e33-a56d-ff79cf85db3c | -14.774 | -59.415501 | 2024-09-26 01:48:28 | METOP-C | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f56f0a6-3075-3bd6-b625-4a21351ab8fd | -14.7759 | -59.423698 | 2024-09-26 01:48:28 | METOP-C | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 209e823d-eaa8-32dd-9414-f422809ee33a | -14.7075 | -59.440701 | 2024-09-26 01:48:30 | METOP-C | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ebdf3b87-9b97-3271-a13d-d43aae46436d | -12.8102 | -54.025799 | 2024-09-26 01:48:38 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 604c7dd5-5168-3b88-8197-e54afb8a32cd | -12.8005 | -54.0285 | 2024-09-26 01:48:38 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d4765cfc-20d5-3345-a000-7349baa20e78 | -12.8053 | -54.046799 | 2024-09-26 01:48:38 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eede9a89-5f08-37f3-816c-5d6bfaa611d0 | -12.5231 | -53.487598 | 2024-09-26 01:48:41 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb58fbeb-1e0d-374a-b95f-a28609bf20fc | -12.5135 | -53.4902 | 2024-09-26 01:48:41 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ffb8c585-5a02-35f9-ab82-bf61090c4f18 | -13.0346 | -57.2869 | 2024-09-26 01:48:48 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3593f3f-db9d-3cb6-9ab0-6abb8567555e | -13.0373 | -57.298 | 2024-09-26 01:48:48 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5e239f9-cb21-30e4-9242-6f5997ff528a | -13.0401 | -57.309101 | 2024-09-26 01:48:48 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e759d75a-c0b5-3125-8989-96e2a31f60ca | -13.0276 | -57.300499 | 2024-09-26 01:48:48 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe5bbf59-25c0-3cdf-9549-f74a804f94e7 | -13.6852 | -60.714298 | 2024-09-26 01:48:51 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9144b756-360e-3bd3-8240-c02737c74c70 | -13.687 | -60.721802 | 2024-09-26 01:48:51 | METOP-C | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cbd78479-fa7c-3de5-9a38-cbfaff68b40f | -11.2074 | -51.134602 | 2024-09-26 01:48:52 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README37.md)
