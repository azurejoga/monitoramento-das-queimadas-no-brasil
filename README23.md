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
| 486ac17b-c094-3184-9c29-cc9a5a7bae6c | -19.24189 | -42.19871 | 2026-08-20 03:28:00 | NOAA-21 | IAPU | MINAS GERAIS | Brasil | 3129301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 79efbb32-7aa0-398b-9cf7-f682619bd726 | -20.28055 | -42.87786 | 2026-08-20 03:28:00 | NOAA-21 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 52fafa41-bad4-397c-8ab7-dca7fd6ae4bb | -18.17944 | -44.70762 | 2026-08-20 03:28:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 678a75ab-6116-305a-91c4-c0f2f4c50bc8 | -17.33508 | -43.62782 | 2026-08-20 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 50.0 |
| ca456229-0e38-32cb-8cf4-b1cb1e90899e | -22.70203 | -43.36378 | 2026-08-20 03:28:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6189b332-fb96-35bf-a972-b26d8a7cbc92 | -17.94257 | -44.40818 | 2026-08-20 03:28:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 317f579d-3594-3f52-a86d-3cb7ffe8a234 | -21.61768 | -49.01702 | 2026-08-20 03:28:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 136901b6-c0d5-39e2-87a8-751d914ff54e | -17.93175 | -44.43023 | 2026-08-20 03:28:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c87b34d-e476-3c32-9382-00f50ea63e3e | -18.17859 | -44.71154 | 2026-08-20 03:28:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3ea5aa21-2554-3e39-845c-faa3d0677d8f | -17.95573 | -41.93554 | 2026-08-20 03:28:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 60d15056-e8cd-36a3-8cf1-cf06ba5108c9 | -19.65786 | -45.9056 | 2026-08-20 03:28:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 79c935ac-9e48-34c7-bf52-a806f439bae4 | -21.44799 | -48.51851 | 2026-08-20 03:28:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b8e2818-4b97-3ad7-b985-946013361d29 | -21.71288 | -47.1464 | 2026-08-20 03:28:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7dd8f89f-eff2-3968-9315-845f48f70e24 | -17.33036 | -43.6223 | 2026-08-20 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 50.0 |
| e4c7ef17-2b0f-32da-925c-da5d1d047e8d | -18.04067 | -44.61845 | 2026-08-20 03:28:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 0842da1a-cf7c-3097-86bd-f4f03f00a323 | -20.29093 | -46.45794 | 2026-08-20 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c4256aa8-1e36-3d24-a432-cecc79c5ab8c | -21.14083 | -43.90855 | 2026-08-20 03:28:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| cdbb3388-4e0e-3eaf-801f-60d38dbef292 | -17.33129 | -43.6309 | 2026-08-20 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 3312738f-8467-31ae-927e-67181c172e2f | -17.33594 | -43.6237 | 2026-08-20 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 50.0 |
| dca14e53-7057-3531-b5b9-bf520138dada | -21.86975 | -46.5723 | 2026-08-20 03:28:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 2a7a3026-8c08-315f-8ddd-36886b123c7a | -17.94193 | -44.40609 | 2026-08-20 03:28:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de42dbf2-77d2-3bd0-ac3e-d66d84811a1c | -18.03289 | -44.62569 | 2026-08-20 03:28:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a11de936-58ca-3038-a30b-e9fdc8ab1c95 | -20.56394 | -47.36213 | 2026-08-20 03:28:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2ebd08a-dc9d-39c4-96ce-47d850ae6ff5 | -17.92991 | -44.43274 | 2026-08-20 03:28:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47e7b7df-b5cc-3b29-8f1c-a6a78c8e3d95 | -17.3387 | -43.62388 | 2026-08-20 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 9c2af240-0f39-31c4-a0e6-fab4335f7e71 | -17.33311 | -43.6225 | 2026-08-20 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 48.8 |
| b9b9b7f3-a11a-385e-bce8-b43eb566f56e | -21.71427 | -47.14066 | 2026-08-20 03:28:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0c0291d3-3f72-3774-83f4-b168280a19b1 | -21.11031 | -45.61382 | 2026-08-20 03:28:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ddf4dcad-73f1-3d5a-b489-0bedb41c12b9 | -17.33421 | -43.63201 | 2026-08-20 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 4d7b6fc9-f276-35f4-8c27-63e0040b5c0c | -20.35074 | -41.55141 | 2026-08-20 03:28:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 876cc101-c045-397f-ab05-5f8e257b2ef1 | -18.03384 | -44.62138 | 2026-08-20 03:28:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 36ad2b6a-b6c7-30d6-8ebc-8b61e1bbf6df | -20.26174 | -46.74297 | 2026-08-20 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c9705605-3180-3f23-b403-b444e422dafc | -20.28122 | -42.87473 | 2026-08-20 03:28:00 | NOAA-21 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9b758830-2936-3a72-a876-a0aa967f1604 | -18.8525 | -47.1439 | 2026-08-20 03:28:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b5b3663-a25e-3592-bf88-ae5c493f53f3 | -20.26172 | -46.74883 | 2026-08-20 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e748b16e-a5dd-353c-82fd-439a21a6f383 | -17.33783 | -43.62791 | 2026-08-20 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 002c084f-b96c-3d86-a217-7b284e2dc566 | -19.43657 | -42.518 | 2026-08-20 03:28:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9b39c394-ad69-3300-badd-e4e4bf263b45 | -18.87988 | -41.09348 | 2026-08-20 03:28:00 | NOAA-21 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| 29970c40-10e5-326f-a27c-d8435ef74721 | -18.03972 | -44.62273 | 2026-08-20 03:28:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 2323759b-944a-36ff-ad16-5c7499461305 | -17.93571 | -42.8015 | 2026-08-20 03:28:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 652ed773-5fe5-3336-a748-f88546dc53c4 | -21.11138 | -45.60915 | 2026-08-20 03:28:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bfdbc794-5681-355e-9aac-e32483462912 | -20.96684 | -44.12543 | 2026-08-20 03:28:00 | NOAA-21 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5b29156d-a962-3fd1-a38e-450d45730b64 | -20.25993 | -46.75082 | 2026-08-20 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3db3fb06-e30d-3bf7-b3b4-5d22d5d17026 | -19.71558 | -46.22214 | 2026-08-20 03:28:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b424ac81-3e61-36f8-afe5-21500512bc62 | -17.33693 | -43.63206 | 2026-08-20 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 37.2 |
| a025850e-d78d-3845-aaf2-c28825a990fe | -17.32858 | -43.63078 | 2026-08-20 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 8a552765-f653-3570-89fb-92d82b9edc7f | -18.03479 | -44.61707 | 2026-08-20 03:28:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 7188f611-7029-34cd-aefa-ca918aa9c725 | -21.61588 | -49.02398 | 2026-08-20 03:28:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cf97fba-7306-39b1-8c9e-b328d79973da | -19.65852 | -45.90897 | 2026-08-20 03:28:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 182c46af-33ed-3d8b-a262-2f21c917aaf4 | -18.84575 | -47.14257 | 2026-08-20 03:28:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 810a00fb-a8ab-3916-8d57-e35ec1797335 | -21.87705 | -46.56879 | 2026-08-20 03:28:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 315e6714-0831-3289-a5bc-36c8541e982e | -6.6938 | -58.942 | 2026-08-20 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 9c5fc8d6-54e5-35aa-8570-a00d7f2214cf | -7.6118 | -45.1571 | 2026-08-20 03:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 4cd13f68-7d70-373a-a38e-8f1b2aa43093 | -9.2071 | -59.771 | 2026-08-20 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 92a91219-44ed-35d7-bfb3-bb0d07c2f039 | -10.3897 | -61.2118 | 2026-08-20 03:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 92e3f61d-c7ec-3d6c-ad4e-c17dac065bd1 | -8.654 | -54.6505 | 2026-08-20 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 97e71cc9-f0e6-3b13-8c1c-9eae2f85b51b | -8.6727 | -54.6492 | 2026-08-20 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 93e9aac3-be5f-3377-a6fd-710046ef3390 | -9.4256 | -60.4353 | 2026-08-20 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| a2d8070e-a862-3ff9-bbcc-35ca658d8827 | -7.5927 | -45.1817 | 2026-08-20 03:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 80980526-d540-302e-8c7c-1a19a79f4150 | -7.593 | -45.1589 | 2026-08-20 03:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 2f28b3bc-acc7-3186-afc3-1d16462af73a | -7.36 | -45.8361 | 2026-08-20 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| e7db8cf3-060e-3ed4-8884-0b0f8323d862 | -9.12 | -61.6011 | 2026-08-20 03:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 4c0a2a2d-5ac4-33ca-a234-1c75f971c62e | -7.6115 | -45.1799 | 2026-08-20 03:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 9ba070eb-1b3d-3d5c-97a2-a30914b269ee | -11.2189 | -55.0585 | 2026-08-20 03:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 3032f26f-fa78-36c5-a62d-18e1ce7fbabf | -9.4257 | -60.416 | 2026-08-20 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| cd281f65-999a-3dd5-b828-176a3879d2e2 | -7.3603 | -45.8136 | 2026-08-20 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 5cb2bfe6-6fd5-3e27-9205-8960e9a6d37e | -7.36 | -45.8361 | 2026-08-20 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| c8af8174-e049-3228-91c6-734302a63e15 | -9.2071 | -59.771 | 2026-08-20 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| a609aa5b-2051-3d1b-af63-a3bb9a0290c5 | -7.6118 | -45.1571 | 2026-08-20 03:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 6623eb05-34c3-3b48-b796-2a4ed5dcecfc | -8.6727 | -54.6492 | 2026-08-20 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 8e093208-03c8-3aa9-baba-e4da800babc0 | -9.4257 | -60.416 | 2026-08-20 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 9e627fc5-6df5-3d0b-8923-dca32aa7d06e | -7.3603 | -45.8136 | 2026-08-20 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| b681d0ea-0f4f-3a53-a171-814ebb7f858d | -11.2189 | -55.0585 | 2026-08-20 03:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 08b2374e-8512-3265-b531-94dc23bfce65 | -7.9751 | -44.6648 | 2026-08-20 03:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 28cce054-e7bf-3a31-871f-c9ee5f566658 | -9.4256 | -60.4353 | 2026-08-20 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 71b28078-12df-3b40-bd13-2c965abb38f5 | -8.654 | -54.6505 | 2026-08-20 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| c979bb5a-e022-32cf-8e31-65ce181a8dbf | -7.6118 | -45.1571 | 2026-08-20 03:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 4da88f1a-ef8c-396b-bcab-ea9592d5e70e | -9.4256 | -60.4353 | 2026-08-20 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 6e098067-9745-380a-9f05-a84fae8b2d2d | -9.2071 | -59.771 | 2026-08-20 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| f2debdf9-4c93-323a-96f6-0c0ab078bc5e | -7.3603 | -45.8136 | 2026-08-20 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| c75455d6-c9d5-3406-84fc-596e1f5978d2 | -7.5927 | -45.1817 | 2026-08-20 03:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 4dcff793-5ac2-39af-9f4a-f661910f2036 | -9.12 | -61.6011 | 2026-08-20 03:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 78d5328b-ebae-3ce6-8e5b-6cae459e4f49 | -10.3897 | -61.2118 | 2026-08-20 03:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 35c295f2-7b2c-3844-8a87-5e220e1243e6 | -7.6115 | -45.1799 | 2026-08-20 03:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 9bb751be-306f-3173-8ce1-a8d6e6b87558 | -8.6727 | -54.6492 | 2026-08-20 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| c4da7cb6-77cb-3d98-89d1-95862f6cfb35 | -2.11639 | -47.1133 | 2026-08-20 03:57:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b75243a8-927e-3f7c-844c-ffbbc57a8a40 | -3.02865 | -41.17002 | 2026-08-20 03:57:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3f2982ff-a8f0-3f01-9293-95fac03415f5 | -0.98141 | -47.50261 | 2026-08-20 03:57:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6edf7a19-4966-3b79-89cf-ae35fd682635 | -2.04777 | -48.03919 | 2026-08-20 03:57:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0dc93f47-e0ea-3388-afe9-cd631cb93a08 | -3.34218 | -39.33044 | 2026-08-20 03:57:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 61636f0a-8a1e-3d1d-ab55-581e15cdeb22 | -2.11561 | -47.11799 | 2026-08-20 03:57:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49c86eef-1701-3ca2-a0fc-9ce17d71683a | -7.6118 | -45.1571 | 2026-08-20 04:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| ba9c440a-8b7b-3a0a-9af2-d3f3d2e8797b | -7.6115 | -45.1799 | 2026-08-20 04:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 86206d09-ce3f-3b97-b398-8e274c62392a | -10.3897 | -61.2118 | 2026-08-20 04:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 9e174a62-3ca6-301a-8aaa-2e5f2b2523e0 | -7.5927 | -45.1817 | 2026-08-20 04:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| c3504c40-62e9-349f-91f8-73cf80905bed | -8.6727 | -54.6492 | 2026-08-20 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 2c79e027-e860-38f1-9ef1-60f60632927f | -8.654 | -54.6505 | 2026-08-20 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 918bd226-4ab4-3d50-8e15-5ab0a4cedaf1 | -11.2189 | -55.0585 | 2026-08-20 04:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 3b34254f-fc9b-3370-bd11-1fa3353a4978 | -3.47641 | -47.70145 | 2026-08-20 04:00:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f1d119c-a27b-36c8-b85a-c118783371b1 | -6.29481 | -43.64748 | 2026-08-20 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README24.md)
