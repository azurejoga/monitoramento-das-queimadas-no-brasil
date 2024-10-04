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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fd2591a-b21f-3144-84ee-2e368a4b0a19 | -2.89212 | -50.71696 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f4215b05-2640-3334-91ea-86115c8aee7c | -2.88983 | -50.7086 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b65fc913-07be-3a23-8b65-6306bc77c228 | -2.88922 | -50.71252 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 04a45d38-5d81-35f0-b907-3dc499fbb119 | -2.88861 | -50.71643 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab34872e-8b09-3bc1-a893-76bd9a22edae | -2.88631 | -50.70806 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5ce3c396-8e2d-3476-9b4f-5bdb0a97e98a | -2.8857 | -50.71198 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 944258a8-99c7-30af-9c63-db25961e45c9 | -2.8828 | -50.70752 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78314a30-5db8-3108-aa27-d74a6fb0179c | -2.88219 | -50.71144 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2224458-3128-3645-aaec-6a2c8264fd7a | -2.88217 | -51.67738 | 2024-10-04 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eaded116-39de-3209-8160-a32fe8797ce6 | -2.87878 | -51.67686 | 2024-10-04 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86b463df-b8a6-3f0d-9b20-99837e38b2dd | -2.87867 | -50.71091 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b2586d7-1ee1-31a3-9a74-b553e38bc532 | -2.8634 | -50.71659 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8807f5d7-294a-3226-bdce-55a29d41be12 | -2.8628 | -50.72051 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2647d25f-789b-33a8-9639-09118ef479e6 | -2.86219 | -50.72442 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ebfb444-e3d4-3e11-be02-252b25c0c7a0 | -2.86049 | -50.71213 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aaf3d0e4-5e5d-3eb9-a649-63c8a2632c14 | -2.85989 | -50.71605 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a002534-8a87-369e-a6ed-a8ab5b7c13ab | -2.85928 | -50.71997 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d78a599d-5245-365e-9b77-d2b20df0dc7d | -2.85637 | -50.71551 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f70ca53c-c5ad-33a0-81a4-aa3c48317776 | -2.85165 | -50.7228 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b72f890c-9d10-3f00-9a80-4c4fc1252a65 | -2.84814 | -50.72227 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6feb0f81-e88b-3d15-b635-0a15db316e3d | -3.89622 | -52.1959 | 2024-10-04 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd62b266-30d2-388f-8408-34acf55fda4c | -3.83109 | -52.18235 | 2024-10-04 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c5d0454-cd57-3042-8e9a-f9c895741f27 | -3.83054 | -52.18592 | 2024-10-04 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f99eb569-287d-347d-8374-7989b5823ee0 | -3.82773 | -52.18182 | 2024-10-04 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96cb6d9f-dd03-30bb-a975-a94d9b7eac0c | -3.82717 | -52.18539 | 2024-10-04 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcba0b41-0de3-37a6-88ca-461886247f4c | -3.78817 | -52.25957 | 2024-10-04 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d5e64ed-a8ed-3976-aeed-93aac986858b | -3.78762 | -52.26313 | 2024-10-04 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 324a2f72-aa81-3252-bfc2-562e25ab6b1b | -3.75859 | -52.25847 | 2024-10-04 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2156b790-362d-3187-a52c-6d33b3f172d4 | -3.75076 | -52.24268 | 2024-10-04 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d14818b6-5eea-3685-b0bf-75f38c38ce9c | -4.09672 | -51.11909 | 2024-10-04 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dd05728-9e69-37e2-b58f-2d07b8bd7879 | -4.09383 | -51.11462 | 2024-10-04 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f684aeb3-1573-326f-bf6a-b7ea4ebcec70 | -4.09323 | -51.11853 | 2024-10-04 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9bb870a-08ee-3dba-b6f2-5af4b59ea1bc | -4.04606 | -51.09242 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3397f2bc-4e70-35bf-875a-23df7283552a | -4.04546 | -51.09627 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5e984c9f-afb9-334c-9ab1-e7c7d7932935 | -4.04256 | -51.09189 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a2490f26-1a9c-3143-8c39-5105b19a755f | -3.96159 | -51.38482 | 2024-10-04 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da805156-b5fa-381a-87b6-01e5b430402e | -3.89952 | -51.26686 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d57b337-27e9-3f12-8325-25fe1f9a6dc3 | -3.87684 | -51.8201 | 2024-10-04 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e9d0515-00da-3c28-8489-fda51b470c4e | -3.85943 | -51.06448 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3daed1d-1c58-3c92-a130-fc1b816bdf48 | -3.85885 | -51.06829 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| feabaad7-5939-3343-a59f-ceecad3aa847 | -3.81163 | -51.18016 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ce0bfe1-9d74-3ef6-a233-40483269a647 | -3.81104 | -51.18396 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eec59ebb-6ec4-36ca-92db-e09308d1068e | -3.80816 | -51.17961 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c09e1c4-c4a8-3052-b3f8-49a13060a685 | -3.80757 | -51.18338 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8e54dd4e-c728-3698-9c76-b1a19a8aae1d | -3.73376 | -51.36248 | 2024-10-04 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0638cdea-ccb4-30d8-bcef-23fcaa56bd2e | -3.70906 | -51.1409 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81e3ae68-21b8-39b9-975f-0620e3d1ccda | -3.67057 | -51.38758 | 2024-10-04 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6879a51b-e198-318c-80b7-981098fcd758 | -6.50819 | -52.56348 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4389f6b-c1c2-3186-a8bf-28e60253c19e | -6.66835 | -51.58998 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40c9a1d5-dcfb-398e-96e9-9ed7cb9637eb | -9.36992 | -52.51195 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef429ede-9740-34b4-9a24-42c6ea49b861 | -9.36644 | -52.51146 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afbad226-cde6-3631-9438-eae77f6a5d58 | -9.36239 | -52.5148 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abca63ad-d378-38d8-af64-a87776394205 | -9.34736 | -52.52044 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f6afe3e-f616-3113-a9a4-3206d39a6885 | -9.34388 | -52.52 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cf84768-9fa8-3717-a769-483816bbe3dc | -9.07355 | -53.26425 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 374df932-a12e-3dd6-92f8-bacace65ed1d | -9.073 | -53.26786 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32a977a3-4efd-30af-a063-18f3fd03c38d | -9.07183 | -53.25284 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25afff25-aa0a-3023-a12b-5cafb52f82f3 | -9.07128 | -53.25647 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fb36d87-10d3-3ec6-af61-15e9d655c61b | -9.07073 | -53.2601 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b0d27a0-66f1-3ea7-8a52-63424f09a34f | -9.07018 | -53.26373 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7172b60d-68e9-3a83-83b9-7ba9054c8770 | -9.06901 | -53.24868 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4917db5a-9b67-3aca-adb4-543beec83285 | -9.06846 | -53.25232 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0eb4b605-7ca3-36e0-a17f-77ca0f50902e | -9.06564 | -53.24816 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25657713-b110-3aec-b75e-3884c77b3196 | -9.06509 | -53.2518 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddcee2f0-e2ec-34eb-bda5-19f03dddaf16 | -9.06171 | -53.25128 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbda0c1e-65c9-3b5b-9b2b-69efe93ed7ed | -9.06116 | -53.25492 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef2fac33-2cfb-3ca7-a174-767ed027cdf5 | -9.06006 | -53.26218 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57757c81-b201-3b21-a443-464a14ac61a5 | -9.06004 | -52.95888 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa54b5ee-c562-3074-a55d-3f85ec6aff50 | -9.05947 | -52.96259 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fd5f1ed-366e-36d5-a8b4-01535a48b15f | -9.0589 | -52.9663 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7040c347-4e2e-3bda-ae99-5724201d29a2 | -9.05834 | -52.97001 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fe363d6f-8a50-3e0b-b141-3bb865758f6c | -9.05777 | -52.97372 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c819441-a394-3b37-aa54-fc9cc2f5783f | -9.05607 | -52.96207 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dffa5690-13f8-3259-81b0-74efa1fe00ef | -9.0555 | -52.96577 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65c5777a-5935-31a4-ab9d-401d3c203df5 | -9.05494 | -52.96946 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bba96ba-b037-3b46-9b8c-bdb4d637fc4a | -9.05437 | -52.97318 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e17cdc11-9ee7-3d6e-92a6-1b53a482a143 | -9.0538 | -52.97691 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a050bbed-f40e-3035-8462-7bc0c14c1cc2 | -9.05323 | -52.98062 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49d31c49-b475-31ab-9aa7-984b8e7e1039 | -9.05041 | -52.97633 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dbf292b3-7efe-329f-bbf3-46c5a88e8598 | -8.96873 | -52.80104 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 77eb552a-93cd-3201-9266-cde00154f3ed | -8.9676 | -52.80849 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3db3212-43ee-391f-b57d-47b9c4dc20ed | -8.96587 | -52.79686 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b93ca8c-e796-39d5-8c30-a3433fd4e677 | -8.96531 | -52.80056 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 401f12bc-2cc0-39d4-8caa-fe9eb4d79b8d | -8.96474 | -52.80427 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9db793f-f224-3c61-8f0f-92a9674fae71 | -8.95561 | -52.79532 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68e2216f-14de-3b2a-9ae1-d5c78776ff3f | -8.94022 | -52.78151 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ade0b34-f0dd-3726-8f86-95dfc6c5ae8d | -8.93679 | -52.78105 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4bbb41d6-502e-3cf7-8696-cad61b334ccd | -8.89851 | -52.75597 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3e29236-c3ea-3ac7-ae7f-edc1821a75ad | -8.64248 | -53.17612 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c38e2862-b14b-35a3-bdfc-ef93867aa5d9 | -8.37838 | -52.37907 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 244f66ee-8a91-310a-9cfe-4043435a0403 | -9.03052 | -52.10854 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4ad9ae72-b7e8-30c3-9214-7106bcdf4eaf | -9.02994 | -52.11239 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f38678a-63df-3161-a9cc-51901deadae8 | -9.02936 | -52.11629 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| edbd48e7-94ea-3b22-a6d0-2af2f88fcbcc | -9.02879 | -52.12017 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2840f8e5-00fb-3675-a4b4-49dd2eae66cb | -9.027 | -52.10806 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aca4eaf3-0278-3e04-ad42-05acc7fd473c | -9.02641 | -52.11197 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf5104c1-1c62-3735-81fc-e485b285e48c | -9.02527 | -52.11968 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d20843e-a161-36ed-a0ec-ce59c82d8cf8 | -9.02348 | -52.10757 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dead2da9-e12c-3eed-97c1-745d1df41b22 | -9.02001 | -52.13091 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62241596-1075-36de-a0d1-c55abc0e57c5 | -9.01996 | -52.10704 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README148.md)
