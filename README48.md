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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 842d59bd-ad3e-32e6-9f6f-ef365a39c4ac | -17.5875 | -57.5122 | 2024-11-11 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.4 |
| 1d20e446-adb7-3ca7-9085-6437ad552cf2 | -17.6266 | -57.5281 | 2024-11-11 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.0 |
| 649ef4a8-2a32-3adb-acf5-7eb0903f3a68 | -17.6069 | -57.5304 | 2024-11-11 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.1 |
| 9a614754-566f-3d20-8fe6-280db4608ff3 | -17.5875 | -57.5122 | 2024-11-11 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.0 |
| 43e37c2d-694e-36b2-a4c3-5c1c53db114c | -17.6266 | -57.5281 | 2024-11-11 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.7 |
| 4500c9e1-91ba-3bae-a037-7b55cd159509 | -17.6069 | -57.5304 | 2024-11-11 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.0 |
| ebef49c8-ffd5-31ba-b10e-06f3395249c6 | -17.2933 | -57.4857 | 2024-11-11 08:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 969caa51-edfe-3cc0-8384-0ff62b4dac50 | -17.5872 | -57.5328 | 2024-11-11 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| cfa3a7c4-f1d8-3ce3-9b9f-ce8990e200e0 | -17.6073 | -57.5099 | 2024-11-11 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.6 |
| 6c686259-06ec-378e-8b2b-cb3ed1328b5a | -15.9985 | -59.3449 | 2024-11-11 08:00:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| efa30bce-8852-3ffa-83d4-354ad706c265 | -17.2933 | -57.4857 | 2024-11-11 08:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 069d4578-1992-368f-b441-79a3920854b1 | -17.5872 | -57.5328 | 2024-11-11 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| d845bc04-d198-37c5-9c87-0e89e76b55a4 | -17.5875 | -57.5122 | 2024-11-11 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 2365408c-3b30-38f1-91bf-7c7e1debfa9a | -17.6266 | -57.5281 | 2024-11-11 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| e2acc17f-534e-3818-815d-3ac4bcf69422 | -17.2936 | -57.4652 | 2024-11-11 08:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.7 |
| b474ef92-35fe-3ac2-b48e-3d7e6f2eec15 | -17.6073 | -57.5099 | 2024-11-11 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 8a70361d-66f2-3391-b979-9ed4a4509654 | -17.6463 | -57.5257 | 2024-11-11 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 42a1698f-710d-367e-b573-fa77b9804656 | -15.9985 | -59.3449 | 2024-11-11 08:10:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| a37ad7ad-e456-3d29-adc9-f96df7c73aa1 | -15.9988 | -59.3248 | 2024-11-11 08:10:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 18246dc1-0819-390c-83e4-1ea6232e5cdd | -17.6069 | -57.5304 | 2024-11-11 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| 3b68b659-5cb9-38f3-b26f-5db0e37d8642 | -17.6266 | -57.5281 | 2024-11-11 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| b650ff6e-2d71-3729-8e79-f2a6b1b8fadc | -17.6069 | -57.5304 | 2024-11-11 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.3 |
| 1a58cad3-03d0-3dce-bec8-96facc10deae | -17.2933 | -57.4857 | 2024-11-11 08:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.1 |
| 58bc1305-80a9-39ff-8eab-f4d213a82f30 | -15.9988 | -59.3248 | 2024-11-11 08:20:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d70b7f38-d233-3f87-993e-814c04b1ce81 | -15.9985 | -59.3449 | 2024-11-11 08:20:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 167553b2-dc93-3f48-b264-cd5b8b572021 | -17.6073 | -57.5099 | 2024-11-11 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 182bd401-1488-39d1-b8a1-0a2ac84d263d | -17.5872 | -57.5328 | 2024-11-11 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| faf1bb02-1d60-371c-a50d-b26f639d4ad8 | -17.6069 | -57.5304 | 2024-11-11 09:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.8 |
| 05c19a26-783c-3b1b-ab21-6ad64b33ef66 | -17.6069 | -57.5304 | 2024-11-11 09:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.2 |
| fdd0c227-9099-35a8-82d1-73c1e3892b89 | -17.6069 | -57.5304 | 2024-11-11 09:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.2 |
| a713891e-9a90-30bc-ae39-3e8e4af0b6a6 | -17.6069 | -57.5304 | 2024-11-11 09:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| c57f829e-ca86-31f2-b744-b9a341cece19 | -17.6069 | -57.5304 | 2024-11-11 10:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.9 |
| 69cb023e-516e-3644-bd8b-15926aabb4d0 | -17.6069 | -57.5304 | 2024-11-11 10:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.6 |
| 09aa02d7-0692-3312-942f-2f0ce155882f | -17.6073 | -57.5099 | 2024-11-11 10:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| ca24c9f8-5db1-3304-a790-2ca8e5904b3b | -17.6069 | -57.5304 | 2024-11-11 10:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.4 |
| aa01363b-2d53-326a-9350-0f8b84304bf9 | -23.9312 | -54.034 | 2024-11-11 10:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 99.0 |
| 9ec1b361-8b17-3108-ab1f-d0d5c94132eb | -17.6073 | -57.5099 | 2024-11-11 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.0 |
| 6f75bad0-ce38-34fd-976f-e2e7fc572ec5 | -17.6069 | -57.5304 | 2024-11-11 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 0c8e5ff3-8403-3faf-b970-c827d202e60f | -17.5875 | -57.5122 | 2024-11-11 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.9 |
| 0adcfb02-7997-388c-b5ec-73c2ee658aa4 | -17.5875 | -57.5122 | 2024-11-11 11:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| 439646ea-c71b-3302-9aff-e9beab66165c | -17.6069 | -57.5304 | 2024-11-11 11:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.1 |
| 9ad3a385-cc40-3a8d-9abe-552f1ecdb32f | -17.2933 | -57.4857 | 2024-11-11 11:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| 5c5daf5f-67d8-38ba-b658-3e99ccf248fd | -17.6073 | -57.5099 | 2024-11-11 11:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.6 |
| c630235a-abd0-3c16-9593-92293d679f49 | -23.9312 | -54.034 | 2024-11-11 11:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 109.4 |
| a38ce061-bc2b-31a6-8184-8491cbb2c90b | -17.6073 | -57.5099 | 2024-11-11 11:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.5 |
| a261e16f-6bee-3c76-a37c-1c138a24f952 | -17.2933 | -57.4857 | 2024-11-11 11:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| fb794b2c-bd80-3f6d-99e9-bd4865a21d86 | -17.6069 | -57.5304 | 2024-11-11 11:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.1 |
| 6cb90619-f7f5-3a66-85a8-48eb78199caa | -17.6266 | -57.5281 | 2024-11-11 11:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| d9785412-3b40-3843-b56d-0209416f1997 | -17.6069 | -57.5304 | 2024-11-11 11:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 4a059ba1-e541-386d-9422-5580a8ac6f84 | -17.6073 | -57.5099 | 2024-11-11 11:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.8 |
| c79230e0-41d8-381c-8784-762f2e2a4f48 | -17.5875 | -57.5122 | 2024-11-11 11:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 6b1657ad-1d54-307f-8cad-1cf3e333fb80 | -17.2933 | -57.4857 | 2024-11-11 11:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.9 |
| b91eeff5-4350-33cf-a29a-872c4d68ad11 | -17.6266 | -57.5281 | 2024-11-11 11:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| e6174aac-227f-327f-ab00-f88571371493 | -17.6069 | -57.5304 | 2024-11-11 11:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.3 |
| ace2a38c-d373-38b3-a406-f63ed4893271 | -17.2933 | -57.4857 | 2024-11-11 11:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 85739324-3c50-379a-be89-a861ddbc0d3d | -17.6073 | -57.5099 | 2024-11-11 11:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| a92d92c8-e4cb-3da1-8969-e31197a1f118 | -17.5872 | -57.5328 | 2024-11-11 11:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 041a5ccb-f97f-3dbe-919c-61bcbc9e0a77 | -17.5875 | -57.5122 | 2024-11-11 11:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 3990c9a4-6d3b-3b68-b80a-66ac7ce2c5ec | -17.2936 | -57.4652 | 2024-11-11 11:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 1db0565c-67ae-3849-9d3a-1376a768db64 | -17.6073 | -57.5099 | 2024-11-11 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| f76f6738-ee11-3b63-8e8c-4ff834958d2d | -17.6266 | -57.5281 | 2024-11-11 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.7 |
| 44d942f9-936c-3d53-96bf-9104b4c01147 | -17.2933 | -57.4857 | 2024-11-11 11:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| a50cecb3-dade-315b-bcca-7e42b97b965f | -17.6069 | -57.5304 | 2024-11-11 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.9 |
| 5f6047e2-29a2-3a7e-8440-bfe7a11c4f63 | -17.5875 | -57.5122 | 2024-11-11 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| d8d9400a-f78f-3146-9b63-8f4317c8bb46 | -17.5872 | -57.5328 | 2024-11-11 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 28a20bdd-40ad-3e83-a94f-483c462c40d9 | -17.6266 | -57.5281 | 2024-11-11 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| 81fafe75-8c8b-303e-ad6c-9fd64043eefa | -17.6073 | -57.5099 | 2024-11-11 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.9 |
| 6d33127a-9660-3b1b-b067-24f60bf77a98 | -17.2936 | -57.4652 | 2024-11-11 11:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| c3486166-e635-3d92-814d-99072cce2c00 | -17.5875 | -57.5122 | 2024-11-11 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 02d96c54-16f0-3c84-abc9-a017fd9cbb9e | -17.2933 | -57.4857 | 2024-11-11 11:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| ebd58f19-9deb-3c3b-9e3c-f7945d27f5cd | -17.6069 | -57.5304 | 2024-11-11 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.1 |
| 420a1842-affc-336c-8a3e-0a7990c194dd | -17.5875 | -57.5122 | 2024-11-11 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.3 |
| b58ccb2b-7ebc-3c59-8520-398923da08f1 | -17.6463 | -57.5257 | 2024-11-11 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.6 |
| e7e01874-ef73-3331-ac55-c4cb222ce996 | -17.5872 | -57.5328 | 2024-11-11 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.8 |
| 9c64356d-da41-3206-be67-0de5d73c8fa3 | -17.6266 | -57.5281 | 2024-11-11 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.5 |
| ab4acc77-03f2-3b33-81c0-aaf9c64c905f | -17.2933 | -57.4857 | 2024-11-11 12:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.7 |
| 882068ed-c222-3222-b156-09f992b2f248 | -17.2936 | -57.4652 | 2024-11-11 12:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| f6499cc2-c6d9-3930-9a73-553311bfc1a9 | -23.9312 | -54.034 | 2024-11-11 12:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 83.5 |
| 1a2e9ed9-f1d9-3e42-956f-14345d2e8657 | -17.6069 | -57.5304 | 2024-11-11 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.9 |
| d6e19e1e-c0aa-3459-8dd4-bc60d01cdbc5 | -17.6073 | -57.5099 | 2024-11-11 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 5a00778d-7704-3bce-bcc2-ffdd9365c635 | -17.6086 | -57.4276 | 2024-11-11 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| abe93206-90ba-3c24-a74d-72fdfdf5cbd7 | -17.5872 | -57.5328 | 2024-11-11 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 01ecd4c1-9cd0-3b1b-892d-18eddb759991 | -17.2933 | -57.4857 | 2024-11-11 12:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.9 |
| 1d829d2a-8d97-34e7-a232-871da065e178 | -17.6283 | -57.4252 | 2024-11-11 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| 29094370-0e4f-3bfc-b58d-3b60ddd7ed85 | -17.6086 | -57.4276 | 2024-11-11 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 006f5187-f7e8-322c-8718-9fe19cf10dc4 | -23.9312 | -54.034 | 2024-11-11 12:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 84.1 |
| 78ae0cad-3b12-34de-b116-917bcb30af97 | -17.6266 | -57.5281 | 2024-11-11 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.1 |
| c058386c-779a-34f3-8982-2b8f95b4aabe | -17.2936 | -57.4652 | 2024-11-11 12:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 3006e554-2dee-3b06-8ee2-0b96c033ef13 | -17.6069 | -57.5304 | 2024-11-11 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.4 |
| e7213ad0-f624-34f6-b7f8-ab40b54ee906 | -17.2737 | -57.488 | 2024-11-11 12:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| b2cceb20-f4cc-352e-954a-bb1833b4952e | -17.5875 | -57.5122 | 2024-11-11 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.2 |
| e4f37a3f-f802-34c0-8218-b7cd35987500 | -17.6283 | -57.4252 | 2024-11-11 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| b664858e-d49a-3aa2-86b3-0cb9acdc419e | -17.6266 | -57.5281 | 2024-11-11 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.0 |
| 4f9e8e9b-b10f-30e3-80d5-ad982c022415 | -17.5872 | -57.5328 | 2024-11-11 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.8 |
| a2b0c7e2-3676-3a89-8d8d-aa454284e2a4 | -17.6069 | -57.5304 | 2024-11-11 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 137.7 |
| 86b61ea9-6898-3e66-bd2c-d47fd396f2c4 | -17.6086 | -57.4276 | 2024-11-11 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 76321d3d-7b9e-33c9-a191-0902b453d361 | -15.9793 | -59.3267 | 2024-11-11 12:20:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 29648b0d-0367-3cb6-a006-fe8b962a94e7 | -17.2933 | -57.4857 | 2024-11-11 12:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 0402a559-a81b-3614-95d9-1d675fc13b8a | -17.2936 | -57.4652 | 2024-11-11 12:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 6d58dd24-87bf-3642-8a92-f05823504432 | -23.9312 | -54.034 | 2024-11-11 12:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 84.5 |


[Clique aqui para ver as próximas entradas](README49.md)
