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
| f5152a6e-c390-3a50-8207-cf6bfc549a2c | -19.57611 | -57.00258 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 593d2a2b-88d6-3d16-a25a-307e63aecc7b | -19.57139 | -56.61819 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 31.6 |
| 544a255f-17db-3419-9a7a-0da5efde75f6 | -19.57033 | -56.69365 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 42.5 |
| 31703898-ee36-33b9-8699-636dd30e686a | -19.56988 | -56.60593 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 0fdf4831-6981-305c-9605-bc2784bd7dda | -19.56882 | -56.68125 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 5f2b6c31-39be-3647-b471-caa378319601 | -19.56838 | -56.59368 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| af8f2ded-fded-330b-ba6e-b2ca56b23a1d | -19.56732 | -56.66888 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 1f2a58e7-5cb3-3357-90b2-229bc1e41524 | -19.56688 | -56.58145 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 04c92ff0-e1d7-385a-b4b0-e3060f5ee210 | -19.56581 | -56.65651 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 9ec50927-0caa-3214-be15-f7c290edc68c | -19.56431 | -56.64417 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 29.2 |
| d44131a0-40e0-314d-919b-066cbd1a659d | -19.56388 | -56.55705 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 27.5 |
| e60c193a-700f-3608-a6d7-39f0cca1b29e | -19.56281 | -56.63186 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 63046ee7-b623-3ceb-a97b-062bee590d8d | -19.5613 | -56.61957 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 47.5 |
| 32ab40fa-01c8-3ed8-a82d-bedda6715439 | -19.5602 | -56.69503 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 077e7e49-5550-3ebe-8188-7fcabed1c04c | -19.55981 | -56.6073 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 44579b9b-2dc0-3024-b25d-1aedb2d3bde3 | -19.55869 | -56.68262 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 40.6 |
| 764524fc-272a-34a7-bc7e-5a95f7df8cbc | -19.5572 | -56.67025 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 9e3e58cc-b8ce-3fe1-93cc-7e3b4e1f3184 | -19.5557 | -56.65789 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 24.7 |
| 73aa5cb6-48a3-33b3-9a1a-89b267aa3f08 | -19.5542 | -56.64555 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 708564b1-3f02-3870-89d8-6dbe20718a47 | -19.55155 | -56.70883 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 3b4783a7-0f15-3e04-9072-25fdfed1cd5a | -19.55122 | -56.62094 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 0372a815-1c58-3300-9c55-77bdc33747e6 | -19.55006 | -56.6964 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 35.2 |
| d8698bfe-7d03-33da-a335-9b7e5cbee824 | -19.54973 | -56.60867 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.6 |
| 81cb86dd-784a-3d1c-be7f-f952f3933769 | -19.54857 | -56.684 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 40.0 |
| 75582acf-d04f-382c-b43f-6bf88cc4216b | -19.54708 | -56.67162 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.0 |
| e5671fb3-eecd-3418-b707-01f2f8777952 | -19.54559 | -56.65926 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 123d71fd-5dc5-30ef-a1c7-40137c4e2781 | -19.54141 | -56.71021 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 0cdf0602-8e81-3c24-94c7-f5dcdfa8d535 | -19.53992 | -56.69779 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.7 |
| cc05b951-50fc-30f7-ac7c-f06fdad76397 | -19.53844 | -56.68538 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| b189be55-eeb9-3dcc-a352-60e676274e6c | -19.53696 | -56.673 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.7 |
| b3ba6920-7a48-39ca-b571-10189061bec6 | -19.53548 | -56.66064 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 38.2 |
| 88f42049-cc96-3edf-8139-d5357e44df80 | -19.53127 | -56.7116 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| fa964faa-c2f8-3056-9935-af4090dd095c | -19.52979 | -56.69917 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.5 |
| 79e3a296-32b4-36de-9896-7b2c670ffd80 | -19.52831 | -56.68676 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 70e1a116-7c22-3fcc-8245-d824f549e03b | -19.52663 | -56.58693 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| d787eb3b-31b5-38f5-881a-ee9fd47bf09a | -19.51526 | -56.66339 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 6576e95b-5a13-3ce1-933b-51c07d002d89 | -19.50672 | -56.67086 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.2 |
| 100d3762-f3eb-3a09-919d-3e5e9564805f | -19.5066 | -56.67713 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 7747362e-df7e-390a-94a2-44a97d82c2ba | -19.50519 | -56.65853 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.4 |
| e9e3a34b-5123-3d20-a10f-f7804190b748 | -19.50515 | -56.66477 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.2 |
| 8ff2cf30-8d45-3ee3-a84e-1b7009dc571c | -19.50369 | -56.65243 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.3 |
| bef353da-2f1e-34af-84b9-5c8e3606a6be | -19.50366 | -56.64622 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.5 |
| d9f17712-194a-3681-bf19-9cfc14a4d4a3 | -19.50224 | -56.64011 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.0 |
| 007da9d8-d876-3815-a06a-98db0131c55d | -19.50214 | -56.63393 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |
| b529eca5-cf12-3fcd-a3ec-d451e8eba41d | -19.49509 | -56.6599 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.7 |
| 91a8d4ae-0d32-3e62-9ad6-8adfb60a8119 | -19.49357 | -56.64759 | 2024-10-24 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 0d214e14-3e4f-3172-9738-b0856756ea44 | -18.67092 | -57.35685 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 4e56fb82-c0fc-3897-8610-2f77859e250c | -18.66532 | -57.3637 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 491d125a-acc9-3a2f-93ee-ce90c9fa7c8b | -18.66371 | -57.35047 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.3 |
| 8406f8c5-b579-3265-8e46-3126e0f4096b | -18.65164 | -57.33864 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 07a90c71-257f-3650-ac8f-ef9cbde43e63 | -18.31915 | -56.21547 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| d6f06409-58c3-3719-b77a-e315a9f20e6d | -18.31774 | -56.20431 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.4 |
| a889b266-6c92-3133-93c6-40b79727167d | -18.31228 | -56.2392 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.8 |
| 29e9e712-361d-3408-8a42-b8eec16dd9da | -18.31211 | -56.15981 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.5 |
| b2f4636c-69fe-3ad1-be27-250759faf5e9 | -18.31088 | -56.228 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.5 |
| 52a3e93a-2791-31d4-8bd0-5474b8081fc6 | -18.31071 | -56.14872 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.7 |
| 2b240a86-83e1-3690-9c38-5bf149c39417 | -18.30931 | -56.13765 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| ef269291-a681-3f16-833d-d77b5ab74cd5 | -18.304 | -54.61524 | 2024-10-24 01:24:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ea0bc571-014c-3e0a-b7d7-920b0610baef | -18.30272 | -54.60565 | 2024-10-24 01:24:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| be8c4f2f-166a-3616-9231-e083cd3173af | -18.3026 | -56.24055 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| f844ec8c-1cf2-3193-a415-31ec209ba414 | -18.30247 | -56.16116 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 97dc5b7b-7990-3eae-bd72-4080660aba33 | -18.3012 | -56.22935 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 39b57a0e-8000-3776-9d6d-d400c3cbbef3 | -18.30107 | -56.15007 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |
| e0806a30-bb0d-3bd1-907c-ec26b62cc4b5 | -18.27897 | -56.05231 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 181724f8-0b82-3d1c-9d0f-dbd9d56f220b | -18.26939 | -56.05366 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 56acd111-b8b1-3008-9348-2723837ea7a1 | -18.26118 | -56.06596 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| da706e7c-5c64-3b2f-a78a-21e029767e05 | -18.25981 | -56.055 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.5 |
| b1dc942c-a1ab-30f7-a197-636d9bcaf5e4 | -18.17797 | -56.31588 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| f57593fc-c2d0-3231-b702-e6e0e8734d47 | -18.16826 | -56.31722 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 36af4096-96f1-337c-a754-1cabc0bb05a4 | -18.11137 | -57.32751 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| c41444f7-3c2e-3375-877c-daf86f6e2f75 | -18.101 | -57.32889 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| a6715fb4-108f-352d-8268-d25fd312f0d7 | -18.09942 | -57.31598 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| e2c1a84d-4df1-3503-bf5d-7d6002cc6a29 | -18.0875 | -57.30448 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.3 |
| ddf83904-01be-3ca4-b979-eb0d19abc393 | -18.08594 | -57.29163 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 54eee5dc-026d-34ab-9bae-f9354a834048 | -18.07146 | -57.34595 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 89322572-e6f6-3527-9125-f739e49e6c19 | -18.0699 | -57.33302 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 00c7bff4-9faf-32a7-9ae5-207592858bbe | -18.06218 | -57.26875 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| c21bad7d-83d7-3d6c-922c-701f5ff6dd1f | -18.05492 | -57.29575 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 8ab88abc-95df-3835-914a-040a2fead344 | -18.04611 | -57.30999 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| a104aaef-7c9d-3841-9133-1f802ea23364 | -17.95481 | -57.22414 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 1d1582c2-314a-3f3d-af74-8141e8408d36 | -17.94303 | -57.21287 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 16e1843d-ec18-33ec-8ce7-38abe5403b6e | -17.93578 | -57.23958 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 55582b78-f26e-3e94-b63f-b64f4a4b2589 | -17.93427 | -57.2269 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.9 |
| 4f9296c1-e576-395d-a95c-2bce5ef5b53e | -17.93277 | -57.21425 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |
| a1acebec-bbfa-38ff-a192-f6245ac9ef70 | -17.92864 | -57.24682 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| e15842f8-391d-3cd3-a426-10e2b242a068 | -17.92706 | -57.23417 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.8 |
| 9d594f88-04ac-34b5-98fe-9a056aef1ab7 | -17.92699 | -57.25364 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 45fded7a-f171-395e-a77a-80b33316157c | -17.9255 | -57.24095 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.4 |
| a77396a6-a809-30fa-8b07-7f3f56c6cb70 | -17.924 | -57.22828 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| e9ebc814-28bd-30c8-a1a2-1c2656236352 | -17.87417 | -57.22838 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 127f326a-7ded-3b0c-9b60-670d188fb763 | -17.83573 | -57.58146 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.6 |
| 544b1edf-3efc-3f6a-9ad0-31df3ed6b848 | -17.83414 | -57.56822 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| b20f4808-7687-3a70-8048-ff6f602e0f32 | -17.82681 | -57.59618 | 2024-10-24 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 87b8431d-9345-377d-9261-cd2179c2033b | -16.75112 | -50.71138 | 2024-10-24 01:24:00 | TERRA_M-M | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 8f170ed7-080e-378b-965a-4ed6474bb2ae | -16.75031 | -50.7173 | 2024-10-24 01:24:00 | TERRA_M-M | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| bffe8b73-ab17-3b39-9852-21e413b9e3e1 | -15.68618 | -51.39049 | 2024-10-24 01:24:00 | TERRA_M-M | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6683b35c-554b-31b3-aac7-7ab26326fd5f | -14.92281 | -45.13719 | 2024-10-24 01:24:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 85b0b4a2-9e4a-3866-b37f-505c47608198 | -14.91703 | -45.10567 | 2024-10-24 01:24:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 49.9 |
| a73dfbbf-5d29-39ec-be9a-5168db36435b | -14.56043 | -49.72694 | 2024-10-24 01:24:00 | TERRA_M-M | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| f696a45b-96bd-3e45-aacc-a620ecb8cdb9 | -14.55851 | -49.73266 | 2024-10-24 01:24:00 | TERRA_M-M | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |


[Clique aqui para ver as próximas entradas](README8.md)
