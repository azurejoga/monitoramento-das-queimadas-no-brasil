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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ecfdcbf-73e2-3de3-ac6e-cd7eb937557d | -10.51881 | -67.88238 | 2024-10-13 05:29:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23ffea04-23a2-316c-a8f7-ba2764d93e15 | -10.51561 | -67.83751 | 2024-10-13 05:29:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a61131e4-d55e-33b3-b90f-dd103fc69b07 | -10.5151 | -67.83388 | 2024-10-13 05:29:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07abfdb7-7fc5-3d3f-b15c-64eb78f0b9ae | -10.51166 | -67.83682 | 2024-10-13 05:29:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d993cac7-d463-3bd7-bc35-9c6373e76a96 | -10.48014 | -68.41389 | 2024-10-13 05:29:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed95c306-fbab-30af-9090-ebaab2658bab | -10.47731 | -68.62754 | 2024-10-13 05:29:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ace5dabb-613e-3f5a-826b-5882d2696e66 | -10.47706 | -68.383 | 2024-10-13 05:29:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 252d4cb4-1c03-3f3f-9968-73c9dfdb7095 | -10.47641 | -68.38673 | 2024-10-13 05:29:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8a8ccf7-ccc6-36ac-9cf8-d4be027696d7 | -10.44984 | -68.22731 | 2024-10-13 05:29:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81510f1f-23fe-3f12-874e-6379109c7bd7 | -10.44967 | -68.2277 | 2024-10-13 05:29:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1ce7959-3a9e-3a88-a31f-4f27978bc8e6 | -10.43882 | -68.36085 | 2024-10-13 05:29:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f75a3d4c-c1a3-3fb6-89e2-afc055b5d88e | -10.43817 | -68.36451 | 2024-10-13 05:29:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 449cd316-4c18-326e-8400-9a501107eec5 | -10.43344 | -68.36749 | 2024-10-13 05:29:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b47e0a10-45a4-33e6-a34b-7859fb9aaf5d | -14.87411 | -57.48003 | 2024-10-13 05:29:00 | NOAA-20 | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5aa0ab4a-e0f9-3ee9-9145-cc1c00dac704 | -11.8981 | -57.47255 | 2024-10-13 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64e505c9-34b6-3f94-81e7-1d4253d417c6 | -11.89765 | -57.47128 | 2024-10-13 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71336c8e-60ba-37ff-8e43-30a1c24ec416 | -11.89442 | -57.46793 | 2024-10-13 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 540d4b4a-e9cb-3bb9-b060-1595da7e446d | -11.89386 | -57.47193 | 2024-10-13 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8996ef7e-bd29-378d-ad09-5b5ff2e9268c | -15.95735 | -59.12385 | 2024-10-13 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56a54c8a-3c83-3f3c-bfd8-6d161f6886e8 | -15.95683 | -59.12773 | 2024-10-13 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37e63755-f4fc-3358-ab65-190ac842a2bb | -15.95333 | -59.1232 | 2024-10-13 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af59777d-f97c-3ab7-9234-dd91fb097989 | -15.9528 | -59.12712 | 2024-10-13 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7a44e83-ca11-3741-9c64-e1e7b678daa3 | -15.94981 | -59.11879 | 2024-10-13 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8be9a633-f182-3ade-836c-e21f0ee0839a | -15.9493 | -59.12258 | 2024-10-13 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01536cf0-3cfe-39ba-8aa1-bc89f305b541 | -15.94919 | -59.09255 | 2024-10-13 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7906a1e5-007b-32c1-9a1d-7d19fdb3ede5 | -15.94878 | -59.12648 | 2024-10-13 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58eeecb1-2a78-3278-97b4-ea7b621a0a18 | -15.94773 | -59.10356 | 2024-10-13 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f843af92-3eec-3d20-8ae7-2e805dd4d9d4 | -15.94527 | -59.12197 | 2024-10-13 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6d644ad-bc1a-39ac-a608-bdda044c1737 | -15.94514 | -59.09203 | 2024-10-13 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ab958f1-90ee-31fe-b209-c93f3b1da4f0 | -15.94466 | -59.09566 | 2024-10-13 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 247a8982-3422-36d2-875a-d48844d0dd64 | -15.94417 | -59.09934 | 2024-10-13 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6eb4070-b7ec-393c-be99-9c4be60e1c42 | -15.94368 | -59.10303 | 2024-10-13 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcefb7ee-cb32-312e-b018-10fc22f2aa7d | -15.94109 | -59.09154 | 2024-10-13 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 347d825d-5672-3e6e-9d5c-2dc34eabcc50 | -15.94061 | -59.09517 | 2024-10-13 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b352f5d-e42a-3e3d-9c11-e04d94ac0861 | -15.69254 | -59.3392 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31a7e480-5e03-3bc0-9a99-8c6e4d561a1b | -15.69177 | -59.3449 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8e1b7d8-4265-3302-ba55-5266324c7a65 | -15.6878 | -59.34437 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be5ce0d1-cbc3-3f59-bd0e-22077ed9e11e | -15.65402 | -59.35546 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c801d8ee-1185-32cf-ade7-323d1c697745 | -15.6508 | -59.34927 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0780a7c8-231d-3a4c-a4be-f47de2fa1246 | -15.65007 | -59.35478 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd7d9148-d15b-337e-b274-7468d5f715c5 | -15.62639 | -59.38776 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c679a71-30dd-3228-be0a-b59ad6d7e203 | -15.62577 | -59.44761 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d41fd89-51bc-3108-a7c8-18752d6215a9 | -15.62567 | -59.39297 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72f45f39-cd96-3086-a2c1-c7a9fc1bfb2d | -15.62494 | -59.39826 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38f1556b-6c38-3dcd-b1e8-d517e0da382c | -15.62477 | -59.394 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4b8ade6-831d-3e95-a235-06e1725a6f14 | -15.62407 | -59.39935 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fa98184-b314-39a8-93c5-e6b08b62caa6 | -15.62337 | -59.40473 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abdb3fa4-2be3-307c-89b0-1ffc665beb37 | -15.62237 | -59.44595 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 905a7a1b-d35c-3c77-ada3-f59728498953 | -15.62183 | -59.44707 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33c10abd-51af-36bf-9c4b-31dccad2e9a6 | -15.61943 | -59.40413 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8b29777-6dac-3cd6-82d8-5077a64c838f | -15.61852 | -59.44182 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1c19fde-fe5f-3126-b8fc-4ed31bb706c4 | -15.61841 | -59.44556 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 854f16c8-9c78-36d7-ac55-a08a4582c669 | -15.61788 | -59.44667 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30958475-5195-303c-b07b-e442ad681a23 | -15.6163 | -59.40254 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f2df70b-24fb-34b5-9b38-c6e59e219cc0 | -15.61512 | -59.44027 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6e422ff-e58a-3f53-a6d4-6e6c944defde | -15.61456 | -59.44138 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab6b987f-66fc-3430-9d11-c49460bde71f | -15.61444 | -59.4452 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3ad1565-b328-3321-bb44-d847c6bbb225 | -15.61158 | -59.40759 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fc8cc7b-f7e2-32dd-8ccf-017292e2ed11 | -15.61118 | -59.43975 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0df646e0-20d2-3e13-ab8d-a2bdc3b4f733 | -15.61083 | -59.41308 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9e6ad5a-a6a9-302a-b97f-14e3ca785e28 | -15.6105 | -59.44469 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f98a495-2880-3eae-8608-48246db9d860 | -15.60937 | -59.42372 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33029921-6e1c-389e-ad06-43ec64ebc317 | -15.6092 | -59.39569 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa146bbc-1952-30fe-819f-f323144f6683 | -15.60863 | -59.42906 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f2893fa-1069-32e9-b3cc-fed5ad4e6d12 | -15.60793 | -59.43418 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c814eb58-ff76-3317-ab97-1b227b8cd5b9 | -15.60136 | -59.39418 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b0b1edc-c157-35a9-a3d4-3b4d8cddea5b | -15.60064 | -59.39946 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77d2b178-66c4-3a61-afab-ae04241e731f | -15.59989 | -59.40491 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2b69187-db30-3853-b09e-d6615316e929 | -15.59742 | -59.3935 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d21adfe8-0a20-3955-a917-b8c09f52c9ab | -15.59597 | -59.40414 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 526d64c8-3757-3933-8030-c5a13d716ee5 | -12.31095 | -59.15819 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ead5703f-a331-3ee5-8eb3-db5a4fe79af5 | -12.30971 | -59.1552 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2a09fb9-6795-31e1-a154-a94ddd6aca23 | -12.14226 | -59.87988 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d268866c-219f-376d-9400-c5bb6827a27e | -12.01952 | -59.59715 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fd4bc64-44c3-34c9-a105-b3a53db1c7d0 | -11.8703 | -58.99713 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5acc64e-7dbd-3060-b289-c278c95cd787 | -11.85218 | -58.87417 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 590b8d6c-31cf-3b82-80cf-0c6f145632c5 | -11.8277 | -58.85099 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99da1386-7380-37bb-b955-c4a1c7720b63 | -11.7649 | -59.95979 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a97dcf09-4d79-3115-8d77-1e7689f40d9e | -11.76063 | -59.96352 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d42cd5a-7a98-3f5f-921e-24ef47b8b657 | -11.7228 | -59.16349 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b866fca6-022b-3576-a3ee-6d6f3b19f0f9 | -11.72212 | -59.16827 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e931ef34-5942-36d6-a815-61aeefd8390b | -11.719 | -59.16293 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4a4d4a2-91ff-394c-9e2c-8dd3b1b64c43 | -11.66848 | -59.93214 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f3fd132-38a1-3b49-9fb9-6919c57c6f34 | -11.65835 | -59.89678 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea5dccba-90f7-31eb-bfe8-1e76eaa86698 | -11.65771 | -59.90112 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 381fc52e-1c3a-39d0-9578-9f81bc576d87 | -12.31443 | -59.2342 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08866b22-04d8-30f1-8d7e-a7d00bdbe0fc | -12.31136 | -59.23641 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d064639a-993f-378c-9e77-692308bcf133 | -12.30906 | -59.15998 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a99def64-0e51-35d4-8295-b9f1630bb76e | -12.3084 | -59.16479 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4f436a5b-84c0-3b83-8a73-118a66578387 | -12.30713 | -59.15756 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 162b5c3c-c652-3c1a-9914-a1ecec93f95b | -12.30644 | -59.16235 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fcf9304b-fee6-3aa3-92d0-7026183bfb3b | -12.26377 | -59.21497 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53b47e9d-4415-33b7-8672-5747b85208f9 | -12.16301 | -59.89205 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75355b1a-eea8-3e5e-8f6d-c59e6aafb063 | -12.14593 | -59.88046 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c2d8311-a66e-3ac6-a084-c2a0161b96e2 | -11.58573 | -59.98696 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8283f2c7-af9c-315a-ab51-9dad516c61a2 | -11.58449 | -59.99552 | 2024-10-13 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2b70d82-459b-3719-be65-17ac5b1b49a2 | -13.65863 | -60.1545 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80c80437-3cc2-31d6-a47f-1d8dc5c1911c | -13.47634 | -59.91713 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d427970a-3e22-3290-9375-dae0a952cd50 | -13.47261 | -59.91658 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| f6bcaf09-fcbd-36b5-b11a-1f8d4b61d063 | -13.13812 | -59.69123 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README102.md)
