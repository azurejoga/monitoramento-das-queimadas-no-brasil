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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f51c7c8b-b350-3ebf-86f0-cf38cfbb5e50 | -16.50563 | -57.73826 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c116d3f0-4c24-3ae0-9c75-73bdb0bd4d94 | -16.50494 | -57.74234 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0074f436-f017-36ff-867f-9250a9a9c4e6 | -16.5049 | -57.7211 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7f951e2a-215d-3548-a187-f5630ceabcce | -16.5042 | -57.72528 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 906ca552-95a4-3812-8cfd-f37ae025ae26 | -16.5028 | -57.73353 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 86120139-83e5-3adc-adb9-1b105ba7fb74 | -16.50211 | -57.73763 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c861171d-bb15-3c06-9bb6-b4111477d2ff | -16.50142 | -57.74171 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f7f6ed17-1326-302b-b801-8767c1b65c7b | -16.50138 | -57.7205 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8dfed060-a5c3-308b-979c-7b40b650e73d | -16.50068 | -57.72466 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d0ec5871-727a-3d1f-8e40-4b65a833fba5 | -16.49998 | -57.72881 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| ec1aeda3-a903-3d73-95f8-8915ae8c9f68 | -16.49928 | -57.73291 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 94aa38dd-0fc5-3113-a3ce-9ef7667b073d | -16.49859 | -57.737 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b97ebc66-7210-38a8-870a-d923196f7f1d | -16.4979 | -57.74109 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 97d54ce0-06c6-370a-bd0b-2c5881f1c149 | -16.49786 | -57.71991 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 38dc7c27-c179-3922-a4d5-92a53bcca3ac | -16.49716 | -57.72405 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1de2d144-afd8-3b4a-a743-7349d87798b9 | -16.49646 | -57.72818 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| add7fee8-c1a1-3891-ba45-9f4a1597d578 | -16.49576 | -57.73228 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 3d2911b8-433f-3011-95ff-d9dc354fd3f3 | -16.49507 | -57.73637 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ef68e641-6024-32d7-9ea6-4db5a6f7f12d | -16.49438 | -57.74047 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| cddfd919-302f-3b23-9390-960dee7bfe25 | -16.12729 | -57.59184 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 428654c4-ae84-3044-9493-b5a96902b580 | -16.12451 | -57.587 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6e393547-b414-3f61-8b37-6222388d4719 | -16.05762 | -57.53009 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4753bf9f-4607-36fa-905b-d875ab2aff6a | -16.05484 | -57.52521 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c72f0bfe-20e9-3783-8f6d-5344da591c5f | -16.0541 | -57.52954 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0cb93f2-31af-3a56-81e9-449b2c06f16b | -16.05207 | -57.52032 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36ee13e2-f721-3993-9b7d-cd954668f940 | -16.05134 | -57.52458 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01384bdc-b810-338e-942f-8cad76b85037 | -16.04855 | -57.51978 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52958858-5744-3a61-9b73-c84efe439d18 | -16.04784 | -57.52395 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5347984-71f2-334b-9d5b-982d80403f83 | -16.58693 | -57.1479 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 53d4bb9c-3e0c-34e9-9738-7cb46b3f90ac | -16.58628 | -57.15178 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 5971fe56-170d-3b1b-8cee-362f72647f06 | -16.58562 | -57.15568 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 6b1a03bd-83c0-35c4-88b6-dde807890507 | -16.58349 | -57.14727 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 636f0eac-d23b-3798-aed2-a5ca10dc6672 | -16.58284 | -57.15115 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| c8229b2d-47d4-341d-b24c-95c7d8fc632c | -16.5827 | -57.21562 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| de48a97e-417c-39f0-b19a-48e770e7beb4 | -16.58219 | -57.15504 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 9c9cfb0b-a5b7-379c-a1bc-bb0d5ea2866f | -16.58204 | -57.21954 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0a5f589b-81c8-37d1-8aea-c38684d4b9e9 | -16.58005 | -57.14666 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| ab0581b4-3869-3041-9f72-aad6fbf8ca7e | -16.57941 | -57.15053 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 69350bcf-f046-3223-9dfd-8621c72c73c7 | -16.57876 | -57.1544 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 4462f62a-9222-3715-b38f-6cf52f4697b7 | -16.57662 | -57.14605 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 44bc8a6d-a526-3229-9f9b-6bd952c27636 | -16.57597 | -57.14991 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f1ff226d-ee51-3116-a542-a3f17aea8ed5 | -16.57532 | -57.15378 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 08051a86-6bef-3e71-9e7a-8ef57e279445 | -16.57335 | -57.16557 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 65356a22-a6e1-35dc-9663-9702724f9ff3 | -16.57318 | -57.14543 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| cfa91c06-4022-3721-b77e-519289b79935 | -16.57253 | -57.1493 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c47e646f-2533-36eb-9b18-b97e918649d6 | -16.57204 | -57.17339 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 9d6b97a3-69f1-309e-ba40-f2849d3e2368 | -16.57189 | -57.15317 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 90a7cd74-d05f-39d2-8df1-aaa32f07e8f7 | -16.57123 | -57.15708 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 03fdc984-1fe5-3115-99dc-2a21a3e4a26b | -16.56845 | -57.15257 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7ea974cd-fc4a-3d02-aacf-ef7d624767d1 | -16.56779 | -57.15648 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 312f7192-9096-325b-884e-a4530e379dc7 | -16.56614 | -57.20861 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 88f181b9-da37-367b-bcdf-cb532317f220 | -16.56335 | -57.20407 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 14d7459e-b4e1-3b77-ae5a-b848a4f7c17c | -16.56168 | -57.25633 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 00a3ebdb-c00d-39a3-9307-83a8138985be | -16.54165 | -57.24868 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 79e45dcc-00de-3f09-b6b3-6e2975bc6a6e | -16.54005 | -57.21604 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5c6eeaa4-921f-399b-ad2d-b1d87323ff0d | -16.5382 | -57.24805 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 2fa0c10b-e036-32b3-8796-1f38b176acd4 | -16.53687 | -57.25593 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5ebf29d0-a515-313f-bdb4-af45dc90f810 | -16.5313 | -57.2468 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7d7dd8c4-08bd-3c5b-ae52-607f226f43a9 | -16.52785 | -57.24618 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ee562f2e-d3bd-3098-8c56-3d759d3653f3 | -16.52719 | -57.25012 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3ba90bf8-2d0a-3ed1-88a4-f4cfb08dbce0 | -16.52652 | -57.25407 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a4fc39f8-4fd6-3f86-a767-0148d4d42f84 | -16.52374 | -57.2495 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 7a520cde-ce22-3265-9695-afe4ddb0122d | -16.50103 | -57.25759 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f87e3ab8-723f-3f27-886a-816b7104b755 | -16.49931 | -57.25397 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f1d0d44e-2890-327e-bcfd-83879d47f327 | -16.49586 | -57.25336 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4e4bcb15-29dd-32ea-8af6-9cd67220084c | -16.49092 | -57.24028 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3dad1862-d9b2-325b-a1c4-056e36f140a8 | -16.49027 | -57.24422 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5009834e-d2d3-3d72-af08-8f300029d3b7 | -16.48682 | -57.2436 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 75477dab-bfcb-3fb6-961e-8288619a5405 | -16.48616 | -57.24755 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f46ae1bf-7d5c-35b4-a4d9-a7bbe0670979 | -16.56106 | -57.47293 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 85dd13a1-c239-3177-85d5-edb85a3382d0 | -16.54612 | -57.41261 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3ef0549a-4da1-3813-bbf5-e669d10df232 | -16.53506 | -57.73809 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f9ebe68d-a85c-30a6-89d7-72edff90cded | -16.53434 | -57.74221 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 47f8d9b8-451e-3a64-a71f-b0ccf5c63c0d | -16.53225 | -57.73333 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d9fe32b4-6686-3651-abf9-c0c8f53db77f | -16.52945 | -57.72859 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| b2f13be0-05da-30c4-b41f-6f2a1bb30cb2 | -16.52881 | -57.72975 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| d7950408-68bc-3596-9d04-5a6df9d9b2eb | -16.52873 | -57.73273 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| aab86e4d-235f-32e8-a23c-1a45331c06f6 | -16.52811 | -57.73389 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 7a0a7ad8-b3c8-3760-aaca-6beb9eea7b0e | -16.52802 | -57.73686 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 6d4e39cf-e64f-37fc-8628-40ca3742774d | -16.52742 | -57.73803 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 576c1e7a-5081-3677-8453-3fede03fec8b | -16.52598 | -57.72502 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| fa990bcf-6aad-3142-908c-afc20602c1da | -16.52592 | -57.72799 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| ddbd1b83-961a-393a-b54f-1decd1565276 | -16.52529 | -57.72914 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| a5bc96af-9414-3fc9-95f2-1046c6d7fe0e | -16.52521 | -57.73212 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 65bdbe03-0100-3b9b-8262-f47c93fe434b | -16.52459 | -57.73328 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 2946f0c4-f6fc-35bb-820b-4f889f7b161b | -16.52449 | -57.73624 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| f72d4698-b2f2-30e9-bab5-3d1fb3b620b2 | -16.5239 | -57.73741 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| a3c79685-e662-3be1-8782-ea83ec918fd0 | -16.52378 | -57.74036 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 23033548-f245-3e08-a55a-80c4d03df870 | -16.5232 | -57.74154 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c01de397-a8bd-33bc-959b-7c53a5242965 | -16.52306 | -57.74449 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| fb006c31-69ae-37e4-be65-44d604b1115a | -17.84462 | -57.6857 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 789de172-0517-3968-8ee6-5da7c7baf0e4 | -16.52251 | -57.74567 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| fd19c473-db9e-3287-88c2-379091415c43 | -16.52246 | -57.72441 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 753d8a72-c548-3a30-b845-e262520ae37a | -16.52177 | -57.72853 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| fbb0ee99-49ac-3506-aceb-04dbc5ad49c9 | -16.52107 | -57.73266 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5f87c26b-7b3a-300d-a8b6-96066f9a6584 | -16.52038 | -57.73679 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 85a2fe0c-f511-3e4f-bd07-df7fd3cc108a | -16.51969 | -57.7409 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| d37c9921-7fb1-335b-9d38-95b2c81b09b8 | -16.51899 | -57.74502 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 7dc499a6-3ceb-3eca-b9c9-7206fe695d4a | -16.51895 | -57.72376 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5bb1a891-232f-3ec8-a03d-d28acd5b28c9 | -16.51825 | -57.7279 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |


[Clique aqui para ver as próximas entradas](README101.md)
