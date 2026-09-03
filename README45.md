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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f38e757c-3ff3-32fc-a61a-f72aca136246 | -3.2035 | -61.20735 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d977fc3b-b933-34b4-afa9-531d1888b7c4 | -6.65145 | -59.4444 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c293c0f-1314-3f46-b06a-b123d58fb155 | -5.20669 | -60.04627 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d8739c4-a50c-3e72-84f3-98c64f9d2489 | -4.63216 | -55.73411 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64809976-a585-389e-a918-9d552c9e98f4 | -3.2039 | -61.2295 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9721ee74-b58a-320d-b965-a5af7fe12d02 | -6.77055 | -59.44264 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b84c7a0-f6c3-3915-8675-4172c692f3ea | -6.00096 | -62.50211 | 2026-09-03 05:42:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 458d1573-5f20-37b5-b0f0-6a71597d0476 | -3.44663 | -56.32062 | 2026-09-03 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f91e4b17-4c21-3fb0-9213-1a2782e87390 | -5.20264 | -60.04564 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 769c0799-5319-35c3-9375-3ebfbef70647 | -6.60101 | -59.11168 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f88dad5-179f-3723-bc24-c4fdc6732263 | -6.31314 | -56.04583 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 02b35ae0-345d-3ff0-afcd-4e3724338d57 | -5.21742 | -60.02958 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3ce00d5-a2ce-3f1f-852d-62554f74cb98 | -2.95475 | -60.90145 | 2026-09-03 05:42:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e67ded8-be87-334c-aaba-31c05eddcb8e | -5.26449 | -60.18544 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3ea76485-db88-3837-b2fe-6b7a4652bbfd | -5.24735 | -60.19006 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bee24f4-531f-3a04-b398-12cc7d82014a | -3.09768 | -61.18886 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb78ae92-85d2-33f0-a4ee-37a5c4c25706 | -6.64396 | -59.4353 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c3bb3840-f2dc-31d2-8ac9-aa2cc4735a4c | -3.20048 | -61.20246 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec5c6a65-e7ef-32f7-9408-21c5771d263f | -6.31763 | -56.0535 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 947d1a2f-43e8-3e64-9912-8793033ebd42 | -5.21336 | -60.02897 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4daa627-f286-389d-97c2-f3dfe30fad83 | -5.26047 | -60.18484 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6182cc86-824c-3350-9546-99443d5f43dc | -4.15153 | -60.70055 | 2026-09-03 05:42:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7b3dd930-d423-38cc-b02d-fa5ccf4f3287 | -6.15018 | -55.67078 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e127cc3-f107-3a5b-937a-7b38db71f947 | -6.15115 | -59.93607 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef11f648-e846-398b-9c88-e7518faddec0 | -5.55728 | -60.23564 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9933685-41a6-31ac-b1fd-29eb5ea561c8 | -5.20212 | -60.04919 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55a04387-df88-3a9b-a5af-375f82d04ed4 | -5.55325 | -60.23503 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e70c058e-5e77-35fb-a6f0-b110f364bcf1 | -5.46635 | -60.06263 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33dba380-8add-374d-a1b7-f5f694fe8932 | -6.19157 | -55.27894 | 2026-09-03 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1603288-ef11-3c74-9ce5-28dfa08b5bb3 | -3.23226 | -61.21616 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8af5d3ca-69bb-3de4-826d-a85cc69d6fd5 | -6.32352 | -56.05081 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2830722e-e510-3ea1-a7ca-9c36d380c32f | -3.36454 | -59.49921 | 2026-09-03 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d92bf32-3bec-3d36-a29b-88bf92f014f8 | -3.834 | -59.39729 | 2026-09-03 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53d90f15-0c45-32a2-a698-bbca2bdc5fbf | -6.68092 | -58.76348 | 2026-09-03 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16fa2181-df13-30e6-a8de-57660bdbb94c | -6.68029 | -58.76797 | 2026-09-03 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 541d2207-6424-35a4-8d16-2b018a010fd6 | -6.75564 | -59.44098 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad80045d-5d54-3736-8013-acd6586c91ce | -3.40746 | -61.31895 | 2026-09-03 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 01a9d288-9c1f-399a-99b3-beee395944a1 | -3.12113 | -61.23217 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9ab4ed6-4831-3ed0-bb5c-a16e41491701 | -4.97586 | -55.84893 | 2026-09-03 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50df94d8-c6e8-3c44-9e36-c3902e45a3fa | -1.48362 | -55.54324 | 2026-09-03 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 405ca0e4-4b10-3e1a-97da-b28daad97a40 | -6.31361 | -56.04238 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d5193819-86f9-3391-ac13-22ebc1d49cd1 | -6.84653 | -59.34327 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8096b7a-b894-36b5-be3d-342f28f41593 | -6.67806 | -59.94397 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4525c8f4-de76-37aa-aadc-ac5cccd660fa | -6.77113 | -59.43845 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f09afd2f-67df-3914-a6cd-c8e686c2a384 | -4.69334 | -56.0616 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79570aab-e1ad-3593-a133-3deefda92aa7 | -4.38152 | -59.93897 | 2026-09-03 05:42:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54233a24-85bf-3bed-936d-dde546d92830 | -6.52857 | -55.10632 | 2026-09-03 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 806cc193-e0e8-35b5-a2da-4cb39dfeb351 | -6.69059 | -59.94572 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ccd1182b-1aae-36e9-ada7-2d6488b42964 | -6.78519 | -59.4201 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b55db5eb-2aa2-3718-9ddf-c76ba4f66138 | -5.92585 | -60.19429 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ebaabe01-0af8-37f5-80aa-22c50f43a3ce | -3.6362 | -60.5481 | 2026-09-03 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3c22988b-1429-345d-b66e-f5cdd24400c9 | -3.36918 | -59.49619 | 2026-09-03 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b204cfb4-95fe-354c-b1cd-36b290cc2e16 | -6.87695 | -56.50573 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 221b8f3c-17ca-398e-b365-154d2705942c | -3.14539 | -60.64259 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf77d0b6-f5d1-38a9-a5e2-097696220b36 | -6.83569 | -58.9699 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 496d2a25-5e3f-32f5-bbc4-b26aa4ac1c40 | -6.14508 | -55.66669 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e625aa37-2cdc-3e3d-9f0e-7db220583224 | -5.20617 | -60.04982 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a92f70ea-76dc-33f1-8466-28fb170d8223 | -5.57028 | -60.1761 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12920194-eadb-3a08-bf56-6c58a8a2326d | -6.76918 | -59.43894 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ffe8a18-4ea2-3d9e-a25b-88708c04d1b8 | -3.44991 | -56.32095 | 2026-09-03 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 775c4774-a160-3e71-911f-7c47dc1fb53f | -3.02659 | -61.48628 | 2026-09-03 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3ede9c2-fda1-341e-83dc-b0b27ed3f086 | -6.69791 | -58.96771 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83841f01-24ea-303c-bb64-cf885695fd76 | -6.31267 | -56.04928 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 2a365dc7-4afe-3564-b05d-d6e7e8ee7d46 | -3.62039 | -60.57491 | 2026-09-03 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60db126b-a081-30df-b15d-22cc1904bb41 | -6.81492 | -58.99992 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf64016a-278e-3ea2-b82f-e3fd4026b007 | -5.59158 | -61.47817 | 2026-09-03 05:42:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c843ce9-d480-3c07-a786-ca6c0915afa9 | -6.30819 | -56.04162 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7d6a8f72-8ef3-365c-bc20-ff1aeb0231be | -3.07995 | -61.18176 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d99e7edc-3a91-34b7-8dc4-994bca2d6794 | -3.11672 | -61.18734 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a16008c5-7ed0-39e1-8b6d-33e8a8682abf | -3.32491 | -59.45568 | 2026-09-03 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8a0f625-f85e-30d3-aa09-6c4fdd790908 | -1.50941 | -54.9593 | 2026-09-03 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fdbc1b6-7213-393d-a18b-73b57ab19ca7 | -3.20219 | -61.216 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e024edba-ea49-3bea-9bde-cdc2a2d87d3b | -6.6004 | -59.11377 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 590f01e9-2e1c-33ae-829d-2cf74ca88bc4 | -6.31408 | -56.03893 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0cc2bd47-5125-36ae-9cf2-511ec10b8d3f | -5.16481 | -60.27734 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b2b97dd-00e7-3ace-8721-cb8d2462a438 | -6.00065 | -62.50135 | 2026-09-03 05:42:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90a913a4-e55d-3b7f-a674-9e6941be446b | -3.38432 | -59.42351 | 2026-09-03 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 101dfeec-4ba5-366c-ac3a-f0894287add3 | -3.39582 | -61.32156 | 2026-09-03 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ff13982-cd03-337a-ad2c-6228f59c3cae | -6.84278 | -59.33836 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 21110660-d0bc-3bea-8d2b-58698b2c575f | -6.64828 | -59.43587 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b6c18980-3e6e-334d-bb0d-88a55eb17a9c | -6.32258 | -56.0577 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b0c0cc0c-f02c-3a63-bd4b-4d5bbe2194a3 | -6.42185 | -58.30486 | 2026-09-03 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 048d000e-59d0-3b29-8991-bfd20f7d2758 | -6.6219 | -55.25187 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e19a690-4158-3dac-b58b-1b7e00514eff | -5.33015 | -60.1404 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 62066b58-8b88-3610-900e-ca09094c3ea3 | -3.39739 | -59.36479 | 2026-09-03 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79948dfd-2cfc-31c4-8e13-d278b405be2d | -6.36426 | -58.28534 | 2026-09-03 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3058282e-74a5-3dd6-af0c-ecfdea93c6a5 | -6.7395 | -59.64173 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2b31393-c140-3571-aa5d-eaa8da563b38 | -6.83725 | -58.97156 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 89b0974f-5f07-3cb7-b83e-632b24bf7f5c | -6.62817 | -55.24868 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6cfe3f6f-c111-3dd3-997b-53449f2c7c19 | -5.20316 | -60.04206 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a4f330f-5032-3c09-8bb5-74902ef18404 | -6.77733 | -56.42032 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d1c3e3f-2056-3c6a-9d8b-b0a02e9f275d | -6.26059 | -55.4307 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46b22411-01c5-37aa-9967-66b60aebd20e | -4.24487 | -62.24 | 2026-09-03 05:42:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0183996f-870f-3826-9434-836c310c017f | -4.97441 | -55.85921 | 2026-09-03 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98281584-5eba-396a-986b-b9b12563b3e6 | -6.77639 | -56.41573 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89c79a12-9c82-3241-a946-5468f9731a8a | -6.75623 | -59.43686 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c218804-8601-3313-b0cc-048cb4996ca9 | -3.83343 | -59.40105 | 2026-09-03 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 562f6dc4-6c42-380d-b96b-a4b47d1cbed3 | -5.32611 | -60.13978 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e6800065-c814-36bd-94e1-7e0d8100e159 | -5.47095 | -60.05964 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65fb7d87-391e-372c-8c7a-1dd2b0dcb831 | -6.69003 | -59.9495 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README46.md)
