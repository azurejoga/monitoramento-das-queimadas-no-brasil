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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 782f00e5-5692-3fcb-a307-32a073b73a8d | -8.4675 | -54.6631 | 2026-09-03 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 53fbd119-9886-324a-a6c8-e8fe3f94465e | -18.7967 | -48.8958 | 2026-09-03 03:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 50.9 |
| ad15a8a3-ef96-3426-9bcb-04c983a099cb | -10.9815 | -45.0874 | 2026-09-03 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 48570f3f-9b0b-3c9b-8f22-847f1e201a04 | -11.316 | -50.5132 | 2026-09-03 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| eeb39ebd-aa94-3319-bd16-c4132ee00033 | -11.0006 | -45.0847 | 2026-09-03 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| fd6892c4-d7d3-343d-97b3-89c53e2a08d2 | -11.3156 | -50.5346 | 2026-09-03 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 434009da-a731-3d3e-8e4b-d729801aa111 | -6.3051 | -56.064 | 2026-09-03 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 726c4888-ccf0-3920-adab-c4353558e83c | -11.3156 | -50.5346 | 2026-09-03 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 89073b5c-dc26-36bd-a494-611a7201f2c3 | -5.5647 | -60.2312 | 2026-09-03 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 4e9a482b-c02e-30bd-b97c-17dd567621dc | -8.4675 | -54.6631 | 2026-09-03 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 19dde0e9-8640-34dc-b0c3-51fd5a5f509d | -6.7463 | -59.4416 | 2026-09-03 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 0f5db350-785f-374d-b8d4-27070a0dd7b3 | -18.7766 | -48.8999 | 2026-09-03 03:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 81b4b791-f876-3a73-a7af-b87fbc2d60c5 | -9.0787 | -65.7151 | 2026-09-03 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 9fde82aa-093d-3e2e-aa52-e26df12a8add | -3.2485 | -47.2657 | 2026-09-03 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 3acc244c-ac2e-3d7f-a1ba-4a85e406a526 | -6.3236 | -56.0632 | 2026-09-03 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 96e2a519-3edc-31b4-b634-8a92b2dca779 | -11.316 | -50.5132 | 2026-09-03 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 43.9 |
| b71c646e-262a-304b-9b57-6ea136a895c4 | -18.776 | -48.9226 | 2026-09-03 03:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 91.4 |
| ee1f03a7-6715-3f67-b3d4-2aa48de8f383 | -8.4677 | -54.6429 | 2026-09-03 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 3f6736b5-c1c3-3e9e-9771-5c5c1a5a7483 | -11.297 | -50.5153 | 2026-09-03 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| e392bd66-4ac1-3c5c-91d3-2f82a6600e62 | -6.6542 | -59.426 | 2026-09-03 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 864c844c-f460-39d1-b19c-49c5e4fd3998 | -6.6698 | -59.9443 | 2026-09-03 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 9b12f472-bec0-3d44-b730-5027380b3a80 | -6.6883 | -59.9436 | 2026-09-03 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 839eb467-89d8-34c7-927d-695e85c967c3 | -6.3237 | -56.0434 | 2026-09-03 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f2ed38f4-efe7-369a-a6d7-9458e3b3c238 | -6.6357 | -59.4459 | 2026-09-03 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 7fca0b5d-145a-306b-bde5-1d1ce7d66bed | -18.7962 | -48.9186 | 2026-09-03 03:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 57.7 |
| d1714739-9a6e-3f86-a582-7aa8aa59bb6b | -6.6541 | -59.4452 | 2026-09-03 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 9dccd5a1-b584-3506-954f-6bf321fa1890 | -6.6882 | -59.9628 | 2026-09-03 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 3da80af0-475c-31d0-86e9-dcb523d6d7db | -6.6356 | -59.4652 | 2026-09-03 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 1020a2f9-f23a-3a97-8e0b-783e7ab23bf5 | -3.2486 | -47.2438 | 2026-09-03 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 08ab6f35-9435-3bc2-9e71-45a4559d2abe | -6.7648 | -59.4408 | 2026-09-03 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 2543ed01-ad35-3a8e-b88b-97784f25c9c5 | -11.2966 | -50.5367 | 2026-09-03 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 2ce308c2-3510-3f0e-b229-8a2474636b16 | -9.0601 | -65.7157 | 2026-09-03 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 47744c82-442b-396f-b1e8-9f41962f9d6e | -6.6358 | -59.4267 | 2026-09-03 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| c72e3b86-4986-35ed-ab7d-7f6dc908d3e3 | -6.3052 | -56.0442 | 2026-09-03 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 021f98e8-0728-3a1e-83ef-d2a973bde80a | -5.5464 | -60.2318 | 2026-09-03 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 0af86ba2-dec7-38b5-bdd0-10539a2d839a | -6.3237 | -56.0434 | 2026-09-03 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| cf9ce40d-2efc-38d7-a577-b5c9e26ce664 | -11.2966 | -50.5367 | 2026-09-03 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 6151e867-991a-381f-bbd0-7c27b71586f9 | -11.3156 | -50.5346 | 2026-09-03 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| cd9a08f7-9834-3fee-8e49-8b73c8947b55 | -8.4677 | -54.6429 | 2026-09-03 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 0c8ee358-9c41-36e8-b191-9c8d6af69ccb | -9.0601 | -65.7157 | 2026-09-03 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| a1608033-0c7a-3484-aedb-0a7b4eba9f0d | -6.6542 | -59.426 | 2026-09-03 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| d91b805c-ac9e-37ef-b3fd-485c57bdac47 | -6.7648 | -59.4408 | 2026-09-03 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 8d9029f8-1b43-3bbc-a5ee-c62d943cd81c | -18.776 | -48.9226 | 2026-09-03 03:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 78.1 |
| e3b4826f-193e-33db-b476-2b562374d6c8 | -9.0786 | -65.7338 | 2026-09-03 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| eec57e45-c390-36b5-beb6-e36cd78cc01d | -6.6883 | -59.9436 | 2026-09-03 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 6034252d-44a3-36a6-86c4-16817e259b73 | -6.6764 | -58.7686 | 2026-09-03 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 434aab6a-b871-301b-ab7c-32ca17f9382f | -9.0787 | -65.7151 | 2026-09-03 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 82be493e-aaba-3cff-850c-71bb831e3d48 | -6.7463 | -59.4416 | 2026-09-03 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| f29c57c7-4f00-3249-ab4e-956db453390e | -6.6356 | -59.4652 | 2026-09-03 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.4 |
| a42225e2-3d5d-37e8-bc97-140eabd89921 | -6.6882 | -59.9628 | 2026-09-03 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 03d04fa9-0dfc-361f-bf7a-ce625c2335ca | -6.6357 | -59.4459 | 2026-09-03 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| da264aaf-161a-31f9-9177-b068d66c35f1 | -3.2485 | -47.2657 | 2026-09-03 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| bb2dbf4b-7769-33d1-959d-abb465cc3d82 | -3.2486 | -47.2438 | 2026-09-03 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| ad5a85f9-3205-318f-968b-bf3dda2c05b0 | -6.6698 | -59.9443 | 2026-09-03 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| acc61eb4-2bdc-3064-a317-533650e91137 | -6.6541 | -59.4452 | 2026-09-03 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 9c03da5c-4e5f-3004-8c80-e5e22d201350 | -6.6358 | -59.4267 | 2026-09-03 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 1129f4cd-12fd-3a29-87af-25a6bbeb7de2 | -6.6697 | -59.9635 | 2026-09-03 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 20f4e4a9-08b2-3937-aaa1-3aa430460147 | -11.297 | -50.5153 | 2026-09-03 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 5f81c1ed-229b-3bf6-848f-119c87f8461c | -6.3052 | -56.0442 | 2026-09-03 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 5dc7f567-9d0d-3a79-8517-3f60bbaf9618 | -11.316 | -50.5132 | 2026-09-03 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| ccb61442-bad1-31c3-b614-f187a811f89f | -6.3236 | -56.0632 | 2026-09-03 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| e511ebe2-41d8-3d8c-b3c4-b07a8cda74dc | -8.5916 | -67.1788 | 2026-09-03 03:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 09a4fa7b-cf56-36b2-bf6f-5dc2518cbd91 | -9.0787 | -65.7151 | 2026-09-03 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 02a1f0cf-09f6-36b2-b7c7-23d2e82ed806 | -6.6697 | -59.9635 | 2026-09-03 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 746f26b5-b090-3d1e-adcb-106b425a7e01 | -3.2485 | -47.2657 | 2026-09-03 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 40ae80e1-769f-30e4-b050-d2202325a7fa | -6.6542 | -59.426 | 2026-09-03 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 490f6975-fb0b-3c7d-81a1-f86f3bcdb99d | -6.6883 | -59.9436 | 2026-09-03 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 9ec4a066-2b05-3042-897c-b4f5189653a2 | -6.6698 | -59.9443 | 2026-09-03 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| dd1a53bf-cb82-31c2-8a8f-161310f302c3 | -6.654 | -59.4645 | 2026-09-03 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 31e517dd-71fe-31f2-a87f-730cbe4a67de | -9.0601 | -65.7157 | 2026-09-03 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| e3f30a89-8720-3123-9e49-e265c5b7b945 | -6.3051 | -56.064 | 2026-09-03 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 58abba50-b2b9-31ee-b3db-0b005e4b4690 | -6.3237 | -56.0434 | 2026-09-03 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| b0ed503e-885e-33b9-a9f8-b70ec778d7e4 | -6.7648 | -59.4408 | 2026-09-03 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |
| f93b7cf2-6e60-34cc-b024-5263192b74a3 | -6.7463 | -59.4416 | 2026-09-03 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 49b9a861-9527-332a-9a9a-db11237a5890 | -6.6882 | -59.9628 | 2026-09-03 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 94a790ce-4997-3838-a73f-44a524aafd1c | -6.6357 | -59.4459 | 2026-09-03 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| e312cce4-1494-3339-aa0c-5d3176aca955 | -6.3052 | -56.0442 | 2026-09-03 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d6347322-24a8-3133-90cd-30b043ff47f1 | -3.2486 | -47.2438 | 2026-09-03 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 8f4c44fa-d904-3ade-b2b8-f231687ef303 | -18.776 | -48.9226 | 2026-09-03 03:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 2777bf11-1938-3e95-ab7b-f09beffcdeeb | -6.6541 | -59.4452 | 2026-09-03 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 0ea86b4d-1c60-3b27-b0ef-6e3869c827a1 | -6.3236 | -56.0632 | 2026-09-03 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 1fe868cd-cc60-3245-8abf-becce8f13367 | -6.6883 | -59.9436 | 2026-09-03 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 747369ca-dd47-3139-974f-4d3cc070f3f9 | -6.7463 | -59.4416 | 2026-09-03 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| d299cdf0-b37c-3519-bee4-f46b645cf5f6 | -6.7648 | -59.4408 | 2026-09-03 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 0c1ad331-3ae7-3e9e-b749-652b8b49080d | -6.6541 | -59.4452 | 2026-09-03 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 00b93800-6fcd-3ec3-8eed-8c6ea0d6c2e9 | -3.2486 | -47.2438 | 2026-09-03 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 02b41a4b-60c5-3c75-ba48-33ca75b42808 | -6.3052 | -56.0442 | 2026-09-03 04:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 25239804-b12a-3b89-a995-62f1a12268be | -6.6697 | -59.9635 | 2026-09-03 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| c82e3e56-5fb8-39cd-ab80-825b5b85339f | -9.0787 | -65.7151 | 2026-09-03 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 9f410faf-11a7-33f1-943f-c147aa9c2dcd | -3.2485 | -47.2657 | 2026-09-03 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| b02b87ff-d8b7-309c-9561-b9f29a73b2de | -6.6698 | -59.9443 | 2026-09-03 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 6fab5607-c1f5-351a-b070-396bdb36bbb0 | -6.6357 | -59.4459 | 2026-09-03 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| be4b054f-935d-37cf-a3ef-4931cd116d6a | -6.3236 | -56.0632 | 2026-09-03 04:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| d93d6426-7a59-38f2-a2ae-cde9e462dc63 | -6.3237 | -56.0434 | 2026-09-03 04:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| ea280a38-4e01-3602-834b-047b46a39b18 | -6.6882 | -59.9628 | 2026-09-03 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 8a3f5063-74c5-35b6-a5bc-176c16c19daa | -8.5916 | -67.1788 | 2026-09-03 04:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 675cfb1f-9492-379d-84fc-e9a5d8fa4ea2 | -1.09417 | -48.05618 | 2026-09-03 04:00:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7317b727-ac5d-3e82-b3a0-96de6beb85aa | -3.33734 | -42.79787 | 2026-09-03 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85d2054c-5e22-3acd-beec-afe748c55877 | -3.33961 | -42.80698 | 2026-09-03 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0956f561-adb0-32d8-8ece-b0de631b0298 | -3.341 | -42.79844 | 2026-09-03 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README17.md)
