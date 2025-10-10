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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 895bdacb-f624-38c4-8b53-74010a092136 | -8.52749 | -46.16277 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb21306e-7c9f-35a7-92c6-88026b86402e | -7.71027 | -42.37665 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c3f5ceee-9448-307e-8075-93bdb043fa2f | -6.66792 | -47.75214 | 2025-10-10 04:00:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f8d67c5-8117-3df7-8711-f1a871d23756 | -7.25928 | -44.09829 | 2025-10-10 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 135d1ac3-3e98-3df9-a972-c97f823e6b42 | -4.39425 | -44.08667 | 2025-10-10 04:00:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4f6c8cc6-59e5-328f-9a95-f181f727530c | -8.514 | -46.13977 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49afc889-1e3d-3ecc-bb4c-aaaf7d5f0c9e | -5.4674 | -44.05799 | 2025-10-10 04:00:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c2899ee-babf-3ff2-9bf3-17fba2b62173 | -4.65282 | -43.20435 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 71d5b6cb-2245-3208-aba7-df8cc1ac187e | -7.54411 | -44.60615 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 12e2613e-248f-3b55-9565-774465b0b2db | -8.22289 | -44.1396 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c46e804-e255-3e59-bbbd-8569ba2fd00d | -7.49792 | -42.74851 | 2025-10-10 04:00:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a49e2c31-a546-3209-9f9a-105ef86142d2 | -8.36062 | -41.38968 | 2025-10-10 04:00:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 80d93951-360c-3d6c-9ed6-def9d8e187ea | -7.49558 | -43.11067 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 03059316-1754-3278-9f08-e89630255943 | -6.81937 | -42.79708 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d7d3e209-95ee-3555-9130-1f618901dd93 | -7.82396 | -44.13439 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bc8c6eb2-465b-3c05-90c4-dc7a2dc31869 | -7.70271 | -42.37931 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9e8f80e1-1b41-3cbd-aea8-899ad4b77132 | -7.73767 | -42.41586 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f0807530-91bb-36dc-b240-cb61fde699ec | -7.2498 | -49.51833 | 2025-10-10 04:00:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcc3b364-b6f5-36c5-92e4-f4caba20b8f2 | -4.65585 | -43.20265 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 11280ae1-b83f-38a5-8e55-9069a5158bc5 | -7.79425 | -44.19557 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99018a77-17f1-3e1f-b3b8-ef5ba2f326be | -6.75051 | -42.84574 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 88fb313d-685c-3502-861b-4c6e9450674b | -7.56057 | -44.29303 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6eea34de-f5fc-38fe-b33f-0012dcf3fec6 | -8.20824 | -43.35703 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| adfb3eb5-7f35-3646-b773-913424c484a6 | -7.06753 | -46.85291 | 2025-10-10 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a52cac39-8f3c-3644-9aad-9d8da310d302 | -6.81647 | -42.79239 | 2025-10-10 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6b8d7d3b-481d-3d35-910d-56d2b0d4b1c5 | -8.52608 | -46.17088 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8a27e1e-60dd-3f4b-8a6c-69a1100f1410 | -8.50829 | -46.17226 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a99805a8-7144-37de-ad76-6ead095fb9a3 | -4.65211 | -43.20203 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6648b732-acdf-3d5b-8770-31d3ad7ba8b9 | -7.79735 | -42.42174 | 2025-10-10 04:00:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7a3ac5bd-30af-3708-bbc4-abcec75dd764 | -7.54967 | -44.59688 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2640bea9-05d6-35ca-b3f8-a995ee61e228 | -7.59997 | -44.0346 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8b51838-2bbf-3687-87a7-5f9c4927b572 | -4.8481 | -42.77187 | 2025-10-10 04:00:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 449e0ae4-621e-378f-bac2-23c1c4d27ca5 | -4.49332 | -45.87262 | 2025-10-10 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf4784ad-0fc8-30db-b10d-2298fab6d8c3 | -9.90564 | -43.55986 | 2025-10-10 04:00:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e14a69d-870e-34e4-8226-8a7886307f8c | -7.26307 | -44.09903 | 2025-10-10 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ddf6e29-67cc-30cd-8861-e482ed18db32 | -5.90653 | -42.85571 | 2025-10-10 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2ebd6550-7b63-3b52-b18e-97e945130682 | -8.07016 | -42.94859 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7ed8803a-1b54-3951-a936-a523a0919718 | -5.79465 | -45.11052 | 2025-10-10 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2002d74-3346-31a9-b091-b46a8bd22891 | -5.54561 | -45.37987 | 2025-10-10 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9ddd745-cc56-338b-80d7-c36f063e3871 | -7.76933 | -44.04391 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89407a1e-33fa-39b8-9cb3-1fe82d3785c6 | -6.58313 | -44.62365 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 63602de5-96bb-372c-986d-d1920ba0559a | -6.98126 | -47.30256 | 2025-10-10 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcbf98bb-601e-37b6-95cf-63e6de6871e7 | -6.74917 | -42.85401 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d6ab9776-97ce-32c4-b7c8-8f11265d15c5 | -7.25973 | -44.91184 | 2025-10-10 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b66e6f6e-591e-3f6c-9ec7-9151c54a2503 | -6.75318 | -42.82924 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 668511ad-2beb-3444-b48a-4f045cb26556 | -7.76869 | -44.04572 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f54e6923-9164-3ea5-a6a2-2133960f6199 | -8.2078 | -43.3756 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3f7fa27f-67dc-39da-89ee-ab1f45f42275 | -7.69862 | -42.3826 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6927989e-a505-3909-bac0-411954a0ffca | -7.68222 | -42.39579 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| cc47c08c-35bb-30b0-aeae-c09bdca2017d | -8.06729 | -42.94394 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 21089744-d626-3cef-b92d-d44be7291223 | -7.09719 | -41.08863 | 2025-10-10 04:00:00 | NOAA-20 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b31c5c38-044b-386c-9f94-f025837d90c0 | -4.64983 | -43.1992 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9c99f23c-3a96-3260-b01e-3b6d6ba02fae | -7.6247 | -43.05455 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e151fd84-06d4-3d08-9efd-1e115ea68297 | -4.64837 | -43.20142 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 806902f8-0290-3575-844e-3a8f1017b274 | -7.54494 | -44.6012 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| ebdffe30-f15d-3037-a62f-6664616b3d76 | -6.75184 | -42.83751 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8688ec98-a616-369d-99bc-d984b00d5d2e | -7.80046 | -46.0238 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b160a85a-b6b8-34e0-96be-617e5c108431 | -7.70965 | -42.38046 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 475df893-4d8a-3e51-b2fd-c4658da37ba8 | -6.73591 | -42.21916 | 2025-10-10 04:00:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 472e7fd8-3197-3d49-8ca0-dc24eb0da225 | -4.49778 | -45.87335 | 2025-10-10 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b4db242-4854-3715-b54a-5f7802e18b76 | -7.79883 | -44.19151 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51b3aefb-16d5-3167-874b-dc20137d7bc7 | -7.77366 | -42.41388 | 2025-10-10 04:00:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6683e7a2-9769-3373-890c-9e5499b6dfe8 | -8.0056 | -44.46665 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5a2639bf-3483-33f5-8341-7baea2bdcda5 | -5.91014 | -42.85637 | 2025-10-10 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 64e18d26-f3a5-3af5-80ad-04d6e104087e | -4.49706 | -45.87774 | 2025-10-10 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3079a52b-006c-3226-91fe-6aa26bc7582b | -6.45613 | -44.57235 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3c30b54-43c9-3417-ac66-3b07585bfa93 | -6.23422 | -43.6132 | 2025-10-10 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc1c6749-215b-3de6-b24e-b866dc9dde5f | -7.49268 | -43.10596 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4334ac32-e1af-3886-a433-f3f0f012b908 | -7.79262 | -46.01834 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9848edb7-c3a3-35bc-a165-46d8a541406b | -6.75476 | -42.84219 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7740f3fa-454d-3cc2-bf83-a4dbe03c3965 | -8.17273 | -43.31826 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f267fb96-dd95-3f9c-bead-0ae8ae3275d7 | -6.64941 | -40.87522 | 2025-10-10 04:00:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9b417b77-baa7-3e70-9e82-a1f76fc88fe4 | -7.33372 | -47.81606 | 2025-10-10 04:00:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d5e9006-c5a7-3a7a-95af-41e2c4389693 | -7.5254 | -42.97615 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8481fb47-2678-3a96-9de3-c537bc589705 | -8.00622 | -43.75913 | 2025-10-10 04:00:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 614ce13f-cb8d-3b39-a6ad-e14afee7c37c | -6.01437 | -45.89699 | 2025-10-10 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c8086e8-b978-3b74-a4e0-2f599f2d368b | -6.58001 | -44.62686 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 29198d4e-0d7c-3338-ab09-652c3ed93b2a | -8.19005 | -43.32547 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d6a98cad-5c68-34ca-812e-241c2508038a | -4.55406 | -46.69098 | 2025-10-10 04:00:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 86a939a1-cdc6-37b2-85f1-8fd0f1b77929 | -8.50832 | -46.14717 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| f406a711-8a68-3caf-9a22-0465e67f28c0 | -7.40181 | -45.92058 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6ddae78-728f-3e71-955e-ad36826352ee | -6.5814 | -44.63377 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 23daa885-1afa-3d6d-b16f-dfcfccd9ed3a | -4.68381 | -45.83702 | 2025-10-10 04:00:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0f8b6dc-af90-3d44-beb3-68900bd9ff91 | -6.65705 | -41.9907 | 2025-10-10 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e26a9f52-2223-392f-9b73-5ac7358e5011 | -8.44771 | -36.34119 | 2025-10-10 04:00:00 | NOAA-20 | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 03517676-22a9-3a2b-a76b-d8d56ac11996 | -4.68822 | -45.8379 | 2025-10-10 04:00:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd80639b-c9a6-3b56-82ed-f8d8d177354d | -4.81703 | -47.35062 | 2025-10-10 04:00:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d5186a6-cd96-3ddf-abcf-7c1cce4a78e4 | -5.05198 | -45.84939 | 2025-10-10 04:00:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f7329147-3364-32bd-b809-b45ee521ffd9 | -7.80188 | -41.6553 | 2025-10-10 04:00:00 | NOAA-20 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9a132ff4-e802-3cac-b7f4-548e795a9fe7 | -7.27765 | -41.96922 | 2025-10-10 04:00:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 06ae56b2-fc6a-3357-a212-2758d78e0ced | -8.20904 | -43.3743 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f77a178f-3ba0-3946-a79a-3c1db86471bb | -10.16949 | -44.59143 | 2025-10-10 04:00:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c8a86317-eb93-3e9c-9282-8c2a4a51db4b | -7.55673 | -44.29243 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9fcda5e-ccc6-3c0e-a203-032f441dc82f | -15.43125 | -44.28297 | 2025-10-10 04:02:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ae705634-7c2c-3e09-9dcd-d938cd87ea46 | -15.73537 | -43.9513 | 2025-10-10 04:02:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17af39a1-4989-31f8-b058-00440aee56a5 | -16.79823 | -49.08472 | 2025-10-10 04:02:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a23d991e-1687-3564-9d12-964f74fd45d7 | -13.29237 | -48.48767 | 2025-10-10 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc04f85f-06fe-3099-abd8-7c6ebd4d5bdc | -14.91548 | -42.219 | 2025-10-10 04:02:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 66e186f2-b330-32dc-b2aa-980f3a06e892 | -11.78222 | -45.04324 | 2025-10-10 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab325004-f49c-3c0c-9918-7ca30b9be713 | -15.82406 | -43.77843 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README26.md)
