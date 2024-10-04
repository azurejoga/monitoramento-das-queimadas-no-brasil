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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce94972c-c6ee-3696-bd6c-a8fdd7ebcbd8 | -9.92104 | -44.0751 | 2024-10-04 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7a2558a-02b7-35fd-8b57-b9dc8c7cca4f | -9.47439 | -44.05551 | 2024-10-04 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2c2726b-58d1-3094-8d44-cbe6634ae8e3 | -2.13218 | -50.99402 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b208729-544d-309c-aea2-bab758c0a85a | -3.54779 | -50.85815 | 2024-10-04 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17ffb4f5-b26f-333a-b0aa-f4fde7eb9bb5 | -3.37333 | -51.21152 | 2024-10-04 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cbc8defb-9879-3406-b290-a4fb2aceeabe | -3.37273 | -51.21219 | 2024-10-04 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4de0e8e9-3621-3e49-8f5a-b9280541e0a4 | -3.37262 | -51.21563 | 2024-10-04 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fad5d76c-1de5-35b6-9a46-8f2ec793f7d9 | -3.37204 | -51.21632 | 2024-10-04 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8a4546f-af54-3c3b-b8d2-dc6a60a7b45b | -3.36684 | -51.21467 | 2024-10-04 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6bd4028e-9a73-38b7-9b08-f2d83b5ea530 | -3.36626 | -51.21535 | 2024-10-04 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d9544d22-8670-3c86-a748-5b07449f31ea | -3.29883 | -50.76212 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68b6ada2-f789-3016-8933-35224843ba15 | -3.29386 | -50.7573 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d675e9cd-8df2-33ce-b726-160f4e093f43 | -3.29322 | -50.76114 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb737b41-6685-31ff-9568-812c8d193ddd | -3.25135 | -50.94113 | 2024-10-04 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3573e0e6-ea5c-3123-a1ba-76d9e5065c48 | -3.22414 | -50.79305 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c67f9d0-cfb9-3a47-bf70-f651b6ac183b | -3.22349 | -50.79684 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb8c5266-7657-3758-be35-7039a441f213 | -3.15833 | -50.89018 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6466aaa6-0ad9-37dd-9523-34641eed4e2c | -3.15767 | -50.89413 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0211c2db-c73d-39d7-b6c0-3f397e6e9865 | -3.15265 | -50.88926 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4058eefb-acf0-347b-9a01-9cad6a1008ba | -2.90379 | -50.7444 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a08f8d6-a373-3397-887b-0e163a84d44a | -2.90121 | -50.74076 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f399df59-3c02-30dc-8c07-e4f58ba13387 | -2.90058 | -50.74459 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9f843fa2-db94-34d2-879c-8a6fac777510 | -2.89996 | -50.71306 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0bc011ca-31b5-34dc-9f3e-5a6058a4bd1c | -2.89933 | -50.71688 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 77bb03f9-01a6-346a-9972-eca4538bc363 | -2.8987 | -50.7207 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d3457479-6c52-3eaa-95e5-501d4e985de0 | -2.89814 | -50.74352 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54561c2c-821e-38b9-aa0c-9b6fe612aaad | -2.89774 | -50.71205 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 850f9d56-d462-344f-8771-39fe75f3d761 | -2.89748 | -50.74736 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c42e423-4c5d-319f-ba7b-d766cd80c040 | -2.89709 | -50.71587 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5db31d30-4076-34d6-9f15-56f6e2dec136 | -2.89643 | -50.7197 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8263c8d5-75e8-3d5a-a627-07f6d99caee2 | -2.89577 | -50.72352 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c11f244b-ffb9-3472-87f0-ba7f26cba51b | -2.89432 | -50.71212 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b76e78c5-f35c-3f01-a4a1-5bf349e6a47a | -2.89369 | -50.71597 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c4cf1755-d985-3660-adef-1f846acdbf77 | -2.88931 | -50.70737 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d36715eb-f8ea-3c7a-b123-b5ff417ad3b6 | -2.88868 | -50.71119 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45f47f59-2252-33ec-a141-71ffb2b8f089 | -2.88367 | -50.70647 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e65c1f99-50eb-3dc5-8579-2b252e86b16d | -2.88304 | -50.71027 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59ca793a-b572-35b5-8f27-a17e538ffce1 | -2.88241 | -50.71409 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2f46031-b58b-3edd-9322-2f98387feae5 | -2.86484 | -50.71521 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 242c8118-bc9d-3f9a-ad8b-c01c16e46762 | -2.86292 | -50.72673 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb164fe0-a48b-3952-a621-853bcaa1c961 | -2.85919 | -50.7143 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca703742-fc6f-3691-b6d8-0166592badf6 | -4.09443 | -51.11541 | 2024-10-04 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 636d12c6-b845-3211-9fa9-3d2c9c99e72d | -4.09379 | -51.11914 | 2024-10-04 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5d60d0f-a550-32c5-91ce-a076d8fdcef5 | -4.04541 | -51.09481 | 2024-10-04 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 989c0b1b-8eda-3f9b-87c1-e8f583df854f | -3.80925 | -51.18059 | 2024-10-04 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ed264990-6415-3a57-a461-b80a3d971554 | -3.80773 | -51.18097 | 2024-10-04 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 13aa8eab-bc29-3680-900c-bc25b4ffefcc | -3.79791 | -51.66523 | 2024-10-04 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 248e0d39-3efe-3aa1-8be4-1e4f6c146e27 | -9.03039 | -52.11052 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 581cf61c-8606-3f70-8b05-3143dfbd062d | -13.47974 | -43.77792 | 2024-10-04 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 29b6fae3-a210-34bd-9dc7-5b484b2a0daa | -13.47699 | -43.77383 | 2024-10-04 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e92bc07-74da-3895-8d11-5629f92ec23b | -13.47642 | -43.77737 | 2024-10-04 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 025450ff-886b-3402-8ada-acf008d4b0e8 | -13.43481 | -44.77381 | 2024-10-04 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 605866a8-ff96-347b-a526-d688f5a6b014 | -13.3857 | -44.29943 | 2024-10-04 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e1758b3-8494-3580-9f32-78e842119826 | -13.02363 | -43.7564 | 2024-10-04 04:10:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7592a90e-b810-3799-a4fd-049cb867e4e0 | -13.02089 | -43.75229 | 2024-10-04 04:10:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a1456fb-f102-3b15-81da-5e8e25dd8b86 | -13.01209 | -44.75682 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4834cba-de67-3f7a-94bf-7e1b3a81c9c6 | -12.73367 | -43.48294 | 2024-10-04 04:10:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfc21f35-e15f-37fa-9df2-e18a4dc6e05c | -12.73036 | -43.4824 | 2024-10-04 04:10:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37077f20-d855-3aa3-9962-176e115212cf | -12.43898 | -44.46263 | 2024-10-04 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cc79f6a-926b-3ca3-83ce-a3d73c3c4b01 | -12.36756 | -44.61436 | 2024-10-04 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7aac37fb-2e6c-3566-bcff-c7280538cff6 | -12.36417 | -44.6138 | 2024-10-04 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d7d1339d-fd66-3ef7-a1f1-1b0f9ad9d5ef | -12.35809 | -44.65104 | 2024-10-04 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8c1d034-55e8-3270-9e85-e21bc9da6c3e | -12.35617 | -44.30241 | 2024-10-04 04:10:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 034824cc-3ab6-3c15-b02f-7caf3bc90cb4 | -12.35557 | -44.30606 | 2024-10-04 04:10:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f7fe687-2c17-308d-8457-3aa81d191b6e | -14.90999 | -45.12638 | 2024-10-04 04:10:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1020a293-6852-366f-83f5-c9fa21cd001c | -14.90938 | -45.13012 | 2024-10-04 04:10:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87284644-b20a-3854-b42b-a552c34c2504 | -14.90661 | -45.1258 | 2024-10-04 04:10:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c73fc387-3e7c-3d65-bd35-aa0d37b1a63a | -14.906 | -45.12953 | 2024-10-04 04:10:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 321b7a7f-e5fd-36cc-bbf0-77c8207b844b | -14.77333 | -44.35137 | 2024-10-04 04:10:00 | NOAA-21 | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 289be7c3-02b2-3383-8710-d749de6ea5a0 | -14.58026 | -44.86836 | 2024-10-04 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6c48895-4e72-3226-9899-16e3d3b201b0 | -14.50831 | -45.22002 | 2024-10-04 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dc51da6-38f5-3ad0-8861-e19d5471423c | -14.31547 | -44.6986 | 2024-10-04 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f40935bc-2f0f-31f8-8e51-25e2b1fdae01 | -14.31488 | -44.70227 | 2024-10-04 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01488132-d74f-38c2-8064-45f0c23e3f7b | -14.18792 | -44.24529 | 2024-10-04 04:10:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 854f6852-6ad5-3756-8a61-74ebb454faef | -14.18734 | -44.24888 | 2024-10-04 04:10:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdf0033f-03e9-3f1d-a67f-b85c923d4316 | -14.16938 | -44.65158 | 2024-10-04 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ef714e1-7cee-3022-8e71-81f0b24219fb | -14.16603 | -44.651 | 2024-10-04 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 62261f08-9166-3034-9d79-37b1b0eff4cf | -14.16327 | -44.64677 | 2024-10-04 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e05871f1-86a6-39db-abfa-419e5034c341 | -14.16267 | -44.65042 | 2024-10-04 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7d9ca9c3-d86b-3fa4-b8e2-d5044fad66d2 | -14.13533 | -43.70103 | 2024-10-04 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f37bd32d-39ec-3796-9c47-a6c0475bd039 | -14.13477 | -43.70458 | 2024-10-04 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b36322b1-4731-3388-b164-98f5fe796791 | -14.10829 | -44.5476 | 2024-10-04 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10357024-dbd1-3e17-9f00-b647bd23b5a4 | -14.04589 | -45.05726 | 2024-10-04 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e57ae14-0ef8-3c48-aadb-dad510d41798 | -14.01165 | -45.07452 | 2024-10-04 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd484507-f275-3cf1-bb60-09f761dddc07 | -13.99454 | -44.02839 | 2024-10-04 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 84b7a94b-6cac-3566-b907-ad4c6551f928 | -13.99397 | -44.03196 | 2024-10-04 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d3da59e4-2c6b-3aab-b295-dc304871d672 | -13.9934 | -44.03553 | 2024-10-04 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8dc686d6-3f6a-372b-8d08-2161771a054a | -13.99122 | -44.02784 | 2024-10-04 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6b157050-7247-308f-99cc-671d1a49e025 | -13.99065 | -44.03141 | 2024-10-04 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cf386aa5-6201-3ac2-a9ce-5b14f2665076 | -13.89259 | -44.27993 | 2024-10-04 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55c46b8b-c17f-3c8a-883b-b14adf83af90 | -15.51697 | -44.32214 | 2024-10-04 04:10:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0d33d42d-cb96-39c3-b98f-c9e2892f8201 | -16.15487 | -44.22785 | 2024-10-04 04:10:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f82a3daf-f9a5-306e-9638-e0959b5a90f8 | -16.0999 | -44.29581 | 2024-10-04 04:10:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a283b83-01f8-3fae-b1a4-37fbdd68c5b2 | -16.09831 | -44.28449 | 2024-10-04 04:10:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee81e5db-3815-3cc2-93a4-c700c3d97d30 | -15.8605 | -45.27081 | 2024-10-04 04:10:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ee52478-9fea-3210-9cb3-7dfe47eaf690 | -15.64594 | -45.16519 | 2024-10-04 04:10:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89397c8f-c008-314b-a6e3-a196cc9d29db | -15.23817 | -45.14069 | 2024-10-04 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bcf3e39-5f4d-3bc3-908d-2971d39e4cce | -17.41917 | -44.94241 | 2024-10-04 04:10:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 771e478b-7027-3bff-b53a-3c5460106e3b | -17.41585 | -44.94183 | 2024-10-04 04:10:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d550c962-dacf-3e98-9daa-c5f0f42a60ff | -17.41252 | -44.94125 | 2024-10-04 04:10:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README69.md)
