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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20c14208-3acd-3164-bac0-3fd2963d31d7 | -2.94352 | -51.58645 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e6e3bb6d-fcd4-3953-983a-397cf69356ea | -3.06114 | -53.28318 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cdf4b10-91b6-3e18-9b4f-f99a4f89fae6 | -3.24694 | -53.63464 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ece64e49-25b6-3c08-9e80-61e7860cee1d | -3.71137 | -53.7533 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0de0d75-05d1-3ebd-92ea-605a379be14e | -3.52884 | -54.32642 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e3c29e9-faaa-33a9-bbbc-a413637d22b8 | -3.31398 | -50.49897 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47df6a15-4476-36e8-9159-ec775df0823a | -3.51969 | -51.65602 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5004e319-33b6-3874-96b5-24317869b5d3 | -3.10015 | -53.73648 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51b7a571-85bb-3fde-88de-c9a33835c605 | -2.83324 | -54.11361 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf4a4dd6-d042-3214-83bb-fcac434987ca | -2.54585 | -53.99468 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ed49079a-3dd5-3687-a6df-0f621f80a98c | -3.39211 | -54.27934 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e4b9293-085b-30a6-85c0-79d5c83757b3 | -3.73338 | -54.22485 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2ac181b-27a6-3b44-adc5-3e9ae165055e | -5.09295 | -45.83953 | 2024-11-28 05:18:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ec29625-5340-319c-821f-dc04925ab26c | -2.80105 | -54.11842 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87a8af10-7f90-3491-87af-02bbb51f55ce | -2.01589 | -55.39151 | 2024-11-28 05:18:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ac6ce35-3d15-3c3d-b872-9986a16f896a | -2.81733 | -51.30162 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1026f480-f1b1-3b58-8ad3-418f9177d29f | -3.24315 | -53.29211 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0949389-a7a7-30dd-95fd-f2b8465e1000 | -2.83562 | -54.12371 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 41ddbc15-c09b-30db-b350-77fe21d1d9af | -3.09732 | -53.80751 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 159ea6d0-bd10-3ac8-873b-be59d4267336 | -2.87335 | -53.98211 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b21a894a-f572-3842-909f-d878c68eb0c2 | -2.80767 | -51.58721 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2d5c8519-d5d5-3a31-ba02-a14af3d17eb8 | -2.93107 | -49.44024 | 2024-11-28 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac320bf3-9a5f-355e-9b50-c99f4ff9ff33 | -3.91569 | -53.67091 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 92559a3c-8ea6-303d-959b-d14253e68d08 | -2.74048 | -54.16429 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9765310a-fa9e-3683-a4c7-e4c1a357aa44 | -2.79815 | -51.80846 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7614385-40a7-333f-a343-dcf93db4ca01 | -3.48008 | -54.67347 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf2501fa-333b-3fb7-a255-23a4b95abd6a | -3.09783 | -50.36613 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 772fc5a5-82dc-30d8-8b72-4f7a660c42ca | -4.089 | -46.1438 | 2024-11-28 05:18:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 263d20a3-e7fb-3917-ac6f-3c7ccf27ddbc | -3.09005 | -51.02905 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a47368f-4c66-3ab7-8143-feb414f8c92c | -3.2958 | -45.51872 | 2024-11-28 05:18:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b82aad65-17fe-36d9-97c0-e51559587c95 | -3.41498 | -50.16058 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6c828970-2b2c-3082-802f-af4b88dff7c9 | -2.59891 | -54.07273 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f767d555-4b33-37b3-89da-4e4c8765aae0 | -3.09697 | -53.73082 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fd9b73b-89f3-3b22-b762-4284600a02b6 | -2.75669 | -54.12609 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 290dcf4c-7ad0-3ed9-8240-01bbbe6a7f51 | -3.24753 | -53.64217 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| abf587d6-7a31-3789-a129-1e4c96427ccd | -2.82252 | -51.79862 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46e6df8c-0742-35ed-a301-25f0eeec01b2 | -2.73955 | -54.16216 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49a02c87-b1ee-3968-b1d1-d0871ab527c9 | -2.78916 | -53.20893 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68040695-2cfc-3a62-ac7a-e1f7fe658a1e | -3.38599 | -51.23704 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a42a2e25-1af0-38bf-89fe-213a40bd0915 | -3.36924 | -50.82492 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ac2c53a9-bed8-310c-bf74-f45cc308c93b | -6.12017 | -46.58873 | 2024-11-28 05:18:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efc5166d-3697-3b20-87dd-98e16a05a66c | -3.09301 | -50.35915 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 26c6bf7a-c190-3327-84f8-e9cffa60fbde | -2.31638 | -51.96063 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f5028404-9988-3817-83b1-74b2e8fd329d | -3.31554 | -50.27677 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2adff7c8-8664-33e5-a0df-d48f0ec5569e | -3.41926 | -53.88266 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 490184ff-f3bc-3bcd-8c7a-3656bd04c4de | -2.87306 | -53.9936 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 351b7118-c2a0-3ee7-ba57-34ae4394093d | -3.1005 | -53.813 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2363b08c-6bb2-3608-89a1-c65ea764da21 | -2.54134 | -54.06367 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| defd8e72-7477-37bb-8a4c-926b7c6c6174 | -2.59197 | -54.06675 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8469a736-e081-33fd-b718-5c87dc37bfac | -3.05828 | -53.21987 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33ab82de-378c-3105-9ef3-d7bec1cf31c4 | -3.13203 | -51.04062 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c723cab0-9b61-39e5-9f17-f327ccd4a11e | -2.82629 | -54.10768 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28fb3b1f-6e0a-3928-bd17-f0649f829d7f | -3.20443 | -50.91478 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6397c8c6-f2bb-3b69-ba10-f4b7802c5f96 | -2.98491 | -53.88572 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2b39fb2-c4fc-362f-a5f8-c7e2da7e1e3c | -2.82843 | -52.94421 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b26a47d-2b49-3b54-a94d-4862e36271f6 | -3.74217 | -51.83704 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 22977fd2-7c46-3e14-9b45-8843b0ffcbde | -4.17684 | -48.63002 | 2024-11-28 05:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b59d15cf-484c-3637-94d4-713b3a3609f2 | -3.91288 | -47.19924 | 2024-11-28 05:18:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6e7aee86-0d7e-38cd-96cd-e21486f760aa | -2.88648 | -54.16719 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63045fe2-69fd-3090-9a7b-f118079074ae | -3.25092 | -53.6353 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a2cd004f-a8c4-344c-abf2-d4c5f1bb9e62 | -3.40926 | -50.98657 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 684998fb-2dba-34ab-8a0b-eefdf2d19bd9 | -3.24506 | -50.76756 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7e86a056-73d0-3a71-9423-7d1a0dcf2248 | -3.25216 | -50.61383 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2591bcc7-199c-372d-886c-b0d5726ac3d9 | -4.35365 | -48.68713 | 2024-11-28 05:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f3d5120-4073-3fd1-864c-2a7da5d69278 | -2.93634 | -49.44116 | 2024-11-28 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cefec914-9c01-3f73-9f6d-f2762a872371 | -3.18128 | -50.28424 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ee3dc35-66a2-3e04-a2e8-908e84b04be0 | -7.94804 | -49.75237 | 2024-11-28 05:18:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 431619fb-d158-3720-96f6-9898812d0d58 | -3.05009 | -54.03746 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 550547b8-1c95-3a23-a9e2-6986ada8ed06 | -2.90038 | -54.17902 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d4d3cd9-d49c-383d-85b3-e6c54ea5637c | -2.96098 | -51.00202 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 44558216-71cf-3db5-81c4-8da3c19fa234 | -4.21988 | -50.89748 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7cedc604-673b-3440-90aa-ca76d31cc98a | -2.86746 | -53.97785 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 91f01243-c405-38ef-b637-769909e9db43 | -2.80728 | -54.1291 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14c51c72-ead5-301f-a2c3-1dc9b46b91a8 | -3.23491 | -54.22212 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ea4102b-0383-37c5-9c3f-045be803b23a | -3.84481 | -50.09274 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e81f7062-13b2-3de5-8f97-b1d4e4547566 | -3.58966 | -50.36396 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73186c91-63ae-37f5-b629-7263ac588ddc | -2.80656 | -54.13382 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cbe8fd17-2eda-3cb5-a9c1-0ee24b735836 | -3.11279 | -53.75611 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a8c3563-3744-3881-83f8-f4c99d184ac1 | -3.0841 | -53.29718 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c911c7a-89de-3097-a8c6-1f0be9c5d9f5 | -3.39105 | -50.32115 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59ed755f-2679-393a-aa0d-914428281f48 | -3.10794 | -53.81647 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b5f70f42-26f4-3184-8e84-9f0dff5adad5 | -3.31562 | -50.27796 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0722935-eab5-3cd2-813c-c28aba74cc7e | -3.69105 | -50.23166 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6591a48-f90e-3da6-8253-3c1fd626ce9a | -3.20592 | -46.59992 | 2024-11-28 05:18:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5165a84c-dc3b-35af-9ab0-f4f622b71c87 | -2.74639 | -54.03662 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 308ca391-1568-3193-b52f-b584509415cd | -3.8577 | -50.147 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc50eb40-7125-3b37-a6d1-b4cb16ed090b | -3.92371 | -53.67218 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 801e0d41-71ec-3c7a-97e6-0869f9906618 | -4.24525 | -54.73734 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcff4c39-852b-324f-887b-ee68d5006ba7 | -2.9732 | -53.88386 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b30bd5ce-67ef-37b0-ad26-2469a9293cdf | -2.86635 | -53.97608 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cc4610e9-f1bf-3f40-9d40-818674f32ba7 | -2.97295 | -51.57668 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44bba858-f86c-3467-9def-4b5cf71cc2c8 | -8.12903 | -47.98301 | 2024-11-28 05:18:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a2ff799-3f9f-30aa-9b53-6d29c19f65a4 | -4.43805 | -46.34322 | 2024-11-28 05:18:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3af7da47-c186-369b-882c-a5f0db8a949c | -2.5941 | -54.23134 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9863f4eb-35d6-3f3e-af41-3704097ebad9 | -2.98391 | -53.35551 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c918adc9-7644-3b5b-a7e1-73854b982807 | -3.04758 | -48.51982 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99d2756b-64f5-3cd1-b344-623b20d1a009 | -2.75118 | -48.66121 | 2024-11-28 05:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 800c3316-c5d5-3ea9-a954-b4543c322594 | -2.80117 | -53.04294 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95984e34-ac9e-3ce8-8d83-b3bb0d5840f9 | -3.52727 | -50.75161 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65ae7b7d-166b-3226-9f2c-dafcbc9b2b97 | -2.94877 | -51.58245 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README84.md)
