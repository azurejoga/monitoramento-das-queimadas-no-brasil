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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ff8f3f9-21ef-371a-86ec-4ff11049164a | -11.798 | -57.243 | 2025-06-21 06:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| da2bb0ed-1b00-31e2-81c4-a8a44f2201c2 | -4.543 | -47.9934 | 2025-06-21 06:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| bc1eba69-063d-3ba8-80ff-4f0887577d21 | -11.7791 | -57.2445 | 2025-06-21 06:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| c1edd2f8-73bb-3d8f-9bf1-737cc914ff61 | -11.8853 | -54.6722 | 2025-06-21 06:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| c5bfb2c4-3644-3ee9-991d-77ce8e9ed0dd | -4.543 | -47.9934 | 2025-06-21 06:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 4629232b-8eb9-3805-aee6-338b62a0cf6f | -11.8853 | -54.6722 | 2025-06-21 06:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| c4d3c873-e06b-3c1b-a013-d5f332ea08ec | -4.5429 | -48.0151 | 2025-06-21 06:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 185.3 |
| 04ef981a-334a-39a5-a805-6ad6cf26086c | -4.5243 | -48.016 | 2025-06-21 06:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 6df9a544-1f80-31f3-8969-93ac61c459b5 | -11.7791 | -57.2445 | 2025-06-21 06:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 93b0673c-631d-3219-887e-11d62c08f7f3 | -11.798 | -57.243 | 2025-06-21 06:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 46906e62-af46-31bb-b3f1-3f96e1972068 | -10.23587 | -64.35983 | 2025-06-21 06:14:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 843a6fd0-0f7e-36d0-ac33-176f12afa461 | -10.23635 | -64.3561 | 2025-06-21 06:14:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b8d0d94-1e4a-3c23-bbc7-7c2fadbad83a | -9.39836 | -63.2677 | 2025-06-21 06:14:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b529e6da-b284-326f-b7ba-f991654ed398 | -9.01713 | -61.2302 | 2025-06-21 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 91c3031b-c45e-3afa-aa1b-3bddeb14bf42 | -9.39891 | -63.26336 | 2025-06-21 06:14:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b45570ed-c289-359d-a97a-d59be2bf2138 | -9.17308 | -61.40694 | 2025-06-21 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 70e3ad47-97d8-3724-82dd-65a48516b493 | -9.02823 | -61.22525 | 2025-06-21 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 22678d8c-b2cb-30b0-9aeb-e24e6fd055c0 | -9.02086 | -61.2303 | 2025-06-21 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fd58d9a7-abeb-35ba-8d84-a5b089b1c139 | -9.01641 | -61.23609 | 2025-06-21 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fceff03c-3012-379e-8914-47b732f83a33 | -4.5429 | -48.0151 | 2025-06-21 06:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 189.0 |
| 37cedba2-2646-3ae8-a409-ef363615376c | -11.7791 | -57.2445 | 2025-06-21 06:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ede24240-f077-3652-b5f3-9ff7e0a52156 | -11.8663 | -54.6739 | 2025-06-21 06:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| dd722357-b4df-361c-8e52-4abf22dc0ec7 | -4.5243 | -48.016 | 2025-06-21 06:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 75b86c22-f260-34a4-b582-ad7a49dfdcde | -11.798 | -57.243 | 2025-06-21 06:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 0bbb4d68-8627-3520-9954-0f00a3899080 | -4.543 | -47.9934 | 2025-06-21 06:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 34243d66-5387-3ed4-ab76-f744a9c0b2ee | -11.8853 | -54.6722 | 2025-06-21 06:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 33a5c113-3fcb-3c17-910b-3d794d9718d5 | -9.47754 | -57.83061 | 2025-06-21 06:29:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9059aace-cdfb-37ab-b4c3-201422b954b9 | -10.02712 | -54.31979 | 2025-06-21 06:29:00 | AQUA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 033e59c4-b293-34fe-8ac5-df0e6f2c6c23 | -9.25633 | -57.5304 | 2025-06-21 06:29:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 5c3f582f-fced-3a7e-a830-f300f683be50 | -9.1679 | -61.39623 | 2025-06-21 06:29:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d71f7700-3966-3f46-8c57-548afa522a11 | -4.5369 | -48.02099 | 2025-06-21 06:29:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 148.1 |
| ea303fc5-fd44-3cba-8010-239a03bba938 | -4.53556 | -47.99222 | 2025-06-21 06:29:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 176.0 |
| c2badcea-741b-39aa-89db-c81eb355e646 | -4.5415 | -47.98856 | 2025-06-21 06:29:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 6cf680cc-197b-3270-9fe6-2b6bd6198912 | -9.25766 | -57.52146 | 2025-06-21 06:29:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 6f107e62-e445-35b7-9c14-6ed6aa6d63ae | -3.9583 | -48.12989 | 2025-06-21 06:29:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 10cfb9f3-baa0-334d-99d2-7d37630c5b08 | -4.53122 | -48.02465 | 2025-06-21 06:29:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 234ae6f8-bd04-3d8e-a7a3-2974dc910de0 | -10.30135 | -57.13435 | 2025-06-21 06:29:00 | AQUA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1c534cc3-d339-376f-8e89-bd91031bc105 | -4.55141 | -47.99465 | 2025-06-21 06:29:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| d5d34394-709f-3096-9fae-b33e3151fb11 | -3.96974 | -48.13682 | 2025-06-21 06:29:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| ba9409f9-23a5-3c8d-ae7a-0a3c01b4e5f4 | -9.16607 | -61.40774 | 2025-06-21 06:29:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b9f6a9ca-4634-3b47-81a3-6831e8c31ea4 | -11.798 | -57.243 | 2025-06-21 06:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 019839b4-6715-376e-8c3c-1553b27e07dd | -10.437 | -47.0594 | 2025-06-21 06:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 4044c517-cd6a-370b-b044-e38b40aed87f | -11.8853 | -54.6722 | 2025-06-21 06:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ab2c6587-1de2-3ade-a391-4ed5c2c96a5b | -4.543 | -47.9934 | 2025-06-21 06:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 1b74488d-5cfa-362d-832e-52970c469be4 | -4.5429 | -48.0151 | 2025-06-21 06:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 173.7 |
| aff51c84-980a-3b5c-b1fa-129d65ee76df | -11.7791 | -57.2445 | 2025-06-21 06:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 34a5e185-153a-34b2-b2cc-d0a9ce6c9447 | -11.78221 | -57.23073 | 2025-06-21 06:31:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2a0d323e-a699-3e1b-bbab-97cd4e5ff297 | -11.87109 | -54.6693 | 2025-06-21 06:31:00 | AQUA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| ec2c0882-4e5d-3943-b365-970c5d40a5de | -11.86928 | -54.68231 | 2025-06-21 06:31:00 | AQUA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 9c1dd8ad-e68e-3035-a750-57f89de1dc37 | -10.88604 | -56.46652 | 2025-06-21 06:31:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 69a73704-0dd8-36d0-b0ea-350a58d12a93 | -11.53338 | -56.97224 | 2025-06-21 06:31:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 79f5c9cc-59aa-3e31-86cc-2a837b288b07 | -11.87863 | -54.66259 | 2025-06-21 06:31:00 | AQUA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 7f8e07d1-8979-3281-bfc3-bbd6f2073784 | -11.791 | -57.22902 | 2025-06-21 06:31:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| dfc44ac9-bbcb-3371-9a95-1df03aa65e8c | -11.8681 | -54.66114 | 2025-06-21 06:31:00 | AQUA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a9359157-8bf0-3b83-94c5-8968a3922d9b | -11.94614 | -58.74702 | 2025-06-21 06:31:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 755b9ca0-2736-354c-b24e-de668bf0034f | -11.8729 | -54.65627 | 2025-06-21 06:31:00 | AQUA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 0fe9d2fa-b7a9-3079-b5d7-d38461ff388a | -12.47161 | -54.42335 | 2025-06-21 06:31:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 05958439-d8ae-3dd7-9b8b-0cb63d34da29 | -11.8769 | -54.67563 | 2025-06-21 06:31:00 | AQUA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 529a0deb-ff76-3fd5-be5e-9269d44eb046 | -11.78829 | -57.24788 | 2025-06-21 06:31:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| cfba9108-22a8-3c6f-b276-cd75b7f270b8 | -11.94479 | -58.75595 | 2025-06-21 06:31:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 11524561-fc18-3336-b36f-b93e2232652d | -12.51286 | -58.35017 | 2025-06-21 06:31:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5dd712ea-341b-3f5d-9b34-ed04d20d74fe | -11.9536 | -58.7573 | 2025-06-21 06:31:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| bc6c14be-ba6b-3f20-addf-d4b6d845991b | -11.78083 | -57.24015 | 2025-06-21 06:31:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 54c40761-77e8-3196-9cd4-87480400c2e8 | -11.86638 | -54.67421 | 2025-06-21 06:31:00 | AQUA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 4e9265d6-227f-326d-9086-2903b9864cff | -10.88744 | -56.45655 | 2025-06-21 06:31:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 133b6f1b-64a6-3463-80c1-e75059b9c0a4 | -11.78965 | -57.23846 | 2025-06-21 06:31:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| d2202531-bc77-3847-8523-6a655679ae9c | -11.8853 | -54.6722 | 2025-06-21 06:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b42a5bc7-7a9a-3156-94e2-b4e2491d1c31 | -11.7791 | -57.2445 | 2025-06-21 06:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 7e5de390-a507-394c-969b-e49680fb27c8 | -4.543 | -47.9934 | 2025-06-21 06:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 09f5b012-9a0f-3cd9-9d74-53fbaded7ee7 | -4.5429 | -48.0151 | 2025-06-21 06:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 179.9 |
| b53012cb-edac-3f95-86ba-f26c037cfb8b | -11.798 | -57.243 | 2025-06-21 06:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| cf529e1f-0d08-3006-8338-9d4cf624ef15 | -4.5429 | -48.0151 | 2025-06-21 06:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 157.0 |
| 6a0b4d0c-14f5-39f1-9779-b2ddb25a74e3 | -11.798 | -57.243 | 2025-06-21 06:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 72839504-56d7-3fb2-ad02-b0f3aa7dec18 | -11.7791 | -57.2445 | 2025-06-21 06:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 5b166146-35b0-3724-a2f6-7915dbe073d2 | -4.543 | -47.9934 | 2025-06-21 06:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 6c495303-7749-31a6-80ad-3667f0f79576 | -11.8853 | -54.6722 | 2025-06-21 06:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 85bb8daf-b604-324a-8760-eb606eee32a7 | -4.543 | -47.9934 | 2025-06-21 07:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 2889e0b2-6b83-3220-909b-ba0e65ef0c2c | -11.798 | -57.243 | 2025-06-21 07:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| fa80ba26-cff8-3f14-86e6-9d94ea5866f7 | -11.8663 | -54.6739 | 2025-06-21 07:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| b2db9c04-b9a2-373b-b7b0-84be5e32ee5d | -4.5429 | -48.0151 | 2025-06-21 07:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 146.1 |
| c8938e8c-ef1b-3399-b147-9062f7bf3577 | -4.5243 | -48.016 | 2025-06-21 07:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 258a2dc1-2690-3810-b441-22f3d74a0342 | -4.543 | -47.9934 | 2025-06-21 07:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| b6274766-3d9b-35f6-a911-5070dbd0bd9c | -4.5429 | -48.0151 | 2025-06-21 07:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 431a425a-92fb-3ddc-a294-b351198c4668 | -4.5243 | -48.016 | 2025-06-21 07:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| f010145e-94ba-350e-8688-fe16498e90c7 | -11.8663 | -54.6739 | 2025-06-21 07:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 6881301e-a2d1-30fa-98d0-294ce8a1bb99 | -11.798 | -57.243 | 2025-06-21 07:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 65b94d81-c065-3a0c-ab74-54a16433a226 | -4.5243 | -48.016 | 2025-06-21 07:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 6d452ec1-f3de-355c-ae55-03036ca99e32 | -4.5429 | -48.0151 | 2025-06-21 07:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| a3c9f731-b170-31b8-a56d-d8419bf97ff7 | -4.543 | -47.9934 | 2025-06-21 07:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c90503e1-d2bb-31b4-aa76-37f40310f7dc | -11.798 | -57.243 | 2025-06-21 07:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| b23ba23c-f724-3f16-88e7-5b164d97cd2b | -4.5429 | -48.0151 | 2025-06-21 07:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 133.5 |
| afe4e8ae-fa29-359b-8dd2-9afe561b6bf7 | -4.543 | -47.9934 | 2025-06-21 07:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 670d3989-1571-365d-9a80-f9d0b1721e03 | -11.798 | -57.243 | 2025-06-21 07:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| c1bc06fb-f7a4-3163-bd36-4d9dca72f4a0 | -11.7791 | -57.2445 | 2025-06-21 07:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 70e7d2cf-9db1-3db4-b0fe-b675deb18a90 | -11.7791 | -57.2445 | 2025-06-21 07:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 2d9b0fec-569a-35e5-8f04-2d1c9edc8ff7 | -4.5243 | -48.016 | 2025-06-21 07:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| de046f08-75bf-38b8-bd38-e8767f8fff5a | -4.5429 | -48.0151 | 2025-06-21 07:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| af10de4d-9f7e-3a7b-bd81-7811af352285 | -11.798 | -57.243 | 2025-06-21 07:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c5bfb13d-f8dd-3908-87c9-dcbb1c0e8855 | -11.798 | -57.243 | 2025-06-21 07:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 284095d5-c868-358b-8f48-d413efbe646b | -4.5429 | -48.0151 | 2025-06-21 07:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |


[Clique aqui para ver as próximas entradas](README29.md)
