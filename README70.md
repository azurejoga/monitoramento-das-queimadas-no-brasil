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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7a5905f-0ab7-3145-b49c-ec7a24dd8aa5 | -4.5199 | -50.42331 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68ed8349-66c8-3717-a58a-c8b9607df059 | -4.51626 | -50.42275 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6db6cbf6-d26d-36fb-b4b2-c675412ef985 | -4.46928 | -50.36082 | 2024-10-12 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 228c59ae-db25-355d-b79f-92dade2c5eea | -6.13556 | -51.13823 | 2024-10-12 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e05ecd15-4b55-3a06-bf1f-6219ca8969f7 | -6.13498 | -51.14213 | 2024-10-12 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbdc1f63-f47b-3792-95de-ddca36dba2b8 | -5.78765 | -49.82237 | 2024-10-12 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 665ec1fe-d875-3db5-a623-f14e26ed5656 | -5.78642 | -49.82392 | 2024-10-12 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0557078-d2d9-349e-b674-059eb5dbe4a6 | -5.63625 | -50.3415 | 2024-10-12 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d98f276d-4184-3ea9-8b5e-6ebdd1b5bad7 | -5.38671 | -50.53394 | 2024-10-12 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 533a7318-0fc6-3bb5-b82c-0eb5da2a6857 | -5.28276 | -50.9887 | 2024-10-12 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ad3b0d6-b6de-3bf4-ba10-2b09fb0c1bd3 | -5.28217 | -50.98715 | 2024-10-12 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5aed7431-e5f5-3865-944a-a5e31b86b550 | -5.26859 | -50.72127 | 2024-10-12 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 563ea4cf-3ba0-32fc-ace0-db1ba3412f5a | -5.20561 | -50.1659 | 2024-10-12 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa3d194e-62dd-3b5d-9d3c-ef9f64f99c6d | -5.20189 | -50.16535 | 2024-10-12 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b854137a-6383-3dd7-8695-3b1750b25e7d | -5.15875 | -49.90656 | 2024-10-12 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7220fa1-02b6-3caf-9af6-31a173518b98 | -5.02056 | -50.87618 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06b931fc-0ae1-3ba3-ab01-c3ea20ddb3f7 | -5.01699 | -50.87561 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbc0ff1c-9f2b-389d-b7c7-e257819d7181 | -7.91829 | -50.86846 | 2024-10-12 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f2e47d0-2d4c-391e-b2c1-f97c89ae011a | -6.83586 | -50.13918 | 2024-10-12 04:57:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 168f43de-5192-3ac4-9607-15aa5cf179da | -3.4617 | -51.55238 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5941d043-c854-3962-b74a-5d2688bd40cb | -2.13041 | -51.2416 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dd76f28-1bff-3d41-822a-126a69098006 | -2.03266 | -51.14727 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f41c130e-a8ee-384a-91a1-89a97c37a741 | -1.25513 | -51.6034 | 2024-10-12 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0abb54dc-8175-3be3-9164-2ed9275945b4 | -3.56214 | -51.51463 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7266a3ef-83e2-3516-a817-1f2aa426efe2 | -3.55651 | -51.48325 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70d33681-d8f3-3534-ace8-9bad6ef37426 | -3.53404 | -51.24039 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f240f85b-99ae-3be1-838d-9bfdbce66f49 | -3.52027 | -51.16777 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f962034b-995c-3689-ad94-1b01ef48dc90 | -3.51821 | -51.16771 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bcca463-5d96-31c8-9540-1c5a023fc443 | -3.51664 | -51.33095 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ddbbec4b-4f0e-3016-9516-83c0e1db518a | -3.48975 | -51.19074 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ec572f1-fac9-368e-b46d-c21f5d3aab02 | -3.48677 | -51.57146 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08e8af87-1ecd-3b2e-b8e9-5e8419a708fa | -3.4862 | -51.57516 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a38c385-75c9-3777-b5cd-cadeaf317d94 | -3.46512 | -51.55292 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5aaeab75-2774-3454-bdb6-142b73707aa4 | -3.46455 | -51.55663 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d1fb6336-8b09-3ae4-b460-159054b5460a | -3.46113 | -51.5561 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 239272bd-8c92-3017-9dc5-f6c8ee993245 | -2.90052 | -51.75589 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4651c345-7351-38f7-86fb-56874779cad2 | -2.89997 | -51.75949 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e577901c-4995-33ba-84d9-906ff9ee96fc | -2.89758 | -51.68495 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad752acd-f675-3cfb-83b9-70e4fc3595fd | -2.89419 | -51.68443 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab93256f-a211-3be3-9c43-8500a9c539d9 | -2.88208 | -51.66444 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23c0aa0d-5dd1-3d83-b993-15508e138044 | -2.88094 | -51.67174 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6d00677-1e8b-38f1-87f2-80b5b7c4f149 | -2.88037 | -51.67537 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d2d9f22-80f6-3a5e-8179-3d73fba7c8fa | -2.87492 | -51.89944 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f97c312f-7d62-3ede-82b6-88cc275c1f6d | -2.87248 | -51.65925 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 536571ad-3144-3496-9253-f648a11c4193 | -2.87191 | -51.66289 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 50d716bf-f9f6-36b0-9169-c199c5e64fc8 | -2.87134 | -51.66653 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 96396663-9475-365c-9b4c-33218fa575a5 | -2.86852 | -51.66237 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 38b844ff-83e1-3ae1-929f-93fbb518dc6d | -2.86795 | -51.666 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2a598562-3254-3aa1-aa73-6c98b7cea7a5 | -2.86456 | -51.66548 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bf254f84-3d6a-3efb-ba6e-262ea11d1a28 | -2.86399 | -51.66911 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f4d3c0dd-515f-3379-b9b5-9531147a7880 | -2.81737 | -51.9898 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48417269-12c1-30bb-b893-53a06242aa62 | -2.80858 | -51.60071 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a693acc-4dd2-38ea-9fe7-f5bea25642c0 | -2.74147 | -51.6461 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2eba4f7-26d7-3b13-bae9-4d578188cbc0 | -3.49601 | -50.80157 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e142d40-debf-3707-ac79-ecf18fec6478 | -3.03517 | -50.56894 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c340798f-728c-320f-badb-a9d748378cb6 | -3.03225 | -50.56433 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 88acb487-7aff-3bd9-a5e2-8f12454456e2 | -3.03162 | -50.56839 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 64f82601-6847-3eca-b41b-cb23ff57ef9c | -3.0287 | -50.56377 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 49c04912-7ae3-308b-b50b-5a281023d4a3 | -3.02807 | -50.56785 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ffea7db4-1625-3dec-8b2c-e302c4c8ef86 | -2.64684 | -51.71002 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6705ae2f-c4a9-37a2-b968-dd231b5b1234 | -2.64403 | -51.70588 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f09d7784-ecca-33d7-83de-8117730f4a35 | -2.64346 | -51.7095 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bbc116c-5f0a-35f3-ad37-eebc90f2dd4e | -2.64065 | -51.70536 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16a4ebcb-3a78-3139-95eb-055e6a944d09 | -2.64007 | -51.75334 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 982e9fda-be93-3066-84d2-625d144d664b | -2.63669 | -51.75282 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e150359-a091-3f3c-a0a8-18a3ff63e8dd | -2.60254 | -51.94927 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3a90eb2-b230-3728-bc90-e8264ae49691 | -2.58627 | -51.92127 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4ae80ba-4e42-3781-b1bb-bb71308c4e53 | -2.58572 | -51.92483 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05335b6a-0bc0-3ccd-bcd0-95fc7d77b38e | -2.58291 | -51.92075 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35448dbc-3241-3f38-8f71-4a19486bb60b | -2.58236 | -51.92431 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 987675f1-72ff-38ac-ab80-f199e117e992 | -2.52368 | -51.84594 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 779b98ae-d73b-3375-93da-f32d29fc0bb9 | -2.38873 | -51.79187 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 793e4d07-14ce-39eb-81cb-9b9b87f2d8e9 | -2.37802 | -50.93238 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1979978f-7a24-3240-81a2-af5f1d8eb6a0 | -2.32544 | -50.63598 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fd769b7-9a11-39d4-b2e8-9b59b76f2f25 | -2.27114 | -50.65599 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87b1df04-f470-336e-b89c-1e25758dda9c | -3.4096 | -51.5709 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04d13882-3981-3df0-a4d5-cbffbec4645e | -3.38746 | -51.34967 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51de5da6-8b05-3bfa-9280-a499668e3956 | -3.34335 | -51.88627 | 2024-10-12 04:57:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 053bf64a-8c4c-34e5-ada3-88422cb24242 | -3.33886 | -50.80798 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 165b03e4-65e7-3171-9487-65eedc789d73 | -3.33825 | -50.81192 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bffa07eb-7eab-30fc-8462-c94ec5d378d6 | -3.33595 | -50.8035 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22348eae-5bfe-3942-862c-1ad4831d3a91 | -3.33534 | -50.80745 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 702725df-2e78-318b-9e0c-d57ef9aa52a9 | -3.30204 | -51.11277 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b18dfcef-2a5e-38e7-98db-625a0c6dafea | -3.28831 | -50.94859 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c621cb92-02ca-37eb-8735-0397ceae0ff3 | -3.28482 | -50.94806 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 634d4946-14ba-3f71-8256-fe0da0f72f68 | -3.28422 | -50.95194 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c26087c5-74e5-35b8-b451-a6ff2d0097aa | -3.28132 | -50.94751 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e42be76-d662-3e5b-8094-352a0b521836 | -3.28072 | -50.9514 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2147d8a6-1a41-31e0-84b9-e90dd914a83e | -3.27961 | -50.79486 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c156a57-9375-31af-8cc0-300ff17b3c2f | -3.27911 | -50.77456 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb05e628-6e50-317f-ab85-a360b7c9cbc0 | -3.27782 | -50.94698 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c663615a-fdc6-3cfb-bbd8-a2fc3751b7d7 | -3.27558 | -50.77403 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d1e1447-3372-3f77-89f1-c5cfa5cce24a | -3.27205 | -50.77351 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b264855-922b-3f6d-956b-34668a2f8252 | -3.27145 | -50.77746 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 713f8530-aeda-39eb-96da-4c2fa6c95f21 | -3.23794 | -50.84936 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 349bd326-f0fc-36f3-afbb-c50b93353f37 | -3.23733 | -50.85327 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e18750ca-b4d2-35fe-8305-fcfa9f630f8e | -3.23443 | -50.84883 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06cb95b0-6820-310a-88d0-3b87e2fca122 | -3.23382 | -50.85274 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d91d58ca-bbb3-378e-b57c-4ca8404e05ff | -3.23092 | -50.84831 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fc84ab5-f6b6-373d-9661-7ca9ebf7b4ef | -3.23031 | -50.8522 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README71.md)
