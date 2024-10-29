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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1ac6155-771c-3b78-9770-d4aaf59ba25a | -3.67634 | -52.27285 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 955cf7cd-25a4-366f-b08f-a3d8e962df5d | -3.47546 | -53.25722 | 2024-10-29 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c70b1fb-402f-3594-b9c1-eb4ece36b37e | -3.40066 | -53.6914 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23e28637-6cf3-3cf4-b24a-3f16aa9cdaf4 | -3.68 | -52.27343 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c697cc66-5313-30e6-bc23-35606131e17b | -3.67932 | -52.27773 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 782bfda1-d7c5-3a8a-83e3-57df1654f5de | -3.67565 | -52.27715 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8623a878-d4ab-339c-b22d-a72a673f889c | -3.47626 | -53.2523 | 2024-10-29 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 811a5b02-6458-3f89-bf06-ce7b498f4cb3 | -3.47238 | -53.25163 | 2024-10-29 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7fc02874-075b-3798-a012-4f4383017fb8 | -4.20866 | -53.86602 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b004b54-cdbd-3c83-9a82-717f42357782 | -4.20811 | -53.86934 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2be6ddac-3686-3f84-aec5-a1697c95fffe | -4.19937 | -53.46107 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65fb8d7c-c1ad-3423-b69e-511ebbbe0d00 | -4.19856 | -53.46601 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50e80aac-c7ce-32d2-9e31-235223d202cd | -4.05006 | -53.41136 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3a10d6e-edcf-3bfe-bb95-0e7ba6623142 | -3.93644 | -53.4675 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 022569b2-bad3-32fe-b80a-78719c67c53f | -3.93627 | -53.46952 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aac9ede6-356d-37ce-b609-4068a4903801 | -3.91542 | -52.39469 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a05e5ef-6192-39f8-b305-590b73b4dba2 | -3.90929 | -52.36304 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7bf5e741-14ae-3788-8e16-6151db1b0e9c | -3.894 | -53.63175 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6e26f06-05ed-3b52-a10c-385c70c1a79e | -3.8877 | -52.38253 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 834ac223-bfe9-3b22-a272-4707a5deba3f | -3.88473 | -52.37746 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dde4c4fd-edad-30a8-a06c-e76a3b93eb81 | -3.88467 | -52.30702 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77481294-6ca5-3bf7-a8b9-07fcba7b9821 | -3.88037 | -52.38116 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9df08182-e95a-3628-b669-fdff96d733c3 | -3.83424 | -52.40986 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d9c4cdd-c9de-3813-a8b2-af991f24b98b | -3.83353 | -52.41428 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 435b3bf2-2c94-3312-b9bb-4fcdddb8b0fe | -4.27639 | -53.62936 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 847960f2-9a96-3ea9-a788-771848abb247 | -4.21949 | -53.5099 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0bf65ec7-0796-33e8-8d6d-97ad204937f2 | -4.20327 | -53.46172 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1498536d-b38a-3937-909c-2bae4f86f4ce | -4.20246 | -53.46667 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5f0cac1-37b6-3fbd-8c77-d3dcb11facb3 | -4.05093 | -53.40983 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bebe5069-8224-33d8-8025-3ac2d6920047 | -4.05085 | -53.40642 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50870d59-7cb1-3ffc-af34-feefbf7d4eff | -4.04183 | -53.23985 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efab8cd3-a71b-376e-a1d1-9c50396d9737 | -3.96556 | -53.43832 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 447421fc-8787-31ee-9d61-b83f766029ca | -3.93957 | -53.47307 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e52ce4d0-dbb4-3815-aa28-17107f0d5303 | -3.89482 | -53.62663 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4198bfb3-a016-347e-8467-1f444ada72fa | -3.88403 | -52.38186 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 88bf3829-4bf3-3fe0-a4b7-2667f484549a | -3.88331 | -52.38642 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 79b526e3-4281-3278-a41b-158ed5d640cc | -3.87963 | -52.38583 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb121642-d036-3ef6-ba4a-803c2e553105 | -3.79375 | -52.28977 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7164d8c6-95d1-349c-a91c-13f27e1b731e | -3.72095 | -52.34464 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b65eae9e-cbfb-302d-b25e-e9989a726be9 | -3.61533 | -53.50953 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d4ce954-04d5-3c1a-896b-77343648a4e5 | -3.61171 | -53.51176 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8bdc02c-5902-3022-a548-0903c6ca9445 | -3.74168 | -53.40385 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06dc7dff-31d9-3018-b146-3b6d09e64b6a | -3.74104 | -53.4058 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 05ef8d64-2f03-33a7-b681-8b87e21727ca | -3.74085 | -53.40884 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00b3421e-1370-31a4-b44a-8a51763084e4 | -3.71249 | -53.7286 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9d49ee7-59d5-312d-aac2-48418f062f7a | -3.61567 | -53.51238 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d145c760-dac4-3425-9255-c30cacffc97d | -4.20921 | -53.86269 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc3772ba-b2bc-30dd-a794-edd5b8f97745 | -4.20524 | -53.86187 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9d208dc-c295-3cbe-a0aa-2f3589a2996c | -4.20412 | -53.86861 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15231ccf-685e-3182-95cb-e248f7527da2 | -4.17794 | -53.74088 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b18f16dd-0df7-3e41-8e7f-0ddd24460666 | -6.16848 | -53.58378 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| adec54d7-9d00-3b87-9f7a-2e5e7ff59d52 | -9.47779 | -54.52713 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a0c39b23-a483-3f29-8636-54aebda40578 | -9.38488 | -54.81177 | 2024-10-29 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 290c6d12-fbbb-33c2-a30b-963776cca203 | -9.50469 | -54.46172 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f48309dc-7710-361d-ba0d-191c4734b731 | -9.47392 | -54.52654 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0da2c775-acec-3590-9d29-b094c95acfec | -10.34187 | -55.01635 | 2024-10-29 04:40:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e42b608b-2bc1-3832-8293-48e77542499a | -10.10384 | -53.64206 | 2024-10-29 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c787da4c-e05a-3ebd-bbc5-29b99427d7d1 | -10.03581 | -54.33243 | 2024-10-29 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a79b3be9-00d7-389b-ba15-97bb1a69d6ce | -10.03203 | -54.33176 | 2024-10-29 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fe00b00-ca5d-3f10-85cc-2f716771cf9a | -10.02826 | -54.33107 | 2024-10-29 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5222268b-4720-3f88-8b8e-a0c3c9a37514 | -3.34039 | -54.61556 | 2024-10-29 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d240024-5a8c-33fa-b410-c1f0c1566332 | -3.33169 | -54.80187 | 2024-10-29 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 994ee265-57aa-3868-a3b4-a933194a88fa | -3.331 | -54.80606 | 2024-10-29 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c541adc1-4fd3-32ed-afaf-7eb6efda711e | -3.3063 | -54.69766 | 2024-10-29 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6d948f8-f4fb-3851-9eaa-d4a5625bccd5 | -3.30497 | -54.69643 | 2024-10-29 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4ed3b40-de5f-3c7a-9574-c90994155dfa | -3.302 | -54.69703 | 2024-10-29 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac9798a7-6d27-30e4-b640-c015ac67bfe0 | -3.29013 | -54.7161 | 2024-10-29 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c0582b2-5813-3d0a-8ff8-83d4863dcbb2 | -3.59482 | -53.78274 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| fbddb5a6-8613-37f0-9a3f-3884494f5b80 | -3.59078 | -53.78223 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f10c5eb-6a3a-3a00-8ec3-848aa0e87bc5 | -3.59019 | -53.78583 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3cbdd49-3a1b-332f-a03a-8b25e7c2c94b | -3.67158 | -54.07946 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a363b0ee-41fc-3d4a-ade1-1732758518e8 | -3.66811 | -54.07495 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93f2f500-bf42-3888-954e-d04a537c9600 | -3.58904 | -54.66319 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6381d4e-3bcc-31cb-9030-228d0337ba8c | -3.58766 | -54.56515 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfde95f8-a62d-3972-ad8b-d41c0a97a673 | -3.58543 | -54.65849 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6dcfff4a-920d-3329-8dd2-d006f0bd7157 | -3.56872 | -54.68031 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f775ea00-9934-3106-98a9-30cd3bd38285 | -3.56641 | -54.66774 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57d0bf9a-2a1a-3cb3-ac0b-4fd80525c9bd | -3.56575 | -54.67171 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c200619f-ce50-386e-ae6f-c48ae808de91 | -3.55603 | -53.99328 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 267e12a8-6b45-31eb-9c85-11a4c94c3e01 | -3.54616 | -54.76377 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b7d5f19-48fa-35ee-9c89-851db1a68bfc | -3.54589 | -54.73879 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c355cb43-4502-330d-a2f8-0192f9f79e91 | -3.54189 | -54.76295 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46316c8f-07c6-35f9-bf6b-bc48c3c9f1f7 | -3.47303 | -54.57506 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75768be9-5202-36c9-8e3b-0b0607f454a6 | -3.46704 | -54.82689 | 2024-10-29 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f6d35c3-727e-3fe9-b020-bdc440de6034 | -3.46097 | -54.62182 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3a97dd6a-4066-3c9f-a316-d64699b9825d | -3.45995 | -54.20121 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 818b5db3-4a5e-3958-8c75-580b2d75922a | -3.4558 | -54.20057 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf8ecd32-db62-3ad6-94f3-ddbb3cfdf296 | -3.443 | -54.14884 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f727342-f7c0-36ba-9fe4-fe310e1d2544 | -3.44192 | -54.25998 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fc64801-b2dd-3fd8-a5a1-d26e3fe21b7e | -3.44131 | -54.26372 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6fc4f358-63e8-38f9-9bb7-5b198e667926 | -3.43889 | -54.14811 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22cbd528-b29e-3d36-91af-a26052dc515e | -3.43775 | -54.25934 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0a0c289-e701-3c4c-8263-a55b9bf0cb69 | -3.43714 | -54.26308 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf532c7b-6d56-36ca-91bf-d2c17629af80 | -3.43178 | -54.2698 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4ebc461-578a-34c5-ade2-6646058dfaad | -3.42733 | -54.58763 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b12929f-3468-322a-8492-76fc85675c6a | -3.4218 | -54.14896 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e6b898e-b5af-3322-9772-2995e68622a0 | -3.40913 | -54.48861 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5bf399b-4822-3234-8290-c16617a74322 | -3.40849 | -54.49252 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07668763-6976-3fdd-9ad6-9ae405d4e2dd | -3.40786 | -54.49644 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 723dced8-211e-355f-aa6e-161e546eee9c | -3.40371 | -54.05931 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README65.md)
