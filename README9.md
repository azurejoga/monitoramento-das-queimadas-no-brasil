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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 299973ae-4a4d-3ca7-a6c4-7f6d3f5b20f8 | -16.4865 | -57.378799 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3f314b03-c1a7-3945-a9ca-9ffa4debf845 | -16.464001 | -57.3214 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 320b85a8-514b-3053-8a15-53bbedcd6ee0 | -16.465599 | -57.3288 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b16f99c7-f35d-3b33-b51e-44f965c6ddf1 | -16.467199 | -57.3363 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6665fb53-6c1e-3bde-afec-6dcf9989010e | -16.4704 | -57.3512 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 18b52cf3-b460-343f-9ee9-a2bfaedd4d28 | -16.472 | -57.358601 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f6c268a3-3068-3521-a2d9-e8b93f832016 | -16.473499 | -57.3661 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 18e6c0f2-86bc-3129-b9d5-ed3aa202da72 | -16.4751 | -57.373501 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f6b087e4-7a09-3bee-8fae-4b20137d683a | -16.4767 | -57.381001 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0e4ed675-c462-33cd-accf-5ed51f9871e0 | -16.4527 | -57.3162 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 474272dd-7d70-38c4-beed-97df0b417f9f | -16.454201 | -57.323601 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f8b8dae3-dd49-30a7-93b2-66593a892062 | -16.455799 | -57.331001 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1e84da43-ce54-3c80-8496-10dbebcbae54 | -16.4622 | -57.360802 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cfb135ba-7f3b-33d8-b237-cd36524803ad | -16.463699 | -57.368301 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 285a9a94-a72c-3034-afbc-2e8f4f458f84 | -16.4669 | -57.383202 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8d0946cf-6b3f-3518-9331-fc9b0d46c28b | -16.4685 | -57.390701 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 65e03572-e522-37da-92f8-8b1b678fb9a0 | -16.4701 | -57.398201 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 498fb184-b65a-3f3f-b580-b8b4d6fbf385 | -16.474899 | -57.420601 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7450a1dc-e11f-3a34-a346-fee29f2ebb25 | -16.4587 | -57.392899 | 2024-09-30 01:11:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 69ff2f83-d9f8-3fe4-b366-18429d3a7944 | -15.8975 | -55.382999 | 2024-09-30 01:11:07 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 55b6f3ae-1966-3df6-ade9-46fbc2c1781e | -15.8991 | -55.390202 | 2024-09-30 01:11:07 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 37b2cef5-8e78-389c-9580-ec3b06abc269 | -16.123899 | -57.507702 | 2024-09-30 01:11:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d612947e-6ac3-38cd-9e03-394b71142ef8 | -16.1255 | -57.515202 | 2024-09-30 01:11:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 925fc707-535c-3708-8269-fc3ab120b6f4 | -16.1157 | -57.517399 | 2024-09-30 01:11:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2962a835-7aed-3151-9d60-8b771c85cd1c | -16.1043 | -57.512199 | 2024-09-30 01:11:12 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b17d379c-dadd-3ae8-8497-4cea8ad4e53f | -16.1059 | -57.5196 | 2024-09-30 01:11:12 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d36e197-c0b3-34d4-967d-ee0d0c2f5a73 | -15.9404 | -57.1772 | 2024-09-30 01:11:13 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0edf7f16-10f6-3615-ba4a-a6854b8cfbad | -15.942 | -57.184502 | 2024-09-30 01:11:13 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 576448a9-698c-396f-832f-7a32b3e8692a | -15.9275 | -57.164799 | 2024-09-30 01:11:13 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 376b55ed-ef2d-34be-8791-624e11fab713 | -15.9291 | -57.1721 | 2024-09-30 01:11:13 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e62384d-5550-34c2-8006-25f3466197f3 | -15.9306 | -57.179401 | 2024-09-30 01:11:13 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 291bcdb4-8f12-3aa1-b2df-f2ffad13beab | -15.9322 | -57.186699 | 2024-09-30 01:11:13 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd5e4e43-6391-3d6d-afab-6a752e8facd6 | -15.9161 | -57.159801 | 2024-09-30 01:11:13 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85709cc3-90ca-383f-a685-347e8ec9ab61 | -15.9177 | -57.167099 | 2024-09-30 01:11:13 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4a42ff77-d985-38bc-8fc8-1caedb7d8173 | -15.9193 | -57.1744 | 2024-09-30 01:11:13 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a3ebe0f-7229-3eb3-9480-8eaae682ff2a | -15.9079 | -57.1693 | 2024-09-30 01:11:14 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3be81541-5cd3-398b-9d20-ba35517867ec | -15.9095 | -57.176601 | 2024-09-30 01:11:14 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cda6e216-eaed-37f1-b5c2-e3433649870a | -15.9126 | -57.1912 | 2024-09-30 01:11:14 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7c50dab9-399a-387f-9d1d-d01d731a7fbe | -15.9142 | -57.198502 | 2024-09-30 01:11:14 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 49f482f8-09ab-331c-87c5-2cdd0626036d | -15.9157 | -57.205898 | 2024-09-30 01:11:14 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0efda85c-6621-3673-8354-c563f6c1f978 | -15.8997 | -57.178799 | 2024-09-30 01:11:14 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 076f189d-62dc-3774-9915-1dbf1b9bc8f2 | -15.9012 | -57.1861 | 2024-09-30 01:11:14 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ac6c6d04-80c1-3fff-907a-66122c377700 | -15.9028 | -57.193401 | 2024-09-30 01:11:14 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 42b78e54-9118-366c-b8d0-327732eec4a7 | -15.9044 | -57.200802 | 2024-09-30 01:11:14 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e46cb36-c625-352e-bc5b-c68ad0eb3349 | -15.9207 | -57.421001 | 2024-09-30 01:11:14 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d141dbce-a401-3820-860c-3829e72d4711 | -15.9223 | -57.428398 | 2024-09-30 01:11:14 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54e02d8f-b9be-3fc2-981d-efcd4198832c | -15.9239 | -57.435902 | 2024-09-30 01:11:14 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6170eafc-4abc-3fbd-871d-9593eac09611 | -15.9109 | -57.423199 | 2024-09-30 01:11:14 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46c2f0f3-53c5-3d8a-804d-24ac1970efb7 | -15.9125 | -57.430599 | 2024-09-30 01:11:14 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 910dcd1e-eb54-31f4-9ab2-ce52d73f6b45 | -13.1864 | -46.290401 | 2024-09-30 01:11:15 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 88d6e371-f1da-3c30-b86c-1f3c84d15734 | -13.1926 | -46.313599 | 2024-09-30 01:11:15 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 27f1e6de-d878-3a2f-99ca-4a2c7d62646d | -13.1768 | -46.293098 | 2024-09-30 01:11:15 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aa0e1eaa-63c8-3cb5-a0fc-3e99d282c1ad | -13.183 | -46.316299 | 2024-09-30 01:11:15 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 45294ee7-880b-37dd-bed2-4dff9276fd1d | -13.1672 | -46.295799 | 2024-09-30 01:11:15 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f916393-83af-34ff-88a4-ac4828cc2f5c | -13.1734 | -46.319 | 2024-09-30 01:11:15 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| de5062a7-6696-39da-a385-ec358a421579 | -13.1796 | -46.342098 | 2024-09-30 01:11:15 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 58102b9c-fe92-3279-bb0f-cd64fbcea60d | -15.8282 | -57.3722 | 2024-09-30 01:11:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d09c754d-b68d-3507-b3e6-d1b91a0d6bd7 | -15.8297 | -57.379601 | 2024-09-30 01:11:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 43ace2ac-8119-367b-9e5e-64ea88da4cee | -15.8089 | -57.3302 | 2024-09-30 01:11:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d7467d3-833f-379b-93bf-c2d75e322f17 | -15.8105 | -57.337601 | 2024-09-30 01:11:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d996fb74-ad07-31f7-abf6-e09864681957 | -15.8121 | -57.344898 | 2024-09-30 01:11:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 313fafad-9759-3c8d-9cbc-347ded5e642c | -15.8152 | -57.359699 | 2024-09-30 01:11:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9c441c5f-211e-3e4e-9f3d-ffb9edd99d94 | -15.8168 | -57.367001 | 2024-09-30 01:11:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f122b227-513c-3f74-af3b-66a15e28e3e7 | -15.8184 | -57.374401 | 2024-09-30 01:11:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2f9b25f8-f940-3ec8-b367-4ce06039876a | -15.8199 | -57.381802 | 2024-09-30 01:11:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6e4d38ba-bfb3-3ee1-afde-f3311f18e0b8 | -15.8023 | -57.347099 | 2024-09-30 01:11:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 79c6b12a-56b5-383f-a910-226177e2fa7e | -15.8038 | -57.3545 | 2024-09-30 01:11:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 930ef0fd-99b4-365b-8f65-2a3db6c4e787 | -15.7786 | -57.766399 | 2024-09-30 01:11:18 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e57d60dc-005c-317c-b747-d052ea271f47 | -15.7802 | -57.773899 | 2024-09-30 01:11:18 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 840b58b6-841f-3d5c-a60a-726fb7b9a0bb | -15.7819 | -57.781502 | 2024-09-30 01:11:18 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ed95af15-52a0-388f-af80-d857f88ed2d5 | -15.7835 | -57.789001 | 2024-09-30 01:11:18 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc8a28aa-04f6-369d-b73f-df86707f99f9 | -15.7704 | -57.7761 | 2024-09-30 01:11:18 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4d3a380-5d18-3361-aec8-203ffd94a0f7 | -15.7721 | -57.783699 | 2024-09-30 01:11:18 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c4797da-b1cb-3894-b4f4-2ea9fa613bac | -15.7737 | -57.791199 | 2024-09-30 01:11:18 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d157a716-b525-3d6e-b695-58940f57b826 | -15.5731 | -56.903301 | 2024-09-30 01:11:18 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e56597f-b835-314f-b287-9b745a02ff2e | -15.5746 | -56.9105 | 2024-09-30 01:11:18 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e1de455e-aaa6-3328-b57c-88959d6b3d91 | -15.5601 | -56.891102 | 2024-09-30 01:11:18 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 430779a2-50d5-3875-8717-0bc3571027b0 | -15.5617 | -56.8983 | 2024-09-30 01:11:18 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5362d163-0fe3-3a29-8937-21bf14e5fef2 | -15.5633 | -56.905499 | 2024-09-30 01:11:18 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9b60f8ac-b4cf-3d02-b07c-3f485f5bd5f5 | -15.5503 | -56.893398 | 2024-09-30 01:11:18 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ad97c76b-8c3c-3839-8822-ebcd168beae2 | -15.5519 | -56.9006 | 2024-09-30 01:11:18 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5da6232d-b0c8-3f87-9988-01eff6b52060 | -15.5535 | -56.907799 | 2024-09-30 01:11:18 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 161f7b49-7541-3ff8-b54a-20d15aa47f54 | -15.555 | -56.914902 | 2024-09-30 01:11:18 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d2776530-ceee-3f22-92b8-145d53fb8489 | -15.5405 | -56.895599 | 2024-09-30 01:11:19 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9faa7d3c-9405-301e-b222-e35b6420287a | -15.5421 | -56.902802 | 2024-09-30 01:11:19 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0f409f7d-819f-3f0c-a097-3a25bcd570d4 | -15.6288 | -57.448299 | 2024-09-30 01:11:19 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f79712f8-aa48-3710-a4ca-dbcd70a9a78c | -15.6304 | -57.4557 | 2024-09-30 01:11:19 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 82a93169-ddba-3776-a1e7-3ef600065ea6 | -15.6174 | -57.4431 | 2024-09-30 01:11:19 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ab463246-93c7-308d-9338-0787de09fb59 | -15.619 | -57.4505 | 2024-09-30 01:11:19 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e3b5ec93-de17-3267-9438-637239c72d4c | -15.606 | -57.437901 | 2024-09-30 01:11:19 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c0c6b920-445b-35a4-a400-02fc8402fc6c | -15.6076 | -57.445301 | 2024-09-30 01:11:19 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 711faf5a-6e0d-32b4-971f-a2ea9f3ce082 | -15.6092 | -57.452702 | 2024-09-30 01:11:19 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 153068e8-751a-3f8f-9a57-51ec30506d72 | -13.4831 | -48.565601 | 2024-09-30 01:11:20 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7f29b43b-42fc-3a24-9365-3fa8ce5133c2 | -13.4735 | -48.568199 | 2024-09-30 01:11:20 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 05ef2862-0def-3a3a-a494-0641d389126b | -15.5946 | -57.4328 | 2024-09-30 01:11:20 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 585c4baf-0a20-3edb-8e0d-85cf1108c4a8 | -15.5962 | -57.440102 | 2024-09-30 01:11:20 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8fefc9f3-6573-32cc-922a-6fd66a05a383 | -15.5978 | -57.447498 | 2024-09-30 01:11:20 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7b25db59-d751-358c-9d5a-1f85d9858c06 | -15.588 | -57.449699 | 2024-09-30 01:11:20 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 29ff75be-7da1-3454-a90b-80d590bfa051 | -13.1679 | -48.545898 | 2024-09-30 01:11:25 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef43c921-fb51-3922-bab0-d68cb64d651e | -14.9596 | -56.215 | 2024-09-30 01:11:26 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README10.md)
