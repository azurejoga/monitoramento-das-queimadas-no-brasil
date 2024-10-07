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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1168813b-3662-3040-8ea3-0c485a4ca770 | -17.12311 | -56.7772 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 49ea2c50-4eb4-328c-a2c2-60063c53dc47 | -17.12057 | -56.76651 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a75f31d0-5aae-3772-bc32-2a0b6b67906e | -17.11989 | -56.77157 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 2605331f-8cb3-31a8-9d0b-66ac4f906e00 | -17.0056 | -56.7059 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 371e62dc-494c-3c03-a419-942696f26f9f | -17.00237 | -56.70025 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a0aa7772-db39-3f51-b43a-b02b0b3e81e7 | -16.9951 | -56.72507 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 7d7882af-bb55-3777-9f46-65e48812bd81 | -16.99254 | -56.71435 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| cdd61237-8585-399a-94c7-0f34e2b36684 | -16.98931 | -56.7087 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 3e673976-04f3-32df-96dd-b66086a4e7dd | -16.96999 | -56.76099 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.0 |
| ebda31f3-6ab3-3981-ba64-4a63f914ff35 | -16.96541 | -56.76546 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 5b831cad-c485-3796-9a2a-25d7c32ac31c | -16.96402 | -56.77553 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| c5485ccd-0eb5-3f11-898d-4caf2cd06f8d | -16.96333 | -56.78056 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 1478db15-f385-394d-8b57-c1b35f6404ab | -16.9625 | -56.76153 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 2574cbec-a3cf-342f-a9dc-5b65171a410d | -16.96221 | -56.75986 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 6b21f7ff-2bb1-3cc7-9e5b-27f2ac5f2ce3 | -16.95625 | -56.7744 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1cabfe2c-07ea-3ba7-be8d-a268024729b8 | -16.87045 | -56.73471 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c51d4562-ae25-372f-9cf2-0a1566e44d06 | -16.87019 | -56.73613 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 97a71bbd-15cf-3aab-b11d-ed1f637b9656 | -16.86762 | -56.72546 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ed9d9ffb-78bb-341f-bc81-3dfe7c45fe6f | -16.86116 | -56.71421 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 2c7803be-e6a2-3ebb-aa3b-c819d0c6b517 | -16.85877 | -56.73301 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f5d665f1-c9bb-3506-9232-e3c783bf630b | -16.84961 | -56.74194 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4abf8393-45f6-3a39-9c98-bf177654f0dd | -17.17578 | -57.3542 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b5ba5ce4-4b49-30b3-80b3-a8b296269f2c | -17.17513 | -57.35891 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 96f5f623-a92f-3bf4-a14d-9ed296ab1fb5 | -17.17331 | -57.3442 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 48371dd9-75d4-3168-b1f9-d4ce808f34a3 | -17.17201 | -57.35364 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 72d20139-38a4-34d7-8ab0-1dc7361f519a | -17.16954 | -57.34365 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 98f0de9d-73a5-32ab-bc60-9f5a25f0bd62 | -17.16889 | -57.34835 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 209448c1-873f-37d1-b708-f7297ef06952 | -17.16824 | -57.35307 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| dd759dc1-6250-34b3-9d3a-533135aab97f | -17.16576 | -57.34309 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.0 |
| beb72ee7-10d1-30a5-9dfc-3529f8881890 | -17.16447 | -57.3525 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 29558101-7ef0-3036-8e2d-82b62a74614d | -17.16382 | -57.35722 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| ebcc7964-5a20-3e21-b258-b67bc3163173 | -17.16199 | -57.34251 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 9de25c7d-b81a-3957-81ee-ba7f1899508e | -17.16134 | -57.34723 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 8a1f0fe6-8fb7-3011-b337-3a9cbf046c87 | -17.15887 | -57.33725 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| b2948225-8f94-39da-864e-1a58868a456f | -17.15822 | -57.34196 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 01375dea-6cfc-31a6-a0b7-2d8bddc632bf | -17.15758 | -57.34667 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| c6fff25b-aea5-3394-85c8-b1c13fb68bbf | -17.15251 | -57.35553 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| b76956f6-05b2-3655-ac5d-52f766b6ac86 | -17.15166 | -57.41766 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| cd10d4b6-6989-3c34-820a-0c7497aa7e76 | -17.15101 | -57.42234 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 960e4441-eac5-31cc-867c-ec39526aaab2 | -17.15003 | -57.34554 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 989494ed-00bd-3010-b1c0-b5e3ee70e92c | -17.14874 | -57.35497 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4741766c-91ab-3f64-b958-7c9b2e79bb86 | -17.1479 | -57.4171 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| bb98dd97-abf8-384d-b063-3218db031d91 | -17.14661 | -57.42646 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| e26bd404-7f3f-33fb-aaf9-7d65932b3009 | -17.13096 | -57.42889 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3a132635-1a39-30ba-9e56-3c66734b5d31 | -17.12785 | -57.42365 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 343a2132-f3b4-36bc-87c4-7c79e9b0c2f3 | -17.12721 | -57.42832 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 23c162ca-7334-368a-ac67-dd57cf2665c4 | -17.11542 | -57.374 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2c96f13b-4ca6-31b2-a8bc-f51ed4081333 | -17.11537 | -57.40271 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 70881c72-3baa-3984-9ea7-02bfd0180d88 | -17.11478 | -57.37869 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| fe3db6a4-8718-3b22-82e8-87ee3961622b | -17.11351 | -57.38808 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a7f91942-2f4e-3280-9e62-a5443b662ad0 | -17.11288 | -57.39277 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9d21c721-9418-3e7a-a339-a946606d12d8 | -17.11161 | -57.40214 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 40e47c14-1ce6-3fd4-ad58-1cc4b26d009c | -17.11102 | -57.37814 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| be19ef99-866b-3d3b-8a87-3758f1213670 | -17.02437 | -56.83209 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 290396ec-2d45-3e3d-9521-390a3fe37d38 | -17.00499 | -56.82925 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ea3e9950-d69e-3528-a66b-ce3a35d9c10e | -17.00432 | -56.83424 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 956baa77-5f97-38a8-9e20-6b7641e63848 | -16.99723 | -56.82811 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9dbaa995-1bfc-3f42-b97f-eee3a5fc4891 | -16.9947 | -56.81753 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| badf2830-b243-3e94-a689-943b7da4589f | -16.98694 | -56.81638 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d60036cb-0a6d-391b-9474-5d4230d673d8 | -16.98051 | -56.80522 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2c9f2abb-3343-30ce-8e6d-7eb52acd3061 | -16.97275 | -56.80409 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| aa81139a-0fad-3176-b962-66e2af47f1b2 | -16.9722 | -56.80234 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0292b4e2-d2db-308a-8057-98ef8b63a280 | -16.97095 | -56.75763 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| f6175a6a-7a75-30bb-8b49-a0ab7fbd2a7d | -16.97069 | -56.75595 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.0 |
| 718607a0-d7dd-327e-a963-6c29680ad70b | -16.97019 | -56.79347 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1b6cfc80-c234-3a23-b655-3e0c6c1b7bef | -16.96832 | -56.80178 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 804dbb8d-9f1a-3a92-8545-67f79d19ef35 | -16.96754 | -56.81356 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 5b702b39-b618-379c-8d7e-2c694007ab18 | -16.96697 | -56.78787 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 02c84dbb-7f46-3bac-9f6d-7690e133a9f7 | -16.96693 | -56.81179 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 54cb7275-d3a6-3f5a-bd8a-07b5d456afdb | -16.9668 | -56.75539 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.0 |
| 30b4273a-90d0-3718-b168-62cef71b7bce | -16.96652 | -56.78616 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b55b5eb7-62d0-300a-9871-7512bb697ff3 | -16.96582 | -56.79118 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 204cc022-bd9a-3f45-aeea-dba7f5aa71ca | -16.96375 | -56.78227 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 17c91b4f-143d-34b7-8649-67254ca41b28 | -16.96184 | -56.76658 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 13ae5f9c-b1e3-30b4-8c2e-8c3eba7cb1f0 | -16.96152 | -56.7649 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d16b7acd-d9ac-3adf-8e1c-0303ed96d22b | -16.96083 | -56.76994 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c22298b8-2a3f-38ec-b797-029467035b77 | -16.96052 | -56.77666 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d106497a-4c6f-3d58-afcc-42dbd6957ae0 | -16.95986 | -56.7817 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0c7663c7-69cf-3ba3-8fae-870f8e9e78f5 | -16.95694 | -56.76937 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8343764b-4ad4-362b-bc69-72a7847e8b0e | -17.15986 | -56.97108 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 97b39ad3-5637-313e-a031-f2184693ae27 | -17.15918 | -56.97602 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| dba492fa-e2fa-3d52-b00e-44a7a2c43c6b | -17.15743 | -56.97258 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e873cd83-0a56-3bf9-914c-7c4de1191eff | -17.14831 | -56.96937 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 352a68d1-e8ca-33e6-a868-74d1d8b9eb3c | -17.13849 | -56.8103 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 985fa849-cdad-358c-b494-23cf9a569a41 | -17.13713 | -56.82037 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 163854ac-a3f7-37d0-9d78-120ab4dcadbb | -17.13528 | -56.8047 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9a69c1a0-be0b-3156-a622-7fb8205e2589 | -17.13392 | -56.81477 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fada74f9-0b80-3ac0-b447-89debc2b1e2a | -17.13207 | -56.7991 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3636356c-3824-3a3c-877f-12edcb34ed44 | -17.1314 | -56.80413 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| af77547f-4c7d-39a8-bf63-de63ffae2973 | -17.13072 | -56.80917 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 51f1e245-314a-3eac-a7bf-225a45ff0c77 | -17.12936 | -56.81923 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 4eea6835-3c16-3f98-b5cd-40cc95c7bb03 | -17.12868 | -56.82426 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d80b507f-6d74-32a6-b702-679a9f468599 | -17.12818 | -56.79853 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3645967a-8f10-3c24-93d3-9fa271cb4266 | -17.12751 | -56.80357 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 8cbe369c-21c8-3382-bd3e-253152edbca6 | -17.12732 | -56.83431 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 3fecb318-a9ab-3d23-bbd9-a6ad1170df07 | -17.12664 | -56.83934 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| fc7b9f71-1651-399d-adf9-2624da3aeb9e | -17.12565 | -56.78788 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 47923e70-2c81-3c4b-8a84-27289467ce94 | -17.12479 | -56.82369 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 20e127d3-1ce5-3267-af4b-42ea053c7245 | -17.12429 | -56.79797 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| c353f0cc-a322-3ff8-8bbb-db6c736869b7 | -17.12411 | -56.82872 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |


[Clique aqui para ver as próximas entradas](README122.md)
