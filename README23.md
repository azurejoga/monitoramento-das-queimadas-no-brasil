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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 730a3986-c9dc-3d62-a26c-331061112f6b | -9.8697 | -63.30082 | 2025-07-11 05:48:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46a4ad66-ba54-3108-8f68-c5e9d3bda186 | -9.86897 | -63.30575 | 2025-07-11 05:48:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b00317af-db4d-35ec-994f-fe3d256182c6 | -9.64398 | -65.73878 | 2025-07-11 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12033478-c409-3652-bce0-196b50e16418 | -6.62814 | -56.27507 | 2025-07-11 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 603c8590-68fa-38d0-9744-4c86153f0571 | -9.92416 | -59.90349 | 2025-07-11 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c191fe0-984f-35c6-ab40-e87016d2e2b8 | -7.89972 | -61.52277 | 2025-07-11 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28220851-ba8b-38d2-96e5-7ceb6036b93e | -9.92677 | -59.90187 | 2025-07-11 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63ded432-0468-3849-a240-eb6f63de8a8c | -7.7828 | -61.37139 | 2025-07-11 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 302919b6-576d-37c5-8bfa-070a6307107a | -10.6672 | -49.4895 | 2025-07-11 05:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| fc1d703a-2a87-3e31-a523-151443729780 | -9.96934 | -64.95811 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74d9d0a8-461c-3e62-ae4e-ec32271fb913 | -14.42962 | -58.7246 | 2025-07-11 05:50:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61d8b129-3137-35ce-a55f-796a30163d6a | -9.96285 | -64.95841 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 575d465c-bda7-3a69-9841-8501e18d8a02 | -9.94507 | -64.95572 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8226873-d6a2-34c1-a98b-2ca77b719967 | -9.96104 | -64.96518 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6084d0e9-e871-3dcb-9e74-ddeca606d298 | -10.8275 | -68.23322 | 2025-07-11 05:50:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a86a062f-35f9-3731-9a1f-c78bddb05362 | -14.4357 | -58.72153 | 2025-07-11 05:50:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77cfa365-4075-325e-b21b-172085852a62 | -9.94802 | -64.96033 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c7407e9-b510-3f8b-b8bf-581df64fee16 | -9.94569 | -64.95164 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0df24ebe-d37b-3cc0-90fa-e775732caa16 | -12.09569 | -64.24622 | 2025-07-11 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 268de911-a52f-3c5b-9bc7-9e972cb1cc29 | -9.96044 | -64.96925 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 294d7e61-e2ea-3805-9629-0ae61f61f12b | -9.96224 | -64.96248 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e780c8ae-46a4-3f4e-b4c8-23bbef041819 | -9.96638 | -64.95351 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| decc98a1-2b92-3917-8cac-3edb0ed02467 | -10.31769 | -67.34824 | 2025-07-11 05:50:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69a48c55-1500-3477-a6da-c5a6834357b7 | -9.96282 | -64.95296 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9793858d-6bb6-3aa6-8856-b8692e3c42d3 | -11.78298 | -64.98369 | 2025-07-11 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa885f0a-fe1b-3574-88b3-09f9ba7c9994 | -9.94385 | -64.96385 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0adf5288-f92e-38fc-8cc6-a291f5b88412 | -9.96163 | -64.96111 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 834f63d6-a0ea-3c60-9e07-92961ae65c66 | -9.96702 | -64.95489 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 543c5156-24e5-3724-86c8-f7d0f6bc0a8e | -10.80802 | -62.00201 | 2025-07-11 05:50:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6474e575-78dd-3d64-8a00-667bd1390e8f | -9.96347 | -64.95435 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 270eafd1-40dc-311c-8754-75d9ff5cdc8d | -9.96641 | -64.95895 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a739b692-98b5-3df9-a652-3cefbb183cb0 | -9.96578 | -64.95758 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8bc0e0eb-a4ed-3c7d-b91d-5e48a79e0d9c | -11.86091 | -62.73619 | 2025-07-11 05:50:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77def7ab-acba-3553-8df3-ab986f510eaf | -9.94863 | -64.95626 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9172ac65-5454-31e7-8512-6e407e61c7b1 | -9.95807 | -64.966 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbf8859b-a8fe-3d09-9789-242371720052 | -9.94029 | -64.96332 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a49d1775-581c-30b9-a243-3bf5f10fc2f2 | -10.11831 | -65.14934 | 2025-07-11 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f3f9661-86b8-3778-8c67-3015ae8322d8 | -9.96101 | -64.9706 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13b1eb1b-47da-3963-8fde-a530bc8892b7 | -9.94091 | -64.95924 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 165f314e-711e-3890-aa3a-fac30e52280a | -9.96039 | -64.97466 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 787c487f-51b7-3552-9732-8d1af31cf94e | -9.96222 | -64.95704 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abfeaaba-6dfe-35c4-9086-1e48c55c0399 | -9.95868 | -64.96194 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acf93dc7-fd7e-36ee-a13d-b6af4f6c68fc | -9.96519 | -64.96165 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e45dd2e8-2d80-3814-b44c-46ea3517549e | -12.09502 | -64.25092 | 2025-07-11 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8335da4-50cd-3e8b-8d6c-a4d55edc8a0e | -12.09191 | -64.24567 | 2025-07-11 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1cafa51-ef2c-31e9-854b-09a16f7f885c | -9.96408 | -64.95029 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 406f3da8-464a-3c79-994b-0e39c1863803 | -9.95985 | -64.97331 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6130279-219e-356d-ab13-d62e0a19dc4d | -9.96162 | -64.96654 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f36191e-5976-3ea7-9b9e-8e45f9e7cd60 | -9.94446 | -64.95979 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4b0a534-5011-31d1-a771-c42e094d426b | -9.96764 | -64.95082 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad2b2a45-27c1-3bb0-b32f-4ce2df170109 | -9.96341 | -64.9489 | 2025-07-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d25715c-427b-3682-985c-75b2c96f22eb | -18.64731 | -55.72503 | 2025-07-11 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 94b61550-a273-3d75-acbb-85631906609b | -18.65124 | -55.73343 | 2025-07-11 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1878d2e8-09ac-363f-87fa-197444da01a3 | -18.65239 | -55.71921 | 2025-07-11 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3955676f-7623-3306-be15-5b945779f555 | -18.65889 | -55.72699 | 2025-07-11 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2a973f31-9d6c-3ad6-92f0-ad43f6319e51 | -18.65181 | -55.72632 | 2025-07-11 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5a70ea88-d105-34d9-9d0a-948e316e54ce | -18.66147 | -55.72628 | 2025-07-11 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b91096ad-1565-3b66-a602-faa92ddfd0dd | -18.65439 | -55.72563 | 2025-07-11 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bc9128a1-6e61-31f2-80db-103fedbbcfea | -18.66597 | -55.72765 | 2025-07-11 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 946b4497-6c79-3888-bd60-044a7d9462a8 | -10.6672 | -49.4895 | 2025-07-11 06:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 08f2570b-7266-3bb8-87ed-abb63cb7d9c4 | -4.54103 | -48.00077 | 2025-07-11 06:20:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 496d103e-49a3-3168-9a0c-60ef7f1e46d6 | -10.57528 | -49.14246 | 2025-07-11 06:22:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 6918e1ec-03aa-3f8c-a30e-10d8f07b804a | -10.57887 | -49.11563 | 2025-07-11 06:22:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| a965613b-d665-3ee6-87cb-a0560363062c | -10.67376 | -49.49311 | 2025-07-11 06:22:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 74672700-861d-3b10-a0b5-be1eae75e029 | -10.57776 | -49.12258 | 2025-07-11 06:22:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 479a657d-7ace-3f6d-8e59-e1be17e258c6 | -13.14772 | -47.29629 | 2025-07-11 06:22:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 4692c668-e45b-3c80-9ddb-2da352658639 | -9.91119 | -47.82729 | 2025-07-11 06:22:00 | AQUA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 1573c33f-8377-303b-8377-d88fca224dda | -10.8405 | -49.11268 | 2025-07-11 06:22:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ce208681-0c69-3c87-b5a9-4a90cb0ea204 | -10.67621 | -49.47431 | 2025-07-11 06:22:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| e0bde838-ec8f-3887-bf2c-ff469a847a1a | -10.57625 | -49.13537 | 2025-07-11 06:22:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| fdf56957-ed11-374a-9ccc-915d1aee97b7 | -10.85337 | -49.1144 | 2025-07-11 06:22:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 43a525bf-8fa2-3963-bd51-cc15805ad6a1 | -18.66442 | -55.72404 | 2025-07-11 06:25:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 7ee19ef2-3702-3319-bc22-151a758edd90 | -10.6862 | -49.4874 | 2025-07-11 06:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| b45896cb-fe8b-3bc7-92fc-6c1fb4e7839a | -22.3933 | -53.8719 | 2025-07-11 07:10:00 | GOES-19 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 97.8 |
| 41180ad9-f2c2-31d8-8d43-2514fdcf9fd7 | -12.8813 | -49.1758 | 2025-07-11 07:40:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| e45283dc-320f-3723-9937-20507ff6ccba | -12.8813 | -49.1758 | 2025-07-11 07:50:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 30cf59a7-c30c-33e9-9ded-5d95fec17614 | -12.8809 | -49.1977 | 2025-07-11 07:50:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| fe087544-b0e3-3b0c-a01c-7bb50076453d | -12.8809 | -49.1977 | 2025-07-11 08:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 5da1e8f0-347f-3073-8274-eb08861f15c3 | -12.8813 | -49.1758 | 2025-07-11 08:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 9679c40e-4f45-31f3-840e-07c6bba24e1e | -12.8813 | -49.1758 | 2025-07-11 08:10:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| ea440024-528c-302c-a54d-257433a33d61 | -6.1421 | -45.9125 | 2025-07-11 08:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| f7de7520-3be3-3825-a3d8-7ef87ff56e7a | -12.8809 | -49.1977 | 2025-07-11 08:10:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 0df59e08-9696-37d2-9799-9d71fe10f5c2 | -6.1421 | -45.9125 | 2025-07-11 08:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| b056c215-821a-3196-bde6-dd376f773f72 | -12.8813 | -49.1758 | 2025-07-11 08:20:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 24ebdf26-8b30-33ca-9255-88949fa6c42f | -12.8809 | -49.1977 | 2025-07-11 08:20:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 612d2ac3-b5d1-3676-bc26-ebaea029e46e | -6.1421 | -45.9125 | 2025-07-11 08:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 98e16004-b435-3ed1-8b06-4dde544c5989 | -12.8809 | -49.1977 | 2025-07-11 08:30:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 56.7 |
| c0c4f8a8-af5e-3629-b79d-1b5277e1cf08 | -12.8813 | -49.1758 | 2025-07-11 08:30:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 865d474d-3914-3f0a-9677-199f2ca88e49 | -12.8809 | -49.1977 | 2025-07-11 08:40:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 105424f8-ca42-34fc-ba56-e7f2e0a062a0 | -22.0953 | -52.5818 | 2025-07-11 08:40:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 60.4 |
| 860c9da4-c8a8-3d3f-91b0-1203399b32a3 | -12.8813 | -49.1758 | 2025-07-11 08:40:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 3ee5615e-a654-3732-8520-d83068050e95 | -22.1161 | -52.5776 | 2025-07-11 08:40:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 52.4 |
| ef24d142-3c72-3555-b256-b525e14317ba | -22.0953 | -52.5818 | 2025-07-11 08:50:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 114.6 |
| f576ccc9-4525-32f2-b3b7-7f055080e7e5 | -22.1161 | -52.5776 | 2025-07-11 08:50:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 97.6 |
| fd4e43ed-6f12-3d00-8296-e46ca8d3652f | -12.8813 | -49.1758 | 2025-07-11 08:50:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 76.0 |
| c8f27d5b-62f2-3cd4-b4c7-75ceb85d770d | -12.8813 | -49.1758 | 2025-07-11 09:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 883cefb0-dd96-3134-84a3-9a28a0887ebf | -9.9148 | -47.8282 | 2025-07-11 11:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 222a5f57-247a-33dc-a08c-37efb6ab421d | -6.98332 | -44.45589 | 2025-07-11 12:08:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a0af906e-a868-3236-b4b2-a88a49f167e9 | -7.49344 | -43.937 | 2025-07-11 12:08:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| afae0ea2-4321-3d90-ba64-49432cc4b9ef | -7.637 | -46.01525 | 2025-07-11 12:08:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |


[Clique aqui para ver as próximas entradas](README24.md)
