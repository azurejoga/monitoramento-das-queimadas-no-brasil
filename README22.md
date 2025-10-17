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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 006169be-c54b-3658-86ce-2b53f9362a97 | -7.10706 | -44.74007 | 2025-10-17 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fcc50cd-8d16-3640-bb26-7d7585e07fbd | -8.60744 | -40.19959 | 2025-10-17 03:28:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 256982eb-9a36-3e46-9ad2-92afd1f3c4f5 | -5.90548 | -44.74625 | 2025-10-17 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a3aa465e-8e93-39ee-bac7-9188c81c5e39 | -6.14189 | -41.79333 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 209dbf46-786e-31d6-bf5c-fb707e5b0e07 | -6.38106 | -41.47554 | 2025-10-17 03:28:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 59daa1c0-305b-38d6-9ce9-d3002aec3c30 | -6.08718 | -42.39477 | 2025-10-17 03:28:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 76a2ad32-4048-32dc-91ff-3aff7c37c888 | -4.3882 | -43.40248 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 00531669-5e23-3e66-93c3-76552dd66d39 | -9.45438 | -40.58745 | 2025-10-17 03:28:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f339ff7d-df14-3a8c-b3a6-27919021dc85 | -7.2924 | -41.95425 | 2025-10-17 03:28:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 65c333a0-12d5-36f0-a827-da9f34725da0 | -8.7233 | -43.87154 | 2025-10-17 03:28:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9819e297-0960-3041-be34-f0a12fba7b5f | -6.99105 | -39.23475 | 2025-10-17 03:28:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 72d7061d-d63c-3d5e-8663-78e2333fa588 | -5.85118 | -42.34324 | 2025-10-17 03:28:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1d00d445-5fb6-30cb-8ce6-49f5a7d54a60 | -6.94372 | -41.56538 | 2025-10-17 03:28:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b453fde4-e3b3-3ab5-bc6c-238602565d19 | -4.81178 | -43.20761 | 2025-10-17 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 079bb737-58ac-3e26-ae41-8764e1ee2f31 | -8.4066 | -46.29779 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80c2b92c-0463-3cb4-961d-725acb4d1512 | -7.02753 | -41.82253 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4539e640-9f70-3979-8582-45a6c1e47ad8 | -8.12175 | -45.55951 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e1f4ea5-aa57-3930-b40c-1278b56154f2 | -7.05471 | -45.06199 | 2025-10-17 03:28:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 962aff50-bfc9-3f56-8e5f-b24e12df949c | -7.95093 | -44.1329 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c249e7e-46e7-3c77-a01f-144fc149a8df | -5.85556 | -43.87066 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 524a3079-e6b7-3882-88ae-f8ac9480f99a | -6.1782 | -42.62432 | 2025-10-17 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 59ecaefe-c16f-3cd1-a6d4-185715ceaccc | -8.2585 | -44.09171 | 2025-10-17 03:28:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3f264afd-385d-3af9-9f1d-c93f85e23bff | -5.87888 | -43.92491 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9feba5d7-10a0-39a0-b33f-5ce7d64f03d9 | -6.12973 | -41.74685 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b902b6d6-55b8-35c0-9933-e2182edeecc2 | -8.37798 | -46.25514 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f4b1eccb-096e-32a8-b09d-a7dd31178acb | -8.25509 | -44.07531 | 2025-10-17 03:28:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54f0e78c-4dc3-343d-8ffb-af23c4f27758 | -7.17255 | -42.37239 | 2025-10-17 03:28:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1db13dc9-ac7e-3450-a821-a18abf856196 | -8.07645 | -45.42502 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 526340f7-7a00-376b-b8ee-a0bc087dc300 | -6.03104 | -41.90871 | 2025-10-17 03:28:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e7e6260e-7aae-3f66-9c38-c23452fb52b5 | -7.84011 | -45.46755 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| adf07ad8-2530-33cc-8582-a1f85e63df71 | -8.30627 | -43.42986 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f4790fb5-5c6c-369d-9760-9ad063569b5c | -3.98073 | -42.49597 | 2025-10-17 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 88550516-aeda-378c-bdf3-1f0ed0bc2d06 | -5.45315 | -44.64656 | 2025-10-17 03:28:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 475e32dc-bc97-361f-8796-f2e500791fe4 | -6.13521 | -41.73415 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 00eff177-3def-32f4-b536-4e36008351b9 | -6.13399 | -41.75569 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e1b18fdd-6f4c-3007-938d-29688360503e | -5.90981 | -44.75159 | 2025-10-17 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1564e9ce-9b78-3f89-956b-fe72bfc4ffe0 | -7.11258 | -44.7475 | 2025-10-17 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c0dd57c-7094-36a3-9e92-e3f8b502a7b9 | -5.88528 | -42.81932 | 2025-10-17 03:28:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| efc6f580-30dc-32cb-b338-a9810111f49e | -6.34432 | -45.48827 | 2025-10-17 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 42751e50-46b1-32af-b2b5-8f542ef170a6 | -5.90876 | -44.75743 | 2025-10-17 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7d6dbf4c-87de-31d9-904f-af78f24ca4d5 | -5.87813 | -43.92785 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33a3799a-f289-3777-8392-14cf49f556b6 | -7.94797 | -44.14818 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cc7dd8d-8507-3008-99a9-31183ff8758c | -7.73077 | -35.11678 | 2025-10-17 03:28:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a0c8c983-8c03-3225-a33e-e215abddcc3b | -6.40191 | -41.48607 | 2025-10-17 03:28:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 50078bb5-907b-3159-8076-3592fc42d54e | -7.41082 | -44.75627 | 2025-10-17 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be86a1eb-104b-3387-abbe-de796346edb1 | -6.42172 | -44.71858 | 2025-10-17 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60287f38-449f-3e9a-ba2b-c3642b96fcbc | -7.1103 | -44.74133 | 2025-10-17 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cd084e7-a163-3661-8b42-5c5c1399daab | -7.46917 | -42.16422 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3452c21a-7271-3878-bea4-a268288c33b3 | -8.4024 | -46.22485 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 827544c1-56dd-3d3a-be8e-4c2d0178afe4 | -8.30298 | -43.4477 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5b605170-d5ea-3ffc-bb2d-45f6fe9ea23b | -3.84384 | -41.57344 | 2025-10-17 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 80d12a2e-eb0f-335a-bb63-aaf34c537f85 | -8.44574 | -46.24784 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2f69f538-dc46-346b-af96-a408c3d3fda5 | -5.24727 | -43.60592 | 2025-10-17 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3c5bd80-e7ef-35ce-bfcc-fb33e379af2e | -4.38274 | -43.39597 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 066b4af0-2487-376f-bd4f-b5402a990c70 | -7.34121 | -43.86826 | 2025-10-17 03:28:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2a319c4d-48a9-388d-98f1-79c0fa993e23 | -5.89284 | -43.20218 | 2025-10-17 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1d07db5e-6379-300c-b685-89478c4412b9 | -7.3515 | -43.86515 | 2025-10-17 03:28:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cfc6b434-28df-3690-9ee0-20ddf971a960 | -7.47764 | -42.76085 | 2025-10-17 03:28:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 74ce11ed-8a39-3912-b009-91f30b813d37 | -4.39824 | -43.42054 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3350908d-bf3d-3abd-88eb-6798af20b8a1 | -7.16971 | -42.52055 | 2025-10-17 03:28:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f45d3d3f-5157-31a1-a86c-fb2179f9c21b | -7.28121 | -41.95227 | 2025-10-17 03:28:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7282c76b-10b0-335b-add7-c3a90c233616 | -3.62272 | -42.77744 | 2025-10-17 03:28:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59ad21aa-9210-31e7-b8f3-e2a72fe3433d | -5.89149 | -43.20122 | 2025-10-17 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7dd69d59-1c62-3cdc-ab34-66ceaac55f02 | -8.30379 | -43.44328 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b4716119-f284-304a-afe2-3efce6bf7175 | -8.41637 | -46.28548 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8b3c105-d988-371b-a59d-f23584e7ebb0 | -5.52799 | -41.33041 | 2025-10-17 03:28:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fa3c8c2a-16ea-3020-8a0f-cde742223b7a | -8.27516 | -43.3625 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d86f5fef-abef-316d-9104-5aeadb730f2b | -6.13402 | -41.77259 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f50fded5-078e-3da7-8f06-393da24d8912 | -6.14929 | -40.91967 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9a53cd98-a039-3574-82b3-451996515731 | -6.35063 | -41.51916 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 63977980-850b-3d76-90ec-f36673ff600d | -7.18048 | -42.36134 | 2025-10-17 03:28:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f5ca4f96-d03f-314b-a7e4-fb9a538a741f | -8.33676 | -46.23962 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fb0f7cfb-9db9-32d7-8637-fb6494d707c6 | -6.31772 | -40.93906 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 771608bc-156f-3882-b2cd-9df4eb50c855 | -6.09447 | -40.88844 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6d97927d-3ef2-32da-bec1-1b428db4cf21 | -7.95193 | -44.11427 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a36e7d05-7e27-33ad-b402-38f80e6df150 | -7.4674 | -42.65929 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6c20b5fc-7d21-39ce-a80e-9c9d7742ef5a | -5.89368 | -43.19742 | 2025-10-17 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 42c8744d-929d-3833-a9c0-d797dd888a63 | -10.01848 | -37.39137 | 2025-10-17 03:28:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b53171dd-68bf-342d-b9f2-8471834e66f0 | -6.32067 | -43.62482 | 2025-10-17 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e404b5cd-37c7-3006-bdcd-3f481380b1ec | -8.41298 | -46.28246 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9bfece46-bf02-3223-bee5-77c6fe3f9b8c | -6.69224 | -40.86806 | 2025-10-17 03:28:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8d1149b8-dfbd-3076-9cbf-97cbab1ebe6d | -8.55369 | -44.58671 | 2025-10-17 03:28:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4aeff1b-6ee2-3e1e-abae-fdee41f557e7 | -6.33744 | -45.48615 | 2025-10-17 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7ca68a5-f9f3-3b2c-bde4-3b5b372f13b2 | -6.34189 | -45.48676 | 2025-10-17 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac92ad9f-b22b-3b40-9852-0fad8c45d7ec | -6.02032 | -41.9356 | 2025-10-17 03:28:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7b62fd74-fc29-34fc-96e4-f4ef038abf0e | -5.87928 | -44.76514 | 2025-10-17 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 41444ef5-23ab-3037-9f2d-c99c35804a52 | -6.13913 | -41.72624 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e3f3c89c-8269-3c3a-b894-9007b2b7660e | -6.82944 | -41.69432 | 2025-10-17 03:28:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e55e34d3-bf03-3a49-a689-273fef8a6f0a | -7.94759 | -44.11627 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aad70830-bfb0-3161-975e-1446c80a8187 | -7.29306 | -41.95063 | 2025-10-17 03:28:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| efd03a08-cac6-3c29-ba6e-2a70b81f2b2b | -4.96172 | -44.96417 | 2025-10-17 03:28:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c148156-425c-3484-9dda-8584a44e17f0 | -7.46291 | -42.15108 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 663aeafc-a91a-36e3-b5b3-a9d39fb0bf0f | -6.82396 | -41.69297 | 2025-10-17 03:28:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b531a563-2534-335f-afb9-e88616ac77b1 | -8.24852 | -43.3388 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 83b60bb1-d320-312d-921d-4228aa6eb842 | -5.85669 | -35.47608 | 2025-10-17 03:28:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 957c7efe-74f1-3dda-9c51-2b7699a184b7 | -8.29321 | -43.39933 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7419e962-87ef-306d-a038-ac96c9ae77c8 | -7.95098 | -44.11934 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b783b593-84fa-367e-b570-581cf7e3d2a4 | -8.11748 | -45.54508 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c832c8df-f6ee-3a52-a3c8-71354c857444 | -7.47277 | -41.52203 | 2025-10-17 03:28:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| be7dfd92-feb5-3584-aa47-045a5e41b16b | -6.31712 | -40.94247 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README23.md)
