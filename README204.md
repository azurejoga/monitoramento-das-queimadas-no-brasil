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

## Dados Diários - Página 204

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 810fff49-f082-377c-8653-7e74b186103e | -9.26115 | -67.81548 | 2024-10-03 07:07:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6efbd220-0e9e-3741-b60e-77728a7f6935 | -9.09379 | -67.5136 | 2024-10-03 07:07:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 5a649210-1fb9-3280-9fe9-aecc853cc0cf | -9.04742 | -67.86072 | 2024-10-03 07:07:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 1e32c2d6-967e-3e5d-984f-b32a7e6bb809 | -9.02162 | -67.73093 | 2024-10-03 07:07:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 56b0c047-70b1-342b-b6c5-8ab6894768cd | -9.01925 | -67.74805 | 2024-10-03 07:07:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 90f75556-2d96-3c61-a442-162cfcbfbc4f | -9.01527 | -67.73529 | 2024-10-03 07:07:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| a92a4b45-bc2d-3096-8cba-6ccf2e911bf3 | -8.78405 | -68.79208 | 2024-10-03 07:07:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f0576865-5eca-37f0-9758-a196b60e2217 | -9.74137 | -68.41558 | 2024-10-03 07:07:00 | AQUA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 9efdaf7c-1cb6-38c0-a938-352ccb27e428 | -9.73922 | -68.43127 | 2024-10-03 07:07:00 | AQUA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1fee9847-9f10-3471-bf2b-1ee175c09939 | -9.73788 | -68.42228 | 2024-10-03 07:07:00 | AQUA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a43faf31-7a45-39e0-9d22-d254c48a913a | -9.72096 | -64.22791 | 2024-10-03 07:07:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.3 |
| a22abbe1-1d8e-3f8e-bb22-1f641702610a | -9.71346 | -64.21971 | 2024-10-03 07:07:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 28.7 |
| f7de22a6-4309-3cec-bf8b-d9489a3c359a | -9.62323 | -67.47186 | 2024-10-03 07:07:00 | AQUA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 91dade92-b06c-33b9-94d4-7c42c401c383 | -9.50025 | -68.49705 | 2024-10-03 07:07:00 | AQUA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 21efed53-b6df-3653-9c95-7caf4afbb328 | -9.38654 | -68.3275 | 2024-10-03 07:07:00 | AQUA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 66d69c7e-3da9-3eb8-87fa-0c6d76144aaa | -9.38497 | -68.31836 | 2024-10-03 07:07:00 | AQUA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 44260ba8-62f3-334b-a348-bc36c43da176 | -21.3067 | -47.599 | 2024-10-03 07:07:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 83.4 |
| b4f5a541-2359-3180-9f52-33264aed8283 | -21.306 | -47.6227 | 2024-10-03 07:07:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 971ef966-0c67-326b-837f-089d29c56032 | -9.0515 | -67.871 | 2024-10-03 07:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 94f7e10e-52c4-3c74-a3fa-f0c622e6a85d | -12.4228 | -62.9807 | 2024-10-03 07:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 248.1 |
| 93320a33-8737-3022-89b7-7359dc89ae44 | -12.4227 | -62.9999 | 2024-10-03 07:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 602.1 |
| fadf70d4-3a1e-334b-807a-cbd26077d881 | -12.4225 | -63.019 | 2024-10-03 07:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 244010af-48e2-3e94-b70e-77da2de65e9e | -12.404 | -62.9817 | 2024-10-03 07:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 163.6 |
| b00c766e-0764-3d5e-9320-ca4c87ec0cca | -12.4038 | -63.0009 | 2024-10-03 07:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 364.5 |
| d8611201-29ca-34b5-9112-cdd801084e7f | -12.4037 | -63.0201 | 2024-10-03 07:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 103.3 |
| f638b265-0a3e-364d-933a-3277d1bea41e | -12.8991 | -62.5491 | 2024-10-03 07:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 5e096b5d-85d3-32d8-97c9-3cd37919ff50 | -12.8802 | -62.5503 | 2024-10-03 07:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 3d029d71-ba77-3400-a141-51130a759c2d | -16.1094 | -50.4489 | 2024-10-03 07:16:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 1b62cfa1-2a4a-3e2e-878f-0eb1865632b0 | -17.0892 | -56.7709 | 2024-10-03 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.5 |
| b29f4a76-10a8-35e9-93b9-56c55f35e377 | -17.0888 | -56.7915 | 2024-10-03 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| 8a457c87-4197-3e6e-af74-15d55b9a6840 | -17.197 | -57.3741 | 2024-10-03 07:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.5 |
| 0cf5f354-11cb-33d6-b541-04232d3d8236 | -21.306 | -47.6227 | 2024-10-03 07:17:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 04574e87-9b3b-380f-9e9b-420cafaa8a53 | -21.3067 | -47.599 | 2024-10-03 07:17:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 3003403b-2c5c-366a-9712-881d7eb564de | -8.9791 | -67.4099 | 2024-10-03 07:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 42e736f4-93b1-3a8b-906f-9a212d0385fe | -9.0515 | -67.871 | 2024-10-03 07:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 540f6fea-ff7f-3ce0-befb-bb0a44cf7e75 | -16.1094 | -50.4489 | 2024-10-03 07:26:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 22cabc0d-f28f-3de3-bd69-050eb810e9f6 | -16.1098 | -50.427 | 2024-10-03 07:26:36 | GOES-16 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 810842ac-91bf-3cd1-a905-9b1f49997198 | -16.129 | -50.4458 | 2024-10-03 07:26:36 | GOES-16 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 6bb6014a-54c9-3423-85c2-f369299a7e1b | -16.1294 | -50.4238 | 2024-10-03 07:26:36 | GOES-16 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| f5800718-d8ad-3dd9-aa80-d8601e1cc784 | -16.6688 | -57.374 | 2024-10-03 07:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| bdfa6c51-9099-327d-9999-5284c3eb093a | -16.6492 | -57.3763 | 2024-10-03 07:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 0c9112f7-e165-3b86-aa97-56d8834ab840 | -16.6489 | -57.3967 | 2024-10-03 07:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.0 |
| 80a96fdc-3f46-3a40-984c-3eeab6a4b5fb | -17.0695 | -56.7733 | 2024-10-03 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.1 |
| 02ddac7d-dbef-3221-b0ce-067054777f1d | -17.0499 | -56.7757 | 2024-10-03 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.1 |
| 76f6c584-e780-3b0a-bd59-e6f2c98fbdc9 | -17.1085 | -56.7892 | 2024-10-03 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 16249455-7ecf-3c94-b109-28cf79041e16 | -17.0502 | -56.7551 | 2024-10-03 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 72ef0c7c-f63d-3249-8095-c578c4ed8140 | -17.0306 | -56.7575 | 2024-10-03 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.7 |
| da752a32-fccb-3d3a-9b90-647ebec33df1 | -17.197 | -57.3741 | 2024-10-03 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 6cfb538a-f7a1-3d80-a710-b6343aa57dd5 | -17.1967 | -57.3946 | 2024-10-03 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 5b0daa7c-67dd-30aa-84b9-864fcf361522 | -17.1774 | -57.3764 | 2024-10-03 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.6 |
| 610be970-0c35-3dd5-9640-653e590a6371 | -17.1771 | -57.3969 | 2024-10-03 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 157.0 |
| 99c087a8-d9bc-37df-b164-aa10e6e5b55e | -19.3159 | -42.5976 | 2024-10-03 07:26:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.2 |
| 181472d1-2949-375b-ab04-fbfa63f61529 | -8.9976 | -67.4094 | 2024-10-03 07:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 2d2105fa-f276-39be-84af-ff19bb5aa1d2 | -9.0515 | -67.871 | 2024-10-03 07:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 9db90fc0-011e-35a1-8111-3f8d92faa164 | -12.4038 | -63.0009 | 2024-10-03 07:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 185.6 |
| 2289ff43-a483-3bd5-bc27-2717c5b79738 | -12.404 | -62.9817 | 2024-10-03 07:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 98.1 |
| b22bcef3-c070-3954-b10e-72e0603dfd59 | -12.4225 | -63.019 | 2024-10-03 07:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 24898534-e715-32b5-bc98-f38965971196 | -12.4227 | -62.9999 | 2024-10-03 07:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 380.0 |
| 33c3f514-f8ea-37fb-aa53-bf590a1d1eb5 | -12.4228 | -62.9807 | 2024-10-03 07:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 171.6 |
| efdb8d5f-4666-3439-88cb-9c9f5597220b | -16.5387 | -58.2427 | 2024-10-03 07:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.6 |
| 17f56581-4fa2-3803-b908-b90dfbb18020 | -16.539 | -58.2225 | 2024-10-03 07:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.0 |
| f4711b9f-7070-3534-810d-738ec6b79401 | -16.5585 | -58.2204 | 2024-10-03 07:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.4 |
| 5e11ae81-17e6-34d2-a8e3-93b8573bde93 | -16.5783 | -58.198 | 2024-10-03 07:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.2 |
| 4ed47b13-ac73-3d99-839b-55ff5acfe901 | -16.5588 | -58.2001 | 2024-10-03 07:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 57c3df65-c318-3500-bcf8-828584905ff4 | -16.6492 | -57.3763 | 2024-10-03 07:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| 9f05200a-0737-3b04-b368-c6f2d495038b | -16.6723 | -57.1488 | 2024-10-03 07:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 0e242aef-ff22-3a58-ae37-9a9ee71248be | -16.6919 | -57.1465 | 2024-10-03 07:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 31ba56f8-5cb3-36b5-a36e-ffdc2d7c5b02 | -16.5582 | -58.2407 | 2024-10-03 07:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.0 |
| f5d6a3ff-140c-35a0-ad8d-315a856668cf | -17.0695 | -56.7733 | 2024-10-03 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| 034e5dff-0f08-3d06-b00d-c82b98fb4363 | -17.0692 | -56.7939 | 2024-10-03 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.8 |
| 46f85438-bdf0-3c6a-aa4f-0aa36e82baab | -17.197 | -57.3741 | 2024-10-03 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.7 |
| 83a0fd30-e77f-37b8-8442-1fda1b73bda3 | -17.1967 | -57.3946 | 2024-10-03 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 9cbe289b-0824-3010-9414-de199e4bfe93 | -17.1774 | -57.3764 | 2024-10-03 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 205.3 |
| 02530059-b982-3939-a13c-3ecb682a0054 | -17.1577 | -57.3787 | 2024-10-03 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.7 |
| e8d16e1f-5653-30fd-aa73-e9fa593abda9 | -17.1574 | -57.3993 | 2024-10-03 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.5 |
| f53b5521-2c55-3759-b926-20181aa36d07 | -17.1771 | -57.3969 | 2024-10-03 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 257.0 |
| 31612f2f-01f2-3aa0-a56b-5c2406ac08a3 | -19.0344 | -43.1944 | 2024-10-03 07:36:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.4 |
| 49d83f0e-16f0-3b90-87c8-515d28835fdf | -9.0515 | -67.871 | 2024-10-03 07:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 4a9cd320-294e-3c7f-9212-8edbd0e1ac27 | -12.4038 | -63.0009 | 2024-10-03 07:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 171.2 |
| fe981ae2-972c-334b-a473-e3612f70610e | -12.404 | -62.9817 | 2024-10-03 07:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 103.2 |
| b6fbe4f1-231a-3fdf-bcd0-18766ff9a8b7 | -12.4225 | -63.019 | 2024-10-03 07:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 283b7230-ab4a-36e9-bfe1-b9160863b107 | -12.4227 | -62.9999 | 2024-10-03 07:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 318.7 |
| 6e42dd4a-01d8-3864-9102-023b807c990b | -12.4228 | -62.9807 | 2024-10-03 07:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 164.1 |
| cac608cd-5cbc-3c90-bcff-26f0ee755aa8 | -12.8802 | -62.5503 | 2024-10-03 07:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 801ed1c3-a0f4-3598-8cc0-f7207a0ffca9 | -12.8991 | -62.5491 | 2024-10-03 07:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 5d281175-5ed9-3cae-8e09-9985d32aebfd | -13.0402 | -51.1432 | 2024-10-03 07:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| bc595784-c936-3a65-a5a6-c5d7ffab55f3 | -13.0406 | -51.1218 | 2024-10-03 07:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| c1b1579c-6823-338e-81a5-cb99dbf7cac2 | -13.0591 | -51.1623 | 2024-10-03 07:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| adca1db4-7581-31a6-8619-4217489276c4 | -13.0594 | -51.1409 | 2024-10-03 07:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 371c0cd6-bafe-37fc-b736-94d4ee67fb40 | -16.6698 | -57.3126 | 2024-10-03 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 0ad082b8-e1c8-3ac5-9550-4fa2d4171279 | -16.5582 | -58.2407 | 2024-10-03 07:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 8db431fa-9825-3c44-b7fd-bb877a74867a | -16.5585 | -58.2204 | 2024-10-03 07:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 0137291d-7571-32cc-b1f4-7ed81848883c | -16.5588 | -58.2001 | 2024-10-03 07:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| d436c907-e293-30b6-b69f-1271297c5e70 | -16.6297 | -57.3785 | 2024-10-03 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.2 |
| de68559e-a8ae-392e-a324-ce2181a9465c | -16.6489 | -57.3967 | 2024-10-03 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.0 |
| 27b7f151-ea38-3114-81f9-3673dc1b350d | -16.6492 | -57.3763 | 2024-10-03 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 147.5 |
| b9117aca-c95e-34c7-afab-0f613033a288 | -16.6919 | -57.1465 | 2024-10-03 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| 320d480f-546a-359c-b2af-a8b1e47b1d20 | -16.6723 | -57.1488 | 2024-10-03 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 9ec5c783-6496-37a8-8ea8-37dcff0e856c | -16.6496 | -57.3558 | 2024-10-03 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| c3c2031e-31e0-34e5-be33-703c7d86c961 | -16.6893 | -57.3104 | 2024-10-03 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.1 |


[Clique aqui para ver as próximas entradas](README205.md)
