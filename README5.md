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
| f7503fcd-6e04-3c0b-abd6-ddb8b27a46bd | 1.51632 | -59.93821 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2bd8a81-0abe-3e8f-bce7-d544a56796c4 | 1.51225 | -59.93891 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23b32d23-b24f-32ac-a036-e6b849968d4b | 1.46895 | -59.92738 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 563c86c2-d94e-3974-ad18-9b3a705b32f3 | 1.48023 | -59.94793 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af97d107-7bda-3cec-b01f-11b55705f9f5 | 1.47009 | -59.93476 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 51750899-1393-3393-a7f9-4e2e35c2172a | 1.49188 | -59.94233 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ad27d5a-9127-37e6-8421-558ddc5614cd | 1.48314 | -59.94004 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c39df91f-49d4-3f7b-b7e4-51b51edd50e1 | 1.13065 | -60.52254 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a216a092-3222-3a59-93fd-d06c57df71e8 | 1.49479 | -59.93447 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7552a693-0bc6-32e3-b08d-7b0a6b23a1de | 1.50703 | -59.93248 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9a9d1c0a-2f52-3b0e-ae6e-16db165fc1cf | 1.50353 | -59.93673 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 986eef2b-d0a9-3058-8691-8857d1873e08 | 1.50646 | -59.92892 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d0be4844-862a-3076-b88f-25469fe7e395 | 1.51167 | -59.93531 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f7630586-0d30-397c-ac95-f305edbc35a8 | 1.48197 | -59.93283 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 84c293ed-541b-33e2-bc8c-5840260bed2b | 1.87857 | -60.91641 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cfd4572c-9386-3653-912d-69ea9ea2bbff | 1.47135 | -59.91589 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 172ce136-1d48-3e73-9836-3947199858ef | 1.48497 | -60.90495 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72051b3d-9d93-3889-b30a-15faa43448ac | 0.23276 | -60.51012 | 2026-02-28 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e44fc0e8-bdea-3e7f-afc8-58400cc9a2b5 | 1.49887 | -59.93381 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e9bb0e9-324b-3a20-a3f7-03b7989e0321 | 1.49072 | -59.93516 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3368eea5-f785-3f2e-bd00-214468002728 | 1.49769 | -59.9265 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b1d0fe9-a159-36cf-b405-e7b9cc932c4d | 1.49241 | -59.91975 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 51414886-3abd-35dd-81a3-866088f1a2d9 | 1.48366 | -59.91745 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24cf02c4-30cb-34fa-937e-48965ff62987 | 1.7516 | -61.16826 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 956ad0e4-60e8-3db9-8e47-c479269a818a | 1.43099 | -59.95232 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e44416a9-3ff0-3c3c-bd0e-d8ad1b3d7872 | 1.50468 | -59.94388 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff1acd28-7349-342e-86ff-22b64c440d17 | 1.50118 | -59.92216 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ba6bd347-6e85-33e2-9289-be8aa23ea3b3 | 1.47884 | -59.9372 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e7aefa5-0128-3338-b940-07e4d5621c1b | 1.50296 | -59.93319 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ff55c6e8-c6f7-3dd3-8898-e292324ae139 | 0.64658 | -60.6647 | 2026-02-28 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c069be0e-9b07-3dd4-a30b-2f2cd52c72b5 | 1.48426 | -59.92114 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 9c154874-6854-3a70-ba7c-33bba9dc54ec | 1.48372 | -59.94363 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c3c94f2-730c-38bc-807e-8c70c1a42812 | 1.48138 | -59.92922 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 4ecf944e-b906-33d7-9fbe-cb3a432289c0 | 1.48124 | -59.92566 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.1 |
| eb1ed1f1-237b-3382-a402-060c97c67348 | 1.49592 | -59.9155 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42d0e5fe-f7bd-33ed-acbd-125ba52637e1 | 1.49945 | -59.9374 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1846b40b-2193-32a2-b684-951acca01bab | 1.48078 | -59.92554 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 27.9 |
| a4a1ebd5-cb8a-3efb-ae15-a94c6cfab925 | 1.47067 | -59.93845 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e76bee7e-c62d-3599-a0e7-4c1114cc207b | 1.48722 | -59.93944 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fa6368b-04e6-3cc8-9312-7c73c3a3377d | 1.48833 | -59.92043 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.5 |
| de95839f-94e9-37dd-b705-4665963be632 | 1.46485 | -59.92798 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9898ff9-e6f8-39c9-9ad0-7287bde9fbb3 | 1.47846 | -59.93703 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8481bb4-5b2e-3c65-916c-7961e952d5b8 | 0.2333 | -60.51358 | 2026-02-28 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92efb4b1-14f1-3339-a7e7-2d4474b2f8e5 | 1.48053 | -59.94811 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55fcb8bb-bb23-3b92-99ae-c6d5120e6fa2 | 1.50587 | -59.92524 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 502d8b28-2cce-3836-9dbf-7f48735c5aec | 1.47247 | -59.92315 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6120ad8e-81ec-3dca-9bb3-566bcf6fba7d | 1.46543 | -59.93168 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 120714b1-7366-3fcb-8596-73aabb1cbb66 | 1.874 | -60.91236 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c2e6b852-5962-32fd-b23a-285a872b6818 | 1.49013 | -59.93151 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 571604d5-5988-3c47-9cb0-99294218c958 | 1.48546 | -59.92854 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.8 |
| da79de76-1fda-393b-92ab-e0ab017f305a | 2.86828 | -60.59245 | 2026-02-28 05:48:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1be9c5a-6b39-30ce-a027-3c0443380a84 | 1.48181 | -59.92935 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.4 |
| d91601e7-f373-33fc-a3d9-95de01a56f70 | 1.47941 | -59.94085 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26c3cc58-42c7-3d9d-8a00-dd657a468bed | 1.42691 | -59.95293 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58c2071a-0bf8-3351-ada0-1ae551d1a273 | 1.46952 | -59.93106 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 38b4867a-e848-357c-8b2d-0a180753ab90 | 2.18791 | -61.91339 | 2026-02-28 05:48:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a23738a0-29c1-37a5-bb0b-317beafb3964 | 1.48405 | -59.9438 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b25e614-82ec-3b7c-aed4-3ee7e81e9867 | 1.48237 | -59.93298 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 8e0acfa0-2c5b-32b8-bfbe-7eb23d591751 | 1.47964 | -59.9443 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71416f50-f27b-3256-b6f5-e103dffe6b89 | 1.47419 | -59.93417 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 407baf20-deba-3700-b2a2-140ccccb551a | 1.4878 | -59.94298 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a8e98d9-b1a5-3cb7-8436-6c69ed70f19d | 1.49829 | -59.93019 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6bcbd4bf-4949-329f-83c3-47300e3fba78 | 1.47729 | -59.92982 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 1aae3dea-bda1-3b0b-b59d-9c4127958971 | 1.47997 | -59.94448 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9218d187-7aca-3154-8a5d-1902470d2f9d | 1.47958 | -59.91814 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd8daeb6-d0b6-37f3-9cea-342ba6d1b652 | 1.49595 | -59.94165 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 668368e5-da82-3778-bac0-1c0151e38cda | 0.22528 | -60.51484 | 2026-02-28 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a7916a9-bab4-3081-b1e1-ccf883b43c41 | 1.4637 | -59.92057 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81c60f68-f19b-37a8-b80a-f13e8b915eb1 | 1.47646 | -59.94879 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f85ae019-e631-3bcb-86c7-6dc9532e8713 | 1.49538 | -59.93809 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a27ffdb-9393-37bf-9658-20403ae884f0 | 1.87476 | -60.91702 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2a51468f-e4ef-3648-9e89-d60fe180df21 | 1.4965 | -59.91911 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f47bd9ea-6012-3742-9745-8edd0de5b7bd | 1.47362 | -59.9305 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.8 |
| a1d752da-086e-3bff-9d0f-12a8da5c4b2a | 1.46667 | -59.91276 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2b0a412-c562-333c-bed2-9ba3d767a630 | 2.87286 | -60.5966 | 2026-02-28 05:48:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26c1d6bf-338d-370c-9d72-9c571986367a | 1.47952 | -59.91452 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e823b831-f52a-34ed-9a9c-4f2c31d476a5 | 1.47191 | -59.91949 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11af93b2-22fa-3cfb-a462-a83b13d683ff | 1.47772 | -59.92997 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 39d08d68-57f9-37d7-9922-570ded8bcb9c | 1.47304 | -59.92682 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f06b8f62-b059-36bd-91ac-aaf636499633 | 1.50876 | -59.9432 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58067eae-aa1e-3787-8bdf-38a315274898 | 1.48486 | -59.92484 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 192d3a87-2f1e-34a2-8743-15117c8484e9 | 1.48293 | -59.9366 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27f97928-b24a-3db5-8836-82699149859a | 1.46837 | -59.92371 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a4839c0-6a35-35a4-a640-7f12c5d9c04b | 0.22983 | -60.51765 | 2026-02-28 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 745d31d4-57e4-372f-b71d-f019cb624ad4 | 1.46019 | -59.92493 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bd4070e-da3e-3474-ae94-e43e7d539537 | 1.87782 | -60.91172 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 27eb7768-4af5-3a13-aaa3-c6948f25790c | 1.46076 | -59.92862 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb0128c2-7c21-3408-baa7-1bf067a25cfe | 0.94128 | -60.26222 | 2026-02-28 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf3dd68f-b62c-37ec-850c-488f420fc093 | 1.47532 | -59.94147 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f0d094d-1a37-3b4c-ae46-7475e8d9b7a8 | 0.22929 | -60.51421 | 2026-02-28 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c78bc0c-69f3-31ea-9fc1-837e78bc3b15 | 1.43156 | -59.95591 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0e491031-c37d-34b2-9d04-07d7083db778 | 2.8782 | -60.60553 | 2026-02-28 05:48:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6d7ffe5-75b1-3424-8629-1605aa256c31 | 1.49361 | -59.92714 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e9210c80-efc6-319e-bcba-779e0876b063 | 1.48349 | -59.94022 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ac3d541-988d-3554-8577-5f31c7133aff | 1.47609 | -59.92246 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 095afb77-51ca-341e-bc42-3f15b3341333 | 1.48953 | -59.92784 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 7bcd4e28-c60e-3615-ac73-bd22964bbe51 | 1.47078 | -59.91226 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a9347fa-0f13-3a19-bd8e-b1dc55b61613 | 1.50818 | -59.9396 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 326486e0-dbcd-3e72-8164-789d96a72180 | 1.47658 | -59.9226 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.1 |
| c3b47e49-0218-31f6-82ae-9676b1aa81dd | 1.48605 | -59.9322 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.8 |


[Clique aqui para ver as próximas entradas](README6.md)
