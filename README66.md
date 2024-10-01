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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2834ccf5-529e-3f92-9bf0-c238f0e36eac | -3.06445 | -50.48462 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7df9b81e-44c0-3327-be1a-cdd1347a2a44 | -2.40836 | -50.32457 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7eb7e397-73da-30f6-8785-9739b79ea5ff | -2.40793 | -50.324 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80671f27-9af3-3224-aedb-1c232b7833e0 | -2.4079 | -50.32746 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| b14bdf4a-d304-3306-99d0-578a1f6ff2b3 | -2.40745 | -50.32688 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9df51621-9341-39d2-bb26-8037ea33475a | -2.40744 | -50.33036 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| ba24e45e-4c8e-3a6b-a397-ac2d1b8095d2 | -2.40698 | -50.33327 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 69e2b29f-e8f1-3159-904d-45785b1d9632 | -2.40696 | -50.32978 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 361aeecd-be69-3719-a1ca-3073b1013f5b | -2.40651 | -50.3362 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 0257e6f4-3371-3633-835d-0a995b736e65 | -2.40648 | -50.33268 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 160c2a49-30c1-37cc-8a31-1673a70fbf2f | -2.40605 | -50.3391 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d6a83aa-c495-32cc-8aaf-d75bdbb3e3d0 | -2.406 | -50.33558 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a6d5e3a-81fd-3229-b505-4189ad5da583 | -2.40559 | -50.34201 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04486291-04b0-365e-8185-4e489efe6532 | -2.40551 | -50.33848 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42dbb55a-d56f-35f6-be7c-c3327817737d | -2.40503 | -50.34138 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba5aa4c0-56b2-33bb-90af-5e760e858f4a | -2.40381 | -50.32082 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed463b4f-9877-3b9c-9c5f-9d2c6298ad4d | -2.4034 | -50.32027 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae3c234c-c153-3db2-b9c0-8669f27f4086 | -2.40335 | -50.32371 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 496ff4ed-f7ad-3125-86e2-b294d273b333 | -2.40291 | -50.32315 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 223612dc-3fad-3f99-ac7c-44efc06f4c97 | -2.40289 | -50.3266 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 10074af6-2d45-30a9-a670-e5425b02c3ad | -2.40243 | -50.32603 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| e235f21d-810b-3a15-ae16-cb0e493c35cb | -2.40242 | -50.3295 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| b9b57b3b-6574-3c07-979e-fd58622bd677 | -2.40196 | -50.33241 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 87dc47cd-f7c4-3793-92ac-a9027f67718d | -2.4015 | -50.33532 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| ed05aa88-2c02-39bd-a31b-089daca1c384 | -2.40146 | -50.33183 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 2e1705a7-3cf8-32f0-aecb-84b5ac0c7834 | -2.40103 | -50.33824 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1a4d04b-cb01-3a30-b89a-3656c7bd7c41 | -2.40098 | -50.33473 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 6f657be3-2364-3d88-8e83-4d96449705a1 | -2.40057 | -50.34115 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b1d4cd5-777c-3905-854b-73d8d74a712e | -2.40049 | -50.33764 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| be5cab22-260c-3cfb-bb4c-d117257f206a | -2.40011 | -50.34406 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41a02766-c235-3237-b649-f2f39d0d87bb | -2.40001 | -50.34053 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7ca3e20f-4a31-390b-80f7-7d3496226cc5 | -2.39964 | -50.34698 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f0be6e3-9dab-375f-9e9d-b6e62ffd70f2 | -2.39952 | -50.34343 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9eeb5086-93d4-3250-8981-8500c5486629 | -2.39879 | -50.31997 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1c7eceb-93b7-3184-92ae-846ac2bc1b63 | -2.39838 | -50.31944 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b0e72a6-d4ae-384a-a1fa-fbcb20494f87 | -2.39833 | -50.32286 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3407a2e-336b-3955-a6a0-5d99bb1477fe | -2.3979 | -50.32232 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec722824-4669-3497-ac82-b6a754f00edc | -2.39787 | -50.32576 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 49a89c5d-e220-342a-a704-bc43cc4469fa | -2.39741 | -50.32521 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| a57091d7-4879-3914-936c-318901f5a911 | -2.3974 | -50.32866 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d9ad673b-a80c-312e-9c8f-1a4504554fd0 | -2.39694 | -50.33157 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 5691c612-5bc1-3ce0-bc5e-6d8d447afed5 | -2.39693 | -50.32809 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| bbee1f7e-f355-31c1-ab77-4af44264a8fe | -2.39648 | -50.33448 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 6b9e80c1-0fc0-3fb3-a72d-045cddc09139 | -2.39644 | -50.33099 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 9c046ad0-01ec-3ea8-a458-ad4f7663c9ab | -2.39601 | -50.33739 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0fc9e54b-f521-3390-a923-3aec24541ef5 | -2.39596 | -50.3339 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 85ee4fed-b927-32c5-aa0e-5b37419cd975 | -2.39555 | -50.3403 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 254876b1-4483-38c5-883a-6052a2ad70d9 | -2.39547 | -50.33679 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8aa0079b-a676-3217-b662-8aa25757f1a4 | -2.39508 | -50.34321 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e146e60-aefe-3f40-b59b-0204ceacda02 | -2.39499 | -50.3397 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eaad76dc-51d0-3c01-b5f2-28056537429f | -2.39462 | -50.34613 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e2ec7b8-2773-3022-b1f4-7c20798625ef | -2.3945 | -50.3426 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9795c11e-94b5-3423-93a8-c1769b6a85e4 | -2.39331 | -50.32204 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c622e12-7276-325a-9923-b1ea1fbbf5a1 | -2.39285 | -50.32494 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9248394c-46f8-3744-8a4c-91e1870afaf5 | -2.39238 | -50.32783 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 11f11069-63cf-30ec-898a-7ee75ad6070b | -2.39192 | -50.33073 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| ca46099d-e9e6-3993-b247-b8373b75f80d | -2.39145 | -50.33364 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 46b8776a-9557-3355-bd9b-d71a71ad2ed1 | -2.39099 | -50.33656 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| beae86c7-1ec3-3fb2-897b-bf849b1e86e4 | -2.39052 | -50.33946 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be658bda-a88c-3580-961b-90134956e496 | -2.38783 | -50.32412 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b35bbc4b-ab30-327b-b68a-e2db76144291 | -2.38736 | -50.327 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1a7f186-5231-3e9c-a845-20049d3e9a8a | -2.3869 | -50.3299 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 459f2eed-124a-39ed-9379-204191342a54 | -2.38643 | -50.33281 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe9a112a-e742-3589-809f-973a189295d1 | -2.38234 | -50.32618 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4b64b42-099b-3e53-9eb4-80061db07881 | -2.38188 | -50.32906 | 2024-10-01 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c31fb329-11ce-3110-97b2-ad915ced05a5 | -4.09591 | -51.12386 | 2024-10-01 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95e9099e-e0fe-3030-87d4-cd7026009ecf | -4.09536 | -51.12703 | 2024-10-01 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4b61ea2-7bf7-3147-b496-54fdbb69e3c8 | -4.09483 | -51.13011 | 2024-10-01 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b3794b8-e3ca-3b43-9a8b-a6becfe5822b | -4.09431 | -51.12217 | 2024-10-01 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a0024f2-5a8d-37b0-8d96-486fd68a8ca9 | -4.09379 | -51.12534 | 2024-10-01 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a689031e-c21b-3eba-9cc6-16e103f4a074 | -4.09327 | -51.12849 | 2024-10-01 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84e9e97d-dd7a-312e-b5a9-76130b99f50d | -4.08862 | -51.12457 | 2024-10-01 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4a6e34d-57b6-34e8-a136-5e1d6c9dfb73 | -4.0881 | -51.12769 | 2024-10-01 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4aa99f8-da3a-35e8-8091-0e9f5d7dd019 | -3.46624 | -53.7985 | 2024-10-01 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3699235c-cbca-33f0-b22a-1ae5919b9ac4 | -3.46537 | -53.80352 | 2024-10-01 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cb97a0f-3286-3ad1-ad58-1ef259c8d46d | -7.07532 | -39.14489 | 2024-10-01 04:12:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c9b6daa1-8743-3a2b-a739-0eb0f96c28ed | -6.7911 | -40.1413 | 2024-10-01 04:12:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 14b7753c-9530-36cb-856e-99829302e550 | -9.25025 | -40.82479 | 2024-10-01 04:12:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0efbe661-6773-3f12-a7eb-3525a65112a6 | -9.24965 | -40.82881 | 2024-10-01 04:12:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c1057068-1bd3-39bb-bfc9-7f31830f6eda | -9.24729 | -40.82024 | 2024-10-01 04:12:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b2910cad-91e1-3538-8505-84e488b0dcec | -9.01723 | -40.5717 | 2024-10-01 04:12:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 366b3924-40d2-38ab-897e-5513121baf75 | -8.94135 | -40.59933 | 2024-10-01 04:12:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bb80e4d6-2176-3fb7-a8c6-1b0cac942202 | -9.57005 | -40.34702 | 2024-10-01 04:12:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 79404148-4fab-3e48-84af-0e84f3eccc7b | -9.46959 | -40.39424 | 2024-10-01 04:12:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 454ec0c6-e582-334b-911f-d963891fe601 | -9.46595 | -40.3937 | 2024-10-01 04:12:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3daa7f99-9fa7-354d-8d8c-dbcae62ee89f | -7.5656 | -41.95427 | 2024-10-01 04:12:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1a9c2de1-82c2-358a-bc8b-7bfcda1ea321 | -7.27835 | -42.05999 | 2024-10-01 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 353fbba9-4281-3d56-992a-247cf0876f52 | -7.27501 | -42.05947 | 2024-10-01 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 93f80082-3b08-3d7f-9aed-48fdac830df6 | -8.92378 | -41.19374 | 2024-10-01 04:12:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 61b228cc-ef20-3eb7-b53d-9a18acb3aabc | -8.43395 | -41.93217 | 2024-10-01 04:12:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dee60e91-d400-3950-b089-1dde3156d562 | -8.4334 | -41.93579 | 2024-10-01 04:12:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4f1f56ba-0de1-360f-b558-d7c4a10bf38d | -8.0428 | -41.06969 | 2024-10-01 04:12:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 24c9a0a4-7f56-3735-b83c-fb75624937e6 | -9.97528 | -42.33392 | 2024-10-01 04:12:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 063ecca7-7e32-3e15-833f-77806cc84b69 | -9.76486 | -41.88002 | 2024-10-01 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cd926858-2153-3cc9-a6fc-9aca3816e288 | -9.7643 | -41.88374 | 2024-10-01 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4f526578-fa7e-3fa3-a7bf-f0545c1b21e3 | -9.76145 | -41.87948 | 2024-10-01 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 6a39c798-8706-3027-b3f4-6609596ae221 | -9.76089 | -41.8832 | 2024-10-01 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| c874fd40-0963-3a57-9df6-0867d23a65ab | -9.76033 | -41.88692 | 2024-10-01 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 1590d4f0-e4ae-318f-b2ab-05781667cb13 | -9.75803 | -41.87896 | 2024-10-01 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 583f8388-8517-38ee-a615-29e8a25f9081 | -9.75747 | -41.88267 | 2024-10-01 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |


[Clique aqui para ver as próximas entradas](README67.md)
