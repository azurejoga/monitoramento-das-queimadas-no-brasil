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
| a1552dc1-6e1f-3f99-91b4-1ab882521a0d | -17.29376 | -42.65768 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5eab0557-3d48-34c1-85c8-3cb39a050c99 | -14.03017 | -55.12749 | 2025-06-02 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a251a1cb-d27d-306f-8799-8bc6fda70070 | -17.29448 | -42.65105 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 89314c29-8fd8-323e-99b5-f83bebecaf75 | -17.28431 | -42.65237 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b2fc78d-47b1-311d-96d7-3463942212f9 | -14.53975 | -58.55547 | 2025-06-02 04:40:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ae39e07-cead-3335-9bfb-b28f59058fda | -12.66575 | -58.21842 | 2025-06-02 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9e269f0-8e46-3f7c-b365-1ce2d7c6a3dc | -11.91868 | -54.8217 | 2025-06-02 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74887b63-58ab-3f78-84b0-5f562c556e5c | -17.57051 | -56.79161 | 2025-06-02 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| aa5b2c44-3618-32c6-95bc-68c828e57ccc | -16.02575 | -43.67728 | 2025-06-02 04:40:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 498b765b-db6b-3a3c-96ea-56b9e6965d1b | -17.03504 | -49.77824 | 2025-06-02 04:40:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43a8d9e3-bc84-30d5-a6a1-f73e96b73848 | -13.36515 | -54.2608 | 2025-06-02 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4588f469-26bd-3dea-a0df-7fa33c16d55a | -11.91407 | -54.82578 | 2025-06-02 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9bd5b8e8-8446-3de6-a9ce-d2c21e9a522d | -17.29038 | -42.64621 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea14c410-c55f-3c09-aa31-5ce64bb84b21 | -11.91786 | -54.82647 | 2025-06-02 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b87f8a3a-9dc8-378b-a4bc-7595f18503ae | -15.77594 | -49.30594 | 2025-06-02 04:40:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a8bce0b-442d-3748-a088-c470e179ee2b | -14.5363 | -58.55402 | 2025-06-02 04:40:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a90d97f-89a7-35a8-af34-85e4e3243575 | -17.2908 | -42.64256 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a153d4b2-b239-304c-b588-899983b946cc | -13.69929 | -52.91257 | 2025-06-02 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ad177b7-0981-35bd-b6f9-6e52ff06cf86 | -16.34932 | -43.69466 | 2025-06-02 04:40:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95d7324c-aa86-33e9-8c11-e4ec8bbbf093 | -17.28959 | -42.65307 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecabb2e7-fd66-316e-9cc0-4c2bc524cfdb | -12.67039 | -58.21938 | 2025-06-02 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61460f26-56a3-34c4-b27f-6681d6325a7f | -18.69097 | -46.98309 | 2025-06-02 04:40:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34360e6c-cf67-3ae6-b400-c780ace571a5 | -11.91325 | -54.83055 | 2025-06-02 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8c20bbc7-c588-398d-a75c-6acfb0ec33c0 | -17.28996 | -42.64331 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09a4c1f0-d708-32d7-a769-63636ce8029d | -17.28882 | -42.65382 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d472d42-23f5-3849-bdba-5e41c1598e4c | -17.28846 | -42.6572 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 700b0332-6341-3b1a-978d-e06f863669ef | -12.49763 | -54.41534 | 2025-06-02 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a64df288-2f82-332b-bc7b-7dce4b6ac650 | -14.03232 | -55.13737 | 2025-06-02 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d865068-dd97-3dee-8db1-3dbf8cb37028 | -14.01974 | -55.1209 | 2025-06-02 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d4bc8284-0c9f-36f4-aa19-5416fe4c56ea | -14.01519 | -55.12479 | 2025-06-02 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a41c0729-51bf-3d13-838c-107af0711d3a | -17.29562 | -42.64054 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 022a2fa2-4dc8-347f-9347-e97350dc3e34 | -13.89051 | -54.63177 | 2025-06-02 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef088935-9fb5-371b-9cba-ff2163770675 | -17.28472 | -42.6488 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b00489f5-e7a7-3eaa-aa3f-2988d4a3e585 | -13.70673 | -52.90996 | 2025-06-02 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bdf74df-908a-3daf-8830-5e890f9eda89 | -15.7794 | -49.3065 | 2025-06-02 04:40:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4aa986fa-bd4a-3b9e-9ecc-60208ba1ac0d | -17.29412 | -42.65437 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8315a434-2c6d-3624-903c-a09f28ee4931 | -17.28919 | -42.65038 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 594725e5-e16b-3e9e-8515-cd6d83b0e8d5 | -13.69992 | -52.90882 | 2025-06-02 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d4b877e-7f77-34ac-89b0-3298ddae957c | -17.29522 | -42.64424 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a49ec41b-e29a-35c3-a48d-e9ca7a434370 | -11.91489 | -54.82101 | 2025-06-02 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b33bee16-e3cf-3616-bbe9-1de320ccac05 | -15.57052 | -47.85573 | 2025-06-02 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74acb526-b657-36a0-b0a9-819ba568b9b5 | -14.02483 | -55.13602 | 2025-06-02 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a1f98df-5c3c-3a17-99cf-5ee24883099a | -18.69147 | -46.98305 | 2025-06-02 04:40:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9eb5108e-d330-3da8-aad4-a67ab5d1a4a5 | -13.0793 | -46.74458 | 2025-06-02 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9dde4e5-f6e3-3fc4-b910-d41acab701f3 | -17.28957 | -42.64693 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3947865f-f5bb-3431-af99-b0adac785d4c | -12.72045 | -54.97018 | 2025-06-02 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 198f6227-4f06-3d96-a2f9-a6452689bfe2 | -13.36802 | -54.26571 | 2025-06-02 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 58fe6fe1-a1cf-3947-966b-bcf8c3de907a | -15.77723 | -49.30671 | 2025-06-02 04:40:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ca1d3dc-9297-31c2-8b07-b9708041c2d6 | -13.36441 | -54.26508 | 2025-06-02 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5290cce9-f2fd-36b2-85ae-85cdb8c3a7cc | -17.29074 | -42.636 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9da839a-748e-3a98-a4ac-04fbf734e1b8 | -19.28818 | -55.15977 | 2025-06-02 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ad33a5f-ee3d-38a8-8735-9285f068ad66 | -13.89985 | -54.6651 | 2025-06-02 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8234e1ef-f9d8-3f70-928f-714534963c9f | -19.28539 | -55.15488 | 2025-06-02 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5734d5e0-2bef-38b2-8e49-3985fcf637e1 | -13.7027 | -52.91313 | 2025-06-02 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 391dd76e-168e-3f60-b617-309652a1ccfb | -17.29036 | -42.63959 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ca6108b-0fab-39b4-a115-8a99d5b20dd6 | -12.66365 | -58.21619 | 2025-06-02 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34dad341-3563-30ed-a245-fa0def4bbe68 | -17.62466 | -50.9154 | 2025-06-02 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1330afdb-3f86-3c55-a3fe-cc5d02634e20 | -16.52677 | -50.55803 | 2025-06-02 04:40:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5cc856c9-1b79-3fe4-b1e6-6fe75876c450 | -14.54068 | -58.55066 | 2025-06-02 04:40:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4f53040-6b1f-3251-897f-c535be20c57e | -12.49396 | -54.41467 | 2025-06-02 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aacdbfcb-b5b7-35be-a394-dc6408a4561e | -17.75787 | -52.4387 | 2025-06-02 04:40:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62581bd7-0516-3747-85c6-dc86bf5b0b77 | -13.36876 | -54.26142 | 2025-06-02 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| d3512ef0-3feb-3808-935f-e4c566311742 | -13.70333 | -52.90939 | 2025-06-02 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1b7e7e4-d53b-363d-8ba2-95900b98e7b0 | -14.02857 | -55.13668 | 2025-06-02 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36f5e523-1dbb-380b-bce6-9fcab32c48bf | -17.2892 | -42.65645 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3cbf08f4-b2c4-352d-9233-607237ef183a | -14.01599 | -55.12022 | 2025-06-02 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75139823-4f8b-3c23-9492-065ccbdd14c9 | -19.2917 | -55.16042 | 2025-06-02 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae142658-1544-32f2-8432-1a9e0285f559 | -11.91028 | -54.8251 | 2025-06-02 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| de6f547a-2677-3cb5-80f6-d654a6db9a32 | -12.71963 | -54.97485 | 2025-06-02 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 378fee81-7611-342f-bb5b-ccd75c1b260d | -16.68177 | -43.8834 | 2025-06-02 04:40:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| edbd17a5-19af-3647-9239-0b1944523170 | -20.08504 | -50.97592 | 2025-06-02 04:42:00 | NOAA-20 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1ceca02c-5ebd-3678-8f5a-51f0d9d180d9 | -22.54061 | -48.8136 | 2025-06-02 04:42:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 324d0658-9bb0-3a61-83ee-a563ea5d9e19 | -21.19592 | -44.93917 | 2025-06-02 04:42:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 587a6b4f-5349-3514-bc7e-830d9ce12b83 | -23.33617 | -46.77172 | 2025-06-02 04:42:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e18cc1cb-2d50-3594-8512-918e76e14064 | -20.47753 | -53.67413 | 2025-06-02 04:42:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09c370da-c805-3a96-9726-1752795dd6b4 | -21.25414 | -48.97332 | 2025-06-02 04:42:00 | NOAA-20 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7829661a-5588-3c69-af2b-73118074bc2b | -19.02025 | -57.62285 | 2025-06-02 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 936bb9e8-04e2-3851-9227-d85bedcf3b51 | -22.53815 | -48.81181 | 2025-06-02 04:42:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a141e0d7-7505-34b5-ab64-ed041cca7d94 | -24.24376 | -50.7381 | 2025-06-02 04:42:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| de0716b0-23e3-32aa-a528-28862190aabc | -20.76169 | -46.76969 | 2025-06-02 04:42:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b7aeca00-1804-329f-a1c2-481845be68d2 | -20.76173 | -46.76825 | 2025-06-02 04:42:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cffd71db-97a2-3806-895f-3289b872773c | -23.42309 | -47.29332 | 2025-06-02 04:42:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0264ce31-14a0-3b64-8306-82d59d329a81 | -27.01443 | -51.27767 | 2025-06-02 04:44:00 | NOAA-20 | IOMERÊ | SANTA CATARINA | Brasil | 4207577 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7e395ebc-72f6-306c-987e-5f3aef428607 | -10.81447 | -56.94118 | 2025-06-02 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b4baa09-09a8-38d1-83fb-9b29a8a0432e | -10.82318 | -56.94239 | 2025-06-02 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d4bc88e7-41c7-3a46-83e2-50d62a0da8e0 | -10.81069 | -56.93635 | 2025-06-02 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d90b1580-8e9c-3639-acee-f5079c65bc3a | -11.45102 | -55.00812 | 2025-06-02 05:29:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d695c29c-fd39-3643-9a24-087cf3bdff0e | -11.44601 | -55.00738 | 2025-06-02 05:29:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f5f1982-cf2a-3c4e-9e60-48bd3262b29d | -10.8339 | -56.96137 | 2025-06-02 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2288f494-85d9-3e8d-a632-0c1a8a0d29f8 | -10.82955 | -56.96076 | 2025-06-02 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09b1c6bd-3a0c-3a53-aaa8-7e7f360a68e9 | -9.58692 | -63.5025 | 2025-06-02 05:29:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a6334b8-5ddd-3c73-853b-d8d83fce2ae5 | -10.81012 | -56.94057 | 2025-06-02 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a6ece5d2-ea08-374b-b9ee-47b5595e102b | -9.57941 | -63.24688 | 2025-06-02 05:29:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8af26e92-e281-3fa0-a35c-ae7049adf8dd | -10.80955 | -56.94479 | 2025-06-02 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 880c539b-edb7-3409-9000-3ae97677c4df | -9.93192 | -59.90494 | 2025-06-02 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ca94d52-cc45-3595-8a75-b42806ea771c | -11.44591 | -55.00861 | 2025-06-02 05:29:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d89e4454-972d-3935-b7c4-09dc7bd8bbec | -9.61391 | -65.2723 | 2025-06-02 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 831da140-c004-3986-b2a7-7ba762530e31 | -11.4513 | -55.00639 | 2025-06-02 05:29:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd6e7c6d-da90-36fd-87d0-47b260035d9d | -10.82261 | -56.94662 | 2025-06-02 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b82caadd-0dec-3fe4-b062-52e65be56ba0 | -10.83071 | -56.95227 | 2025-06-02 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README8.md)
