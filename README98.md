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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1a97c44-eb69-3978-b428-6c2527c264d0 | -8.71238 | -54.79191 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8dd46b1-83e5-35d7-81af-eae9202d4df6 | -8.71232 | -54.77067 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54644a0a-9ae0-3500-9384-a748c606b06e | -8.71184 | -54.79537 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7796f351-0d4a-3e6d-a276-7f3b93da1863 | -8.71129 | -54.79884 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 705ae1a5-a055-37a5-b906-16dc1c135c77 | -8.71075 | -54.8023 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 87aa42d5-041c-3590-9fe8-0dba829458f5 | -8.70953 | -54.74536 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30d5ce91-38ba-3b2c-ae1d-6610ef05d168 | -8.70908 | -54.79139 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e520fb7f-4a34-3ab8-904f-b20fa0b87944 | -8.70902 | -54.77015 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c8e1c37-2177-305a-b79d-84e8609bfb04 | -8.70898 | -54.74883 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae1a138d-8eab-31f8-bc39-c0e57758e284 | -8.70854 | -54.79485 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd890c4e-bd60-38cf-92b8-4510f4d0121d | -8.70799 | -54.79831 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8668422a-68fb-3ee5-9068-4e83a8740295 | -8.70745 | -54.80178 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 560c4b2a-13a7-3234-9a42-d1694b131a77 | -8.70578 | -54.79087 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 129d1904-7732-342a-8494-4ab37d227a4b | -8.70524 | -54.79433 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2a01dcbd-eab4-361a-8a75-4ba226c8c7a9 | -8.7047 | -54.79779 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| afcade01-1aad-3a13-982d-d8ceceeccc3e | -8.70303 | -54.78689 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fcc074b-afc5-3830-9157-60eb15cd2568 | -8.70248 | -54.79035 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 52fd2c69-2053-38c4-b381-c85de9aee0f7 | -8.70194 | -54.79381 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 218e59bb-61c7-3ac7-bbed-6189bb060a6c | -8.70184 | -54.75125 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 720ed821-3f45-318e-9255-956b97d57847 | -8.69973 | -54.78637 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b3bec90-1a92-3f0c-b969-91739950a74c | -8.69918 | -54.78983 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e26f359c-c126-318b-8eb4-890fbcfea6b5 | -8.69854 | -54.75073 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7dc4fcc-0225-3546-ad41-cf68b8645fb5 | -8.69697 | -54.78239 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5da1b1b9-599d-3c9c-8664-2fa1165423b8 | -8.69643 | -54.78585 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8ab7b29d-6066-348c-aa43-4b2245da5f7d | -8.69524 | -54.75021 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5eb2c075-9afa-37f3-bd0b-2feaee54f796 | -8.69367 | -54.78188 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 41a77a80-73cd-3f49-8669-31ce89fa6947 | -8.69037 | -54.78135 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 16f5e46f-b632-32f7-9e2f-11ad6aad7594 | -8.68707 | -54.78083 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e37a85d-726d-3c09-abba-ac27b7a86b05 | -8.68047 | -54.77979 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4a8cef3-e630-3359-9ba2-f8d36d613669 | -8.67556 | -54.81097 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0dcb4648-73ec-3e3b-9528-82e94e19a23b | -8.67501 | -54.81444 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77142856-73a3-339d-8621-7754f21da9d9 | -8.43302 | -54.68381 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 884cd455-73ab-335b-be2d-25b12fc28617 | -8.43248 | -54.68727 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 838d255b-cea7-3c1f-a4cf-70e5a69fbf73 | -8.42918 | -54.68674 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d888a74c-340a-3de1-b9cf-1143961df1f9 | -8.42642 | -54.68276 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 773fff47-ab26-32bf-a58b-78955b4e15b5 | -8.42479 | -54.69315 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33e24aad-526a-38cd-972c-0bd9089da0e7 | -8.42316 | -54.70354 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74493838-d010-3afd-abad-9e93ebc9b395 | -8.42261 | -54.707 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3500b05-1d7c-3a78-b24e-ce4ef9634a56 | -8.41986 | -54.70302 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e630998c-e6ac-31bc-b3a4-04c868305146 | -8.21677 | -54.67383 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05bd61eb-bf13-359d-b10f-234a9d0a7d49 | -7.97535 | -53.82523 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b3ef84b-c75e-31fa-b0d0-87483362a652 | -7.97481 | -53.82872 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b76a0c8-0fa3-37b7-ba35-962dd31f4f8e | -9.46789 | -53.58401 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e343a6a1-ad52-3df0-b6e2-16740bf88846 | -9.46734 | -53.58759 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12ff6133-9321-39ed-b422-65056ba74880 | -9.46454 | -53.58348 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e012f9a6-c29e-30eb-904f-c9ffd06d69fe | -9.46065 | -53.58655 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b789a3e-cf20-3e67-a741-1674c07e91d9 | -9.45895 | -53.57525 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a8a4b93-bbf2-356a-b0ec-3f465082ba27 | -9.56816 | -54.03632 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf3b3903-a3d8-351b-b519-1dc66d60fb19 | -9.56762 | -54.03985 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74580f5b-4c82-38a1-8327-f3e205f560bc | -9.56098 | -54.03879 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68946cc0-802c-35eb-ad57-617af8d95175 | -9.5515 | -54.93078 | 2024-09-26 04:57:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23f4db58-e520-3fdd-b872-61c66bde1bb2 | -9.5482 | -54.93026 | 2024-09-26 04:57:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95061da7-73b4-3f17-84f8-6aa3cec79b6d | -9.52111 | -54.60208 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d2d5f7e-5c61-32cc-b80b-0f5274242959 | -9.52057 | -54.60555 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5c7a2b9-27bb-3f41-b32b-34a6d4f6f629 | -9.51726 | -54.60503 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00b14b93-81d2-3d20-ba92-f193b562f20d | -9.50635 | -54.01889 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c701e631-d526-3460-af60-075ce9f97d2a | -9.50628 | -54.61044 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 578f5fbe-e72a-3c93-b852-49513e0030a5 | -9.48746 | -54.55756 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45756e71-6f26-3eb6-9d6e-03038f3405ed | -9.48471 | -54.55355 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31732d7d-f702-3883-bd44-0cdc641554a8 | -9.48416 | -54.55704 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6cdf28f-bae2-32e7-bc11-19ed3bc8872e | -9.48362 | -54.56052 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8b73a15-16f3-3e27-bb0d-3000e2c4dab3 | -9.48308 | -54.56401 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25757b50-6b83-33b4-bd30-5a5b8b91e2c4 | -9.48254 | -54.56749 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4491376d-1ea6-33b2-a248-c858453f4a02 | -9.48086 | -54.55651 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54c396e7-9e11-3a7b-8729-ca321b8cd8bd | -9.48032 | -54.56 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee7d8799-2841-33c9-b304-fd916fef69c1 | -9.47978 | -54.56348 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42191030-51a7-3fb8-b4ff-5564c679482a | -9.4781 | -54.55249 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4382753-afe1-3b15-83c5-37346827e43d | -9.47756 | -54.55598 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cae5ba75-205a-33e2-ab86-6030a6a2d941 | -9.47426 | -54.55545 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62befbb8-b47f-3284-b2df-3d4af7318a55 | -9.46712 | -54.55788 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2201e85-4a19-3537-b6d5-cacdc4797f47 | -9.46657 | -54.56136 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68d665c2-a9b5-33e3-92e4-f046d904cba4 | -9.46603 | -54.56484 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f8483b25-d37b-3b8c-8986-b70bc4d4837a | -9.46285 | -54.5601 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7b1cef8-72f8-3960-868f-9147af06781c | -9.46231 | -54.56358 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0fc268a3-f109-310a-bd05-5fd705de0021 | -9.39775 | -54.73841 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a3b15a4-b0ca-38df-9214-30daffb59dfd | -9.3972 | -54.74188 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f97109ea-2b6f-3fbe-900c-8bb33ef87560 | -9.85438 | -53.83398 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d37bd225-9225-3510-8818-f47752a0ef43 | -9.84837 | -53.87312 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 906e6a34-d1dd-39f2-a1f2-693ffc732c5d | -9.82232 | -54.10838 | 2024-09-26 04:57:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 682f8964-c593-3dd8-8d42-bb172ba4f898 | -9.82178 | -54.1119 | 2024-09-26 04:57:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57eb0329-7015-3194-81ec-2f41046d6b52 | -9.81933 | -54.01751 | 2024-09-26 04:57:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 001bcd3a-1984-3fac-84ca-586f58339e7b | -9.819 | -54.10786 | 2024-09-26 04:57:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b93d650c-8efd-39b5-b7c0-3930ddccf765 | -9.81846 | -54.11139 | 2024-09-26 04:57:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac10f22f-8daa-368c-9181-79716b46964a | -9.81738 | -53.59013 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7276d1e-8c8b-3aa4-b054-8f287120f823 | -9.81323 | -54.01292 | 2024-09-26 04:57:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f917c167-36dc-3573-a455-02dc4659b598 | -9.81122 | -53.5855 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a4ffb66-f12e-3d82-afcc-cdf97f326e59 | -9.81067 | -53.58909 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b198ade-abc5-3a41-96df-4027a187eac0 | -9.81011 | -53.59269 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f65eb59a-4581-3853-826f-59f18bd53f74 | -9.80842 | -53.58138 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d7bfe58b-2620-357b-89fb-9f14054b5838 | -9.80786 | -53.58498 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea23c445-01a9-3c92-a679-b641612c0bfa | -9.80731 | -53.58857 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92fe768d-9099-3955-a5ad-88dcd0e99967 | -9.80676 | -53.59216 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00ab6007-d082-3922-82be-524f883241dc | -9.80506 | -53.58086 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b9c1e7e-fcee-3b23-b7c8-cffd315356a4 | -9.80451 | -53.58446 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94e1d395-e173-3c9e-b206-965038e03f33 | -9.80396 | -53.58805 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29f14c04-2729-3fea-a6db-a13bd09c290e | -9.80341 | -53.59164 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 700bcb79-f23b-31a6-a7c9-7070806cbeb7 | -9.80285 | -53.59524 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15fc43a5-eaa6-37aa-91e9-37325c224cc8 | -9.8017 | -53.58035 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db07874c-5ea0-3a1d-a5b5-89114c2d1151 | -9.80115 | -53.58394 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c13421bb-5c19-3766-bc2d-83c41e604cb8 | -9.8006 | -53.58753 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README99.md)
