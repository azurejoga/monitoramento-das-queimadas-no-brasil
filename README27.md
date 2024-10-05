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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 476703b0-4bf4-3e92-810c-3890179a2832 | -16.92072 | -57.70388 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 8c0d40c1-27c8-3fcc-98f4-dfc6a78e6520 | -16.9192 | -57.69374 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 19a1a194-20f4-3287-afd7-fb537784e5ae | -16.89142 | -57.69834 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| dcd8e160-167e-3d0f-9fa9-5f78fad41e56 | -16.88989 | -57.6882 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 0b0db131-0fa4-37f3-a230-f99df1076740 | -16.84638 | -57.46405 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| c663c25c-5d73-3a31-b723-cfb1c1470a54 | -16.83224 | -57.47228 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| b4b119c4-4148-392d-97ea-833a0f79a69c | -16.82668 | -57.81827 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 7311ea6a-184d-3f5e-96f9-ed550480da91 | -16.82518 | -57.80823 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 1333fdf6-2225-3205-a6d2-88555d3e7fc0 | -16.82132 | -57.46345 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| a4bb4d7c-d4c3-3c73-81be-853ac72ac91d | -16.81977 | -57.45305 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 3498fe8a-a8e5-3f9d-8ead-a3177e55a3c9 | -16.81746 | -57.81979 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 3705c54a-5c29-35d0-8691-a51874c4b7d2 | -16.80824 | -57.82131 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 74e4b1d5-06a7-34cf-87d5-0d9f65fd6ce1 | -16.80102 | -57.39197 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 7ea191d3-9e72-3ab0-a21a-3cd5ab8ce83c | -16.79287 | -57.83027 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 36009588-d7eb-39da-8b7f-0461c8be7b7c | -16.78851 | -57.43692 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| c145482c-d19e-3bb2-b3a1-53af7333d776 | -16.78697 | -57.49046 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 26f26ca0-aed7-38b9-9d0a-784fdc00c76f | -16.78541 | -57.48009 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 7918a177-1445-37a5-b585-389b7d583725 | -16.78513 | -57.84182 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| a16e6fa5-04a8-3e73-a052-f4b2f6fc0cf6 | -16.77604 | -57.48165 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 5678b868-a940-383b-82cd-dfba5e781ed8 | -16.77447 | -57.47127 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 808caf08-d003-37a9-a4b1-92e6941dd8c0 | -16.77289 | -57.46087 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 62f84598-0b1d-3a28-bbf0-9e5119653f2e | -16.77132 | -57.45047 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 1dd621a4-dfe0-3620-b532-161e46929c7c | -16.76974 | -57.44005 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 36fd20b4-9aa1-3244-82f7-6e81ecf750ad | -16.76667 | -57.48321 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.3 |
| 87b6e17e-92ef-3c0b-847b-3cb7d5ba7b7c | -16.7651 | -57.47283 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 94b4cd97-5fac-3677-b8af-d5f106d628d9 | -16.76352 | -57.46244 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 7a20254a-364e-3356-9cd3-1abf406deb0a | -16.75889 | -57.49514 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 81b40d9a-5937-314b-8241-9e07981c7ce7 | -16.75731 | -57.48477 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.3 |
| a129056f-bbe6-3176-9176-cbfe93a9f779 | -16.75414 | -57.464 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 4399ec46-d507-34e8-acf6-d090656bd204 | -16.74794 | -57.48633 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 178988f2-03f1-3f10-b705-8b6367d853cf | -16.74007 | -57.47279 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 7a31d8e4-fb98-3c3f-bbd7-d6eda55db66b | -16.73853 | -57.46238 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 991c03fd-ccf3-32d3-8796-b270e33b695e | -16.7307 | -57.47435 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 5a6b5053-a331-32da-a730-089562a83710 | -16.72915 | -57.46394 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| db83507e-b744-39bc-849e-ea5f77dd5743 | -16.71976 | -57.46551 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 63f9911f-1f47-329f-8f10-3c422d6afe29 | -16.71821 | -57.45509 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 1d7e6bc2-4ed2-3521-a131-1caae4653c9b | -16.71038 | -57.46707 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 00f1c78d-26c9-384a-bb06-985c263fd04c | -16.69925 | -57.16971 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 925f5c4b-73ff-38a8-af83-c491d1779524 | -16.69758 | -57.15896 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| ecb70dde-486b-3d37-ba6a-eea52f59d50d | -16.69431 | -57.16594 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 3f1863d7-c8a8-3349-826c-1d717a66d103 | -16.69005 | -57.45979 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.5 |
| d29240f8-c6ee-30ee-ae7b-6402b5480c29 | -16.68848 | -57.44936 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| ef2df514-3a8e-387b-826b-7fd10d46ed3f | -16.68681 | -57.37448 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.3 |
| 9f9cdefa-b079-3e1f-afd5-9cfce571f5cf | -16.68522 | -57.36395 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.1 |
| 93861764-e350-3d5a-81f1-95e87e48ea64 | -16.67909 | -57.45093 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 8eaaa7bb-e24d-3792-8fbe-d30d1d5ce29a | -16.67739 | -57.37605 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 9b397ea0-1498-3715-a17e-39006b6215c2 | -16.67579 | -57.36553 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 15df4cc8-f16d-302b-a683-6532e4b292ae | -17.04007 | -56.79535 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 07d8401e-6c00-3fbc-8b25-3d590b79610f | -17.03761 | -56.71519 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 38c0b39d-40e7-38f5-87b3-40fdc24248a8 | -17.03586 | -56.70391 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.0 |
| 68002e39-5ae0-377d-974e-9c67d1ea3e1a | -17.03038 | -56.797 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.5 |
| c41e08ec-e2f4-38bc-a92d-a0b28b2e28c1 | -17.02865 | -56.78583 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| d3d589ad-020e-3b0e-8cb3-15c9deab2d7e | -17.02613 | -56.70559 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 8e254416-2962-3b75-be58-9d842a9db23b | -17.02167 | -56.74103 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.6 |
| 03d85761-5426-345f-b0f8-36d6fd240693 | -17.0207 | -56.79865 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 8f87e446-e84a-3126-84a6-b2dae5f39af6 | -17.01991 | -56.72979 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 460866f4-061e-3270-a136-cc2f52939688 | -17.01896 | -56.78749 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| a51a5885-efb1-3d5e-94d6-c9a725cff891 | -17.01195 | -56.74269 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.7 |
| 1bf2002b-d71b-3f5a-8968-4b14bd778f9d | -17.01019 | -56.73145 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |
| c8378d76-fed3-352f-811b-d7a7b566f95c | -17.00927 | -56.78915 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| c63e6269-58a6-3d63-8127-70a526f2f0fc | -17.00746 | -56.79579 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 6979b0f5-20bb-3fb1-b3a7-d75252ee4ec1 | -17.00577 | -56.7846 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| 9f87df6d-7aad-30cf-8d0b-ac476df65dfc | -17.004 | -56.75557 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| d60f8141-4100-3e4e-8353-0450f3bdc6ee | -17.00237 | -56.76218 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 01baf857-485a-3538-bf49-af3449936ad9 | -17.00224 | -56.74435 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 33db517c-9e84-3269-8ff3-b59f893b689e | -17.00067 | -56.75094 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| a5764884-7ffc-3efd-b713-c9b05966a082 | -17.00047 | -56.73311 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| d9dc16c8-c14b-3282-9294-d5e5775cd08f | -16.99896 | -56.7397 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.4 |
| 935a28cb-1f9b-324d-8584-9b3a03fcfc60 | -16.99777 | -56.79745 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| fb88f6df-22b8-36aa-aa2b-727daf2c7493 | -16.99607 | -56.78627 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.9 |
| 12a749a6-dbfe-3f2d-b6cb-ad9f6690957c | -16.99437 | -56.77507 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.5 |
| c45fd648-7aff-375d-891a-361d0044c3ef | -16.99266 | -56.76385 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 44.2 |
| 3f478524-fc5f-3851-ac17-991c83bdd2b7 | -16.99095 | -56.75261 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| c2e5dedd-4159-312c-ba8f-1ee785f69017 | -16.98638 | -56.78793 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.5 |
| ae74c766-638b-3366-9b0d-c82d5fa55fe4 | -16.98467 | -56.77673 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 141.7 |
| b347728b-7fe8-3776-b87a-bfe3c5e3f191 | -16.98296 | -56.76551 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.3 |
| 98ff925a-1918-3bb5-9f0f-b2b57695f9ad | -16.97668 | -56.7896 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 0d9b0cfe-9e89-316c-b2e8-021d74175d8b | -16.97497 | -56.77839 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 313.2 |
| b607d48c-bf56-3905-8db6-ff9604bf8d23 | -16.97325 | -56.76717 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.7 |
| 08b7c864-3ea5-37b1-9aca-00f319d72f5a | -16.96527 | -56.78006 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| c40b2cea-a3d7-3bbe-accc-7bf40dd49feb | -16.96354 | -56.76884 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 2eaefcb2-efe3-302b-87de-fad09b4221ba | -17.15971 | -56.97264 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| a462f3bc-8278-31c0-a305-0a26d67f0d47 | -17.15803 | -56.96172 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| fca95916-911f-3167-9b4a-d3dad4d7a1e9 | -17.14669 | -56.7597 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| a91657e8-c4cd-3923-b1c2-080c4de357cd | -17.12558 | -56.75184 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| bdb78a27-fda6-336f-9daa-86e536680ea3 | -17.12384 | -56.74063 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 6b3448ec-1922-3f48-b463-2c164315c7b8 | -17.12111 | -56.78701 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| f8e8ae80-8bdf-3ca8-8f30-30a112dc845b | -17.11937 | -56.77586 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 1b79ae06-7988-3a67-ba61-8aa2fbd5101f | -17.11589 | -56.75351 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 14891945-5b96-3d22-9779-514253872289 | -17.11415 | -56.74231 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.9 |
| 22aaaab5-eac4-3a37-914c-e44e2d7eb4e5 | -17.11317 | -56.7998 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.7 |
| 7924a467-4469-39c3-995e-68646681a655 | -17.11143 | -56.78867 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 9b4f2178-01cb-32ea-9859-53c03640b5e5 | -17.10969 | -56.77752 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 53a9b03e-7f6c-334a-ab45-8c82fb8778b2 | -17.1035 | -56.80146 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 54eb39c1-42d4-3855-a301-7c4355237764 | -17.10176 | -56.79033 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 54bb9f5b-69cf-375b-bfef-40815fc195ef | -17.09984 | -56.79655 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| b425e653-2cc0-36e9-b125-ad5b5e55c877 | -17.09017 | -56.79821 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| f774a390-ba92-36d8-9a45-d7be7a882ee3 | -17.08847 | -56.78705 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 6c1d8187-3849-387d-a961-ca1123a90746 | -17.08677 | -56.77588 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |
| 0869847c-ffee-32a8-8ce6-fb78f0c2f028 | -17.08507 | -56.76469 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |


[Clique aqui para ver as próximas entradas](README28.md)
