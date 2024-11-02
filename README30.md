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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 648bf153-5d7b-3938-adbc-aa858d835377 | -2.20602 | -46.52463 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 602de843-1377-3b47-9987-e235796325cf | -2.19913 | -46.46954 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d9df299-89de-3ea3-9364-76cd2c5cc671 | -2.19529 | -46.46892 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 950f8349-cfe2-368e-9f34-8edd4c62f4e2 | -2.17302 | -46.7292 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6fb50af9-c306-31f1-b036-0a8eb6f4668e | -2.17071 | -46.71872 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e576622-90ee-3007-a988-fbb78973b3d0 | -2.16991 | -46.72364 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 779fbd99-25c3-3ab1-8fa5-4048a695fd52 | -2.16911 | -46.72857 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d21678bf-8f95-32bf-b0c3-a4126209c7f0 | -2.44878 | -46.8902 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8630f5f8-e207-359a-b981-f112a201692d | -2.44807 | -46.8911 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e501856-6e3b-39ed-b374-e4718411b600 | -2.44743 | -46.34979 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bcdabec-6709-3e79-a648-3939e597a676 | -2.44668 | -46.35444 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb3a4662-6bca-35e7-b54c-da02cd4f510b | -2.44362 | -46.34917 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23812f0e-5395-311c-b06b-cdb330965a2a | -2.44287 | -46.35384 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b48dfa5a-f7e5-36f7-a978-f344fc987087 | -2.4284 | -46.71425 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38808e87-676d-3116-a402-ac74c13e8ece | -2.42607 | -46.70381 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 697eef2e-a741-3d40-91f2-c9489074619a | -2.42297 | -46.69826 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c92813b-8aa6-3297-b091-eff34ea5bad9 | -2.41909 | -46.69762 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bd6c07b-1837-3609-bdcb-78eeec27ba67 | -2.4152 | -46.69699 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54e0e388-457c-3a52-b357-444e6e8a83c8 | -2.41387 | -46.43598 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7393a728-5675-31b6-9106-f84735789f27 | -2.40969 | -46.73131 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 201a5a8e-8bca-3e0c-9bf4-db9f294dcce1 | -2.40812 | -46.74115 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21365386-2bed-343d-962a-bc71cd6e2ae6 | -2.40733 | -46.74607 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70282571-3c0d-39e9-8801-a8036c10ef8a | -2.4058 | -46.73065 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e3ef879-543f-3e28-9e85-989344cd1c5d | -2.40343 | -46.74543 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3749916c-872c-33e8-8246-2802d2632fea | -2.40033 | -46.73985 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5514ea90-d941-30fc-af49-565ecaf19c5a | -2.39419 | -46.70361 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8054cd10-ebeb-3de8-b38e-05639ebd8430 | -2.39333 | -46.73364 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c335c81-9f79-3e3b-ba02-6c45a3d1a80e | -2.3894 | -46.57578 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b8e2b36-a6c9-3e2f-a820-71824bebb950 | -2.38865 | -46.58059 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 091ee16f-d5db-30c0-b03d-bcb8f1e29f9f | -2.38677 | -46.57796 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e266f8b4-361a-3b06-b9fb-f0de53098936 | -2.38554 | -46.57516 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa0a9fc8-1fec-3354-82f9-1f4d0be08ee6 | -2.38479 | -46.57998 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c27f8685-b91a-32e6-aee1-b58dab9ce9e1 | -2.38369 | -46.57257 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa2bb1cd-3edc-381c-a2bf-6dc455af0f3d | -2.38244 | -46.72682 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6f36b10-919d-36c3-83b6-eb84cda35a72 | -2.38243 | -46.56975 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| beead64b-4a5d-3290-af35-0d0d37d71834 | -2.38168 | -46.57457 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 837b954c-95a9-3c14-b768-3c4beca968db | -2.3814 | -46.56237 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6deeb41-3117-3340-a13b-adf27605aa1b | -2.38061 | -46.56717 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87c9e0b9-140b-3857-a59a-e6eb8c101c99 | -2.38007 | -46.55953 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af5af92d-3ada-322f-b82e-262349171aa2 | -2.37983 | -46.57197 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e85a67e-a4e5-3742-bfe5-71ddda3e4ad5 | -2.37932 | -46.56433 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3583bec2-af2f-330c-b190-7c8da39883a3 | -2.37904 | -46.57677 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46d2be25-9e17-3359-9b91-c6b639dabc58 | -2.37857 | -46.56915 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be68d612-fcf3-3016-9441-642717aeeba0 | -2.37781 | -46.57396 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3374921-90ef-3212-ad6c-e9867fba9036 | -2.37604 | -46.76625 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35881a66-19ff-32b5-906f-72c81a911bfb | -2.37597 | -46.57137 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e87a837a-89fb-3be8-a649-dff9e95ad88c | -2.37294 | -46.7607 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20469352-9e15-32d4-96f0-0ed5a3703c4a | -2.37214 | -46.76562 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6084d4c7-ff5d-3e07-8e5a-0c82d1b66de0 | -2.36835 | -46.5086 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69ca0b1c-6c13-3853-83e1-2b2d06884e80 | -2.36729 | -46.41611 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0883a7ea-78b6-3e46-bc48-bfa1f7a33566 | -2.36654 | -46.42082 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1b75410-3d2d-3e6a-9066-b14772a7c90b | -2.36652 | -46.80017 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 445143c1-d054-381d-ab18-0ce5090e9e5b | -2.3645 | -46.50801 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb38629c-0b28-351b-ae85-41cabece2073 | -2.34827 | -46.46148 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab1e5fe4-8014-3457-af87-5677feb98594 | -2.34752 | -46.46621 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4475ff29-9bb6-3e54-980b-0ba763e03a1c | -2.34368 | -46.46558 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c89357dc-f3a3-3364-ab6b-c9460aef184b | -2.34084 | -46.65738 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 902f9a96-1129-35a6-b49e-356b22b806de | -2.33839 | -46.52332 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb3ad195-07ee-3ec7-80e0-aa8432b7794b | -2.33761 | -46.52815 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d61f6d3-a435-3c8d-a0b0-45bcffca97ba | -2.33454 | -46.5227 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df21d8b2-c0f8-35ed-8e3e-84460a0549a8 | -2.33377 | -46.52751 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f800ce1-f49c-3fda-91a7-41c304298285 | -2.33074 | -46.62085 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be6ccabc-a9ce-300d-9295-aba0d25fd89a | -2.32997 | -46.62569 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 763b9fe0-a8cf-30b7-b71f-69a9d54e5539 | -2.32609 | -46.62509 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc4c4493-8196-3c55-a2f1-fa68a5a4f882 | -2.32299 | -46.61963 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ebee594-bb29-3da4-917c-917421b01cb2 | -2.32299 | -46.52084 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 689b6211-f60f-3b43-9651-ac244adb0bb4 | -2.31914 | -46.52022 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34781117-021f-3825-a482-8894193a60d8 | -2.31606 | -46.51481 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 003a19bb-fadd-3e6d-aa01-2da29fc66f37 | -2.31529 | -46.51959 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0073dc8-67db-30a4-9086-21ba0344290c | -2.31221 | -46.51421 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae6ce343-9672-32af-978b-aceeac9bc607 | -2.31144 | -46.51898 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5de612af-6136-3b21-acfb-9c791366d3aa | -2.30759 | -46.51836 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2384edfd-93d9-303c-b90f-7fd5c8988339 | -2.30252 | -46.82306 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 830771a8-10c6-387e-ac4c-5d5940b3beda | -2.2986 | -46.82244 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9c81f8e-c529-3f2a-87ae-5aa7fcc0dd6f | -2.28213 | -46.4681 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d6c7ad0-29a2-30f3-baf3-b65ab7eb071a | -2.28001 | -46.7381 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8acea532-551b-32b0-b31f-71cfe23241ed | -2.27914 | -46.49907 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22d2190d-be39-3e11-ade3-bfe3d1bd4d81 | -2.27905 | -46.79381 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0f371ce-2da7-3b9d-bd87-0d1e3f6685c5 | -2.27866 | -46.67233 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47fff9cd-448e-3c8e-8494-83ae13c22030 | -2.27857 | -46.6975 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccadb4ce-55a6-3722-8fc8-89c16189cad0 | -2.27828 | -46.46748 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0ce0c8b-b4b4-3460-9010-7b6b82ffe0aa | -2.27824 | -46.79884 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7a47bfa-73a0-3a32-94f1-d90434f3a193 | -2.27786 | -46.67725 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f994f566-c1dd-34f5-bf40-68dc2cd88fd9 | -2.27778 | -46.7024 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b4de39cc-2c36-3e22-ba7b-d6d7e579b1e7 | -2.27742 | -46.80391 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 41429a25-e716-3159-99e5-61144ee5143d | -2.27682 | -46.75785 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8028eca0-50ec-3804-8ba6-187404d0097d | -2.27601 | -46.76284 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d8760a1-d76c-3e2e-b862-ebc0cb67de5b | -2.27397 | -46.67667 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 423dd529-c10d-3180-87b6-d8d8488b6f86 | -2.27388 | -46.70179 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0c2c874-5e63-3282-b203-d25cec95785b | -2.27308 | -46.7067 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87c7a9d0-6055-36ca-965e-e6c9b9ec6baf | -2.2729 | -46.75724 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ab12cb3-11c2-3e99-aa25-c6ab4d0e5338 | -2.2721 | -46.76219 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ec62e33-60da-330b-a8fe-62f8e41882f8 | -2.2713 | -46.76718 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9754abb2-60af-3539-874e-419de2d348b5 | -2.26918 | -46.70609 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56b3a286-11a4-303a-ab3b-f55f0af82472 | -2.26528 | -46.7055 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 345f5ae3-0860-35c5-991d-16a9ab44b9f6 | -2.2651 | -46.67826 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8d88abe-cb71-3584-9e90-57a271e8c160 | -2.2624 | -46.64975 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbea7492-682b-3e14-82fa-d17ef5b5bf1f | -2.26229 | -46.67481 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ac37945-3228-3d4f-a6a1-c187668e1528 | -2.26198 | -46.67272 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 604ed86e-8cf8-3924-96ad-d00d60bcac84 | -2.26121 | -46.67763 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README31.md)
