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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8e97cf3-939b-3b9b-acc9-af8d91ca9457 | -19.65309 | -56.74868 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| c533b842-8a5f-3ed9-9468-bb13a739d473 | -19.65269 | -56.77328 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 3abdd6ba-f292-3060-b3c5-bdf04a153c43 | -19.65234 | -56.75262 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 4a4e2b37-9530-34f7-805d-0b32955ca643 | -19.65199 | -56.73203 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 27.8 |
| 0d2867c9-22d8-321c-86ea-c3caf6e7ce0e | -19.65193 | -56.77724 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 011c0293-cfd3-3b3f-9cb4-7645c9ab82bf | -19.65158 | -56.75658 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| e4b2429b-dc60-36a3-8aab-dd538a002e5c | -19.65123 | -56.73597 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 02b8c165-9a1d-3eb6-aaa4-453d31c20bcc | -19.65117 | -56.78121 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| c3badbf6-bd26-32bd-813b-4897c8193090 | -19.65083 | -56.76054 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| bf1dcd8f-77e4-38b7-bbfd-a583a20b9481 | -19.65048 | -56.73991 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.8 |
| d945ca24-cd64-3479-9659-dd0fd599592b | -19.65007 | -56.76449 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| dbb01fcb-12dc-35aa-aadf-8df6d9e9e93a | -19.64972 | -56.74386 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| adba707e-b315-369b-8636-1c4335ac9d21 | -19.64931 | -56.76844 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| fc0204f2-5d5b-3fe3-a453-7eac1e9f60ec | -19.64897 | -56.74781 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 441d88a3-2a1c-3cad-9761-1b1702b938ab | -19.64856 | -56.7724 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| e7bd7f23-e0a2-3f2e-a125-05c83ba3db6a | -19.64821 | -56.75176 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 8578c077-cb4a-39c8-bd16-aed1e059484a | -19.64745 | -56.75571 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6417eb44-bb8c-3b0f-b8f9-6cf5919b54c9 | -19.64711 | -56.7351 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 28.1 |
| c94ad935-7e32-31b6-98f8-d8203d320f87 | -19.64704 | -56.78034 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 6acd6871-fe75-3733-b10d-0227bffebf7d | -19.6467 | -56.75967 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 2cd9b803-d643-391e-94bd-e28596e5fdeb | -19.64635 | -56.73905 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 28.1 |
| 26b3370f-4583-37db-a187-99c425b9600c | -19.64594 | -56.76362 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 438cc062-bd52-3976-8648-8a19bf51ce4c | -19.6456 | -56.743 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| d9ccf1d3-4d81-3db0-9c05-c21ee8f37fff | -19.64519 | -56.76759 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| b562b274-78cd-3053-b6a9-38eb510d4452 | -19.64484 | -56.74694 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 16a5867c-3395-33e8-822d-a70555f46bcf | -19.64443 | -56.77154 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 0b252e5c-9449-3c5b-8b8c-e36067634ffa | -19.64409 | -56.75089 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 466a86b3-e91b-393e-b5bd-f4e520f818a8 | -19.64333 | -56.75485 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 0bdb4983-6900-3e4b-a311-144e58bae551 | -19.64257 | -56.7588 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a133d23d-d518-3502-a113-0eade0182775 | -19.64223 | -56.73819 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 28.1 |
| a6ccc676-435f-3acf-8714-09154ebc687e | -19.64181 | -56.76276 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 46c91baa-17ec-361a-b3b5-177b92404914 | -19.64148 | -56.74213 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 6cf4e28c-1d41-3b4b-a332-f5df424e3cb6 | -19.64105 | -56.76672 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 43c81813-455e-342f-b4d7-187efcc88cfd | -19.64072 | -56.74608 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| b52a73bf-cef5-3f44-94c1-2760f068b224 | -19.63996 | -56.75003 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 0e4ff40e-4cea-3566-9589-4c154c23b32e | -19.63811 | -56.73732 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| f63b4596-6a99-307b-98d2-1c06dde9bdc9 | -19.63735 | -56.74127 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 9799d95d-f531-3b78-92ac-c17ba532014a | -19.63659 | -56.74522 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| aa20746d-7f84-315b-9ac7-b7167f610195 | -19.63508 | -56.75311 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| bdd69d8b-efb6-3f22-a01a-14875b1af7a3 | -19.63432 | -56.75707 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a645c0e0-2f02-33d7-8c50-1490cc457377 | -19.63247 | -56.74435 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 94a2a9d2-c4fd-38e0-943d-8ebbc6a3aceb | -19.63171 | -56.74829 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 274872c8-2d93-3270-84b2-2a000bd93141 | -19.63095 | -56.75225 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| a08c8f29-0edf-3cc0-92e1-a746f0be6bd3 | -19.63019 | -56.75621 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 06dc4498-cf11-37ad-ab7e-14ebf94b69dc | -19.62943 | -56.76017 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7099cf31-dafe-3cc8-8dff-1a9d6c9fe50a | -19.62866 | -56.76412 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| fa3d3b93-0064-3204-b625-2a84d39443f7 | -19.6279 | -56.76808 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| bec722ec-4da1-3ee3-8b46-3c5d9a792582 | -19.62758 | -56.74743 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 37f665ee-6f29-3647-ae1a-af84b373719e | -19.62682 | -56.75138 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 94aa38c6-e6dc-3861-965b-9b3ddc4f5d30 | -19.6253 | -56.7593 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 7f413570-a0d4-3191-9ea8-e4b8ffaa8314 | -19.62453 | -56.76325 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 4a91b8a5-3c15-378f-af3d-d164a11b11d5 | -19.62377 | -56.76722 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| d6e8d741-035e-36c3-a715-5b94ee20b278 | -19.61964 | -56.76635 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| f596d0b9-f489-3d4e-b96f-94f677e2314a | -19.61888 | -56.7703 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f6450852-e3d8-3877-8a6a-27b4cd635b0d | -19.61811 | -56.77426 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2c55270a-42d9-3d07-97a4-e3bd0f47954c | -19.7235 | -56.73884 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f7ac933d-df55-36d3-a8ea-72975ecdc6c9 | -19.72276 | -56.74279 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| e5fda0d8-1311-374f-a371-e353f7aacbc5 | -19.72161 | -56.73781 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 580bca90-43ea-3c77-8be3-6f98385cd529 | -19.72084 | -56.74175 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 8aabdeff-ea44-35a9-ba72-482ac54ee13b | -19.71864 | -56.74193 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 8f4b3c37-1f36-31f9-93d4-fcbcd994f9e3 | -19.71672 | -56.74089 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| bdbe2a75-efdf-33b1-bc96-7504043e4f91 | -19.716 | -56.73317 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4a77de93-f99d-39eb-b617-da7bfc83d4d2 | -19.71526 | -56.73711 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| bf6559f0-68e3-3bf1-84ed-337f3e2c88ce | -19.71452 | -56.74106 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 597f2ce9-9d4a-34b2-bc2a-9796fedea378 | -19.71188 | -56.7323 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7a22a887-fe11-3532-9e19-c980ab9df0c6 | -19.71114 | -56.73625 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 133d5ea0-70a0-38f1-a3cd-c29895021d06 | -19.71041 | -56.74019 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1e653a34-f9b5-3fdd-bf80-b581b7543245 | -19.70861 | -56.7727 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0acc95f0-64d7-328a-9143-d82e9cb65009 | -19.70786 | -56.77666 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 41078498-9353-3740-ab71-6031866a9b1e | -19.70777 | -56.73143 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0fae1be5-65e9-30d9-9a44-db7450a2df76 | -19.70703 | -56.73538 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9f74f112-1381-3a20-a242-de61406b64c6 | -19.7067 | -56.75996 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a32a857d-7f04-30c3-87b5-911559a2e496 | -19.55064 | -56.6901 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b38cee2d-3a46-3e9d-85ee-1fe57ec6d131 | -19.55027 | -56.66961 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| a7553086-306f-3836-8fd7-938f2383a221 | -19.54991 | -56.60457 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1763f76a-ad16-3bb2-a057-5de8e3507d45 | -19.54988 | -56.69403 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| dad7dfb1-6ad7-3ed9-b1b6-c41d84113db1 | -19.54952 | -56.67353 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 3dc87333-6b14-3b28-b0be-49d58b3b6089 | -19.54917 | -56.60846 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b54ae0a7-ba09-3051-9c70-74c9adec6b56 | -19.54913 | -56.69797 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 9c6d8734-7db0-3a4a-b68e-772189b3562f | -19.54877 | -56.67746 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 25d4d5ab-79f3-377c-b54b-be31d30d444c | -19.54838 | -56.70191 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 8b345e75-d369-3b5e-ad4e-8b9822e12f87 | -19.54802 | -56.68139 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| f915cb79-8b25-34ee-8ed1-3d7e07155aac | -19.54766 | -56.66092 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 9dbc77b6-f509-3a3a-a8b6-a0bc62a18d22 | -19.54727 | -56.68531 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| f6111e82-50ea-33ca-87b1-dfdeb4a0e571 | -19.54691 | -56.66484 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 0cfef45e-af6f-30e9-ade0-8400b5a817e1 | -19.54652 | -56.68924 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 27b989fe-b8e1-301f-947d-96fb19fbc163 | -19.54616 | -56.66876 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 01729500-cd05-356c-9a42-c02cb4385f40 | -19.54577 | -56.69318 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a83bc210-e54c-34cd-9c2d-f532ff633035 | -19.54541 | -56.67268 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| a14cc5fc-cdd9-3e74-8dcf-dd7ff4e3dfa6 | -19.54507 | -56.6076 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 460c19fe-cac3-3b65-a20c-e4f41784a607 | -19.54501 | -56.69711 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 9f9a64b2-46b0-317b-8fcb-b5fdab2c1fb7 | -19.54466 | -56.6766 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| e0efed26-5ba3-370e-a73a-5a6e1b310a61 | -19.54426 | -56.70105 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 3b43f795-baf7-3bf4-a796-cda1b3a987f4 | -19.54391 | -56.68053 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| f9ee5410-84cd-30ed-8653-5cf0158161c4 | -19.54315 | -56.68445 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 302a5c6a-70ae-37d1-8eca-88b5dfcf9bdb | -19.5428 | -56.66398 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| b4a4d190-fa89-3780-8f5e-d30c4e1ddb51 | -19.5424 | -56.68839 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 58bc97a9-8850-3d33-ad6d-373135d96bf7 | -19.54205 | -56.6679 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 6ec72e30-e422-3795-9951-be473d585b4c | -19.54165 | -56.69231 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e835bd75-3d9c-3860-b258-04a8c55d379a | -19.54129 | -56.67182 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |


[Clique aqui para ver as próximas entradas](README58.md)
