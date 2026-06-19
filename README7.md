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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2355397-cd76-30a5-b7c1-beddee4375ac | -18.97565 | -52.45181 | 2026-06-19 04:29:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fa09e3d-f04b-39ce-bfd3-47c8004d83da | -17.10828 | -49.75664 | 2026-06-19 04:29:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98fb10a1-b02a-38a1-9b86-74a4b661c76b | -17.32196 | -43.64529 | 2026-06-19 04:29:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9e804008-cc96-36fc-a927-ab2a44896c5f | -15.07348 | -55.8092 | 2026-06-19 04:29:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15cd2263-6491-3d86-b537-6e92a6329fde | -15.07607 | -55.81305 | 2026-06-19 04:29:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cee697a8-14f0-3406-9e9a-9a7325f7a0ad | -18.4938 | -51.66767 | 2026-06-19 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ceff037-74be-3f79-b57b-3616f9f1d824 | -16.2689 | -60.00647 | 2026-06-19 04:29:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35a216e0-1eb5-325a-9a2c-02453dffb6d8 | -17.10887 | -49.75298 | 2026-06-19 04:29:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb792455-abd8-37b5-a283-7ddc1fed12c6 | -18.97927 | -52.45245 | 2026-06-19 04:29:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 764145a4-6129-373a-a809-4dd3cc837e7b | -17.31799 | -43.64466 | 2026-06-19 04:29:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7f57db9e-4c40-3cef-9554-f361842cbb8f | -18.97416 | -52.45329 | 2026-06-19 04:29:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 102d392c-1fa2-3883-a0bb-5fbfe3464c43 | -19.48677 | -52.71278 | 2026-06-19 04:29:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bc7e60a-1dcb-3e39-a771-422305613029 | -19.4896 | -52.71795 | 2026-06-19 04:29:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48d497c6-765a-3de2-ab72-933428efaa1f | -18.97777 | -52.45391 | 2026-06-19 04:29:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd96e95b-8c01-3cd8-b253-82b0b0f6857f | -18.43428 | -50.55975 | 2026-06-19 04:29:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 633df50c-c427-3637-a208-5121dbf3280c | -17.34862 | -53.81192 | 2026-06-19 04:29:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70885bd3-77e0-3673-97c4-24b0327dfca0 | -16.1328 | -58.49604 | 2026-06-19 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8dd2c196-5c18-3a0d-a935-43a900a95c90 | -18.83298 | -51.47275 | 2026-06-19 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79671c0c-d135-3413-a8c0-98d06ec99acb | -21.22888 | -44.14892 | 2026-06-19 04:29:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c90105bc-08b0-3d46-be81-280caef40147 | -19.75047 | -53.54391 | 2026-06-19 04:29:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f7bb3fe-a080-3afa-bd80-999da8522cff | -20.87852 | -43.766 | 2026-06-19 04:29:00 | NOAA-21 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f859e006-8a01-362f-8edd-07f173f926ba | -17.72675 | -52.55167 | 2026-06-19 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0b3fdae0-2c1b-3039-9d7b-9c2f5fb77b59 | -16.26388 | -60.0006 | 2026-06-19 04:29:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdf5ebfe-a642-3012-8836-19839cd339e0 | -19.49039 | -52.71351 | 2026-06-19 04:29:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12a00994-51bc-3954-834b-26f2339b962c | -16.26288 | -60.00526 | 2026-06-19 04:29:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 993a1e67-a878-3ed2-8242-aef7d836840a | -17.32267 | -43.6398 | 2026-06-19 04:29:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4024af1c-b3ac-3fbe-9af5-c7b424f69038 | -17.11161 | -49.75721 | 2026-06-19 04:29:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcd5e477-ec20-36ca-84a9-69a5d5fe0a25 | -15.07132 | -55.8123 | 2026-06-19 04:29:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc00f552-d47b-3a73-9f99-95bca746e54a | -19.74207 | -53.54724 | 2026-06-19 04:29:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 834fad53-a3b7-3185-9926-00df25923a49 | -17.35655 | -53.81361 | 2026-06-19 04:29:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fc40812-761c-35a6-9685-83d7d9906f04 | -18.82606 | -51.47145 | 2026-06-19 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9431b7b8-ea67-35f8-b209-e930840702a3 | -15.73614 | -48.21213 | 2026-06-19 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb2533d3-ef54-3e72-b11d-ecb44aa3f47a | -16.13357 | -58.49234 | 2026-06-19 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| eeda4e3f-074a-3963-bb2c-ce1da99f2cd4 | -18.98287 | -52.45312 | 2026-06-19 04:29:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad79b645-0c1b-3e32-b9ea-405bdd44df84 | -18.82952 | -51.4721 | 2026-06-19 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 000ee7aa-d244-3f17-9d66-6a05b8e939b6 | -19.36076 | -48.72156 | 2026-06-19 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 97b26ab5-349c-3636-98b7-b5856207f535 | -19.48598 | -52.71721 | 2026-06-19 04:29:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc3aaa63-c83f-3ad2-bdbe-edbe5a35eaf3 | -17.10946 | -49.74932 | 2026-06-19 04:29:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fccdd19-d6a1-3654-a9ab-9187076d9051 | -19.49322 | -52.71867 | 2026-06-19 04:29:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7bf2932f-fdd9-3575-81fe-a67c757ddae6 | -12.8741 | -44.3593 | 2026-06-19 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| b2aa4546-cba1-32eb-995c-5db3a5ff4b2c | -12.8736 | -44.3828 | 2026-06-19 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| b3fe8403-3fcc-332a-bf15-b0b518ed15ff | -16.0342 | -43.4224 | 2026-06-19 04:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 63.1 |
| f6ce28fd-e341-383a-bb23-1608f9cfcd11 | -22.80152 | -49.33758 | 2026-06-19 04:32:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 346e681b-7cd4-3ff3-a574-c194d4553e3b | -21.27193 | -56.03647 | 2026-06-19 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1cd85d21-9a24-3fe8-82ab-b2bf12f8b60f | -22.78655 | -49.34652 | 2026-06-19 04:32:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b54f69e2-09a5-3bc1-a4a6-dc76ad9a69a4 | -22.78542 | -49.35401 | 2026-06-19 04:32:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9aca3e9f-b464-3f9e-83d1-d2948230f4fb | -22.89793 | -43.58559 | 2026-06-19 04:32:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 991d7ff9-d281-3769-83af-5bc9e472a4e8 | -22.78267 | -49.34968 | 2026-06-19 04:32:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40e925ed-17e7-3198-868f-96b3ee04aea3 | -22.78598 | -49.35026 | 2026-06-19 04:32:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f32ec5dd-abe9-3f7c-93a1-d3d0770fa958 | -22.80427 | -49.34192 | 2026-06-19 04:32:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65970a62-4646-3851-ad37-436c68b29425 | -21.26898 | -56.0371 | 2026-06-19 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe3acfde-9149-38e9-aad0-feb99d74174b | -22.78987 | -49.3471 | 2026-06-19 04:32:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0377530e-db23-38ac-a694-874266ba7d6d | -22.7965 | -49.34826 | 2026-06-19 04:32:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb820faf-3f62-3329-87b5-35d661ebedc7 | -23.56595 | -46.83676 | 2026-06-19 04:32:00 | NOAA-21 | CARAPICUÍBA | SÃO PAULO | Brasil | 3510609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0781a8e2-da81-3e8a-abe4-95ea66bae9e2 | -21.2728 | -56.0321 | 2026-06-19 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 041bd216-2c93-308f-ba5f-37854038f427 | -22.80484 | -49.33816 | 2026-06-19 04:32:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93dcb477-4298-3d0f-93a5-4269ad0ef061 | -12.8736 | -44.3828 | 2026-06-19 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| e9f83ce7-07c8-30da-aa1d-fcb9bd5da0d7 | -12.8741 | -44.3593 | 2026-06-19 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 44ee55cb-8055-31e3-bde9-7f8f22cec5cb | -16.0342 | -43.4224 | 2026-06-19 04:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 873cfc74-ab25-38f2-972a-bf674524e568 | -12.8741 | -44.3593 | 2026-06-19 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| f6f3e372-ea4a-3e1c-8362-4bca4e37dc43 | -12.8548 | -44.3625 | 2026-06-19 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| fef417f4-1225-3e8c-a8a0-230e5b155989 | -12.8736 | -44.3828 | 2026-06-19 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 3e7ee17b-3ff9-3035-b62d-fe85172c9b3b | -2.27194 | -50.69024 | 2026-06-19 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 71887db0-3f99-3731-b2b1-62b890775c62 | -12.8736 | -44.3828 | 2026-06-19 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 9bd40353-f782-30d3-b44b-b65ce78b950f | -12.8741 | -44.3593 | 2026-06-19 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| b23d1cd8-1f14-3583-a401-1de3e4f7a649 | -11.05686 | -52.46196 | 2026-06-19 05:01:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25498056-58cc-379b-a5bd-67bf9e1725fb | -11.06398 | -52.46239 | 2026-06-19 05:01:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2992d47-70c8-347a-9940-aa2c5415e0fb | -10.05213 | -48.0994 | 2026-06-19 05:01:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0c9aa184-2072-33f2-944f-db592cada520 | -11.06793 | -52.45924 | 2026-06-19 05:01:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b388646b-a26d-3eec-851a-43cd3f9953df | -10.98659 | -47.7515 | 2026-06-19 05:01:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 509c86f5-e94a-3bf3-b7c5-13c41deb220b | -11.33223 | -48.00088 | 2026-06-19 05:01:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ccaf9d3-4333-3845-94fa-a18bf9fcd06a | -11.06737 | -52.46291 | 2026-06-19 05:01:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9995b615-ecc7-3df9-b49b-9106fc97074b | -11.33652 | -48.00153 | 2026-06-19 05:01:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c415cec1-8c62-3dfc-b5fc-30d162638fb8 | -10.05796 | -48.08853 | 2026-06-19 05:01:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dac6a30b-15d7-3a19-bc04-d80cae738512 | -10.05687 | -48.0962 | 2026-06-19 05:01:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7f60c3d1-c467-35b1-b6dd-c7d16b19a724 | -7.63281 | -50.01936 | 2026-06-19 05:01:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63f39efc-bb9e-37c3-9c89-1b8dd66de0f3 | -8.78805 | -46.63026 | 2026-06-19 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55b49aa2-5df3-3a82-9f7b-1327daeb6e97 | -11.31071 | -51.41799 | 2026-06-19 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6090e5a0-fa13-36d7-9288-e74beca9058a | -10.54595 | -53.73158 | 2026-06-19 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f1bc6d3-744d-30a0-923d-e42176e496fa | -10.06216 | -48.08913 | 2026-06-19 05:01:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1871a625-c45c-37da-9137-a9b397ffd079 | -3.85185 | -54.22273 | 2026-06-19 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5fefc3cd-9cf9-36b1-86ab-749c8adb3089 | -3.85397 | -54.22237 | 2026-06-19 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30ee50a8-72a8-3d1c-a2de-c9d39d3204e7 | -8.89711 | -48.00346 | 2026-06-19 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 176d3b91-893b-357c-ba33-2889a1f351e0 | -10.98285 | -47.74661 | 2026-06-19 05:01:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 927b3217-ddbb-3159-8725-a6a616b5048c | -7.36344 | -49.85691 | 2026-06-19 05:01:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c81aff3-061f-3ee2-aee9-dc3fbb8b8b11 | -10.04905 | -48.09102 | 2026-06-19 05:01:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdf1a966-fb8f-3018-928f-ee2b61ec9b2c | -7.35855 | -49.8648 | 2026-06-19 05:01:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d86815bd-e908-32c1-90b6-93e02aad98ea | -11.058 | -52.45461 | 2026-06-19 05:01:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 171e549f-b31d-38a2-b904-b52409ff3936 | -7.35554 | -49.86003 | 2026-06-19 05:01:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55a85504-cdcd-3903-a910-2f0f42673e05 | -4.23617 | -49.17599 | 2026-06-19 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bae6806-eb09-3998-98d4-cac92ea8b4e8 | -10.90796 | -54.13623 | 2026-06-19 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 308970bb-b872-3818-9836-450db86e9bd2 | -10.55193 | -46.339 | 2026-06-19 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45aaf2d3-ec0a-3598-b3ee-6653008893da | -4.23253 | -49.17545 | 2026-06-19 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b051580c-039d-3d26-9dc8-608e2d828ec6 | -4.35072 | -47.7603 | 2026-06-19 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e3718687-2ceb-36c0-a24f-9fc793014b33 | -8.91585 | -46.9418 | 2026-06-19 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36b683ad-6270-39cc-8ab3-4c0eec2d68dd | -11.31131 | -51.41402 | 2026-06-19 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3284e6a7-4c83-3d9f-ae19-fbab7f8da999 | -10.16094 | -56.61714 | 2026-06-19 05:01:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c01b864-273a-32c4-adb8-221f9bb0d569 | -9.67994 | -47.03935 | 2026-06-19 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21b28e5c-b951-327d-af3c-5d02c28f1ef2 | -11.0572 | -52.46131 | 2026-06-19 05:01:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d19828c-9b57-3eac-8532-e8766ad7ea96 | -10.91122 | -46.33649 | 2026-06-19 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README8.md)
