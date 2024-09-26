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

## Dados Diários - Página 167

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f90c27dc-9047-329c-8eb5-83d703d5355a | -9.75985 | -68.52276 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7eb900d6-3c01-3566-852f-a40b6ad544d8 | -9.62998 | -68.61222 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d2dd6f79-6fe8-34cc-ad55-c478e2599bdc | -9.52908 | -68.43478 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 045de025-e4bf-341b-9efa-80914f23d22b | -9.5059 | -68.51492 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79070ceb-e6b7-33c0-8589-58d99fc4f05e | -9.50208 | -68.45966 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 544dc71a-86b7-3e35-beed-96843d5fc321 | -9.50152 | -68.46322 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb1ec034-a84e-3075-83da-42f879d28456 | -9.49988 | -68.452 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4538a3c-9503-3b62-81cc-8d1ff0972694 | -9.49931 | -68.45555 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a5431ca-2616-3b8b-9d80-993653e255b3 | -9.49874 | -68.45911 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 599c790d-aec4-3305-bb4c-b8e9edcb365d | -9.49818 | -68.46267 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08e0877f-b023-3505-858b-acc509a7da18 | -10.55637 | -68.02259 | 2024-09-26 05:48:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7460388b-fd3e-3edd-b0d9-c08ad69143a3 | -10.53483 | -67.79322 | 2024-09-26 05:48:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9063bc9-29ab-392e-8fdd-9d6a82022c78 | -10.53428 | -67.79671 | 2024-09-26 05:48:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 321134f5-cda7-3c70-92d8-a7f0cca81cdd | -10.52933 | -67.84969 | 2024-09-26 05:48:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7c2d771-8ed7-30b8-bc19-d51d996afe91 | -10.52602 | -67.84915 | 2024-09-26 05:48:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 624021a8-127c-3d02-a486-c5c886ed9581 | -10.52049 | -67.77657 | 2024-09-26 05:48:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39437304-1947-34f7-83c0-810bd2d2793c | -10.51994 | -67.78008 | 2024-09-26 05:48:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76ada4f5-9164-3ba2-935b-b25540be45b4 | -10.46753 | -67.76807 | 2024-09-26 05:48:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 732bac13-48dd-372d-a916-babf17e2a1a5 | -10.46367 | -67.77103 | 2024-09-26 05:48:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37b7294e-24ee-3890-9f5a-e94f0227bc3a | -10.46312 | -67.77454 | 2024-09-26 05:48:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdfdf98f-3bf2-33af-9277-3c739bc58b88 | -10.42837 | -68.05942 | 2024-09-26 05:48:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b7c585b-01b9-35e6-bf05-f85ab148e009 | -10.39639 | -67.87491 | 2024-09-26 05:48:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9226cda5-7630-319d-91fe-b5b965bcc7d4 | -10.39363 | -67.87089 | 2024-09-26 05:48:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a7ad75c-1538-37f9-9f8b-284fa64ad03d | -10.39308 | -67.87437 | 2024-09-26 05:48:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ee01285-d466-34d5-9fad-9f937b032a75 | -10.38977 | -67.87384 | 2024-09-26 05:48:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a93443cf-eb0d-34c4-b9f0-37083b59a10a | -10.36255 | -68.15308 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce27b6e8-c684-3f9a-b582-9d4b1b10853b | -10.36199 | -68.15659 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 408f5b37-600d-3a1d-9f07-265198695979 | -10.35923 | -68.15253 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95d6c2b1-3406-378e-8c1b-e30e74f09f22 | -10.35552 | -68.00455 | 2024-09-26 05:48:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0dafef1-0b71-3f9c-ac27-1c3e783665bd | -10.33799 | -68.2861 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0fddb85-cd43-3626-a206-cfa123ed1118 | -10.33743 | -68.28962 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66d2cfc7-3e8b-3637-9237-8938a54c9a1f | -10.2908 | -67.96214 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f73d2604-685a-3679-a3d7-129c6373d26e | -10.27195 | -68.08118 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ad17ecd-930c-3786-96bc-0d580b4a4885 | -10.25403 | -68.25838 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c842e4c8-3dd9-39d5-8f08-f814d4801efb | -10.25347 | -68.26189 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 622e5e45-dce7-3ba8-8fe1-2c942b2582ff | -10.14941 | -67.71712 | 2024-09-26 05:48:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9811d54f-8a29-3675-9b50-713bcffe7b7d | -10.1461 | -67.71659 | 2024-09-26 05:48:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1a87d0b-9482-3948-8368-6098aeba16c3 | -10.08878 | -67.8649 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0555765e-e1f4-34f4-a6b0-f817c63e1666 | -10.08693 | -68.51789 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc41ff1d-2db3-3de8-a542-1e19d9bdd25d | -10.08547 | -67.86436 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 638c3ab0-4743-352d-a4da-a7322f4bcf55 | -10.08359 | -68.51734 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63e922a9-95eb-328d-8e25-a0bbe038c9b8 | -10.06595 | -68.47807 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 117c56c9-6d2b-38c6-86a1-38fb8315b783 | -10.06217 | -68.58685 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1f0da8c-e31b-33df-a1d4-a10e83ed46b0 | -10.0616 | -68.59041 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30062645-5809-34ab-a334-892282465d11 | -10.06103 | -68.59397 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b16329c2-4d44-3ff1-9350-8bb96f227ae6 | -10.05941 | -68.58275 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf9dc818-fd7f-3f81-b486-f734af4a282f | -10.05883 | -68.58631 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4db6f326-d421-3848-9229-3d3c1efaa42a | -10.05826 | -68.58986 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e242731-2729-31f4-940b-76fc1b0a846b | -10.05492 | -68.58931 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14bb1cc4-18b2-3cfe-b011-7d566bdd4123 | -10.58356 | -54.24035 | 2024-09-26 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12c92e21-a186-35ca-be31-31c417695cf0 | -10.58286 | -54.2366 | 2024-09-26 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 498b33f1-843c-3eb4-8e19-a7330329b8d0 | -10.58211 | -54.24339 | 2024-09-26 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b5564332-d270-36a3-9cec-d72d4ef5df75 | -10.37092 | -53.76899 | 2024-09-26 05:48:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 122d1725-f185-3e05-950d-9724c79c5902 | -10.3701 | -53.77618 | 2024-09-26 05:48:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05955b65-cf66-3db0-9bde-819f8471dcfb | -10.3657 | -53.7813 | 2024-09-26 05:48:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 31e2da24-eef1-3769-953d-8ee430b7fe40 | -10.363 | -53.77507 | 2024-09-26 05:48:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b169a98-3a0e-34ca-8f76-8289e62fbb04 | -10.36219 | -53.78217 | 2024-09-26 05:48:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 880a59d2-c091-3cb1-b777-d3f6308f903d | -10.3586 | -53.78022 | 2024-09-26 05:48:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c690361b-8ca3-30b7-89e7-6651dec77d67 | -11.20827 | -54.77826 | 2024-09-26 05:48:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 749fa83e-ad8b-3963-9b12-35480a4787c6 | -11.20669 | -54.77775 | 2024-09-26 05:48:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 65ec1ec9-e3c7-3cec-9d13-43e7aae1a9ae | -11.20597 | -54.78379 | 2024-09-26 05:48:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ad200f4a-5607-3b0b-aea4-69f2c3de9edb | -11.20214 | -54.7715 | 2024-09-26 05:48:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4ddfe6d5-3747-3761-a37a-b956730f069a | -11.20146 | -54.77754 | 2024-09-26 05:48:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e4594886-77ac-31f2-9842-9c14ff7922a2 | -11.20077 | -54.78361 | 2024-09-26 05:48:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8ba73567-50a9-3118-822d-3bd927a73296 | -11.2006 | -54.77104 | 2024-09-26 05:48:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| b7a3e712-a01d-35ec-807d-3ede4efb4843 | -11.19987 | -54.7771 | 2024-09-26 05:48:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 92d1f3f4-3092-3762-b5e3-48378d28bf82 | -11.19603 | -54.76448 | 2024-09-26 05:48:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 599a3730-9335-3f2d-8c59-c1d89630be5c | -11.19533 | -54.77079 | 2024-09-26 05:48:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1ae86553-11ca-3f36-9287-b10547c1d49e | -11.19454 | -54.76402 | 2024-09-26 05:48:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bcc312e2-b181-366c-9716-cf54aa792b1e | -11.19379 | -54.77033 | 2024-09-26 05:48:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 351a0802-b9f4-37fb-9bb6-3c8fba0ae267 | -11.18852 | -54.76999 | 2024-09-26 05:48:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4542ceb7-3868-3895-82d0-dd134cfcb675 | -11.01538 | -53.9502 | 2024-09-26 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 38d3136c-5768-3fe0-8e64-2b5a07a1d14d | -11.00906 | -53.94233 | 2024-09-26 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f79e51e6-a676-3586-b57c-e307be7026a8 | -10.93726 | -54.27173 | 2024-09-26 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6c2b64a6-ea12-30a1-9de2-7d1ea3521be9 | -10.93616 | -54.2732 | 2024-09-26 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7804b95f-88c4-3366-8f5f-f107e928cc0e | -10.93025 | -54.27109 | 2024-09-26 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 111e7ebd-83c8-3cab-8ce6-a2976047436c | -10.92917 | -54.27251 | 2024-09-26 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e2208186-0dbf-3531-9a42-79004d87d41e | -10.92221 | -54.27145 | 2024-09-26 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 131b3098-5197-30a0-a7f6-fedfa004fc61 | -11.49271 | -56.78097 | 2024-09-26 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47ddfaf4-c336-388c-b921-d1b401f785e7 | -11.48666 | -56.7803 | 2024-09-26 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ffa185b-dfb7-34d8-800b-daa7ef7e40a2 | -11.4851 | -56.77676 | 2024-09-26 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cbd028f-fd4d-32b8-ba78-2157a3dd7fe1 | -11.48453 | -56.78136 | 2024-09-26 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0101b2bc-948b-3e51-a3ec-8fec733a70d2 | -9.90839 | -57.06181 | 2024-09-26 05:48:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f8e5f2cf-888e-3553-ae29-7e698d341d9d | -9.90308 | -57.05715 | 2024-09-26 05:48:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2b9c58d7-7cbf-3559-9d7e-0a407e4f7af4 | -9.90256 | -57.0612 | 2024-09-26 05:48:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1acf315b-3fe7-3c5a-9daf-d4b8603b6a04 | -9.76416 | -57.79272 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afecb79a-b2c7-32bf-81ab-158b62359adf | -9.76091 | -57.77382 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d59b6c68-130b-30da-8de7-41182b47c11a | -9.76085 | -57.77815 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c8b4173-a15e-3c29-ac75-486ba32ee088 | -9.76037 | -57.78178 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c62152f-7a9c-3d97-88f0-999b3ed37423 | -9.75955 | -57.78468 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb87627f-60ef-384d-bc3a-3f3c836dd6cd | -9.75909 | -57.78832 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 501ff18e-0290-3c60-a085-70ff8b6ad052 | -9.69728 | -58.08937 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbad0180-eed4-3889-8564-7a5f79743585 | -9.6928 | -58.08162 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55db68e3-55cb-3c39-b3f0-5d12d56bfde8 | -9.69187 | -58.08859 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e02b0f5-0f62-32f8-ac50-42aa63fe1a8e | -9.69141 | -58.09206 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbc82cdd-f0c8-383f-8c19-00857c1f9ca7 | -9.69096 | -58.09555 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce43f1eb-83ee-37bd-b1d6-748375ce7862 | -9.70096 | -57.20329 | 2024-09-26 05:48:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac13870c-6953-356b-8d1c-d2b6ddb5ac0a | -10.31565 | -56.79186 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee0b9d0a-3050-3655-abdc-707437d8e185 | -10.31298 | -56.79173 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 26396a9e-e8a4-358e-9524-fed7c94245e3 | -10.3097 | -56.79113 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README168.md)
