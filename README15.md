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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9948c873-c9c3-3c0e-acda-8f95fec8bc3a | -1.18864 | -51.97832 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1989e4e6-eef9-3be1-b3bb-725a4523c004 | -2.80677 | -54.13746 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 8fda1ca5-aa39-31c1-9f9b-0637a5835b6a | -3.29033 | -50.61398 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 61fb1dc6-c10a-3f33-a0e3-1d086f91f32d | -2.1773 | -53.2546 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 95d39a36-0b28-3c2d-8181-95bbcb1b02ad | -3.27136 | -50.61672 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 58ac887e-4ead-3487-8412-b0045056267d | -2.18449 | -53.77329 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 817a3b86-0c5c-3cd6-8079-bf073be31b45 | -1.10857 | -53.38868 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 77441ea2-7810-33ec-b793-95e853f32f0f | -1.80213 | -52.74121 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| fda25e97-bfb3-3f58-8c7a-0679db9bb46b | -1.53974 | -51.19231 | 2024-11-27 01:09:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 705159dd-0c4c-3099-a683-908282896724 | -2.44325 | -53.9734 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c8d31838-d067-34dc-b71c-d7dbca72012e | -2.19587 | -53.78983 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ec2303d9-fef8-3c31-878a-0c5f98538b58 | -2.25313 | -53.4626 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 212d5152-4ff7-3f97-9c1c-3848cadf6ed0 | -3.22839 | -50.31509 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 68c5833e-4a70-3797-90b6-793fb3029d96 | -2.57988 | -53.9665 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5a897520-15f6-30e5-8d70-040ade7d54de | -3.34283 | -50.19455 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c82ded84-7b7c-3a7e-aebc-a5c9587e899c | -3.1139 | -53.10634 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cfb72423-354e-317a-be98-a9af22a49996 | -3.10349 | -50.36101 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| ca218c68-9eb8-3d52-a769-307c79331272 | -3.38261 | -50.10524 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1936ff47-65c8-37c2-93c7-c17a05bc39b5 | -3.29336 | -51.15546 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e2c79b77-d80a-3a7e-9d3b-ed78aa7b8fb9 | -2.61481 | -48.36803 | 2024-11-27 01:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3eefae72-3efd-33e5-bf4b-6eec03187041 | -3.5737 | -53.02279 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 620aafe8-b631-3724-9b8d-de55aeaa2944 | -3.93896 | -47.99165 | 2024-11-27 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 4315a5b1-c9c0-345b-8224-5d425f0cd117 | -3.23279 | -54.09071 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 07260056-a331-3ca2-bbf1-2d8931d1bfeb | -3.24157 | -54.22019 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fd7908f9-672c-31d9-921c-498517418786 | -1.96946 | -52.02902 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1ae14e48-ab9e-3ce2-92df-65063a3d9ab4 | -3.33702 | -53.30878 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fb5e8e09-75aa-31ea-ac4d-ee1cadc26334 | -1.66013 | -52.71925 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e27fe309-38b2-35a7-a613-9399a965980c | -2.2466 | -53.62259 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 00d377e9-7071-374a-813b-835b8eb04422 | -1.10979 | -53.39748 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 392cf77e-4d57-368f-a366-73c0be3602c2 | -2.70545 | -45.66087 | 2024-11-27 01:09:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 62.3 |
| ef2b829a-4f2d-3283-919c-759f48e8324d | -1.47765 | -52.66637 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3aa9315f-4288-3f39-9882-177318e7033a | -1.19505 | -53.87956 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d2399b85-4854-3f65-a3a0-b323f95fdc26 | -1.80337 | -52.75008 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| cd0c9203-4d9d-3c22-b0d3-0475ba7b974e | -1.66902 | -52.71799 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| cdf43517-d343-33c0-adf0-ee3f3050a52e | -2.63318 | -51.77012 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 747dbb38-eb8e-37a4-aeeb-1ea1aa9a559c | -3.58571 | -53.25246 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 241ffd0d-fffa-3e3a-9622-03d6a8cddde6 | -2.10002 | -53.36153 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9e6cd592-78d6-3d34-8a6c-ce060d7bb1d3 | -2.69678 | -45.6443 | 2024-11-27 01:09:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 6810421f-2f90-3f60-9f18-381a5a9daf75 | -3.23836 | -44.14878 | 2024-11-27 01:09:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 31.6 |
| c1986112-be55-3ab6-9419-006b6f432ce8 | -3.72901 | -49.95268 | 2024-11-27 01:09:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d7b42752-78bd-3e5f-9fe7-dc41666f7117 | -1.67746 | -46.93527 | 2024-11-27 01:09:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| be80a788-994f-3b8b-ab4c-a2bd1996479a | -1.279 | -54.54493 | 2024-11-27 01:09:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7dcb396f-d877-3ac7-b106-767c8f01ba55 | -2.5957 | -51.83193 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ebd74ee5-1e0a-3962-ad38-89095754de0a | -2.50204 | -54.53318 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 25257b24-76b4-381d-9c78-9c87d4f1889f | -2.59247 | -54.05674 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 63b46e5a-55c3-33b4-9d1c-9153f9cc7b3b | -1.76896 | -53.63047 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 3e35d0c2-b25d-39ff-a37e-6d5609e79fb5 | -2.25436 | -53.47143 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 062b444e-5746-3824-b7fd-5556adb937bd | -3.70657 | -50.43977 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0280f1d8-ba36-3a41-8e1e-1a465ac94d64 | -3.49912 | -53.81605 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 04a43069-0f7a-3016-911f-687519698934 | -3.90496 | -50.60677 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 4651ccb8-2eb3-35e0-a1e4-de6e4207d12f | -3.09048 | -54.1261 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 00a9a146-de85-31fb-bbdd-0ede05b776f7 | -2.79918 | -53.02556 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 69f736b2-552b-3586-9b62-5091dc0bb31b | -2.7104 | -53.1787 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bbe02f82-a85c-34c5-89bd-8ec272778d9c | -3.23105 | -50.1946 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3a0cb82e-d62d-3386-9349-f028d7f7536a | -3.75151 | -52.65276 | 2024-11-27 01:09:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 67560c97-c5c9-30bc-bfeb-726d40ba946e | -3.60883 | -49.8975 | 2024-11-27 01:09:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cf7b2a62-fc31-3353-89c7-39acc2f09186 | -2.35373 | -47.65135 | 2024-11-27 01:09:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 8b617797-cf8b-33ea-9fe8-7b2895c3e3fc | -1.22857 | -51.80383 | 2024-11-27 01:09:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b7619a55-4378-35d3-87c1-f9872f916b61 | -3.01592 | -48.60466 | 2024-11-27 01:09:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c57948bb-ebc5-39dc-9dcf-a72194028bbc | -3.67526 | -53.55977 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 8ce7cdf4-fea3-3b3f-acfe-dfe573a31e11 | -3.44 | -54.12408 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| af577587-6199-3f62-a9ee-b5c59850b4d2 | -2.92878 | -48.63791 | 2024-11-27 01:09:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 5246e805-1af4-3b81-ba2e-2197e493e871 | -2.57189 | -49.09662 | 2024-11-27 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 06e28fd3-0d89-3134-abcd-e96fe682c5ac | -3.28796 | -51.11684 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 94b17709-5f65-32f5-94ad-eb55e86d612b | -3.24426 | -53.64185 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 00ee062f-9924-386f-9288-739a3dffcf55 | -1.6205 | -52.3689 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e3ed8cda-003f-3087-8aa5-02fc62f4e440 | -1.69151 | -52.60861 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 496471fd-c66a-388c-8071-77b9dd601073 | -3.05758 | -53.68941 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d28046ab-4bab-36fc-adbc-9e4c747ad86a | -3.03922 | -51.77556 | 2024-11-27 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 48fd2b4c-4b06-3053-9a8f-67e640dfa4ae | -2.78829 | -53.20672 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 889f5f9c-4868-34d7-97d5-822a349a15ac | -1.36625 | -52.12943 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 328a085f-ff59-3afd-a465-d1ded09a6ff1 | -3.10065 | -53.7379 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4f5a696b-0730-3b86-82b7-fdd159c502bc | -3.10759 | -53.98462 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| adac6a7e-87db-339c-aae1-94be7c547159 | -2.28746 | -47.9189 | 2024-11-27 01:09:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 2d763592-6636-349f-a75a-c1037cec59b8 | -2.80701 | -54.07257 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f5988afa-5f3a-3c6d-aa64-09eacbd6a528 | -3.34711 | -53.31638 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e32b6045-dce2-3ea7-a8b2-535284744502 | -1.31273 | -51.74754 | 2024-11-27 01:09:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6aef4729-0f17-3760-adc0-403f0dc37302 | -3.46748 | -50.26233 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1d0404cb-b977-304c-9e37-a67d97e44da5 | -3.5007 | -50.4922 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 23cde432-4569-392b-b65c-7d1a6c7c1b2f | -2.97542 | -51.58316 | 2024-11-27 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| eec84f7c-c909-32cc-908b-f3c5a32dfd16 | -3.23932 | -53.93577 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 09361bf6-ec43-3d8e-b03a-2bfb188a0e5d | -3.19045 | -50.83028 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 70120e48-fbd1-3e4a-832e-baf7df8a2c77 | -1.39887 | -53.55396 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 38ecddac-ab29-3451-afa4-3f7df960bd54 | -1.78312 | -52.73485 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 339813a5-cb6d-3ef7-be8c-18e1c486bf6a | -1.66029 | -52.25544 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 541f7bac-2631-3dce-97a0-8640f0a5b573 | -2.81837 | -54.75892 | 2024-11-27 01:09:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 454a7057-32ec-3bfc-9b97-02bc1b97d302 | -3.22381 | -54.09205 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 3ac597d8-4da1-3fcf-953a-ce6393e75d64 | -3.43872 | -54.11488 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1e4d7709-d06b-3823-bbe2-70fd6ee9a2fc | -3.67402 | -53.55085 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| cd6c0fe4-a270-3d5b-8d6a-b7dbd4614b56 | -2.81969 | -54.76851 | 2024-11-27 01:09:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5799ee39-1868-3f12-94e8-1929bb04f873 | -2.70201 | -51.99718 | 2024-11-27 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3cc2693a-ca15-394d-9685-55296aaa5d09 | -2.86521 | -46.82009 | 2024-11-27 01:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| b393387d-2a69-392f-a809-992423f04cb9 | -3.0898 | -50.35811 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 19c522d4-0c68-32d5-ac32-a7a6cfeb07e9 | -1.20361 | -51.75916 | 2024-11-27 01:09:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d662362e-0625-374c-b5e8-739c1c56aff9 | -3.12257 | -53.7559 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9731bb5a-33c4-31bd-8208-77ef56032ee9 | -2.83785 | -51.85086 | 2024-11-27 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fa20f3a4-da5a-3ce1-890b-6e8339041211 | -3.96037 | -49.35279 | 2024-11-27 01:09:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 653d76d7-5fd1-3bc7-b25b-c789f7b7da07 | -2.80803 | -53.02431 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f4537ddd-022f-39cc-a493-1ca127ce5a70 | -1.4873 | -52.53119 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6dd0feed-5b08-3986-ab19-569c597f306f | -3.09137 | -51.02821 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README16.md)
