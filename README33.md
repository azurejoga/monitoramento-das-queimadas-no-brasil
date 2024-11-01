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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 769dd451-3b89-3f0c-a033-6969df936f90 | -2.17393 | -48.83049 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2161e1f-f435-339a-a0a2-5305eac12da2 | -2.17268 | -48.72861 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1619c720-561f-34c3-b3e6-28193e4d19d3 | -2.1721 | -48.73227 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| abb5afa6-11e8-3d68-97c6-49b032a55bb2 | -2.16869 | -48.73173 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9e81eb47-eb2a-32f6-8b5e-f2215db015f4 | -2.72144 | -47.99187 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25fdba77-ff49-344a-afc6-223e10c983c9 | -2.71866 | -47.98785 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f7d9460-bb58-3c2d-a0c1-858456fe93ff | -2.71811 | -47.99134 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed707246-29a7-3bfa-a14c-33fbe5d624f7 | -2.71755 | -47.99484 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d644be1-0180-34c5-b5db-19b37d833e56 | -2.71422 | -47.99432 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e33244c5-c2ec-37a1-a27b-b50918c71803 | -2.7109 | -47.9938 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a8a20d0-cb3a-38a2-a3bb-98f38398aa99 | -2.7069 | -48.29953 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a047f9e-5933-3b2d-a307-7ec10f6c48cf | -2.70299 | -48.30256 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47de54a9-e915-3016-ba97-62d279acb614 | -2.69964 | -48.30204 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0bc1d977-2a67-3404-bb26-389741a2b18f | -2.69685 | -48.29797 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c209a69-ffb0-369c-ada1-cc7b197b9f16 | -2.66938 | -48.13099 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42985a1d-2fa5-3656-a0ef-49e364fb6f29 | -2.66604 | -48.13047 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4974a06-e446-3dbb-834d-0ca550af6322 | -2.66549 | -48.13399 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efa5ff27-3b23-342d-a065-241f906732c4 | -2.63774 | -48.39814 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f6616a2-436e-3e26-88f0-54a287b44cdb | -2.62095 | -48.32985 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 887073d5-747d-35f7-b2da-60d3ff2b326e | -2.62039 | -48.33341 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf1346c4-b167-30bf-8088-9b8a4695a380 | -2.6176 | -48.32933 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b58cc1fc-ed82-3abb-8ea1-50427e4a6a85 | -2.61704 | -48.33288 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d628f6e-e64a-30ac-a1ec-83da1e70ea6f | -2.61424 | -48.32881 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9da1c4b9-5d29-3b34-a63b-8da8ef201325 | -2.61368 | -48.33236 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1839b02f-23ba-3e62-8a6f-03542a3f3fce | -2.61143 | -48.36847 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6de5bd52-6cc9-3bba-b055-a51bd7fc8c32 | -2.60807 | -48.36794 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58a9bffb-125b-3f42-8135-42c753a95b2b | -2.59367 | -48.15525 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8bf20fd-7730-37e5-b802-9f8b5c1b3c6d | -2.59311 | -48.15878 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfbebddd-776c-3fc4-a44c-2e4530d2d525 | -2.59255 | -48.1623 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fd027396-f281-3ec7-a0e8-0fc5579f830e | -2.59034 | -48.15468 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fffc2dfd-47c6-3dad-b44d-8218ac301aba | -2.58977 | -48.15826 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20cf68f5-f20f-3aaf-8675-ae9d73407c5a | -2.58921 | -48.16178 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6141c146-23a1-3d42-96dd-478b42f841d7 | -2.57487 | -48.08353 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29473c4b-b891-3a4a-800a-076fcb1dc095 | -2.57472 | -47.97577 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 539b0547-930b-3d13-9107-cc308d22e388 | -2.57417 | -47.97926 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91e5809f-6c3a-3ff2-9b17-bd0d7660b4da | -2.57139 | -47.97525 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c694274-7ca0-3f7e-a62c-4711517161c2 | -2.57084 | -47.97874 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15c3b4b6-72e7-3268-b909-f069d6fb8456 | -2.55382 | -48.17399 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8c7f0936-c387-3a99-831c-864c6155c3f2 | -2.55048 | -48.17347 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8015404f-ea1b-311a-b272-94add1256284 | -2.53854 | -47.51503 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a8defae-25bc-30ac-a6af-24488e30fb54 | -2.538 | -47.51847 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5504185-a462-3617-9b80-f3255bad32d7 | -2.53768 | -48.2113 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9d86eec-18a6-3d29-8ecb-f45704631d78 | -2.53523 | -47.51451 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44c700fb-7cee-3219-91d1-155c88a78833 | -2.53469 | -47.51796 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4039e99a-b9a1-3938-9819-79caa1765372 | -2.73142 | -48.74402 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b458aec-6f7b-3f89-ac4c-fad0e00f5128 | -2.7286 | -48.73986 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f152bda-9140-35ae-8309-f13338055507 | -2.72802 | -48.74349 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84699420-4cce-3d6e-aba6-38e31edc22cd | -2.72745 | -48.74712 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5aea9d07-89e4-355b-9f4d-e069d0bda9a9 | -2.72471 | -48.72063 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbe8da1e-c640-310d-bba1-5658193e12e2 | -2.72405 | -48.7466 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6536a862-ed5f-38ac-a8a1-22cd86c79b25 | -2.72066 | -48.74606 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b32128ee-f0d7-3341-a16e-33ac5470bf77 | -2.71727 | -48.74553 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7dc2763-7254-30b3-a4ae-41252b465475 | -2.70551 | -48.63657 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 896df01e-9e48-3945-9436-06d3ae4dc7cc | -2.70157 | -48.63965 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b45c064-549b-3d17-807a-baf55711ff81 | -2.69818 | -48.63911 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f27b8aaf-8470-3e57-b5f1-a5f6ab8ca6ca | -2.69762 | -48.64274 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 091b73ae-c106-3ce1-a53d-d72130786c8f | -2.69705 | -48.64636 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e5362ae-f5b3-30d1-8971-e351da1db9ed | -2.6948 | -48.63858 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b625bc10-7c26-3e46-9ed6-f3892274a1aa | -2.69423 | -48.64221 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7bade1a-2cb2-31f7-ad4d-1b29ef5f6350 | -2.69366 | -48.64583 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b078a11-b1dc-3d72-a1ce-4a4bd996709f | -2.69142 | -48.63805 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a780af7a-a239-367f-8a06-589d83d932cd | -2.69085 | -48.64168 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2f07fd8-6782-33b2-a022-ba69fde9a50d | -2.66999 | -48.6421 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fdb0aec-5bde-355a-b4c4-4ef004c985a1 | -2.66337 | -48.57451 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29da550b-f5ed-35fc-9324-652e498c64fc | -2.65672 | -48.52925 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c751e580-3b7c-3dc4-9392-0234379877e8 | -2.63643 | -48.54814 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4e358b6-21ca-3bc3-94c3-fbb74b35431e | -2.63535 | -48.53325 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9e528d2-8591-3116-b5fa-daa5e5b6b83f | -2.63306 | -48.5476 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84eeaba3-1038-34cd-bf7a-7683839457f6 | -2.63255 | -48.52913 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a761b85d-6f17-3aa9-903a-d0079b40e6a3 | -2.63249 | -48.5512 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa341592-7f17-3b0b-bf33-7cc08cf3e5ea | -2.63198 | -48.53271 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 579b4f37-dfed-3ad4-afd8-c3266381fe18 | -2.52044 | -48.46402 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7df9684f-2de2-32ec-8026-fcb1019b0b65 | -2.51987 | -48.4676 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e493aa2e-47ba-3f7a-af8d-6bede2b96edb | -2.5193 | -48.47118 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8e6aec3-6040-334b-b37b-d6ba48d4c751 | -2.51814 | -48.46717 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7476613b-a77c-350b-9791-a586fe2010b6 | -2.5159 | -48.43743 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 52b62fbe-ca20-3e4b-9a7d-220f55d8cb61 | -2.46417 | -48.50284 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8bb9a761-0a3a-3510-86ad-ace439b57d2c | -2.46079 | -48.50231 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b6df4e16-abdb-32a4-be9a-72a1bfdcbc98 | -2.45856 | -48.4946 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08f0e7ce-c515-3fcf-b262-85991e0f567f | -2.45799 | -48.49819 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef04a842-9f46-3576-a814-b9d795fcb0ff | -2.45742 | -48.50178 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 995d7a26-214c-309c-9452-c00bd0dafb43 | -2.45405 | -48.50125 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d799ae2f-49d7-3863-8c6b-a7b2687caf17 | -2.44872 | -48.62244 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1028ce4f-ef7d-3c97-be51-852f92d05a4b | -2.44735 | -48.47812 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53a17f01-05c6-3cf9-b19c-45198388b7f3 | -2.44534 | -48.6219 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3067d2c5-88ab-3447-ba46-2d5a23b1406d | -2.44477 | -48.62553 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17fa4255-f5a4-3440-8252-bb894bd32945 | -2.44341 | -48.48117 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe7bb84a-ae25-3535-aabf-4360fd8cd6e0 | -2.44336 | -48.50326 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 165b308a-9fb8-32b4-9fc8-ed3882725b49 | -2.44293 | -48.44069 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25da541e-90cd-3110-b2aa-d91f0241a8a9 | -2.44138 | -48.625 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cb50a02-4e0d-3b29-b990-3cbb3f1707f3 | -2.44029 | -48.60997 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 84875b10-8825-3968-8229-1b61b6351419 | -2.44004 | -48.48065 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f7cbc89-9aae-3b52-9825-4719f5bab93a | -2.43972 | -48.6136 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4354b4d2-0023-3ca4-9fd3-2ca1a4c88ecf | -2.43914 | -48.61722 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 577ffac8-aeb8-322c-b4e3-bec9212e38d8 | -2.43547 | -48.50939 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7cd9da59-85ed-34b4-b20e-cae182eae97c | -2.43267 | -48.50526 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4534b9d-2a7a-3461-97f5-69350c7ba6ba | -2.43221 | -48.46471 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c484bd5-6ca7-3840-9f9e-bc564ff84921 | -2.43164 | -48.4683 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59ecbd75-3029-3299-975a-500ceb492943 | -2.42929 | -48.50473 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0481b95-3bcb-3935-92cd-e285dfcbe26c | -2.42694 | -48.54126 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README34.md)
