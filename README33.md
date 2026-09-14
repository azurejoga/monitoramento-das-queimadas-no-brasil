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
| 45b16b6b-6949-38d0-a0bd-2b955c13175e | -2.90059 | -50.4399 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f19b7cc8-2bc6-378f-aa62-33592e316660 | -3.61853 | -54.60331 | 2026-09-14 04:51:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6551eea3-ff87-3770-9c46-097eaab66bc9 | -2.67548 | -57.56453 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4068d9d7-eb4d-3a08-82a0-e2c372bf9f4a | -3.46549 | -47.46452 | 2026-09-14 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f95e1397-8b13-3117-99e8-3e9bfe7c8f6d | -2.91654 | -50.42478 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 60a1571e-142b-3ac8-8f42-f57ad0f48fdc | -2.91985 | -50.4253 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4e8f7b2-9ddf-3c69-b7fa-8d13f0951af3 | -2.82159 | -51.34515 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e51a35c-102b-333e-be09-75d309316169 | -2.94019 | -50.40382 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25177ca4-6228-3c9d-9c2f-0ab17738ce71 | -3.04302 | -51.25513 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8caf41d8-f5d9-326f-a53e-577199823930 | -3.7598 | -51.14752 | 2026-09-14 04:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fb0c935f-af4d-3f88-a1cd-d44747fbb81f | -3.1707 | -58.65476 | 2026-09-14 04:51:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7810599f-45b8-3164-b333-fd2333dec61d | -2.9589 | -50.39267 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecdc7b03-6486-3df8-8227-f14d966e16ae | -2.92366 | -50.40124 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 385e2e12-ef89-3ba3-827b-89f0dac15bd2 | -2.77136 | -45.49732 | 2026-09-14 04:51:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b00ba950-3858-3e26-ba27-70e555ed5f63 | -3.53811 | -53.97861 | 2026-09-14 04:51:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 00c44974-1193-3600-9ae3-5fca5da6e7c7 | -2.87962 | -50.42252 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cd0b019-30e5-33f1-822d-f0e1eecea182 | -2.97908 | -48.97644 | 2026-09-14 04:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07e853f0-1958-3e33-9d86-65b90144b329 | -3.7972 | -44.11519 | 2026-09-14 04:51:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80ab7968-dc84-37ef-9cd6-14776107e25b | -2.92152 | -50.43613 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2153721a-30ff-36b6-8c3a-acc841a21017 | -3.42761 | -54.53669 | 2026-09-14 04:51:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82540fe9-2990-3e59-861f-afcf58476b10 | -2.91763 | -50.4179 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c1d916cd-dffb-3354-9334-cea27d56565d | -2.9165 | -50.40364 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 329b53d2-1c59-3ab3-8b1a-5560803ed302 | -2.22596 | -60.04535 | 2026-09-14 04:51:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ad60c96-7f9b-3a5e-8328-a47aee887295 | -2.89842 | -50.45364 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a89d7a3b-bdce-3acc-9f5b-f7e4fcd23653 | -2.93751 | -50.44216 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff2ce1bf-e8db-3007-9ff3-7f21eabf59be | -5.11432 | -41.07935 | 2026-09-14 04:51:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3f763ceb-b98d-38c8-ac60-31f613213277 | -2.92537 | -50.43321 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b86ff86b-4364-31d8-a003-1c19f5e2f56f | -2.9049 | -50.39125 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| c0ae940f-71ec-3182-ab35-bc009c456e3a | -2.90164 | -50.41188 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 570e2cef-7585-3074-89fb-a142f706e519 | -2.90444 | -50.43697 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| a0303d1d-ebe3-3534-bfb8-6017c0c5474e | -2.90658 | -50.40208 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c2a7a30d-e43e-3f6d-b5bf-f9eeecc690f4 | -2.88737 | -50.43782 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 627f7173-6da4-3af4-b1a3-3371834209fd | -5.28741 | -45.2636 | 2026-09-14 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd177bd9-fc87-3776-b703-cf0e354e4862 | -4.12484 | -48.93489 | 2026-09-14 04:51:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cda4968-a34f-37e3-b730-56628e94354a | -3.75317 | -51.14648 | 2026-09-14 04:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a2a6597-5e2d-3214-9238-602a17aff27f | -2.92918 | -50.40915 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| abb43f42-1756-3328-9406-537a7ffbf105 | -2.94902 | -50.41225 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8d05ef6-6bb5-39e7-a5dc-be3729bb1cb6 | -2.96279 | -50.41089 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05f4866a-6d92-3aef-a48d-e2bd13f0a277 | -2.90327 | -50.40157 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7437c347-be77-349f-a854-68e4b3063013 | -2.89231 | -50.42803 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 94fc9e9f-993c-331a-a417-cf7f40d9d223 | -2.90436 | -50.39469 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| b274f530-fc28-3099-8e6e-a02648c7994e | -2.9237 | -50.42237 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3d99ed5-2d58-38e5-bc1e-eac0c1008748 | -3.3644 | -50.74913 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac11274b-903d-378d-8249-5aa9b5b3a011 | -3.22709 | -50.58673 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26b0b9a4-5e99-32b8-bd26-c5a2d8c50892 | -2.87636 | -50.44314 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2128786-bcc4-39fc-b926-68e0b6337876 | -2.90888 | -50.45176 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ee38f35-bd65-3e06-ad3a-0e436127f473 | -4.85408 | -48.36057 | 2026-09-14 04:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| be350395-a484-3bba-9873-c72a7e7534bc | -3.11246 | -53.9473 | 2026-09-14 04:51:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3be4608-9944-30f8-9290-65cb2d1bb751 | -1.86306 | -47.98145 | 2026-09-14 04:51:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 22b8c89d-22f9-3fed-b6bc-2ca5fd61e70f | -2.89896 | -50.45021 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5045a6c3-47e2-3ae0-b1aa-335efb33ddeb | -2.88846 | -50.43095 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 533b16b8-72eb-32a9-8b85-64630a70721f | -3.04524 | -51.26263 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db3b3e23-aebb-35d0-baf0-a3964f7aac57 | -2.61664 | -54.72601 | 2026-09-14 04:51:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 424daa05-12dd-306f-8d2c-d6c553bac015 | -2.92424 | -50.41894 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 33832913-4de5-362a-8a09-3dc7b878a272 | -1.2328 | -54.20699 | 2026-09-14 04:51:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8535d58b-809f-3538-8074-4c91f22352ae | -2.92751 | -50.39832 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76e88d22-c884-3475-ada9-4c28220f745a | -2.91537 | -50.38937 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 89e78ef2-518b-376f-aaef-960d689ff1c6 | -3.86139 | -51.9793 | 2026-09-14 04:51:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0384727-f760-3feb-97f0-5434ba57d399 | -2.89783 | -50.43594 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fa9773af-f1de-3613-87d6-668c1a1f62c6 | -2.93688 | -50.40331 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68c7c636-1073-360a-af5f-377aef41786f | -2.92592 | -50.42977 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2b90d682-670a-3f85-a62b-ab7a14eebfc5 | -3.16269 | -58.64054 | 2026-09-14 04:51:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2996835f-4053-36e8-880e-f23d424f4109 | -2.74052 | -57.62141 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a805a4f2-3635-311a-a325-bf6f1dec10dd | -2.70193 | -57.54895 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0d34bc58-fcc9-3742-b7e4-b7e4c8555f54 | -2.90884 | -50.43061 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 4fbaf52d-c8ef-3e7d-a50f-1981a49dbb14 | -2.88075 | -50.43679 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02ffabad-3d8f-3cf4-954b-8ee0ab432070 | -2.88841 | -50.40981 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 883b1fe4-69a4-3b2e-8bb1-d88451701496 | -2.92035 | -50.40072 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 13d0e1fa-308d-3e25-bb07-42af17f0cad1 | -2.89507 | -50.43198 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| cc8865e1-9c1d-30a2-84ec-8bea7bcfc8a3 | -2.91817 | -50.41447 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 44a23c8f-3d1b-3e6a-b00d-35e722505789 | -2.91428 | -50.39624 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c662431e-5157-33bf-96a2-dbab7d3db840 | -2.92261 | -50.42925 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6c696c3d-b7dc-31ad-b0a0-c29ae610123a | -2.96221 | -50.39318 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e69a567-85bb-3025-8d7f-18bbae4a49e4 | -2.96388 | -50.40401 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa700d48-ffe0-3d06-8dfb-6b1f1c01c8d2 | -1.71516 | -54.95098 | 2026-09-14 04:51:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 041391d1-858b-3570-a01b-a46f9cc2de5c | -2.94789 | -50.39798 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2b656ac-eddf-391a-acf8-1cf3b0c41571 | -2.92701 | -50.42289 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2c768ea9-832c-342a-8b19-c99843c240e8 | -3.92656 | -52.25117 | 2026-09-14 04:51:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9fc7771-992d-34e5-8359-13c85d2c20bc | -3.17168 | -58.649 | 2026-09-14 04:51:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a8385a6d-5895-3822-bf96-5738be075300 | -2.70115 | -57.55381 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 02449db7-92bf-3303-b11a-501794a28193 | -2.88017 | -50.41908 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e43175ad-f941-3b17-bfee-260464981391 | -2.92043 | -50.443 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11b5fa06-3918-37b0-8992-810291cd1a26 | -2.88188 | -50.45105 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| add48282-59e3-38ce-ae7d-fb1c29a65dd1 | -2.69676 | -57.53886 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d26ccd8a-d431-3058-86a1-1c12a8d60a9d | -2.92475 | -50.39436 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 914b98f4-9818-3956-9e80-76d2bf6daa08 | -2.70778 | -57.61597 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4df6a5b5-ec19-3021-8bdc-4576a240bbc7 | -2.93634 | -50.40675 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b1d6a93-197b-3ee3-8a6c-308fbbc0ed5f | -2.88297 | -50.44418 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d45fc7a-e440-3ec8-8f79-feaa3bba000c | -3.86196 | -51.97573 | 2026-09-14 04:51:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cdc1bd5e-8a15-3844-8e77-0149416b6d32 | -3.38548 | -50.76663 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd674556-0117-331d-80c5-027ae19bb7b8 | -2.69977 | -57.54936 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 38835122-8782-3a6d-87e0-6dfcc52cdada | -2.93303 | -50.40623 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fe7bd26-f58d-3fa4-a6f8-7a86ecf8d258 | -2.91215 | -50.43114 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| b2b01780-fa1a-3a6d-bb68-3b2acd4b718a | -2.89946 | -50.42563 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| f5728fa7-98e3-3018-8aec-a1230d92594b | -2.91759 | -50.39676 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d2274fc4-3cb6-3af0-a30b-ec23c58e42a7 | -2.06035 | -45.98161 | 2026-09-14 04:51:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5755350-251f-306d-bb67-aa06fb544c55 | -2.93801 | -50.41758 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3c6e00d-cf5a-39e3-be9e-6ccdf2f2f842 | -2.95287 | -50.40933 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1cc7ef17-5fa3-31f8-9c95-bdafd02aa0e5 | -2.91436 | -50.43853 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| be46eb04-4083-35cc-b615-2d14cf50473a | -2.92809 | -50.41602 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README34.md)
