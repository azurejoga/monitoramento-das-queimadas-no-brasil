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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 873252a3-cfd1-3663-8d22-224d21063b6c | -12.3051 | -57.5605 | 2026-05-05 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 189.8 |
| e2a3d1b6-2f67-3bc2-a9b5-4b7a740841f5 | -13.9926 | -56.6234 | 2026-05-05 15:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| fa549951-3386-3a1d-9102-ee638acd153e | -10.3973 | -49.8629 | 2026-05-05 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 92e3694c-009a-3501-9d7b-1926051e9912 | -12.3051 | -57.5605 | 2026-05-05 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 185.6 |
| e9f1c620-65d4-3e00-bd4e-b911f27387f0 | -12.2862 | -57.5621 | 2026-05-05 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 131.1 |
| ad36e6d1-ecdb-3780-822c-7bb83f981092 | -11.879 | -49.7171 | 2026-05-05 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| ba8e3858-534d-39a1-ae6c-ce02b095fec6 | -13.9924 | -56.6437 | 2026-05-05 15:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 2b922cbe-a281-38e7-80b9-f501d6e46699 | -12.0674 | -45.3229 | 2026-05-05 15:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 029bed27-8475-3519-81b6-b2aafe0e575c | -14.0115 | -56.6418 | 2026-05-05 15:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| de0c19b7-4664-34d6-a37b-e67f6011957c | -12.3321 | -50.0073 | 2026-05-05 15:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 00485b05-4837-3c0b-9740-6f095a20e1a4 | -11.9748 | -49.6838 | 2026-05-05 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 092605da-15ef-3f0c-be70-b79883eff860 | -12.3508 | -50.0266 | 2026-05-05 15:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| a9f13303-8979-37fd-8bba-5c0b7808f476 | -12.3512 | -50.005 | 2026-05-05 15:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 147.5 |
| f62316fd-dea6-3248-b7c9-9e8507bd8ed9 | -14.0272 | -47.5898 | 2026-05-05 15:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| c65194b1-f3b3-3840-8048-fa78f8889560 | -13.9926 | -56.6234 | 2026-05-05 15:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 96478c83-4984-3121-b677-be3f2be9b1ff | -10.3973 | -49.8629 | 2026-05-05 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 73548d6c-d991-3840-b912-6d5d8f46679b | -13.9924 | -56.6437 | 2026-05-05 15:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| db6e9658-bdd8-34de-b386-d695628b58bc | -12.3512 | -50.005 | 2026-05-05 15:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 1eaf6769-4dab-3736-b013-d7fa18064683 | -12.0674 | -45.3229 | 2026-05-05 15:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 6d017e42-3f93-3c05-98c7-d6e8463e2be4 | -12.3321 | -50.0073 | 2026-05-05 15:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 28b2588b-0e0e-32cd-96c0-7b37c1056cca | -12.3321 | -50.0073 | 2026-05-05 15:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| a08a1a22-4298-3463-8682-af17d1e0fa86 | -12.3512 | -50.005 | 2026-05-05 15:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 3a244aed-a332-3df3-9f31-163f47349bb5 | -13.9926 | -56.6234 | 2026-05-05 15:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| ca58b40d-cdb0-3563-94fe-3f49c7821f2a | -10.3973 | -49.8629 | 2026-05-05 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| bdb77568-a625-300a-aef1-bc27d499642c | -14.0272 | -47.5898 | 2026-05-05 15:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| eb2fa9db-9223-347d-9363-2050185f5d70 | -13.9924 | -56.6437 | 2026-05-05 15:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 4213954b-05f1-3d56-bcc4-4c7ae4c3d8d7 | -12.0674 | -45.3229 | 2026-05-05 15:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 2937026f-4cde-3c5f-8010-47211c358abe | -14.0077 | -47.5929 | 2026-05-05 15:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 53.4 |
| d227e86b-6dd8-3f48-8e27-3d871b12a441 | -10.3973 | -49.8629 | 2026-05-05 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 222.5 |
| 49c24d89-1a69-3a08-b729-098bf00f58b1 | -12.3512 | -50.005 | 2026-05-05 15:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| bf505da3-2b94-39e1-9789-19b474b238db | -12.3321 | -50.0073 | 2026-05-05 15:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 7d1b64ef-422a-36a4-8443-c7c48b25a66b | -10.397 | -49.8844 | 2026-05-05 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 0bd7d232-dfe8-365f-9546-390c439cdfbe | -12.5031 | -58.4979 | 2026-05-05 15:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 312.1 |


