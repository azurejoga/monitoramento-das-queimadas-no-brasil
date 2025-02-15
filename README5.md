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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9da0ace-66c4-38fd-8c5c-406683544c9f | -21.95256 | -52.88306 | 2025-02-15 12:38:00 | TERRA_M-T | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 100f8544-e489-3283-87f1-1e38904b3f0d | -20.32077 | -52.43993 | 2025-02-15 12:38:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1d7655b6-5d20-39bb-95a9-5df235ce7ba2 | -16.07791 | -45.87787 | 2025-02-15 12:38:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d6601488-0113-3110-aae7-38cda77d4cc3 | -21.1688 | -51.46624 | 2025-02-15 12:38:00 | TERRA_M-T | NOVA INDEPENDÊNCIA | SÃO PAULO | Brasil | 3533205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 33b80df6-44f7-3ac6-9656-d6dcecc768d8 | -20.15834 | -47.92645 | 2025-02-15 12:38:00 | TERRA_M-T | MIGUELÓPOLIS | SÃO PAULO | Brasil | 3529708 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 48f309cb-7eb6-3115-9982-179513eb26f0 | -19.88322 | -44.89378 | 2025-02-15 12:38:00 | TERRA_M-T | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a73e834b-f1a7-3827-a7a4-4d3349859730 | -22.83441 | -46.33301 | 2025-02-15 12:38:00 | TERRA_M-T | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 7d18df03-ac22-30da-828f-629a53b0f3f3 | -19.02495 | -50.38745 | 2025-02-15 12:38:00 | TERRA_M-T | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 8999934c-a9cf-3db0-94ea-2a4dd8995904 | -21.62681 | -51.78199 | 2025-02-15 12:38:00 | TERRA_M-T | PRESIDENTE VENCESLAU | SÃO PAULO | Brasil | 3541505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 6f1e7469-da8a-36cb-bdec-807f508a90d4 | -22.81179 | -46.28331 | 2025-02-15 12:38:00 | TERRA_M-T | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| f1e8cb32-52d5-3c22-9955-5dcc1696a941 | -21.60538 | -54.69799 | 2025-02-15 12:38:00 | TERRA_M-T | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 2291b7c9-a25c-3970-9e2c-422923cf9f46 | -15.46021 | -42.27784 | 2025-02-15 12:38:00 | TERRA_M-T | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9304491c-96aa-3eeb-9b06-599dd9c3d66e | -18.45313 | -49.64317 | 2025-02-15 12:38:00 | TERRA_M-T | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 9fb655a8-9eca-397a-8daf-5e23d406df59 | -22.80145 | -46.28198 | 2025-02-15 12:38:00 | TERRA_M-T | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 65779a9f-8c68-36e1-b4c2-12eb4de5716e | -22.58161 | -43.63007 | 2025-02-15 12:38:00 | TERRA_M-T | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 44dbb606-163c-3303-ba57-e425033c024b | -19.31868 | -46.05149 | 2025-02-15 12:38:00 | TERRA_M-T | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ff302b3c-5cd4-3a97-b550-579ecbc4ba9b | -16.17598 | -46.58665 | 2025-02-15 12:38:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d9145a98-31e7-3176-8475-4d52e29cd124 | -22.72941 | -48.97217 | 2025-02-15 12:40:00 | TERRA_M-T | BOREBI | SÃO PAULO | Brasil | 3507456 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f26ef5c1-2298-32df-b559-23ed4514cd2c | -21.98237 | -54.06321 | 2025-02-15 12:40:00 | TERRA_M-T | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 56294161-95b1-3853-81f2-bc616c107f9e | -22.11809 | -53.50704 | 2025-02-15 12:40:00 | TERRA_M-T | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| afe2bf52-5682-3769-96b7-efa74f64af81 | -23.30999 | -47.43243 | 2025-02-15 12:40:00 | TERRA_M-T | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| eafc313d-b881-35af-a67b-3f112abaecfa | -23.17375 | -53.21044 | 2025-02-15 12:40:00 | TERRA_M-T | SANTA ISABEL DO IVAÍ | PARANÁ | Brasil | 4123709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 4134c26d-470c-3ca3-b2d5-ae0b211d689a | -23.36168 | -47.51589 | 2025-02-15 12:40:00 | TERRA_M-T | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 1122b8ad-9136-3343-8777-fa8dd91461e0 | -23.11953 | -47.0095 | 2025-02-15 12:40:00 | TERRA_M-T | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| e7badf4c-2a7b-3f1c-87d8-ea0b692e7d74 | -22.30532 | -52.92665 | 2025-02-15 12:40:00 | TERRA_M-T | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| cee957d1-6d2a-31b8-9023-fe82aa9230d1 | -22.5748 | -43.6322 | 2025-02-15 14:00:00 | GOES-16 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 97.8 |
| eaf5a6d1-db71-3db1-93ad-ab0c34615312 | -22.5748 | -43.6322 | 2025-02-15 14:20:00 | GOES-16 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 122.1 |
| 6444415f-0861-3a6f-b16a-990bc7f3c499 | -22.5748 | -43.6322 | 2025-02-15 14:30:00 | GOES-16 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 90.9 |


