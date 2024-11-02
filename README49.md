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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69b39fbd-5acd-3fc2-b266-b76aab095c70 | -3.16706 | -51.07219 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f5d799e2-64f0-3e0a-b01b-b826b298d041 | -3.16685 | -51.08315 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1022684c-b281-3a6a-90ac-02e884791804 | -3.16656 | -51.07527 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d55b3b53-892a-3ddf-addb-f89dedce66d4 | -3.16606 | -51.07837 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 51090a9f-f477-3a23-bd4e-b37d80989b05 | -3.16556 | -51.08146 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a9008c17-f4ab-3a3c-95d2-920211108c12 | -3.16273 | -51.07609 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4040257-1f1f-3b5b-b21f-7495b69566ea | -3.15056 | -51.14773 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45cfd6f5-0f93-37fa-8ddb-7b18377bc5f0 | -3.15 | -51.15099 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 060632c7-0e4f-380c-bd74-3ecb3edfab74 | -3.14923 | -51.14944 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95877df0-ff0d-339e-8188-574af84faac3 | -3.137 | -51.02896 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8ade49cc-1d1f-3856-9e4e-c9f217318e75 | -3.13649 | -51.03202 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afd64c07-6cdb-31fc-92e0-29e3c51710e6 | -3.13136 | -51.03105 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65038446-85ab-3dd0-8ef0-967d1d0a2858 | -3.11029 | -51.12651 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b214c4f1-a142-3682-ac43-470aa9e7e8c1 | -3.10976 | -51.12973 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f6e47bb4-601b-374e-a5e2-7c80d2fe50fd | -3.10924 | -51.1329 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0f62f8d8-da1a-354d-8d17-87ac9636c793 | -3.10871 | -51.13607 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b8b28505-bbfb-301f-97e8-5fb41e44dd2b | -3.10818 | -51.1393 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b64e4140-a7f6-3fc8-bf39-a36c79a4e58a | -3.10564 | -51.12241 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67814448-1db2-3142-b664-028d8e5a4269 | -3.1051 | -51.12566 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37fd8a33-c749-3e27-97b9-acb0bb9b5848 | -3.10456 | -51.1289 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3cb010ff-10e3-33b8-8b5a-3314bdc68d1f | -3.10403 | -51.1321 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9b66f7a0-bf93-3e29-a155-56d671e3ba1a | -2.85015 | -51.36503 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72c39e01-cd0d-380a-9df0-245febe707b0 | -2.83404 | -51.808 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77b46b31-926a-3c8b-88ac-de9efa019632 | -2.83312 | -51.80721 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5820dece-45ed-3666-99f9-56f63e267a1c | -2.83255 | -51.81073 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bce58559-be78-3984-8bc8-05705e10a85c | -2.82917 | -51.80362 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 00669829-eac9-37aa-9ccd-02fee4ceeb0f | -2.81054 | -51.34149 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fab450c8-528a-3a1a-b980-71550eafc716 | -2.80999 | -51.34478 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9977de3-2508-3637-b396-6e91004f4585 | -2.80943 | -51.34807 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| edb20180-928b-39cf-b99d-fbd2f8826338 | -2.80617 | -51.34249 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 146bdbb7-400f-38e1-ae0b-9cdaa59305ee | -2.80564 | -51.34579 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8131f85c-6f27-3764-b3ab-248be7fe4623 | -2.80511 | -51.34907 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d70d7dfe-c0e1-3469-bb6f-87f7e44609b4 | -2.80414 | -51.34721 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99ef437f-6f7c-329b-b00d-768236cf0153 | -2.79997 | -51.60159 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 41163d66-226c-3589-b68e-1945d57d5cc7 | -2.79941 | -51.60497 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ec9a0cc2-5dcd-3c14-8e13-91818703aea5 | -2.79884 | -51.6084 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e114819b-7316-3ca8-b3fa-2118c826123a | -2.79827 | -51.61182 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e8b3528d-ec19-38e4-851f-f8d5f9e1b72d | -2.79704 | -51.75383 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e7ed58ba-cef8-343a-b7ef-5a2513273e64 | -2.79459 | -51.60064 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cb51aa94-b67c-3eba-beee-53b90e02b1c2 | -2.79402 | -51.60407 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ac598ac0-063d-362f-89db-06d2ba48097a | -2.79345 | -51.60749 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 91ba6626-77ef-33e1-849d-f7c9e40fced6 | -2.79289 | -51.6109 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b13da9a7-da26-3ec3-b936-9ad2a0bb4787 | -2.76631 | -51.67025 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6d80aa1-5481-3b1a-bbbc-39ecf91e4ed2 | -2.76516 | -51.67712 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14378842-8401-3895-9c82-e476dbc93056 | -2.74282 | -51.73639 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a1dc097-d8e0-3b37-84fb-7ca766e47ae1 | -2.74226 | -51.73986 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 286b56f9-acd0-365b-a0ac-a1dc0337c372 | -2.7417 | -51.74335 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 913f8531-4ad7-3a6a-be0c-8fae52af0b41 | -2.73896 | -51.73331 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 477f9df5-6165-35f4-acbc-cb35d730f062 | -2.73836 | -51.73681 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c662b259-60eb-3018-a298-8d340ea5bd8c | -2.73778 | -51.7403 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3338755a-b498-3de2-965d-4eece34827e1 | -2.73626 | -51.74239 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b7d1bef-fafb-3cda-8fbd-5b000faa3a54 | -2.73352 | -51.7324 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b83848d-c333-333f-9a93-f0355aa3d804 | -2.73293 | -51.7359 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a7db0e3-924f-3128-bcbc-b38506124caa | -2.73252 | -51.73098 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0a286b7-6c88-34b8-9871-635d83d41eca | -2.72807 | -51.73154 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da60e445-4ac4-3ab5-b918-d71924ecdf69 | -2.72445 | -51.71183 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f66e2820-6f96-3f74-8ecc-d2734dab6849 | -2.71903 | -51.71089 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 292db5f3-6ec3-3fee-8834-a3d8dece0f39 | -2.64987 | -51.75703 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2956543-3d39-39e8-b40d-5e8ffade0031 | -2.64973 | -51.72445 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11ed6c60-f3ee-35fb-8a49-615a05592275 | -2.64383 | -51.75964 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8294b48a-5bbf-33ca-8f48-8611a1baf818 | -2.6354 | -51.73578 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c477bc10-6e10-3b0e-89d0-ede3a008e0fa | -2.58247 | -51.92257 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc084af2-36c8-3afb-b6cb-1903434e2d47 | -2.5822 | -51.92568 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efc8cf7c-5a0a-313f-b51f-8b0beb51838e | -2.52116 | -51.782 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 925688b0-93f8-3cf6-9f00-83d4986982cc | -2.52062 | -51.78246 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bb89869-f340-3323-9cf7-c30d23f9ed44 | -2.52058 | -51.7855 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 94dcdd53-b65a-310b-b668-f640845e4f11 | -2.52006 | -51.78598 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 51d545bb-b0cc-3d5c-bd62-2fc4eca17092 | -2.51999 | -51.78902 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 26db7607-f7be-3318-85ed-c4cd270edcbb | -2.51949 | -51.78951 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4eaf144f-06be-3301-8c92-ea09f0f26eb0 | -2.51939 | -51.79257 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e0b3ae37-03ac-3df6-83d1-fc407da08ec5 | -2.51892 | -51.79309 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e617755-5c95-3ad8-b048-140509299b14 | -3.53109 | -51.47678 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| dda01be3-61cc-37ed-947b-7bae82d93251 | -3.52581 | -51.47595 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 432524f5-d7ef-38f0-91db-467737cfbe90 | -3.43755 | -51.52051 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9320dd4-a988-3ecd-99bd-9fbac00abddc | -3.43699 | -51.52383 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d22c5786-e69a-3a32-819d-9207f49ebcf9 | -3.43642 | -51.52715 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff5bf4a6-a33a-3504-abcf-58378dc01081 | -3.0262 | -51.37243 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ccbe260-17f9-3882-85d8-6820d2951849 | -3.02092 | -51.37153 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fece5ec5-7c3b-3e86-80f9-62733766c7d4 | -3.02037 | -51.37479 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1ab06ce-6a6d-30e2-b39b-3d2d73eaab6f | -3.01982 | -51.37804 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5be17b95-3e99-30e6-b9f2-32dc0c1ad355 | -3.00704 | -51.58427 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0fe609d-55cf-3c12-934a-1f1b4582eb13 | -3.00647 | -51.58765 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c385a3eb-a37f-33b0-a201-78c20e01e1c2 | -3.00367 | -51.80469 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25df71f5-bec7-3d04-99a7-90814066a46a | -3.00281 | -51.57661 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 07d2cffb-9b5f-3fd6-b5e4-a951a77e0d41 | -3.00225 | -51.57993 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 25a89dc4-4f63-3d18-97f2-cb194e5a7505 | -3.00168 | -51.58334 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6a1d4ff0-f3a5-3d0f-b5f1-e83be4dc68d6 | -3.00111 | -51.58676 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| eb9e28c1-ab47-3577-a940-f376064667c6 | -2.99687 | -51.57916 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8c8f16a4-f897-3617-ab7c-34f312d942ef | -2.9963 | -51.58257 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bc6d0b52-c094-34b2-8c1f-64bd3541b9a2 | -2.99572 | -51.58599 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5326bc9f-37a6-3a20-a985-07fd4fa110ad | -2.96893 | -51.43024 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b69f7eac-d4a2-32d9-8174-c74e2b1fd0cb | -2.96839 | -51.43355 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93ba7067-86d4-344e-a17e-cea592161e92 | -2.96363 | -51.42933 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d970ed95-6b95-3cfb-bc11-6b57b39efce0 | -2.96308 | -51.43267 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c8df6f6-760b-3389-bdc2-21236e4fa562 | -2.90096 | -51.77627 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e35a5305-6f19-3d4b-b504-ac96ddd757dd | -2.90039 | -51.77973 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a5641507-7c44-3e90-b505-905ccf3c7b27 | -2.89991 | -51.48352 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb6878a8-cf6c-3608-8ba9-1d5487192bd5 | -2.89935 | -51.48683 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f53effb-55b6-3554-beb5-d5c29b989491 | -2.88586 | -51.66596 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b58e0c82-bda0-31fd-b209-9420e022db56 | -2.88159 | -51.65825 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README50.md)
