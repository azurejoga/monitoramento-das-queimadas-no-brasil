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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fddedf1-16af-3ca2-98a8-fb18ad6576d3 | -1.09555 | -53.389 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e78feee-57cf-3e5a-9f18-b02c467c594a | -3.60707 | -49.98923 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 75db3232-27df-3513-9105-20f62ba03bf7 | -2.54636 | -47.98085 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ed4607f-d46c-30c3-a329-167c8fb77475 | -1.04221 | -51.74037 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4a883858-ff7f-3cd1-860a-e1089446b3bf | -2.9399 | -49.12246 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a147406-6d7e-3b45-a30c-839a2eb17dac | -3.30842 | -51.57368 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d2970a0-2b56-3ad4-938f-a5b086dce0a4 | -4.34944 | -48.13038 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b2d5f60-ede5-3be9-ba5d-bee586a374c4 | -4.62368 | -48.02405 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d82b051b-bfae-37c6-bc5f-caaf303c64fb | -2.42133 | -50.47925 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8a1713d-59d1-394e-adaf-85cf9bd862e1 | -2.29705 | -51.98567 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4eacf52b-f15d-3897-8e9c-25c2594c9a05 | -2.66297 | -48.78354 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3882e533-1231-311f-8976-96b4076481ba | -3.51456 | -42.17788 | 2024-11-30 04:40:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c0a98812-bec1-3de6-bf3f-4fbf67aa2a24 | -1.10996 | -51.74155 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1f99e10-676d-34ae-a8d2-a7c79a7a7daa | -3.44803 | -49.48399 | 2024-11-30 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c981f29-1b62-3c7f-988c-0a0a40e99ab7 | -4.43868 | -46.00884 | 2024-11-30 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| c66b5ffd-f298-3e2e-ba43-136503b0a0bb | -3.06528 | -49.36388 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95b1ec9e-5013-34a9-a921-af39cdd55afd | -2.31529 | -49.07014 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa17d587-5a36-30e5-a42c-551fe5e83e86 | -2.96097 | -48.61564 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d1725bc-4e62-356f-9876-9ca0713744ec | -2.61077 | -54.20468 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcf3ddcd-0b39-302c-ac7a-175c31e26a82 | -2.72519 | -48.66656 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82b9507d-e894-3f2e-b94a-c5c15af6f814 | -1.56767 | -52.14145 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d406da37-04d0-3f13-983c-eb57c9f2e4ef | -1.51587 | -51.14517 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95515623-be45-3fc3-8c79-4a6f494ef3db | -4.6785 | -48.15248 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac2dba5b-64ef-33c4-99a3-8cba148fdc95 | -4.17515 | -48.61774 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ee4cef1-6386-3d60-8b58-9afe6af6b00d | -1.16461 | -53.77412 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a18acad-2366-340b-8c08-8f908c3ab160 | -2.37784 | -47.88374 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 365415c8-ec6b-3fc8-9594-7a13cc2f2701 | -4.82077 | -41.28165 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 13e93375-8654-3985-a493-624aec26b41c | -2.98556 | -53.2923 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88a68615-b129-30ef-aebc-7a4095db2a3d | -2.18643 | -48.39225 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 860f4834-6721-3b5a-abe5-a0213cd3a38d | -3.29847 | -53.69221 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3db5c60b-1c19-3144-abb5-709c86785bd5 | -1.33655 | -51.42978 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab68d7f3-8fd3-3edb-944c-820b8eb89ce0 | -1.27314 | -51.62949 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b23a19f9-7a92-3909-ac58-5188a3a57b41 | -2.43441 | -50.39587 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30958e06-6680-3237-b71d-e342b03aa591 | -3.11055 | -53.1026 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27b2ec81-8479-3e1e-aa13-279de5f659ec | -1.14175 | -53.70626 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88f9ca4e-d8c1-3660-aa1a-c56c1137a627 | -2.79756 | -53.04536 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8bc74f4-3cfd-3e31-903c-ffd9c0b6e8ed | -3.27314 | -50.55505 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e70a6ef5-1a14-31e5-a5f9-ee917a2ae1c1 | -3.97944 | -46.64247 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc30d599-f6d6-3ef0-8871-e9f0dc0f3b90 | -3.25461 | -53.29078 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0037a80a-eb04-308c-ae14-b067df15b8fc | -3.4679 | -46.19703 | 2024-11-30 04:40:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0deb0b31-2b9f-3b5f-83f1-891a9b7c6a45 | -1.43238 | -53.39407 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb7d3e7a-b1b1-3e08-9262-c55b61a3424a | -3.93526 | -52.15035 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4fb0a87f-8e22-361a-b395-697b0ff34158 | -2.06403 | -51.1872 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 307bcee1-5c92-388a-ba7e-0b93d0e9dce0 | -3.79106 | -49.94322 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1943a1ea-6676-3b64-ad0a-38d6c41a28ad | -2.59197 | -53.98108 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c71eb4e1-8a92-30ee-86e9-6c63807601b2 | -3.05272 | -53.24393 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8ad38c6-8b02-3084-9cd9-e9b169405303 | -2.20059 | -52.24022 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bd6f0bb-cc76-3082-8f1b-6d1c47dcbfbb | -2.5388 | -46.41616 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08874fe0-e2c5-3ac4-b7ef-3cb5ee6034ce | -2.27681 | -48.42435 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5c173ec-7c45-3f8e-afcf-4eae0446638e | -3.40533 | -53.02938 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3d6e3825-8fdc-38a9-97b5-4943227e4aac | -3.74593 | -54.68369 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d3821c70-403a-37ed-9b31-537ce7de6cc3 | -1.65707 | -52.40642 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58b2c033-580f-3da7-aa76-27044309fe43 | -2.63197 | -51.74484 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| f45ac2c7-d915-3003-bf8b-bfed4e6f12d4 | -3.01845 | -49.53346 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 564aad6d-3a18-3e81-bc8a-d9eb8f0b641d | -2.83569 | -54.10128 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc066ec8-34a1-3f1f-b512-20c01f792b97 | -3.51399 | -53.77823 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18faace6-e739-319a-9f40-49c608892813 | -3.17012 | -46.29695 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 374b0a4e-4f23-3839-ab7b-d10a56c09de7 | -1.41064 | -51.58644 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| adabbf4c-3847-33d5-b422-549dee3ad66e | -2.17918 | -46.60756 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d16adebe-b5bb-3d98-abb0-ff99cd5b7cc7 | -1.19118 | -51.77425 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b61e8de-4121-3009-9cb1-ca87375ebc2c | -3.91249 | -50.10182 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d7c7e9b-3a45-38e2-a2be-8a0f3325370a | -1.20175 | -51.75446 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1b5efaf-671b-33cf-bfe6-c874c7308309 | -3.97191 | -41.516 | 2024-11-30 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 919b942d-0c9e-35e5-abe8-55e3f93d8918 | -1.18755 | -51.7737 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9547d597-cc6e-3618-8bb0-ce864a0e4f31 | -3.60151 | -49.98119 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b228c1eb-5cb0-3115-bcda-f4245fa444b9 | -1.598 | -52.28485 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8d62f34-6fe0-390a-936e-bbe1422c4927 | -2.77507 | -50.30501 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdf979bf-d5cb-39a2-9938-30027e874743 | -1.17165 | -53.41239 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2c58645-07ae-39bf-bd32-668e8240d348 | -1.31679 | -51.66879 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae41723c-a9eb-3bb4-ab12-e94771690fa5 | -4.25357 | -47.57853 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 86771276-4570-3b3c-b8a2-ba5d279d8576 | -3.46669 | -50.23422 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cbb2737-47ea-32e3-942e-0ba4260d8912 | -2.73663 | -47.98214 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4a6a3b8-be70-37ac-8aa4-d6b9a3bfc150 | -2.61156 | -46.57943 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d6b075a-d06b-35ca-8de6-bbc2933ae8cb | -1.17965 | -53.41364 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a107c683-e029-3aea-bdae-87b885ad2e80 | -2.90315 | -54.17501 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6b05e9b-17c2-319c-a30d-233855e212cd | -4.97943 | -47.23437 | 2024-11-30 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6ab8d18-fb5a-3979-83d7-d08381bfd54c | -2.69269 | -48.65805 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77fe3241-c83f-3b3b-a936-882162d72e68 | -4.08611 | -47.02073 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da40d25b-8c5b-3eaf-933a-d646a343ef23 | -3.87214 | -49.83832 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cb15630-0141-3cce-9bec-1100124be1c0 | -3.60155 | -50.00272 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5266249b-3491-373a-83cc-d4727c48a96a | -2.80422 | -54.06305 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3f19b79-a74d-30c0-8c20-df30d330f889 | -3.96333 | -48.09608 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16f4bdea-ef6c-3a13-9406-bf9d856c0d44 | -3.8136 | -46.58663 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8196fcd1-d8bb-3506-9aae-1dff1ce0d9fc | -2.20654 | -48.32842 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe44aee1-a6e0-31de-b9a1-f0f59e35be63 | -3.21016 | -50.28485 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b78174a6-7720-3b4d-a722-bf1f86f0a08d | -3.53048 | -52.15731 | 2024-11-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 259e6be5-1ec3-33f9-8c8d-168c08397629 | -2.7109 | -46.19839 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8b38676-d1e9-3218-98eb-e10b22860709 | -1.21129 | -51.7645 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d56c9661-9d19-3b91-9c81-5d31e64a5cad | -3.25495 | -54.21996 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b820354c-ee0c-39c8-ae5b-1a1fdef4a892 | -1.87388 | -53.95773 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 779b34c1-8fd8-3333-94ee-45561ee29a5f | -4.56701 | -48.61129 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e399000-143a-30d0-adf1-6137ed02c4d0 | -3.30475 | -50.37604 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0542e107-a9b7-3082-a111-9b82b35bc271 | -3.1415 | -46.62201 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f200bf91-7695-3763-bfe7-e137dc41b324 | -3.09702 | -54.29245 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f505bec-a1b8-3872-aa1c-cdadba0d4aad | -3.94881 | -49.76131 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e75ab8b3-54cf-3db4-82db-8dc9ae0786b0 | -2.27383 | -46.4242 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d25171b7-c722-3a83-ae14-a0762841f411 | -3.50102 | -53.8335 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 092f675c-1fc8-3770-b193-f6466766bd1b | -3.18386 | -50.27714 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b6f7421-0596-382a-bb57-6699765720ef | -6.07529 | -48.04713 | 2024-11-30 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 80bb7038-1bf5-3296-b52b-20831e10a483 | -2.46314 | -46.56076 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README62.md)
