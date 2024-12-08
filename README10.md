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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c637c26b-25bc-33c0-acc5-8cf3f889c026 | -10.37437 | -49.92881 | 2024-12-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc7771f5-e452-31ef-9140-caa719835d83 | -9.20346 | -48.02673 | 2024-12-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3977ebc9-4c94-3293-aa97-8a9567d45875 | -12.41404 | -49.69088 | 2024-12-08 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9605a7ee-1779-3fdf-af94-1263576ac5c6 | -12.77846 | -54.22703 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1970501d-7567-3ad0-a904-2cc2f7ec93e8 | -13.89855 | -54.62956 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d567c43c-e704-39ba-b1c5-4f5672340692 | -11.82475 | -57.82869 | 2024-12-08 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3e28c60-bf64-381a-9c7e-834658165a02 | -7.97709 | -50.69696 | 2024-12-08 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 438c2435-bdb4-367c-98ae-a300c4dfbd86 | -12.85134 | -51.93095 | 2024-12-08 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f34b0d1f-4a8c-375d-bc96-f6fc63c09590 | -12.78361 | -54.21896 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9a2f9e5-c151-35b4-85a4-16b8980f64a0 | -12.86357 | -51.94043 | 2024-12-08 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c0969eb3-eb0f-3096-8f7e-8455026f0a15 | -12.40846 | -49.68264 | 2024-12-08 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5163ad42-d21c-3229-b0b4-2476177869c0 | -12.78576 | -54.22831 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8e8c355-86ca-3fbe-a007-6ba599c566fd | -12.47935 | -54.50972 | 2024-12-08 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3603e448-7b1b-38d7-8f76-794272273a73 | -12.12556 | -54.291 | 2024-12-08 04:38:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3fc55b4-071b-3991-9d15-be47e0822c4c | -13.66043 | -52.10358 | 2024-12-08 04:38:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea650697-dfa9-3d11-87a1-1bb8876de2df | -12.85687 | -51.9393 | 2024-12-08 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 177c4c7c-6e59-3a7c-9451-05442351bcc0 | -13.62549 | -44.51905 | 2024-12-08 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df0de59a-fe68-332c-aa2b-bd98d41a97c1 | -12.85132 | -58.22444 | 2024-12-08 04:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| df0a4956-30c1-39ce-b2cb-ecc171eaa53b | -12.78286 | -54.22332 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7db79526-9cab-3bc1-9f24-844fa220615b | -12.78047 | -54.21612 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b23b064-3693-3193-aed6-54090e1e67f8 | -13.89195 | -54.63041 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 49993211-44d8-3ef3-ab7a-066ab100b294 | -15.57984 | -46.56116 | 2024-12-08 04:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c75c7afe-943d-3a37-83c0-c0f690dca5e4 | -12.85017 | -51.93817 | 2024-12-08 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a54dfd01-33d0-350f-91cd-148a1978e165 | -11.2081 | -53.82035 | 2024-12-08 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d76ce004-c3a1-340e-9318-7b686112a58e | -13.87986 | -47.38963 | 2024-12-08 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d658658-9daa-39a8-aaa6-128e01fcf6c1 | -14.77124 | -50.53201 | 2024-12-08 04:38:00 | NOAA-20 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e41579a-1fd3-377b-8843-157da9457df4 | -9.25787 | -48.67938 | 2024-12-08 04:38:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b8ca7339-debd-3147-98b4-51e8706169eb | -12.32082 | -51.51511 | 2024-12-08 04:38:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33977b1b-bfa4-3cd6-80a6-83776aae449d | -15.56923 | -47.85852 | 2024-12-08 04:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0de5e531-984f-3ef5-b128-87994a73f900 | -9.25842 | -48.67578 | 2024-12-08 04:38:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bb1e465d-9cb6-3c9e-a65b-4f949c85efcf | -12.21584 | -54.22929 | 2024-12-08 04:38:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dfd2d47-43a2-3618-b3a6-017109418ae3 | -13.17125 | -53.24479 | 2024-12-08 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 068d705f-dd41-3141-abcc-7c318c0a6e33 | -12.85034 | -58.22964 | 2024-12-08 04:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 777de279-3339-347d-b83d-b9ef00e2ff73 | -13.88353 | -47.39029 | 2024-12-08 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 559803a6-19ac-37c3-9209-4ca7471391b6 | -12.85628 | -51.94292 | 2024-12-08 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50867c3f-7a4c-3476-a943-84ee16aa7ccf | -12.41125 | -49.68676 | 2024-12-08 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ca29003-11f4-3811-bc5a-07e0bf52f389 | -12.50812 | -57.83776 | 2024-12-08 04:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 911a8537-539e-326e-a599-71033cd2efdd | -9.22126 | -50.69366 | 2024-12-08 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 30a78a34-fe9b-3036-9023-802729965c1e | -11.72225 | -57.43726 | 2024-12-08 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64c5ea83-e1ec-39d1-8908-e5cc31f543ca | -13.06807 | -52.04176 | 2024-12-08 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dea1a54-80e9-3891-ad75-a03377fe7e47 | -13.08317 | -48.11655 | 2024-12-08 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48caf4b5-1593-38ff-a369-0abeae8f7769 | -12.78211 | -54.22767 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 089bd2f7-a222-36af-8251-84f61bf4af1d | -12.54059 | -48.32241 | 2024-12-08 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6902bf2a-bc0a-3541-9443-eadfe48f6a78 | -12.53658 | -57.73458 | 2024-12-08 04:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5a9c94a8-0064-31e3-a8c5-1e9562112813 | -12.77828 | -54.22918 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3ce4bc3b-2415-3f3b-8d04-e50ca9a13da8 | -12.79092 | -54.22022 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd1d5ceb-ee40-39f1-a63f-1ff589ae6d71 | -12.86415 | -51.93681 | 2024-12-08 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cf3ae84f-8100-3028-9dc0-67145bb15b41 | -7.97652 | -50.70051 | 2024-12-08 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1947dff5-7215-352d-93ff-74cbac040d15 | -10.52855 | -56.24472 | 2024-12-08 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8da2e673-35bb-3966-a228-50c704e5cbad | -11.20436 | -53.82151 | 2024-12-08 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ca31b02-8724-3480-8447-5ee4c977145f | -12.53204 | -57.73364 | 2024-12-08 04:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c75fc67a-c3ed-3366-b856-6c440ae8eb2d | -15.56988 | -47.85388 | 2024-12-08 04:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2caa45be-0873-360e-b6d9-d4d353aa58ea | -12.69069 | -46.76285 | 2024-12-08 04:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9daa705e-f502-3d5b-83bf-ed86f3693093 | -13.88114 | -50.09533 | 2024-12-08 04:38:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ee494cf-71c8-39da-b454-6c2d17d3bc23 | -13.89929 | -54.63178 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 47b368f7-1545-32ea-92a3-703ab7106dc4 | -11.7214 | -57.44194 | 2024-12-08 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8c93a52-6387-3e24-91c8-d738b4f9543b | -12.27946 | -49.50404 | 2024-12-08 04:38:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28bf7840-2149-3736-a069-6849859dfa62 | -12.77996 | -54.21834 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a819ac10-7a00-3a03-ad94-a8bfeb402adc | -15.07722 | -48.94591 | 2024-12-08 04:38:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7d0e42c-160b-3c82-9bd8-fbfc45899c58 | -10.00631 | -48.06201 | 2024-12-08 04:38:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e9f5436-79c2-30c4-9fa7-ad1b6ebf3aca | -12.69445 | -46.76341 | 2024-12-08 04:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53f5d659-8e79-3379-8d37-d10d2825faf2 | -10.98487 | -55.94923 | 2024-12-08 04:38:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6aa6f44-fa3a-336f-acc8-e95fdb6d13d0 | -10.41547 | -51.891 | 2024-12-08 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd69cbe3-c461-3ef9-890b-1d56a4237935 | -9.09916 | -49.22503 | 2024-12-08 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba4ab9f9-6583-3a99-952b-6d492e61e34f | -11.74672 | -54.72748 | 2024-12-08 04:38:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de3c8b7b-47ba-3c07-bbbf-676fd3609beb | -15.97776 | -52.33353 | 2024-12-08 04:40:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 355bcd66-c2d7-33ec-8711-4442447ab842 | -15.0917 | -59.64918 | 2024-12-08 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2434056f-9be5-31a6-91db-fa157443b1dc | -15.36418 | -53.12783 | 2024-12-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4256905-7f76-32cd-9402-95f7bf6c8424 | -15.08529 | -59.62964 | 2024-12-08 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1be16dd6-6be5-3a80-a97f-8922399c57cc | -17.67528 | -42.74565 | 2024-12-08 04:40:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 307da919-2473-3792-8da5-ecfe07f74011 | -19.02065 | -57.62178 | 2024-12-08 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 95506152-845a-3a6b-a959-29e47424babc | -18.0435 | -52.22418 | 2024-12-08 04:40:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db185d85-e325-33b6-ad63-5e3e8014a5f8 | -16.67944 | -43.88637 | 2024-12-08 04:40:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c4286d9-e40d-3de2-86c7-84c4f60a7709 | -15.083 | -59.64125 | 2024-12-08 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d518f3ca-80eb-36fc-9ac4-1cd2b2d0b7b7 | -14.45069 | -56.82436 | 2024-12-08 04:40:00 | NOAA-20 | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35b617cd-5697-3712-8502-82a527569974 | -15.08906 | -59.63651 | 2024-12-08 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bb9b5726-b147-32df-a439-b3b353b0c689 | -15.15717 | -56.48106 | 2024-12-08 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e0af66d-bc0b-3fbb-a638-d841017a9f54 | -15.09131 | -59.62504 | 2024-12-08 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d060961b-c683-3ae8-b435-f668a7e10c11 | -16.01187 | -53.68888 | 2024-12-08 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc89e320-5f0b-3a7c-b196-f6e73bcc3ab7 | -18.95545 | -53.69357 | 2024-12-08 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f100e407-95e3-33c6-b024-0c7acda5c02b | -15.84036 | -54.11153 | 2024-12-08 04:40:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2bfcf4e-779f-3411-b9dc-f725fd817842 | -15.37036 | -53.13278 | 2024-12-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df4e724b-cd59-3402-9ddc-64457a005c25 | -15.25902 | -53.57139 | 2024-12-08 04:40:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 73ea9e60-761d-3498-bcd7-dc48cd65b9cd | -17.47783 | -51.82845 | 2024-12-08 04:40:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a27ca66-80a1-3b33-b99d-57aa3c7dded5 | -15.84315 | -54.11289 | 2024-12-08 04:40:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9222a64e-371e-3be0-a25a-b6058f3237be | -18.95208 | -53.69296 | 2024-12-08 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36bd5646-e750-3eb9-907f-420ce529e34d | -15.26118 | -53.5798 | 2024-12-08 04:40:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11e716bd-041d-38e8-b899-dc33193a7560 | -15.6629 | -49.38317 | 2024-12-08 04:40:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27467356-f088-3a0b-9359-764eec0d9f76 | -15.09056 | -59.65498 | 2024-12-08 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fffe23b-7323-3179-9907-3cfe0b5305de | -15.0902 | -59.63071 | 2024-12-08 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 10a54869-5ad7-3fae-af5d-05cd14b0d825 | -15.36695 | -53.13219 | 2024-12-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57c8f4ac-1be2-3d7c-9f01-cdf66cb57b60 | -15.86776 | -53.26468 | 2024-12-08 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32ef3ee8-46e3-3eb9-86f4-7422d90b904d | -15.97718 | -52.33715 | 2024-12-08 04:40:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80ba6b7b-558c-31ee-9df1-d513d86b6cb5 | -18.95146 | -53.69674 | 2024-12-08 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afb1949b-f555-3574-a531-0bf448db2317 | -15.16247 | -56.47468 | 2024-12-08 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ab30b60-4dc1-30c1-ad1f-dc718006e5c4 | -15.36078 | -53.12724 | 2024-12-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 883abb5e-5b68-3aa3-8264-a628d831c0e6 | -15.07581 | -59.65174 | 2024-12-08 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f821b676-4716-369a-b4b5-19d2c4300a5b | -17.74058 | -54.22289 | 2024-12-08 04:40:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d465b40-bb90-351b-ad18-cee69eb83066 | -19.14766 | -52.64949 | 2024-12-08 04:40:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7be93432-692f-3b07-821e-5f18a645eb5e | -17.67564 | -42.74232 | 2024-12-08 04:40:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README11.md)
