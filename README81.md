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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2addb7b9-f97c-3489-9f28-6b84d81c4309 | -2.93552 | -54.36612 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24e8d7fa-2bc0-3781-8ada-8f10cad03acc | -2.88872 | -53.98898 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06434352-9fcf-32bb-9913-012073f9a49c | -2.88758 | -54.49378 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91a7819e-da68-3486-8719-d29dd4a11e46 | -2.8578 | -54.59614 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93a06b32-f542-3fe3-a5b9-61d7ba361e36 | -2.78928 | -54.02328 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 403974e2-9c8d-3939-b198-b6bf6f9a2242 | -2.78578 | -54.02274 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a956c1cb-6fc0-381d-9591-aa6dca09fdad | -2.78313 | -53.97034 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e71d1c8-1bd3-3ce6-808a-d68c4d406ef5 | -2.74165 | -54.1231 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef96c7a6-852d-3d41-a239-bf165cec6627 | -2.73816 | -54.12256 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dea4cbfc-a902-3452-8545-a7b1d3448804 | -2.57816 | -53.98428 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e2e2880-c9d7-3e77-a824-6e8d3cbb8b0a | -2.56803 | -54.02644 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ddc989a-9d9d-3993-b82e-445e909f0b45 | -2.56453 | -54.0259 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ab8e1b8-e132-3981-b104-6b8b3a903aba | -2.55994 | -54.00934 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 9ec1a675-aaeb-3880-b894-e64f537aa4b2 | -2.55934 | -54.01321 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d472177a-6922-329b-9058-6a2edd542c06 | -2.55644 | -54.0088 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a2b7a2c-0b87-330e-b459-a0fd8cca8bd0 | -2.54655 | -54.00331 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 401e547e-9445-30ca-a61b-12fbdb354a21 | -2.54306 | -54.00272 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1196c0a-00cb-3032-b110-492edda98fb3 | -2.49853 | -54.12993 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b20ad3cd-9c05-35f0-b52d-0f2379040a9f | -2.28158 | -53.7727 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdc7aa94-e62d-3fba-8d9f-c0fd45076dc6 | -2.28096 | -53.77665 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21380e5a-a1e8-3be5-83ca-3f767374dad1 | -2.27744 | -53.77611 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e56f9967-7d90-3b41-8ca0-df27c4f064a0 | -2.27391 | -53.77557 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 496427ac-d55a-36e0-89d3-b8f1bc0f8173 | -2.25363 | -53.71983 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26e8c45a-6d42-317b-b4bf-06df4cf790f8 | -2.24534 | -53.72668 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 431efe40-8029-35bb-81b7-b74416fe51ea | -2.15888 | -54.6273 | 2024-10-30 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c7919e1-cb1b-3655-ab26-6cb6f45d1685 | -4.50785 | -55.45855 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aaff9211-4d0d-38d4-82f0-4e5570e621ed | -4.50729 | -55.46217 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddb1d03f-8195-3f94-acf7-878da3516bca | -4.50504 | -55.45442 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcb53d1a-6bbd-3c5c-8e67-d190e94395e9 | -4.50448 | -55.45804 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03c98766-7069-352c-be6b-8e96fb75e743 | -4.48865 | -55.08298 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de61f36d-a936-3864-b9c8-8e098a2caed2 | -4.36377 | -55.21033 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc261c2f-dc40-3c08-82ac-9655d35e6772 | -4.34167 | -55.12855 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8935a4e3-ee09-37fa-a177-539c92f6fcea | -4.34111 | -55.13221 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 758fa06c-75cc-3bd3-8f67-2c6bf80feda8 | -4.27285 | -55.07351 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ffebd80-de46-39a6-b616-409ccfaa2ef4 | -4.26944 | -55.07299 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d01d12a-a370-3670-9d31-866f6e987982 | -4.20322 | -55.23099 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79d96dff-86e3-39ea-8fab-b6328a6fcfb2 | -4.14798 | -55.33361 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5341d6c-3731-321d-aa0b-e019617c8536 | -4.14742 | -55.3372 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 761c08ed-6782-3cf2-8e85-09583a4d6460 | -4.1446 | -55.3331 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56330921-a9bd-38fb-b7a9-f8c25e8f1611 | -4.14404 | -55.3367 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 632ce854-a9f7-3735-b496-6db95a030e5e | -4.1282 | -54.90001 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1cae251-afd5-3adb-94d1-5894df485ac4 | -4.03967 | -54.76857 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06bb185b-9baf-3d8c-acf9-4c13602ac740 | -4.02139 | -54.81916 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5172158-254e-394d-8208-330fcfbef8be | -4.02081 | -54.7999 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7385dbb-7239-3a76-bb02-b18ce525369e | -4.02025 | -54.80359 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b18d01f3-f66d-38e9-bf54-f9055cc9868b | -4.01968 | -54.80733 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15d6b846-b276-3aeb-bfb0-c996aa4b5115 | -4.01854 | -54.81483 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0142f26d-6e29-34ef-af55-003b971182fb | -4.01796 | -54.81863 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfa9bf8f-c0e1-38b1-aac3-88ac6995e8a4 | -4.01774 | -54.79995 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 070c4a4d-eac7-36df-aca1-588760490144 | -4.01716 | -54.80365 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 327a6ca8-acc9-3eea-8258-27fc645a64dd | -4.01682 | -54.80308 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd91a3cc-71cd-3a8d-bd87-ca5c6b70a903 | -4.01396 | -54.82185 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7e785ce-eecb-3051-9ac0-45aa083a2fdc | -3.95714 | -54.75999 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f5ae4be-8e8b-3632-a4b0-9c0cb27c0e2d | -3.95427 | -54.75574 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ff2ee04-aa3b-321c-be53-23c98104a29d | -3.9537 | -54.75946 | 2024-10-30 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9f29b89-1424-3d9b-b111-226f662842c9 | -4.10481 | -53.94017 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d116a749-3d74-38e4-9e69-0a0ecc8a4b7a | -4.10418 | -53.94429 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19100ecd-dddb-35cc-9697-6f60ef532186 | -4.10355 | -53.94834 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d453718-65fe-3bb2-8e49-b3aef7152bfd | -4.10293 | -53.95236 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d792f895-9a6b-3ea4-86e7-21fc2094eb39 | -4.10231 | -53.95644 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| acd578aa-953a-3cd4-b8ad-044abb729d18 | -4.1006 | -53.9438 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b45e794-27a6-3dd9-ac08-ae98c3c482f3 | -3.96759 | -54.14919 | 2024-10-30 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 130921f2-30a9-3975-9822-a0f01124a508 | -3.96406 | -54.14867 | 2024-10-30 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1096633-4b5e-360a-b5ae-cd544c841cab | -3.95422 | -54.00039 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3331bde3-f80d-3871-98d7-3e1d8c74c6ac | -3.87562 | -54.22849 | 2024-10-30 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f503978f-f034-336c-bc94-594e4abbd1fe | -3.69812 | -54.0666 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1af00a2-0392-377d-a586-32416f660d22 | -3.69776 | -54.06966 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 707002c7-4d9d-3aa5-8002-b542c9494172 | -3.68622 | -54.21672 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9621b890-4f47-3c7b-b045-955ead52b231 | -3.67434 | -54.31811 | 2024-10-30 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3eedd3ba-b392-3e42-a115-780990094ceb | -3.66855 | -54.30925 | 2024-10-30 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 183a190f-2d8f-38ca-85bf-cdd68b069858 | -3.66506 | -54.3087 | 2024-10-30 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02dd0fa6-0f6e-300f-81b8-2187bbf8f24a | -3.66446 | -54.31261 | 2024-10-30 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94fabc3b-cc3b-300c-9469-382bd2a32560 | -3.66157 | -54.30814 | 2024-10-30 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62dd0eb3-c293-3895-b42f-a098ef3023e5 | 1.04134 | -54.64675 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6f065d2-3072-3b31-95ed-bce70cb9423b | -2.11779 | -55.9089 | 2024-10-30 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b9322cc-c51d-3d68-8742-764a0e826b89 | -2.11683 | -55.80616 | 2024-10-30 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2339e2cb-92a9-3184-a8c1-58e0ecbd3730 | -2.11448 | -55.90838 | 2024-10-30 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5069855c-3839-3fbe-9db4-429db58f9319 | -2.07576 | -55.72185 | 2024-10-30 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b81bad6d-0f13-35e6-b660-4c30c5ccb5a3 | -2.02786 | -55.7676 | 2024-10-30 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0886fb38-7044-3bc8-8249-c83422ec57bc | -2.02732 | -55.77106 | 2024-10-30 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a04c5166-6e15-3ce2-a247-9ee860d225d5 | -2.02367 | -55.72821 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dea3d259-5105-337b-8d8e-bbb20189d687 | -1.9766 | -55.68192 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f970a388-b1a2-39f7-b03e-62246e26d737 | -1.93076 | -56.34431 | 2024-10-30 05:08:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7b087f88-6a03-35b3-8e11-f505229b2afe | -1.76668 | -55.69876 | 2024-10-30 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e420a4b5-9553-3d4b-a156-4e855ca10672 | -1.76541 | -55.6419 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa7f8213-2065-31ab-bf15-dbae224de4e8 | -1.76337 | -55.69826 | 2024-10-30 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7224eac-31a4-3515-823b-304560ad2987 | -1.7621 | -55.6414 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fc241ab-d49d-326b-960e-633220a301a4 | -1.75946 | -55.22661 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ba579ae-da5c-311e-b705-9f26937fe0ed | -1.75891 | -55.23012 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8dd94576-9413-3310-b25c-a7fde94e90e2 | -1.75884 | -55.66216 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8113c5f4-641f-3480-8adf-91615543c011 | -1.75878 | -55.64088 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eb68904b-6cda-3302-9135-0b420c53421a | -1.75656 | -56.19791 | 2024-10-30 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c10ef33-56f1-3f89-951d-d366e69ee3af | -1.75499 | -55.66511 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd6fbc14-1233-3139-86f4-274b9579561a | -1.75279 | -56.0458 | 2024-10-30 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9679dd97-8d9c-38fb-a290-b2390470dfec | -1.74861 | -54.96754 | 2024-10-30 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45ff4d52-139e-33a1-bbce-281ff178f0d6 | -1.74558 | -55.24967 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0ac2899-23fa-3892-8548-27f98ca77044 | -1.74525 | -54.96702 | 2024-10-30 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c312d47b-9a10-3ca6-b1bb-3e37c7dabab4 | -1.74502 | -55.25319 | 2024-10-30 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 749672f7-4095-348f-953d-8d1b188ca979 | -1.74349 | -56.06193 | 2024-10-30 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c9d78ad-0aad-34ac-a5ee-709e323cc5eb | -1.73419 | -56.07807 | 2024-10-30 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README82.md)
