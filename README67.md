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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9c9ce50-1520-3ab0-a5c2-4f2c71b8927d | -8.6043 | -46.53969 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 504c962f-af6d-3172-8d43-64c063310d8e | -8.4215 | -46.31727 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 426b507a-5b01-3495-99ce-f1b56aae111b | -8.42115 | -46.3195 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ab4b8a3-57cd-3336-a271-544e855ab820 | -8.41545 | -46.3238 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40b535f8-d371-316d-b28d-b32cf14d708a | -8.41493 | -46.32677 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a50a58a5-cb80-3237-b4af-bb7983db1679 | -8.41451 | -46.32897 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 09c87a69-4990-3af1-ac1c-54a7afc491cf | -8.38107 | -46.37955 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cefa4b67-c4f1-37e6-9e5d-f32f16fb1cb5 | -8.03243 | -46.06353 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47452367-2fce-36ec-86ea-beda64304749 | -9.0673 | -46.08849 | 2024-10-02 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e17d34d0-7c2e-329b-b0e2-08cd47334e69 | -8.62773 | -46.54087 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4517861-25e2-3cd2-8166-4df578876618 | -8.60913 | -46.54062 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eae89ef1-ea88-3ec7-a5f3-aab9fc73d719 | -8.60267 | -46.54161 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a622fa6-4fad-35d9-b1e1-d23a85dc6667 | -8.59857 | -46.54406 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26f7b4a2-8afb-3e30-8904-51084c7821b6 | -8.59465 | -46.53792 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bffbfae9-48e8-324a-9b45-f4d7cfe9ffa0 | -8.59374 | -46.54313 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8d036a7-9044-348c-be1a-ada7d6402b0f | -8.41582 | -46.32162 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8cf92847-62a2-39c3-93af-f12b5fbe6bd5 | -14.79702 | -48.77996 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60ee7f89-adc8-36b4-a5a8-80a783a77ca1 | -13.12979 | -51.22771 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 59423b90-8bb8-37db-897f-1ac5994a121c | -13.12424 | -51.22988 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5253fde-8eab-32cd-858a-2d7dd87f2953 | -13.12284 | -51.23103 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd7d883c-243a-3705-ab59-6eb4e2a1a0c3 | -13.11975 | -51.43615 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d9f3fcd9-f378-327b-9432-16e6e98aee5e | -13.11876 | -51.44094 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 644db056-aa34-3ee1-b040-6282af3de1ac | -13.11267 | -51.43961 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c5160f2e-c24d-3023-8238-a851e00a8d14 | -13.10854 | -51.42868 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bb84c05a-b376-3ee6-bdc0-003ef09d6843 | -13.10756 | -51.43348 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 243e71fc-fd8c-3899-bcf5-f37422883a12 | -13.10657 | -51.43828 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 19cb9a60-7533-3b9b-92e1-9ee8416f4db1 | -13.10245 | -51.42735 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0a04e231-221a-3e29-b6c8-3dc9da9ad82a | -13.10146 | -51.43215 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8e43c03a-0a07-3a2c-80d1-23ef13cfd1d8 | -13.10091 | -51.19092 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 016ff67b-9767-35ff-a76c-062859f6d944 | -13.0993 | -51.19187 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b52089a8-2a08-344d-ab37-d10fc8daaac0 | -13.09916 | -51.38169 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbb67a60-181d-3cf3-95b4-35f34354e421 | -13.09876 | -51.38329 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fded67c-daa1-3e22-9c4e-65b42c025718 | -13.09818 | -51.38645 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3dc5913-82c7-34a4-80dd-857a4bf126ff | -13.09735 | -51.42121 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b5a49e9-e14d-3ae3-ae4f-781698684eee | -13.09719 | -51.39122 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b57ffaa-6c7e-3428-af8e-639ddcb958d8 | -13.09636 | -51.42601 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e026cb8-8201-3279-95e3-e45f367b405b | -13.09364 | -51.37717 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ae8cb22-4457-342f-bdb3-580c11d19af9 | -13.09309 | -51.38036 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 963ac56d-be8a-319f-a514-2f8595dbe03f | -13.0921 | -51.38512 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ac5e9dd-c6b4-337e-97d6-cd28e0c53560 | -13.09206 | -51.41679 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96061bec-3261-31df-a901-9d9713ea93aa | -13.09173 | -51.38671 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e14ccf37-ae8d-3f14-8288-56f566104855 | -13.09111 | -51.38989 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa8f6e39-20f9-3ed2-b239-cbd96a52e73b | -13.08715 | -51.40899 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 681e916f-81e2-3c57-a065-e44eeff74261 | -13.08693 | -51.41065 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86403078-76e5-341e-bb15-f9f4ac94c873 | -13.08616 | -51.41377 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8eecec5e-1e74-3295-bd42-a3b2f9c81ca7 | -13.08597 | -51.41545 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bb0784b-65b8-39ff-86c7-aa6a2ed53799 | -13.08277 | -51.39972 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 740cb87b-07f4-3099-afcb-17e06b46c992 | -13.08205 | -51.40289 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9eb5ff9c-5541-3fc5-8201-16dae4613910 | -13.08181 | -51.40451 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b74a3464-c8a7-3b1e-be89-7a79c169a1d5 | -13.08106 | -51.40766 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1583955-a9ed-3929-8d9b-1ab6c8aa26aa | -13.08085 | -51.4093 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a8b46e27-2d78-3ec1-b848-eacde254ecf9 | -13.07669 | -51.39837 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca31bc88-33e8-39c6-b01d-19eb61c5b541 | -13.07572 | -51.40317 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ef5769c-0d8b-3ec1-8219-a3381268270d | -13.07497 | -51.40634 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10d83d4b-67fd-3fe8-9a11-47da253e8832 | -13.18159 | -51.25708 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff682a04-cbca-3140-acb1-ac24f96578ec | -13.18064 | -51.26175 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 41043d5d-c7dc-3af5-a522-653745fc93f9 | -13.17557 | -51.25574 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28bde255-7f11-3f9f-9bc1-d7b0eaa45051 | -13.17049 | -51.24976 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c9d4ead-4ca7-37e5-bd05-4ad324b2cfa7 | -13.16955 | -51.2544 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2892d01f-275b-3d03-ae72-7a3ebf44a225 | -13.16447 | -51.24844 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30f9720c-b6b9-3bba-856b-4b760033ccbc | -13.1594 | -51.24246 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b6bc3ab-f822-31d0-8666-32a37ba148f7 | -13.15845 | -51.24712 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9859ced3-78e9-31d7-af6d-538ade90faae | -13.15338 | -51.24115 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 675ab594-eb0e-3658-8d73-8af81151d532 | -13.15243 | -51.2458 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7937f949-6e2f-323c-99be-6cd926e2317a | -17.68878 | -53.21167 | 2024-10-02 03:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9bbf36a8-5dd3-354c-898b-8c75c5b4cf62 | -17.68601 | -53.20773 | 2024-10-02 03:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3bdc6cc-c8d3-31e0-be4e-843b807235e8 | -17.68483 | -53.21312 | 2024-10-02 03:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5cc125c-83ab-3215-994e-429470e21d78 | -12.54976 | -53.13828 | 2024-10-02 03:55:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7dce008f-f64c-3b78-9ae7-b7e90ea9e27b | -12.54848 | -53.14431 | 2024-10-02 03:55:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3acde9de-7cda-3a3c-ab0b-c5ceba754dfd | -12.5417 | -53.14274 | 2024-10-02 03:55:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee3b2b0a-3fa7-30d8-8f30-aa1e66ae6f6a | -12.53623 | -53.13499 | 2024-10-02 03:55:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b69fc445-974a-3e35-bbe2-38dcaba691e5 | -18.89022 | -54.50772 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78498d27-9cac-3329-9345-e557bb2e0cf0 | -18.8883 | -54.50673 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a5963c8-9eee-39d8-aea2-94cd4d630e60 | -18.88763 | -54.51898 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ea33fa32-4058-31a0-8199-f287e2855168 | -18.88701 | -54.51214 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8b928a8-a469-3ac8-97cb-ab5339c78162 | -18.88637 | -54.52447 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0b7496aa-31cd-315c-a1ae-63a2dbcf5522 | -18.8857 | -54.5177 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99c71bf4-b420-317a-9812-a95b1d18cd67 | -18.88441 | -54.52311 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 319bb295-14b1-3bb7-86d7-496450450f6e | -18.88379 | -54.50561 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e10b457a-3102-3116-87a3-830ff6107b98 | -18.88192 | -54.50444 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1886db2b-ab9e-3f1f-bed6-c83abddbf020 | -18.88005 | -54.5218 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe4490d6-4501-3160-8de4-19eb27338d4b | -18.87805 | -54.52073 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c78abd5-e214-3612-a610-4347b45251eb | -14.33342 | -43.54839 | 2024-10-02 03:55:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5bb8dfd-aade-3d56-928b-870b093ed7f5 | -17.20487 | -39.51145 | 2024-10-02 03:55:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 64f5eb0d-09a7-3e14-b392-1c50734a683d | -17.20152 | -39.51088 | 2024-10-02 03:55:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| deba6482-77da-345e-a7c7-199bd0e1a269 | -18.04119 | -39.92537 | 2024-10-02 03:55:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4613f1f4-a5fa-349e-af60-8685a1070816 | -20.31601 | -40.39468 | 2024-10-02 03:55:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2fcd36d8-d355-365d-9de3-301e3d8fa8b3 | -19.55271 | -40.22459 | 2024-10-02 03:55:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 906274d4-9d0d-38ae-a587-d4a03325236a | -19.54936 | -40.22403 | 2024-10-02 03:55:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6b03de17-a65b-3b36-975e-a89d88ba10da | -15.65596 | -40.25142 | 2024-10-02 03:55:00 | NOAA-20 | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0f722da9-b60b-306c-8653-3948d955657d | -16.37765 | -40.54346 | 2024-10-02 03:55:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| d06d939a-6161-368e-98db-ab5068c9c2d7 | -17.84171 | -41.42367 | 2024-10-02 03:55:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5ad51b3f-daac-36d2-9b28-182196dbb387 | -17.77399 | -40.53628 | 2024-10-02 03:55:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6cf257ad-3dec-3647-b922-f7dfa9e9408d | -19.43538 | -41.37615 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4cc6b086-14bb-39fa-a3cd-7eca6196cf9c | -19.43481 | -41.37981 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7d57d2cf-6a0b-3c49-a124-dd3570f26ba9 | -19.43265 | -41.37191 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7640b3d6-c342-3d95-b6db-06d182903ddc | -19.43208 | -41.37557 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| eaf04bc2-a798-351d-bc85-48a5af1cf02b | -19.4315 | -41.37922 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1c6470ea-d6be-3057-8438-010d64cf7c9c | -19.42934 | -41.37133 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8d5390a9-0886-303e-9510-6ada3be68228 | -19.42876 | -41.37499 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README68.md)
