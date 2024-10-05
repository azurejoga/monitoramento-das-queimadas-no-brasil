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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a8382a0-c911-3e23-9155-9a2fede74203 | -11.07862 | -54.77531 | 2024-10-05 04:38:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe9eecee-23c1-3bd6-8498-eaf8c5590e28 | -11.07782 | -54.78012 | 2024-10-05 04:38:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ea817f5-9485-31fc-9d0b-b92d909d2e02 | -11.07701 | -54.78495 | 2024-10-05 04:38:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 020519eb-800c-3c38-8bf4-2813477ebbb2 | -11.0764 | -54.77753 | 2024-10-05 04:38:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cd05ed5-fc0c-3c61-9119-a2059dc88b13 | -11.07556 | -54.78234 | 2024-10-05 04:38:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 487afd11-f8be-324f-8593-12bf1339c867 | -11.0326 | -53.99323 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03e5c507-0e68-3868-81ca-8e67d0e7439f | -10.99975 | -54.25388 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb4f7fa7-f6bc-310a-8fb8-9879bde76463 | -10.99602 | -54.2532 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b51fff95-348e-3838-83cb-8d303fe38dff | -10.97585 | -54.02106 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aec6630b-08ff-34fe-9314-df72e2fd2177 | -10.97366 | -54.01148 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d0a9490-7364-30f9-a4b6-eec42e2e7ff6 | -10.97291 | -54.01594 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0247af72-24c3-3b33-b934-291ac006efe2 | -10.97217 | -54.0204 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e90ac49-99bb-3b19-8e92-c1f0ed7fa4c3 | -10.96849 | -54.01974 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a6c5caf-2008-34fd-a7b5-05c3eecf3447 | -10.93028 | -54.24806 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 958a088d-89bf-330b-980b-1780650de94d | -11.88752 | -54.80983 | 2024-10-05 04:38:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 728f31d7-6ae1-3df9-ad33-8ed2687122c1 | -12.47137 | -54.18182 | 2024-10-05 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 528dd997-b189-3b0a-8288-c123aa9079ab | -12.46846 | -54.17685 | 2024-10-05 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef3d7e80-28a6-3c9f-ae67-4894e7181106 | -12.46773 | -54.18117 | 2024-10-05 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22359a13-f5bf-34ac-9ddf-eb50198d899c | -12.467 | -54.1855 | 2024-10-05 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb0a1a5e-2d9f-3344-8e70-50a8622edd9d | -12.46482 | -54.17621 | 2024-10-05 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50aadc3f-0f93-35d0-a367-7ea4a90b3aba | -12.46409 | -54.18053 | 2024-10-05 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c9f3541-82aa-3357-8e4b-2ed1de0662c9 | -12.46336 | -54.18486 | 2024-10-05 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 697b8dbe-b033-3ce1-b3fe-edd7a76f38cd | -12.46044 | -54.17989 | 2024-10-05 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38100105-7d31-39fd-96d9-eab96b8dc167 | -6.87085 | -55.12055 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5df6b7e4-7d5f-30c6-ac80-3eb45865909b | -6.76721 | -54.9894 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63599840-d3f2-32f9-99a0-e4db59256336 | -6.67171 | -55.37564 | 2024-10-05 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22e58fff-bc8c-373e-ba59-0bdd00ac9eed | -6.58255 | -55.39108 | 2024-10-05 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17f50e2e-a8ec-3c89-8a7f-91a3cc3712b9 | -7.95316 | -54.78851 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb63dc12-45f1-3fe7-9dbb-cbc8adc18057 | -7.94974 | -54.78429 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9be1921d-f0c2-3db3-8ff6-2079c2841a6c | -7.94914 | -54.78782 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56682280-fa0c-3c1f-a65c-8b8dc9dd1743 | -7.94853 | -54.79136 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d139690a-3b7a-3854-97f6-846cf68ede04 | -7.94572 | -54.7836 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b8b536f-0951-350c-b0cd-3285c992a629 | -7.94511 | -54.78713 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45a3f66c-428a-3518-be62-7e5775735d68 | -7.94472 | -54.76531 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b318648-02fe-3cc1-a5bc-4bb2baf65996 | -7.9407 | -54.76462 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1893d5e-f9dd-3455-9b18-5e53539658dd | -7.9082 | -54.75547 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 755b2742-213b-3ee9-9a21-b573f255f389 | -7.90761 | -54.75899 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0fbc1eee-8d11-3f39-a209-176ab77d861f | -7.90477 | -54.75124 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a76adc73-6151-3232-a10c-92096e383358 | -7.90418 | -54.75475 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fdd056ec-2f2c-3dcd-9c8f-247e6b86f2c3 | -7.90359 | -54.75827 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cc445d2-d770-32fe-8b75-6f382a924126 | -7.903 | -54.7618 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abfc6e6b-6210-399c-81a2-f946a5e3ee81 | -7.90241 | -54.76535 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8eda6aca-abcd-3f31-a3aa-ebc95555c0ae | -7.90075 | -54.75054 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77ccef29-a46d-3db0-8059-cdc0f417e4bd | -7.90016 | -54.75406 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b74057d2-9671-32fc-bbfb-e351cfd8ca68 | -7.89898 | -54.7611 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 030bdf3a-3e02-3568-8bb2-be32ff6d7a80 | -7.89733 | -54.74629 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6711efa6-55ab-3c17-b31b-3d6de8e9dcff | -7.89674 | -54.74983 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 090d9788-8d3f-359e-9bca-e3c55bb0e20e | -7.89614 | -54.75338 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e3914b2-731e-3339-b345-ac582404d1b8 | -7.89496 | -54.7604 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9655825-d982-3eff-834f-f1f53ee01538 | -7.89332 | -54.74556 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79b137d6-212f-347d-8254-9cf15909fe9e | -7.89272 | -54.7491 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5de4ecfa-ba7b-343e-b1df-6fef403f5419 | -7.88322 | -54.88001 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42f0f8e3-9e68-36c4-89f6-df7d9ad631ba | -7.87917 | -54.8793 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0613f53f-8ce9-3278-b7e3-59dbeb668d32 | -7.87857 | -54.88288 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5327b22-321b-35ee-80d1-18cfc580cb9d | -7.87797 | -54.88647 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 822efff7-8575-3019-92aa-a0771e1598f4 | -7.87572 | -54.875 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 692533c0-16b8-3cd2-914e-0da725a9b2c6 | -7.87512 | -54.8786 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89daae68-0843-33fb-bcdf-019b3d3b8c41 | -7.87452 | -54.88219 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fdc3401-7b4c-358e-9396-879ec24ee818 | -7.87392 | -54.88576 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e76662a-a5c2-318e-bcf5-0af3c181b26c | -7.87228 | -54.87069 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6ddeaaf-a6e6-3c8e-92a3-5d3f9b40e426 | -7.87167 | -54.8743 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46c65033-2151-3b6b-97ad-516cf431b39b | -8.5133 | -55.15603 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02a661f3-0c27-31cc-827f-41432f32ed9d | -8.51269 | -55.15968 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccbab10e-5505-3ce2-965f-428f2346b478 | -8.51253 | -55.15535 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 825b16ee-7a76-3646-bf31-16e24f0279ac | -8.51189 | -55.159 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6530706e-278c-3d81-a42d-0d18bec9aeb7 | -8.50921 | -55.15533 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbbab79c-9f98-3943-9dc7-1c90a2fdafe8 | -8.5086 | -55.159 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01e7cc4e-50aa-3bbd-8171-a72767bf71f1 | -8.44628 | -55.45397 | 2024-10-05 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28ca8440-a940-3a9e-8a43-dec7194cfe9c | -8.44562 | -55.45786 | 2024-10-05 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03ece50c-cb24-376d-9608-52a9fc82dc50 | -8.27477 | -55.10853 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 341342f4-d3e9-38f9-be85-f0d3e85578e2 | -8.19182 | -55.17382 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7224cef2-ada0-3f7c-8adb-157d3381e588 | -8.18224 | -55.21441 | 2024-10-05 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1d4cee3-3881-3660-a6a8-6f93099e60ef | -8.18059 | -55.214 | 2024-10-05 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ada8d47-204e-3c2e-afc4-af4707d51450 | -8.11483 | -55.08806 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f14a9f69-6987-394f-934a-7f526ad4d43e | -10.37717 | -55.6383 | 2024-10-05 04:38:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca2da6d0-54ee-3665-8a05-a011576ed8b5 | -10.37372 | -55.63382 | 2024-10-05 04:38:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4bab6612-29f5-343e-b70e-6ae51f8f4cfb | -11.91994 | -56.94492 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17b98e31-374c-39b6-adcd-dc98984d4193 | -11.91638 | -56.93979 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c78656f8-1465-354a-b55f-55c5fb792f6d | -11.91561 | -56.94404 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f518f57-028b-365d-813e-9636d9394f19 | -11.91282 | -56.93473 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 310acfb4-bfc5-3aad-bc5c-23f72c87b0ae | -11.91205 | -56.93896 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd98601d-ca19-3f16-ab9d-6ab0eba78626 | -11.91127 | -56.94319 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18bbd4e7-a1da-3885-b8ed-ecef2d35c523 | -11.9105 | -56.94743 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a24e1aca-2737-3565-b1e9-229aff9de4da | -11.9077 | -56.93817 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9bb39d11-a863-3214-af1e-bfdf8ef798a4 | -11.90693 | -56.94239 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45c01ede-1bc9-3414-826b-e1116df02b36 | -11.90616 | -56.9466 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80e17edc-49fc-34f0-b3a7-88d57be43956 | -11.90539 | -56.9508 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1701397a-43f0-3724-9367-f0ac4d40e9e7 | -11.90259 | -56.94158 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa456798-3df7-3bb6-9c71-68839eaa86a0 | -11.90149 | -56.94318 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d4501aa-4b44-3ad0-9d2b-8d6528c61015 | -11.89979 | -56.93236 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8896dfcb-1f2a-3eb2-ab56-777aa97e5e8e | -11.89902 | -56.93655 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cef4cbc-708a-3c63-bdf6-23a8d8393457 | -11.89862 | -56.93394 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 09a12452-56b2-3552-81fe-2c7a3cda616b | -11.89825 | -56.94074 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cdc6fc87-1be9-3d2e-8bb9-61d931dd2124 | -11.89789 | -56.93814 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d274b7fb-297b-3ba4-881d-bcd0da684425 | -11.89715 | -56.94234 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0a6649e-1707-3036-a940-bbdfad4eb104 | -11.89671 | -56.94915 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7957a68-7de5-361b-a7a8-89c09fddb0d3 | -11.89641 | -56.94655 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e50c6fb-9f31-34c7-bf7c-fddd178ac701 | -11.89566 | -56.95078 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 13af490e-4443-377f-b4c9-f2a2d34b673e | -11.89545 | -56.93153 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f997b57e-a315-3ba2-8543-7a53665b1f03 | -11.89468 | -56.93572 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README112.md)
