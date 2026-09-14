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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c425e056-8c2a-32ae-a368-bd8aca5d633d | -4.45654 | -50.158 | 2026-09-14 04:51:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f6fdcd1-4919-3f27-afef-d9589a564dbd | -3.79407 | -44.10564 | 2026-09-14 04:51:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d12f32f-ec8f-384f-a3b1-bcebc1515454 | -2.70059 | -57.54449 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f2613421-2af8-3847-8f82-93b9cfe656a3 | -2.90821 | -50.39177 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 718f3f01-3183-304a-a26e-af4b62a81878 | -2.90495 | -50.41239 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3129c43b-86ab-3489-b819-c859dbf2bbe0 | -2.87331 | -50.43873 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6296cc27-38ad-335c-bad1-0a847d750104 | -2.9363 | -50.3856 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef2615bc-0576-3bae-83e3-8ffcbd12f40c | -4.08 | -48.95141 | 2026-09-14 04:51:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcc06d7b-d53b-3b44-8663-3b5d72df5326 | -5.28259 | -45.2669 | 2026-09-14 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1b0c48bf-d20b-3b1b-95ba-426a932169b6 | -2.90557 | -50.45124 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c598011-6dc5-3681-b40d-0256a3a91400 | -2.88791 | -50.43439 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 485b8e43-3919-3d7c-b1c6-1da4fe5a9930 | -4.0834 | -48.95192 | 2026-09-14 04:51:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6433b4f6-0304-383f-b9b7-73532f756a97 | -2.89235 | -50.44917 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42285387-0614-38eb-9338-b198fb2bd7f1 | -2.88787 | -50.41324 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5666ac5b-18e8-3a02-ab71-e3e2028b5c7c | -3.21566 | -48.97159 | 2026-09-14 04:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ff46b83-635c-328e-bc72-2b4bbcbec46f | -2.89503 | -50.41084 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 51210dee-f6a9-3dd3-ae4b-237c2c978c67 | -1.46058 | -52.96602 | 2026-09-14 04:51:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da89cb2b-5325-3acd-bb7a-23872d69818d | -2.89838 | -50.4325 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0a0ec397-ce8a-3a0e-8883-b905c668e65d | -2.88126 | -50.4122 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae4ea29d-9998-31e5-8e94-b1413f7944d3 | -2.67628 | -57.55965 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3fe678d8-801d-3a65-a0e9-bee0bb81e919 | -3.53238 | -55.53891 | 2026-09-14 04:51:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 583d279a-00fb-32ab-b836-64381ca9e282 | -2.94191 | -50.4358 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd8cdf22-d393-3f91-9663-ffb342aac4f0 | -2.90273 | -50.405 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f3b8f29c-5958-3090-8775-50431baca394 | -2.09951 | -50.60612 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d966df17-8f0b-38f8-86e8-99ed91ba36ef | -2.9468 | -50.40486 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a60979af-e1ed-3694-b3bf-f0d7b232d6fe | -2.90386 | -50.41927 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 4cd54287-411f-3e80-8e1a-57ff6a6e00d5 | -2.9242 | -50.3978 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5173201-b17e-33af-98ff-57ff3dbc2b36 | -2.93747 | -50.42101 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39765f18-41bd-3c48-a005-88c951e519bf | -2.6504 | -48.57264 | 2026-09-14 04:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c66c85cc-c0ea-3ec8-957e-b7d9cfd34290 | -2.82566 | -49.2371 | 2026-09-14 04:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad416df5-9442-3557-9594-2dd76d9d64fd | -2.67013 | -57.53859 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87f1f235-80cc-34c9-ae2c-2da228919958 | -2.90771 | -50.41635 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 2cab4424-5a97-3e24-80ac-160be8b29c45 | -2.89616 | -50.42511 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 4ff8e739-65be-346a-8987-777144ad01b9 | -3.75649 | -51.147 | 2026-09-14 04:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 56c86a49-bae0-306e-90f6-cc27d2652b59 | -2.9661 | -50.4114 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c0e62ee-d257-378b-96c5-7adb02afba06 | -2.95727 | -50.40298 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac808989-783b-3df4-9ef7-bd1974b6064b | -3.38742 | -50.38965 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 47bf2ced-4ac7-386a-a1dc-e7d0c9f8afde | -2.92144 | -50.39384 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9c9fe04d-5af4-3c60-a3c2-97067bccbf56 | -2.70271 | -57.54407 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e1aa7405-9048-3f87-be56-ae080a0ea4bb | -3.38688 | -50.39309 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a2eccf63-843f-377b-9326-dcccbb956ee4 | -1.71036 | -54.95543 | 2026-09-14 04:51:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05988af5-067b-39ad-8e4d-39ff370c90b7 | -2.90989 | -50.4026 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c783010c-b55a-37af-b167-b7d17835dd5d | -2.94844 | -50.39455 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87bfc228-f954-3849-a2f7-c0c02c04e070 | -3.40359 | -53.20075 | 2026-09-14 04:51:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6dca14c-799b-3dc4-b5e3-ddea4f5e5b32 | -3.22324 | -50.58965 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c80f0045-84ed-3e25-9512-4a4066d8b810 | -3.19578 | -51.0197 | 2026-09-14 04:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30bdae31-fdf3-3710-b9d9-ebaf60efcc62 | -2.96459 | -49.56067 | 2026-09-14 04:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18e39eb8-eb63-3764-8b18-5781ebc62290 | -3.60735 | -53.85065 | 2026-09-14 04:51:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3626d7a-2e1f-3d6f-9bce-cb470a0f72a5 | -2.89344 | -50.4423 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 694954bd-fafb-31eb-b4fc-39bf17c1e5bd | -3.39373 | -50.75735 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50dee3b5-08df-318a-931c-4f3e7fdb6c48 | -3.53295 | -55.53545 | 2026-09-14 04:51:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f651624-7864-32cf-b497-6b731bc0e412 | -2.90001 | -50.42219 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| a18761b7-7231-3461-aa89-29fe015df939 | -2.836 | -57.63995 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31bc8614-9592-3c92-a6c2-9fc51b31632b | -2.91152 | -50.39229 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a55553d7-7ca5-3fbb-93a8-ab9815797655 | -3.75594 | -51.15046 | 2026-09-14 04:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 626d1216-eb54-3355-9252-aa7a89c209ca | -2.92098 | -50.43956 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ac731795-46d8-3640-9282-b24a6e8f1d55 | -2.94295 | -50.40778 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dab95a4-4526-320c-a71f-16e96fe4902d | -2.96003 | -50.40693 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fad1a97-1247-3eb2-8211-223b874fb2c5 | -2.61189 | -54.75468 | 2026-09-14 04:51:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 29b88606-0918-3223-ab0b-4e18aa6c326e | -2.90382 | -50.39813 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9851039a-2519-3f1f-868c-fca96f41438e | -2.88243 | -50.44761 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ede3551c-03fa-3eed-b2d5-64f0878ea109 | -2.91482 | -50.39281 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3c4d8d99-fa69-32b1-b4ed-81b1e338aef8 | -3.84657 | -49.05363 | 2026-09-14 04:51:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f6a7935-f75a-3033-8163-7e132950129e | -2.93412 | -50.39935 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9c0d6b7-f513-337d-9670-c68775ba3ab7 | -2.95564 | -50.41329 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9bec9ef1-e432-334c-93bc-944146cc6916 | -2.8769 | -50.43971 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5448a7a4-a627-38cd-892e-d42f60b392e0 | -3.38933 | -50.76371 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fd3ea20-2dcc-3815-9964-fd30aa11a918 | -2.89779 | -50.4148 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| be064a8c-97ec-3e67-82c8-d99f7a2506b8 | -2.89729 | -50.43938 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ebed0e2a-c5f3-3996-81a8-1a8227fec411 | -2.94404 | -50.40091 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eadbec1c-d726-375a-ac61-95b4f5f5ed31 | -3.16172 | -58.64732 | 2026-09-14 04:51:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 41aa4209-6055-3c7d-b7e8-9a079c6ffff8 | -3.77426 | -51.35593 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b618b879-fd84-32fe-8ef3-543d195c0623 | -2.93856 | -50.41413 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d1ce62a-5ab8-346e-82d9-a8b9688ef4a5 | -2.89557 | -50.40741 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee04934d-7ee2-3f4a-b4d9-dacee0b0f735 | -3.38026 | -50.39206 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1f7eac48-4a87-398f-8dbc-92577f68f64f | -3.17079 | -58.65376 | 2026-09-14 04:51:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 78a92084-2ac8-30f6-b81a-3accf3b5aedf | -2.92922 | -50.43029 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 330b7b58-ef1e-371c-a0ef-73cdf2a59bd9 | -2.9358 | -50.41018 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2569b9a7-b7d4-325f-83c9-553b174dfe10 | -2.93081 | -50.39883 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad1aa6ad-9695-33b8-99e5-43bb5d37c3d3 | -2.87908 | -50.42596 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f53b11c3-b196-3811-a163-e56ea843b4fa | -3.846 | -49.05726 | 2026-09-14 04:51:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 509d419d-cf52-38a8-b1a2-9b0c8d8ff4f8 | -2.88352 | -50.44074 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35fec8da-2069-3b40-b5cc-c89620bd759a | -3.39043 | -50.75682 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47f90681-1cb2-395c-a62d-017e312a475a | -2.89122 | -50.4349 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ff487378-5d35-3b2e-8f19-41b6a4b7bd0d | -2.95451 | -50.39902 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63a6ec4f-105f-3326-abb2-6472b84ef3c6 | -2.67469 | -57.56942 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 76a1861e-40d0-33b1-b4eb-e2cc2c53c040 | -2.88021 | -50.44023 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fad3339d-507c-3921-93e1-786f1a6f8160 | -2.91219 | -50.45227 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c512596-412a-3240-a5d6-cf14a6876fdc | -3.07511 | -51.20312 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 040b7e64-6893-37b2-92e6-9c889add5921 | -2.96443 | -50.40058 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abe57bfe-4c41-3ac7-80b0-4014e0dd1402 | -2.90662 | -50.42323 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| a5ff94e0-944c-3683-b48f-44cf7748ea85 | -2.89448 | -50.41428 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| dce1c1d2-5e2b-35c1-b6b8-11dd224d7a7a | -2.90114 | -50.43645 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 11f0a7b6-d9a0-30fe-8136-087b30911ed5 | -2.93529 | -50.43476 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71ecb438-842c-3f75-91b9-55db7c188ddc | -2.91323 | -50.42426 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a0a92a42-f8db-31d2-9e95-e3921edbb94c | -2.89176 | -50.43147 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| bb62b150-ae2c-3e6a-a6c6-d168feebd6a4 | -3.22048 | -50.5857 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4abeba7-a38a-378c-84f3-c63e6ddfde89 | -2.94848 | -50.41569 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3734141c-8db2-3556-855e-1c11ad9aa600 | -2.69419 | -57.53764 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2b8a0998-5d11-3f75-b678-77d26fad71e7 | -4.28807 | -51.05108 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README36.md)
