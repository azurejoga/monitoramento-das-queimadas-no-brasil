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
| 080745f9-36d9-392e-b3c0-1001360402b1 | -16.47256 | -57.3143 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a6dc748c-dd31-3f39-a64c-3fb557c21261 | -16.47174 | -57.31894 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c5c98ed7-6b77-3025-92b2-edff01946144 | -16.46964 | -57.30896 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 99ae236b-43cf-33d8-98cf-73ff42b292fc | -16.46883 | -57.31359 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 349b0bf0-27ff-343b-b224-1e0cdcaebdd6 | -16.46862 | -57.42482 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| d0a6ae8f-9bf4-3b85-991c-71b0f422007b | -16.466 | -57.35162 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 147a9d2e-13b6-3351-b4ef-859235834d1c | -16.46555 | -57.33222 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b9942817-f947-3284-ad5e-35113cf4ab24 | -16.46518 | -57.35631 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 36468b0b-e38f-31e4-8239-3a56b7387f26 | -16.4651 | -57.3129 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 7336c3ba-6236-3711-9a6b-1a39a8051b8d | -16.46405 | -57.42881 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 97a563fe-061b-3dfe-bdb0-fe09f4389057 | -16.46398 | -57.3851 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ff50dcf1-83d8-3008-b2ea-0ed362bd0a85 | -16.46353 | -57.36566 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| efbd4c8c-55e7-3268-83f9-6547c0d485c6 | -16.46062 | -57.36028 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 06967a5c-17cc-36b5-b2ac-97d07319cddd | -16.4603 | -57.42811 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a648a1c0-ca40-3a7e-999e-612461bfa487 | -16.4598 | -57.36495 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8e81074b-3427-384a-bd96-bb5512ca5b2e | -16.45974 | -57.32149 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cc4d1302-3d7c-3933-a122-3a5494f6fba3 | -16.45936 | -57.34553 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| fd189b0e-eea1-3a09-b0aa-d0e4e4785764 | -16.45897 | -57.36963 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 66dab174-264d-3a9c-a1b1-1b33a5946cfa | -16.45892 | -57.32615 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b683cfcb-0b9f-38aa-92b4-ef8074c0f7b8 | -16.45853 | -57.35022 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 12d6d393-a411-3afa-8d75-469788227775 | -16.45737 | -57.42269 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7d387bcc-6c3a-337e-9c18-eda6954f185b | -16.45655 | -57.42739 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d763ee2e-2a11-3af3-b2ea-c7980c95aa01 | -16.45402 | -57.39775 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cd46cb90-60a2-34b5-af6d-4b19f69575aa | -16.45197 | -57.43138 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| fc4d4af9-5bde-3014-bcdb-c2dbafe750ce | -16.45063 | -57.32941 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a031dfe4-5b62-3ac9-b68b-3fad41c7e52e | -16.45028 | -57.39705 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a01fe133-92ad-3609-a4df-9869173a7cd6 | -16.44945 | -57.40175 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b5a77df3-5b2b-3001-8dea-2d438ecbd4d7 | -16.44739 | -57.43537 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 397db622-75dd-3980-bfc8-112dd15c0f01 | -16.44653 | -57.39635 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 66f0c3a5-f86b-3466-8ec3-1814a2cab660 | -16.44608 | -57.33337 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 212f206b-e4d0-351a-9b47-4a0a3aae1891 | -16.44196 | -57.40034 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c05cdb6d-e5fc-3cde-89f4-f0c65d0a5c63 | -16.44072 | -57.42924 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 61272011-039f-35da-86bc-d2379feaef28 | -16.84591 | -57.69424 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 4a02174f-9898-3857-b038-9c99dba12c48 | -16.84506 | -57.69907 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 0a829e98-5919-3b77-8e96-f1830383b5a5 | -16.82475 | -57.72515 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9c04fd99-ecfb-3e71-b0e9-50e80f906081 | -16.82229 | -57.8052 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c318cc7c-1db2-3978-b9ab-f9dc977fce98 | -16.82143 | -57.81009 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3b9417f8-6b3b-3a85-b792-ea354c16f10f | -16.82096 | -57.72443 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| b1a74afe-5902-3e9b-b156-df58c2476cb2 | -16.81849 | -57.80447 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ec2132dd-5fd0-33fc-b7f8-1fa5a441c6f5 | -16.81761 | -57.80936 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 67394f6f-63f5-3f99-ae7a-19d0236590c6 | -16.81642 | -57.79396 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e40bc911-71ed-32b1-a60a-ff3c2aa422f1 | -16.81555 | -57.79885 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7252cfb8-4e86-35ce-9a6e-f13ee9479299 | -16.81468 | -57.80374 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6c70c6a8-5c46-3beb-a9c7-845199d2b59f | -16.8138 | -57.80863 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 13dba174-29f4-3be4-b79b-f874c7c2836a | -16.81174 | -57.79812 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 83b5b46f-d185-31d7-814e-c30e57b8d37a | -16.81087 | -57.80301 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| df151a12-5537-318b-8aa7-971402325fa4 | -16.80912 | -57.8128 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 48e83789-ced8-36e9-91b6-cc6560d65155 | -16.80531 | -57.81207 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c03d14ff-2ffb-3ae8-93a8-3599b60d9467 | -16.80428 | -57.68632 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9d2d00e9-49e5-3895-9952-7351cd9ae930 | -16.79593 | -57.82041 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 61907003-9386-3948-843f-b4f0544090e8 | -16.79211 | -57.81968 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 995c7c1a-4b8b-3cc6-8a37-d5e1809699cb | -16.7883 | -57.81895 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 85a72908-f030-3890-8837-963635c407c8 | -16.7836 | -57.82312 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d3eac799-c392-3eba-a9b2-7b963a5383e2 | -16.77597 | -57.82166 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e6d17f4a-fd96-3a97-b5d2-75600df89a7c | -16.77216 | -57.82094 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4bb5ea28-5533-3dc6-b18a-308565da19c7 | -16.76923 | -57.81532 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a63d7661-b998-371c-a05a-afb15a3d560f | -16.76541 | -57.81459 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 088c3a9d-dfcd-3b1d-ab40-bcb4d6ad32a6 | -16.76464 | -57.78164 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8db365e2-9fd5-33e6-801e-911bbde56bc1 | -16.76311 | -57.78381 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0a8aa54e-56a6-3a89-b875-864aad8833d0 | -16.7616 | -57.81387 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 4d2a8b57-ccd8-3f7e-a57c-c181c690d4e0 | -16.76084 | -57.78091 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ae1f5fef-69ac-3acd-b412-8392facd6a6e | -16.76036 | -57.80611 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c4abe71e-303b-3cd7-bfcd-ece013fccec0 | -16.75998 | -57.7858 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| a2d1bc2b-69ac-38f2-b434-5de22e6ccaf2 | -16.75956 | -57.80335 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 2dbab4b6-b6dc-3727-b2a1-404d0cbd7251 | -16.7595 | -57.81102 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 1320c487-9f13-326f-81de-b4bbfdc75a4e | -16.7593 | -57.78308 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 001b4229-751e-3617-8886-305f7b095d7e | -16.75867 | -57.80825 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| f90c99d2-517f-304b-b673-e01656477ce5 | -16.75655 | -57.80539 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 3e312f44-3614-338e-90d5-1afedfdfe4af | -16.84702 | -57.75448 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ad10984f-5136-3fc8-94f6-de970145e6a5 | -16.84616 | -57.75934 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3a4c218b-ec42-3fcb-9a3f-a2aa3656f6cd | -16.8453 | -57.76421 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9c0e68c7-327a-3f3d-be3c-8435f31c3480 | -16.84322 | -57.75374 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 94974b34-bb8f-30c8-89ed-5b3f4f0155ad | -16.84236 | -57.75861 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6f1967b0-a48a-3bf7-a2fd-832a58147130 | -16.8415 | -57.76348 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4013ef4d-895a-3051-85e2-445b5f6eaefc | -16.84063 | -57.76835 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 986241f9-faa3-3272-b7c9-b93236767e1a | -16.83942 | -57.75302 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c1f97149-68a4-384d-9646-c4aeba305de8 | -16.83856 | -57.75788 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e05d8f27-25f5-34a7-94f9-def47d7a89bf | -16.83562 | -57.7523 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e028f905-f8c8-3d70-99dd-7dfd1efbdaba | -16.83476 | -57.75716 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b7bba604-65fd-3b44-b842-2cb777ff01b3 | -16.63185 | -57.32153 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2270729d-89f3-34df-a0f2-12a32d2786ac | -16.62893 | -57.35938 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 82a8f9cb-dea9-3f1d-934a-7a1c48b86cf0 | -16.7549 | -57.48232 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.4 |
| 7f4664d7-dd05-31e5-99dd-62e9ab88dd47 | -16.75406 | -57.48703 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| f330f3d0-9a73-3134-9502-18b1b8cfc1af | -16.75115 | -57.48161 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.4 |
| 717759a9-d2be-3fd1-923b-7e1fe396f1c2 | -16.75032 | -57.48632 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| 5e31ff74-31e6-3b5b-ac6e-55810a56a0e0 | -16.74741 | -57.4809 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 7cd5a8c2-8e11-3f37-bd3b-77b4ce9946cd | -16.74657 | -57.48562 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 8c785d42-d636-3daa-86c9-3d036f4e0ee9 | -16.74573 | -57.49033 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 1cbf6c70-f734-31ed-bce7-75d96a46b466 | -16.74539 | -57.38377 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 004a21a6-b1bf-3c54-a2eb-d215e8075dcc | -16.74454 | -57.43184 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 46b2720b-79b4-3d70-90a8-9d075354d69d | -16.7437 | -57.43652 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| bcd5b7b2-37f9-3ab3-a032-af3fa29e7d24 | -16.74366 | -57.48019 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 816f8167-6d45-3e39-a589-b443bd76a26e | -16.74249 | -57.37842 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 8ba614de-d084-31bc-bcbc-1f755561ddb5 | -16.74166 | -57.38307 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| b9de77eb-5181-3441-bdc4-6f130ef23d29 | -16.73996 | -57.43583 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 08569789-8f05-3235-99cd-b6fe55748237 | -16.73706 | -57.43044 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| e6f6d96a-562d-3606-9f06-f57becb5ff2f | -16.73623 | -57.43512 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 401a02cf-1126-331b-b441-ea894f1f3b74 | -16.73617 | -57.47878 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 30d6f966-ca91-3bfc-b926-6198dc6abdd6 | -16.73333 | -57.42974 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| f6a87ffe-cf7f-3634-a9c7-aca4fe4c78f8 | -16.73326 | -57.47337 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |


[Clique aqui para ver as próximas entradas](README112.md)
