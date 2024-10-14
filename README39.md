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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a92fadd-9061-378f-9569-2e93004b14fc | -6.07036 | -42.40448 | 2024-10-14 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0de7e321-a17e-3aef-b648-6dfdeca8dbb0 | -6.04266 | -43.34731 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bf417415-7fdb-399d-b9a4-2f972e96d1be | -6.03931 | -43.3468 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fb4afac7-3402-3756-bfd0-7d560a0d140b | -6.03596 | -43.34627 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 946d2128-dbc0-3166-a797-ace96a444ab0 | -6.0333 | -43.38601 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4787b2a3-0601-37ad-969d-83c434f6d4c4 | -5.96099 | -43.19257 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f2bd64ff-6315-3294-bcd4-e72361896a12 | -5.95763 | -43.19206 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5158c4cf-edac-3052-8beb-85b988adfe46 | -7.32423 | -42.227 | 2024-10-14 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2a3adb05-832f-32a8-921e-63a55cc07039 | -5.95427 | -43.19154 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7e14cfa1-3434-3624-b78e-058f2075a01e | -5.95262 | -43.20229 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 72c472dd-7fbf-31f7-929f-6a064ded15c2 | -5.87844 | -42.56047 | 2024-10-14 04:19:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 05acc0b0-7736-31eb-b50d-16f144b2d2ba | -5.80023 | -43.00203 | 2024-10-14 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| be7b8cb3-8054-31d9-8cf8-0e3d10b3cf19 | -5.7738 | -42.78298 | 2024-10-14 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ba5d452a-0ac4-30cc-aa6f-42b2e3bb5bcb | -5.76588 | -42.78924 | 2024-10-14 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 777c4470-22b5-3034-8e3f-a88e9c7970fb | -5.76305 | -42.78506 | 2024-10-14 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 20a62b87-7e0c-3c3b-909d-12bdbad7af3c | -5.76249 | -42.78873 | 2024-10-14 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4bb24024-0752-3bda-99ca-0f11882445eb | -5.33539 | -43.0159 | 2024-10-14 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7990f465-9a0e-39c6-b5c9-18b875903531 | -5.33271 | -42.5281 | 2024-10-14 04:19:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| eddb3e72-0d37-3eac-8c34-ef5d14eac1e2 | -5.23201 | -42.4748 | 2024-10-14 04:19:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 36cfaba2-259c-31aa-8bb8-1487654270f8 | -5.22859 | -42.47432 | 2024-10-14 04:19:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d9547c31-ba22-3fc7-b491-cde5f320e4dc | -5.22631 | -42.4664 | 2024-10-14 04:19:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 54f8111d-6c28-30fd-8e77-8f76c4deef1a | -5.22517 | -42.47381 | 2024-10-14 04:19:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 40c271c0-50eb-3cae-a391-607211e6df9e | -5.22461 | -42.4775 | 2024-10-14 04:19:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 40b01458-75b0-3519-819d-8312f2e40e1e | -5.22289 | -42.46587 | 2024-10-14 04:19:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| af9a86da-ca34-3545-8cb6-c66873660b7f | -5.22232 | -42.4696 | 2024-10-14 04:19:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6c861e6e-7685-3199-86ab-d93a085d11f9 | -5.22176 | -42.4733 | 2024-10-14 04:19:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c8ae5ba1-1a7e-39d2-add0-256a20d1290e | -5.22005 | -42.46161 | 2024-10-14 04:19:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 846e152a-1b2b-3359-9af2-03f33b75a2cd | -5.21948 | -42.46534 | 2024-10-14 04:19:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 962c174c-d738-35cc-a5df-b48df15370a6 | -7.43788 | -43.00653 | 2024-10-14 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7c24a54d-a8c8-3ce6-b687-116de0f62550 | -7.43672 | -42.99122 | 2024-10-14 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f401e9f7-ce02-3290-a924-cc75418af0f9 | -7.43616 | -42.99492 | 2024-10-14 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| aedf0bff-8f80-3377-9160-c511669faac0 | -7.43391 | -43.00969 | 2024-10-14 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6f09f64c-826f-3acf-a52e-d4511e65f61d | -7.42764 | -43.00499 | 2024-10-14 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1034bfd7-8789-3394-b47c-3b883dfcbbf9 | -7.42708 | -43.00866 | 2024-10-14 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 62b6a4b7-9e27-32e3-ba49-c31218150e8d | -7.42653 | -43.01233 | 2024-10-14 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0bbcb2eb-8c62-330c-afb9-74649168b9cf | -7.42648 | -42.98967 | 2024-10-14 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 572ee920-ad46-33f6-86c0-01aacf8c0826 | -7.42535 | -42.99707 | 2024-10-14 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 750c6523-1cd5-314a-8dda-bf0606450826 | -7.42479 | -43.00077 | 2024-10-14 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b131cfbb-6270-3ca6-811e-722a94b54b14 | -7.42423 | -43.00446 | 2024-10-14 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 095d2f67-cd7f-3270-bfa6-685884d2401e | -7.32072 | -42.22645 | 2024-10-14 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a3ea7a5e-240b-333b-ac66-c871b98772f4 | -7.29201 | -42.22607 | 2024-10-14 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3fc7d4a4-e5ec-3fe6-8dd2-d7abf67a7043 | -7.21877 | -42.30071 | 2024-10-14 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 110c7f7c-dc2e-3c45-a3f0-4dbb62bd43e6 | -7.21818 | -42.30459 | 2024-10-14 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9903ec7d-2ac8-3c7d-88a3-8f1dedb95775 | -7.20831 | -42.27497 | 2024-10-14 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1d6ebfb9-6640-3b7a-bfcd-1024b97afe17 | -7.20653 | -42.28686 | 2024-10-14 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2dea9e92-d25d-3f64-b824-50fa81343c9b | -7.20594 | -42.29076 | 2024-10-14 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| bb37e60e-e51a-34c3-9550-682777d95500 | -7.20421 | -42.27839 | 2024-10-14 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6821cd03-a8d9-3157-9beb-f9ffe239b5df | -7.20362 | -42.28235 | 2024-10-14 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9e569522-bd36-3144-a454-8587968acbbd | -7.20303 | -42.28629 | 2024-10-14 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1d7adb5a-4652-38af-a05e-b85a32625eb2 | -7.20244 | -42.29019 | 2024-10-14 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 92584966-be5e-3f8e-9bba-7a580c9d1c53 | -7.19954 | -42.28568 | 2024-10-14 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7bd6952e-f463-3ff5-8d69-aa9b30301e0c | -7.17603 | -42.62976 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 67f8ec49-5d5b-357d-b785-dcda617aeefd | -7.17545 | -42.63357 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6d9bf6fa-1c44-30e9-bb22-1160be9dd7ba | -7.17487 | -42.63737 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8356677f-2ef5-3d1d-ade6-401df078e8c3 | -7.17429 | -42.64118 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9683ccd2-dc39-3aa2-a363-697777bde017 | -7.17317 | -42.60207 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e5eea035-5e8f-374e-8c97-b8ad4d53ea84 | -7.17259 | -42.60589 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 237a4ede-9d0a-3787-b25a-33b24724d270 | -7.17258 | -42.62923 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c55209dc-4a6c-321d-a543-c34cb5d3dca8 | -7.1703 | -42.5977 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 95c40bd3-7c9c-3f69-b1d8-a6ead7b12e60 | -7.16969 | -42.64822 | 2024-10-14 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cb36e3a8-18c0-3379-a460-340f1009dcda | -7.16742 | -42.59333 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9cb9779b-f120-33f6-8db4-a0c2929da0f3 | -7.16624 | -42.64769 | 2024-10-14 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 07e0aa51-25e0-301d-8475-b986cbdd7f6e | -7.1628 | -42.64714 | 2024-10-14 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 65f7620d-1692-3551-bdc2-aa183a1b0f0d | -7.16051 | -42.59226 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0cd393b7-048c-3111-a933-0db2f5d56e5f | -7.15705 | -42.59171 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 58a8e2ef-07b7-37aa-83e8-ea205598b474 | -7.14384 | -42.65584 | 2024-10-14 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b5ab8d4b-1c36-3e88-b278-dad516970865 | -7.14327 | -42.65962 | 2024-10-14 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2d8c1059-bad4-32d2-a0ec-c9252ab61a18 | -7.09344 | -43.01142 | 2024-10-14 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4671d143-81b2-3efc-b52f-b050718ae610 | -7.09004 | -43.0109 | 2024-10-14 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0b9c70b4-37b5-38b6-8b4b-6ebc2871d896 | -7.08948 | -43.0146 | 2024-10-14 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 35eb0a26-ae33-3b52-9287-cff39600ad04 | -7.08872 | -42.65202 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5a5d8f77-8c55-3298-923b-af411f306322 | -7.08814 | -42.6558 | 2024-10-14 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| afe19438-a16c-3c4c-8354-efdfd51e79a0 | -7.08756 | -42.65956 | 2024-10-14 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b9619a38-899a-305c-b2c3-09cc6afcb3a1 | -7.08608 | -43.01407 | 2024-10-14 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f524aef0-afeb-3f5e-8b75-fdd7e749027a | -7.08412 | -42.65904 | 2024-10-14 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 701c0040-a90b-3e02-bcba-e679334dc660 | -7.08357 | -42.6396 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9b192c54-ba2d-32e9-bb46-6d85197a47ff | -7.08067 | -42.65852 | 2024-10-14 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f6550d01-d813-3adf-8f5c-8baed079f3ad | -7.08012 | -42.63908 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cf01c202-82c3-35d8-a381-bbb7521a57fd | -7.0801 | -42.66228 | 2024-10-14 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| df271064-8250-3481-b833-7199a9f0b805 | -7.07667 | -42.63853 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a469f568-7f8f-3cb4-a144-d11a77e02878 | -7.07378 | -42.65747 | 2024-10-14 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6bdc195c-42ff-385c-9b12-eaf984165dd1 | -7.07091 | -42.65316 | 2024-10-14 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 608bb8a8-85c5-38a8-94e8-166a3ae36883 | -7.07034 | -42.65694 | 2024-10-14 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ccbb5789-d31e-30a2-a66b-f2753f7911eb | -7.06461 | -42.64826 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 16ddd10f-2534-32f9-b07a-3962706682d8 | -6.94446 | -42.19697 | 2024-10-14 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 132b255f-1660-346a-9f94-a8612503f42f | -6.81654 | -42.78028 | 2024-10-14 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e74f2d55-ad83-374d-ac04-6ce061af98fa | -6.81653 | -42.75731 | 2024-10-14 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f60919cf-f3f1-3490-8f17-f52df7484ded | -6.8131 | -42.75679 | 2024-10-14 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b314f592-0da5-3396-b91f-1e82d6e9d911 | -6.66378 | -42.23708 | 2024-10-14 04:19:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e6217423-bb73-3d74-89c0-f3163a2b583d | -6.66158 | -42.08425 | 2024-10-14 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| edb5ddce-d74b-3840-a1ce-71935a38eed3 | -6.66028 | -42.2366 | 2024-10-14 04:19:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 760c861d-0a71-3a55-9098-8bba6af21a61 | -6.53347 | -43.38703 | 2024-10-14 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 15a76935-af77-3930-a49b-81d7321f334d | -6.53292 | -43.39062 | 2024-10-14 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2fe83cce-6897-3c4e-9307-eeeca66286b5 | -6.52733 | -43.38235 | 2024-10-14 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| aa891d12-e9f0-3105-8505-650b01bf831a | -6.72747 | -43.56188 | 2024-10-14 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f7801153-fde6-3363-894f-6fc0810e6b8d | -6.70454 | -43.0283 | 2024-10-14 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f666205c-6e9d-37e5-a381-dad6ec406a3f | -6.52486 | -43.01605 | 2024-10-14 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f5473b3-5ad7-342a-837b-4368e1b90be0 | -6.49874 | -43.34506 | 2024-10-14 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ba59ab2a-1b42-3e6a-b0ee-5f17877a91fb | -6.4971 | -43.35572 | 2024-10-14 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 55b83be7-eafb-32dc-8e9f-14c89a669a37 | -6.49594 | -43.34091 | 2024-10-14 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README40.md)
