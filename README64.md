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
| c91bbb81-0637-322f-b6d0-297cd0c74824 | -9.13028 | -51.53149 | 2024-09-26 04:06:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b66e3154-152e-354a-b891-80c769636b16 | -9.12962 | -51.53498 | 2024-09-26 04:06:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c94e62d6-4761-3b0e-b87e-d75bacdffa5c | -9.1848 | -50.34761 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d583e039-5dad-3e55-81f7-7337e92f55c4 | -9.1798 | -50.34665 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a4a414b-93a3-3079-b137-62a3ffbc62d4 | -8.04115 | -50.43113 | 2024-09-26 04:06:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e40cb9c2-d00f-3564-b043-d9158f281c6e | -8.03656 | -50.42719 | 2024-09-26 04:06:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07715ad0-dca7-3df8-8e52-03432f411f65 | -8.03346 | -50.44427 | 2024-09-26 04:06:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cea74b5-e1da-347a-8060-b34a330cb6e3 | -8.03291 | -50.44733 | 2024-09-26 04:06:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aeb6ed77-f2db-30b3-a66b-416a7b5fd417 | -8.02779 | -50.44627 | 2024-09-26 04:06:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e85e9579-da20-3e9d-a02e-d0120b9f0dc7 | -9.34501 | -51.07514 | 2024-09-26 04:06:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ddece7ce-5e0f-346c-9473-4000f375e86f | -9.34439 | -51.07851 | 2024-09-26 04:06:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3f266e8e-ecdf-3307-bf7d-70b97ee5f86a | -9.33979 | -51.07406 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 60c4ee7f-8a70-38bf-a96a-9ccf6f060509 | -9.33919 | -51.07732 | 2024-09-26 04:06:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 94c65e22-a730-3bcc-8130-9b65cec44fe2 | -9.33858 | -51.08062 | 2024-09-26 04:06:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 02d0cb59-d8c5-3c6f-af31-3032b440f0e9 | -9.33394 | -51.07635 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a314a8d-f7fc-3026-8aa5-7f410fb4acf8 | -9.33334 | -51.07962 | 2024-09-26 04:06:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18e1eefa-79a1-3789-a638-6f5b57cc7eaa | -9.3327 | -51.08306 | 2024-09-26 04:06:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5572586-8f8e-3f59-bf10-a2681d3c51c2 | -9.32999 | -50.74207 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a24d74b8-ecb3-399c-a534-8884f57f73ba | -9.32951 | -50.74471 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2db5dd1c-5b53-3dfa-a0f2-3e49b65b7587 | -9.32896 | -50.74775 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9837164d-c349-3a5b-b2e6-5b0121fca2aa | -9.32635 | -50.7329 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3353a8a-f8b5-34f4-afd1-36b1be619195 | -9.32587 | -50.73558 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ccd344f3-3add-39bc-b21d-5e7174694e73 | -9.32274 | -50.72366 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97f94acd-ee30-3a14-88ae-a4633505c069 | -9.32224 | -50.72636 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bcb19cd-1c6d-3980-87a1-75d9ef4962c2 | -9.31818 | -50.71956 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60dbca21-b730-371b-9f42-399fb0d98e8c | -9.31722 | -50.72486 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03b8761a-6f00-36b2-848e-22a570950f14 | -9.30437 | -50.7662 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13948d31-7165-3bac-8f76-7e85ee12ffb7 | -9.30367 | -50.77009 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5ba951d-0267-3609-82b9-e247d801662b | -9.29988 | -50.7617 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a5a03d5-1aa7-3bfd-be66-a08bd79ccfbe | -8.93155 | -50.70174 | 2024-09-26 04:06:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4db52b80-ff96-3f20-8cf2-79d853a8cd10 | -8.6926 | -51.00745 | 2024-09-26 04:06:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d5443e9-64ff-3b9d-b9a6-0c49df1b5a07 | -8.69207 | -51.01036 | 2024-09-26 04:06:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b685dc38-98af-349d-a464-5ec2510ef936 | -8.68715 | -51.00743 | 2024-09-26 04:06:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6439ad03-8bbb-3ffd-bd17-596a15d797b4 | -8.68664 | -51.01018 | 2024-09-26 04:06:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3d17ee6-59f3-343e-aa20-a0660c998722 | -9.44769 | -51.52713 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75e1573e-56a0-363f-aa76-11c48fbfa78c | -9.44617 | -51.51554 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cdd6987-eb14-3f5e-9367-329362a4d221 | -9.44551 | -51.51907 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f31789e5-6fbc-31b6-a24c-ee8a10279c72 | -9.44485 | -51.52259 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ada4be62-9e35-35d3-a2db-dca648f5a316 | -9.44422 | -51.51541 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 439eaa93-c857-362e-bff6-73f9316ca4e5 | -9.4442 | -51.52602 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac333053-544f-3dbb-9e86-adebb55795ad | -9.44358 | -51.51899 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94d3209c-2f33-386e-bbac-aa456e18b80c | -9.44294 | -51.52252 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06ecf2e5-73ac-36bd-b611-42e31632a432 | -9.44277 | -51.50399 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3ed0d4d-faa7-3068-b2fd-b955ae05b40a | -9.44152 | -51.51064 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43a40d0c-56ea-3490-918b-f353b9ac055b | -9.44087 | -51.51409 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9b84f99-56e7-3353-8ba7-b24c52420293 | -9.43956 | -51.5104 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35e0cbd5-aec1-3afb-a904-966d9d53cbe3 | -9.43681 | -51.50607 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca7e8e61-a1f7-34e0-b6de-ac8a697dfa5a | -9.43668 | -51.47729 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 479db4bd-aa54-3cdb-ba9d-8737000788cc | -9.4362 | -51.50931 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df095343-4113-38bd-bc47-a1d10a99905c | -9.43604 | -51.48069 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ca18b8c-cb03-3e42-a033-6418086ad58c | -9.43556 | -51.51267 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb577c1d-940a-3729-89af-014bc81f6973 | -9.43481 | -51.50588 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97bc7557-e920-3c96-a50a-be58ede5457d | -9.43448 | -51.47706 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 124b75b8-e4c1-3964-92b6-a29f45bdd709 | -9.43421 | -51.50917 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c30a2b67-d29b-32e9-bc1e-da216a51efa3 | -9.43386 | -51.48044 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41d5601c-2f68-36e3-8a8c-b5bad4a61f9c | -9.43359 | -51.51259 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 214ebae2-6b92-3e6d-b849-c7acdd6420c0 | -9.43324 | -51.48384 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f8a3479-4fbf-392a-b742-e0ceb269e084 | -9.43262 | -51.48727 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dce007e2-f62c-34e1-8da2-6209ce3ba587 | -9.43147 | -51.50484 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddce090a-e9b4-3d1c-b432-34facd0cf4d7 | -9.43083 | -51.50817 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 901d75d2-d50e-347c-93fd-b5c0b57e6d57 | -9.4285 | -51.47932 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f21fcd05-1451-3091-9301-1269a31ab3de | -9.42661 | -51.48972 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ddd3c60-ebdd-3a81-b0df-de41433ba94b | -9.40842 | -51.46748 | 2024-09-26 04:06:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37b6cf40-4bed-39fc-9899-ae56929b4500 | -9.40782 | -51.47079 | 2024-09-26 04:06:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a5208ee-c6e6-3561-b4d9-ef142e4d1d19 | -9.37882 | -51.84493 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 527e17bf-f99c-303a-b061-cf87b3a9b164 | -9.37845 | -51.844 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b05cfe83-8f21-318d-95ff-2e8b97d6aad0 | -9.37335 | -51.84368 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cae8f722-af4c-3818-becf-ebfa9dff093f | -9.37299 | -51.8427 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcb31aec-bc69-361e-997b-b97faea57377 | -10.86387 | -51.16758 | 2024-09-26 04:06:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aca91c66-2804-34f2-b506-5a5ac069d423 | -10.86329 | -51.1707 | 2024-09-26 04:06:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5ea9ce7-c019-3da9-9f89-cee2203ab6c0 | -10.85874 | -51.16656 | 2024-09-26 04:06:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc97164c-22dc-30f1-959a-df27a4ce1f81 | -10.85361 | -51.16553 | 2024-09-26 04:06:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7fb3e95-b2e0-39a3-800b-e275cd04535e | -10.85304 | -51.16862 | 2024-09-26 04:06:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9371b17d-4da8-3fb4-9cae-98e5f5b7f909 | -10.85246 | -51.17172 | 2024-09-26 04:06:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9db1573a-6ffe-3d06-965c-9c3770506821 | -10.84733 | -51.17069 | 2024-09-26 04:06:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0787ab48-3591-3528-a969-ad07f1530176 | -10.6117 | -51.13024 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e40eec2-0dc2-3ec4-b3f1-1c5ac85de43a | -10.60772 | -51.12304 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9047b64-445b-32c4-b43d-815737d740cb | -10.60655 | -51.12928 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2cecbe0-a1b3-34da-85e0-3b8b3d813b10 | -10.60317 | -51.11893 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 922a3b1b-fe20-3a41-894f-22c8d544f5d8 | -10.53853 | -51.11415 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f5c4690-ee35-398e-a60d-c7a57efd352b | -10.53798 | -51.11712 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c11c30c2-9890-36b7-90bf-d4607ad7fae2 | -10.53743 | -51.12009 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c86fe14-b61b-3d8d-bb1b-8119d1ff9f98 | -10.51963 | -51.15826 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2aac6181-7496-3b4f-9d57-e5a8c4e3a7db | -10.51911 | -51.16105 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64ad7c78-7c3f-3753-bb81-0fc2c2249146 | -10.51363 | -51.16171 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2966c788-5b65-3d67-84ff-33a2e27ce6c5 | -10.49643 | -50.84149 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 598fa592-c1ea-3e5a-94f0-d505f310c94e | -10.49607 | -50.7584 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18e5ae46-fbf5-36fc-bae4-558c777305a2 | -10.49553 | -50.76131 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9cacb3a-b05e-3269-bb22-181edf7e4373 | -10.49137 | -50.84053 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0bb0911-81bc-3ba5-b439-863fa84710c2 | -10.49104 | -50.75742 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8074b9f3-2e57-3782-b7ea-c08be1df5eb6 | -10.49051 | -50.76032 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30ded2be-e47f-3c64-a62e-276d167267cd | -10.46839 | -50.76712 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ddf2a1f-62c5-31fe-b48e-cde9bb114474 | -10.46783 | -50.77013 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aadd68d2-4294-3b74-8f10-fdeef341e6ca | -10.46496 | -51.24908 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56def77f-df08-3812-bc81-bac2af17f34f | -10.46458 | -51.24796 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cf30af5-82c9-32ff-a76d-17b4bb6a671e | -10.46155 | -50.77585 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0378ccb0-6ffa-3f74-a98a-ed26bb5a6cd1 | -10.46098 | -50.77892 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9be557e-8f59-324f-80d5-a8c52042c4e1 | -10.46041 | -50.78196 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bac3774-1b68-3fe0-9a3c-0dded2d894a0 | -10.45984 | -50.78499 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b30471e5-c59b-3e5c-9ff6-7918d07bbfeb | -11.21766 | -51.15414 | 2024-09-26 04:06:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |


[Clique aqui para ver as próximas entradas](README65.md)
