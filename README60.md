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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0306932a-c623-370b-8c28-3b751abc57f6 | -10.45327 | -69.71708 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42e489b4-cdb7-3263-8463-df65b91d2561 | -10.92461 | -69.33423 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fab318d9-968d-3f57-837c-a9aecbd1bbcb | -10.92076 | -69.3372 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ce08717-8526-3cd8-96a7-9853d20e2302 | -10.90539 | -69.4136 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a6cba94-c4f9-3b53-a6f9-29aee55351d4 | -10.89933 | -69.40903 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bfb164a-3a6d-326f-8b7e-aa89a94015fc | -10.89823 | -69.41603 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e59eba1b-eacb-3323-ac2a-eba9322c45e5 | -10.89548 | -69.41201 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5307840b-ae2d-3c21-b38e-018b32178ebe | -10.89154 | -69.32893 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c104cee1-6fe8-3108-9333-5c8e83047fe3 | -10.8883 | -69.39293 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3ba3cf1-1045-37fe-8a27-c9c17d3f50c1 | -10.88775 | -69.39643 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6af4a50e-7bc1-3c26-ae3e-6ca91291403c | -10.88499 | -69.3924 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7195eeb3-1325-34e7-b817-9cafa5863916 | -10.88444 | -69.3959 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff188914-e333-3a74-9875-647a2f1a13e9 | -10.88225 | -69.40988 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d852c4a-3a07-3a64-8eed-980acbb0945e | -10.86872 | -69.36447 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1be4c70-755c-3fa6-b6e2-af634bdaea81 | -10.86542 | -69.36394 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8aa7678e-1673-31d1-9f6c-c471ee9bf46c | -10.86379 | -69.39593 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c4bb7e2-fbf5-3c14-8f62-bdd0c4070abe | -10.86048 | -69.3954 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab1b475e-5b9f-3bc7-aebd-1a3e22a8b297 | -10.85938 | -69.40239 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 003737f6-d817-3e9d-83a5-3181a2e2fa09 | -10.85884 | -69.40588 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fdc8be3-8717-3876-a1e9-6825c1556d4d | -10.85719 | -69.41637 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7049bb7a-d388-340f-9376-8459ba5d5c94 | -10.8384 | -69.34168 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb906f03-e2c4-36c6-a578-d789a9de026e | -10.82855 | -69.4261 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 131e1ea9-06cc-3595-8383-77d15b534e88 | -10.82189 | -69.36054 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fea2208d-3244-3057-ba12-4d827c007abd | -10.72027 | -69.35922 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f99ce96-6ed0-3afa-9c22-80530ba0a081 | -10.69218 | -69.36546 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52ff35b2-f0c8-38a8-88e1-4eceb7af093b | -10.69163 | -69.36894 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37b0db6b-fdc8-3b15-9add-751381bf9a39 | -10.68942 | -69.36143 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95da03ce-698a-30c1-852c-932f868f0e98 | -10.68887 | -69.36493 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f60b7cdc-f0c9-3ced-85d6-809bc7738ab6 | -10.68833 | -69.36842 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a56d4b3-44fb-3585-9494-bd9aaa8eb952 | -10.68612 | -69.36091 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 352e0852-5208-3ea2-96c1-1faba4de50d9 | -10.68007 | -69.37783 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15d8d598-5506-32f7-ad2a-38d37a031242 | -10.67238 | -69.40525 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e79ddf22-93bb-31b4-a5f4-c8e238337da7 | -10.67019 | -69.41922 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 185f8f6a-9976-3ef4-9aa8-014d7d2f3bb7 | -10.66964 | -69.42271 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aa64e7e5-70f1-38d3-9263-a78305a43e83 | -10.66541 | -69.2964 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d30b03b2-44d5-3545-899e-7633d287c4cc | -10.65165 | -69.31927 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1e48776-e6bc-36c3-94a9-adb9499a2c95 | -10.58612 | -69.34815 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0415ed24-bc93-3cd9-8d7a-14fb29c3e21f | -10.4512 | -69.29767 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b5afe6f-5eeb-3e3b-a6ee-30924a2bf135 | -10.451 | -69.36591 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20800700-dbf4-363e-818d-e1a48b16dd56 | -10.44955 | -69.30814 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9196b05f-e3e4-36f3-b464-06b28b197365 | -10.14822 | -69.32454 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d94c0fe-5aca-3d96-a2c3-0092475aa940 | -10.14492 | -69.32401 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 287c5410-90a1-365f-84ec-e0aa8546e0cf | -10.92195 | -69.45927 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b95ae73-f9c2-39c4-b88d-dbe0bfaedf03 | -10.90713 | -69.63971 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbddbc04-9e87-35be-bb97-45516edaf786 | -10.89334 | -69.74857 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0526dd5-595b-3574-b925-ef2c6da6d724 | -10.89058 | -69.74454 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37b27c83-f216-39d0-894e-f683add7356e | -8.03339 | -70.20387 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65155dbb-a4ec-3805-b8f6-e3072e6dd2b4 | -8.03281 | -70.20747 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 460ac495-e5dc-39f2-afc6-23a1a299a6df | -7.94122 | -70.6838 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 817bd69a-739e-3d99-b2f4-1936cd390cd7 | -7.86038 | -70.62122 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad54d34b-27a5-3e3c-8d2e-eda501aa1431 | -8.96487 | -71.86282 | 2024-10-17 05:53:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3a56421-d28e-3c0d-8d5d-0fda9b26fd89 | -8.89466 | -71.29556 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 198138f9-876a-3573-9336-af48b8842e11 | -8.87125 | -70.55379 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 49ec1dad-293e-3abb-8c23-67386760be77 | -8.8525 | -71.33593 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40114c7a-aa26-35fe-9afa-d8151e020e83 | -8.84365 | -70.55301 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51e46743-4153-3356-89d0-e303954cf8f2 | -8.84237 | -70.55313 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b0f455f-b1b2-391f-9cce-b7a3aacb6882 | -8.8214 | -71.2295 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc8fa201-0f0d-3a40-8ecf-7a19ac175fe2 | -8.80892 | -70.58881 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c3832ba-f6ff-3db3-ab54-731c1d864ec4 | -8.80554 | -70.58826 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2bd1113b-7eb0-337c-8193-a6a31ce79118 | -8.70651 | -71.02817 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2df670d5-6b5c-31a8-b25e-2ac144c92805 | -8.70308 | -71.02759 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66486439-c2fa-3bbf-8b2a-e45dd1accdeb | -8.70247 | -71.03135 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37b6c52c-0762-3638-9c0f-bdac49d83d16 | -8.69438 | -71.03775 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6f7e036-7bfa-3578-8e29-f70c3d2b8086 | -8.68143 | -71.56065 | 2024-10-17 05:53:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 779f225e-bbbd-3c24-a9c8-d1d10b17f654 | -8.6806 | -71.56149 | 2024-10-17 05:53:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 316e437c-a8cc-31b3-bcf8-0da413d3f188 | -8.67072 | -71.55582 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7d4753d-604d-36b6-9127-32e32654bef1 | -8.65411 | -71.61388 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 493ea10a-aa04-3450-a752-1856eede7612 | -8.44158 | -70.71383 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26ae9a4e-d983-3d34-bf5a-8689aba5b713 | -8.44085 | -70.80502 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7952ee7c-c646-3223-ab08-36c2e6d47644 | -8.3274 | -70.57539 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a874f3c-0a36-326e-b5a1-e28eb266959e | -8.24677 | -71.1578 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e099610a-63f2-3eb0-8fe5-cbc4436631b2 | -8.24528 | -70.84323 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57606531-b162-3825-bb33-438aa4666cad | -8.23748 | -70.89195 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32373ac4-5f4f-34ae-984c-35d570a7a75e | -8.17563 | -70.83955 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2ac952f-3a73-3f69-ba63-cc22852ad82c | -8.16357 | -70.22137 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a385a2b8-e7b3-3b2b-bfa7-acb7f5363c62 | -8.15303 | -70.20123 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8481c344-0064-3f45-904a-26b71a1e7151 | -8.0823 | -71.25774 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68a38a12-a909-3d3a-8e06-65899890a008 | -8.04419 | -70.95744 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c7ae535-affe-38c8-899f-d105ba11534b | -8.02472 | -70.90389 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71b3ca3f-3fd4-3c42-9eb9-482d5946d746 | -8.02168 | -70.90362 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a85e6c5-872f-373b-ac9e-9b83864caee6 | -7.98398 | -71.39073 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ad3bd11-898e-3fe5-ad07-2a9a52c5c8f6 | -7.97202 | -71.33234 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b9099e4c-f9ec-32f9-9387-6517c088add0 | -7.95311 | -71.38159 | 2024-10-17 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 84682e57-af4c-333d-a363-458350242183 | -7.93242 | -72.40602 | 2024-10-17 05:53:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a1d0577-c80f-37bf-b728-90ceeb792a76 | -7.89187 | -72.44444 | 2024-10-17 05:53:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc78171c-465a-3d8b-bbee-915e5be9bb0c | -7.88743 | -72.44819 | 2024-10-17 05:53:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 447e0532-3ced-3470-827a-0c1211a389a3 | -7.88669 | -72.45261 | 2024-10-17 05:53:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59f6d948-37f2-33ae-b3f4-70e33385479b | -7.88594 | -72.45704 | 2024-10-17 05:53:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d18d6843-2568-33d7-b0f6-df796c986a30 | -7.8165 | -73.05327 | 2024-10-17 05:53:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1573b98-22ef-31df-8951-472a3de87baf | -7.81149 | -73.10654 | 2024-10-17 05:53:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfcae338-4843-3953-9f77-afb5e81059f8 | -7.81068 | -73.11134 | 2024-10-17 05:53:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cede84b0-c669-318b-af66-1227ca662f76 | -7.80684 | -73.11068 | 2024-10-17 05:53:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa59af92-84e0-3cf1-95b8-85227e0d16ca | -7.79696 | -73.00594 | 2024-10-17 05:53:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13cb75b1-9f17-356d-be3a-64c74d721e97 | -7.76861 | -72.85388 | 2024-10-17 05:53:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc771aa9-2c91-3f98-9b44-112cdda0f62b | -7.74333 | -72.91206 | 2024-10-17 05:53:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72a047e0-31fc-3bdc-ba4a-281374811102 | -7.6851 | -72.91401 | 2024-10-17 05:53:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f493ddeb-0093-3af5-94e8-ab3de644c289 | -7.65441 | -72.49468 | 2024-10-17 05:53:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f665aeb-8d14-34d3-b176-3a0881360142 | -7.65246 | -72.49644 | 2024-10-17 05:53:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 632aad3e-4af8-3acf-87c2-cae677566620 | -7.33698 | -72.90712 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e945905-7b5f-3f03-a0d1-576b864ef90d | -7.93438 | -72.90641 | 2024-10-17 05:53:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README61.md)
