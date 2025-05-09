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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a03dc10-51cb-3485-b5d4-b5919fdc7d27 | -6.69434 | -42.13533 | 2025-05-09 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9f2f8f88-137f-3812-a082-6f6c435b17c5 | -7.08293 | -44.37404 | 2025-05-09 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14e5043a-2f54-3b54-9a9a-40597fed1d58 | -5.61981 | -39.49174 | 2025-05-09 03:47:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 48083239-a03c-3ea4-838e-0083f5d80ece | -6.96646 | -42.78616 | 2025-05-09 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c541d186-ddc9-319e-b6d1-cc35a756ce29 | -6.97073 | -42.7774 | 2025-05-09 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fc1d6ef2-33f1-31f0-baf5-31ed29ac35e0 | -13.03293 | -45.07858 | 2025-05-09 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b20c2bc8-69f0-378c-a860-f078b4092e77 | -11.56436 | -47.87149 | 2025-05-09 03:47:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 362ce2fa-8b4f-3c94-8834-55c6657ac158 | -10.67187 | -44.3786 | 2025-05-09 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2a4cb424-3d91-3d17-bc55-bc830e39f54e | -12.32163 | -44.51087 | 2025-05-09 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07672d30-1936-346a-865c-4a322c4b55df | -11.77355 | -48.20246 | 2025-05-09 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8de3636-85d9-377b-bdcb-ada69f16681c | -10.96832 | -44.43859 | 2025-05-09 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6a8489b-1066-34b8-a33c-174ba88ddf3c | -12.31724 | -44.51011 | 2025-05-09 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d0cd041-9460-3127-aef0-3a0f1c36e54d | -13.02844 | -45.07771 | 2025-05-09 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 810c8b8b-dd6d-3c16-a401-d40a6571cdb7 | -6.61324 | -48.01465 | 2025-05-09 03:47:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb8913c5-0b57-3bf7-9d50-f2b6e32a3e93 | -7.62553 | -46.47826 | 2025-05-09 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e79dc0e-2c92-392b-a6df-c4dc9b31f0ef | -10.97278 | -44.43943 | 2025-05-09 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 60ae2e79-fd01-3917-83d4-b4f0d88029fc | -14.20848 | -45.46222 | 2025-05-09 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0c0416a9-0012-3afc-a9f5-bc237c029d13 | -8.0759 | -43.11985 | 2025-05-09 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 7084e9a0-a18a-3900-938c-400cd260f694 | -12.32206 | -44.50949 | 2025-05-09 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ca59050-59f8-3c1c-a6f4-094cf6726f67 | -5.56589 | -43.48303 | 2025-05-09 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83990a57-1501-31f5-a3f1-7f8ebbfd1549 | -7.07084 | -44.38722 | 2025-05-09 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a968495f-8697-3e02-8270-1492abdf5a2a | -6.69371 | -42.13904 | 2025-05-09 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b6a63529-e97a-38b5-8ac4-3558f8135560 | -5.16335 | -45.10145 | 2025-05-09 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 09eb5fe5-1b68-346a-b2d4-7fb8d8ffd78a | -5.77218 | -43.48566 | 2025-05-09 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6cbd48d-9d55-35fb-8b2a-74818b405e24 | -5.79222 | -43.61626 | 2025-05-09 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2676aa8-4eaa-3ec9-b92a-050f42bc5ab0 | -7.21335 | -43.11858 | 2025-05-09 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| bffafa52-e9df-3273-99b5-2d346475b098 | -7.21406 | -43.11438 | 2025-05-09 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 678d84d2-40c6-3dfc-a549-493973683ed5 | -10.96913 | -44.4341 | 2025-05-09 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ddd5d03-4d91-3b06-ae93-a48d327a8e9e | -11.48015 | -43.81046 | 2025-05-09 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52ac690c-9e30-338c-bb04-dbaa4fb22481 | -11.56345 | -47.6142 | 2025-05-09 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da09bd74-a18a-39f7-a1b7-70d0a78d9898 | -14.20311 | -45.46603 | 2025-05-09 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8cec021c-d580-3543-8884-83a1110092df | -8.0752 | -43.12395 | 2025-05-09 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 14e9c626-083c-34a1-ba79-0d8fde02b39f | -10.67108 | -44.38302 | 2025-05-09 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 1c23b572-b666-3708-a7e7-21d830172c77 | -13.45585 | -47.62397 | 2025-05-09 03:47:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 922d78f0-9eb6-30ab-abe7-f5034282bab5 | -12.5884 | -48.33857 | 2025-05-09 03:47:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03849ca4-f11c-3f3f-82a0-ca94667a8969 | -11.47665 | -43.80554 | 2025-05-09 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de793cef-5299-32ba-a871-364a9d521a06 | -6.96933 | -42.78539 | 2025-05-09 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cd78a8d9-ceeb-39d4-a37b-2b7b887be4e0 | -7.62179 | -46.4754 | 2025-05-09 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78426a36-9eb8-3c97-809b-da8abddb8b21 | -12.31767 | -44.50872 | 2025-05-09 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33182516-ed95-3d5c-a646-3d96a5776ed2 | -14.19946 | -45.46044 | 2025-05-09 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 613bd148-c565-3021-a16d-c2d7363d641e | -5.16481 | -45.10305 | 2025-05-09 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b2fdf7ae-e555-3461-889f-89e68828d706 | -6.79281 | -38.74444 | 2025-05-09 03:47:00 | NOAA-20 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4a70bb48-d973-3806-a48d-468ba9b5fc8a | -10.97198 | -44.44392 | 2025-05-09 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6e0e21da-fce4-3d11-8fdf-f5416392f6af | -7.62114 | -46.47889 | 2025-05-09 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21c3a0c7-073b-344f-87b9-0ba8e70b075e | -10.99266 | -44.4573 | 2025-05-09 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74b9597c-9eb1-3c81-9853-b0345721f249 | -13.61335 | -43.97226 | 2025-05-09 03:47:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 722b91fc-0c5b-3097-8f76-5a6cafc63c76 | -6.97141 | -42.78289 | 2025-05-09 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c4d15ea4-32c4-32b1-929e-851b659226ef | -14.20912 | -45.46523 | 2025-05-09 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e61aee4-946f-3089-a235-4580d8c27891 | -14.63646 | -45.12518 | 2025-05-09 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a9ccff7-934d-395c-92d1-2d78b1dd3f93 | -14.21726 | -45.47169 | 2025-05-09 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6576b39f-416b-3d11-b123-82eaa8810df4 | -14.20551 | -45.45966 | 2025-05-09 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4feb3fd3-6dd5-3e0b-86bd-9ef747aa0261 | -15.25143 | -47.46811 | 2025-05-09 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14e27c52-374f-360c-a389-1af31620c232 | -16.68 | -43.88314 | 2025-05-09 03:49:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8405e28a-5408-3dcd-9391-41022cef52c7 | -18.26406 | -53.00442 | 2025-05-09 03:49:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df8cc59a-98bc-37eb-8ba5-92f0ade8c420 | -14.2001 | -45.46347 | 2025-05-09 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02f99014-00c3-3f95-926c-d20c30a37423 | -21.62472 | -43.4675 | 2025-05-09 03:49:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 71cea0f5-30ff-3db4-b8f9-236cf7aafbde | -20.06185 | -49.36378 | 2025-05-09 03:49:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 54db51c2-bc70-3fa5-9f68-8550e2bde7e0 | -9.61624 | -37.04343 | 2025-05-09 03:49:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f49dc87c-7466-3809-a7b2-bc62e714d8cc | -15.25648 | -47.46909 | 2025-05-09 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1c815b8e-82fd-399d-99ca-9727d2de1b6b | -20.06187 | -49.36377 | 2025-05-09 03:49:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 998ac14c-066e-3561-96be-22c384be2c88 | -20.06254 | -49.36049 | 2025-05-09 03:49:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 79fe25bf-b49e-36ad-a734-5a914914f0ec | -20.05597 | -49.36587 | 2025-05-09 03:49:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c8cd4b27-9dcb-3721-9d68-6aee0fe8895b | -14.21815 | -45.46701 | 2025-05-09 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c2de337-95f2-378e-8b49-b5420b5e97a7 | -14.22628 | -45.47347 | 2025-05-09 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2af95077-0471-3084-8878-11313e982e99 | -21.3561 | -48.73335 | 2025-05-09 03:49:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f991f6d0-ab9f-3c13-a44e-da213d046d1d | -18.4118 | -42.66035 | 2025-05-09 03:49:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5ab31d99-a298-3d00-b30a-51076fb57732 | -14.20823 | -45.46992 | 2025-05-09 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| edf7c061-71c4-3103-9a7b-979c2c877297 | -18.25739 | -53.00296 | 2025-05-09 03:49:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d37ead4-a314-34bf-be56-726639ee4e44 | -15.56909 | -47.85695 | 2025-05-09 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbbbaac5-4909-309b-89fc-770e469798a6 | -14.64002 | -45.13043 | 2025-05-09 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f451a931-5a64-3f6d-9fb6-4ec49e9f9923 | -21.39785 | -48.53297 | 2025-05-09 03:49:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f82825a-6870-3abd-86dd-022c7ce711a0 | -16.68062 | -43.88188 | 2025-05-09 03:49:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d5386d0-4183-312d-b591-e3df4808f195 | -14.64083 | -45.12604 | 2025-05-09 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9245251a-5e15-3741-8843-d563ff444de1 | -10.55013 | -42.42802 | 2025-05-09 03:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dd5e95a3-05d8-3d14-87f9-4689e6fef677 | -20.05596 | -49.36589 | 2025-05-09 03:49:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 49a2a931-1b61-3728-8dd0-d4e1b773530a | -17.77651 | -42.80819 | 2025-05-09 03:49:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74dbc1dc-7718-3ee2-99fa-d567aeb5ee51 | -19.84549 | -54.22215 | 2025-05-09 03:49:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c968a9b-5e95-3981-bdef-099c7ddd8044 | -14.63728 | -45.12079 | 2025-05-09 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b07ff9db-8d85-3ab9-83e0-d27f3ddbe0b9 | -16.2969 | -43.5666 | 2025-05-09 03:49:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61dc42b8-411d-3f5c-8d74-33216eecb43a | -17.52541 | -52.11842 | 2025-05-09 03:49:00 | NOAA-20 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33cdc09e-0198-3500-a4b9-7faade4d4508 | -10.55101 | -42.42294 | 2025-05-09 03:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e3690532-ea37-37e5-a98d-41caaaad0f9c | -14.22088 | -45.47727 | 2025-05-09 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 796db230-c226-39e7-8cbb-3c57131d7595 | -21.36095 | -48.73454 | 2025-05-09 03:49:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 511461c6-0e53-3c5f-9e8a-2a8fb2840f4e | -18.71526 | -47.17139 | 2025-05-09 03:49:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1035033-7093-32a9-a310-7c2c99dba43d | -17.68756 | -48.63874 | 2025-05-09 03:49:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e54e887-6f09-341c-9577-15c045d96b65 | -14.22717 | -45.46879 | 2025-05-09 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31ececc2-6a03-3c89-b464-73ca846ce230 | -14.64439 | -45.13131 | 2025-05-09 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b76633b-49e8-3934-a129-20c664d17db1 | -19.15975 | -47.8195 | 2025-05-09 03:49:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c1db4987-394d-3c28-8838-b807ad510928 | -15.53261 | -41.67887 | 2025-05-09 03:49:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 09840ad8-1287-39df-a889-0c1ab657c1c4 | -19.15504 | -47.81801 | 2025-05-09 03:49:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6479a0f-d73e-37c5-99cd-d7c74d91f08f | -19.83861 | -54.22044 | 2025-05-09 03:49:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 130e528c-25c4-39af-a20b-b0982a0aa275 | -16.29747 | -43.56922 | 2025-05-09 03:49:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36a5f144-7b0f-370f-b998-8afff9037f91 | -15.53188 | -41.68303 | 2025-05-09 03:49:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4c0478e6-7a8e-320a-a202-65f5482d4203 | -14.20372 | -45.46903 | 2025-05-09 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 550c6f85-3a6a-3c4f-a323-b0a5677126a4 | -14.22266 | -45.4679 | 2025-05-09 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b71abe40-682b-34cf-8de5-bf8e323d5b31 | -10.59899 | -39.06528 | 2025-05-09 03:49:00 | NOAA-20 | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 74028db7-e300-3879-96e0-a9beaa57bdec | -14.64165 | -45.12166 | 2025-05-09 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2100de88-040f-3d88-b9af-2c6efbe4382f | -17.47102 | -45.47278 | 2025-05-09 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7552c268-fe5e-3523-9a67-57f75edb5b3d | -15.53288 | -41.68063 | 2025-05-09 03:49:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2dfc06f2-e162-392c-81f3-1e1cc4f1660e | -18.04052 | -39.92478 | 2025-05-09 03:49:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README5.md)
