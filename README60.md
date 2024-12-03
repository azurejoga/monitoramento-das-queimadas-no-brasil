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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d2039a5-8f51-3aa4-b6d8-8454219dd352 | -3.54464 | -51.50066 | 2024-12-03 05:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24ca281f-a047-3d96-aa99-785e5c0af505 | -2.44108 | -53.8837 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dbbc534-e687-300d-950d-55a75e09fa6d | -1.52192 | -60.32317 | 2024-12-03 05:25:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3e03b10-b4e1-3339-a99b-6899e88fb563 | -3.00833 | -53.211 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7435ee49-80b8-3296-9643-da92d3bd2261 | -2.78501 | -55.36003 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fe8b0ff-d8f0-3d61-9119-cbbdccb374c6 | -3.40433 | -50.22977 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fab10c07-f7d3-31c4-8729-179ce0a6d7b4 | -3.25921 | -53.62508 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 34f5ddb5-e8fd-3897-a103-75d55c4235fd | -3.26478 | -50.21556 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e714e58-bf83-32a5-996a-3661000b64f1 | -2.36062 | -53.93081 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83d9fa83-5f17-323a-83fd-2db86323249f | -3.30292 | -53.66702 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6118b1cf-92c4-31d8-9411-f48dbccc0e7f | -1.70206 | -52.62725 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 919e26fe-8146-30f4-bbf9-7a7a8950b7f8 | -2.2621 | -53.60954 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77b71059-4882-32a9-8d1a-569ca2ba7600 | -1.66682 | -52.39799 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 626c53a1-8944-3c64-872b-c267a9834bac | -2.20087 | -53.77893 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8ab93f45-6325-33bc-8b54-b12176b35ac0 | -4.17261 | -48.1911 | 2024-12-03 05:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bcf23578-7f5f-35a6-9ba1-bf2a7cbda73f | -2.60628 | -55.71228 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afa4ac50-9c60-33c2-a0b3-621347d5dc00 | -2.78493 | -55.36145 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 075f73f5-50b9-347d-ab87-32e19eeccf73 | -2.33444 | -53.81492 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 412f5ff3-e9d6-3167-b1f7-425ed241690c | -2.79353 | -53.04964 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 117fc514-0a1a-3e90-a72b-7df9ef6081f7 | -1.30125 | -52.85544 | 2024-12-03 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88f05e33-eb45-3519-b6c3-1493ed7cb93a | -3.35132 | -51.20897 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1bceb90-3f9e-3ca9-a460-a0dc793e95ec | -10.46652 | -58.67834 | 2024-12-03 05:25:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3765a147-20a7-3e70-906e-334c9e2d091f | -3.25631 | -50.62034 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64a307ff-20f4-3d43-b323-9f337b769d8e | -2.63802 | -54.20955 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 921a1bbb-0009-3efe-8de1-6672f5107005 | -2.2058 | -53.77552 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd17236e-2eb8-31d3-bb1c-3d53ed264913 | -1.75663 | -52.79689 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 026770d9-5a32-33ac-a912-0a88458d0c49 | -3.25865 | -53.66339 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 92b3f455-fe55-3bed-9c2a-1119e73bb64b | -3.2653 | -50.21197 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ab4e3e9-14f2-3040-ad5f-206d6c913647 | -2.7854 | -51.71635 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 057d5b87-f52a-3512-926e-2da57cd25f93 | -1.88106 | -53.30242 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d61a3381-7f41-33b9-9ed7-3bae4640fdc9 | -3.10437 | -53.28858 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9b0c19a-2e7c-3e49-9150-c39a00aa993b | -2.81553 | -53.05948 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea7cc066-0cfe-350e-b4b7-32007a1c59f1 | -12.79804 | -61.50322 | 2024-12-03 05:25:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 60d2b0c1-5a74-3b20-890d-a4a56e15862a | -2.63319 | -54.21286 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d61d653-766c-3cd4-9193-31c47db98659 | -2.78109 | -55.35947 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddd2e3d8-e1b5-313e-a035-0e356122964b | -1.94597 | -53.34691 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8f37ec4-e807-3cff-9250-eb91f957ba2e | -3.26872 | -53.62208 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e07ab463-2159-3d32-a891-2bc5bbed3163 | -3.26197 | -53.64171 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43d36773-2f30-3d52-90e9-8999e67dbbf5 | -3.10919 | -54.03562 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 375e65e4-9697-34e7-b855-bd8072a0cadb | -2.45315 | -53.71712 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 104f08c9-c432-3303-8bcd-b2418bd8a80d | -1.74066 | -52.62339 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ccbec745-0840-371d-9177-117855af8944 | -3.2617 | -53.34021 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8a0ceb06-4358-3647-a066-5e759c8d72a1 | -1.95107 | -53.34322 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8d85b6cb-2fa6-38b0-acb2-2baf78198d45 | -2.35454 | -53.71205 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc286de2-bcd5-3fa9-a041-99d14e08268f | -2.56367 | -53.39903 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1d24500-6303-3983-a085-bc7dfe3219a3 | -3.01943 | -54.03103 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52aff00e-9d42-36fc-97f9-6dce8abb25ae | -3.32532 | -50.22112 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75d1bea7-4617-32cd-a67f-255908f5aa74 | -1.74163 | -52.64827 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ff39633f-7ef1-30db-b10b-036efefbfa17 | -3.1046 | -53.23335 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 407ebf5f-8683-303f-95e6-032fa80a08ed | -3.02956 | -53.87252 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b220c952-2568-3265-b31d-161cc2d54785 | -3.08169 | -53.09949 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6cce23c-578a-38a3-b0a2-35458bde8f9c | -2.81788 | -53.04383 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0dd14224-1742-3a12-a7ca-2ed24db86307 | -3.02656 | -54.18827 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad87bd7d-8a24-3a9a-a7c3-3fbdb90f1cd7 | -3.18617 | -51.16352 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c48e8e34-718d-3778-aa55-e6f0c40515ed | -3.55059 | -51.46031 | 2024-12-03 05:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96aaee0b-6b71-3072-870c-ea57693b4ce4 | -2.41722 | -54.15289 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11f09cc6-3725-39f9-8f9f-f731ef0f80c1 | -3.53994 | -51.4967 | 2024-12-03 05:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e699386-a017-3368-839a-d327b10a996d | -2.72579 | -54.17344 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8ca275d-23b7-33d3-8639-e8a6e88ff152 | -2.98663 | -53.35228 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f98d67da-bb11-33f0-ac10-a4a536a69773 | -12.57749 | -57.81164 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5d87192b-10fb-3670-89d5-3450466a6fb6 | -11.26292 | -60.765 | 2024-12-03 05:25:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b39f713d-7405-30ac-a40d-001cbd8fe0cb | -3.1899 | -54.51297 | 2024-12-03 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7882658-a168-3978-a741-dd6fc52c7cbf | -3.25922 | -53.65634 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a9c72d76-04c8-3bba-8194-3c3517fe4b44 | -2.00108 | -53.28375 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 007ea3fe-f204-351a-b0a3-767856f233d2 | -1.40118 | -53.6648 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6003da9-0482-3f00-b853-b7d5c4512fe6 | -4.16219 | -48.59106 | 2024-12-03 05:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 63c8d21c-d924-3d54-a489-6962158fe2d6 | -3.02682 | -54.04044 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f164e021-f5bd-3bdf-b67f-1380e585d3fe | -3.08151 | -53.37757 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6269844c-22d0-39f2-9a70-b3e59ec48b03 | -3.27286 | -53.62983 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4c2597a6-2d9e-324e-9f20-b2653adb7bb7 | -2.98793 | -53.90232 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a18ccc6d-7411-3d0e-aa58-52458144b577 | -2.80885 | -55.30851 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e53467cf-5a07-3772-b8fc-cf273987baf0 | -3.26908 | -53.62487 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b4c036e4-ff22-3815-a492-733828b9a503 | -1.65985 | -52.75277 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d87059a-c87b-3d59-b596-fad136bae4a0 | -3.26809 | -53.62645 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dfae1a64-8559-3d45-86f4-843f67ca9b73 | -3.34653 | -51.20499 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 246d91cd-a80d-3fef-9d50-251adbb67082 | -2.44666 | -54.01167 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd5dc915-d064-35e7-bdbf-9c44f1ac2aca | -2.86582 | -53.9944 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c720037-ab8e-3478-b887-01edf1f35b58 | -2.56432 | -53.39465 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b431c1b1-bf13-3e99-bd3d-9777219a6625 | -2.78346 | -55.37004 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a73bce2-8187-3752-ac4d-f31e4fd6456a | -13.11311 | -58.04375 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35381d52-774a-35ec-8f73-fb3e72f77201 | -1.75422 | -52.78205 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 985a90b3-2e44-3874-84be-62a7ec6838f7 | -3.55151 | -51.45409 | 2024-12-03 05:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 393307d9-add4-3181-bba3-6709d9d99e58 | -1.26136 | -53.37695 | 2024-12-03 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e41db41-20c4-3a95-b35a-d45a232df209 | -2.81042 | -53.06187 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b193685b-9772-33fe-9500-99411209c0ee | -1.73971 | -52.78462 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d876ca8b-86a9-3e18-b5d0-2a91384d4b12 | -3.18528 | -54.34241 | 2024-12-03 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c0d18fbf-1fa4-3679-9dd4-c9a9977311c0 | -3.25799 | -53.66769 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d4fdeb6d-5279-3011-bfb1-339d90c76da2 | -2.44431 | -54.02767 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c8fecc6d-0ea7-3892-bd2b-9638446da2c6 | -1.74457 | -52.62895 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98de256b-e1a8-3145-af9a-c5aa9fcd291d | -2.71144 | -58.29481 | 2024-12-03 05:25:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d31dbe35-6fb1-3ced-bcc9-1a7995089d87 | -2.81257 | -53.04782 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f9a0995-d9d5-3e98-99be-aca1e656a592 | -3.25184 | -54.21627 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca9efdfc-199d-3984-9c8c-76e64676936d | -3.28313 | -50.79156 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cf39d5e-d996-306e-84d7-f65006dfbe7e | -2.80247 | -53.0526 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76253b69-cb20-38ea-8ad6-cca4ec2c78e2 | -2.88542 | -54.00996 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60a0039b-91ca-3938-af9e-6a07e2225fa8 | -2.80842 | -53.04392 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a2f9cafc-c061-3f1f-adec-90ff869fe09a | -3.09214 | -54.29873 | 2024-12-03 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b04f5516-439d-33a0-a0df-6a0286a56cc1 | -3.26048 | -53.64765 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c849865-5b20-3c16-8450-00fb5492b493 | -2.98731 | -53.9064 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 612eea4b-8b41-3b33-bc80-06d5c67bb566 | -1.99662 | -53.28306 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README61.md)
